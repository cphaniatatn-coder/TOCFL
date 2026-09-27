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


def biji_kopi(x, y, s=1.0):
    return elips(x, y, 8 * s, 11 * s, 'h') + jalur(f'M{f(x)} {f(y - 10 * s)} q{f(-4 * s)} {f(10 * s)} 0 {f(20 * s)}', 'w')


# ---------------- B13–B24 ----------------
def _kepala(x, tinggi, jenis):
    s_ = sendi(x, LANTAI, tinggi, jenis)
    return s_['cy'], s_['r']


def kelas_murid(jenis_list, y=200):
    o = lantai()
    n = len(jenis_list)
    for i, j in enumerate(jenis_list):
        o += orang(40 + i * (220 / max(n - 1, 1)), tinggi=100, jenis=j, baju='a' if j == 'gadis' else 'h')
    return o


# B13 — angka & jumlah
A['B13-1'] = lantai() + sekolah(95, 200, 150, 100) + papan_angka(230, 70, '215人', 100, 46)
A['B13-2'] = lantai() + sekolah(95, 200, 150, 100) + papan_angka(230, 70, '320人', 100, 46)
A['B13-3'] = (lantai() + garis((150, 60), (150, 200), k='t') + orang(45, tinggi=110, jenis='laki', baju='h') + orang(100, tinggi=115, jenis='laki', baju='a')
              + orang(200, tinggi=108, jenis='gadis', baju='a') + orang(255, tinggi=112, jenis='gadis', baju='h'))
A['B13-4'] = layar_ponsel(150, 110, '', 2.6) + teks(150, 100, '0912-', 22, angka=True) + teks(150, 130, '345-678', 22, angka=True)
A['B13-5'] = kelas_murid(['gadis'] * 5)

# B14 — sekolah
A['B14-1'] = lantai() + tas_buka(150, 196, 13, 1.6)
A['B14-2'] = lantai() + sekolah(210, 200, 130, 90) + orang(80, tinggi=90, jenis='gadis', baju='a') + tas_punggung(58, 138, .75)
A['B14-3'] = lantai() + tas_buka(150, 196, 12, 1.6)
A['B14-4'] = lantai() + sekolah(200, 200, 150, 100, '高中') + orang(70, tinggi=150, jenis='laki', baju='h') + tas_punggung(46, 104, .9)
A['B14-5'] = kalender_bulan(95, 34, 9, '', 130, 130) + lantai() + jalan_kaki(230, 'laki', 110, 'a') + tas_punggung(210, 124, .7)

# B15 — bahasa
A['B15-1'] = lantai() + meja(150, 150, 240) + kertas(185, 132, 70, 30, 0) + orang(110, tinggi=150, jenis='wanita', duduk=156, baju='a', tangan={'ka': [(20, 20), (54, 26)]}) + pulpen(186, 128, 40, -40)
A['B15-2'] = lantai() + orang(85, tinggi=160, jenis='wanita', baju='a', wajah='nyanyi') + gelembung(200, 70, 150, 70, teks(200, 80, 'こんにちは', 22, angka=True), (-1, 1))
A['B15-3'] = kertas_kotak(150, 40, 180, 150)
A['B15-4'] = (lantai() + orang(80, tinggi=160, jenis='pria', baju='h', wajah='kaget', tangan={'ka': [(20, -4), (40, -20)]}) + orang(190, tinggi=150, jenis='wanita', baju='a')
              + orang(250, tinggi=145, jenis='pria', baju='a') + centang(220, 22, 1.2) + jalur('M110 36 q10 4 16 0 M110 48 q10 4 16 0', 'g'))
A['B15-5'] = lantai() + kamus(150, 196)

