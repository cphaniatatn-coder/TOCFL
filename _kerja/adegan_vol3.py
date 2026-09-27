"""Adegan ilustrasi 聽力 Part 1 — Volume 3 (C01–C67). ID = <modul>-<n> (listen_pic ke-n, urut isi → soal → bank)."""
from svg_adegan import *
from adegan_vol2 import potret, pelari, tunjuk_ke, burung, jam_kecil, rambut_terurai, garis_jatuh, pegang_perut, piala, kembang_api, meja_bundar, JOG, LARI

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


# ================= komponen C13–C24 =================
def cucu_banyak(nenek_x=60, jenis_cucu='laki', n=4, rambut='uban', jenis='nenek'):
    o = lantai() + orang(nenek_x, tinggi=150, jenis=jenis, baju='a', rambut=rambut, rok=None if jenis == 'nenek' else False)
    for i in range(n):
        o += orang(nenek_x + 60 + i * (180 / max(n, 1)), tinggi=88 + (i % 2) * 8, jenis=jenis_cucu, baju='h' if i % 2 else 'p')
    return o


def pengantin(x_pr=110, x_lk=195):
    s_ = sendi(x_pr, LANTAI, 155, 'wanita')
    o = jalur(f'M{f(x_pr - s_["r"] * 1.2)} {f(s_["cy"] - s_["r"] * .6)} Q{f(x_pr)} {f(s_["cy"] - s_["r"] * 1.6)} {f(x_pr + s_["r"] * 1.2)} {f(s_["cy"] - s_["r"] * .6)} L{f(x_pr + s_["r"] * 2)} {f(s_["cy"] + 60)} L{f(x_pr - s_["r"] * 2)} {f(s_["cy"] + 60)} Z', 'p')
    o += orang(x_pr, tinggi=155, jenis='wanita', baju='p', wajah='puas', tangan={'ka': [(10, 20), (4, 36)]})
    o += bentuk((x_pr - 34, 116), (x_pr + 34, 116), (x_pr + 46, 200), (x_pr - 46, 200), k='p')
    o += orang(x_lk, tinggi=165, jenis='pria', baju='h', wajah='puas', tangan={'ki': [(10, 20), (4, 36)]})
    return o + bunga(x_pr + 16, 106, .6) + garis((x_lk, 70), (x_lk, 84), k='w')


def kacamata_hitam(x, cy, r):
    return kotak(x - r * .8, cy - r * .22, r * .7, r * .34, 'h', 3) + kotak(x + r * .1, cy - r * .22, r * .7, r * .34, 'h', 3) + garis((x - r * .1, cy - r * .1), (x + r * .1, cy - r * .1))


def mesin_kopi(x, bawah):
    return (kotak(x - 34, bawah - 70, 68, 70, 'a', 5) + kotak(x - 24, bawah - 60, 48, 20, 'h', 3) + garis((x - 10, bawah - 40), (x - 10, bawah - 30), lebar=5)
            + garis((x + 10, bawah - 40), (x + 10, bawah - 30), lebar=5) + cangkir(x, bawah - 4, .35, False))


def nampan(x, y, w=60):
    return elips(x, y, w / 2, 6, 'a') + cangkir(x - 12, y - 4, .3, False) + cangkir(x + 14, y - 4, .3, False)


def layar_berita(x, bawah, w=170):
    t = w * .62
    return (kotak(x - w / 2, bawah - t - 10, w, t, 'p', 4) + kotak(x - w / 2 + 8, bawah - t - 2, w - 16, t - 16, 'a', 2)
            + kotak(x - w / 2 + 8, bawah - 30, w - 16, 12, 'h') + orang(x, kaki=bawah - 18, tinggi=90, jenis='wanita', baju='h') + kotak(x - 40, bawah - 46, 80, 18, 'h', 2) + kotak(x - 5, bawah - 10, 10, 10, 'p'))


def stik_game(x, y, s=1.0):
    return (jalur(f'M{f(x - 40 * s)} {f(y - 14 * s)} Q{f(x)} {f(y - 24 * s)} {f(x + 40 * s)} {f(y - 14 * s)} Q{f(x + 56 * s)} {f(y + 24 * s)} {f(x + 36 * s)} {f(y + 22 * s)} '
                  f'Q{f(x)} {f(y + 8 * s)} {f(x - 36 * s)} {f(y + 22 * s)} Q{f(x - 56 * s)} {f(y + 24 * s)} {f(x - 40 * s)} {f(y - 14 * s)} Z', 'h')
            + kotak(x - 30 * s, y - 4 * s, 16 * s, 5 * s, 'n') + kotak(x - 24.5 * s, y - 9.5 * s, 5 * s, 16 * s, 'n') + bulat(x + 22 * s, y - 6 * s, 3.5 * s, 'n') + bulat(x + 30 * s, y + 1 * s, 3.5 * s, 'n'))


def papan_keluar(x, y, isi='', arah=0, w=150, h=60):
    """Papan hijau-hitam 'pintu keluar': orang berlari + pintu; isi = nomor; arah -1 kiri, 1 kanan."""
    o = kotak(x - w / 2, y, w, h, 'h', 6) + kotak(x - w / 2 + 10, y + 10, 26, 40, 'n', 2)
    o += orang(x - w / 2 + 50, kaki=y + 50, tinggi=40, jenis='pria', baju='p', wajah=None, kaki_pose={'ki': (-10, 0), 'ka': (10, -6)}).replace('class="h"', 'class="n"').replace('class="g"', 'class="w"')
    if isi:
        o += teks(x + 34, y + 44, isi, 36, angka=True, warna='#fff')
    if arah:
        o += garis((x + 10, y + 30), (x + 60, y + 30), k='w') + bentuk((x + 60, y + 22), (x + 70, y + 30), (x + 60, y + 38), k='n') if arah > 0 else garis((x + 10, y + 30), (x + 60, y + 30), k='w') + bentuk((x + 10, y + 22), (x, y + 30), (x + 10, y + 38), k='n')
    return o


def gerbong_mrt(penuh=True):
    o = kotak(16, 16, 268, 188, 'p', 10) + kotak(30, 30, 240, 50, 'a', 6) + garis((16, 170), (284, 170), k='t') + garis((30, 20), (270, 20), lebar=3)
    o += kotak(24, 140, 252, 18, 'a', 4)
    if penuh:
        for i in range(6):
            o += orang(45 + i * 42, tinggi=150, jenis='pria' if i % 2 else 'wanita', baju='h' if i % 3 == 0 else 'a', wajah='senyum', tangan={'ka': [(6, -30), (0, -60)]})
    return o


def skuter(x, lantai_y=LANTAI, s=1.0):
    return (bulat(x - 44 * s, lantai_y - 18 * s, 18 * s, 'h') + bulat(x + 44 * s, lantai_y - 18 * s, 18 * s, 'h') + bulat(x - 44 * s, lantai_y - 18 * s, 6 * s, 'n') + bulat(x + 44 * s, lantai_y - 18 * s, 6 * s, 'n')
            + jalur(f'M{f(x - 58 * s)} {f(lantai_y - 30 * s)} L{f(x - 10 * s)} {f(lantai_y - 30 * s)} L{f(x + 20 * s)} {f(lantai_y - 60 * s)} L{f(x + 40 * s)} {f(lantai_y - 60 * s)} L{f(x + 52 * s)} {f(lantai_y - 34 * s)} L{f(x + 30 * s)} {f(lantai_y - 30 * s)} Q{f(x - 20 * s)} {f(lantai_y - 20 * s)} {f(x - 58 * s)} {f(lantai_y - 30 * s)} Z', 'a')
            + kotak(x - 50 * s, lantai_y - 46 * s, 44 * s, 14 * s, 'h', 6) + garis((x + 34 * s, lantai_y - 60 * s), (x + 30 * s, lantai_y - 92 * s), lebar=4) + garis((x + 20 * s, lantai_y - 92 * s), (x + 44 * s, lantai_y - 92 * s), lebar=5))


def rambu(x, isi, coret=True, lantai_y=LANTAI, r=48):
    o = garis((x, lantai_y), (x, lantai_y - 100), lebar=5) + bulat(x, lantai_y - 100 - r, r, 'p') + isi
    if coret:
        o += f'<circle cx="{f(x)}" cy="{f(lantai_y - 100 - r)}" r="{f(r)}" fill="none" stroke="#111" stroke-width="7"/>' + garis((x - r * .7, lantai_y - 100 - r * 1.7), (x + r * .7, lantai_y - 100 - r * .3), lebar=7)
    return o


def huruf_p(x, y, uk=56):
    return teks(x, y + uk * .36, 'P', uk, angka=True)


def kapal(x, y, s=1.0):
    return (jalur(f'M{f(x - 90 * s)} {f(y)} L{f(x + 90 * s)} {f(y)} L{f(x + 70 * s)} {f(y + 36 * s)} L{f(x - 76 * s)} {f(y + 36 * s)} Z', 'h')
            + kotak(x - 56 * s, y - 34 * s, 100 * s, 34 * s, 'p', 4) + kotak(x - 30 * s, y - 60 * s, 56 * s, 26 * s, 'p', 4)
            + ''.join(bulat(x - 40 * s + i * 20 * s, y - 18 * s, 5 * s, 'h') for i in range(5)) + kotak(x + 6 * s, y - 84 * s, 16 * s, 26 * s, 'a'))


def laut(y=160):
    return bentuk((16, y), (284, y), (284, 204), (16, 204), k='a') + jalur(f'M24 {y + 14} q10 -8 20 0 t20 0 t20 0 M150 {y + 26} q10 -8 20 0 t20 0 t20 0 M200 {y + 10} q10 -8 20 0 t20 0', 'w')


def kabin_penuh():
    o = kotak(16, 16, 268, 188, 'p', 30) + kotak(40, 26, 220, 20, 'a', 8)
    for j in range(2):
        for i in range(4):
            x = 55 + i * 62 + (32 if i >= 2 else 0) - 16
            y = 70 + j * 62
            o += kotak(x - 20, y, 40, 50, 'a', 6) + bulat(x, y + 4, 11) + jalur(f'M{f(x - 11)} {f(y + 2)} q2 -12 11 -12 q9 0 11 12', 'h')
    return o


def topan():
    o = lantai() + awan(150, 40, 1.2, 'h') + jalur('M150 50 m-40 0 a40 16 0 1 1 80 0 a30 12 0 1 1 -60 0 a18 8 0 1 1 36 0', 'w')
    o += hujan(150, 70, 260, 60, 13) + angin(20, 120, .8)
    return o + kotak(245, 150, 8, 50, 'h') + jalur('M249 150 Q262 110 286 104 Q270 128 260 150 Z', 'p') + kotak(30, 150, 8, 50, 'h') + jalur('M34 150 Q48 112 70 106 Q56 130 44 150 Z', 'p')


def kolam_panas(x=150, y=150):
    o = elips(x, y, 120, 30, 'a') + ''.join(elips(x + dx, y + dy, rx, ry, 'p') for dx, dy, rx, ry in ((-110, -10, 20, 14), (100, -14, 24, 16), (-60, 26, 18, 10), (90, 22, 20, 12)))
    return o + uap_(x - 40, y - 26, 1.4) + uap_(x + 40, y - 26, 1.4)


# ================= C13–C24 =================
A['C13-1'] = cucu_banyak(55, 'laki', 4)
A['C13-2'] = cucu_banyak(55, 'laki', 4)
A['C13-3'] = lantai() + orang(90, tinggi=125, jenis='laki', baju='a') + panah(90, 50, 90, 70, 4) + teks(90, 44, '我', 18) + orang(165, tinggi=150, jenis='pria', baju='h') + orang(235, tinggi=140, jenis='pria', baju='p')
A['C13-4'] = lantai() + orang(90, tinggi=150, jenis='nenek', rambut='pendek', rok=False, baju='a', kacamata=True) + meja(210, 150, 120) + kue_ultah(210, 150, '80', .7)
A['C13-5'] = cucu_banyak(55, 'gadis', 4)

