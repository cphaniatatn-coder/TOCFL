"""Adegan ilustrasi 聽力 Part 1 — Volume 2 (B01–B46). ID = <modul>-<n> (listen_pic ke-n, urut isi → soal → bank)."""
from svg_adegan import *

A = {}
JOG = {'ki': [(16, 20), (30, 4)], 'ka': [(10, 28), (-6, 44)]}   # tangan berayun saat lari
LARI = {'ki': (-26, 0), 'ka': (22, -10)}


def pelari(x, jenis='pria', baju='a', tinggi=150):
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan=JOG, kaki_pose=LARI)


def tunjuk_ke(x, jenis, tinggi, sisi=1, baju='a', wajah='senyum'):
    """Orang menunjuk ke samping (sisi 1 = kanan)."""
    t = {'ka' if sisi == 1 else 'ki': [(20, -6), (46, -14)]}
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan=t, wajah=wajah)


# B01 — olahraga
A['B01-1'] = (lantai() + ring_basket(255) + orang(110, tinggi=165, jenis='pria', baju='a', tangan={'ki': [(10, -30), (4, -64)], 'ka': [(10, -30), (4, -64)]})
              + bola(110, 18, 14, 'basket'))
A['B01-2'] = lantai() + matahari(245, 52, 16) + jalur('M200 118 Q245 96 290 118', 't') + pelari(120, 'pria', 'a', 160)
A['B01-3'] = lantai() + gawang(235, 200, 100, 70) + orang(90, tinggi=120, jenis='laki', baju='h', kaki_pose={'ki': (-10, 0), 'ka': (30, -18)}) + bola(145, 184, 14)
A['B01-4'] = (lantai() + orang(130, tinggi=165, jenis='pria', baju='a', tangan={'ki': [(4, 24), (30, 18)], 'ka': [(-14, 24), (6, 18)]})
              + tongkat_bisbol(150, 92, 215, 40) + bola(250, 66, 9))
A['B01-5'] = lantai() + matahari(60, 60, 18) + jalur('M16 120 Q60 96 104 120', 't') + pelari(170, 'wanita', 'a', 155)

# B02 — rencana akhir pekan
A['B02-1'] = lantai() + pohon(250, s=.9) + tikar(120, 150, 200, 44) + keranjang(90, 164, 1.1) + buah_apel(150, 166, .6) + roti(190, 168, .45)
A['B02-2'] = (lantai() + pohon(40, s=.9) + pohon(262, s=.8) + tikar(150, 164, 200, 36) + keranjang(215, 176, .8)
              + orang(118, tinggi=130, jenis='wanita', duduk=176, baju='a') + orang(170, tinggi=100, jenis='gadis', duduk=176, baju='h'))
A['B02-3'] = (lantai() + orang(130, tinggi=165, jenis='pria', baju='a', wajah='puas') + headphone(130, 49, 14)
              + not_musik(200, 70) + not_musik(236, 110) + not_musik(60, 96))
A['B02-4'] = (lantai() + garis((20, 40), (280, 40), k='t') + ''.join(bentuk((30 + i * 36, 40), (48 + i * 36, 40), (39 + i * 36, 58), k='h' if i % 2 else 'a') for i in range(7))
              + orang(70, tinggi=140, jenis='wanita', baju='a', tangan=LAMBAI) + orang(150, tinggi=150, jenis='pria', baju='h', tangan={'ki': [(14, -30), (6, -58)]})
              + orang(230, tinggi=110, jenis='laki', baju='a', tangan=LAMBAI))
A['B02-5'] = garis((16, 196), (284, 196), k='t') + bingkai(150, 34, 170, 120, gunung(150, 154, 160, 90) + matahari(200, 64, 10) + pohon(98, 154, .5))

