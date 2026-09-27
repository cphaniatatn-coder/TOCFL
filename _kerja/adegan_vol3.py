"""Adegan ilustrasi 聽力 Part 1 — Volume 3 (C01–C67). ID = <modul>-<n> (listen_pic ke-n, urut isi → soal → bank)."""
from svg_adegan import *
from adegan_vol2 import potret, pelari, tunjuk_ke, burung, jam_kecil, rambut_terurai, garis_jatuh, pegang_perut, piala, kembang_api, meja_bundar

A = {}


# ================= komponen Volume 3 =================
def kulkas(x, lantai_y=LANTAI, w=70, h=150):
    return kotak(x - w / 2, lantai_y - h, w, h, 'p', 6) + garis((x - w / 2, lantai_y - h + 50), (x + w / 2, lantai_y - h + 50)) + garis((x + w / 2 - 12, lantai_y - h + 16), (x + w / 2 - 12, lantai_y - h + 38), lebar=4) + garis((x + w / 2 - 12, lantai_y - h + 64), (x + w / 2 - 12, lantai_y - h + 100), lebar=4)


def dapur(x_kompor=190):
    return lantai() + kulkas(260) + kompor(x_kompor, 130, 110) + api(x_kompor, 128, .7) + wajan(x_kompor, 112, .9)


def baju_berserakan():
    return (kaos(70, 186, .35, 'a') + kaos(230, 190, .3, 'p') + bentuk((120, 196), (160, 190), (170, 198), k='h') + buku(190, 198, 30, 10, 'h')
            + kertas(40, 190, 22, 16, 30) + kertas(262, 150, 20, 14, -20) + jalur('M150 150 q10 -10 20 0 M60 140 q8 -8 16 0', 'g'))


def noda(x, y, r=10):
    return jalur(f'M{f(x - r)} {f(y)} q{f(r * .4)} {f(-r * 1.2)} {f(r * 1.1)} {f(-r * .6)} q{f(r * .9)} {f(r * .2)} {f(r * .5)} {f(r * 1.1)} q{f(-r * .5)} {f(r * .8)} {f(-r * 1.2)} {f(r * .4)} Z', 'h')


def kantong_sampah(x, bawah, s=1.0):
    return (jalur(f'M{f(x - 34 * s)} {f(bawah)} Q{f(x - 44 * s)} {f(bawah - 50 * s)} {f(x - 10 * s)} {f(bawah - 64 * s)} L{f(x + 10 * s)} {f(bawah - 64 * s)} Q{f(x + 44 * s)} {f(bawah - 50 * s)} {f(x + 34 * s)} {f(bawah)} Z', 'h')
            + jalur(f'M{f(x - 10 * s)} {f(bawah - 64 * s)} l-6 {f(-14 * s)} M{f(x + 10 * s)} {f(bawah - 64 * s)} l6 {f(-14 * s)}', 'g'))


def celana(x, y, s=1.0, k='a', lubang=False):
    o = jalur(f'M{f(x - 40 * s)} {f(y)} L{f(x + 40 * s)} {f(y)} L{f(x + 48 * s)} {f(y + 150 * s)} L{f(x + 8 * s)} {f(y + 150 * s)} L{f(x)} {f(y + 50 * s)} L{f(x - 8 * s)} {f(y + 150 * s)} L{f(x - 48 * s)} {f(y + 150 * s)} Z', k)
    o += garis((x - 40 * s, y + 14 * s), (x + 40 * s, y + 14 * s), k='t')
    if lubang:
        o += elips(x - 26 * s, y + 100 * s, 11 * s, 9 * s, 'p') + jalur(f'M{f(x - 37 * s)} {f(y + 100 * s)} l-4 -3 M{f(x - 15 * s)} {f(y + 100 * s)} l4 -3', 't')
    return o


def mesin_cuci(x, lantai_y=LANTAI, w=110, h=120, rusak=False):
    o = kotak(x - w / 2, lantai_y - h, w, h, 'p', 8) + kotak(x - w / 2, lantai_y - h, w, 24, 'a', 8) + bulat(x + w / 2 - 16, lantai_y - h + 12, 5, 'h')
    o += bulat(x, lantai_y - h / 2 + 8, 36, 'p') + bulat(x, lantai_y - h / 2 + 8, 28, 'a') + jalur(f'M{f(x - 20)} {f(lantai_y - h / 2 + 14)} q10 -10 20 0 t20 0', 'w')
    if rusak:
        o += awan(x + 30, lantai_y - h - 24, .35, 'a') + awan(x - 20, lantai_y - h - 36, .28, 'a') + silang(x, lantai_y - h / 2 + 8, 22, 6)
    return o