A['C14-1'] = lantai() + kereta(170, 196, 230) + orang(40, tinggi=150, jenis='pria', baju='h', wajah='nyanyi', tangan={'ka': [(12, 24), (-4, -4)]}) + jalur('M60 50 l14 -6 M60 58 l16 0', 'g') + jam_kecil(250, 40, 9, 59, 22)
A['C14-2'] = lantai() + pengantin()
_cyh, _rh = sendi(150, LANTAI, 170, 'pria')['cy'], sendi(150, LANTAI, 170, 'pria')['r']
A['C14-3'] = lantai() + orang(150, tinggi=170, jenis='pria', baju='h', wajah='senyum', tangan={'ka': [(20, 20), (4, 40)]}) + kacamata_hitam(150, _cyh, _rh) + bintang(100, 40, 8) + bintang(210, 50, 6)
A['C14-4'] = lantai() + pengantin(90, 170) + bulat(250, 70, 16, 't') + bulat(265, 70, 16, 't') + bintang(257, 50, 6)
A['C14-5'] = lantai() + papan_tulis(95, 30, 150, 80) + orang(230, tinggi=170, jenis='pria', baju='a', kacamata=True, tangan={'ki': [(10, -10), (34, -40)]})

A['C15-1'] = lantai() + kotak(120, 120, 164, 80, 'a') + mesin_kopi(250, 120) + orang(170, kaki=200, tinggi=150, jenis='pria', baju='h') + kotak(120, 120, 164, 80, 'a') + mesin_kopi(250, 120) + cangkir(140, 118, .35, True)
A['C15-2'] = lantai() + kotak(120, 120, 164, 80, 'a') + mesin_kopi(250, 120) + orang(170, kaki=200, tinggi=145, jenis='wanita', baju='h') + kotak(120, 120, 164, 80, 'a') + mesin_kopi(250, 120) + cangkir(140, 118, .35, True)
A['C15-3'] = lantai() + orang(100, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 16), (44, 20)]}, kacamata=True) + tas_kerja(70, 196, .7) + orang(200, tinggi=160, jenis='pria', baju='a', tangan={'ki': [(20, 16), (44, 20)]})
A['C15-4'] = lantai() + meja(90, 150, 120) + orang(200, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(16, -10), (30, -20)]}) + nampan(236, 64, 60)
A['C15-5'] = lantai() + papan_tulis(80, 30, 120, 70) + orang(170, tinggi=160, jenis='wanita', baju='a', rambut='uban', tangan={'ki': [(10, -10), (30, -30)]}) + murid_belakang(230, 200, 120) + murid_belakang(275, 200, 125, 'gadis')

A['C16-1'] = kotak(16, 16, 268, 188, 'p') + kotak(90, 26, 120, 60, 'p') + grafik([2, 4, 3, 6], 100, 80, 100, 48) + meja(150, 150, 220) + orang(50, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(250, tinggi=135, jenis='pria', duduk=160, baju='h') + orang(150, kaki=200, tinggi=80, jenis='pria', baju='a')
A['C16-2'] = kotak(16, 16, 268, 188, 'p') + jendela(230, 30, 60, 46) + bulan_bintang(226, 52, .4) + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'a') + lampu(150, 60, True, 30)
A['C16-3'] = kotak(16, 16, 268, 188, 'p') + jam_dinding(240, 60, 34, 3, 0) + meja(130, 150, 200) + orang(60, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(200, tinggi=135, jenis='pria', duduk=160, baju='h')
A['C16-4'] = kotak(16, 16, 268, 188, 'p') + jam_dinding(240, 60, 34, 9, 0) + meja(130, 150, 200) + orang(60, tinggi=130, jenis='pria', duduk=160, baju='h') + orang(200, tinggi=135, jenis='wanita', duduk=160, baju='a')
A['C16-5'] = dua_panel(orang_ponsel(75, 'pria', 150, baju='a') + gelembung(110, 30, 60, 34, silang(110, 30, 10, 4), (-1, 1)), sofa(225, 200, 110) + orang(225, tinggi=140, jenis='wanita', duduk=160, baju='a', wajah='puas')) + lantai()

A['C17-1'] = lantai() + gunung(170, 200, 260, 170, False) + orang(120, kaki=130, tinggi=80, jenis='pria', baju='h') + tas_punggung(106, 70, .5) + orang(170, kaki=95, tinggi=76, jenis='wanita', baju='a') + tas_punggung(157, 38, .5)
A['C17-2'] = lantai() + gunung(170, 200, 260, 170, False) + orang(140, kaki=120, tinggi=90, jenis='pria', baju='a') + tas_punggung(124, 52, .6) + garis((160, 70), (170, 120), lebar=3)
A['C17-3'] = lantai() + bulan_bintang(250, 36, .5) + pohon(40, s=.8) + jalan_kaki(130, 'wanita', 150, 'a') + jalan_kaki(190, 'pria', 160, 'h')
A['C17-4'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='puas') + headphone(110, sendi(110, 200, 160, 'pria')['cy'], sendi(110, 200, 160, 'pria')['r']) + not_musik(180, 70) + not_musik(220, 110) + jalur('M200 40 q-10 -12 -20 0 q-10 12 20 30 q30 -18 20 -30 q-10 -12 -20 0', 'h')
A['C17-5'] = lantai() + pohon(40, s=.9) + pohon(265, s=.8) + bangku(150) + jalan_kaki(120, 'wanita', 150, 'a') + jalan_kaki(180, 'pria', 160, 'h')

A['C18-1'] = (lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='wanita', duduk=150, baju='a', tangan={'ki': [(20, 24), (34, 30)], 'ka': [(20, 24), (34, 30)]})
              + kotak(112, 118, 76, 60, 'p', 2) + kotak(116, 122, 68, 12, 'h') + bulat(150, 150, 9, 'a') + bentuk((136, 174), (164, 174), (158, 160), (142, 160), k='a'))   # sampul majalah bergambar
A['C18-2'] = (kotak(16, 16, 268, 80, 'a') + ''.join(potret(x, 150, 22, 'pria' if i % 2 else 'wanita', 'tawa', 'h' if i % 2 else 'a') for i, x in enumerate((50, 110, 170, 230))) + teks(150, 60, 'ha ha ha', 20, angka=True))
A['C18-3'] = lantai() + layar_berita(190, 150, 170) + meja(190, 150, 120) + orang(60, tinggi=150, jenis='pria', duduk=160, baju='a', kacamata=True)
A['C18-4'] = lantai() + tv(200, 150, 120) + meja(200, 150, 110) + orang(80, tinggi=120, jenis='laki', duduk=160, baju='a', wajah='tawa', tangan={'ki': [(14, 20), (30, 16)], 'ka': [(14, 20), (30, 16)]}) + stik_game(96, 126, .4)
A['C18-5'] = lantai() + matahari(260, 36, 12) + layar_berita(190, 150, 150) + meja(190, 150, 110) + orang(60, tinggi=150, jenis='wanita', duduk=160, baju='a', tangan={'ka': [(14, 20), (-2, -2)]}) + cangkir(80, 94, .4, True)

A['C19-1'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='nyanyi', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(12, 30), (-8, -8)]}, kaki_pose={'ki': (-8, 0), 'ka': (30, -24)}) + mikrofon(182, 58, .9) + not_musik(230, 60)
A['C19-2'] = lantai() + meja(160, 140, 200) + kertas(170, 128, 70, 22) + orang(90, tinggi=140, jenis='gadis', duduk=150, baju='a', tangan={'ka': [(22, 10), (60, 14)]}) + headphone(90, sendi(90, 150, 140, 'gadis', 150)['cy'], sendi(90, 150, 140, 'gadis', 150)['r']) + not_musik(240, 60)
A['C19-3'] = A.get('C19-3', '') + lantai() + bulan_bintang(250, 30, .5) + garis((20, 60), (280, 60), k='t') + ''.join(lampion(40 + i * 44, 72, .7) for i in range(6)) + kotak(20, 130, 110, 70, 'a') + kotak(170, 130, 110, 70, 'a') + jalan_kaki(150, 'wanita', 115, 'a')
A['C19-4'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h', wajah='nyanyi', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(12, 30), (-8, -8)]}, kaki_pose={'ki': (-8, 0), 'ka': (30, -24)}) + mikrofon(182, 58, .9) + not_musik(230, 60)
A['C19-5'] = tiket(110, 60, 120, 60) + tiket(190, 110, 120, 60)

A['C20-1'] = kotak(16, 16, 268, 188, 'a') + papan_keluar(150, 40, '2') + lantai() + orang(100, tinggi=100, jenis='pria', baju='h', kaki_pose={'ki': (-14, 0), 'ka': (14, 0)})
A['C20-2'] = kotak(16, 16, 268, 188, 'a') + kotak(16, 150, 268, 54, 'p') + garis((16, 150), (284, 150), lebar=5) + kereta(150, 146, 250) + orang(250, kaki=200, tinggi=60, jenis='pria', baju='h')
A['C20-3'] = kotak(16, 16, 268, 188, 'a') + papan_keluar(150, 60, '', 1)
A['C20-4'] = kotak(16, 16, 268, 188, 'a') + papan_keluar(150, 60, '', -1)
A['C20-5'] = gerbong_mrt(True)

A['C21-1'] = lantai() + rambu(150, skuter(150, 70, .45), True, 200, 50)
A['C21-2'] = lantai() + skuter(150, 200, 1.1) + orang(130, kaki=150, tinggi=120, jenis='wanita', baju='a', wajah='takut', tangan={'ki': [(20, -20), (40, -30)], 'ka': [(20, -20), (40, -30)]}) + jalur('M80 90 q-10 10 0 20 M220 90 q10 10 0 20', 'g')
A['C21-3'] = lantai() + kotak(20, 30, 60, 60, 'h', 6) + huruf_p(50, 56, 50).replace('<text', '<text style="fill:#fff"') + mobil(110, 200, 100) + mobil(220, 200, 100, k='a') + garis((165, 200), (165, 170), k='t')
A['C21-4'] = lantai() + rambu(150, huruf_p(150, 52, 56), True, 200, 50)
A['C21-5'] = lantai() + mobil(90, 200, 110) + skuter(220, 200, .8) + mobil(170, 170, 80, k='a') + skuter(60, 160, .5) + jalur('M120 40 l20 20 M160 30 l-10 24 M200 44 l-20 14', 'g') + teks(150, 26, '!!', 20, angka=True)

A['C22-1'] = lantai() + orang(80, tinggi=160, jenis='pria', baju='a') + koper(140, 196, 1.0) + koper(190, 196, 1.2) + koper(245, 196, .9) + koper(190, 128, .7)
A['C22-2'] = kalender_senin(150, 40, 2, 3) + pesawat(150, 150, .45) + panah(150, 118, 150, 132, 3)
A['C22-3'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='sakit', tangan={'ka': [(20, 30), (46, 44)]}) + koper(190, 196, 1.3) + keringat(84, 44) + jalur('M230 120 l12 -8 M232 136 l14 0', 'g')
A['C22-4'] = kalender_bulan(90, 40, 5, '', 110, 110) + teks(90, 175, '這個月', 18) + kalender_bulan(215, 40, 6, '', 110, 110) + pesawat(215, 110, .28)
A['C22-5'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='sakit', tangan={'ki': [(20, 30), (30, 50)], 'ka': [(20, 30), (30, 50)]}) + kardus(150, 196, 90, 50) + keringat(124, 44) + keringat(180, 40)

A['C23-1'] = laut(160) + kapal(150, 130, 1.0) + awan(60, 40, .4) + awan(240, 50, .35)
A['C23-2'] = laut(170) + kapal(190, 140, .8) + tiket(70, 40, 100, 50) + pesawat(62, 64, .18) + silang(70, 64, 26, 6)
A['C23-3'] = lantai() + gedung(120, tingkat=5, lebar=150) + kotak(200, 60, 80, 50, 'p', 4) + kotak(212, 80, 56, 14, 'h') + kotak(212, 70, 10, 24, 'h') + silang(240, 85, 26, 6)
A['C23-4'] = kabin_penuh()
A['C23-5'] = laut(160) + jalur('M200 160 Q240 110 280 160 Z', 'a') + pohon(240, 150, .4) + kapal(110, 140, .7)

A['C24-1'] = topan()
A['C24-2'] = lantai() + awan(150, 60, 1.6, 'h') + jalur('M150 70 m-60 0 a60 24 0 1 1 120 0 a44 18 0 1 1 -88 0 a26 10 0 1 1 52 0', 'w') + rumah(150, 200, 110, 60)
A['C24-3'] = kolam_panas() + orang(110, kaki=190, tinggi=110, jenis='wanita', baju='p', wajah='puas') + orang(190, kaki=190, tinggi=115, jenis='pria', baju='p', wajah='puas') + kolam_panas().replace('class="a"', 'class="a"')[:0]
A['C24-4'] = dua_panel(topan().replace(lantai(), ''), rumah(225, 200, 110, 70) + orang(210, kaki=196, tinggi=50, jenis='laki', baju='a') + orang(240, kaki=196, tinggi=60, jenis='wanita', baju='h')) + lantai()
A['C24-5'] = kolam_panas(150, 150) + pohon(40, 180, .5) + pohon(265, 180, .5)


# ================= komponen C25–C36 =================
def kado(x, bawah, s=1.0):
    return (kotak(x - 30 * s, bawah - 50 * s, 60 * s, 50 * s, 'a', 3) + kotak(x - 34 * s, bawah - 62 * s, 68 * s, 14 * s, 'p', 3) + kotak(x - 5 * s, bawah - 62 * s, 10 * s, 62 * s, 'h')
            + jalur(f'M{f(x)} {f(bawah - 62 * s)} q{f(-22 * s)} {f(-22 * s)} {f(-24 * s)} {f(-6 * s)} q{f(4 * s)} {f(8 * s)} {f(24 * s)} {f(6 * s)} q{f(20 * s)} {f(2 * s)} {f(24 * s)} {f(-6 * s)} q{f(-2 * s)} {f(-16 * s)} {f(-24 * s)} {f(6 * s)} Z', 'h'))


def balon(x, y, s=1.0, k='a'):
    return elips(x, y, 16 * s, 20 * s, k) + bentuk((x - 4 * s, y + 20 * s), (x + 4 * s, y + 20 * s), (x, y + 25 * s), k='h') + jalur(f'M{f(x)} {f(y + 25 * s)} q{f(6 * s)} {f(14 * s)} 0 {f(28 * s)} q{f(-6 * s)} {f(14 * s)} 0 {f(28 * s)}', 't')


def pesta():
    return (lantai() + balon(40, 50, 1, 'a') + balon(70, 40, .9, 'h') + balon(250, 44, 1, 'p') + balon(275, 60, .8, 'a') + not_musik(150, 40)
            + orang(110, tinggi=140, jenis='wanita', baju='a', wajah='tawa', tangan=LAMBAI) + orang(190, tinggi=150, jenis='pria', baju='h', wajah='tawa', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(24, -20), (36, -56)]}))


