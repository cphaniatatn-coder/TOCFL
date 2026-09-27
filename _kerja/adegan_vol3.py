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
