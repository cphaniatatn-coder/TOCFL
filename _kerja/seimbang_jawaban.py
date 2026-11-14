"""Seimbangkan posisi jawaban benar di SEMUA soal (latihan modul + Tes Bab) tanpa mengubah isi soal.

Cara: per paket (12 soal latihan satu 單元, atau 10 soal Tes Bab satu 單元) tiap soal diberi posisi target
dengan cara rakus: huruf yang paling jarang dipakai di paket itu (soal 4 opsi boleh D), seri → pertahankan posisi
lama (supaya perubahan & rekaman audio baru seminimal mungkin), lalu acak dengan benih tetap (hasil bisa diulang).
Opsi benar DITUKAR dengan opsi di posisi target; huruf yang dirujuk di "why" (A/B/C/D berdiri sendiri) ikut
ditukar, begitu pula terjemahan English-nya di terjemahan_en.json. Soal cloze (閱讀 Part 4) tidak diubah.

Pemakaian:  py _kerja/seimbang_jawaban.py          (pratinjau: sebaran sebelum/sesudah + soal yang perlu dicek)
            py _kerja/seimbang_jawaban.py tulis    (tulis ke _kerja/isi, _kerja/soal, _kerja/bank, terjemahan_en.json)
Sesudah menulis: bangun_modul → bangun_bank → terjemah → buat_audio (rekaman 聽力 Part 1 berubah karena huruf dibacakan).
"""
import collections, glob, json, os, random, re, sys
K = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, K)
from simpan_json import simpan   # noqa: E402
sys.stdout.reconfigure(encoding='utf-8')
HURUF = re.compile(r'(?<![A-Za-z0-9])([A-D])(?![A-Za-z0-9])')


def tukar_huruf(s, a, b):
    """Tukar huruf pilihan a<->b (indeks) di teks penjelasan."""
    if a == b or not s:
        return s
    A, B = 'ABCD'[a], 'ABCD'[b]
    return HURUF.sub(lambda m: B if m.group(1) == A else A if m.group(1) == B else m.group(1), s)


def simpan_aman(p, baru):
    """simpan_json.simpan; bila format file campuran (isi/A01, B01, C01: dialog ringkas + soal berindentasi),
    ganti hanya objek soal yang berubah, di tempatnya, dengan indentasi aslinya."""
    try:
        return simpan(p, baru)
    except ValueError:
        pass
    from simpan_json import _akhir_objek, _soal_urut
    teks = open(p, encoding='utf-8').read()
    lama = json.loads(teks)
    lama_s, baru_s = _soal_urut(lama), _soal_urut(baru)
    rentang, i = [], 0
    while True:
        i = teks.find('{', i)
        if i < 0:
            break
        if re.match(r'\{\s*"type":\s*"', teks[i:i + 40]):
            e = _akhir_objek(teks, i)
            rentang.append((i, e)); i = e
        else:
            i += 1
    if len(rentang) != len(lama_s) or any(json.loads(teks[a:b]) != o for (a, b), o in zip(rentang, lama_s)):
        raise ValueError(f'{p}: objek soal tidak bisa dipetakan — tidak ditulis')
    out, akhir = [], 0
    for (a, b), o, n in zip(rentang, lama_s, baru_s):
        out.append(teks[akhir:a])
        if o == n:
            out.append(teks[a:b])
        else:
            kol = a - (teks.rfind('\n', 0, a) + 1)
            out.append(json.dumps(n, ensure_ascii=False, indent=1).replace('\n', '\n' + ' ' * kol))
        akhir = b
    out.append(teks[akhir:])
    hasil = ''.join(out)
    if json.loads(hasil) != baru:
        raise ValueError(f'{p}: hasil tidak sama dengan data baru — tidak ditulis')
    open(p, 'w', encoding='utf-8', newline='').write(hasil)
    return True