def jemuran(y=60):
    o = garis((30, y), (270, y), lebar=3) + garis((30, y), (30, LANTAI), lebar=4) + garis((270, y), (270, LANTAI), lebar=4)
    return o + kaos(90, y + 50, .5, 'p') + celana(170, y + 4, .35, 'a') + kaos(235, y + 50, .5, 'a') + ''.join(garis((x, y - 4), (x, y + 8), lebar=3) for x in (80, 100, 158, 182, 225, 245))


def denah_kamar(n=3, w=260, h=170):
    """Denah rumah tampak atas dengan n kamar tidur (tempat tidur) + ruang tamu (sofa)."""
    o = kotak(150 - w / 2, 20, w, h, 'p')
    lw = w / n
    for i in range(n):
        x0 = 150 - w / 2 + i * lw
        if i:
            o += garis((x0, 20), (x0, 20 + h * .55), lebar=3)
        o += kotak(x0 + lw / 2 - 18, 34, 36, 50, 'a', 4) + kotak(x0 + lw / 2 - 14, 38, 28, 12, 'p', 3)
    o += garis((150 - w / 2, 20 + h * .55), (150 + w / 2, 20 + h * .55), lebar=3)
    o += kotak(150 - 50, 20 + h * .7, 100, 26, 'h', 6)
    return o


def pagar(x1, x2, y=LANTAI, t=40):
    return garis((x1, y - t * .7), (x2, y - t * .7), lebar=3) + ''.join(garis((x, y), (x, y - t), lebar=4) for x in range(int(x1), int(x2) + 1, 16))


def rumah_2lantai(x, lantai_y=LANTAI, w=150):
    o = bentuk((x - w / 2 - 10, lantai_y - 150), (x, lantai_y - 190), (x + w / 2 + 10, lantai_y - 150), k='h') + kotak(x - w / 2, lantai_y - 150, w, 150, 'p')
    o += garis((x - w / 2, lantai_y - 76), (x + w / 2, lantai_y - 76), lebar=3)
    return o + jendela(x - 36, lantai_y - 136, 36, 30) + jendela(x + 36, lantai_y - 136, 36, 30) + jendela(x - 36, lantai_y - 60, 36, 30) + pintu(x + 36, lantai_y, 64, 36)


def gembok(x, y, s=1.0):
    return (jalur(f'M{f(x - 16 * s)} {f(y)} L{f(x - 16 * s)} {f(y - 18 * s)} A{f(16 * s)} {f(16 * s)} 0 0 1 {f(x + 16 * s)} {f(y - 18 * s)} L{f(x + 16 * s)} {f(y)}', 'g', 6 * s)
            + kotak(x - 24 * s, y, 48 * s, 38 * s, 'h', 5) + bulat(x, y + 16 * s, 5 * s, 'n') + kotak(x - 2 * s, y + 18 * s, 4 * s, 10 * s, 'n'))


def kunci(x, y, s=1.0, sudut=0):
    return (f'<g transform="rotate({sudut} {f(x)} {f(y)})">' + bulat(x - 26 * s, y, 13 * s, 'a') + bulat(x - 26 * s, y, 5 * s, 'n')
            + kotak(x - 14 * s, y - 4 * s, 44 * s, 8 * s, 'h', 2) + kotak(x + 18 * s, y + 4 * s, 5 * s, 8 * s, 'h') + kotak(x + 26 * s, y + 4 * s, 5 * s, 6 * s, 'h') + '</g>')


def pintu_gembok(x=150):
    return lantai() + pintu(x, 200, 170, 90) + gembok(x + 30, 110, .9)


def sikat_gigi(x, y, s=1.0, sudut=-20):
    return (f'<g transform="rotate({sudut} {f(x)} {f(y)})">' + kotak(x - 70 * s, y - 6 * s, 110 * s, 12 * s, 'a', 6) + kotak(x + 28 * s, y - 16 * s, 40 * s, 12 * s, 'h', 2)
            + ''.join(garis((x + 32 * s + i * 7 * s, y - 16 * s), (x + 32 * s + i * 7 * s, y - 28 * s), lebar=3) for i in range(5)) + '</g>')