def tagihan(x, y, s=1.0):
    return kotak(x - 18 * s, y - 26 * s, 36 * s, 52 * s, 'p', 2) + ''.join(garis((x - 12 * s, y - 16 * s + i * 9 * s), (x + 12 * s, y - 16 * s + i * 9 * s), k='t') for i in range(4))


def tisu(x, y, s=1.0):
    return jalur(f'M{f(x - 12 * s)} {f(y - 10 * s)} q{f(6 * s)} {f(-6 * s)} {f(12 * s)} 0 q{f(6 * s)} {f(6 * s)} {f(12 * s)} 0 l{f(-2 * s)} {f(20 * s)} l{f(-20 * s)} 0 Z', 'p')


def rak_obat(x, lantai_y=LANTAI, w=120, h=130):
    o = kotak(x - w / 2, lantai_y - h, w, h, 'p')
    for j in range(3):
        y = lantai_y - h + 12 + j * 40
        o += garis((x - w / 2, y + 30), (x + w / 2, y + 30), lebar=3) + ''.join(botol_obat(x - w / 2 + 16 + i * 22, y + 30, .38) for i in range(5))
    return o


def apotek(x, lantai_y=LANTAI, w=170, h=120):
    return (kotak(x - w / 2, lantai_y - h, w, h, 'p') + kotak(x - w / 2, lantai_y - h, w, 28, 'h') + palang(x, lantai_y - h + 14, .3).replace('class="h"', 'class="n"')
            + kotak(x - w / 2 + 12, lantai_y - h + 40, 60, 50, 'p') + botol_obat(x - w / 2 + 30, lantai_y - h + 86, .35) + botol_obat(x - w / 2 + 54, lantai_y - h + 86, .35)
            + kotak(x + 14, lantai_y - 80, 56, 80, 'a') + garis((x + 42, lantai_y - 80), (x + 42, lantai_y)))


def kamera(x, y, s=1.0):
    return kotak(x - 30 * s, y - 20 * s, 60 * s, 40 * s, 'h', 6) + bulat(x, y, 13 * s, 'p') + bulat(x, y, 7 * s, 'a') + kotak(x - 20 * s, y - 28 * s, 16 * s, 8 * s, 'h', 2)


def perban(x, y, w=26, h=30):
    return kotak(x - w / 2, y, w, h, 'p', 4) + ''.join(garis((x - w / 2, y + 7 + i * 8), (x + w / 2, y + 7 + i * 8), k='t') for i in range(3))


def lampu_ide(x, y, s=1.0):
    return (bulat(x, y, 14 * s, 'p') + kotak(x - 7 * s, y + 12 * s, 14 * s, 10 * s, 'a', 2) + ''.join(garis((x + math.cos(math.radians(a)) * 20 * s, y + math.sin(math.radians(a)) * 20 * s),
                                                                                                  (x + math.cos(math.radians(a)) * 28 * s, y + math.sin(math.radians(a)) * 28 * s), lebar=2.4) for a in (200, 240, 270, 300, 340)))


def lembar_soal(x, y, n=20, w=140, h=170):
    o = kotak(x - w / 2, y, w, h, 'p')
    for i in range(10):
        for j in range(2):
            k = i + j * 10 + 1
            o += teks(x - w / 2 + 14 + j * 70, y + 20 + i * 15, f'{k}.', 11, angka=True, anchor='start') + garis((x - w / 2 + 36 + j * 70, y + 18 + i * 15), (x - w / 2 + 62 + j * 70, y + 18 + i * 15), k='t')
    return o


def pantai():
    return (bentuk((16, 150), (284, 150), (284, 204), (16, 204), k='p') + bentuk((16, 120), (284, 120), (284, 150), (16, 150), k='a')
            + jalur('M24 132 q10 -8 20 0 t20 0 t20 0 M160 140 q10 -8 20 0 t20 0', 'w') + matahari(250, 40, 16)
            + garis((80, 196), (80, 110), lebar=4) + jalur('M40 116 Q80 76 120 116 Z', 'h'))


def toga(x, cy, r):
    return bentuk((x - r * 1.5, cy - r * .8), (x, cy - r * 1.4), (x + r * 1.5, cy - r * .8), (x, cy - r * .3), k='h') + garis((x + r * 1.2, cy - r * .8), (x + r * 1.3, cy + r * .3), lebar=2)


def gulungan(x, y, s=1.0):
    return (kotak(x - 40 * s, y - 26 * s, 80 * s, 52 * s, 'p') + elips(x - 40 * s, y, 7 * s, 30 * s, 'a') + elips(x + 40 * s, y, 7 * s, 30 * s, 'a')
            + ''.join(garis((x - 28 * s + i * 12 * s, y - 18 * s), (x - 28 * s + i * 12 * s, y + 18 * s), k='t') for i in range(5)))


def timbangan(x, y, s=1.0):
    return (garis((x, y), (x, y + 80 * s), lebar=5) + kotak(x - 26 * s, y + 80 * s, 52 * s, 10 * s, 'h', 2) + garis((x - 50 * s, y + 10 * s), (x + 50 * s, y + 10 * s), lebar=4)
            + garis((x - 50 * s, y + 10 * s), (x - 60 * s, y + 40 * s), k='t') + garis((x - 50 * s, y + 10 * s), (x - 40 * s, y + 40 * s), k='t')
            + garis((x + 50 * s, y + 10 * s), (x + 40 * s, y + 40 * s), k='t') + garis((x + 50 * s, y + 10 * s), (x + 60 * s, y + 40 * s), k='t')
            + jalur(f'M{f(x - 64 * s)} {f(y + 40 * s)} Q{f(x - 50 * s)} {f(y + 54 * s)} {f(x - 36 * s)} {f(y + 40 * s)} Z', 'a') + jalur(f'M{f(x + 36 * s)} {f(y + 40 * s)} Q{f(x + 50 * s)} {f(y + 54 * s)} {f(x + 64 * s)} {f(y + 40 * s)} Z', 'a')
            + bulat(x, y, 6 * s, 'h'))


def lampu_kristal(x, y, s=1.0):
    o = garis((x, y - 20 * s), (x, y), lebar=3) + jalur(f'M{f(x - 40 * s)} {f(y + 10 * s)} Q{f(x)} {f(y + 30 * s)} {f(x + 40 * s)} {f(y + 10 * s)}', 'g', 4)
    return o + ''.join(bentuk((x + dx * s, y + 14 * s + abs(dx) * .1 * s), (x + dx * s - 5 * s, y + 26 * s), (x + dx * s, y + 36 * s), (x + dx * s + 5 * s, y + 26 * s), k='p') for dx in (-36, -18, 0, 18, 36))


# ================= C25–C36 =================
A['C25-1'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 10), (44, 4)]}) + kado(152, 110, .8) + orang(220, tinggi=155, jenis='wanita', baju='a', wajah='puas')
A['C25-2'] = pesta()
A['C25-3'] = lantai() + meja(150, 150, 240) + orang(60, tinggi=140, jenis='wanita', duduk=160, baju='a', wajah='puas') + orang(240, tinggi=140, jenis='pria', duduk=160, baju='p', wajah='puas') + orang(150, tinggi=165, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(20, 10), (40, -4)]}) + kartu_kredit(196, 86, .6) + tagihan(120, 136, .7)
A['C25-4'] = kalender_senin(150, 20, 2, 3) + balon(150, 130, 1.1, 'a') + balon(122, 144, .9, 'h') + balon(178, 146, .9, 'p')
A['C25-5'] = lantai() + stasiun(210, 200, 130, 90) + jam_kecil(210, 60, 3, 0, 14) + orang(70, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (40, 12)]}) + orang(130, tinggi=160, jenis='pria', baju='h', tangan={'ki': [(20, 10), (40, 12)]})

A['C26-1'] = lantai_kamar() + ranjang(120, 200, 170) + bulat(66, 132, 13) + muka(66, 132, 13, 'lelah') + jalur('M52 126 q2 -18 16 -18 q12 0 13 14', 'a') + orang(235, tinggi=140, jenis='gadis', baju='a', tangan={'ki': [(20, 10), (44, 4)]}) + gelas(188, 108, 'air', .4)
A['C26-2'] = lantai() + rumah_sakit(225, 200, 120, 100) + orang(70, tinggi=150, jenis='nenek', rambut='uban', baju='a', tangan={'ka': [(16, 20), (30, 30)]}) + garis((50, 110), (46, 200), lebar=4) + orang(120, tinggi=130, jenis='gadis', baju='h', tangan={'ki': [(16, 20), (30, 30)]})
A['C26-3'] = lantai_kamar() + ranjang(130, 200, 190) + bulat(70, 134, 13) + muka(70, 134, 13, 'sakit') + jalur('M56 129 q2 -18 16 -18 q12 0 13 14', 'h') + orang(240, tinggi=150, jenis='wanita', baju='p', rambut='pendek', tangan={'ki': [(20, 10), (40, 10)]}) + kotak(228, 44, 24, 8, 'p', 2)
A['C26-4'] = lantai() + kios_buah(200, 200, 150) + orang(60, tinggi=160, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(16, 26), (30, 44)]}) + keranjang(86, 170, .6) + orang(115, tinggi=100, jenis='laki', baju='h')
A['C26-5'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -4), (40, -14)]}) + gelembung(90, 30, 60, 34, bintang(90, 30, 9), (1, 1)) + orang(210, tinggi=165, jenis='pria', baju='h', wajah='tawa') + jalur('M238 30 q-10 -12 -20 0 q-10 12 20 30 q30 -18 20 -30 q-10 -12 -20 0', 'h')

