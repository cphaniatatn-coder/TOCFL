"""Adegan ilustrasi 聽力 Part 1 — Volume 1 (A01–A25). ID = <modul>-<n> (listen_pic ke-n, urut isi → soal → bank)."""
from svg_adegan import *

A = {}

# A01 — sapaan & nama
A['A01-1'] = lantai() + bulan_bintang(50, 40, .75) + rumah(215) + orang(120, tinggi=145, jenis='wanita', baju='a', tangan=LAMBAI)
A['A01-2'] = kartu_nama(150, 60, '王大文', 200, 100)
A['A01-3'] = kartu_nama(150, 60, '李美美', 200, 100)
A['A01-4'] = lantai() + jalur('M16 200 Q150 190 284 200', 't') + matahari(230, 70, 22) + garis((190, 118), (270, 118), k='t') + orang(110, tinggi=160, jenis='pria', baju='h', tangan=LAMBAI)
A['A01-5'] = (lantai() + orang(95, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, 18), (48, 4)]})
              + kartu_nama(205, 70, '陳', 130, 80))

# A02 — asal & bahasa
A['A02-1'] = lantai() + orang(90, tinggi=160, jenis='pria', wajah='kaget') + gelembung(205, 70, 140, 70, teks(205, 82, '你好！', 34), (-1, 1))
A['A02-2'] = lantai() + orang(90, tinggi=155, jenis='wanita', wajah='kaget', baju='a') + gelembung(205, 70, 140, 70, teks(205, 82, 'Hello!', 30, angka=True), (-1, 1))
A['A02-3'] = lantai() + orang(110, tinggi=160, jenis='pria', tangan={'ka': [(16, -8), (22, -40)]}) + bendera_taiwan(146, 24, 126, 84)

# A03 — keluarga
A['A03-1'] = (kotak(40, 186, 220, 10, 'h') + garis((40, 196), (40, 210)) + garis((260, 196), (260, 210))
              + bingkai(150, 34, 120, 140, orang(150, kaki=174, tinggi=120, jenis='wanita', baju='a')))
A['A03-2'] = keluarga('adik_lk')
A['A03-3'] = keluarga('kakak_pr')
A['A03-4'] = keluarga('ibu')
A['A03-5'] = (lantai() + orang(150, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 30), (40, 54)], 'ka': [(20, 30), (40, 54)]})
              + orang(78, tinggi=90, jenis='gadis', tangan={'ka': [(8, -2), (20, -8)]}) + orang(222, tinggi=90, jenis='laki', baju='a', tangan={'ki': [(8, -2), (20, -8)]}))

# A04 — jumlah anggota keluarga
A['A04-1'] = (lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', tangan={'ki': [(20, 30), (40, 56)], 'ka': [(20, 30), (40, 56)]})
              + orang(86, tinggi=92, jenis='laki', tangan={'ka': [(8, -2), (18, -10)]}) + orang(214, tinggi=92, jenis='gadis', baju='h', tangan={'ki': [(8, -2), (18, -10)]}))
A['A04-2'] = lantai() + orang(70, tinggi=100, jenis='laki', baju='h') + orang(150, tinggi=92, jenis='gadis') + orang(230, tinggi=100, jenis='laki', baju='a')
A['A04-3'] = (lantai() + orang(150, tinggi=165, jenis='pria', baju='a', tangan={'ki': [(20, 30), (40, 56)], 'ka': [(20, 30), (40, 56)]})
              + orang(84, tinggi=92, jenis='gadis', tangan={'ka': [(8, -2), (18, -10)]}) + orang(216, tinggi=92, jenis='gadis', baju='h', tangan={'ki': [(8, -2), (18, -10)]}))
A['A04-4'] = lantai() + orang(70, tinggi=150, jenis='wanita', baju='a') + orang(150, tinggi=88, jenis='laki', baju='h') + orang(230, tinggi=150, jenis='wanita', baju='a')
A['A04-5'] = (lantai() + orang(120, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 30), (40, 56)]})
              + orang(190, tinggi=92, jenis='gadis', baju='h', tangan={'ki': [(8, -2), (18, -10)]}))