def sabun(x, y, s=1.0):
    return kotak(x - 30 * s, y - 16 * s, 60 * s, 32 * s, 'p', 12 * s) + ''.join(bulat(x + dx * s, y - 24 * s - dy * s, r * s, 'p') for dx, dy, r in ((-18, 4, 5), (-4, 10, 7), (14, 2, 4)))


def botol_sampo(x, bawah, s=1.0):
    return (jalur(f'M{f(x - 28 * s)} {f(bawah)} L{f(x - 28 * s)} {f(bawah - 90 * s)} Q{f(x)} {f(bawah - 104 * s)} {f(x + 28 * s)} {f(bawah - 90 * s)} L{f(x + 28 * s)} {f(bawah)} Z', 'p')
            + kotak(x - 10 * s, bawah - 118 * s, 20 * s, 18 * s, 'h', 3) + kotak(x - 28 * s, bawah - 70 * s, 56 * s, 40 * s, 'a')
            + jalur(f'M{f(x - 16 * s)} {f(bawah - 40 * s)} q{f(4 * s)} {f(-20 * s)} {f(16 * s)} {f(-24 * s)} q{f(12 * s)} {f(4 * s)} {f(16 * s)} {f(24 * s)}', 'w'))


def handuk(x, y, w=50, h=70, k='a'):
    return kotak(x - w / 2, y, w, h, k, 3) + garis((x - w / 2, y + h - 12), (x + w / 2, y + h - 12), k='w' if k == 'h' else 't')


def bau(x, y):
    return jalur(f'M{f(x)} {f(y)} q-8 -10 0 -20 q8 -10 0 -20 M{f(x + 14)} {f(y + 4)} q-8 -10 0 -20 q8 -10 0 -20', 'g')


def nyamuk(x, y, s=1.0):
    return (elips(x, y, 9 * s, 4 * s, 'h') + elips(x - 3 * s, y - 7 * s, 7 * s, 3.5 * s, 'p') + elips(x + 4 * s, y - 7 * s, 7 * s, 3.5 * s, 'p')
            + garis((x + 8 * s, y), (x + 18 * s, y + 2 * s), lebar=1.8) + ''.join(garis((x - 6 * s + i * 5 * s, y + 3 * s), (x - 9 * s + i * 5 * s, y + 12 * s), lebar=1.5) for i in range(3)))


def pengeras_suara(x, y, s=1.0):
    return kotak(x - 26 * s, y - 40 * s, 52 * s, 80 * s, 'h', 6) + bulat(x, y - 14 * s, 11 * s, 'a') + bulat(x, y + 18 * s, 16 * s, 'a') + jalur(f'M{f(x + 34 * s)} {f(y - 20 * s)} q14 20 0 40 M{f(x + 46 * s)} {f(y - 32 * s)} q24 32 0 64', 'g')


def asap_kota():
    return awan(80, 40, .5, 'a') + awan(170, 30, .45, 'a') + garis((60, 60), (60, 90), k='t')


def sawah(y=150):
    o = bentuk((16, y), (284, y), (284, 204), (16, 204), k='a')
    for i in range(12):
        o += jalur(f'M{24 + i * 22} {y + 40} l-4 -14 M{24 + i * 22} {y + 40} l0 -18 M{24 + i * 22} {y + 40} l4 -14', 'g')
    return o


def grafik(nilai, x0=40, y0=190, w=220, h=150, label=None):
    n = len(nilai)
    bw = w / n * .6
    o = garis((x0, y0 - h), (x0, y0), (x0 + w, y0), lebar=3)
    m = max(nilai)
    for i, v in enumerate(nilai):
        bh = h * .9 * v / m
        o += kotak(x0 + (i + .2) * w / n, y0 - bh, bw, bh, 'a' if i < n - 1 else 'h')
    return o


def tabel_tinggi(x=150):
    o = kotak(x - 110, 20, 40, 180, 'p') + ''.join(garis((x - 110, 30 + i * 20), (x - 96 + (i % 2) * 8, 30 + i * 20), k='t') for i in range(9))
    return o + orang(x - 40, tinggi=80, jenis='laki', baju='a') + orang(x + 20, tinggi=120, jenis='laki', baju='a') + orang(x + 85, tinggi=170, jenis='pria', baju='a') + panah(x - 40, 60, x + 70, 26, 4)


