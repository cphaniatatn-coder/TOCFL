"""Buat audio Mandarin Taiwan (zh-TW, Microsoft Neural via edge-tts) untuk semua teks yang bisa diputar di app.

- Suara ditentukan oleh pembicara: perempuan → suara perempuan, laki-laki → suara laki-laki.
  Peta pembicara → profil ada di js/media.js (blok SPEAKERS) — satu sumber untuk app & skrip ini.
- Nama file = hash cyrb53 dari "PROFIL|teks" (base36), dihitung sama persis di js/media.js,
  jadi app tidak perlu memuat daftar audio apa pun sebelum bisa memutar.
- Setiap rekaman dipotong heningnya (awal & akhir) supaya langsung berbunyi saat diklik.
- Hanya membuat file yang BELUM ada → aman dijalankan ulang setelah mengedit dialog/soal.

Pemakaian:  py _kerja/buat_audio.py     (butuh internet + `pip install edge-tts imageio-ffmpeg`)
"""
import asyncio, hashlib, json, os, re, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
import edge_tts, imageio_ffmpeg

K = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(K)
OUT = f'{R}/audio/tts'
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
os.makedirs(OUT, exist_ok=True)

# Profil suara (semua zh-TW). Microsoft hanya punya 1 suara laki-laki zh-TW,
# jadi tokoh laki-laki kedua & anak laki-laki dibedakan dengan nada (pitch).
PROFIL = {
    'F1': dict(voice='zh-TW-HsiaoChenNeural'),
    'F2': dict(voice='zh-TW-HsiaoYuNeural'),
    'M1': dict(voice='zh-TW-YunJheNeural'),
    'M2': dict(voice='zh-TW-YunJheNeural', pitch='-8Hz'),
    'K':  dict(voice='zh-TW-YunJheNeural', pitch='+30Hz', rate='+5%'),
}
RATE = '-5%'   # sedikit lebih pelan dari normal, untuk pelajar Band A
js = open(f'{R}/js/media.js', encoding='utf-8').read()
PEMBICARA = json.loads(re.search(r'/\* SPEAKERS \*/\s*const SPEAKERS = (\{.*?\});', js, re.S).group(1))

# --- cyrb53: harus identik dengan js/media.js ---
_M = 0xFFFFFFFF
def _imul(a, b): return (a * b) & _M
def cyrb53(s, seed=0):
    h1, h2 = (0xdeadbeef ^ seed) & _M, (0x41c6ce57 ^ seed) & _M
    b = s.encode('utf-16-le')                      # sama dengan charCodeAt (unit UTF-16)
    for i in range(0, len(b), 2):
        ch = b[i] | (b[i + 1] << 8)
        h1 = _imul(h1 ^ ch, 2654435761); h2 = _imul(h2 ^ ch, 1597334677)
    h1 = _imul(h1 ^ (h1 >> 16), 2246822507); h1 ^= _imul(h2 ^ (h2 >> 13), 3266489909)
    h2 = _imul(h2 ^ (h2 >> 16), 2246822507); h2 ^= _imul(h1 ^ (h1 >> 13), 3266489909)
    return 4294967296 * (2097151 & h2) + h1
def nama(kunci):
    n, d, o = cyrb53(kunci), '0123456789abcdefghijklmnopqrstuvwxyz', ''
    while n: n, r = divmod(n, 36); o = d[r] + o
    return o or '0'


def narator(text):
    """Kalimat tanpa pembicara (soal 聽力 Part 1/2, judul, contoh): selang-seling suara perempuan/laki-laki, tetap per teks."""
    return 'F1' if int(hashlib.md5(text.encode()).hexdigest(), 16) % 2 == 0 else 'M1'