# A05 — tanggal, umur
A['A05-1'] = kalender_bulan(150, 40, 5, 3, 150, 150) + kue_ultah(235, 196, s=.4)
A['A05-2'] = kue_ultah(150, 192, '18', 1.1)
A['A05-3'] = lantai() + orang(95, tinggi=165, jenis='pria', baju='h', wajah='senyum') + meja(210, 150, 120) + kue_ultah(210, 150, '40', .7)
A['A05-4'] = lantai() + orang(90, tinggi=100, jenis='gadis', baju='a', wajah='senyum') + meja(200, 150, 120) + kue_ultah(200, 150, '5', .6)
A['A05-5'] = kalender_bulan(150, 40, 10, 10, 150, 150)

# A06 — hobi
A['A06-1'] = lantai() + orang(100, tinggi=160, jenis='pria', wajah='nyanyi', tangan={'ka': [(12, 30), (-8, -8)]}) + mikrofon(132, 62) + not_musik(190, 60) + not_musik(230, 100)
A['A06-2'] = (lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(24, -20), (36, -56)]},
                              kaki_pose={'ki': (-8, 0), 'ka': (30, -26)}) + jalur('M96 70 q-10 10 0 20 M204 70 q10 10 0 20', 't'))
A['A06-3'] = (lantai() + orang(80, tinggi=110, jenis='laki', baju='h', kaki_pose={'ki': (-12, 0), 'ka': (26, -14)}) + bola(150, 186, 14)
              + orang(225, tinggi=105, jenis='gadis', baju='a', tangan={'ki': [(20, -6), (30, -30)], 'ka': [(20, -6), (30, -30)]}))
A['A06-4'] = (lantai() + tv(250, 150, 70) + meja(250, 150, 70) + sofa(115) + orang(110, tinggi=150, jenis='pria', wajah='lelah', duduk=150, baju='a',
                                                                                    tangan={'ki': [(4, 30), (-2, 44)], 'ka': [(4, 30), (-2, 44)]}) + bola(40, 188, 12))
A['A06-5'] = lantai() + kuda_gambar(210) + orang(105, tinggi=100, jenis='gadis', baju='a', tangan={'ka': [(20, -4), (46, -14)]}) + garis((166, 90), (180, 80), lebar=3)

# A07 — rupa
A['A07-1'] = lantai() + orang(150, tinggi=170, jenis='pria', badan=.62, baju='p')
A['A07-2'] = (lantai() + orang(110, tinggi=165, jenis='pria', kacamata=True, baju='h') + orang(200, tinggi=100, jenis='laki', kacamata=True, baju='h'))
A['A07-3'] = lantai() + orang(115, tinggi=182, jenis='wanita', baju='a') + orang(205, tinggi=128, jenis='pria', baju='p')
A['A07-4'] = (lantai() + orang(105, tinggi=160, jenis='pria', baju='h') + orang(195, tinggi=160, jenis='pria', baju='a')
              + jalur('M60 40 L240 40', 't') + garis((60, 34), (60, 46), k='t') + garis((240, 34), (240, 46), k='t'))