def foto_bayi(x=150, y=30):
    return (kotak(x - 90, y, 180, 150, 'h', 5) + kotak(x - 82, y + 8, 164, 134, 'p')
            + elips(x, y + 100, 60, 26, 'a') + bulat(x - 36, y + 80, 20) + muka(x - 36, y + 80, 20, 'tidur') + jalur(f'M{f(x - 40)} {f(y + 62)} q4 -6 8 0', 'g')
            + kotak(x - 20, y + 84, 70, 30, 'p', 14))


# ================= C01–C12 =================
A['C01-1'] = lantai() + meja(150, 150, 220) + piring(150, 144, 50) + orang(150, tinggi=150, jenis='pria', baju='a', wajah='puas', tangan={'ki': [(4, 30), (-14, 46)], 'ka': [(4, 30), (-14, 46)]}, badan=1.25) + piring(150, 144, 50)
A['C01-2'] = dapur() + orang(95, tinggi=160, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(22, 10), (50, 4)]})
A['C01-3'] = dapur() + orang(95, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(22, 10), (50, 4)]})
A['C01-4'] = lantai() + meja(150, 150, 220) + piring(150, 144, 80) + ''.join(bulat(120 + i * 14, 140 - (i % 2) * 3, 2.2, 'h') for i in range(5)) + garpu(210, 136, 60, 10)

A['C02-1'] = kotak(16, 16, 268, 188, 'p') + ranjang(210, 200, 120) + baju_berserakan() + noda(100, 180) + noda(160, 196, 8) + kantong_sampah(40, 200, .6)
A['C02-2'] = kotak(16, 16, 268, 188, 'p') + ranjang(200, 200, 140) + baju_berserakan() + buku(120, 196, 30, 10, 'a') + buku(150, 180, 26, 8, 'h')
A['C02-3'] = lantai() + sofa(200) + orang(70, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 10), (46, 20)]})
A['C02-4'] = lantai() + meja(170, 120, 150) + buku(150, 120, 30, 20, 'a') + orang(80, tinggi=150, jenis='laki', baju='a', wajah='kaget') + silang(170, 90, 34, 8)
A['C02-5'] = kaos(150, 110, 1.9, 'p') + noda(130, 90, 14) + noda(175, 130, 11) + noda(145, 150, 8)

A['C03-1'] = lantai() + jalur('M100 60 L200 60 L210 170 L90 170 Z', 'a') + jalur('M130 160 l14 -20 l10 16 l12 -18 l8 22', 'p') + buah_apel(150, 196, .5) + buah_apel(200, 196, .45) + garis_jatuh(170, 188)
A['C03-2'] = lantai() + pintu(250, 200, 140, 60) + kantong_sampah(190, 200, .9) + orang(70, tinggi=165, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(20, 0), (48, 10)]}) + orang(130, tinggi=100, jenis='laki', baju='h')
A['C03-3'] = celana(150, 40, .95, 'a', lubang=True)
A['C03-4'] = lantai() + mesin_cuci(150, 200, 130, 130, rusak=True)
A['C03-5'] = lantai() + matahari(260, 30, 14) + jemuran(60)

A['C04-1'] = lantai() + meja(190, 130, 150) + buku_tumpuk(190, 130, 2, 50, 14) + orang(90, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(22, 16), (54, 22)]})
A['C04-2'] = denah_kamar(3)
A['C04-3'] = lantai() + pagar(16, 284) + pohon(250, s=.8) + rumah(60, 200, 90, 70) + anjing(170, 198, .8) + bola(215, 190, 9)
A['C04-4'] = lantai() + rumah_2lantai(150)
A['C04-5'] = lantai() + pagar(16, 284) + pohon(260, s=.7) + meja(150, 130, 120) + orang(70, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(20, 10), (40, 12)]}) + orang(230, tinggi=150, jenis='pria', baju='a', tangan={'ki': [(20, 10), (40, 12)]})

A['C05-1'] = pintu_gembok()
A['C05-2'] = celana(150, 30, .95, 'a') + kotak(160, 50, 40, 44, 'p', 3) + kunci(180, 72, .6, -30)
A['C05-3'] = lantai() + pintu(190, 200, 170, 90) + kunci(200, 120, .7, 0) + orang(80, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(26, 14), (60, 28)]})
A['C05-4'] = lantai() + orang(80, tinggi=110, jenis='laki', baju='h', tangan={'ka': [(20, 0), (40, -4)]}) + kunci(150, 118, .6, 0) + orang(220, tinggi=165, jenis='wanita', baju='a', rambut='uban', tangan={'ki': [(20, 10), (40, 0)]})
A['C05-5'] = pintu_gembok()

