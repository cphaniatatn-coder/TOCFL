"""Ilustrasi 聽力 Part 1 tes awal/akhir modul mini (bergaya buku soal TOCFL, SVG buatan kode).

    py _kerja/mini/gambar_tes.py   → img/soal/T<level><paket>-<no>.svg + lembar periksa _kerja/gambar/periksa_tes.html
                                     (WAJIB dicek visual: detail kunci cocok & tidak ambigu dengan pengecoh)
buat_mini.py memasang gambar ini otomatis (picture.img) bila file-nya ada.
"""
import json, os, sys
K = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); R = os.path.dirname(K)
sys.path.insert(0, K)
from svg_adegan import *

MASAK = {'ka': [(26, 18), (62, 10)]}
A = {}

# ---------- A0 · paket A ----------
A['TA0A-1'] = (lantai() + orang(52, tinggi=168, jenis='pria', baju='h') + orang(122, tinggi=156, jenis='wanita', baju='a')
               + orang(190, tinggi=96, jenis='laki', baju='p') + orang(250, tinggi=92, jenis='gadis', baju='h'))
A['TA0A-2'] = lantai() + meja(120, 130, 170) + buku(108, 130, 40, 26, 'h') + buku(150, 130, 30, 40, 'a') + kursi(250)
A['TA0A-3'] = (lantai() + ranjang(110, 200, 190) + orang(110, tinggi=150, jenis='pria', duduk=150, baju='a', wajah='lelah',
               tangan={'ki': [(-10, -26), (-4, -54)], 'ka': [(10, -26), (4, -54)]}) + weker(245, 80, 34, 7, 30))
A['TA0A-4'] = (lantai() + awan(150, 30, 1.3, 'a') + hujan(150, 56, 250, 70, 13)
               + orang(150, tinggi=140, jenis='pria', baju='h', wajah='sedih', tangan={'ki': [(-12, -8), (-2, -34)], 'ka': [(12, -8), (2, -34)]}))
# ---------- A0 · paket B ----------
A['TA0B-1'] = (lantai() + orang(42, tinggi=166, jenis='pria', baju='h') + orang(102, tinggi=154, jenis='wanita', baju='a')
               + orang(160, tinggi=100, jenis='laki', baju='p') + orang(214, tinggi=92, jenis='gadis', baju='h') + orang(266, tinggi=82, jenis='laki', baju='a'))
A['TA0B-2'] = lantai() + ranjang(150, 200, 220) + sepatu(130, 197, .7) + sepatu(190, 197, .7)
A['TA0B-3'] = (lantai() + ranjang(120, 200, 200) + bulat(40, 128, 13) + muka(40, 128, 13, 'tidur') + jalur('M26 123 q2 -18 16 -18 q12 0 13 14', 'h')
               + teks(78, 104, 'z z', 18, angka=True) + jam_dinding(255, 64, 32, 10, 30) + bulan_bintang(195, 34, .6))
A['TA0B-4'] = (lantai() + matahari(60, 50, 24, 'h') + orang(175, tinggi=160, jenis='pria', baju='p', wajah='lelah', tangan={'ka': [(14, -6), (10, -26)]})
               + keringat(150, 44) + keringat(200, 52) + keringat(155, 90, .8))

# ---------- A1 · paket A ----------
A['TA1A-1'] = lantai() + kompor(190, 130) + api(190, 128, .8) + wajan(190, 112, 1.0) + orang(85, tinggi=160, jenis='pria', baju='a', tangan=MASAK)
A['TA1A-2'] = (lantai() + orang(150, tinggi=150, jenis='wanita', baju='h', wajah='sedih', badan=1.9,
               tangan={'ki': [(-14, 34), (-16, 72)], 'ka': [(14, 34), (16, 72)]}))
A['TA1A-3'] = (teks(80, 30, '臺北', 26) + termometer(80, 44, 15) + teks(128, 150, '15°', 24, angka=True)
               + teks(220, 30, '雅加達', 26) + termometer(220, 44, 32) + matahari(268, 72, 12) + teks(268, 150, '32°', 24, angka=True))
A['TA1A-4'] = (lantai() + menara_bandara(260) + pesawat(140, 120, .75) + orang(60, tinggi=140, jenis='wanita', baju='a', tangan={'ka': [(12, 30), (20, 56)]})
               + koper(88, 200, .55))
# ---------- A1 · paket B ----------
A['TA1B-1'] = lantai() + meja(170, 150, 160) + baskom_cuci(170, 150) + kaos(170, 120, .35, 'a') + orang(85, tinggi=158, jenis='wanita', baju='a', tangan={'ka': [(24, 26), (60, 36)]})
_x = 150   # celana kependekan: kaki terlihat jauh di bawah ujung celana
A['TA1B-2'] = (lantai() + orang(_x, tinggi=170, jenis='pria', baju='a', wajah='sedih')
               + bentuk((_x - 15, 114), (_x + 15, 114), (_x + 17, 150), (_x + 3, 150), (_x, 126), (_x - 3, 150), (_x - 17, 150), k='h')
               + panah(220, 152, 220, 196, 4) + panah(220, 196, 220, 152, 4))