# A08 — tempat tinggal
A['A08-1'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(125, tinggi=145, jenis='wanita', baju='a') + orang(178, tinggi=150, jenis='pria', baju='h')
A['A08-2'] = lantai_kamar() + jendela(150, 40, 70, 50) + ranjang(95, 200, 130) + orang(215, tinggi=145, jenis='pria', baju='a')
A['A08-3'] = lantai() + gedung(120, tingkat=7, sorot=5) + panah(222, 200 - 5 * 24 + 11, 172, 200 - 5 * 24 + 11, 4) + teks(252, 200 - 5 * 24 + 20, '5F', 26, angka=True)
A['A08-4'] = lantai() + gedung(120, tingkat=10, sorot=10, tt=18) + panah(222, 200 - 10 * 18 + 9, 172, 200 - 10 * 18 + 9, 4) + teks(256, 200 - 10 * 18 + 18, '10F', 24, angka=True)
A['A08-5'] = lantai() + rumah(95) + pohon(250) + matahari(250, 40, 14) + orang(190, tinggi=140, jenis='wanita', baju='a')

# A09 — letak benda
A['A09-1'] = lantai() + meja(150, 128, 160) + tv(150, 128, 116)
A['A09-2'] = lantai() + meja(110, 120, 140) + kursi(242)
A['A09-3'] = (garis((16, 150), (284, 150), k='t') + kotak(70, 40, 160, 60, 'h', 6) + bentuk((78, 100), (222, 100), (262, 160), (38, 160), k='p')
              + bentuk((60, 128), (240, 128), (262, 160), (38, 160), k='a') + elips(115, 110, 26, 8) + elips(185, 110, 26, 8)
              + kotak(38, 160, 224, 12, 'h') + kotak(95, 178, 110, 30, 'h') + tv(150, 178, 100))
A['A09-4'] = lantai() + meja(150, 110, 200) + bola(125, 186, 13) + bola(170, 186, 13)
A['A09-5'] = (lantai() + kursi(186, 176, arah=-1, s=.75) + orang(120, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(22, 14), (46, 18)]}))

# A10 — jam
A['A10-1'] = jam_dinding(150, 110, 88, 7, 30)
A['A10-2'] = jam_dinding(150, 110, 88, 10, 0)
A['A10-3'] = (lantai_kamar() + jendela(215, 36, 60, 46) + bulan_bintang(212, 58, .45) + ranjang(110, 200, 170)
              + bulat(56, 136, 13) + muka(56, 136, 13, 'tidur') + jalur('M42 131 q2 -18 16 -18 q12 0 13 14', 'h') + jam_dinding(230, 150, 30, 11, 0) + teks(92, 110, 'z z', 18, angka=True))
A['A10-4'] = weker(120, 110, 70, 6, 0) + matahari(245, 60, 18)
A['A10-5'] = jam_dinding(150, 110, 88, 12, 30)

# A11 — hari
A['A11-1'] = kalender_minggu(150, 70, 5, 6, 280).replace('>日<', '>日<')   # urutan diganti di bawah
A['A11-2'] = lantai() + bioskop(200) + orang(70, tinggi=140, jenis='wanita', baju='a') + orang(120, tinggi=150, jenis='pria', baju='h')
A['A11-3'] = kalender_minggu(150, 70, 2, 3, 280)
A['A11-4'] = kalender_minggu(150, 70, 1, 0, 280)
A['A11-5'] = lantai() + pohon(215) + pohon(270, s=.8) + bangku(240) + jalan_kaki(70, 'wanita', 140, 'a') + jalan_kaki(125, 'pria', 150, 'h') + panah(150, 60, 196, 60, 4)

# A12 — sekolah
A['A12-1'] = ruang_kelas(guru=True)
A['A12-2'] = (lantai() + papan_tulis(150, 16, 170, 56) + murid_belakang(60, 200, 100) + meja_kelas(60) + murid_belakang(150, 200, 100, 'gadis') + meja_kelas(150)
              + murid_belakang(240, 200, 100) + meja_kelas(240))
A['A12-3'] = lantai() + orang(150, tinggi=140, jenis='laki', baju='a', tangan={'ka': [(10, 20), (-6, 34)]}) + buku(170, 146, 28, 38, 'h') + tas_punggung(116, 100)
A['A12-4'] = (lantai() + papan_tulis(95, 30, 150, 80) + mimbar(225) + orang(225, kaki=200, tinggi=175, jenis='wanita', baju='a', tangan={'ki': [(14, -14), (40, -34)]}, kacamata=True)
              + mimbar(225))