A['C06-1'] = lantai() + meja(150, 140, 220) + handuk(150, 116, 90, 24, 'a')
A['C06-2'] = sikat_gigi(150, 110, 1.4, -15)
A['C06-3'] = lantai() + kursi_depan(120, 150) + orang(120, tinggi=150, jenis='pria', baju='a', duduk=150, wajah='tawa') + gelembung(230, 60, 90, 50, bulat(215, 60, 3.5, 'h') + bulat(230, 60, 3.5, 'h') + bulat(245, 60, 3.5, 'h'), (-1, 1))
A['C06-4'] = kotak(16, 16, 268, 188, 'p') + garis((60, 50), (240, 50), lebar=5) + handuk(110, 50, 60, 90, 'a') + handuk(190, 50, 60, 90, 'h') + bentuk((40, 170), (260, 170), (250, 200), (50, 200), k='p')
A['C06-5'] = lantai() + botol_sampo(150, 196, 1.3)

A['C07-1'] = weker(150, 110, 70, 6, 0)
A['C07-2'] = (lantai_kamar() + jendela(230, 30, 60, 46) + bulan_bintang(225, 52, .45) + jam_dinding(70, 56, 30, 0, 0) + ranjang(150, 200, 180)
              + orang(210, tinggi=150, jenis='pria', baju='p', wajah='lelah'))
A['C07-3'] = lantai() + meja(150, 150, 220) + piring(110, 144, 50, telur_ceplok(110, 140, .8)) + gelas(200, 146, 'susu', .8) + jam_dinding(240, 50, 30, 8, 0) + orang(40, tinggi=150, jenis='wanita', baju='a', wajah='kaget')
A['C07-4'] = lantai_kamar() + jendela(220, 30, 60, 46) + matahari(220, 52, 9) + jam_dinding(70, 56, 28, 9, 0) + ranjang(130, 200, 180) + bulat(76, 136, 13) + muka(76, 136, 13, 'tidur') + jalur('M62 131 q2 -18 16 -18 q12 0 13 14', 'h') + teks(112, 110, 'z z', 18, angka=True)
A['C07-5'] = kalender_senin(150, 14, 5, 5) + ''.join(silang(150 - 140 + 40 * (i + .5) + 80, 62, 12, 4) for i in range(3)) + lantai() + orang(150, tinggi=110, jenis='pria', baju='a', wajah='sedih') + bau(110, 120) + bau(180, 110)

A['C08-1'] = kotak(16, 16, 268, 188, 'p') + ranjang(150, 200, 200) + ''.join(nyamuk(x, y, 1.3) for x, y in ((50, 36), (110, 50), (175, 32), (240, 46), (80, 96), (150, 86), (215, 100), (260, 80)))
A['C08-2'] = lantai() + gedung(230, tingkat=6, lebar=90) + mobil(150, 200, 110) + teks(190, 90, '!!', 26, angka=True) + orang(60, tinggi=160, jenis='wanita', baju='a', wajah='marah', tangan={'ki': [(16, -4), (0, -24)], 'ka': [(16, -4), (0, -24)]}) + jalur('M150 110 l14 -10 M160 124 l16 0 M150 138 l14 10', 'g')
A['C08-3'] = kotak(16, 16, 268, 188, 'p') + ''.join(nyamuk(x, y, 1.5) for x, y in ((50, 40), (120, 34), (200, 50), (255, 38), (80, 90), (165, 100), (235, 110), (45, 150), (115, 160), (190, 170), (255, 175)))
A['C08-4'] = dua_panel(pengeras_suara(60, 100, .9) + not_musik(110, 60) + not_musik(120, 130), orang(225, tinggi=160, jenis='pria', baju='a', wajah='marah', tangan={'ki': [(16, -4), (0, -24)], 'ka': [(16, -4), (0, -24)]})) + lantai()
A['C08-5'] = lantai() + orang(150, kaki=200, tinggi=140, jenis='pria', baju='a', wajah='lelah', duduk=196, tangan={'ki': [(20, 30), (40, 50)], 'ka': [(20, 30), (40, 50)]}) + keringat(118, 80) + keringat(186, 76) + keringat(150, 50, .8)