A['C27-1'] = potret(150, 84, 44, 'pria', 'puas', 'a') + headphone(150, 84, 44) + not_musik(235, 70) + not_musik(60, 90)
A['C27-2'] = dua_panel(orang_ponsel(75, 'wanita', 150, baju='a') + gelembung(110, 30, 56, 34, bulat(96, 30, 3, 'h') + bulat(110, 30, 3, 'h') + bulat(124, 30, 3, 'h'), (-1, 1)), ponsel(225, 110, 2.4, 'p') + gelembung(225, 96, 60, 30, garis((208, 96), (242, 96), k='t'), (-1, 1)))
A['C27-3'] = potret(150, 84, 44, 'pria', 'puas', 'a') + headphone(150, 84, 44)
A['C27-4'] = potret(150, 84, 44, 'pria', 'senyum', 'h') + headphone(150, 84, 44)
A['C27-5'] = lantai() + orang(150, kaki=190, tinggi=160, jenis='wanita', baju='a', wajah='tawa', tangan={'ki': [(20, -20), (30, -50)], 'ka': [(10, 10), (0, -10)]}, kaki_pose={'ki': (-20, -10), 'ka': (20, -10)}) + ponsel(162, 82, .8) + bintang(80, 40, 8) + bintang(230, 50, 7) + bintang(210, 20, 5)

A['C28-1'] = potret(150, 84, 44, 'pria', 'sakit', 'a') + jalur('M144 104 q-4 14 0 22 q4 -8 0 -22', 'p') + tisu(200, 150, 1.6)
A['C28-2'] = potret(150, 84, 44, 'wanita', 'sakit', 'a') + garis((170, 110), (220, 96), lebar=5) + bulat(222, 95, 5, 'h') + jalur('M100 40 l-10 -10 M200 40 l10 -10 M150 20 l0 -12', 'g')
A['C28-3'] = potret(150, 84, 44, 'pria', 'sakit', 'h') + jalur('M196 104 l24 -8 M198 116 l28 0 M196 128 l24 8', 'g', 4) + teks(248, 80, 'khk', 16, angka=True)
A['C28-4'] = (potret(150, 94, 44, 'pria', 'sakit', 'a') + garis((104, 200), (84, 150), (100, 96), lebar=15) + garis((196, 200), (216, 150), (200, 96), lebar=15) + elips(100, 90, 12, 20, 'p') + elips(200, 90, 12, 20, 'p')
              + jalur('M90 40 l-12 -10 M210 40 l12 -10 M150 30 l0 -16', 'g'))   # dua tangan menekan pelipis
A['C28-5'] = lantai() + matahari(250, 40, 18) + orang(130, tinggi=165, jenis='pria', baju='a', wajah='lelah') + keringat(104, 44) + keringat(158, 40) + keringat(96, 90, .8) + keringat(166, 100, .9) + keringat(130, 120, .8)

A['C29-1'] = lantai() + rak_obat(220) + kasir(120, 200) + orang(50, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (40, -6)]}) + botol_obat(120, 108, .4)
A['C29-2'] = piring(70, 110, 50) + panah(126, 110, 176, 110, 5) + pil(230, 110, 1.2) + teks(70, 170, '✔', 26, angka=True)
A['C29-3'] = lantai() + apotek(150)
A['C29-4'] = lantai() + rumah_sakit(95, 200, 150, 120) + apotek(235, 200, 90, 90)
A['C29-5'] = potret(150, 84, 44, 'pria', 'lelah', 'a') + jalur('M118 92 q12 8 24 0 M158 92 q12 8 24 0', 't') + keringat(100, 50) + awan(236, 30, .25, 'a')

A['C30-1'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='sakit', tangan={'ki': [(4, 36), (2, 64)], 'ka': [(4, 36), (2, 64)]}) + jalur('M120 150 l-12 -2 M118 164 l-12 4 M182 150 l12 -2 M184 164 l12 4', 'g')
A['C30-2'] = lantai() + orang(90, tinggi=165, jenis='wanita', baju='a', rambut='uban', wajah='marah', tangan={'ka': [(20, -10), (44, -20)]}) + kursi_depan(220, 150) + orang(220, tinggi=120, jenis='laki', duduk=150, baju='h', wajah='senyum', tangan={'ki': [(10, 14), (24, 10)], 'ka': [(10, 14), (24, 10)]}) + ponsel(220, 130, .8)
A['C30-3'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='sakit') + perban(158, 150, 18, 30)
A['C30-4'] = lantai() + orang(150, tinggi=190, jenis='pria', baju='a', badan=.8, kaki_pose={'ki': (-10, 0), 'ka': (10, 0)}) + panah(210, 90, 210, 196, 3) + panah(210, 196, 210, 92, 3)
A['C30-5'] = lantai() + orang(70, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(16, -6), (30, -14)]}) + kamera(116, 76, .6) + orang(220, tinggi=150, jenis='wanita', baju='a', wajah='kaget', tangan={'ki': [(4, 30), (6, 60)], 'ka': [(4, 30), (6, 60)]}) + teks(150, 36, '!', 30, angka=True)

A['C31-1'] = lantai() + jam_kecil(60, 44, 8, 20, 26) + pintu(150, 200, 140, 60) + jalan_kaki(210, 'laki', 140, 'a', 'kaget') + keringat(230, 70)
A['C31-2'] = lantai() + papan_tulis(80, 26, 110, 60) + orang(70, tinggi=160, jenis='wanita', baju='a', wajah='marah', tangan={'ka': [(16, -10), (26, -40)]}) + jam_kecil(126, 30, 8, 30, 18) + pintu(230, 200, 140, 60) + orang(230, tinggi=130, jenis='laki', baju='h', wajah='kaget')
A['C31-3'] = lantai() + papan_tulis(80, 26, 120, 64) + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -6), (50, -12)]}) + orang(220, tinggi=130, jenis='laki', baju='h', tangan=ANGKAT)
A['C31-4'] = lantai() + orang(150, tinggi=140, jenis='gadis', baju='a', wajah='puas', tangan=ANGKAT) + lampu_ide(210, 40)
A['C31-5'] = lembar_soal(150, 20)

A['C32-1'] = pantai() + orang(190, kaki=196, tinggi=120, jenis='pria', baju='p', wajah='puas')
A['C32-2'] = pantai() + orang(160, kaki=196, tinggi=120, jenis='wanita', baju='a') + orang(230, kaki=196, tinggi=80, jenis='laki', baju='h') + bola(270, 186, 10)
A['C32-3'] = kalender_senin(150, 20, 2, 3) + sekolah(150, 200, 120, 70) + silang(150, 164, 40, 8)
A['C32-4'] = lantai() + ''.join(salju(30 + (i * 67) % 250, 20 + (i * 29) % 60, 6) for i in range(8)) + pesawat(110, 110, .4) + panah(170, 110, 210, 130, 4) + rumah(245, 200, 80, 60)
A['C32-5'] = lantai() + meja(150, 150, 230) + buku_tumpuk(80, 150, 4, 60, 16) + buku_tumpuk(220, 150, 4, 60, 16) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='lelah', tangan=TA) + keringat(120, 50)

_cyg, _rg = sendi(150, LANTAI, 165, 'pria')['cy'], sendi(150, LANTAI, 165, 'pria')['r']
A['C33-1'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(20, 0), (40, -20)]}) + toga(150, _cyg, _rg) + gulungan(206, 50, .45)
A['C33-2'] = kalender_tahun(95, 50, 2026) + teks(95, 146, '今年', 20) + kalender_tahun(205, 50, 2027, True) + toga(205, 104, 20)
A['C33-3'] = lantai() + meja(170, 140, 200) + kertas(150, 126, 60, 24) + kertas(210, 126, 50, 22, 6) + teks(150, 130, '中', 14) + teks(210, 130, '文', 14) + orang(80, tinggi=165, jenis='pria', baju='p', kacamata=True, duduk=150, tangan={'ka': [(22, 10), (54, 14)]})
A['C33-4'] = kalender_tahun(95, 50, 2026) + teks(95, 146, '今年', 20) + kalender_tahun(205, 50, 2027, True) + toga(205, 104, 20)
_p3, _pos3 = podium(150)
A['C33-5'] = lantai() + _p3 + orang(_pos3[1][0], kaki=_pos3[1][1], tinggi=100, jenis='pria', baju='a', wajah='puas', tangan=ANGKAT) + bulat(150, 64, 8, 'a') + garis((144, 50), (150, 58), (156, 50), k='t')

A['C34-1'] = lantai() + meja(170, 140, 200) + kertas(190, 126, 80, 24) + teks(180, 132, '永', 18) + orang(80, tinggi=160, jenis='pria', baju='a', duduk=150, tangan={'ka': [(22, 0), (60, -10)]}) + garis((150, 108), (176, 124), lebar=4) + kotak(146, 100, 8, 12, 'h', 2)
A['C34-2'] = lantai() + meja(150, 140, 220) + kertas(150, 126, 90, 24) + teks(150, 132, '永', 18) + orang(80, tinggi=130, jenis='gadis', duduk=150, baju='a', tangan={'ka': [(22, 0), (44, -8)]}) + garis((110, 118), (128, 124), lebar=4) + orang(230, tinggi=165, jenis='wanita', baju='h', rambut='uban', tangan={'ki': [(20, 10), (40, 20)]})
A['C34-3'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='kaget', tangan={'ka': [(20, 20), (46, 20)]}) + kamus(190, 180, 90, 110)
A['C34-4'] = lantai() + meja(170, 150, 200) + kamus(190, 150, 80, 90) + orang(80, tinggi=150, jenis='pria', duduk=160, baju='h', tangan={'ka': [(22, 10), (60, 20)]})
A['C34-5'] = lantai() + papan_tulis(80, 26, 110, 60) + orang(170, tinggi=165, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(16, -20), (18, -46)]}) + teks(204, 54, '1', 26, angka=True) + jalur('M230 60 a14 14 0 1 1 -4 -12', 'g') + bentuk((226, 42), (234, 48), (224, 52), k='h')

A['C35-1'] = lantai() + papan_tulis(100, 26, 170, 90) + teks(70, 80, '你好', 24, warna='#fff') + orang(230, tinggi=165, jenis='pria', baju='a', kacamata=True, tangan={'ki': [(10, -10), (30, -40)]})
A['C35-2'] = lantai() + papan_tulis(100, 26, 170, 90) + teks(80, 80, '學', 30, warna='#fff') + orang(230, tinggi=165, jenis='wanita', baju='a', tangan={'ki': [(10, -10), (30, -40)]})
A['C35-3'] = lantai() + meja_bundar(150, 140, 200) + orang(60, tinggi=120, jenis='gadis', duduk=160, baju='a') + orang(240, tinggi=125, jenis='laki', duduk=160, baju='h') + orang(150, kaki=200, tinggi=80, jenis='laki', baju='p') + titik_obrolan(80, 40, 56, 30, (1, 1)) + titik_obrolan(220, 40, 56, 30, (-1, 1))
A['C35-4'] = lantai() + papan_tulis(80, 26, 110, 60) + orang(70, tinggi=165, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + meja_kelas(150) + meja_kelas(250) + orang(250, tinggi=130, jenis='laki', baju='h') + murid_belakang(150, 200, 100, 'gadis')
A['C35-5'] = lantai() + papan_tulis(80, 26, 120, 70) + orang(170, tinggi=165, jenis='pria', baju='a', tangan={'ki': [(20, -10), (50, -30)]}) + murid_belakang(235, 200, 110) + murid_belakang(275, 200, 110, 'gadis')

A['C36-1'] = lantai() + meja(180, 140, 190) + timbangan(200, 50, .8) + buku(150, 140, 40, 30, 'h') + orang(70, tinggi=150, jenis='pria', duduk=150, baju='a')
A['C36-2'] = lantai() + timbangan(210, 40, 1.0) + orang(90, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(16, 14), (30, 10)]}) + buku(130, 110, 36, 40, 'h')
A['C36-3'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='nyanyi') + gelembung(70, 50, 100, 50, teks(70, 58, '你好', 22), (1, 1)) + gelembung(232, 50, 100, 50, teks(232, 58, 'Lí hó', 18, angka=True), (-1, 1))
A['C36-4'] = lantai() + meja(160, 140, 200) + gulungan(160, 118, .7) + orang(60, tinggi=150, jenis='wanita', duduk=150, baju='a') + bentuk((222, 60), (262, 60), (242, 30), k='a') + ''.join(kotak(225 + i * 12, 60, 6, 40, 'p') for i in range(3))
A['C36-5'] = lantai() + gedung(150, tingkat=5, lebar=190) + ''.join(bintang(90 + i * 30, 44, 9) for i in range(5)) + lampu_kristal(150, 130, 1.0)


# ================= komponen C37–C48 =================
def papan_isi(isi, uk=40, x=150, y=30, w=220, h=110):
    return papan_tulis(x, y, w, h) + teks(x, y + h / 2 + uk * .36, isi, uk, angka=True, warna='#fff')