A['TA1B-3'] = (lantai() + orang(110, tinggi=175, jenis='pria', baju='h') + orang(195, tinggi=150, jenis='pria', baju='a')
               + teks(110, 216, '小明', 16) + teks(195, 216, '小文', 16))
A['TA1B-4'] = lantai() + kereta(185, 196, 210) + orang(45, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(12, 30), (20, 56)]}) + koper(72, 196, .6)

# ---------- A2 · paket A ----------
A['TA2A-1'] = (lantai() + rak_buku(205, 200, 110, 160) + orang(95, tinggi=158, jenis='wanita', baju='a', tangan={'ka': [(20, -20), (50, -40)]})
               + buku(150, 72, 22, 30, 'h'))
A['TA2A-2'] = (lantai() + meja(105, 140, 150) + piring(100, 134, 46) + bulat(86, 130, 2.5, 'h') + bulat(108, 129, 2, 'h') + bulat(118, 131, 2.5, 'h')
               + anjing(205, 198, 1.1) + bulat(262, 152, 3, 'h') + bulat(270, 162, 2.5, 'h') + bulat(256, 166, 2.5, 'h'))
A['TA2A-3'] = lantai() + toko(110, 200, 170, 120) + papan_angka(245, 60, '全部八折', 100, 46, uk=22)
A['TA2A-4'] = (lantai() + jendela(60, 30, 80, 60) + bulan_bintang(60, 52, .6) + jam_dinding(240, 50, 28, 9, 0)
               + meja(160, 140, 170) + komputer(185, 140, 90) + orang(110, tinggi=150, jenis='pria', duduk=145, baju='h', wajah='lelah', tangan={'ka': [(26, 4), (56, -2)]}))
# ---------- A2 · paket B ----------
A['TA2B-1'] = (lantai() + kardus(205, 200, 100, 60) + kaos(205, 132, .4, 'a')
               + orang(100, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(26, 20), (70, 30)]}))
A['TA2B-2'] = (lantai() + meja(170, 130, 170) + kucing(200, 130, .9)
               + bentuk((70, 198), (82, 186), (88, 198), k='p') + bentuk((96, 198), (104, 182), (114, 198), k='p') + bentuk((120, 198), (126, 190), (136, 198), k='p')
               + jalur('M74 176 l-6 -8 M100 172 l0 -10 M126 176 l6 -8', 'g'))
A['TA2B-3'] = lantai() + toko(110, 200, 170, 120) + papan_angka(245, 60, '全部七折', 100, 46, uk=22)
A['TA2B-4'] = (lantai() + papan_tulis(85, 30, 120, 70) + garis((45, 85), (75, 60), (100, 72), (125, 45), k='t', lebar=3)
               + orang(55, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(16, -14), (36, -34)]})
               + meja(215, 150, 130) + orang(185, tinggi=120, jenis='pria', duduk=150, baju='h') + orang(245, tinggi=120, jenis='pria', duduk=150, baju='p'))


def main():
    from svg_lib import bungkus
    os.makedirs(f'{R}/img/soal', exist_ok=True)
    for i, isi in A.items():
        open(f'{R}/img/soal/{i}.svg', 'w', encoding='utf-8').write(bungkus(isi))
    kartu = ''
    for lv in ('A0', 'A1', 'A2'):
        T = json.load(open(f'{K}/mini/tes_{lv}.json', encoding='utf-8'))
        for paket, items in T.items():
            for t in items:
                i = f'T{lv}{paket}-{t["no"]}'
                if t['type'] == 'listen_pic':
                    kartu += (f'<figure><img src="../../img/soal/{i}.svg"><figcaption><b>{i}</b> {t["question"]}<br>✔ {t["options"][t["answer"]]}'
                              f'<br><small>✗ {" / ".join(o for k, o in enumerate(t["options"]) if k != t["answer"])}<br>{t["picture"]["label"]}</small></figcaption></figure>')
                    if i not in A:
                        print('BELUM ADA GAMBAR', i)
    os.makedirs(f'{K}/gambar', exist_ok=True)
    open(f'{K}/gambar/periksa_tes.html', 'w', encoding='utf-8').write(
        '<!doctype html><meta charset="utf-8"><style>body{font-family:sans-serif;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:10px}'
        'figure{margin:0;border:1px solid #ccc;padding:4px}img{width:100%}figcaption{font-size:12px}</style>' + kartu)
    print(f'{len(A)} gambar ditulis; lembar periksa: _kerja/gambar/periksa_tes.html')


if __name__ == '__main__':
    main()