# B03 — pertandingan
_p, _pos = podium(150)
A['B03-1'] = lantai() + _p + orang(_pos[1][0], kaki=_pos[1][1], tinggi=100, jenis='pria', baju='a', tangan=ANGKAT) + orang(_pos[2][0], kaki=_pos[2][1], tinggi=100, jenis='pria', baju='a') + orang(_pos[3][0], kaki=_pos[3][1], tinggi=100, jenis='pria', baju='h') + panah(_pos[3][0], _pos[3][1] - 140, _pos[3][0], _pos[3][1] - 106, 5)
A['B03-2'] = lantai() + _p + orang(_pos[1][0], kaki=_pos[1][1], tinggi=100, jenis='pria', baju='h', tangan=ANGKAT) + panah(_pos[1][0], 12, _pos[1][0], 26, 5)
A['B03-3'] = (lantai() + orang(60, tinggi=140, jenis='wanita', baju='a', wajah='nyanyi', tangan={'ki': [(14, -30), (6, -58)], 'ka': [(14, -30), (6, -58)]})
              + orang(150, tinggi=150, jenis='pria', baju='h', wajah='nyanyi', tangan={'ki': [(14, -30), (6, -58)], 'ka': [(14, -30), (6, -58)]})
              + orang(240, tinggi=135, jenis='wanita', baju='p', wajah='nyanyi', tangan={'ki': [(14, -30), (6, -58)], 'ka': [(14, -30), (6, -58)]}))
A['B03-4'] = tiket(150, 60, 220, 110) + tongkat_bisbol(80, 150, 150, 80) + bola(170, 110, 16) + teks(236, 124, 'VS', 20, angka=True)
A['B03-5'] = lantai() + _p + orang(_pos[1][0], kaki=_pos[1][1], tinggi=100, jenis='pria', baju='a', tangan=ANGKAT) + orang(_pos[2][0], kaki=_pos[2][1], tinggi=100, jenis='pria', baju='h') + panah(_pos[2][0], _pos[2][1] - 140, _pos[2][0], _pos[2][1] - 106, 5)

# B04 — sedang apa
A['B04-1'] = lantai() + meja(170, 130, 180) + komputer(185, 130, 90) + orang(85, tinggi=150, jenis='pria', duduk=140, baju='h', tangan={'ka': [(26, 4), (56, -2)]}) + sinyal(250, 40)
A['B04-2'] = lantai() + meja(170, 130, 180) + komputer(185, 130, 90) + orang(85, tinggi=150, jenis='wanita', duduk=140, baju='a', tangan={'ka': [(26, 4), (56, -2)]}) + sinyal(250, 40)
A['B04-3'] = (lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (38, -4)]}) + orang(210, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 10), (38, -4)]})
              + titik_obrolan(120, 24, 56, 32, (-1, 1)) + titik_obrolan(186, 30, 56, 32, (1, 1)))
A['B04-4'] = lantai() + orang_ponsel(150, 'pria', 165, baju='a') + sinyal(190, 60)
A['B04-5'] = dua_panel(orang(75, kaki=200, tinggi=150, jenis='wanita', baju='a') + komputer(75, 190, 96) + titik_obrolan(112, 36, 56, 32, (-1, 1)),
                       orang(225, kaki=200, tinggi=155, jenis='pria', baju='h') + komputer(225, 190, 96) + titik_obrolan(188, 36, 56, 32, (1, 1)))

# B05 — tamu
A['B05-1'] = (lantai() + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 16), (46, 10)]}) + cangkir(172, 100, .6) + meja(230, 150, 90)
              + orang(250, tinggi=110, jenis='wanita', duduk=150, baju='h'))
A['B05-2'] = (lantai() + meja(150, 150, 220) + kue_ultah(150, 150, '', .75) + ''.join(garis((110 + i * 20, 112), (110 + i * 20, 96), lebar=4) for i in range(5))
              + orang(60, tinggi=140, jenis='wanita', baju='a', tangan=LAMBAI) + orang(245, tinggi=145, jenis='pria', baju='h', tangan={'ki': [(14, -30), (6, -58)]})
              + ''.join(bentuk((96 + i * 28, 40), (108 + i * 28, 40), (102 + i * 28, 30), k='h') for i in range(4)))