def diagram(persen, x=150, y=110, r=80, ikon=''):
    a = math.radians(persen * 3.6)
    besar = 1 if persen > 50 else 0
    o = bulat(x, y, r, 'p')
    if persen >= 100:
        o += bulat(x, y, r, 'a')
    else:
        o += jalur(f'M{f(x)} {f(y)} L{f(x)} {f(y - r)} A{f(r)} {f(r)} 0 {besar} 1 {f(x + math.sin(a) * r)} {f(y - math.cos(a) * r)} Z', 'a')
    return o + ikon


def antrean(x0=40, n=6, lantai_y=LANTAI):
    return ''.join(orang(x0 + i * 40, tinggi=140 - (i % 3) * 8, jenis='wanita' if i % 2 else 'pria', baju='h' if i % 3 == 0 else 'a') for i in range(n))


def harga_coret(x, y):
    return label_harga(x - 30, y, '100', 120, 50) + garis((x - 80, y + 36), (x + 10, y + 16), lebar=5) + label_harga(x + 40, y + 70, '80', 120, 50)


def sarung_tangan(x, y, s=1.0, k='a'):
    return (jalur(f'M{f(x - 22 * s)} {f(y + 40 * s)} L{f(x - 24 * s)} {f(y - 10 * s)} Q{f(x - 24 * s)} {f(y - 30 * s)} {f(x - 14 * s)} {f(y - 30 * s)} L{f(x - 14 * s)} {f(y - 44 * s)} Q{f(x - 8 * s)} {f(y - 52 * s)} {f(x - 2 * s)} {f(y - 44 * s)} '
                  f'L{f(x)} {f(y - 50 * s)} Q{f(x + 6 * s)} {f(y - 58 * s)} {f(x + 12 * s)} {f(y - 50 * s)} L{f(x + 14 * s)} {f(y - 44 * s)} Q{f(x + 20 * s)} {f(y - 50 * s)} {f(x + 26 * s)} {f(y - 42 * s)} '
                  f'L{f(x + 24 * s)} {f(y - 10 * s)} L{f(x + 36 * s)} {f(y - 22 * s)} Q{f(x + 44 * s)} {f(y - 18 * s)} {f(x + 36 * s)} {f(y - 4 * s)} L{f(x + 22 * s)} {f(y + 40 * s)} Z', k)
            + kotak(x - 24 * s, y + 30 * s, 48 * s, 14 * s, 'h', 3))


def sweter(x, y, s=1.0):
    o = kaos(x, y, s, 'a') + kotak(x - 30 * s, y + 20 * s, 60 * s, 10 * s, 'h')
    return o + ''.join(jalur(f'M{f(x - 22 * s + i * 11 * s)} {f(y - 20 * s)} l{f(5 * s)} {f(8 * s)} l{f(5 * s)} {f(-8 * s)}', 't') for i in range(4)) + ''.join(jalur(f'M{f(x - 22 * s + i * 11 * s)} {f(y + 2 * s)} l{f(5 * s)} {f(8 * s)} l{f(5 * s)} {f(-8 * s)}', 't') for i in range(4))


def sandal(x, y, s=1.0):
    return (elips(x, y, 22 * s, 44 * s, 'a') + jalur(f'M{f(x - 16 * s)} {f(y - 4 * s)} Q{f(x)} {f(y - 26 * s)} {f(x + 16 * s)} {f(y - 4 * s)}', 'g', 6 * s))


def mesin_edc(x, y, s=1.0):
    return kotak(x - 24 * s, y - 36 * s, 48 * s, 72 * s, 'h', 6) + kotak(x - 18 * s, y - 30 * s, 36 * s, 20 * s, 'a', 2) + ''.join(kotak(x - 16 * s + (i % 3) * 12 * s, y - 2 * s + (i // 3) * 10 * s, 8 * s, 6 * s, 'n', 1) for i in range(9))


def koin(x, y, r=12):
    return bulat(x, y, r, 'a') + bulat(x, y, r * .6, 't')


def membungkuk(x, jenis='wanita', baju='a'):
    s_ = sendi(x, LANTAI, 160, jenis)
    return (orang(x, tinggi=160, jenis=jenis, baju=baju, wajah='puas', tangan={'ki': [(4, 26), (-12, 42)], 'ka': [(4, 26), (-12, 42)]}) + jalur(f'M{f(x - 30)} {f(s_["cy"] - 30)} q30 -16 60 0', 't'))


def tongkat(x, y1, y2):
    return garis((x, y1), (x + 4, y2), lebar=4) + jalur(f'M{f(x)} {f(y1)} q-12 -6 -14 6', 'g', 4)


def bento(x, y, s=1.0):
    o = kotak(x - 60 * s, y - 36 * s, 120 * s, 72 * s, 'h', 6) + kotak(x - 54 * s, y - 30 * s, 60 * s, 60 * s, 'p', 3)
    o += kotak(x + 10 * s, y - 30 * s, 44 * s, 28 * s, 'a', 3) + kotak(x + 10 * s, y + 2 * s, 44 * s, 28 * s, 'a', 3)
    return o + ''.join(bulat(x - 42 * s + (i % 4) * 12 * s, y - 20 * s + (i // 4) * 12 * s, 2.4 * s, 't') for i in range(16)) + telur_ceplok(x + 32 * s, y + 18 * s, .4 * s)


def tahu(x, y, s=1.0):
    return kotak(x - 20 * s, y - 16 * s, 40 * s, 32 * s, 'p', 3) + kotak(x + 4 * s, y - 24 * s, 30 * s, 26 * s, 'p', 3)


def mangga(x, y, s=1.0):
    return (jalur(f'M{f(x - 26 * s)} {f(y + 8 * s)} Q{f(x - 30 * s)} {f(y - 30 * s)} {f(x + 6 * s)} {f(y - 30 * s)} Q{f(x + 34 * s)} {f(y - 28 * s)} {f(x + 28 * s)} {f(y + 4 * s)} Q{f(x + 22 * s)} {f(y + 28 * s)} {f(x - 6 * s)} {f(y + 26 * s)} Q{f(x - 22 * s)} {f(y + 24 * s)} {f(x - 26 * s)} {f(y + 8 * s)} Z', 'a')
            + garis((x + 6 * s, y - 30 * s), (x + 10 * s, y - 38 * s), lebar=3) + jalur(f'M{f(x + 10 * s)} {f(y - 36 * s)} q{f(14 * s)} {f(-8 * s)} {f(22 * s)} 0 q{f(-10 * s)} {f(8 * s)} {f(-22 * s)} 0 Z', 'h'))


def anggur(x, y, s=1.0):
    o = garis((x, y - 44 * s), (x, y - 30 * s), lebar=3) + jalur(f'M{f(x)} {f(y - 40 * s)} q{f(16 * s)} {f(-10 * s)} {f(26 * s)} {f(-2 * s)} q{f(-12 * s)} {f(8 * s)} {f(-26 * s)} {f(2 * s)} Z', 'h')
    for j, n in enumerate((4, 3, 3, 2, 1)):
        for i in range(n):
            o += bulat(x - (n - 1) * 8 * s + i * 16 * s, y - 24 * s + j * 13 * s, 8 * s, 'a' if (i + j) % 2 else 'h')
    return o


def jeruk(x, y, s=1.0):
    return bulat(x, y, 24 * s, 'a') + bulat(x, y - 20 * s, 2.6 * s, 'h') + jalur(f'M{f(x)} {f(y - 22 * s)} q{f(10 * s)} {f(-10 * s)} {f(18 * s)} {f(-4 * s)} q{f(-8 * s)} {f(8 * s)} {f(-18 * s)} {f(4 * s)} Z', 'h') + ''.join(bulat(x + dx * s, y + dy * s, 1.4 * s, 'h') for dx, dy in ((-8, 4), (6, -4), (10, 10), (-2, 12)))


def steak(x, y, s=1.0, matang=True):
    o = jalur(f'M{f(x - 50 * s)} {f(y)} Q{f(x - 54 * s)} {f(y - 30 * s)} {f(x - 10 * s)} {f(y - 30 * s)} Q{f(x + 50 * s)} {f(y - 34 * s)} {f(x + 52 * s)} {f(y - 4 * s)} Q{f(x + 40 * s)} {f(y + 20 * s)} {f(x)} {f(y + 18 * s)} Q{f(x - 44 * s)} {f(y + 18 * s)} {f(x - 50 * s)} {f(y)} Z', 'h' if matang else 'a')
    return o + ''.join(garis((x - 30 * s + i * 20 * s, y - 20 * s), (x - 20 * s + i * 20 * s, y + 8 * s), k='w') for i in range(4))


def salad(x, y, s=1.0):
    return (jalur(f'M{f(x - 60 * s)} {f(y)} Q{f(x)} {f(y + 50 * s)} {f(x + 60 * s)} {f(y)} Z', 'p') + ''.join(daun(x + dx * s, y + dy * s, 1.4 * s) for dx, dy in ((-36, -6), (-12, -12), (14, -8), (36, -4), (0, -2)))
            + bulat(x - 20 * s, y - 14 * s, 6 * s, 'h') + bulat(x + 24 * s, y - 16 * s, 6 * s, 'h'))


def nampan_paket(x, y, s=1.0):
    return (kotak(x - 90 * s, y - 50 * s, 180 * s, 100 * s, 'a', 8) + mangkuk_mi(x - 46 * s, y - 16 * s, .3 * s, sumpit=False, uap=False) + piring(x + 40 * s, y - 10 * s, 36 * s, daging(x + 40 * s, y - 14 * s, .5 * s))
            + elips(x - 40 * s, y + 28 * s, 26 * s, 12 * s, 'p') + cangkir(x + 50 * s, y + 38 * s, .35 * s, False))


def meja_reserved(x, lantai_y=LANTAI):
    return meja(x, lantai_y - 60, 130) + kotak(x - 20, lantai_y - 84, 40, 24, 'p', 3) + garis((x - 12, lantai_y - 76), (x + 12, lantai_y - 76), k='t') + garis((x - 12, lantai_y - 68), (x + 8, lantai_y - 68), k='t')


# ================= C37–C48 =================
A['C37-1'] = lantai() + papan_isi('2.5', 60)
A['C37-2'] = lantai() + papan_isi('3 + 5 = 8', 44)
A['C37-3'] = lantai() + papan_isi('10 − 4 = 6', 42)
A['C37-4'] = lantai() + papan_isi('10 + 10 = 20', 38)
A['C37-5'] = kertas(150, 110, 150, 180, 0) + teks(150, 84, '98.5', 48, angka=True) + bulat(150, 70, 56, 'g')

A['C38-1'] = diagram(50) + teks(150, 214, '', 1)
A['C38-2'] = diagram(50, 120, 110, 80) + cangkir(120 + 40, 96, .45, False) + cangkir(250, 190, .8, True)
A['C38-3'] = lantai() + pohon(40, s=.8) + pohon(265, s=.7) + ''.join(jalan_kaki(x, j, t, b) for x, j, t, b in ((80, 'wanita', 120, 'a'), (125, 'pria', 130, 'h'), (170, 'wanita', 118, 'p'), (215, 'pria', 126, 'a')))
A['C38-4'] = diagram(100 / 3, 110, 110, 80) + ''.join(orang(215 + i * 30, tinggi=70, jenis='laki', baju='h' if i == 0 else 'p') for i in range(3)) + topi_di(215, sendi(215, 200, 70, 'laki')['cy'], sendi(215, 200, 70, 'laki')['r'])
A['C38-5'] = diagram(90)

A['C39-1'] = termometer(150, 30, 31, 40, 140) + teks(215, 110, '31°', 30, angka=True)
A['C39-2'] = kotak(16, 16, 268, 188, 'h', 4) + kotak(24, 24, 252, 172, 'p') + ''.join(orang(46 + (i % 7) * 34, kaki=110 + (i // 7) * 80, tinggi=62, jenis='laki' if i % 2 else 'gadis', baju='a' if i % 3 else 'h') for i in range(14)) + papan_angka(230, 150, '21人', 70, 30, False, 20)
A['C39-3'] = lantai() + rambu(150, orang(150, kaki=140, tinggi=60, jenis='laki', baju='h'), True, 200, 50) + teks(215, 80, '12↓', 28, angka=True)
A['C39-4'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a') + kue_ultah(90, 60, '20', .35) + orang(200, tinggi=110, jenis='laki', baju='h') + kue_ultah(200, 110, '10', .35)
A['C39-5'] = lantai() + rambu(150, mobil(150, 176, 60), False, 200, 50) + teks(225, 70, '18+', 30, angka=True)

A['C40-1'] = lantai() + toko(250, 200, 80, 110) + antrean(30, 5)
A['C40-2'] = harga_coret(150, 50)
A['C40-3'] = lantai() + kotak(210, 60, 80, 140, 'p') + kotak(226, 110, 48, 90, 'h') + antrean(20, 5)
A['C40-4'] = lantai() + bulan_bintang(250, 26, .45) + garis((20, 50), (280, 50), k='t') + ''.join(lampion(40 + i * 44, 62, .6) for i in range(6)) + ''.join(orang(30 + i * 30, tinggi=110 - (i % 3) * 10, jenis='wanita' if i % 2 else 'pria', baju='h' if i % 3 == 0 else 'a') for i in range(9))
A['C40-5'] = lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(160, 198, 1.9) + jalur('M54 150 l-14 -6 M52 170 l-16 0', 'g')

_cyw, _rw = sendi(150, LANTAI, 165, 'wanita')['cy'], sendi(150, LANTAI, 165, 'wanita')['r']
A['C41-1'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', tangan={'ki': [(20, 20), (30, 0)], 'ka': [(20, 20), (30, 0)]}) + sarung_tangan(104, 96, .5, 'h') + sarung_tangan(196, 96, .5, 'h')
A['C41-2'] = lantai() + ''.join(salju(40 + (i * 67) % 230, 20 + (i * 31) % 60, 6) for i in range(8)) + sweter(150, 120, 1.6)
A['C41-3'] = lantai() + sandal(115, 120, 1.2) + sandal(185, 120, 1.2)
A['C41-4'] = lantai() + ''.join(salju(40 + (i * 67) % 230, 20 + (i * 31) % 60, 6) for i in range(8)) + sarung_tangan(110, 130, 1.2, 'a') + sarung_tangan(190, 130, 1.2, 'h')
A['C41-5'] = lantai() + sofa(210, 200, 120) + orang(80, tinggi=160, jenis='pria', baju='a') + sandal(64, 198, .3) + sandal(96, 198, .3)

A['C42-1'] = lantai() + kasir(200) + mesin_edc(170, 90, .8) + orang(80, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 0), (50, -2)]}) + kartu_kredit(150, 76, .5)
A['C42-2'] = lantai() + kasir(210) + mesin_edc(180, 90, .7) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -10), (40, -20)]}) + kartu_kredit(136, 60, .55)
A['C42-3'] = lantai() + meja(150, 130, 220) + piring(100, 124, 40) + koin(190, 120, 10) + koin(212, 122, 10) + koin(200, 108, 10) + silang(200, 116, 30, 6)
A['C42-4'] = kotak(90, 60, 120, 90, 'p', 12) + kotak(98, 68, 104, 74, 'a', 8) + teks(150, 116, '?', 34, angka=True) + label_harga(240, 150, '1000', 90, 40)
A['C42-5'] = lantai() + kasir(220) + membungkuk(150, 'wanita', 'h')

A['C43-1'] = lantai() + orang(130, tinggi=165, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(12, 30), (22, 50)]}) + keranjang(170, 170, .9)
A['C43-2'] = lantai() + keranjang(150, 196, 2.2) + buah_apel(120, 132, .7) + buah_apel(160, 128, .7) + pisang(170, 140, .4)
A['C43-3'] = lantai() + toko(130, 200, 170, 120) + ''.join(orang(220 + i * 26, tinggi=100 + (i % 2) * 14, jenis='wanita' if i % 2 else 'pria', baju='h' if i % 2 else 'a') for i in range(3)) + orang(90, tinggi=80, jenis='pria', baju='p')
A['C43-4'] = lantai() + kios_buah(150, 200, 200) + orang(150, tinggi=150, jenis='wanita', baju='h', rambut='uban', wajah='tawa', tangan=LAMBAI)
A['C43-5'] = lantai() + orang(150, tinggi=150, jenis='nenek', rambut='uban', rok=False, baju='a', tangan={'ka': [(14, 30), (24, 56)]}) + tongkat(178, 110, 200) + jalur('M100 170 l-20 0 M104 184 l-16 0', 'g')

A['C44-1'] = kaos(150, 110, 1.9, 'birutua')
A['C44-2'] = lantai() + kasir(210) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (46, -6)]}) + kaos(150, 80, .4, 'p') + panah(140, 40, 190, 40, 4) + panah(190, 54, 140, 54, 4)
A['C44-3'] = bentuk((16, 60), (284, 60), (284, 204), (16, 204), k='a') + jalur('M24 70 q10 -8 20 0 t20 0 t20 0 M180 80 q10 -8 20 0 t20 0', 'w') + potret(150, 50, 16, 'pria', 'kaget', 'p')[:0] + bulat(150, 50, 14) + muka(150, 50, 14, 'kaget') + panah(250, 70, 250, 196, 3) + panah(250, 196, 250, 72, 3)
A['C44-4'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 0), (46, -6)]}) + kaos(150, 80, .4, 'a') + kasir(220) + panah(170, 40, 210, 40, 4) + panah(210, 54, 170, 54, 4)
A['C44-5'] = lantai() + bentuk((16, 176), (284, 176), (284, 204), (16, 204), k='a') + jalur('M24 186 q10 -8 20 0 t20 0 t20 0 M180 190 q10 -8 20 0 t20 0', 'w') + orang(150, kaki=196, tinggi=160, jenis='laki', baju='a', wajah='puas')