# B16 — belajar
A['B16-1'] = lantai() + meja(160, 140, 220) + buku_tumpuk(230, 140, 2, 50, 14) + kertas(160, 128, 60, 20) + lampu(250, 70) + orang(95, tinggi=150, jenis='laki', duduk=146, baju='a', wajah='senyum', tangan={'ka': [(24, 16), (54, 22)]})
A['B16-2'] = kalender_senin(150, 14, 2, 3) + lantai() + meja(150, 150, 200) + kertas(170, 136, 60, 24) + orang(110, tinggi=140, jenis='gadis', duduk=154, baju='a', tangan={'ka': [(22, 16), (52, 20)]})
A['B16-3'] = (lantai() + tas_buka(90, 196, 0, 1.0) + orang(190, tinggi=150, jenis='laki', baju='a', wajah='kaget')
              + gelembung_pikiran(235, 50, 90, 64, buku(235, 66, 30, 32, 'h') + silang(235, 50, 20, 5), 205, 84))
A['B16-4'] = lantai() + meja(160, 140, 220) + buku(200, 140, 40, 26, 'a') + kertas(160, 128, 60, 20) + orang(95, tinggi=150, jenis='pria', duduk=146, baju='h', tangan={'ka': [(24, 16), (54, 22)]})
A['B16-5'] = kotak(70, 90, 160, 60, 'p', 10) + kotak(78, 98, 144, 44, 'a', 6) + gelembung_pikiran(220, 44, 90, 60, pulpen(220, 44, 60, -20) + silang(220, 44, 22, 5), 190, 74)

# B17 — perpustakaan & buku
A['B17-1'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='pria', duduk=150, baju='a', tangan={'ki': [(20, 0), (30, -20)], 'ka': [(20, 0), (30, -20)]}) + koran(150, 60, 150, 90)
A['B17-2'] = lantai() + rak_buku(55, 200, 90, 160) + rak_buku(250, 200, 80, 160) + meja(150, 140, 110) + buku(150, 140, 34, 20, 'a') + orang(150, tinggi=130, jenis='gadis', duduk=150, baju='a')
A['B17-3'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(20, -14), (30, -48)]}) + buku(200, 58, 38, 48, 'h') + bintang(236, 30, 8) + bintang(170, 20, 6)
A['B17-4'] = lantai() + rak_buku(60, 200, 100, 160) + kasir(215) + label_harga(232, 24, '120', 100, 40) + orang(140, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(16, 16), (30, 20)]}) + buku(186, 116, 24, 30, 'a')
A['B17-5'] = lantai() + lonceng(230, 60, .6) + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='kaget', tangan={'ka': [(16, -4), (2, -26)]}) + jalur('M150 36 q10 12 0 24 M162 28 q16 20 0 40', 'g')

# B18 — musim & cuaca
A['B18-1'] = lantai() + gunung(150, 200, 260, 150) + ''.join(salju(40 + (i * 53) % 230, 20 + (i * 37) % 120, 7) for i in range(10))
A['B18-2'] = lantai() + gedung(70, tingkat=5, lebar=80) + rumah(210, 200, 110, 70) + ''.join(salju(30 + (i * 61) % 250, 18 + (i * 29) % 90, 6) for i in range(12))
A['B18-3'] = lantai() + pohon(250) + ''.join(bunga(30 + i * 40, 150 + (i % 2) * 12, .9) for i in range(5)) + kupu(80, 80) + kupu(170, 60, .8)
A['B18-4'] = (lantai() + manusia_salju(220) + orang(90, tinggi=160, jenis='pria', baju='h', wajah='sedih') + syal(90, 72, 14)
              + ''.join(salju(30 + (i * 67) % 250, 20 + (i * 31) % 70, 6) for i in range(8)))
A['B18-5'] = lantai() + pohon_gugur(150, 200, 1.2)

# B19 — perbandingan
A['B19-1'] = lantai() + orang(110, tinggi=175, jenis='pria', baju='h') + orang(200, tinggi=110, jenis='laki', baju='a') + garis((150, 25), (240, 25), k='t') + garis((150, 90), (240, 90), k='t')
A['B19-2'] = (teks(80, 30, '台北', 26) + termometer(80, 44, 12) + salju(40, 90, 10) + teks(128, 150, '12°', 24, angka=True)
              + teks(220, 30, '高雄', 26) + termometer(220, 44, 28) + matahari(262, 76, 12) + teks(268, 150, '28°', 24, angka=True))
