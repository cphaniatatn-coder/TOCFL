"""Buat audio Mandarin Taiwan (zh-TW, Microsoft Neural via edge-tts) untuk semua teks yang bisa diputar di app.

- Suara ditentukan oleh pembicara: perempuan → suara perempuan, laki-laki → suara laki-laki.
  Peta pembicara → profil ada di js/media.js (blok SPEAKERS) — satu sumber untuk app & skrip ini.
- Nama file = hash cyrb53 dari "PROFIL|teks" (base36), dihitung sama persis di js/media.js,
  jadi app tidak perlu memuat daftar audio apa pun sebelum bisa memutar.
- Hening tiap rekaman diratakan: awal 250 ms (bantalan agar suku kata pertama tidak termakan saat perangkat audio
  baru aktif), akhir 150 ms; mp3 64 kbps.
- Teks yang DIUCAPKAN bisa berbeda dari teks yang ditampilkan (_kerja/ucapan.json): homofon untuk kata
  polifon yang dibaca salah oleh TTS, 和 → bacaan Taiwan hàn dalam kalimat, dan kata tanpa homofon
  (得 děi) diucapkan dalam kalimat pembawa lalu dipotong pada batas katanya.
- Hanya membuat file yang belum ada ATAU yang aturannya berubah (suara/kecepatan/nada/teks ucapan) —
  tanda tiap rekaman disimpan di _kerja/audio_versi.json → aman dijalankan ulang setelah mengedit.

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
    # Anak: suara perempuan dengan nada sedikit naik terdengar wajar (seperti rekaman buku ajar);
    # suara laki-laki +30Hz dulu terdengar seperti robot. Di B46 lawan bicaranya HsiaoYu, jadi pakai HsiaoChen.
    'K':  dict(voice='zh-TW-HsiaoChenNeural', pitch='+15Hz', rate='+5%'),
}
RATE = '-5%'
AWAL_MS, BITRATE = 250, '64k'          # hening awal (bantalan) & kualitas mp3
OLAH = f'awal{AWAL_MS}-{BITRATE}'      # ikut tanda rekaman → ubah angka di atas = semua rekaman dibuat ulang   # sedikit lebih pelan dari normal, untuk pelajar Band A
js = open(f'{R}/js/media.js', encoding='utf-8').read()
UCAPAN = json.load(open(f'{K}/ucapan.json', encoding='utf-8'))
VERSI = f'{K}/audio_versi.json'
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


def ucapan(kunci_prof, text):
    """Teks yang benar-benar dikirim ke TTS (+ kata yang dipotong bila memakai kalimat pembawa)."""
    if kunci_prof == 'W':
        if text in UCAPAN['potong']:
            return tuple(UCAPAN['potong'][text])
        return text, None
    text = UCAPAN.get('teks', {}).get(text, text)   # penggantian untuk satu kalimat persis
    for pola, ganti in UCAPAN['kalimat']:
        text = re.sub(pola, ganti, text)
    return text, None


def profil(prof, ambil):
    # kata yang dipotong dari kalimat pembawa diucapkan lebih pelan supaya tidak terdengar terpotong/terburu-buru
    return dict(PROFIL[prof], rate='-25%') if ambil else PROFIL[prof]


def tanda(prof, kunci_prof, text):
    ucap, ambil = ucapan(kunci_prof, text)
    p = profil(prof, ambil)
    return f"{p['voice']}|{p.get('rate', RATE)}|{p.get('pitch', '+0Hz')}|{ucap}|{ambil or ''}|{OLAH}"


def narator(text):
    """Kalimat tanpa pembicara (soal 聽力 Part 1/2, judul, contoh): selang-seling suara perempuan/laki-laki, tetap per teks."""
    return 'F1' if int(hashlib.md5(text.encode()).hexdigest(), 16) % 2 == 0 else 'M1'


def kumpulkan():
    job = {}   # kunci ("PROFIL|teks", sama dengan yang dihitung app) → (profil suara, teks)
    tak_dikenal = set()

    def tambah(kunci_prof, prof, text):
        text = (text or '').strip()
        if text:
            job[f'{kunci_prof}|{text}'] = (prof, kunci_prof, text)

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
        if t.get('type') == 'listen_pic':   # 聽力 Part 1: pertanyaan, lalu "A，…" "B，…" "C，…" (sama dengan Soal.picTexts di app)
            for x in [t['question']] + [f'{"ABC"[i]}，{o}' for i, o in enumerate(t['options'])]:
                tambah('N', narator(x), x)

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
                tambah('W', 'F1', e.get('say') or e['w'])   # kosakata: satu suara yang konsisten; say = teks ucapan polifon
    if os.path.exists(f'{R}/data/bank_soal.json'):
        for ts in json.load(open(f'{R}/data/bank_soal.json', encoding='utf-8')).values():
            for t in ts:
                soal(t)
    mini = f'{K}/mini'   # tes awal/akhir modul mini (uji coba thesis), dirakit oleh buat_mini.py
    for fn in sorted(os.listdir(mini)) if os.path.isdir(mini) else []:
        if fn.startswith('tes_') and fn.endswith('.json'):
            for paket in json.load(open(f'{mini}/{fn}', encoding='utf-8')).values():
                for t in paket:
                    soal(t)
                    if t.get('type') == 'listen_dialog' and t.get('question'):   # 問 dibacakan setelah bunyi bel (studi.js)
                        tambah('N', narator(t['question']), t['question'])
    return job, tak_dikenal


def potong(src, dst, iris=None):
    """Ratakan hening: awal tepat AWAL_MS (bantalan — speaker/Bluetooth/HP butuh ±100–300 ms untuk "bangun";
    tanpa bantalan suku kata pertama ikut termakan), akhir 150 ms. Simpan mp3 mono 24 kHz.
    iris=(mulai, akhir) detik: ambil satu kata saja dari kalimat pembawa (dengan fade pendek)."""
    f = ('silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.02,areverse,'
         'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.15,areverse,'
         f'adelay={AWAL_MS}:all=1,asetpts=N/SR/TB')
    if iris:
        a, b = iris
        f = f'atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={b - a - 0.04:.3f}:d=0.04,' + f
    subprocess.run([FFMPEG, '-v', 'error', '-y', '-i', src, '-af', f, '-ac', '1', '-ar', '24000',
                    '-c:a', 'libmp3lame', '-b:a', BITRATE, dst + '.part.mp3'], check=True)
    os.replace(dst + '.part.mp3', dst)


async def rekam(p, ucap, ambil, tmp):
    """Simpan rekaman ke tmp; bila `ambil` diisi, kembalikan (mulai, akhir) kata itu di kalimat pembawa."""
    c = edge_tts.Communicate(ucap, p['voice'], rate=p.get('rate', RATE), pitch=p.get('pitch', '+0Hz'),
                             boundary='WordBoundary')
    batas = []
    with open(tmp, 'wb') as f:
        async for m in c.stream():
            if m['type'] == 'audio':
                f.write(m['data'])
            elif m['type'] == 'WordBoundary':
                batas.append((m['text'], m['offset'] / 1e7, (m['offset'] + m['duration']) / 1e7))
    if not ambil:
        return None
    i = next(i for i, b in enumerate(batas) if b[0] == ambil)
    akhir = batas[i + 1][1] if i + 1 < len(batas) else batas[i][2] + 0.1
    return max(0, batas[i][1] - 0.02), akhir


async def satu(sem, pool, prof, kunci_prof, text, path, gagal):
    ucap, ambil = ucapan(kunci_prof, text)
    p = profil(prof, ambil)
    async with sem:
        for coba in range(4):
            try:
                tmp = os.path.join(tempfile.gettempdir(), os.path.basename(path) + '.raw.mp3')
                iris = await rekam(p, ucap, ambil, tmp)
                await asyncio.get_running_loop().run_in_executor(pool, potong, tmp, path, iris)
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
    versi = json.load(open(VERSI, encoding='utf-8')) if os.path.exists(VERSI) else {}
    baru = {n: tanda(*v) for n, v in target.items()}
    for n in target:   # rekaman lama tanpa catatan dianggap sudah sesuai aturan sekarang
        if n not in versi and os.path.exists(f'{OUT}/{n}.mp3'):
            versi[n] = baru[n]
    todo = [(*v, f'{OUT}/{n}.mp3') for n, v in target.items()
            if not os.path.exists(f'{OUT}/{n}.mp3') or versi.get(n) != baru[n]]
    print(f'{len(job)} teks; perlu direkam (baru/aturan berubah): {len(todo)}')
    sem, gagal = asyncio.Semaphore(8), []
    with ThreadPoolExecutor(6) as pool:
        for k in range(0, len(todo), 200):
            await asyncio.gather(*(satu(sem, pool, *x, gagal) for x in todo[k:k + 200]))
            print(f'  … {min(k + 200, len(todo))}/{len(todo)}', flush=True)
    gagal_set = set(gagal)   # yang gagal tetap memakai tanda lama → dicoba lagi pada run berikutnya
    versi = {n: (versi.get(n, '') if v[2] in gagal_set else baru[n])
             for n, v in target.items() if os.path.exists(f'{OUT}/{n}.mp3')}
    json.dump(dict(sorted(versi.items())), open(VERSI, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    sisa = [f for f in os.listdir(OUT) if f.endswith('.mp3') and f[:-4] not in target]
    for f in sisa:                                     # rekaman untuk teks yang sudah tidak ada
        os.remove(f'{OUT}/{f}')
    print(f'Selesai. gagal: {len(gagal)}; rekaman lama dihapus: {len(sisa)}')
    if gagal:
        print('   ', ' | '.join(gagal[:20]))


if __name__ == '__main__':
    asyncio.run(main())