A['B05-3'] = lantai() + sofa(110) + kotak(200, 40, 80, 110, 'p', 6) + roti(240, 110, .45) + larangan(240, 96, 32)
A['B05-4'] = (lantai() + kardus(80, 124, 64, 40) + kardus(80, 162, 70, 40) + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='sedih', tangan={'ki': [(10, 20), (4, 60)], 'ka': [(10, 20), (4, 60)]})
              + kardus(80, 124, 64, 40) + orang(215, tinggi=165, jenis='pria', baju='h'))

# B06 — kenalan
A['B06-1'] = (lantai() + orang(60, tinggi=150, jenis='nenek', baju='a', rambut='uban', tangan={'ka': [(6, 30), (14, 60)]}) + garis((80, 110), (84, 200), lebar=4)
              + orang(150, tinggi=165, jenis='pria', baju='h') + orang(240, tinggi=90, jenis='gadis') + panah(150, 8, 150, 26, 5))
A['B06-2'] = lantai() + orang(100, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 16), (44, 20)]}) + orang(200, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 16), (44, 20)]})
A['B06-3'] = lantai() + pohon(260, s=.8) + orang(50, tinggi=90, jenis='laki', baju='h', tangan=LAMBAI) + orang(110, tinggi=85, jenis='gadis', baju='a') + bola(150, 188, 12) + orang(190, tinggi=90, jenis='laki', baju='a', kaki_pose={'ki': (-10, 0), 'ka': (20, -12)})
A['B06-4'] = kalender_senin(150, 30, 2, 3) + lantai() + orang(100, tinggi=90, jenis='wanita', baju='a', tangan={'ka': [(14, 10), (30, 12)]}) + orang(200, tinggi=95, jenis='pria', baju='h', tangan={'ki': [(14, 10), (30, 12)]})
A['B06-5'] = lantai() + orang(150, tinggi=160, jenis='nenek', rambut='uban', baju='a', wajah='puas', rok=False)

# B07 — rumah baru
A['B07-1'] = lantai() + meja(160, 130, 160) + buku(140, 130, 40, 30, 'h') + buku(175, 200, 40, 26, 'a') + tunjuk_ke(55, 'pria', 160, 1, 'a')
A['B07-2'] = lantai() + kardus(80, 200, 90, 60) + kardus(80, 140, 76, 50) + kardus(180, 200, 90, 70) + kardus(250, 200, 50, 40, 'p')
A['B07-3'] = (lantai() + gedung(95, tingkat=6, lebar=110) + gedung(215, tingkat=5, lebar=90) + kotak(40, 42, 110, 22, 'h') + buku(95, 60, 20, 14, 'p')
              + orang(160, tinggi=120, jenis='laki', baju='a'))
A['B07-4'] = (lantai_kamar() + ranjang(60, 200, 90) + ranjang(240, 200, 90) + orang(125, tinggi=150, jenis='pria', baju='a')
              + orang(180, tinggi=155, jenis='pria', baju='h', kacamata=True))
A['B07-5'] = lantai() + rumah(150, 200, 230, 110) + orang(275, tinggi=60, jenis='pria', baju='a')

# B08 — ruangan
A['B08-1'] = kotak(20, 20, 260, 180, 'p') + jendela_buka(150, 60, 110, 90)
A['B08-2'] = kotak(20, 16, 260, 188, 'p') + lampu(150, 70, True) + meja(150, 160, 150, 40)
_r, _ya = penampang_rumah()
A['B08-3'] = lantai() + _r + kloset(90, 200, 1.1) + kotak(54, 118, 70, 12, 'p', 3) + panah(165, 150, 118, 170, 5)
A['B08-4'] = kotak(20, 16, 260, 188, 'p') + ac(150, 40, True)
A['B08-5'] = lantai() + _r + lemari_buku(90, _ya - 4, 70, 56) + meja(150, _ya - 30, 50, 26) + panah(190, 36, 132, 70, 5)