A['B19-3'] = (lantai() + orang(90, tinggi=165, jenis='pria', baju='h', wajah='nyanyi', tangan={'ka': [(16, -10), (8, -30)]}) + jalur('M120 40 l40 -14 M122 52 l46 0 M120 64 l40 14', 'g', 4)
              + orang(230, tinggi=150, jenis='wanita', baju='a', wajah='sakit', tangan={'ki': [(16, -4), (0, -24)], 'ka': [(16, -4), (0, -24)]}))
A['B19-4'] = lantai() + orang(110, tinggi=175, jenis='pria', baju='a') + orang(200, tinggi=100, jenis='laki', baju='h') + panah(200, 58, 200, 84, 4) + teks(200, 50, '我', 18)
A['B19-5'] = lantai() + orang(110, tinggi=155, jenis='wanita', baju='a', tangan={'ka': [(16, -2), (-2, -24)]}) + bibir_bisik(128, 60) + orang(210, tinggi=160, jenis='pria', baju='h')

# B20 — pakaian & aksesori
_cy, _r = _kepala(150, 165, 'pria')
A['B20-1'] = (lantai() + orang(150, tinggi=165, jenis='pria', baju='p', tangan={'ki': [(14, 40), (30, 74)], 'ka': [(14, 40), (30, 74)]}, badan=1.5)
              + bentuk((150 - _r * 2, _cy + _r * 1.3), (150 + _r * 2, _cy + _r * 1.3), (150 + _r * 2.8, 150), (150 - _r * 2.8, 150), k='a')
              + garis((150, _cy + _r * 1.3), (150, 150), k='t'))
_cy2, _r2 = _kepala(150, 165, 'wanita')
A['B20-2'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a') + kacamata_di(150, _cy2, _r2)
A['B20-3'] = (lantai() + garis((30, 40), (270, 40), lebar=4) + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -20), (40, -50)]})
              + bentuk((150, 50), (190, 50), (200, 170), (140, 170), k='a') + garis((170, 42), (170, 50)) + garis((170, 50), (170, 170), k='t'))
A['B20-4'] = (lantai() + orang(150, tinggi=150, jenis='wanita', baju='p', tangan={'ki': [(14, 40), (26, 76)], 'ka': [(14, 40), (26, 76)]})
              + bentuk((150 - 22, 80), (150 + 22, 80), (150 + 46, 202), (150 - 46, 202), k='a') + garis((150, 80), (150, 202), k='t'))
A['B20-5'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a') + topi_di(150, _cy2, _r2)

# B21 — warna, berat (soal warna DIBERI WARNA)
A['B21-1'] = lantai() + sepatu(105, 196, 1.4, 'hijau') + sepatu(205, 196, 1.4, 'hijau')
A['B21-2'] = (jalur('M110 30 L190 30 L205 196 L160 196 L150 90 L140 196 L95 196 Z', 'biru') + garis((110, 44), (190, 44), k='t'))
A['B21-3'] = lantai() + orang(110, tinggi=160, jenis='gadis', baju='a', wajah='puas', tangan={'ka': [(20, -10), (30, -40)]}) + tas_punggung(170, 24, 1.1) + garis((148, 42), (170, 24), k='t')
A['B21-4'] = lantai() + sepatu(105, 196, 1.4, 'biru') + sepatu(205, 196, 1.4, 'biru')
A['B21-5'] = lantai() + orang(130, tinggi=150, jenis='laki', baju='a', wajah='sakit', tangan={'ka': [(14, 30), (30, 60)]}) + tas_punggung(170, 150, 1.4) + keringat(160, 50) + keringat(100, 60, .8)

# B22 — belanja
A['B22-1'] = lantai() + botol(80, 196, 1.3) + botol(140, 196, 1.3) + kaleng(220, 196, 1.4)
A['B22-2'] = lantai() + minimarket(150)
A['B22-3'] = lantai() + kasir(200) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (46, -8)]}) + tas_belanja(150, 118, .9) + orang(250, tinggi=150, jenis='pria', baju='h')
A['B22-4'] = lantai() + kios_buah(95, 200, 150) + troli(225, 200, 1.0) + buah_apel(225, 108, .6) + buah_apel(208, 112, .5)
A['B22-5'] = lantai() + botol(115, 196, 1.5) + botol(185, 196, 1.5)