A['C45-1'] = lantai() + meja(150, 150, 220) + bento(150, 124, .7) + orang(150, kaki=150, tinggi=90, jenis='pria', baju='a', wajah='puas')[:0] + orang(60, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='puas', tangan={'ka': [(20, 10), (50, 4)]})
A['C45-2'] = lantai(196, 30, 270) + bento(150, 130, 1.4)
A['C45-3'] = lantai() + meja(170, 140, 200) + mangkuk_mi(170, 110, .45, sumpit=False) + garam(240, 132, .8) + orang(70, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (44, 4)]}) + jalur('M60 30 l0 0', 't') + teks(110, 40, '↓', 28, angka=True)
A['C45-4'] = lantai() + meja(150, 150, 220) + bento(190, 124, .6) + orang(80, tinggi=150, jenis='wanita', duduk=160, baju='a', wajah='tawa', tangan={'ka': [(16, -4), (26, -30)]}) + jempol(120, 60, 1.0)
A['C45-5'] = lantai() + meja(150, 150, 240) + piring(90, 144, 40, ikan(90, 136, .5)) + piring(230, 144, 40, tahu(230, 134, .6)) + silang(230, 124, 26, 6) + orang(150, tinggi=150, jenis='pria', baju='h', wajah='marah', tangan={'ka': [(20, 10), (44, 20)]})

A['C46-1'] = lantai() + mangga(80, 160, 1.2) + mangga(150, 160, 1.2) + mangga(220, 160, 1.2)
A['C46-2'] = mangga(150, 120, 2.6)
A['C46-3'] = anggur(150, 120, 2.2)
A['C46-4'] = lantai() + jeruk(80, 170, 1.2) + jeruk(150, 170, 1.2) + jeruk(220, 170, 1.2)
A['C46-5'] = lantai() + matahari(250, 40, 18) + mangga(130, 140, 2.0)

A['C47-1'] = lantai() + meja(150, 150, 240) + piring(150, 144, 90, steak(150, 132, 1.0)) + uap_(150, 100, 1.2)
A['C47-2'] = lantai() + meja(150, 150, 240) + piring(150, 144, 90, steak(150, 132, 1.0)) + centang(230, 60, 1.4) + uap_(150, 100, 1.0)
A['C47-3'] = lantai() + meja(150, 150, 240) + piring(210, 144, 50) + pegang_perut(90, 'pria', 150, 'a', 'lapar') + jalur('M60 130 q8 -8 16 0 t16 0', 'g') + keringat(64, 40)
A['C47-4'] = lantai() + piring(150, 150, 110, steak(150, 138, 1.3)) + garis((130, 104), (140, 150), k='w') + kotak(122, 110, 14, 30, 'a')
A['C47-5'] = lantai() + orang(150, kaki=200, tinggi=140, jenis='wanita', baju='a', wajah='lelah', duduk=196, tangan={'ki': [(20, 30), (40, 50)], 'ka': [(20, 30), (40, 50)]}) + keringat(120, 80) + keringat(184, 76)

A['C48-1'] = kotak(16, 16, 268, 188, 'p') + jendela(90, 40, 100, 80) + meja(90, 150, 110) + kursi_depan(40, 150)[:0] + meja(230, 150, 90) + panah(90, 130, 90, 142, 2) + tunjuk_ke(200, 'wanita', 150, -1, 'a')
A['C48-2'] = lantai(196, 40, 260) + salad(150, 120, 1.6)
A['C48-3'] = dua_panel(orang_ponsel(75, 'wanita', 150, baju='a') + sinyal(108, 70), meja_reserved(225))
A['C48-4'] = dua_panel(orang_ponsel(75, 'pria', 155, baju='h') + sinyal(108, 70), meja_reserved(225) + kotak(165, 40, 110, 60, 'p') + mangkuk_mi(220, 66, .25, sumpit=False))
A['C48-5'] = nampan_paket(150, 110, 1.2)


# ---------------- perbaikan C37–C48 ----------------
def bento(x, y, s=1.0):   # versi baru: nasi putih + umeboshi, lauk di sekat, sumpit (tanpa pola titik)
    o = kotak(x - 64 * s, y - 38 * s, 128 * s, 76 * s, 'h', 8) + kotak(x - 58 * s, y - 32 * s, 62 * s, 64 * s, 'p', 4) + bulat(x - 27 * s, y, 7 * s, 'h')
    o += kotak(x + 10 * s, y - 32 * s, 48 * s, 30 * s, 'p', 3) + telur_ceplok(x + 34 * s, y - 14 * s, .45 * s)
    o += kotak(x + 10 * s, y + 2 * s, 48 * s, 30 * s, 'p', 3) + daging(x + 34 * s, y + 20 * s, .38 * s)
    return o + garis((x - 70 * s, y + 46 * s), (x + 70 * s, y + 34 * s), lebar=4) + garis((x - 70 * s, y + 54 * s), (x + 70 * s, y + 42 * s), lebar=4)


def uang_kertas(x, y, nilai, w=120, h=60):
    return kotak(x - w / 2, y - h / 2, w, h, 'a', 4) + bulat(x - w / 2 + 22, y, 14, 'p') + teks(x + 16, y + 10, nilai, 26, angka=True)


A['C39-3'] = lantai() + rambu(150, orang(150, kaki=78, tinggi=50, jenis='laki', baju='h'), True, 200, 50) + teks(222, 72, '12', 30, angka=True) + panah(250, 50, 250, 84, 3)
A['C39-4'] = (lantai() + orang(90, tinggi=165, jenis='pria', baju='a') + gelembung(150, 30, 70, 40, teks(150, 40, '20', 26, angka=True), (-1, 1))
              + orang(215, tinggi=110, jenis='laki', baju='h') + gelembung(265, 80, 60, 36, teks(265, 90, '10', 24, angka=True), (-1, 1)))
A['C39-5'] = lantai() + rambu(150, '<g transform="translate(150 52) scale(.36) translate(-150 -150)">' + mobil(150, 200, 180) + '</g>', False, 200, 50) + teks(228, 70, '18+', 30, angka=True)
A['C41-5'] = lantai() + sofa(150, 200, 200) + orang(150, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='puas') + sandal(126, 196, .42).replace('rotate', 'rotate') + sandal(174, 196, .42)
A['C42-4'] = uang_kertas(95, 90, '1000') + koin(200, 80, 16) + koin(232, 96, 16) + koin(206, 112, 16) + silang(215, 96, 34, 7)
A['C45-1'] = lantai() + meja(170, 150, 200) + bento(185, 122, .6) + orang(60, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='puas', tangan={'ka': [(20, 10), (50, 4)]})
A['C45-2'] = lantai(196, 30, 270) + bento(150, 120, 1.5)
A['C45-4'] = lantai() + meja(150, 150, 220) + bento(195, 122, .55) + orang(80, tinggi=150, jenis='wanita', duduk=160, baju='a', wajah='tawa', tangan={'ka': [(16, -4), (26, -30)]}) + jempol(120, 60, 1.0)


