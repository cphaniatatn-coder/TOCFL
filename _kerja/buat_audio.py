"""Buat audio Mandarin Taiwan (zh-TW, Microsoft Neural via edge-tts) untuk semua teks yang bisa diputar di app.

- Suara ditentukan oleh pembicara: perempuan → suara perempuan, laki-laki → suara laki-laki.
- Hasil: audio/tts/<id>.mp3 + data/audio.json (peta "PROFIL|teks" → id, dan peta pembicara → profil).
- Hanya membuat file yang BELUM ada, jadi aman dijalankan ulang setelah mengedit dialog/soal.

Pemakaian:  py _kerja/buat_audio.py            (butuh internet)
"""
import asyncio, hashlib, json, os, sys
import edge_tts

K = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(K)
OUT = f'{R}/audio/tts'
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
PEMBICARA = {
    # perempuan
    '李美美': 'F1', '小姐': 'F1', '店員': 'F1', '老闆娘': 'F1', '護士': 'F1', '陳安安': 'F1', '女': 'F1',
    '安妮': 'F2', '陳老師': 'F2', '媽媽': 'F2', '美美的媽媽': 'F2',
    # laki-laki
    '王大文': 'M1', '王先生': 'M1', '先生': 'M1', '陳先生': 'M1', '司機': 'M1', '男': 'M1',
    '志明': 'M2', '老闆': 'M2', '醫生': 'M2',
    # anak laki-laki
    '小明': 'K', '安妮的弟弟': 'K',
}


def pid(prof, text):
    p = PROFIL[prof]
    return hashlib.sha1(f"{p['voice']}|{p.get('pitch', '')}|{p.get('rate', RATE)}|{text}".encode()).hexdigest()[:12]


def narator(text):
    """Kalimat tanpa pembicara (soal 聽力 Part 1/2, judul, contoh): selang-seling suara perempuan/laki-laki, tetap per teks."""
    return 'F1' if int(hashlib.md5(text.encode()).hexdigest(), 16) % 2 == 0 else 'M1'


def kumpulkan():
    job = {}   # kunci manifest → (profil, teks)
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


async def satu(sem, prof, text, path, gagal):
    p = PROFIL[prof]
    async with sem:
        for coba in range(4):
            try:
                com = edge_tts.Communicate(text, p['voice'], rate=p.get('rate', RATE), pitch=p.get('pitch', '+0Hz'))
                await com.save(path + '.part')
                os.replace(path + '.part', path)
                return
            except Exception as e:  # jaringan/limit: coba lagi pelan-pelan
                await asyncio.sleep(2 + coba * 3)
        gagal.append(text)


async def main():
    job, tak = kumpulkan()
    if tak:
        print('⚠ pembicara tanpa profil (memakai F1):', ' '.join(sorted(tak)))
    manifest = {}
    todo = []
    for kunci, (prof, text) in job.items():
        i = pid(prof, text)
        manifest[kunci] = i
        if not os.path.exists(f'{OUT}/{i}.mp3'):
            todo.append((prof, text, f'{OUT}/{i}.mp3'))
    todo = list({x[2]: x for x in todo}.values())   # satu file per (suara, teks)
    print(f'{len(job)} teks, {len(set(manifest.values()))} file audio, belum dibuat: {len(todo)}')
    sem, gagal = asyncio.Semaphore(8), []
    done = 0
    for k in range(0, len(todo), 200):
        await asyncio.gather(*(satu(sem, *x, gagal) for x in todo[k:k + 200]))
        done += len(todo[k:k + 200]); print(f'  … {done}/{len(todo)}', flush=True)
    for kunci in list(manifest):
        if not os.path.exists(f'{OUT}/{manifest[kunci]}.mp3'):
            del manifest[kunci]
    json.dump({'speakers': PEMBICARA, 'clips': manifest}, open(f'{R}/data/audio.json', 'w', encoding='utf-8'),
              ensure_ascii=False, separators=(',', ':'))
    used = set(manifest.values())
    sisa = [f for f in os.listdir(OUT) if f.endswith('.mp3') and f[:-4] not in used]
    print(f'Selesai. gagal: {len(gagal)}; file tak terpakai (boleh dihapus): {len(sisa)}')
    if gagal: print('   ', ' | '.join(gagal[:20]))


if __name__ == '__main__':
    asyncio.run(main())