A['C09-1'] = dua_panel(gedung(75, tingkat=6, lebar=90) + awan(50, 36, .35, 'a') + awan(105, 26, .3, 'a'), rumah(225, 200, 90, 60) + pohon(270, s=.6) + centang(225, 40, 1.2)) + lantai()
A['C09-2'] = sawah(150) + rumah(150, 150, 110, 70) + pohon(40, 150, .6) + gunung(250, 150, 120, 70, False)
A['C09-3'] = lantai() + gunung(150, 200, 280, 120, False) + angin(40, 40, .6) + orang(150, kaki=150, tinggi=90, jenis='pria', baju='a', wajah='puas', tangan={'ki': [(14, -20), (30, -30)], 'ka': [(14, -20), (30, -30)]})
A['C09-4'] = lantai() + gedung(50, tingkat=7, lebar=70) + gedung(120, tingkat=6, lebar=60, tt=26) + gedung(190, tingkat=8, lebar=70, tt=22) + gedung(260, tingkat=5, lebar=50) + mobil(150, 200, 70)
A['C09-5'] = (teks(80, 30, '這裡', 24) + termometer(80, 44, 22) + angin(20, 110, .35) + teks(128, 150, '22°', 24, angka=True)
              + teks(220, 30, '那裡', 24) + termometer(220, 44, 34) + matahari(266, 80, 11) + teks(268, 150, '34°', 24, angka=True))

A['C10-1'] = grafik([9, 7, 5, 3, 1.5]) + dompet(230, 50, .4) + panah(60, 60, 240, 150, 4)
A['C10-2'] = ''.join(termometer(55 + i * 70, 40, t, 40, 110) + teks(55 + i * 70, 200, f'{t}°', 18, angka=True) for i, t in enumerate((25, 18, 11, 5))) + salju(270, 60, 9)
A['C10-3'] = lantai() + jendela(240, 30, 60, 46) + bulan_bintang(236, 52, .4) + meja(150, 140, 180) + buku(150, 140, 60, 14, 'a') + orang(80, tinggi=150, jenis='wanita', duduk=150, baju='a', tangan={'ka': [(22, 10), (60, 14)]}) + pulpen(160, 124, 40, -30)
A['C10-4'] = label_harga(60, 130, '50', 80, 40) + label_harga(150, 90, '80', 80, 40) + label_harga(240, 40, '120', 90, 40) + panah(40, 190, 260, 110, 4)
A['C10-5'] = kertas(80, 110, 70, 90, -8) + kertas(150, 106, 70, 90, 2) + kertas(220, 110, 70, 90, 8) + teks(80, 80, '5/1', 16, angka=True) + teks(150, 76, '5/2', 16, angka=True) + teks(220, 80, '5/3', 16, angka=True) + pulpen(230, 180, 80, -20)

A['C11-1'] = lantai() + awan(90, 60, .9, 'a') + awan(200, 50, 1.0, 'a') + awan(150, 100, .8, 'a') + rumah(150, 200, 110, 60)
A['C11-2'] = lantai() + pintu(250, 200, 140, 60) + orang(90, tinggi=165, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(20, 6), (44, -4)]}) + payung(160, 92, 26) + orang(200, tinggi=120, jenis='laki', baju='h')
A['C11-3'] = lantai() + matahari(150, 60, 32) + rumah(150, 200, 110, 60)
A['C11-4'] = lantai() + awan(80, 70, 1.0, 'a') + awan(210, 60, 1.1, 'a') + pohon(230, s=.8) + orang(100, tinggi=140, jenis='pria', baju='a')
A['C11-5'] = lantai() + orang(80, tinggi=165, jenis='wanita', baju='a', rambut='uban', wajah='marah', tangan={'ka': [(20, -10), (44, -20)]}) + kursi_depan(210, 150) + orang(210, tinggi=110, jenis='laki', duduk=150, baju='h', tangan={'ki': [(10, 10), (24, 0)], 'ka': [(10, 10), (24, 0)]}) + ponsel(210, 132, .9) + silang(150, 40, 14, 5)

A['C12-1'] = sawah(150) + gunung(230, 150, 140, 70, False) + orang(100, kaki=196, tinggi=110, jenis='laki', baju='a') + matahari(60, 40, 14)
A['C12-2'] = foto_bayi()
A['C12-3'] = sawah(160) + rumah(170, 160, 110, 70) + orang(70, kaki=200, tinggi=90, jenis='gadis', baju='a')
A['C12-4'] = foto_bayi() + ranjang(150, 214, 170).replace('class="h"', 'class="a"')[:0]
A['C12-5'] = lantai() + tabel_tinggi(150)