# ================= komponen C49–C60 =================
def kedelai(x, y, n=4, s=1.0):
    return ''.join(elips(x + i * 12 * s, y - (i % 2) * 5 * s, 6 * s, 5 * s, 'a') for i in range(n))


def kentang_goreng(x, bawah, s=1.0):
    return ''.join(kotak(x - 16 * s + i * 7 * s, bawah - 50 * s - (i % 3) * 6 * s, 5 * s, 30 * s, 'p', 1) for i in range(5)) + bentuk((x - 20 * s, bawah - 28 * s), (x + 20 * s, bawah - 28 * s), (x + 16 * s, bawah), (x - 16 * s, bawah), k='h')


def mi_cup(x, bawah, s=1.0):
    return (bentuk((x - 34 * s, bawah - 80 * s), (x + 34 * s, bawah - 80 * s), (x + 26 * s, bawah), (x - 26 * s, bawah), k='p') + kotak(x - 34 * s, bawah - 60 * s, 68 * s, 22 * s, 'h')
            + jalur(f'M{f(x - 30 * s)} {f(bawah - 80 * s)} q{f(8 * s)} {f(-12 * s)} {f(16 * s)} 0 t{f(16 * s)} 0 t{f(16 * s)} 0 t{f(12 * s)} 0', 't') + uap_(x, bawah - 90 * s, s))


def kartu_arc(x, y, s=1.0):
    return (kotak(x - 70 * s, y - 44 * s, 140 * s, 88 * s, 'p', 8) + kotak(x - 70 * s, y - 44 * s, 140 * s, 18 * s, 'a', 8) + kotak(x - 58 * s, y - 18 * s, 40 * s, 50 * s, 'a', 3)
            + bulat(x - 38 * s, y - 2 * s, 9 * s, 'p') + ''.join(garis((x - 6 * s, y - 12 * s + i * 12 * s), (x + 56 * s, y - 12 * s + i * 12 * s), k='t') for i in range(4)))


def celengan(x, bawah, s=1.0):
    return (elips(x, bawah - 34 * s, 46 * s, 32 * s, 'a') + bulat(x + 38 * s, bawah - 44 * s, 12 * s, 'a') + elips(x + 48 * s, bawah - 40 * s, 6 * s, 5 * s, 'p')
            + kotak(x - 10 * s, bawah - 68 * s, 20 * s, 4 * s, 'h') + ''.join(garis((x + dx * s, bawah - 8 * s), (x + dx * s, bawah), lebar=7 * s) for dx in (-28, -10, 14, 30))
            + bentuk((x + 22 * s, bawah - 62 * s), (x + 30 * s, bawah - 76 * s), (x + 34 * s, bawah - 60 * s), k='a') + koin(x, bawah - 84 * s, 9 * s))


def pencuri(x, tinggi=150):
    s_ = sendi(x, LANTAI, tinggi, 'pria')
    return orang(x, tinggi=tinggi, jenis='pria', baju='h', wajah='kaget', tangan={'ki': [(20, -10), (30, -40)], 'ka': [(20, -10), (30, -40)]}) + kotak(x - s_['r'], s_['cy'] - s_['r'] * .35, s_['r'] * 2, s_['r'] * .5, 'h', 3) + bulat(x - s_['r'] * .38, s_['cy'] - s_['r'] * .1, s_['r'] * .12, 'n') + bulat(x + s_['r'] * .38, s_['cy'] - s_['r'] * .1, s_['r'] * .12, 'n')


def polisi(x, tinggi=165, tangan=None):
    s_ = sendi(x, LANTAI, tinggi, 'pria')
    return orang(x, tinggi=tinggi, jenis='pria', baju='a', tangan=tangan) + kotak(x - s_['r'] * 1.2, s_['cy'] - s_['r'] * 1.25, s_['r'] * 2.4, s_['r'] * .55, 'h', 3) + kotak(x - s_['r'] * 1.4, s_['cy'] - s_['r'] * .75, s_['r'] * 2.8, s_['r'] * .2, 'h') + bintang(x, s_['cy'] - s_['r'] * 1.0, s_['r'] * .2).replace('class="h"', 'class="n"')


def rantai_putus(x, y):
    return (elips(x - 22, y, 12, 7, 't') + elips(x - 6, y, 12, 7, 't') + elips(x + 20, y + 4, 12, 7, 't') + jalur(f'M{f(x + 4)} {f(y - 10)} l6 20', 'g', 3))


def tebing(x=150):
    return bentuk((16, 90), (190, 90), (200, 204), (16, 204), k='a') + garis((190, 90), (200, 204), lebar=3) + lantai(204, 200, 284)


def tanda_bahaya(x, y, s=1.0):
    return bentuk((x, y - 30 * s), (x + 30 * s, y + 22 * s), (x - 30 * s, y + 22 * s), k='kuning') + teks(x, y + 16 * s, '!', 32 * s, angka=True) + garis((x, y + 22 * s), (x, y + 80 * s), lebar=4)


def pipa_limbah(x, y):
    return kotak(x - 60, y, 60, 14, 'h') + jalur(f'M{f(x)} {f(y + 7)} q14 0 14 20 q0 10 -8 24', 'g', 6)


def tong_daur(x, bawah, k='a'):
    return kotak(x - 24, bawah - 56, 48, 56, k, 4) + kotak(x - 28, bawah - 64, 56, 10, 'h', 3) + jalur(f'M{f(x - 10)} {f(bawah - 36)} l10 -12 l10 12 M{f(x + 10)} {f(bawah - 30)} l-10 10 l-10 -10', 'w' if k == 'h' else 'g', 3)


def sinterklas(x, tinggi=165, tangan=None):
    s_ = sendi(x, LANTAI, tinggi, 'pria')
    r = s_['r']
    o = orang(x, tinggi=tinggi, jenis='pria', baju='a', badan=1.35, wajah='puas', tangan=tangan)
    o += jalur(f'M{f(x - r * 1.1)} {f(s_["cy"] + r * .1)} Q{f(x)} {f(s_["cy"] + r * 2.6)} {f(x + r * 1.1)} {f(s_["cy"] + r * .1)} Q{f(x)} {f(s_["cy"] + r * 1.1)} {f(x - r * 1.1)} {f(s_["cy"] + r * .1)} Z', 'p')
    o += jalur(f'M{f(x - r * 1.1)} {f(s_["cy"] - r * .6)} Q{f(x)} {f(s_["cy"] - r * 2.6)} {f(x + r * 1.6)} {f(s_["cy"] - r * .9)} L{f(x + r * 1.1)} {f(s_["cy"] - r * .6)} Z', 'h')
    o += kotak(x - r * 1.2, s_['cy'] - r * .8, r * 2.4, r * .4, 'p', 3) + bulat(x + r * 1.7, s_['cy'] - r * .9, r * .3, 'p')
    return o + kotak(x - r * 1.9, s_['pinggang'] - r * .3, r * 3.8, r * .5, 'h')


def karung(x, bawah, s=1.0):
    return jalur(f'M{f(x - 34 * s)} {f(bawah)} Q{f(x - 44 * s)} {f(bawah - 60 * s)} {f(x - 8 * s)} {f(bawah - 70 * s)} L{f(x + 8 * s)} {f(bawah - 70 * s)} Q{f(x + 44 * s)} {f(bawah - 60 * s)} {f(x + 34 * s)} {f(bawah)} Z', 'a') + garis((x - 10 * s, bawah - 66 * s), (x + 10 * s, bawah - 66 * s), lebar=4)


def hiasan_imlek(x, lantai_y=LANTAI):
    o = pintu(x, lantai_y, 150, 80) + kotak(x - 64, lantai_y - 140, 18, 110, 'h', 2) + kotak(x + 46, lantai_y - 140, 18, 110, 'h', 2) + kotak(x - 50, lantai_y - 162, 100, 18, 'h', 2)
    o += bentuk((x - 12, lantai_y - 108), (x, lantai_y - 120), (x + 12, lantai_y - 108), (x, lantai_y - 96), k='h')
    return o + lampion(x - 90, lantai_y - 150, 1.0) + lampion(x + 90, lantai_y - 150, 1.0)


def petasan(x, y, n=5):
    return ''.join(kotak(x - 6 + (i % 2) * 8, y + i * 14, 12, 12, 'h', 2) for i in range(n)) + garis((x, y - 10), (x, y), k='t') + kembang_api(x + 30, y + 10, 14)


def plus_minus(x, y, tanda='+', k='a'):
    o = bulat(x, y, 26, k)
    o += garis((x - 14, y), (x + 14, y), lebar=6)
    if tanda == '+':
        o += garis((x, y - 14), (x, y + 14), lebar=6)
    return o


def es_krim_jatuh(x, bawah):
    return bentuk((x - 12, bawah - 40), (x + 12, bawah - 40), (x, bawah - 4), k='a') + elips(x + 34, bawah - 6, 22, 8, 'p') + bulat(x + 30, bawah - 14, 12, 'p')


def tulisan_kacau(x, y, w=150, h=100):
    o = kertas(x, y, w, h, -4)
    return o + jalur(f'M{f(x - 60)} {f(y - 20)} q10 -16 20 0 t20 -4 t14 8 t20 -10 t20 6 M{f(x - 58)} {f(y + 6)} q12 14 20 -4 t18 6 t22 -8 t20 10 M{f(x - 54)} {f(y + 30)} q8 -12 22 2 t18 -6 t20 8', 'g', 3)


# ================= C49–C60 =================
A['C49-1'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(14, 26), (-4, -6)]}) + gelas(138, 66, 'susu', .5) + gelas(215, 196, 'susu', 1.3) + kedelai(250, 190, 3)
A['C49-2'] = lantai() + meja(200, 140, 150) + hamburger(180, 136, .4) + kentang_goreng(240, 136, .8) + silang(210, 100, 40, 7) + orang(70, tinggi=160, jenis='pria', baju='a', wajah='marah', tangan={'ka': [(22, -10), (40, -20)]})
A['C49-3'] = lantai() + matahari(250, 40, 16) + meja(150, 150, 220) + gelas(140, 146, 'susu', 1.2) + kedelai(190, 140, 4, 1.2)
A['C49-4'] = lantai() + jendela(240, 30, 60, 46) + bulan_bintang(236, 52, .4) + meja(140, 150, 200) + mi_cup(140, 146, 1.0)
A['C49-5'] = lantai() + kaleng(170, 196, 1.8) + silang(170, 150, 40, 8) + orang(70, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, -10), (40, -20)]})

A['C50-1'] = lantai() + loket(200) + kartu_arc(200, 60, .45) + orang(80, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 0), (50, -6)]}) + orang(215, kaki=150, tinggi=90, jenis='wanita', baju='a')
A['C50-2'] = kartu_arc(150, 110, 1.3)
A['C50-3'] = lantai() + orang(110, tinggi=165, jenis='pria', baju='a', wajah='sakit', tangan={'ka': [(16, 30), (30, 56)]}) + koper(160, 190, 1.3) + keringat(84, 44)
A['C50-4'] = lantai() + loket(190) + orang(190, kaki=150, tinggi=100, jenis='wanita', baju='a', wajah='tawa', tangan={'ki': [(20, -4), (36, -10)]}) + orang(70, tinggi=160, jenis='pria', baju='h', wajah='puas') + bintang(260, 40, 8)
A['C50-5'] = label_harga(150, 70, '100', 170, 70) + centang(240, 40, 1.4)

A['C51-1'] = lantai() + loket(200) + gedung_bank(200, 200, 150, 60)[:0] + teks(200, 40, '$', 30, angka=True) + orang(80, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + uang_kertas(150, 100, '', 60, 30)
A['C51-2'] = lantai() + kotak_pos(210) + orang(100, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(22, -4), (46, -14)]}) + amplop(152, 72, 42, 28, -10)
A['C51-3'] = lantai() + celengan(120, 196, 1.3) + kalender_bulan(240, 40, 3, '', 80, 80)
A['C51-4'] = lantai() + kotak_pos(220) + orang(110, tinggi=165, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(20, -10), (36, -30)]}) + amplop(150, 46, 48, 32, 0)
A['C51-5'] = tulisan_kacau(150, 80) + potret(150, 200, 26, 'pria', 'kaget', 'a') + teks(210, 170, '?', 30, angka=True)

