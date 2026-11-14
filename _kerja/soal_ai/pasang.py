"""Pasang draf soal hasil tulis ulang ke file sumber: py _kerja/soal_ai/pasang.py A02

- hasil/<kode>-latihan.json (12, urut KOMPOSISI_LATIHAN) → soal latihan modul. Jumlah soal di _kerja/isi dipertahankan
  (diisi dulu dengan soal non-listen_pic: 聽P2, 聽P3, 閱P2/P4/P5 …), sisanya ke _kerja/soal/vol1.json — supaya
  ID gambar listen_pic (<kode>-1, -2, …, urut isi → soal → bank) tetap sesuai.
- hasil/<kode>-tes.json (10) → _kerja/bank/vol1.json.
Kolom pola_pengecoh dibuang (tetap tersimpan di hasil/). Sesudahnya: bangun_modul → bangun_bank → terjemah → buat_audio.
"""
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.dirname(HERE)
sys.path.insert(0, K)
from seimbang_jawaban import simpan_aman   # noqa: E402

bersih = lambda t: {k: v for k, v in t.items() if k != 'pola_pengecoh'}


def berkas_isi(kode):
    for f in sorted(glob.glob(f'{K}/isi/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        if 'modules' in d:
            for m in d['modules']:
                if m['code'] == kode:
                    return f, d, m
        elif os.path.basename(f)[:-5] == kode:
            return f, d, d
    sys.exit(f'{kode} tidak ada di _kerja/isi')


def nomori_gambar(kode, urut):
    """ID gambar listen_pic = posisi (<kode>-n, urut isi → soal → bank; lihat gambar_soal.py). Bila draf memakai
    ID lain, kunci adegan di adegan_vol<N>.py diganti namanya supaya cocok, lalu picture.img disesuaikan."""
    v = {'A': 1, 'B': 2, 'C': 3}[kode[0]]
    peta, n = {}, 0
    for t in urut:
        if t['type'] == 'listen_pic':
            n += 1
            lama = t['picture'].get('img')
            if lama and lama != f'{kode}-{n}':
                peta[lama] = f'{kode}-{n}'
            t['picture']['img'] = f'{kode}-{n}'
    if not peta:
        return
    pa = f'{K}/adegan_vol{v}.py'
    teks = open(pa, encoding='utf-8').read()
    for a in peta:
        teks = teks.replace(f"A['{a}']", f"A['__tmp_{a}']")
    for a, b in peta.items():
        teks = teks.replace(f"A['__tmp_{a}']", f"A['{b}']")
    open(pa, 'w', encoding='utf-8', newline='').write(teks)
    print('  gambar dinomori ulang:', ', '.join(f'{a}→{b}' for a, b in peta.items()))


def sinkron_draf(kode, urut):
    """Samakan picture.img listen_pic di hasil/<kode>-latihan.json & -tes.json dengan ID posisi, supaya pemasangan
    ulang tidak menomori gambar dua kali. Urutan listen_pic di draf (latihan lalu tes) = urutan isi → soal → bank."""
    ids = [t['picture']['img'] for t in urut if t['type'] == 'listen_pic']
    L = json.load(open(f'{HERE}/hasil/{kode}-latihan.json', encoding='utf-8'))
    T = json.load(open(f'{HERE}/hasil/{kode}-tes.json', encoding='utf-8'))
    for t, i in zip([t for t in L + T if t['type'] == 'listen_pic'], ids):
        t['picture']['img'] = i
    json.dump(L, open(f'{HERE}/hasil/{kode}-latihan.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(T, open(f'{HERE}/hasil/{kode}-tes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def main(kode):
    v = {'A': 1, 'B': 2, 'C': 3}[kode[0]]
    L = [bersih(t) for t in json.load(open(f'{HERE}/hasil/{kode}-latihan.json', encoding='utf-8'))]
    T = [bersih(t) for t in json.load(open(f'{HERE}/hasil/{kode}-tes.json', encoding='utf-8'))]
    f, d, m = berkas_isi(kode)
    n = len(m.get('tasks', []))
    bukan_pic = [t for t in L if t['type'] != 'listen_pic']
    isi = bukan_pic[:n]
    sisa = [t for t in L if not any(t is x for x in isi)]
    nomori_gambar(kode, isi + sisa + T)
    sinkron_draf(kode, isi + sisa + T)
    m['tasks'] = isi
    simpan_aman(f, d)
    for sub, isi_baru in (('soal', sisa), ('bank', T)):
        cocok = [p for p in sorted(glob.glob(f'{K}/{sub}/vol{v}*.json')) if kode in json.load(open(p, encoding='utf-8'))]
        p = cocok[0]
        dd = json.load(open(p, encoding='utf-8'))
        dd[kode] = isi_baru
        simpan_aman(p, dd)
    print(f'{kode}: isi {len(isi)} + soal {len(sisa)} + bank {len(T)} dipasang')


if __name__ == '__main__':
    for k in sys.argv[1:]:
        main(k)