# B23 — tas & pembayaran
A['B23-1'] = lantai() + orang(130, tinggi=165, jenis='wanita', baju='a', tangan={'ka': [(12, 30), (22, 60)]}) + tas_tangan(160, 170, 1.0)
A['B23-2'] = lantai() + kasir(210) + orang(90, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 0), (46, -10)]}) + kartu_kredit(150, 62, .8)
A['B23-3'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a') + kotak(96, 60, 20, 44, 'h', 6) + tas_punggung(116, 70, .6)
A['B23-4'] = lantai() + kios_buah(150, 200, 200) + orang(150, tinggi=150, jenis='pria', baju='h', rambut='pendek').replace('class="p"', 'class="p"')
A['B23-5'] = kotak(80, 40, 140, 150, 'p', 26) + kotak(95, 55, 110, 120, 'a', 16) + dompet(150, 118, .7) + garis((80, 90), (220, 90), k='t')

# B24 — makanan
A['B24-1'] = lantai() + es_krim(95, 196, 1.2) + piring(205, 190, 60, potong_kue(205, 186, .9))
A['B24-2'] = (lantai() + meja(150, 150, 240) + piring(200, 144, 50, cabai(185, 128, .7) + cabai(200, 134, .6)) + orang(95, tinggi=150, jenis='pria', baju='a', wajah='sakit')
              + keringat(120, 40) + jalur('M84 70 l-12 10 M94 76 l-2 14 M104 70 l10 10', 'g'))
A['B24-3'] = lantai() + es_krim(150, 196, 1.6)
A['B24-4'] = lantai() + meja(150, 150, 240) + mangkuk_mi(190, 120, .4, sumpit=False) + garam(240, 110, .8) + orang(90, tinggi=150, jenis='wanita', baju='a', wajah='sakit')
A['B24-5'] = lantai() + meja(150, 150, 240) + piring(100, 144, 50, potong_kue(100, 140, .75)) + cangkir_kopi(200, 146, .9) + biji_kopi(258, 134) + biji_kopi(272, 142, .8)



# ---------------- B25–B36 ----------------
MASAK = {'ka': [(22, 10), (50, 4)]}


def burung(x, y, arah=1, s=1.0):
    a = arah
    return (elips(x, y, 18 * s, 11 * s, 'a') + bulat(x + a * 16 * s, y - 8 * s, 8 * s, 'a') + bentuk((x + a * 23 * s, y - 9 * s), (x + a * 32 * s, y - 6 * s), (x + a * 23 * s, y - 4 * s), k='h')
            + bulat(x + a * 18 * s, y - 10 * s, 1.8 * s, 'h') + bentuk((x - a * 14 * s, y), (x - a * 30 * s, y - 8 * s), (x - a * 28 * s, y + 4 * s), k='h')
            + jalur(f'M{f(x - a * 4 * s)} {f(y - 2 * s)} q{f(-a * 8 * s)} {f(-14 * s)} {f(-a * 18 * s)} {f(-10 * s)}', 'g') + garis((x, y + 10 * s), (x, y + 18 * s), k='t'))

# B25 — memasak & alat makan
A['B25-1'] = lantai() + kompor(185, 130) + api(185, 128, .8) + wajan(185, 112, 1.0) + orang(80, tinggi=160, jenis='pria', baju='a', tangan=MASAK)
A['B25-2'] = lantai() + panggangan(185, 110) + daging(160, 104, .6) + daging(210, 104, .55) + api(185, 120, .6) + orang(70, tinggi=160, jenis='pria', baju='h', tangan=MASAK)
A['B25-3'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, 6), (48, -2)]}) + sendok(190, 86, 120, -20)
A['B25-4'] = lantai() + kompor(190, 140) + api(190, 138, .8) + panci_goreng(190, 90, 120) + paha_ayam(175, 80, .8) + orang(80, tinggi=160, jenis='wanita', baju='h', tangan=MASAK)
A['B25-5'] = garpu(150, 110, 170, -25)