A['C52-1'] = lantai() + polisi(90, 170, {'ka': [(20, 0), (46, 0)]}) + pencuri(200, 150)
A['C52-2'] = lantai() + polisi(200, 170, {'ki': [(20, 0), (46, 0)]}) + pencuri(90, 150)
A['C52-3'] = lantai() + garis((70, 130), (70, 200), lebar=6) + rantai_putus(100, 176) + kotak(120, 196, 120, 4, 'a') + teks(180, 120, '?', 44, angka=True) + orang(250, tinggi=150, jenis='wanita', baju='a', wajah='kaget')
A['C52-4'] = lantai() + ''.join(garis((50 + i * 36, 140), (50 + i * 36, 200), lebar=4) for i in range(5)) + garis((40, 140), (200, 140), lebar=4) + rantai_putus(120, 168) + orang(250, tinggi=160, jenis='pria', baju='h', wajah='kaget', tangan=TA)
A['C52-5'] = lantai_kamar() + jendela(230, 30, 60, 46) + bulan_bintang(226, 52, .4) + jam_kecil(70, 56, 3, 0, 26) + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'kaget') + jalur('M82 131 q2 -18 16 -18 q12 0 13 14', 'h')

A['C53-1'] = dua_panel(topan().replace(lantai(), ''), rumah(225, 200, 110, 70) + orang(205, kaki=196, tinggi=55, jenis='pria', baju='a') + orang(240, kaki=196, tinggi=50, jenis='wanita', baju='h')) + lantai()
A['C53-2'] = topan() + orang(150, tinggi=140, jenis='pria', baju='a', wajah='takut', tangan={'ki': [(20, -10), (40, -24)], 'ka': [(20, -10), (40, -24)]}) + tanda_bahaya(250, 90, .8)
A['C53-3'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(22, -10), (40, -20)]}) + gelas(180, 196, 'susu', 1.2) + jalur('M154 142 q26 -10 52 0', 'p') + silang(180, 150, 36, 7)
A['C53-4'] = tebing() + tanda_bahaya(120, 40, 1.0) + orang(60, kaki=90, tinggi=70, jenis='pria', baju='h', wajah='takut')
A['C53-5'] = lantai() + sekolah(210, 200, 130, 90) + jam_kecil(210, 40, 7, 50, 18) + jalan_kaki(80, 'laki', 120, 'a') + tas_punggung(60, 108, .7) + centang(140, 40, 1.2)

A['C54-1'] = kotak(16, 16, 268, 188, 'h', 6) + bulat(150, 100, 60, 'n') + bulat(130, 86, 10, 't') + bulat(172, 118, 7, 't') + bintang(50, 40, 5).replace('class="h"', 'class="n"') + bintang(250, 170, 5).replace('class="h"', 'class="n"')
A['C54-2'] = kotak(16, 16, 268, 188, 'h', 6) + ''.join(bintang(x, y, r).replace('class="h"', 'class="n"') for x, y, r in ((40, 40, 7), (90, 70, 5), (140, 30, 8), (200, 60, 6), (250, 35, 7), (60, 130, 6), (120, 110, 8), (180, 150, 6), (240, 120, 7), (100, 170, 5), (220, 180, 6)))
A['C54-3'] = kotak(16, 16, 268, 188, 'h', 6) + bulat(150, 110, 70, 'n') + bulat(126, 90, 12, 't') + bulat(176, 130, 9, 't') + bulat(160, 84, 6, 't')
A['C54-4'] = lantai() + matahari(150, 60, 40, 'h') + orang(80, tinggi=140, jenis='pria', baju='p', wajah='lelah') + keringat(58, 70) + keringat(104, 76) + orang(230, tinggi=140, jenis='wanita', baju='a', wajah='lelah', tangan={'ka': [(14, -6), (10, -26)]})
A['C54-5'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(22, 0), (50, -10)]}) + bunga(150, 60, 1.4) + orang(225, tinggi=165, jenis='pria', baju='h', wajah='tawa')

A['C55-1'] = laut(90) + kantong_sampah(80, 150, .5) + botol(150, 130, .5) + kaleng(210, 140, .7) + ikan(240, 170, .5, 'a') + kertas(120, 180, 20, 14, 30)
A['C55-2'] = sungai = (bentuk((16, 120), (284, 150), (284, 204), (16, 204), k='a') + pipa_limbah(80, 70) + gedung(40, 70, 3, lebar=50) + kantong_sampah(150, 180, .45) + botol(220, 190, .4) + ikan(250, 170, .4, 'p'))
A['C55-3'] = dua_panel(orang(75, tinggi=140, jenis='pria', baju='a', tangan={'ki': [(14, 20), (30, 10)], 'ka': [(14, 20), (30, 10)]}) + buku(75, 110, 40, 30, 'h') + kalender_senin(75, 10, 5, 5, 120)[:0], pelari(225, 'pria', 'a', 140)) + lantai() + teks(150, 26, '週末', 20)
A['C55-4'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='takut') + gelembung(200, 50, 110, 50, teks(200, 60, '中文？', 22), (-1, 1)) + garis((96, 60), (124, 60), lebar=4)
A['C55-5'] = lantai() + tong_daur(70, 200, 'a') + tong_daur(140, 200, 'h') + tong_daur(210, 200, 'p') + orang(265, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(20, 0), (40, -4)]}) + botol(232, 108, .35)

A['C56-1'] = lantai() + sinterklas(150, 165)
A['C56-2'] = (kotak(16, 16, 268, 188, 'p') + lampion(50, 44, .8) + lampion(250, 44, .8) + meja_bundar(150, 130, 220) + piring(150, 128, 50, ikan(150, 122, .6))
              + orang(50, tinggi=120, jenis='nenek', rambut='uban', duduk=160, baju='a') + orang(250, tinggi=125, jenis='pria', duduk=160, baju='h') + orang(150, kaki=200, tinggi=70, jenis='laki', baju='a'))
A['C56-3'] = lantai() + sinterklas(120, 165, {'ka': [(10, 10), (30, -20)]}) + karung(200, 196, 1.2)
A['C56-4'] = lantai() + hiasan_imlek(150) + petasan(262, 60, 6)
A['C56-5'] = lantai() + sinterklas(90, 165, {'ka': [(20, 10), (46, 4)]}) + kado(160, 108, .6) + orang(210, tinggi=90, jenis='laki', baju='a', wajah='tawa') + orang(260, tinggi=85, jenis='gadis', baju='h', wajah='tawa')

A['C57-1'] = potret(150, 84, 44, 'wanita', 'gugup', 'a')
A['C57-2'] = lantai() + orang(110, tinggi=165, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(20, -4), (44, -10)]}) + orang(200, tinggi=150, jenis='wanita', baju='a', wajah='gugup') + keringat(222, 40)
A['C57-3'] = potret(150, 84, 44, 'pria', 'gugup', 'a') + keringat(96, 60) + jam_kecil(236, 150, 11, 55, 30) + panah(222, 100, 200, 118, 3)
A['C57-4'] = lantai() + jam_dinding(230, 60, 36, 8, 55) + jalan_kaki(110, 'wanita', 160, 'a', 'gugup') + keringat(136, 40)
A['C57-5'] = potret(150, 96, 50, 'laki', 'takut', 'a') + jalur('M250 20 l-14 30 l12 0 l-16 34', 'g', 5) + awan(60, 30, .35, 'h')

A['C58-1'] = potret(150, 84, 44, 'pria', 'tawa', 'a')
A['C58-2'] = lantai() + orang(150, kaki=180, tinggi=160, jenis='wanita', baju='a', wajah='tawa', tangan={'ki': [(20, -20), (30, -50)], 'ka': [(20, -20), (30, -50)]}, kaki_pose={'ki': (-20, -10), 'ka': (20, -10)}) + bintang(80, 40, 8) + bintang(230, 50, 7)
A['C58-3'] = lantai() + pintu(40, 200, 150, 60)[:0] + orang(90, tinggi=160, jenis='pria', baju='a', wajah='kaget', tangan={'ki': [(20, -20), (30, -40)], 'ka': [(20, -20), (30, -40)]}) + orang(210, tinggi=160, jenis='wanita', baju='h', wajah='tawa', tangan={'ki': [(20, 10), (40, 4)]}) + kado(162, 110, .5) + teks(150, 30, '!', 30, angka=True)
A['C58-4'] = lantai() + meja(200, 150, 150) + kertas(200, 138, 70, 20) + centang(200, 110, 1.0) + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ki': [(20, -30), (10, -60)], 'ka': [(20, -30), (10, -60)]})
A['C58-5'] = lantai() + gunung(200, 200, 200, 130) + matahari(250, 40, 14) + orang(70, tinggi=160, jenis='wanita', baju='a', wajah='kaget', tangan={'ki': [(20, -10), (10, -30)], 'ka': [(20, -10), (10, -30)]}) + bintang(120, 40, 7) + bintang(150, 70, 5)

A['C59-1'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, -4), (40, -10)]}) + titik_obrolan(120, 30, 56, 30, (-1, 1)) + orang(210, tinggi=160, jenis='wanita', baju='h', wajah='puas', tangan={'ka': [(16, -6), (26, -30)]}) + jempol(246, 60, 1.0)
A['C59-2'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, -4), (40, -10)]}) + gelembung(160, 40, 80, 50, lampu_ide(160, 42, .7), (-1, 1)) + orang(230, tinggi=160, jenis='wanita', baju='h', wajah='kaget')
A['C59-3'] = kotak(16, 16, 268, 188, 'p') + meja(150, 150, 220) + orang(150, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, -20), (40, -40)], 'ka': [(20, -20), (40, -40)]}) + orang(50, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(250, tinggi=135, jenis='pria', duduk=160, baju='a') + teks(60, 60, '?', 30, angka=True) + teks(240, 60, '?', 30, angka=True)
A['C59-4'] = lantai() + meja(150, 140, 240) + ''.join(potong_kue(60 + i * 60, 136, .5) for i in range(4)) + panah(180, 40, 180, 90, 5) + teks(250, 50, '1', 30, angka=True)

A['C60-1'] = lantai() + gedung(150, tingkat=5, lebar=130) + plus_minus(50, 60, '+', 'a') + plus_minus(250, 60, '-', 'a')
A['C60-2'] = lantai() + awan(150, 30, 1.0, 'a') + hujan(150, 50, 240, 50, 10) + tikar(120, 170, 160, 26) + keranjang(90, 180, .6) + orang(230, tinggi=150, jenis='wanita', baju='a', wajah='sedih')
A['C60-3'] = lantai() + orang(120, tinggi=150, jenis='laki', baju='a', wajah='sedih', tangan={'ka': [(16, 20), (30, 30)]}) + es_krim_jatuh(180, 200)
A['C60-4'] = lantai() + meja(170, 150, 200) + piring(200, 144, 50, ikan(200, 136, .6)) + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='sedih', tangan={'ka': [(22, -4), (44, -10)]}) + silang(200, 110, 18, 5)


# ---------------- perbaikan C49–C60 ----------------
A['C49-5'] = lantai() + botol(180, 196, 1.6) + silang(180, 130, 44, 8) + orang(70, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, -10), (40, -20)]})
A['C51-1'] = lantai() + loket(200) + teks(200, 40, '$', 30, angka=True) + orang(80, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + uang_kertas(160, 100, '100', 84, 36)
A['C51-5'] = lantai() + tulisan_kacau(200, 80, 150, 100) + orang(70, tinggi=165, jenis='pria', baju='a', wajah='kaget', tangan={'ka': [(16, -6), (22, -30)]}) + teks(120, 40, '?', 30, angka=True)
A['C53-3'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(22, -10), (40, -20)]}) + botol(190, 196, 1.6) + silang(190, 130, 44, 8)
A['C55-3'] = dua_panel(orang(75, tinggi=140, jenis='pria', baju='a', tangan={'ki': [(14, 26), (26, 40)], 'ka': [(14, 26), (26, 40)]}) + buku(75, 132, 40, 30, 'h'), pelari(225, 'pria', 'a', 140)) + lantai()
A['C55-4'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='gugup') + gelembung(200, 50, 110, 50, teks(200, 60, '中文？', 22), (-1, 1))
A['C59-3'] = kotak(16, 16, 268, 188, 'p') + meja(150, 150, 220) + orang(150, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 0), (40, -10)], 'ka': [(20, 0), (40, -10)]}) + orang(50, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(250, tinggi=135, jenis='pria', duduk=160, baju='a') + teks(60, 60, '?', 30, angka=True) + teks(240, 60, '?', 30, angka=True)