A['A12-5'] = (lantai() + pintu(60, 200, 140, 64) + lonceng(220, 58, .7) + tas_punggung(128, 116, .8) + jalan_kaki(150, 'laki', 110, 'h')
              + tas_punggung(200, 118, .8) + jalan_kaki(222, 'gadis', 105, 'a'))

# A13 — alat tulis
A['A13-1'] = pulpen(150, 90, 150, -8) + pulpen(150, 140, 150, -8)
A['A13-2'] = lantai() + meja(150, 130, 200) + komputer(170, 130, 96) + orang(75, tinggi=150, jenis='wanita', baju='a', duduk=140, tangan={'ka': [(26, 4), (56, -2)]})
A['A13-3'] = lantai() + meja(150, 150, 240) + kertas(80, 118, 44, 56, -8) + kertas(150, 116, 44, 56, 4) + kertas(220, 118, 44, 56, -3)
A['A13-4'] = lantai(186, 60, 240) + buku_tumpuk(150, 186, 3, 130, 30)
A['A13-5'] = lantai() + papan_tulis(210, 28, 140, 70) + meja_kelas(95) + orang(95, tinggi=125, jenis='laki', baju='a', duduk=150, tangan=ANGKAT, wajah='senyum')

# A14 — ujian
A['A14-1'] = (lantai() + meja(150, 140, 200) + kertas(185, 118, 50, 40, 0) + orang(110, tinggi=150, jenis='pria', baju='a', duduk=146, wajah='sedih', tangan=TA)
              + keringat(140, 60) + keringat(78, 70, .8))
A['A14-2'] = kertas(150, 110, 150, 170, 0) + teks(150, 140, '字', 88) + silang(150, 110, 58, 10)
A['A14-3'] = (lantai() + orang(110, tinggi=150, jenis='gadis', baju='a', wajah='puas', tangan={'ka': [(24, -6), (44, -30)]}) + kertas(205, 80, 70, 90, 6)
              + centang(195, 62) + centang(200, 92) + centang(205, 118, .8))
A['A14-4'] = lantai() + papan_tulis(95, 30, 150, 70) + orang(70, tinggi=160, jenis='wanita', baju='a') + orang(210, tinggi=125, jenis='laki', baju='h', tangan=ANGKAT)

# A15 — minuman
A['A15-1'] = lantai() + gelas(125, 200, 'susu', 1.6) + kotak_susu(210, 200, 1.1)
A['A15-2'] = lantai() + gelas(150, 200, 'air', 2, es=True)
A['A15-3'] = lantai() + orang(130, tinggi=165, jenis='pria', baju='a', wajah='puas', tangan={'ka': [(14, 26), (-4, -6)]}) + cangkir(160, 66, .55)
A['A15-4'] = lantai() + teko(110, 200, 1.2) + cangkir(220, 196, 1.0)
A['A15-5'] = lantai() + gelas(150, 196, 'air', 1.8, es=True) + larangan(150, 130, 70)

# A16 — makanan
A['A16-1'] = lantai() + jendela(230, 30, 80, 64) + matahari(230, 62, 10) + meja(130, 150, 200) + piring(130, 144, 70, telur_ceplok(130, 142, .9))
A['A16-2'] = lantai() + jendela(230, 30, 80, 64) + bulan_bintang(222, 60, .5) + meja(130, 150, 200) + piring(130, 144, 76, ikan(128, 136, .9))
A['A16-3'] = (lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='puas', badan=1.35) + elips(150, 118, 30, 24, 'a')
              + garis((122, 90), (112, 112), (140, 120), lebar=4.6) + garis((178, 90), (188, 112), (160, 120), lebar=4.6)
              + meja(150, 150, 260) + piring(55, 146, 36) + piring(245, 146, 36) + elips(150, 144, 22, 6, 'p'))
A['A16-4'] = lantai() + jam_dinding(235, 54, 34, 12, 0) + meja(125, 150, 200) + piring(125, 144, 76, ikan(123, 136, .9))
A['A16-5'] = lantai() + meja(150, 150, 240) + piring(150, 144, 60) + orang(150, tinggi=150, jenis='laki', baju='a', wajah='lapar', tangan={'ki': [(0, 24), (-10, 44)], 'ka': [(0, 24), (-10, 44)]}) + piring(150, 144, 60)