def kumpulkan():
    job = {}   # kunci ("PROFIL|teks", sama dengan yang dihitung app) → (profil suara, teks)
    tak_dikenal = set()

    def tambah(kunci_prof, prof, text):
        text = (text or '').strip()
        if text:
            job[f'{kunci_prof}|{text}'] = (prof, text)

    def baris(lines):
        for l in lines:
            prof = PEMBICARA.get(l['sp'])
            if not prof:
                tak_dikenal.add(l['sp']); prof = 'F1'
            tambah(prof, prof, l['zh'])

    def soal(t):
        if t.get('lines'):
            baris(t['lines'])
        if t.get('audio'):
            tambah('N', narator(t['audio']), t['audio'])

    for v in (1, 2, 3):
        for m in json.load(open(f'{R}/data/modul_vol{v}.json', encoding='utf-8'))['modules']:
            tambah('N', narator(m['title']), m['title'])
            for d in m['dialogs']:
                baris(d['lines'])
            for t in m['tasks']:
                soal(t)
            for g in m['grammar']:
                for e in g['examples']:
                    tambah('N', narator(e['zh']), e['zh'])
            for r in m.get('recycle', []):
                tambah('N', narator(r['zh']), r['zh'])
            for e in m['vocab']['core'] + m['vocab']['supplement']:
                tambah('W', 'F1', e['w'])          # kosakata: satu suara yang konsisten
    if os.path.exists(f'{R}/data/bank_soal.json'):
        for ts in json.load(open(f'{R}/data/bank_soal.json', encoding='utf-8')).values():
            for t in ts:
                soal(t)
    return job, tak_dikenal


def potong(src, dst):
    """Buang hening di awal (sisakan 30 ms) & akhir (sisakan 150 ms), simpan mp3 mono 24 kHz."""
    f = ('silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.03,areverse,'
         'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.15,areverse')
    subprocess.run([FFMPEG, '-v', 'error', '-y', '-i', src, '-af', f, '-ac', '1', '-ar', '24000',
                    '-c:a', 'libmp3lame', '-b:a', '48k', dst + '.part.mp3'], check=True)
    os.replace(dst + '.part.mp3', dst)


async def satu(sem, pool, prof, text, path, gagal):
    p = PROFIL[prof]
    async with sem:
        for coba in range(4):
            try:
                tmp = os.path.join(tempfile.gettempdir(), os.path.basename(path) + '.raw.mp3')
                await edge_tts.Communicate(text, p['voice'], rate=p.get('rate', RATE),
                                           pitch=p.get('pitch', '+0Hz')).save(tmp)
                await asyncio.get_running_loop().run_in_executor(pool, potong, tmp, path)
                os.remove(tmp)
                return
            except Exception:  # jaringan/limit: coba lagi pelan-pelan
                await asyncio.sleep(2 + coba * 3)
        gagal.append(text)


async def main():
    job, tak = kumpulkan()
    if tak:
        print('⚠ pembicara tanpa profil (memakai F1) — tambahkan ke SPEAKERS di js/media.js:', ' '.join(sorted(tak)))
    target = {nama(k): v for k, v in job.items()}
    if len(target) != len(job):
        sys.exit('Tabrakan hash nama file — ganti seed cyrb53 di media.js & skrip ini.')
    todo = [(prof, text, f'{OUT}/{n}.mp3') for n, (prof, text) in target.items() if not os.path.exists(f'{OUT}/{n}.mp3')]
    print(f'{len(job)} teks; belum ada rekaman: {len(todo)}')
    sem, gagal = asyncio.Semaphore(8), []
    with ThreadPoolExecutor(6) as pool:
        for k in range(0, len(todo), 200):
            await asyncio.gather(*(satu(sem, pool, *x, gagal) for x in todo[k:k + 200]))
            print(f'  … {min(k + 200, len(todo))}/{len(todo)}', flush=True)
    sisa = [f for f in os.listdir(OUT) if f.endswith('.mp3') and f[:-4] not in target]
    for f in sisa:                                     # rekaman untuk teks yang sudah tidak ada
        os.remove(f'{OUT}/{f}')
    print(f'Selesai. gagal: {len(gagal)}; rekaman lama dihapus: {len(sisa)}')
    if gagal:
        print('   ', ' | '.join(gagal[:20]))


if __name__ == '__main__':
    asyncio.run(main())