# B26 — minuman & buah
A['B26-1'] = lantai() + gelas_isi(110, 196, 1.6, 'a', True) + buah_apel(210, 190, 1.4)
A['B26-2'] = lantai() + orang(120, tinggi=165, jenis='pria', baju='a', wajah='puas', tangan={'ka': [(14, 26), (-4, -6)]}) + kaleng_soda(148, 70, .8) + keringat(96, 40)
A['B26-3'] = lantai() + matahari(240, 50, 20) + semangka(130, 110, 1.3)
A['B26-4'] = lantai() + cangkir(150, 190, 1.8, True) + elips(150, 190 - 72, 36, 6, 'a') + kantong_teh(172, 120)
A['B26-5'] = pisang(150, 120, 1.6)

# B27 — jajanan
A['B27-1'] = piring(150, 160, 120, pangsit(100, 152, 1.1) + pangsit(150, 150, 1.1) + pangsit(200, 152, 1.1) + pangsit(125, 136, 1.0) + pangsit(175, 136, 1.0))
A['B27-2'] = lantai(196, 60, 240) + hamburger(150, 180, 1.3)
_nightm = (lantai() + bulan_bintang(250, 30, .5) + garis((20, 60), (280, 60), k='t') + ''.join(lampion(40 + i * 44, 72, .7) for i in range(6))
           + kotak(20, 130, 110, 70, 'a') + kotak(170, 130, 110, 70, 'a') + kotak(14, 118, 122, 14, 'h') + kotak(164, 118, 122, 14, 'h'))
A['B27-3'] = _nightm + orang(150, tinggi=112, jenis='wanita', baju='p')
A['B27-4'] = _nightm + orang(130, tinggi=110, jenis='wanita', baju='p', tangan={'ka': [(12, 20), (-4, -2)]}) + orang(175, tinggi=116, jenis='pria', baju='h')
A['B27-5'] = lantai() + meja(150, 150, 240) + piring(190, 144, 56, mangkuk_mi(190, 120, .3, sumpit=False)) + orang(90, tinggi=150, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(16, -4), (26, -30)]}) + jempol(130, 64, 1.0)

# B28 — restoran & kedai teh
A['B28-1'] = lantai() + meja(150, 150, 240) + orang(80, tinggi=150, jenis='wanita', baju='a', duduk=156, tangan={'ka': [(20, -6), (40, -16)]}) + orang(225, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(16, 10), (34, 14)]}) + buku_menu(175, 110, .9)
A['B28-2'] = lantai() + kedai_teh(150)
A['B28-3'] = (lantai() + kotak(150, 50, 134, 150, 'p') + kotak(186, 100, 56, 100, 'h') + ''.join(bintang(172 + i * 24, 70, 9) for i in range(4))
              + orang(40, tinggi=140, jenis='wanita', baju='a') + orang(80, tinggi=150, jenis='pria', baju='h') + orang(118, tinggi=145, jenis='wanita', baju='p'))
A['B28-4'] = (kotak(20, 16, 260, 188, 'p') + lampion(60, 50, .8) + lampion(240, 50, .8) + meja(150, 150, 200) + teko(150, 146, .5) + cangkir(100, 146, .4, False) + cangkir(200, 146, .4, False)
              + orang(60, tinggi=130, jenis='wanita', baju='a', duduk=160) + orang(240, tinggi=135, jenis='pria', baju='h', duduk=160))

# B29 — jarak
A['B29-1'] = lantai() + rumah(95) + pohon(200) + pohon(250, s=.8) + bangku(225)
A['B29-2'] = rumah(50, 200, 70, 50) + jalan_panjang(70, 196, 230, 60) + sekolah(245, 90, 70, 50)
A['B29-3'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ki': [(10, 24), (30, 10)], 'ka': [(10, 24), (30, 10)]}) + peta(110, 92, 120, 70)
A['B29-4'] = lantai() + stasiun(210, 200, 130, 90) + orang(95, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -6), (46, -14)]})
A['B29-5'] = lantai() + rumah(80, 200, 110, 80) + jalan_kaki(210, 'pria', 150, 'h') + koper(250, 196, .8)