# A17 — restoran
A['A17-1'] = mangkuk_mi(150, 100, 1.1)
A['A17-2'] = (lantai() + meja(150, 150, 240) + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='senyum', tangan={'ka': [(20, 20), (4, -6)]})
              + garis((158, 72), (190, 128), lebar=3) + garis((164, 70), (196, 126), lebar=3) + mangkuk_mi(160, 128, .45, sumpit=False))
A['A17-3'] = piring(150, 160, 110, bakpao(110, 160, 1.3) + bakpao(190, 160, 1.3))
A['A17-4'] = (lantai() + kotak(170, 40, 114, 160, 'p') + kotak(200, 90, 56, 110, 'h') + kotak(176, 48, 102, 32, 'h') + mangkuk_mi(227, 62, .18, sumpit=False, uap=False)
              + orang(50, tinggi=140, jenis='wanita', baju='a') + orang(100, tinggi=155, jenis='pria', baju='h') + orang(148, tinggi=110, jenis='laki', baju='p'))
A['A17-5'] = piring(150, 160, 110, roti(150, 156, 1.2))

# A18 — belanja
A['A18-1'] = struk(150, 30, '350', 140, 170)
A['A18-2'] = label_harga(150, 78, '120', 180, 76)
A['A18-3'] = lantai() + toko(95) + orang(222, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(8, 30), (4, 50)], 'ka': [(8, 30), (4, 50)]}) + tas_belanja(196, 190, .8) + tas_belanja(250, 190, .8)
A['A18-4'] = label_harga(150, 78, '300', 180, 76)
A['A18-5'] = (lantai() + orang(95, tinggi=160, jenis='pria', baju='a', wajah='sedih', tangan={'ka': [(20, 16), (40, 0)]}) + keringat(118, 44) + dompet(200, 92, .9)
              + bulat(230, 142, 7, 'p'))

# A19 — pakaian (soal warna diberi warna)
A['A19-1'] = lantai() + sepatu(110, 196, 1.5) + sepatu(210, 196, 1.5)
A['A19-2'] = kaos(150, 110, 1.9, 'm')
A['A19-3'] = (lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(160, 198, 1.9)
              + jalur('M54 150 l-14 -6 M52 170 l-16 0 M56 188 l-14 6', 'g'))   # tumit menyembul keluar dari sepatu yang kecil
A['A19-4'] = lantai() + orang(150, tinggi=175, jenis='wanita', baju='m')
A['A19-5'] = (lantai() + sepatu(160, 198, 2.5) + jalur('M84 30 L84 150 Q84 178 104 180 L158 182 Q170 182 170 172 L150 150 L112 138 L112 30', 'p')
              + panah(190, 165, 232, 165, 3) + panah(232, 165, 190, 165, 3))   # celah di ujung sepatu yang kebesaran

# A20 — kendaraan
A['A20-1'] = lantai() + kereta(160, 196, 250) + orang(40, tinggi=130, jenis='wanita', baju='a') + tas_punggung(58, 110, .8)
A['A20-2'] = awan(60, 50, .6) + awan(240, 160, .5) + pesawat(150, 110, 1.1)
A['A20-3'] = lantai() + kotak(170, 60, 114, 140, 'p') + bentuk((160, 60), (227, 20), (294, 60), k='h') + lonceng(227, 50, .22) + pintu(227, 200, 70, 40) + jalan_kaki(90, 'laki', 110, 'h') + tas_punggung(70, 112, .7)
A['A20-4'] = lantai() + mobil(150, 200, 230, taksi=True, k='a')
A['A20-5'] = lantai() + mobil(80, 200, 140) + mobil(225, 200, 140, k='a')