def paket():
    """Kembalikan daftar (file, data, [(kode, jenis, [soal...])]) — soal adalah objek di dalam data (diubah di tempat)."""
    out = []
    for f in sorted(glob.glob(f'{K}/isi/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        mods = d['modules'] if 'modules' in d else [dict(d, code=os.path.basename(f)[:-5])]
        src = d['modules'] if 'modules' in d else [d]
        out.append((f, d, [(m['code'], 'latihan-isi', s.get('tasks', [])) for m, s in zip(mods, src)]))
    for sub, jenis in (('soal', 'latihan-soal'), ('bank', 'tes')):
        for f in sorted(glob.glob(f'{K}/{sub}/*.json')):
            d = json.load(open(f, encoding='utf-8'))
            out.append((f, d, [(c, jenis, ts) for c, ts in d.items()]))
    return out


def main():
    tulis = len(sys.argv) > 1 and sys.argv[1] == 'tulis'
    berkas = paket()
    # gabungkan latihan-isi + latihan-soal per 單元 = satu paket latihan (12 soal)
    kelompok = collections.defaultdict(list)
    for f, d, grup in berkas:
        for kode, jenis, ts in grup:
            kelompok[(kode, 'tes' if jenis == 'tes' else 'latihan')] += ts
    kamus_p = f'{K}/terjemahan_en.json'
    kamus = json.load(open(kamus_p, encoding='utf-8'))
    sebelum, sesudah = collections.Counter(), collections.Counter()
    berubah, cek_manual, en_baru, en_hilang = 0, [], {}, 0
    for (kode, jenis), ts in sorted(kelompok.items()):
        rng = random.Random(f'{kode}|{jenis}')
        soal = [t for t in ts if 'answer' in t and t.get('type') != 'cloze' and len(t.get('options', [])) in (3, 4)]
        urut = soal[:]
        rng.shuffle(urut)
        hitung = collections.Counter()
        for t in urut:
            n, lama = len(t['options']), t['answer']
            sebelum[(jenis, 'ABCD'[lama])] += 1
            pilihan = list(range(n))
            minimum = min(hitung[k] for k in pilihan)
            calon = [k for k in pilihan if hitung[k] == minimum]
            target = lama if lama in calon else rng.choice(calon)
            hitung[target] += 1
            sesudah[(jenis, 'ABCD'[target])] += 1
            why = t.get('why', '')
            terpakai = {m.group(1) for m in HURUF.finditer(why)}
            if any('ABCD'.index(h) >= n for h in terpakai):
                cek_manual.append(f'{kode} {jenis}: huruf di why melebihi jumlah opsi — {why[:70]}')
            if target == lama:
                continue
            berubah += 1
            o = t['options']
            o[lama], o[target] = o[target], o[lama]
            t['answer'] = target
            t['why'] = tukar_huruf(why, lama, target)
            if why in kamus and isinstance(kamus[why], str):
                en_baru[t['why']] = tukar_huruf(kamus[why], lama, target)
            elif why.strip():
                en_hilang += 1
    print(f'Soal diubah urutannya: {berubah}')
    for jenis in ('latihan', 'tes'):
        s0 = {h: sebelum[(jenis, h)] for h in 'ABCD'}
        s1 = {h: sesudah[(jenis, h)] for h in 'ABCD'}
        tot = sum(s0.values())
        print(f'{jenis:8s} sebelum: ' + ' '.join(f'{h} {100 * v / tot:.0f}%' for h, v in s0.items())
              + ' | sesudah: ' + ' '.join(f'{h} {100 * v / tot:.0f}%' for h, v in s1.items()))
    print(f'Terjemahan English disesuaikan: {len(en_baru)} | tanpa terjemahan lama (akan masuk terjemahan_kurang): {en_hilang}')
    if cek_manual:
        print(f'Perlu dicek manual ({len(cek_manual)}):')
        for x in cek_manual[:20]:
            print('  ', x)
    if not tulis:
        print('\n(pratinjau — jalankan dengan argumen "tulis" untuk menyimpan)')
        return
    # bila gagal di tengah jalan: semua file sumber terlacak git → pulihkan dengan git checkout
    n = sum(simpan_aman(f, d) for f, d, _ in berkas)
    kamus.update(en_baru)
    simpan_kamus = json.dumps(kamus, ensure_ascii=False, indent=1)
    open(kamus_p, 'w', encoding='utf-8').write(simpan_kamus + '\n')
    print(f'{n} file sumber ditulis; terjemahan_en.json diperbarui.')


if __name__ == '__main__':
    main()