# B30 — arah
A['B30-1'] = perempatan('kanan')
A['B30-2'] = perempatan('kiri')
A['B30-3'] = lantai() + rumah(225, 200, 110, 80) + jalan_kaki(60, 'wanita', 150, 'a') + jalan_kaki(120, 'laki', 100, 'h') + panah(140, 40, 175, 40, 4)
A['B30-4'] = perempatan('kanan')
A['B30-5'] = lantai() + rumah(200, 200, 140, 90) + jam_dinding(60, 60, 36, 6, 0) + jalan_kaki(110, 'pria', 140, 'a')

# B31 — kendaraan
A['B31-1'] = lantai() + sekolah(235, 200, 100, 80) + pengendara_sepeda(110, 'laki', 'a', 110)
A['B31-2'] = (lantai() + kotak(40, 40, 220, 160, 'p', 14) + kotak(60, 60, 180, 70, 'h', 6) + bulat(90, 186, 16, 'h') + bulat(210, 186, 16, 'h')
              + orang(150, kaki=150, tinggi=100, jenis='pria', baju='a', tangan={'ki': [(10, 20), (20, 24)], 'ka': [(10, 20), (20, 24)]}) + elips(150, 124, 30, 8, 'g') + kotak(40, 140, 220, 12, 'a'))
A['B31-3'] = lantai() + sekolah(70, 200, 110, 80) + mobil(200, 200, 150) + orang(275, tinggi=90, jenis='laki', baju='h', tangan=LAMBAI)
A['B31-4'] = lantai() + gedung(245, tingkat=6, lebar=80) + pengendara_sepeda(110, 'pria', 'h', 130) + tas_kerja(86, 138, .45)
A['B31-5'] = (lantai() + kereta(170, 196, 220) + orang(40, tinggi=150, jenis='wanita', baju='a', rambut='uban', tangan=LAMBAI)
              + orang(100, tinggi=120, jenis='gadis', baju='h', tangan={'ki': [(14, -30), (6, -58)]}))

# B32 — arah gerak
A['B32-1'] = kotak(90, 30, 120, 170, 'h') + orang(150, kaki=208, tinggi=175, jenis='pria', baju='a') + panah(250, 90, 250, 170, 6) + lantai()
A['B32-2'] = lantai() + pesawat_depan(150, 60, .8) + panah(150, 118, 150, 140, 5) + orang(150, tinggi=60, jenis='pria', baju='h', tangan={'ka': [(8, -10), (8, -24)]})
A['B32-3'] = lantai() + menara_bandara(250) + pesawat(115, 150, .8) + garis((16, 190), (200, 190), k='t')
A['B32-4'] = lantai() + gedung(150, tingkat=5, lebar=170) + kotak(120, 130, 60, 70, 'h') + orang(150, kaki=208, tinggi=150, jenis='wanita', baju='a') + panah(40, 130, 40, 190, 6)
A['B32-5'] = awan(60, 150, .5) + awan(240, 40, .45) + pesawat(130, 100, .8) + panah(40, 160, 270, 160, 6)

# B33 — datang & pergi
A['B33-1'] = lantai() + garis((16, 190), (284, 190), k='t') + pesawat(170, 150, .8) + teks(60, 60, '臺灣', 34) + panah(250, 110, 230, 130, 4)
A['B33-2'] = lantai() + kereta(170, 196, 220) + orang(38, tinggi=150, jenis='pria', baju='h') + koper(62, 196, .6)
A['B33-3'] = kotak(20, 16, 260, 188, 'p') + kursi_depan(90, 150) + kotak(170, 40, 70, 160, 'h') + bentuk((240, 40), (262, 30), (262, 206), (240, 200), k='p') + jalan_kaki(215, 'pria', 140, 'a')
A['B33-4'] = kalender_tahun(55, 60, 2024) + kalender_tahun(150, 60, 2025, True) + kalender_tahun(245, 60, 2026) + teks(245, 160, '今年', 20) + pesawat(150, 94, .22)
A['B33-5'] = kotak(20, 16, 260, 188, 'p') + kursi_depan(100, 150) + meja(180, 150, 90) + kotak(222, 40, 50, 160, 'h') + bentuk((272, 40), (284, 34), (284, 206), (272, 200), k='p')