# A21 — arah
A['A21-1'] = lantai() + stasiun(70, 200, 110, 80) + orang(215, tinggi=150, jenis='pria', baju='a', tangan={'ki': [(20, -10), (48, -18)]}) + panah(170, 40, 120, 40, 5)
A['A21-2'] = lantai() + stasiun(230, 200, 110, 80) + orang(85, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(20, -10), (48, -18)]}) + panah(130, 40, 180, 40, 5)
A['A21-3'] = (lantai() + jalan_kaki(90, 'wanita', 150, 'a') + jam_dinding(215, 90, 56, 0, 0, False)
              + jalur(f'M215 90 L215 34 A56 56 0 0 1 {f(215 + 56 * math.sin(math.radians(30)))} {f(90 - 56 * math.cos(math.radians(30)))} Z', 'a'))
A['A21-4'] = lantai() + pohon(225) + pohon(275, s=.8) + bangku(240) + orang(80, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, -10), (48, -18)]}) + panah(130, 40, 180, 40, 5)
A['A21-5'] = lantai() + rambu_halte(180) + bangku(90, 200, 90)

# A22 — tubuh & sakit
A['A22-1'] = lantai() + orang(150, tinggi=165, jenis='pria', wajah='sakit', baju='a', tangan=TA) + jalur('M120 22 l-8 -8 M150 16 l0 -10 M180 22 l8 -8', 'g')
A['A22-2'] = (lantai() + kursi_depan(150, 140) + orang(150, tinggi=150, jenis='wanita', duduk=140, wajah='sakit', baju='a', tangan={'ki': [(4, 40), (-8, 60)], 'ka': [(4, 40), (4, 60)]})
              + jalur('M112 180 l-12 -4 M110 192 l-14 2 M122 172 l-8 -10', 'g'))
A['A22-3'] = lantai() + orang(130, tinggi=165, jenis='pria', wajah='sakit', baju='a', tangan={'ka': [(14, 20), (-4, -6)]}) + kertas(140, 60, 22, 18, 10) + jalur('M170 50 l20 -8 M172 60 l24 0 M170 70 l20 8', 'g')
A['A22-4'] = (lantai() + orang(150, tinggi=165, jenis='pria', wajah='sakit', baju='a', tangan={'ki': [(14, 20), (40, 24)], 'ka': [(12, 20), (-30, 26)]})
              + kotak(98, 88, 16, 14, 'a', 3) + jalur('M86 80 l-10 -8 M84 96 l-12 0 M90 110 l-8 8', 'g'))
A['A22-5'] = (lantai() + kursi_depan(150, 140) + orang(150, tinggi=150, jenis='pria', duduk=140, wajah='lelah', baju='a', tangan={'ki': [(2, 40), (-4, 60)], 'ka': [(2, 40), (-4, 60)]})
              + keringat(178, 30) + keringat(122, 38, .8))

# A23 — dokter & obat
A['A23-1'] = lantai() + orang(120, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(14, 26), (-4, -6)]}) + pil(146, 58, .6) + gelas(215, 196, 'air', 1.2)
A['A23-2'] = (lantai() + orang(90, tinggi=165, jenis='wanita', baju='p', kacamata=True, tangan={'ka': [(20, 20), (46, 10)]}) + jalur('M80 70 q10 22 20 0', 't')
              + botol_obat(148, 108, .7) + orang(225, tinggi=150, jenis='pria', baju='a', wajah='sakit', tangan={'ki': [(20, 20), (40, 10)]}))