# B09 — bantu-bantu
A['B09-1'] = kotak(20, 16, 260, 188, 'p') + ac(150, 70, rusak=True)
A['B09-2'] = lantai() + meja(170, 150, 160) + baskom_cuci(170, 150) + orang(90, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(24, 26), (60, 36)]})
A['B09-3'] = kotak(20, 16, 260, 188, 'p') + lampu(200, 70, True) + orang(90, kaki=200, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -20), (52, -48)]})
A['B09-4'] = lantai() + meja(150, 150, 170) + tv_retak(150, 150, 150)
A['B09-5'] = (kotak(20, 16, 260, 188, 'p') + kotak(175, 50, 70, 150, 'h') + bentuk((245, 50), (272, 38), (272, 204), (245, 200), k='p')
              + bulat(264, 124, 3, 'h') + tunjuk_ke(90, 'pria', 160, 1, 'h'))   # pintu terbuka

# B10 — kebiasaan
A['B10-1'] = kotak(20, 16, 150, 188, 'p') + pancuran(95, 80) + orang(95, tinggi=110, jenis='pria', baju='p', wajah='puas') + jam_sektor(228, 100, 56, 20)
A['B10-2'] = kotak(20, 16, 150, 188, 'p') + pancuran(95, 80) + orang(95, tinggi=110, jenis='wanita', baju='p', wajah='puas') + jam_sektor(228, 100, 56, 15)
A['B10-3'] = lantai() + kalender_minggu(150, 12, 0, 0, 260).replace('>今天<', '>週日<') + sofa(150, 200, 170) + orang(150, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='puas')
A['B10-4'] = kotak(20, 16, 260, 188, 'p') + jendela(230, 30, 70, 56) + bulan_bintang(225, 58, .45) + pancuran(110, 90) + orang(110, tinggi=120, jenis='wanita', baju='p', wajah='puas')
A['B10-5'] = lantai_kamar() + jendela(215, 36, 60, 46) + matahari(215, 58, 9) + ranjang(110, 200, 170) + bulat(56, 136, 13) + muka(56, 136, 13, 'tidur') + jalur('M42 131 q2 -18 16 -18 q12 0 13 14', 'h') + teks(92, 110, 'z z', 18, angka=True)

# B11 — kerja
A['B11-1'] = jam_dinding(75, 100, 58, 9, 0) + panah(140, 100, 160, 100, 6) + jam_dinding(225, 100, 58, 5, 0)
A['B11-2'] = lantai() + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'h') + orang(250, tinggi=160, jenis='wanita', baju='a', tangan={'ki': [(10, 24), (20, 30)]}) + tas_kerja(230, 196, .6)
A['B11-3'] = lantai() + gedung(70, tingkat=5, lebar=90) + jam_dinding(225, 50, 30, 5, 0) + jalan_kaki(200, 'pria', 140, 'h') + tas_kerja(178, 156, .45)
A['B11-4'] = kalender_senin(150, 24, 2, 3) + tas_kerja(150, 190, 1.2)
A['B11-5'] = lantai() + orang(80, tinggi=110, jenis='laki', baju='a') + gelembung_pikiran(195, 70, 150, 110, orang(195, kaki=118, tinggi=90, jenis='pria', baju='p', kacamata=True) + jalur('M187 64 q8 18 16 0', 't') + palang(222, 60, .3), 118, 110)

# B12 — keluarga & hewan
A['B12-1'] = lantai() + kucing(95, 196, 1.2) + kucing(210, 196, 1.2, 'a')
A['B12-2'] = lantai() + anjing(140, 198, 1.4)
A['B12-3'] = kotak(18, 18, 264, 184, 'h', 4) + kotak(26, 26, 248, 168, 'p') + rumah(95, 184, 100, 70) + orang(200, kaki=184, tinggi=140, jenis='nenek', rambut='pendek', baju='a', rok=False) + orang(250, kaki=184, tinggi=78, jenis='laki')
A['B12-4'] = lantai() + orang(60, tinggi=150, jenis='nenek', rambut='uban', baju='a') + kucing(135, 198, .8) + kucing(195, 198, .8, 'a') + kucing(255, 198, .8, 'h')
A['B12-5'] = kotak(18, 18, 264, 184, 'h', 4) + kotak(26, 26, 248, 168, 'p') + papan_tulis(110, 44, 140, 70) + orang(225, kaki=184, tinggi=140, jenis='pria', baju='a', kacamata=True, tangan={'ki': [(10, -10), (34, -40)]})