# B34 — alam
A['B34-1'] = (bentuk((16, 150), (284, 150), (284, 204), (16, 204), k='a') + ''.join(jalur(f'M{24 + i * 20} 150 l4 -10 l4 10', 't') for i in range(13)) + pohon(260, 150, .8)
              + orang(100, tinggi=120, jenis='wanita', duduk=172, baju='p') + orang(170, tinggi=125, jenis='pria', duduk=172, baju='h'))
A['B34-2'] = lantai_kamar() + pintu(250, 200, 140, 60) + ranjang(110, 200, 170) + bulat(56, 136, 13) + muka(56, 136, 13, 'tidur') + jalur('M42 131 q2 -18 16 -18 q12 0 13 14', 'h') + tas_kerja(200, 196, .6)
A['B34-3'] = lantai() + pohon(150, s=1.5) + burung(125, 60) + burung(180, 80, -1)
A['B34-4'] = lantai() + lonceng(60, 50, .5) + rumah(225, 200, 110, 80) + jalan_kaki(130, 'laki', 110, 'a') + tas_punggung(110, 120, .7) + panah(150, 40, 190, 40, 4)
A['B34-5'] = gunung(90, 150, 180, 110) + gunung(220, 150, 170, 90, False) + jalur('M16 200 C80 150 180 190 284 160 L284 180 C180 210 80 170 16 216 Z', 'a') + garis((16, 150), (284, 150), k='t') + pohon(40, 190, .5) + matahari(250, 36, 12)

# B35 — penginapan & izin
A['B35-1'] = (lantai() + gedung(150, tingkat=5, lebar=160) + kotak(95, 30, 110, 44, 'h', 4) + kotak(112, 52, 76, 10, 'n') + kotak(112, 40, 6, 22, 'n')
              + kotak(182, 52, 6, 12, 'n') + elips(130, 47, 9, 5, 'n'))   # papan bergambar tempat tidur
A['B35-2'] = lantai() + gedung(95, tingkat=5, lebar=120) + papan_angka(230, 80, '$500', 110, 50)
A['B35-3'] = (lantai() + orang(90, tinggi=165, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(22, 0), (48, -6)]}) + orang(210, tinggi=100, jenis='laki', baju='h', tangan={'ki': [(14, 6), (30, -4)]})
              + cangkir(170, 118, .5) + silang(150, 70, 14, 5))
A['B35-4'] = lantai_kamar() + ranjang(150, 200, 200) + orang(110, tinggi=150, jenis='wanita', baju='a') + orang(190, tinggi=125, jenis='gadis', baju='h')
A['B35-5'] = lantai() + orang(90, tinggi=165, jenis='wanita', baju='a', rambut='uban', wajah='puas') + centang(90, 16, 1.2) + orang(200, tinggi=110, jenis='gadis', baju='h', tangan=LAMBAI) + koper(245, 196, .8)

# B36 — pos & bank
A['B36-1'] = lembar_prangko(150, 70, 3, 2, 48)
A['B36-2'] = lantai() + loket(200) + kotak(172, 34, 56, 40, 'p', 4) + amplop(200, 54, 40, 26) + orang(80, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 0), (46, -8)]}) + amplop(140, 80, 44, 30, -10)
A['B36-3'] = (lantai() + meja(150, 150, 220) + pulpen(190, 138, 60, 0) + orang(70, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(26, 8), (58, 14)]})
              + orang(240, tinggi=150, jenis='pria', baju='h'))
A['B36-4'] = lantai() + gedung_bank(150)
A['B36-5'] = lantai() + kotak_pos(200) + orang(100, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, 0), (48, -6)]}) + amplop(166, 82, 40, 26, 20)