A['A23-3'] = lantai_kamar() + ranjang(150, 200, 220) + bulat(60, 128, 13) + muka(60, 128, 13, 'tidur') + jalur('M46 123 q2 -18 16 -18 q12 0 13 14', 'h') + teks(96, 104, 'z z', 18, angka=True)
A['A23-4'] = lantai() + rumah_sakit(200) + jalan_kaki(75, 'pria', 150, 'a', 'sakit')
A['A23-5'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', wajah=None) + muka(110, 200 - 160 + 13.6, 13.6, 'senyum') + jam_pasir(215, 110, 1.4)

# A24 — cuaca
A['A24-1'] = lantai() + awan(150, 30, 1.2, 'a') + hujan(150, 58, 240, 60, 11) + orang(150, tinggi=145, jenis='wanita', baju='h', tangan={'ka': [(8, -6), (-14, -30)]}) + payung(150, 72, 58)
A['A24-2'] = (lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='sedih', tangan={'ki': [(20, 12), (-10, 26)], 'ka': [(20, 12), (-10, 26)]})
              + kotak(134, 68, 32, 10, 'a', 4) + kotak(150, 72, 10, 28, 'a', 3) + jalur('M110 90 l-8 4 l8 4 l-8 4 M190 90 l8 4 l-8 4 l8 4', 'g')
              + salju(60, 60, 10) + salju(240, 50, 8) + salju(250, 120, 9) + salju(50, 130, 7) + salju(92, 30, 6) + salju(212, 150, 6))
A['A24-3'] = lantai() + gunung(150, 200, 260, 150, salju=False) + bunga(70, 150) + bunga(110, 160) + bunga(190, 158) + bunga(230, 150) + bunga(150, 168)
A['A24-4'] = lantai() + matahari(60, 50, 22, 'h') + orang(170, tinggi=160, jenis='pria', baju='p', wajah='lelah', tangan={'ka': [(14, -6), (10, -26)]}) + keringat(145, 44) + keringat(196, 52) + keringat(150, 90, .8)
A['A24-5'] = (lantai() + gunung(120, 200, 220, 140) + angin(170, 60, .9)
              + kotak(245, 150, 8, 50, 'h') + jalur('M249 150 Q262 110 286 104 Q270 128 260 150 Z', 'p'))

# A25 — telepon & sopan santun
A['A25-1'] = dua_panel(orang_ponsel(75, 'laki', 140, baju='h') + sinyal(108, 70),
                       orang_ponsel(225, 'wanita', 160, baju='a').replace('class="h"', 'class="h"') + sinyal(192, 70, -1))
A['A25-2'] = (ponsel(150, 110, 3.2, 'p') + kotak(128, 80, 44, 60, 'h') + bentuk((142, 96), (142, 124), (164, 110), k='n'))
A['A25-3'] = lantai() + orang(90, tinggi=155, jenis='wanita', baju='a', tangan=LAMBAI) + orang(210, tinggi=160, jenis='pria', baju='h', tangan={'ki': [(14, -30), (6, -58)]})
A['A25-4'] = dua_panel(orang_ponsel(75, 'wanita', 150, baju='h') + sinyal(108, 70), orang_ponsel(225, 'wanita', 150, baju='a') + sinyal(192, 70, -1))
A['A25-5'] = (lantai() + orang(95, tinggi=160, jenis='pria', baju='a', wajah='sedih', tangan={'ki': [(4, 18), (-20, 12)], 'ka': [(4, 18), (-20, 12)]}) + keringat(122, 46)
              + orang(215, tinggi=150, jenis='wanita', baju='h', wajah='kaget') + buku(175, 200, 34, 12, 'h'))

# A25-1 panel kanan = ibu (rambut sanggul abu), kiri = anak
A['A25-1'] = dua_panel(orang_ponsel(75, 'laki', 130, baju='h') + sinyal(108, 70),
                       orang(225, tinggi=160, jenis='wanita', baju='a', rambut='uban', tangan={'ki': [(12, 16), (-6, -22)]})
                       + ponsel(225 - sendi(225, 200, 160, 'wanita')['lb'] / 2 + 2, sendi(225, 200, 160, 'wanita')['bahu'] - 23, .75) + sinyal(192, 70, -1))
# A11-1: kalender Senin-pertama agar "besok" (Minggu) ada di kanan "hari ini" (Sabtu)
A['A11-1'] = kalender_senin(150, 70, 5, 6)
A['A11-3'] = kalender_senin(150, 70, 1, 2)
A['A11-4'] = kalender_minggu(150, 70, 1, 0, 280)
