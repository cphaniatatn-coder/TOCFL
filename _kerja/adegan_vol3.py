"""Adegan ilustrasi 聽力 Part 1 — Volume 3 (C01–C67). ID = <modul>-<n> (listen_pic ke-n, urut isi → soal → bank)."""
from svg_adegan import *
from adegan_vol2 import dokter2
from adegan_vol2 import kelas_murid, potret, pelari, tunjuk_ke, burung, jam_kecil, rambut_terurai, garis_jatuh, pegang_perut, piala, kembang_api, meja_bundar, JOG, LARI

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
A['C01-4'] = dapur() + orang(95, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(22, 10), (50, 4)]})
A['C01-5'] = lantai() + meja(150, 150, 220) + piring(150, 144, 80) + ''.join(bulat(120 + i * 14, 140 - (i % 2) * 3, 2.2, 'h') for i in range(5)) + garpu(210, 136, 60, 10)

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
A['C15-3'] = lantai() + kotak(120, 120, 164, 80, 'a') + mesin_kopi(250, 120) + orang(170, kaki=200, tinggi=145, jenis='wanita', baju='h') + kotak(120, 120, 164, 80, 'a') + mesin_kopi(250, 120) + cangkir(140, 118, .35, True)
A['C15-2'] = lantai() + orang(100, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 16), (44, 20)]}, kacamata=True) + tas_kerja(70, 196, .7) + orang(200, tinggi=160, jenis='pria', baju='a', tangan={'ki': [(20, 16), (44, 20)]})
A['C15-4'] = lantai() + meja(90, 150, 120) + orang(200, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(16, -10), (30, -20)]}) + nampan(236, 64, 60)
A['C15-5'] = lantai() + papan_tulis(80, 30, 120, 70) + orang(170, tinggi=160, jenis='wanita', baju='a', rambut='uban', tangan={'ki': [(10, -10), (30, -30)]}) + murid_belakang(230, 200, 120) + murid_belakang(275, 200, 125, 'gadis')

A['C16-1'] = kotak(16, 16, 268, 188, 'p') + kotak(90, 26, 120, 60, 'p') + grafik([2, 4, 3, 6], 100, 80, 100, 48) + meja(150, 150, 220) + orang(50, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(250, tinggi=135, jenis='pria', duduk=160, baju='h') + orang(150, kaki=200, tinggi=80, jenis='pria', baju='a')
A['C16-3'] = kotak(16, 16, 268, 188, 'p') + jendela(230, 30, 60, 46) + bulan_bintang(226, 52, .4) + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'a') + lampu(150, 60, True, 30)
A['C16-2'] = kotak(16, 16, 268, 188, 'p') + jam_dinding(240, 60, 34, 3, 0) + meja(130, 150, 200) + orang(60, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(200, tinggi=135, jenis='pria', duduk=160, baju='h')
A['C16-4'] = kotak(16, 16, 268, 188, 'p') + jam_dinding(240, 60, 34, 9, 0) + meja(130, 150, 200) + orang(60, tinggi=130, jenis='pria', duduk=160, baju='h') + orang(200, tinggi=135, jenis='wanita', duduk=160, baju='a')
A['C16-5'] = dua_panel(orang_ponsel(75, 'pria', 150, baju='a') + gelembung(110, 30, 60, 34, silang(110, 30, 10, 4), (-1, 1)), sofa(225, 200, 110) + orang(225, tinggi=140, jenis='wanita', duduk=160, baju='a', wajah='puas')) + lantai()

A['C17-1'] = lantai() + gunung(170, 200, 260, 170, False) + orang(120, kaki=130, tinggi=80, jenis='pria', baju='h') + tas_punggung(106, 70, .5) + orang(170, kaki=95, tinggi=76, jenis='wanita', baju='a') + tas_punggung(157, 38, .5)
A['C17-3'] = lantai() + gunung(170, 200, 260, 170, False) + orang(140, kaki=120, tinggi=90, jenis='pria', baju='a') + tas_punggung(124, 52, .6) + garis((160, 70), (170, 120), lebar=3)
A['C17-2'] = lantai() + bulan_bintang(250, 36, .5) + pohon(40, s=.8) + jalan_kaki(130, 'wanita', 150, 'a') + jalan_kaki(190, 'pria', 160, 'h')
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
A['C20-3'] = kotak(16, 16, 268, 188, 'a') + kotak(16, 150, 268, 54, 'p') + garis((16, 150), (284, 150), lebar=5) + kereta(150, 146, 250) + orang(250, kaki=200, tinggi=60, jenis='pria', baju='h')
A['C20-2'] = kotak(16, 16, 268, 188, 'a') + papan_keluar(150, 60, '', 1)
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

A['C59-3'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, -4), (40, -10)]}) + titik_obrolan(120, 30, 56, 30, (-1, 1)) + orang(210, tinggi=160, jenis='wanita', baju='h', wajah='puas', tangan={'ka': [(16, -6), (26, -30)]}) + jempol(246, 60, 1.0)
A['C59-2'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, -4), (40, -10)]}) + gelembung(160, 40, 80, 50, lampu_ide(160, 42, .7), (-1, 1)) + orang(230, tinggi=160, jenis='wanita', baju='h', wajah='kaget')
A['C59-4'] = kotak(16, 16, 268, 188, 'p') + meja(150, 150, 220) + orang(150, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, -20), (40, -40)], 'ka': [(20, -20), (40, -40)]}) + orang(50, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(250, tinggi=135, jenis='pria', duduk=160, baju='a') + teks(60, 60, '?', 30, angka=True) + teks(240, 60, '?', 30, angka=True)
A['C59-5'] = lantai() + meja(150, 140, 240) + ''.join(potong_kue(60 + i * 60, 136, .5) for i in range(4)) + panah(180, 40, 180, 90, 5) + teks(250, 50, '1', 30, angka=True)

A['C60-2'] = lantai() + gedung(150, tingkat=5, lebar=130) + plus_minus(50, 60, '+', 'a') + plus_minus(250, 60, '-', 'a')
A['C60-3'] = lantai() + awan(150, 30, 1.0, 'a') + hujan(150, 50, 240, 50, 10) + tikar(120, 170, 160, 26) + keranjang(90, 180, .6) + orang(230, tinggi=150, jenis='wanita', baju='a', wajah='sedih')
A['C60-4'] = lantai() + orang(120, tinggi=150, jenis='laki', baju='a', wajah='sedih', tangan={'ka': [(16, 20), (30, 30)]}) + es_krim_jatuh(180, 200)
A['C60-5'] = lantai() + meja(170, 150, 200) + piring(200, 144, 50, ikan(200, 136, .6)) + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='sedih', tangan={'ka': [(22, -4), (44, -10)]}) + silang(200, 110, 18, 5)


# ---------------- perbaikan C49–C60 ----------------
A['C49-5'] = lantai() + botol(180, 196, 1.6) + silang(180, 130, 44, 8) + orang(70, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, -10), (40, -20)]})
A['C51-1'] = lantai() + loket(200) + teks(200, 40, '$', 30, angka=True) + orang(80, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + uang_kertas(160, 100, '100', 84, 36)
A['C51-5'] = lantai() + tulisan_kacau(200, 80, 150, 100) + orang(70, tinggi=165, jenis='pria', baju='a', wajah='kaget', tangan={'ka': [(16, -6), (22, -30)]}) + teks(120, 40, '?', 30, angka=True)
A['C53-3'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(22, -10), (40, -20)]}) + botol(190, 196, 1.6) + silang(190, 130, 44, 8)
A['C55-3'] = dua_panel(orang(75, tinggi=140, jenis='pria', baju='a', tangan={'ki': [(14, 26), (26, 40)], 'ka': [(14, 26), (26, 40)]}) + buku(75, 132, 40, 30, 'h'), pelari(225, 'pria', 'a', 140)) + lantai()
A['C55-4'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='gugup') + gelembung(200, 50, 110, 50, teks(200, 60, '中文？', 22), (-1, 1))
A['C59-4'] = kotak(16, 16, 268, 188, 'p') + meja(150, 150, 220) + orang(150, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 0), (40, -10)], 'ka': [(20, 0), (40, -10)]}) + orang(50, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(250, tinggi=135, jenis='pria', duduk=160, baju='a') + teks(60, 60, '?', 30, angka=True) + teks(240, 60, '?', 30, angka=True)


# ================= komponen C61–C67 =================
def jam_tangan(x, y, s=1.0):
    return kotak(x - 14 * s, y - 60 * s, 28 * s, 120 * s, 'a', 6) + jam_kecil(x, y, 10, 10, 30 * s)


def cincin(x, y, s=1.0):
    return (bulat(x, y + 20 * s, 34 * s, 'a') + bulat(x, y + 20 * s, 24 * s, 'p')
            + bentuk((x - 16 * s, y - 16 * s), (x + 16 * s, y - 16 * s), (x + 22 * s, y - 8 * s), (x, y + 12 * s), (x - 22 * s, y - 8 * s), k='p')
            + garis((x - 22 * s, y - 8 * s), (x + 22 * s, y - 8 * s), k='t') + jalur(f'M{f(x - 28 * s)} {f(y - 30 * s)} l6 6 M{f(x + 28 * s)} {f(y - 30 * s)} l-6 6 M{f(x)} {f(y - 36 * s)} l0 8', 'g', 3))


def jaket_di(x, tinggi=160, jenis='pria', kaki=LANTAI):
    s_ = sendi(x, kaki, tinggi, jenis)
    r, b, p = s_['r'], s_['bahu'], s_['pinggang']
    return (garis((x, b + 2), (x, p + 8), k='w', lebar=3) + jalur(f'M{f(x - r * .6)} {f(b)} L{f(x)} {f(b + r * .9)} L{f(x + r * .6)} {f(b)}', 'w', 3)
            + kotak(x - s_['lb'] / 2 + 5, p - r * .9, r * .7, r * .5, 'p', 2) + kotak(x + s_['lb'] / 2 - 5 - r * .7, p - r * .9, r * .7, r * .5, 'p', 2))


def cermin(x, bawah, w=70, h=150):
    return elips(x, bawah - h / 2 - 10, w / 2, h / 2, 'p') + jalur(f'M{f(x - w / 4)} {f(bawah - h + 20)} l14 -14 M{f(x - w / 4)} {f(bawah - h + 44)} l24 -24', 't', 3) + garis((x - 20, bawah), (x + 20, bawah), lebar=5)


def kalender_3hari(x, y, w=240):
    lw = w / 7
    o = kotak(x - w / 2, y, w, 90, 'p', 4) + kotak(x - w / 2, y, w, 22, 'h', 4)
    for i in range(7):
        cx = x - w / 2 + lw * (i + .5)
        if i:
            o += garis((x - w / 2 + lw * i, y + 22), (x - w / 2 + lw * i, y + 90), k='t')
        if i < 3:
            o += kotak(x - w / 2 + lw * i + 3, y + 26, lw - 6, 60, 'a', 3)
        o += teks(cx, y + 64, str(i + 1), 18, angka=True)
    return o + jalur(f'M{f(x - w / 2 + 2)} {f(y + 56)} q{f(lw * 1.5)} -40 {f(lw * 3 - 4)} 0', 'g', 4)


# ================= C61–C67 =================
A['C61-1'] = lantai() + rak_buku(110, w=130, h=160) + orang(230, tinggi=165, jenis='wanita', baju='a', wajah='gugup', tangan={'ki': [(20, -10), (40, -24)]}) + buku(178, 86, 26, 36, 'h') + silang(178, 50, 16, 5)
A['C61-2'] = lantai() + kursi(150, s=1.2) + orang(150, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='lelah', tangan={'ka': [(16, 10), (30, 0)]}) + buku(194, 128, 30, 38, 'h') + gelembung_pikiran(80, 30, 70, 40, teks(80, 42, '…', 26, angka=True))
A['C61-3'] = lantai() + kardus(150, 200, 90, 60) + bola(150, 110, 44, 'sepak') + silang(240, 70, 26, 7)
A['C61-4'] = lantai() + kotak(30, 90, 120, 110, 't') + kotak(34, 94, 112, 106, 'p') + pintu(90, 200, 90, 44) + sofa(225, 200, 150) + panah(170, 70, 130, 70, 4) + silang(150, 40, 18, 5)
A['C61-5'] = lantai() + papan_tulis(80, 20, 110, 60) + orang(70, tinggi=165, jenis='wanita', baju='h', wajah='puas', tangan={'ka': [(20, -6), (40, -14)]}) + panah(110, 110, 150, 110, 4) + orang(220, tinggi=140, jenis='laki', baju='a', wajah='tawa') + titik_obrolan(250, 40, 56, 30, (-1, 1))

A['C62-1'] = lantai() + kotak(170, 60, 100, 140, 'p', 4) + jam_tangan(220, 110, .8) + label_harga(220, 40, '$99999', 110, 36) + orang(80, tinggi=165, jenis='pria', baju='a', wajah='sedih') + dompet(120, 140, .6)
A['C62-2'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='lelah', tangan={'ki': [(10, 40), (14, 70)], 'ka': [(10, 40), (14, 70)]}) + tas_belanja(110, 190, 1.0) + tas_belanja(190, 190, 1.0) + tas_belanja(80, 196, .8) + tas_belanja(222, 196, .8) + keringat(126, 40) + keringat(176, 46)
A['C62-3'] = cincin(120, 100, 1.6) + label_harga(230, 60, '$$$', 100, 40) + dompet(230, 150, 1.0) + silang(230, 150, 30, 6)
A['C62-4'] = lantai() + orang(130, tinggi=160, jenis='pria', baju='a', wajah='sakit', tangan={'ki': [(20, 50), (34, 70)], 'ka': [(20, 50), (34, 70)]}) + kardus(130, 200, 120, 80, 'h') + keringat(106, 50) + keringat(156, 46)
A['C62-5'] = lantai() + mobil(190, w=170) + label_harga(190, 50, '$$$$$', 130, 44) + orang(55, tinggi=160, jenis='pria', baju='a', wajah='kaget')

A['C63-1'] = lantai() + awan(150, 36, 1.2, 'a') + hujan(150, 60, 250, 60, 12) + orang(110, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(10, -20), (18, -40)]}) + payung(128, 86, 40) + orang(220, tinggi=150, jenis='pria', baju='h', wajah='kaget', tangan={'ki': [(20, -30), (10, -60)], 'ka': [(20, -30), (10, -60)]})
A['C63-2'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='kaget', tangan={'ka': [(12, -20), (0, -46)]}) + lampu_ide(150, 20, 1.0)
A['C63-3'] = lantai() + orang(60, tinggi=150, jenis='wanita', baju='a', wajah='tawa') + orang(150, tinggi=160, jenis='pria', baju='h', wajah='tawa') + orang(240, tinggi=150, jenis='gadis', baju='a', wajah='tawa') + teks(105, 40, '哈', 22) + teks(200, 34, '哈', 22)
A['C63-4'] = kotak(16, 16, 268, 188, 'p') + kotak(60, 30, 180, 130, 'a') + awan(150, 54, .9, 'h') + hujan(150, 80, 160, 70, 10) + garis((150, 30), (150, 160), lebar=6) + garis((60, 95), (240, 95), lebar=6) + kotak(50, 160, 200, 12, 'h')
A['C63-5'] = lantai() + orang(90, tinggi=165, jenis='wanita', baju='a', wajah='gugup', tangan={'ka': [(14, -10), (4, -36)]}) + gelembung_pikiran(210, 40, 110, 70, teks(210, 60, '?', 40, angka=True))

A['C64-1'] = lantai() + orang(150, tinggi=170, jenis='pria', baju='h', wajah='puas') + jaket_di(150, 170, 'pria')
A['C64-2'] = lantai() + pintu(230, 200, 150, 70) + kotak(195, 50, 20, 150, 'a') + orang(90, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(22, -10), (46, -18)]}) + titik_obrolan(70, 30, 56, 30, (1, 1))
A['C64-3'] = lantai() + pintu(220, 200, 150, 70) + kotak(185, 50, 20, 150, 'a') + jalan_kaki(140, 'pria', 160, 'h') + jaket_di(140, 160, 'pria') + panah(170, 110, 200, 110, 4)
A['C64-4'] = lantai() + jendela_buka(210, 40, 100, 80) + orang(90, tinggi=165, jenis='wanita', baju='h', tangan={'ka': [(22, -20), (50, -36)]}) + titik_obrolan(70, 30, 56, 30, (1, 1))
A['C64-5'] = lantai() + cermin(220, 200) + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='tawa', rok=True) + bintang(70, 70, 7) + bintang(150, 60, 6) + bintang(90, 130, 5)

A['C65-1'] = piring(150, 110, 110) + bulat(110, 104, 34, 'p') + daging(170, 86, .8) + ikan(180, 128, .7) + telur_ceplok(120, 138, .5)
A['C65-2'] = lantai() + meja(150, 140, 240) + piring(80, 134, 30, ikan(80, 128, .4)) + piring(150, 134, 30, daging(150, 128, .4)) + piring(220, 134, 30, roti(220, 126, .4)) + orang(60, kaki=140, tinggi=110, jenis='pria', baju='a', wajah='tawa', tangan={'ki': [(14, -20), (20, -40)], 'ka': [(14, -20), (20, -40)]}) + orang(240, kaki=140, tinggi=100, jenis='wanita', baju='h', wajah='tawa', tangan={'ki': [(14, -20), (20, -40)], 'ka': [(14, -20), (20, -40)]})
A['C65-3'] = lantai() + ''.join(kursi_depan(x, 160) + orang(x, tinggi=120, jenis=j, duduk=160, baju=b) for x, j, b in ((40, 'pria', 'a'), (100, 'wanita', 'h'), (160, 'pria', 'h'), (220, 'wanita', 'a'), (270, 'pria', 'a')))
A['C65-4'] = lantai() + gelas(150, 196, 'air', 2.2)
A['C65-5'] = papan_tulis(150, 14, 150, 50) + kelas_murid(['laki', 'gadis', 'laki', 'gadis', 'laki', 'gadis'])

A['C66-1'] = kartu_arc(150, 110, 1.3)
A['C66-2'] = lantai() + meja(150, 150, 200) + lembar_soal(110, 120, 10, 50, 30)[:0] + kertas(110, 138, 50, 20) + orang(150, kaki=150, tinggi=100, jenis='laki', baju='a', tangan={'ka': [(16, -4), (30, -20)]}) + kartu_arc(200, 62, .4)
A['C66-3'] = lantai() + rak_buku(250, w=80, h=160) + meja(120, 150, 150) + komputer(130, 146, 70) + orang(50, tinggi=140, jenis='wanita', duduk=160, baju='a', tangan={'ka': [(20, 0), (40, 0)]})
A['C66-4'] = lantai() + rak_buku(60, w=90, h=170) + rak_buku(250, w=80, h=170) + meja(155, 150, 130) + buku(155, 126, 40, 22, 'a') + orang(155, kaki=150, tinggi=100, jenis='pria', baju='a', tangan={'ki': [(10, 20), (20, 16)], 'ka': [(10, 20), (20, 16)]})
A['C66-5'] = lantai_kamar() + jendela(230, 30, 60, 46) + matahari(230, 52, 12) + jam_dinding(70, 56, 26, 12, 0) + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + jalur('M82 131 q2 -18 16 -18 q12 0 13 14', 'h') + teks(130, 110, 'Z z', 18, angka=True)

A['C67-1'] = lantai() + pintu(250, 200, 150, 60) + orang(90, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 0), (44, -4)]}) + kotak(70, 40, 40, 10, 'h', 3) + bento(160, 100, .45) + orang(205, tinggi=160, jenis='wanita', baju='a', wajah='tawa')
A['C67-2'] = lantai() + skuter(120) + kotak(110, 90, 40, 36, 'a', 4) + jam_sektor(240, 60, 36, 55)
A['C67-3'] = dua_panel(rumah(75, 200, 100, 70) + matahari(120, 34, 14) + orang(75, kaki=196, tinggi=50, jenis='pria', baju='a'),
                       rumah(225, 200, 100, 70) + bulan_bintang(270, 40, .4) + orang(225, kaki=196, tinggi=50, jenis='pria', baju='a')) + lantai()
A['C67-4'] = kalender_3hari(150, 30) + kertas(110, 170, 60, 40) + pulpen(160, 168, 60, -30)
A['C67-5'] = lantai() + jendela(240, 30, 60, 46) + bulan_bintang(236, 52, .4) + meja(150, 150, 200) + lampu(210, 70, True, 40)[:0] + buku(150, 130, 44, 24, 'a') + orang(90, kaki=150, tinggi=100, jenis='wanita', baju='a', tangan={'ka': [(20, 20), (40, 20)]}) + jam_kecil(60, 40, 11, 0, 20)


# ---------------- perbaikan C61–C67 ----------------
A['C61-2'] = lantai() + sofa(150, 200, 170) + orang(150, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='lelah', tangan={'ka': [(16, 10), (30, 0)]}) + buku(194, 128, 30, 38, 'a') + gelembung_pikiran(80, 30, 70, 40, teks(80, 42, '…', 26, angka=True))
A['C61-5'] = lantai() + orang(70, tinggi=165, jenis='wanita', baju='h', wajah='puas', tangan={'ka': [(20, -6), (40, -14)]}) + panah(110, 110, 150, 110, 4) + orang(220, tinggi=140, jenis='laki', baju='a', wajah='tawa') + titik_obrolan(250, 40, 56, 30, (-1, 1))
A['C62-1'] = lantai() + kotak(170, 70, 100, 130, 'p', 4) + jam_tangan(220, 120, .8) + label_harga(220, 40, '$$$$', 100, 36) + orang(80, tinggi=165, jenis='pria', baju='a', wajah='sedih') + dompet(120, 140, .6)
A['C65-2'] = lantai() + meja(150, 140, 150) + piring(105, 134, 22, ikan(105, 128, .3)) + piring(150, 134, 22, daging(150, 128, .3)) + piring(195, 134, 22, roti(195, 126, .3)) + orang(40, tinggi=160, jenis='pria', baju='a', wajah='tawa', tangan={'ki': [(14, -20), (20, -40)], 'ka': [(14, -20), (20, -40)]}) + orang(260, tinggi=150, jenis='wanita', baju='h', wajah='tawa', tangan={'ki': [(14, -20), (20, -40)], 'ka': [(14, -20), (20, -40)]})
A['C65-4'] = lantai() + bentuk((104, 56), (196, 56), (186, 196), (114, 196), k='p') + bentuk((106, 66), (194, 66), (186, 196), (114, 196), k='a') + jalur('M112 66 q10 -6 20 0 t20 0 t20 0 t20 0', 'g', 3)
A['C65-5'] = lantai() + papan_tulis(150, 12, 140, 44) + ''.join(murid_belakang(55 + i * 95, 160, 80, 'gadis' if i % 2 else 'laki') for i in range(3)) + ''.join(murid_belakang(55 + i * 95, 200, 100, 'laki' if i % 2 else 'gadis') + meja_kelas(55 + i * 95) for i in range(3))
A['C66-4'] = lantai() + rak_buku(60, w=90, h=170) + rak_buku(250, w=80, h=170) + orang(155, tinggi=130, jenis='pria', duduk=170, baju='a') + meja(155, 150, 130) + buku(155, 146, 40, 16, 'a')
A['C67-5'] = lantai() + jendela(240, 30, 60, 46) + bulan_bintang(236, 52, .4) + orang(120, tinggi=130, jenis='wanita', duduk=170, baju='a') + meja(150, 150, 200) + buku(130, 146, 44, 16, 'a') + jam_kecil(60, 40, 11, 0, 20)

# --- C01 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
from adegan_vol2 import bld, jam_penuh, mi, nasi_goreng, kue, kotak_teh


def nonton(x0=0):
    return lantai() + sofa(110, w=170) + orang(80, tinggi=130, jenis='wanita', baju='a', duduk=150) + orang(140, tinggi=135, jenis='pria', baju='h', duduk=150) + tv(250, 150, 80) + meja(250, 150, 80)


A['C01-3'] = nonton() + piring(200, 196, 30, '')
A['C01-L4a'] = lantai() + meja(150, 170, 220) + piring(150, 162, 70, '') + jalur('M110 158 q10 -6 20 0 M150 160 q8 -4 16 0', 'g', 2) + orang(260, tinggi=150, jenis='pria', baju='h', wajah='puas')
A['C01-L4b'] = lantai() + meja(150, 170, 220) + mangkuk_mi(150, 140, .5, sumpit=True, uap=False) + orang(260, tinggi=150, jenis='pria', baju='h', wajah='puas')
A['C01-L4c'] = lantai() + meja(150, 170, 220) + nasi_goreng(150, 140, 1.2) + orang(260, tinggi=150, jenis='pria', baju='h', wajah='lapar')
A['C01-L5a'] = jam_dinding(150, 105, 80, 11, 0)
A['C01-L5b'] = jam_dinding(150, 105, 80, 1, 30)
A['C01-L5c'] = jam_dinding(150, 105, 80, 11, 30)
A['C01-L6a'] = nonton()
A['C01-L6b'] = lantai() + meja(160, 150, 200) + buku(200, 150, 50, 20, 'a') + kertas(160, 128, 60, 20) + teks(160, 132, '中文', 12) + orang(90, tinggi=150, jenis='pria', duduk=156, baju='h', tangan={'ka': [(24, 16), (54, 22)]})
A['C01-L6c'] = lantai() + meja(160, 150, 200) + buku(200, 150, 50, 20, 'a') + kertas(160, 128, 60, 20) + teks(160, 132, 'ABC', 12, angka=True) + orang(90, tinggi=150, jenis='pria', duduk=156, baju='h', tangan={'ka': [(24, 16), (54, 22)]})
A['C01-L8a'] = lantai() + meja(160, 150, 200) + mangkuk_mi(170, 120, .4, sumpit=True) + orang(90, tinggi=150, jenis='pria', duduk=156, baju='h', tangan={'ka': [(24, 0), (54, -10)]})
A['C01-L8b'] = lantai() + meja(160, 150, 200) + piring(220, 146, 30, '') + kertas(160, 128, 60, 20) + orang(90, tinggi=150, jenis='pria', duduk=156, baju='h', tangan={'ka': [(24, 16), (54, 22)]}) + pulpen(175, 124, 40, -40)
A['C01-L8c'] = lantai() + sofa(100) + orang(100, tinggi=140, jenis='pria', baju='h', duduk=150) + tv(240, 150, 90) + meja(240, 150, 90)
A['C01-L9'] = lantai() + meja(150, 170, 240) + piring(90, 162, 40, '') + piring(150, 162, 40, '') + piring(210, 162, 40, '') + garpu(250, 150, 50, -20)
A['C01-L10'] = lantai() + kotak(40, 20, 220, 120, 'h', 4) + teks(150, 95, '完', 50, warna='#fff') + jam_dinding(260, 170, 24, 11, 0)
A['C01-T3a'] = lantai() + meja(150, 170, 200) + cangkir_kopi(150, 166, 1.2)
A['C01-T3b'] = lantai() + meja(150, 170, 200) + cangkir_kopi(110, 166, 1.0) + kotak(170, 140, 70, 26, 'a', 12)
A['C01-T3c'] = lantai() + meja(150, 170, 200) + piring(150, 162, 60, telur_ceplok(150, 156, 1.0))
A['C01-T4a'] = nonton() + teks(250, 20, '2nd', 18, angka=True)
A['C01-T4b'] = nonton().replace('', '') + teks(250, 20, 'NEW', 18, angka=True)
A['C01-T4c'] = lantai() + rumah(200, 200, 140, 100) + jalan_kaki(70, 'wanita', 150, 'a') + panah(110, 130, 140, 130, 4)
A['C01-T6a'] = dapur() + orang(95, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(22, 10), (50, 4)]})
A['C01-T6b'] = lantai() + meja(160, 150, 200) + mangkuk_mi(170, 120, .4, sumpit=True) + orang(90, tinggi=140, jenis='wanita', duduk=156, baju='a', tangan={'ka': [(24, 0), (54, -10)]})
A['C01-T6c'] = dapur() + orang(95, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(22, 20), (50, 20)]}) + piring(160, 120, 30, '') + jalur('M150 106 a6 6 0 1 1 1 0 M166 100 a5 5 0 1 1 1 0', 'g', 2)
A['C01-T7'] = lantai() + meja(150, 150, 160) + ''.join(kursi(x, s=.8) for x in (50, 110)) + ''.join(kursi(x, arah=-1, s=.8) for x in (190, 250))
A['C01-T8'] = lantai() + meja(150, 170, 200) + wajan(150, 150, 1.4, isi=False)

# --- C02 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
from adegan_vol2 import bld


def lemari(x, lantai_y=LANTAI, w=90, h=150, buka=False):
    o = kotak(x - w / 2, lantai_y - h, w, h, 'p', 4) + garis((x, lantai_y - h), (x, lantai_y)) + bulat(x - 8, lantai_y - h / 2, 3, 'h') + bulat(x + 8, lantai_y - h / 2, 3, 'h')
    return o


def gantungan(x, y, k='a', s=1.0):
    return jalur(f'M{f(x)} {f(y)} q0 -10 8 -10', 'g', 2.5) + bentuk((x - 26 * s, y + 14 * s), (x, y), (x + 26 * s, y + 14 * s), k='p') + kaos(x, y + 64 * s, .7 * s, k)


def meja_belajar(x, lantai_y=LANTAI):
    return kotak(x - 60, lantai_y - 80, 120, 10, 'h') + kotak(x + 20, lantai_y - 70, 36, 70, 'p') + garis((x - 56, lantai_y - 70), (x - 56, lantai_y), lebar=5) + garis((x + 22, lantai_y - 52), (x + 54, lantai_y - 52), k='t')


def tas_kecil(x, y):
    return kotak(x - 20, y - 24, 40, 24, 'a', 5) + jalur(f'M{x - 10} {y - 24} q10 -14 20 0', 'g', 3)


A['C02-L4a'] = lantai() + sofa(150) + kaos(110, 150, .6, 'a') + kaos(170, 146, .6, 'p')
A['C02-L4b'] = lantai() + garis((40, 30), (260, 30), lebar=4) + gantungan(90, 32) + gantungan(150, 32, 'p') + gantungan(210, 32)
A['C02-L4c'] = lantai() + lemari(150)
A['C02-L5a'] = lantai() + sofa(150)
A['C02-L5b'] = lantai() + rak_buku(150, 200, 120, 160)
A['C02-L5c'] = lantai() + meja_belajar(150)
A['C02-L6a'] = lantai() + mesin_cuci(200) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (50, 10)]}) if 'mesin_cuci' in globals() else lantai()
A['C02-L6b'] = lantai() + toko(200) + orang(70, tinggi=160, jenis='wanita', baju='a') + gantungan(130, 60, 'p', .7)
A['C02-L6c'] = lantai() + toko(200) + orang(70, tinggi=160, jenis='wanita', baju='a') + sofa(200, w=110).replace('', '')
A['C02-L8a'] = A['C02-L4a']
A['C02-L8b'] = A['C02-L4b']
A['C02-L8c'] = lantai() + lemari(150) + kaos(150, 140, .5, 'a')
A['C02-L9'] = lantai() + rak_buku(150, 200, 140, 170)
A['C02-L10'] = lantai() + jam_dinding(60, 50, 32, 8, 50) + pelari(150, 'laki', 'h', 120) + bld(250, '學校', 80, 70)
A['C02-T3a'] = lantai() + sofa(150) + tas_kecil(150, 150)
A['C02-T3b'] = lantai() + lemari(150) + tas_kecil(150, 80)
A['C02-T3c'] = lantai() + meja_belajar(150) + tas_kecil(130, 120)
A['C02-T4a'] = lantai() + sofa(150)
A['C02-T4b'] = lantai() + lemari(150)
A['C02-T4c'] = lantai() + kursi(150, s=1.4)
A['C02-T6a'] = lantai() + meja_belajar(150) + buku(120, 120, 30, 12, 'a')
A['C02-T6b'] = lantai() + meja_belajar(150) + buku(110, 120, 30, 10, 'a') + buku(130, 112, 30, 10, 'h') + kertas(160, 112, 30, 16, 20) + kertas(140, 104, 26, 14, -15) + noda(100, 112, 6)
A['C02-T6c'] = lantai() + sofa(150)
A['C02-T7'] = lantai() + sofa(140) + label_harga(250, 40, '999', 90, 40)
A['C02-T8'] = lantai() + sofa(150) + larangan(150, 90, 40)

# --- C03 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def wastafel(x, lantai_y=LANTAI):
    return kotak(x - 60, lantai_y - 90, 120, 90, 'p') + kotak(x - 50, lantai_y - 90, 100, 20, 'a', 4) + garis((x + 30, lantai_y - 90), (x + 30, lantai_y - 110), (x + 14, lantai_y - 110), lebar=4)


def basah(x, y):
    return ''.join(jalur(f'M{x + dx} {y} q-4 8 0 12 q4 -4 0 -12', 'a') for dx in (-20, 0, 20))


A['C03-L4a'] = lantai() + pintu(250, 200, 140, 60) + orang(150, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(16, 30), (26, 40)]}) + kantong_sampah(185, 196, .6) + panah(200, 80, 230, 80, 4)
A['C03-L4b'] = lantai() + wastafel(200) + piring(200, 114, 30, '') + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (50, 10)]})
A['C03-L4c'] = lantai() + mesin_cuci(210, 200, 110, 120) + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (50, 10)]}) + kaos(140, 120, .4, 'a')
A['C03-L5a'] = lantai() + awan(150, 20, 1.0, 'a') + garis((30, 60), (270, 60), lebar=3) + kaos(100, 120, .8, 'a') + kaos(200, 120, .8, 'p') + basah(100, 136) + basah(200, 136)
A['C03-L5b'] = lantai() + mesin_cuci(150, 200, 130, 130)
A['C03-L5c'] = lantai() + jendela(60, 40, 60, 50) + meja(170, 150, 160) + kotak(120, 126, 100, 12, 'a', 3) + kotak(124, 114, 92, 12, 'p', 3) + kotak(128, 102, 84, 12, 'a', 3)
A['C03-L6a'] = lantai() + awan(150, 20, 1.0, 'a') + hujan(150, 30, 200, 30) + garis((30, 70), (270, 70), lebar=3) + kaos(110, 130, .7, 'a') + kaos(190, 130, .7, 'p')
A['C03-L6b'] = lantai() + mesin_cuci(150, 200, 130, 130)
A['C03-L6c'] = lantai_kamar() + ranjang(110, 200, 140) + garis((190, 60), (270, 60), lebar=3) + kaos(230, 120, .6, 'a')
A['C03-L8a'] = lantai() + kotak(160, 140, 90, 60, 'a', 6) + ''.join(garis((166 + i * 14, 142), (166 + i * 14, 198), k='t') for i in range(6)) + orang(80, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 20), (50, 30)]}) + kaos(190, 136, .4, 'p')
A['C03-L8b'] = lantai() + pintu(250, 200, 140, 60) + jalan_kaki(150, 'pria', 160, 'h') + kantong_sampah(185, 190, .6) + panah(200, 70, 230, 70, 4)
A['C03-L8c'] = lantai() + kantong_sampah(190, 200, 1.1) + orang(80, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 20), (50, 30)]}) + kertas(170, 60, 30, 20, 10)
A['C03-L9'] = A['C03-5']
A['C03-L10'] = lantai() + wastafel(200) + piring(190, 114, 30, '') + piring(210, 110, 30, '') + noda(200, 104, 5) + orang(80, tinggi=160, jenis='wanita', rambut='uban', baju='a', tangan={'ka': [(20, 0), (48, 10)]})
A['C03-T3a'] = A['C03-L8b']
A['C03-T3b'] = lantai() + wastafel(200) + piring(200, 114, 30, '') + orang(90, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 10), (50, 10)]})
A['C03-T3c'] = lantai() + mesin_cuci(210, 200, 110, 120) + orang(90, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 10), (50, 10)]})
A['C03-T4a'] = lantai() + kotak(110, 120, 80, 80, 'a', 6) + jalur('M106 120 L194 120', 'g', 6)
A['C03-T4b'] = lantai() + pintu(150, 200, 150, 80)
A['C03-T4c'] = lantai() + mesin_cuci(110, 200, 110, 120) + kantong_sampah(220, 200, .9)
A['C03-T6a'] = lantai() + tas_buka(150, 150, 0, 1.4) + jalur('M120 130 l14 -20 l10 16 l12 -18 l8 22', 'p') + buku(140, 196, 30, 10, 'a') + buku(190, 196, 26, 10, 'h') + garis_jatuh(160, 160)
A['C03-T6b'] = lantai() + tas_buka(150, 196, 0, 1.6) + bintang(230, 60, 8)
A['C03-T6c'] = lantai() + tas_buka(150, 196, 10, 1.6)
A['C03-T7'] = lantai() + kantong_sampah(150, 200, 1.6)
A['C03-T8'] = lantai() + mesin_cuci(190, 200, 110, 120) + ''.join(kaos(70, 196 - i * 18, .5, 'a' if i % 2 else 'p') for i in range(4))

# --- C04 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def rumah_n(x, n, lantai_y=LANTAI, w=130):
    th = 54 * n
    o = bentuk((x - w / 2 - 10, lantai_y - th), (x, lantai_y - th - 36), (x + w / 2 + 10, lantai_y - th), k='h') + kotak(x - w / 2, lantai_y - th, w, th, 'p')
    for i in range(n):
        y = lantai_y - 54 * (i + 1)
        if i: o += garis((x - w / 2, lantai_y - 54 * i), (x + w / 2, lantai_y - 54 * i), lebar=3)
        o += jendela(x - 32, y + 12, 30, 24) + (jendela(x + 32, y + 12, 30, 24) if i else pintu(x + 32, lantai_y, 44, 28))
    return o


def sepatu_pasang(x, y, s=.8):
    return sepatu(x - 20 * s, y, s, 'a') + sepatu(x + 30 * s, y, s, 'a')


A['C04-L4a'] = lantai() + rumah_n(150, 2)
A['C04-L4b'] = lantai() + rumah_n(150, 3)
A['C04-L4c'] = lantai() + rumah_n(150, 1)
A['C04-L5a'] = lantai() + pintu(150, 200, 150, 70) + sepatu_pasang(150, 198)
A['C04-L5b'] = lantai() + sofa(150) + sepatu_pasang(140, 150, .6)
A['C04-L5c'] = lantai_kamar() + ranjang(150, 200, 190) + sepatu_pasang(150, 196, .6)
A['C04-L6a'] = lantai() + rumah_2lantai(150) + sofa(118, 124, 50).replace('', '') if False else lantai() + rumah_2lantai(150) + panah(80, 70, 110, 70, 4) + kotak(96, 52, 40, 20, 'a', 5)
A['C04-L6b'] = lantai_kamar() + ranjang(110, 200, 140) + sofa(240, w=90)
A['C04-L6c'] = lantai() + sofa(150, w=170) + tv(260, 150, 50) + jendela(60, 40, 50, 40)
A['C04-L8a'] = lantai() + jendela(60, 40, 50, 40) + meja(170, 150, 140) + sofa(60, w=80).replace('', '')
A['C04-L8b'] = A['C04-5']
A['C04-L8c'] = lantai_kamar() + ranjang(100, 200, 120) + meja(230, 150, 90)
A['C04-L9'] = lantai() + kursi(150, s=1.4) + kucing(150, 198, .7)
A['C04-L10'] = lantai() + gedung(150, tingkat=10, lebar=110, tt=16)
A['C04-T3a'] = A['C04-L5a']
A['C04-T3b'] = A['C04-L5c']
A['C04-T3c'] = A['C04-L5b']
A['C04-T4a'] = lantai_kamar() + ranjang(150, 200, 190)
A['C04-T4b'] = lantai() + pagar(16, 284) + pohon(220) + bunga(80, 180) + bunga(120, 186)
A['C04-T4c'] = lantai() + sofa(80, w=120) + kompor(230, 130, 90)
A['C04-T6a'] = lantai() + sofa(140, w=170) + tv(260, 150, 50)
A['C04-T6b'] = lantai_kamar() + ranjang(100, 200, 120) + sofa(240, w=90)
A['C04-T6c'] = lantai() + pagar(16, 284) + pohon(260, s=.7) + sofa(140)
A['C04-T7'] = lantai() + pagar(16, 120) + pohon(60, s=.7) + rumah(210, 200, 130, 90) + bunga(110, 190)
A['C04-T8'] = lantai_kamar() + ranjang(90, 200, 110) + pintu(240, 200, 150, 60) + sepatu_pasang(240, 198, .6) + panah(120, 175, 200, 175, 4)

# --- C05 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kotak_surat(x, lantai_y=LANTAI, isi=''):
    return garis((x, lantai_y), (x, lantai_y - 90), lebar=6) + kotak(x - 40, lantai_y - 150, 80, 60, 'p', 8) + kotak(x - 26, lantai_y - 134, 52, 8, 'h', 2) + teks(x, lantai_y - 104, '信箱', 14) + isi


def beri(kepada, benda):
    o = lantai() + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (46, -4)]}) + benda + panah(140, 40, 180, 40, 4)
    return o + kepada


A['C05-L4a'] = lantai() + kotak_surat(150) + kunci(150, 70, .5, 0)
A['C05-L4b'] = celana(150, 30, .95, 'a') + kotak(160, 50, 40, 44, 'p', 3) + kunci(180, 72, .6, -30)
A['C05-L4c'] = lantai() + meja(150, 140, 180) + kunci(150, 128, .7, 0)
A['C05-L5a'] = beri(orang(220, tinggi=160, jenis='wanita', rambut='uban', baju='p'), uang_kertas(150, 80, '$', 50, 26))
A['C05-L5b'] = beri(orang(220, tinggi=100, jenis='laki', baju='h'), uang_kertas(150, 80, '$', 50, 26))
A['C05-L5c'] = beri(orang(220, tinggi=155, jenis='wanita', baju='h'), uang_kertas(150, 80, '$', 50, 26))
A['C05-L6a'] = uang_kertas(150, 105, '$300', 200, 100)
A['C05-L6b'] = uang_kertas(150, 105, '$200', 200, 100)
A['C05-L6c'] = uang_kertas(150, 105, '$100', 200, 100)
A['C05-L8a'] = lantai() + orang(80, tinggi=110, jenis='gadis', baju='a', tangan={'ka': [(20, 0), (40, -4)]}) + kunci(150, 118, .6, 0) + orang(220, tinggi=165, jenis='pria', baju='h') + panah(120, 60, 180, 60, 4)
A['C05-L8b'] = lantai() + orang(80, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 0), (46, -4)]}) + amplop(150, 82, 40, 26) + orang(220, tinggi=110, jenis='gadis', baju='a') + panah(120, 40, 180, 40, 4)
A['C05-L8c'] = lantai() + orang(80, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 0), (46, -4)]}) + kunci(150, 82, .6, 0) + orang(220, tinggi=110, jenis='gadis', baju='a') + panah(120, 40, 180, 40, 4)
A['C05-L9'] = lantai() + pintu(150, 200, 170, 90) + kunci(170, 120, .7, 0) + gembok(130, 120, .5)
A['C05-L10'] = A['C05-3']
A['C05-T3a'] = A['C05-L4b']
A['C05-T3b'] = lantai() + tas_buka(150, 196, 0, 1.6) + kunci(150, 100, .6, 0)
A['C05-T3c'] = lantai() + pintu(150, 200, 170, 90) + kunci(170, 120, .7, 0)
A['C05-T4a'] = lantai() + kotak_surat(200) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (46, -10)]}) + amplop(200, 60, 40, 26)
A['C05-T4b'] = lantai() + anjing(170, 198, 1.1) + orang(70, tinggi=160, jenis='wanita', baju='a')
A['C05-T4c'] = lantai() + kereta(170, 196, 220) + orang(40, tinggi=150, jenis='wanita', baju='a') + teks(170, 40, '臺中', 20)
A['C05-T6a'] = beri(orang(220, tinggi=160, jenis='wanita', rambut='uban', baju='p'), uang_kertas(150, 80, '$', 50, 26)).replace('', '')
A['C05-T6b'] = lantai() + orang(80, tinggi=160, jenis='wanita', rambut='uban', baju='p', tangan={'ka': [(20, 0), (46, -4)]}) + uang_kertas(150, 80, '$', 50, 26) + orang(220, tinggi=155, jenis='wanita', baju='a') + panah(140, 40, 180, 40, 4)
A['C05-T6c'] = lantai() + orang(80, tinggi=160, jenis='wanita', rambut='uban', baju='p', tangan={'ka': [(20, 0), (46, -4)]}) + kunci(150, 80, .6, 0) + orang(220, tinggi=155, jenis='wanita', baju='a') + panah(140, 40, 180, 40, 4)
A['C05-T7'] = celana(150, 30, .95, 'a') + kotak(150, 50, 60, 54, 'p', 3) + kunci(165, 70, .5, -30) + uang_kertas(170, 90, '$', 36, 18)
A['C05-T8'] = A['C05-4']

# --- C06 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def pasta_gigi(x, y, s=1.0):
    return bentuk((x - 50 * s, y - 14 * s), (x + 40 * s, y - 14 * s), (x + 50 * s, y), (x + 40 * s, y + 14 * s), (x - 50 * s, y + 14 * s), k='p') + kotak(x + 48 * s, y - 7 * s, 14 * s, 14 * s, 'h', 2)


def gulung_tisu(x, y, s=1.0):
    return kotak(x - 26 * s, y - 30 * s, 52 * s, 60 * s, 'p', 6) + elips(x, y - 30 * s, 26 * s, 8 * s, 'p') + bulat(x, y - 30 * s, 6 * s, 'a')


A['C06-L4a'] = pasta_gigi(140, 80, 1.2) + sikat_gigi(150, 150, 1.1, 0)
A['C06-L4b'] = sabun(100, 130, 1.4) + handuk(200, 80, 80, 90, 'a')
A['C06-L4c'] = lantai() + botol_sampo(150, 196, 1.3)
A['C06-L5a'] = lantai() + meja(150, 150, 200) + botol_sampo(150, 146, .8)
A['C06-L5b'] = lantai() + meja(150, 150, 200) + botol_sampo(110, 146, .8) + botol_sampo(190, 146, .8)
A['C06-L5c'] = lantai() + meja(150, 150, 200) + sabun(110, 140, .8) + sabun(190, 140, .8)
A['C06-L6a'] = lantai() + botol_sampo(100, 196, 1.0) + pasta_gigi(210, 160, .8)
A['C06-L6b'] = lantai() + gulung_tisu(100, 160, 1.2) + pasta_gigi(210, 160, .8)
A['C06-L6c'] = lantai() + botol_sampo(100, 196, 1.0) + gulung_tisu(210, 160, 1.2)
A['C06-L8a'] = lantai() + meja(150, 150, 200) + sikat_gigi(150, 140, .8, 0)
A['C06-L8b'] = lantai() + meja(150, 150, 200) + sikat_gigi(120, 140, .7, 0) + pasta_gigi(200, 136, .5)
A['C06-L8c'] = lantai() + meja(150, 150, 200) + pasta_gigi(150, 136, .7)
A['C06-L9'] = lantai() + kotak(170, 120, 100, 80, 'p') + kotak(180, 120, 80, 18, 'a', 4) + sabun(210, 110, .5) + orang(90, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 20), (60, 20)]}) + jalur('M190 104 a5 5 0 1 1 1 0 M204 96 a4 4 0 1 1 1 0', 'g', 2)
A['C06-L10'] = kotak(40, 20, 220, 180, 'p') + kotak(100, 40, 100, 50, 'a', 6) + bentuk((90, 110), (210, 110), (190, 200), (110, 200), k='a') + elips(150, 108, 62, 14, 'p') + garis((220, 60), (270, 60), lebar=5) + garis((222, 50), (222, 70), lebar=4) + bulat(246, 60, 6, 'a') + teks(246, 110, '?', 30, angka=True)
A['C06-T3a'] = lantai() + kotak(60, 120, 180, 80, 'p', 30) + handuk(150, 110, 80, 30, 'a')
A['C06-T3b'] = lantai() + kursi(150, s=1.3) + handuk(140, 120, 60, 30, 'a')
A['C06-T3c'] = lantai() + pintu(150, 200, 170, 90) + handuk(130, 40, 40, 70, 'a') + handuk(170, 40, 40, 70, 'h')
A['C06-T4a'] = lantai() + kotak(110, 90, 80, 110, 'p', 12) + kotak(140, 64, 20, 26, 'h', 2) + garis((150, 64), (150, 50), (196, 50), lebar=6) + garis((196, 50), (196, 62), lebar=4) + kotak(122, 120, 56, 40, 'a', 4)
A['C06-T4b'] = sabun(150, 110, 2.0)
A['C06-T4c'] = lantai() + botol_sampo(150, 196, 1.3)
A['C06-T6a'] = lantai() + pintu(220, 200, 150, 70) + orang(120, tinggi=110, jenis='laki', baju='h', wajah='nangis')
A['C06-T6b'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=110, jenis='laki', baju='h', duduk=150, wajah='tawa')
A['C06-T6c'] = lantai() + pintu(220, 200, 150, 70) + orang(120, tinggi=110, jenis='laki', baju='h', wajah='tawa', tangan=LAMBAI)
A['C06-T7'] = lantai() + gulung_tisu(80, 160, 1.0) + gulung_tisu(150, 160, 1.0) + gulung_tisu(220, 160, 1.0)
A['C06-T8'] = lantai() + papan_tulis(210, 30, 120, 60) + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='tawa') + gelembung(170, 40, 60, 30, teks(170, 46, '♪', 16, angka=True), (-1, 1))

# --- C07 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def malam(x=230):
    return jendela(x, 30, 60, 46) + bulan_bintang(x - 5, 52, .45)


def kamar_tidur_nyenyak(jam_h=0):
    return lantai_kamar() + malam() + jam_dinding(70, 56, 28, jam_h, 0) + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + teks(130, 110, 'Z z', 18, angka=True)


A['C07-L4a'] = lantai() + malam() + meja(150, 150, 200) + buku_tumpuk(120, 150, 3, 50, 12) + orang(200, tinggi=150, jenis='pria', baju='p', wajah='lelah', duduk=150)
A['C07-L4b'] = kamar_tidur_nyenyak()
A['C07-L4c'] = lantai() + malam() + meja(150, 150, 200) + kotak(110, 100, 70, 50, 'h', 4) + kotak(116, 106, 58, 38, 'a', 2) + orang(220, tinggi=150, jenis='pria', baju='p', wajah='tawa', duduk=150)
A['C07-L5a'] = lantai() + pintu(200, 200, 160, 80) + jalan_kaki(140, 'wanita', 155, 'a') + panah(230, 80, 270, 80, 4)
A['C07-L5b'] = A['C07-3']
A['C07-L5c'] = lantai_kamar() + matahari(220, 52, 9) + jendela(220, 30, 60, 46) + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur')
A['C07-L6a'] = kotak(50, 60, 200, 90, 'h', 12) + kotak(62, 72, 176, 66, 'a', 6) + teks(150, 124, '8:30', 48, angka=True)
A['C07-L6b'] = kotak(50, 60, 200, 90, 'h', 12) + kotak(62, 72, 176, 66, 'a', 6) + teks(150, 124, '8:00', 48, angka=True)
A['C07-L6c'] = kotak(50, 60, 200, 90, 'h', 12) + kotak(62, 72, 176, 66, 'a', 6) + teks(150, 124, '8:40', 48, angka=True)
A['C07-L8a'] = kamar_tidur_nyenyak()
A['C07-L8b'] = lantai_kamar() + matahari(220, 52, 9) + jendela(220, 30, 60, 46) + weker(70, 60, 26, 7, 0) + orang(150, tinggi=160, jenis='pria', baju='a', wajah='tawa', tangan=LAMBAI)
A['C07-L8c'] = A['C07-L4a']
A['C07-L9'] = jam_dinding(150, 105, 80, 7, 0)
A['C07-L10'] = lantai_kamar() + malam() + jam_dinding(70, 56, 28, 0, 0) + ranjang(150, 200, 180) + orang(210, tinggi=150, jenis='pria', baju='p', wajah='lelah') + panah(190, 110, 160, 130, 4)
A['C07-T3a'] = jam_dinding(150, 105, 80, 10, 0)
A['C07-T3b'] = jam_dinding(150, 105, 80, 11, 0)
A['C07-T3c'] = jam_dinding(150, 105, 80, 2, 0)
A['C07-T4a'] = lantai() + meja(150, 150, 200) + kotak(110, 90, 80, 60, 'a', 2) + ''.join(garis((120, 104 + i * 12), (180, 104 + i * 12), k='t') for i in range(2)) + teks(150, 140, '?', 22, angka=True) + orang(230, tinggi=150, jenis='wanita', baju='a', wajah='sedih', duduk=150)
A['C07-T4b'] = kotak(80, 30, 140, 160, 'a', 4) + teks(150, 110, '100', 48, angka=True) + orang(250, tinggi=150, jenis='wanita', baju='a', wajah='tawa')
A['C07-T4c'] = lantai() + gedung(150, tingkat=3, lebar=150, tt=30) + kotak(105, 150, 90, 50, 'h') + silang(150, 175, 18, 5)
A['C07-T6a'] = kamar_tidur_nyenyak(0)
A['C07-T6b'] = lantai() + malam() + jam_dinding(70, 56, 28, 0, 0) + meja(150, 150, 160) + kotak(120, 100, 60, 50, 'h', 4) + kotak(126, 106, 48, 38, 'a', 2) + orang(220, tinggi=110, jenis='laki', baju='h', duduk=150)
A['C07-T6c'] = lantai() + matahari(240, 40, 12) + jam_dinding(70, 56, 28, 12, 0) + meja(150, 150, 160) + kotak(120, 100, 60, 50, 'h', 4) + kotak(126, 106, 48, 38, 'a', 2) + orang(220, tinggi=110, jenis='laki', baju='h', duduk=150)
A['C07-T7'] = lantai_kamar() + ranjang(110, 200, 160) + bulat(56, 136, 13) + muka(56, 136, 13, 'tidur') + gelembung(210, 60, 120, 80, kotak(170, 30, 80, 60, 'a', 2) + ''.join(garis((180, 44 + i * 12), (240, 44 + i * 12), k='t') for i in range(3)), (-1, 1))
A['C07-T8'] = lantai_kamar() + malam() + jam_dinding(80, 70, 50, 1, 0)

# --- C08 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---


def gonggong(x, y):
    return teks(x, y, '!!', 22, angka=True) + jalur(f'M{x - 18} {y + 8} q6 -8 0 -16 M{x - 26} {y + 12} q10 -14 0 -28', 'g', 3)


def kamar_lantai_atas(isi_atas, isi_bawah):
    return lantai() + garis((16, 100), (284, 100), lebar=4) + isi_atas + isi_bawah


A['C08-L4a'] = kamar_lantai_atas(orang(150, kaki=98, tinggi=80, jenis='wanita', baju='a', wajah='tawa') + not_musik(190, 30, .7) + not_musik(210, 60, .7), ranjang(150, 200, 160, ) + orang(260, tinggi=90, jenis='pria', baju='a', wajah='marah'))
A['C08-L4b'] = lantai() + anjing(150, 198, 1.1) + gonggong(220, 110)
A['C08-L4c'] = A['C08-1']
A['C08-L5a'] = lantai() + ''.join(salju(x, y) for x, y in ((40, 40), (100, 70), (170, 40), (250, 60), (60, 120), (220, 120))) + orang(150, tinggi=160, jenis='wanita', baju='h', wajah='sedih')
A['C08-L5b'] = lantai() + matahari(240, 50, 18) + orang(130, tinggi=160, jenis='wanita', baju='a', wajah='lelah') + keringat(105, 70) + keringat(160, 76)
A['C08-L5c'] = lantai() + awan(150, 20, 1.0, 'a') + hujan(150, 30, 220, 40) + orang(150, tinggi=160, jenis='wanita', baju='a')
A['C08-L6a'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='marah') + gelembung(220, 60, 110, 70, ac(220, 46, False, False, 80) + silang(220, 60, 26, 6), (-1, 1))
A['C08-L6b'] = lantai() + ac(90, 40) + ''.join(salju(x, y) for x, y in ((40, 130), (150, 110), (260, 60), (270, 140))) + orang(210, tinggi=150, jenis='pria', baju='h', wajah='sedih', tangan={'ki': [(10, 30), (34, 34)], 'ka': [(10, 30), (34, 34)]})
A['C08-L6c'] = lantai() + ac(90, 40, False, True) + orang(210, tinggi=150, jenis='pria', baju='a', wajah='lelah') + keringat(184, 90) + keringat(236, 96)
A['C08-L8a'] = A['C08-L5a']
A['C08-L8b'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='sedih', tangan={'ki': [(10, 40), (30, 50)], 'ka': [(10, 40), (30, 50)]}) + gelembung(230, 50, 70, 50, piring(230, 56, 40, ''), (-1, 1))
A['C08-L8c'] = lantai() + matahari(240, 50, 18) + pintu(60, 200, 150, 70) + orang(150, tinggi=160, jenis='pria', baju='a', wajah='lelah') + keringat(124, 70) + keringat(176, 76)
A['C08-L9'] = lantai() + anjing(130, 198, 1.2) + gonggong(210, 100) + gonggong(250, 140)
A['C08-L10'] = A['C08-5']
A['C08-T3a'] = lantai() + matahari(240, 40, 16) + rumah(130, 200, 120, 90)
A['C08-T3b'] = lantai() + bulan_bintang(240, 40, .7) + anjing(130, 198, 1.0) + gonggong(210, 110)
A['C08-T3c'] = lantai() + matahari(60, 120, 16) + garis((16, 140), (284, 140), lebar=2) + rumah(200, 200, 120, 90)
A['C08-T4a'] = rumah(150, 200, 140, 100) + lantai() + uang_kertas(150, 50, '$$$', 140, 50)
A['C08-T4b'] = A['C08-1']
A['C08-T4c'] = A['C08-L4a']
A['C08-T6a'] = kamar_lantai_atas(matahari(40, 40, 12) + orang(150, kaki=98, tinggi=80, jenis='wanita', baju='a', wajah='tawa') + not_musik(190, 30, .7), '')
A['C08-T6b'] = kamar_lantai_atas(bulan_bintang(40, 40, .5) + orang(150, kaki=98, tinggi=80, jenis='wanita', baju='a', wajah='tidur') + teks(190, 40, 'Z z', 16, angka=True), '')
A['C08-T6c'] = kamar_lantai_atas(bulan_bintang(40, 40, .5) + orang(150, kaki=98, tinggi=80, jenis='wanita', baju='a', wajah='tawa') + not_musik(190, 30, .7) + not_musik(215, 60, .7), '')
A['C08-T7'] = A['C08-3']
A['C08-T8'] = lantai() + matahari(240, 50, 20) + ac(90, 40) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='lelah') + keringat(124, 80)

# --- C09 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kota(mobil_n=1):
    o = lantai() + gedung(50, tingkat=7, lebar=70) + gedung(120, tingkat=6, lebar=60, tt=26) + gedung(190, tingkat=8, lebar=70, tt=22) + gedung(260, tingkat=5, lebar=50)
    return o + ''.join(mobil(60 + i * 70, 200, 60) for i in range(mobil_n))


def desa():
    return sawah(150) + rumah(150, 150, 110, 70) + pohon(40, 150, .6) + gunung(250, 150, 120, 70, False)


def harga(x, y, t):
    return kotak(x - 40, y - 18, 80, 36, 'a', 6) + teks(x, y + 8, t, 20, angka=True)


A['C09-L4a'] = desa()
A['C09-L4b'] = lantai() + gunung(150, 200, 280, 140, False) + rumah(150, 110, 80, 50)
A['C09-L4c'] = kota() + orang(150, tinggi=100, jenis='pria', baju='a')
A['C09-L5a'] = dua_panel(rumah(75, 200, 90, 60) + pohon(130, s=.5) + harga(75, 50, '$'), gedung(225, tingkat=6, lebar=80) + harga(225, 30, '$$$$')) + lantai()
A['C09-L5b'] = dua_panel(rumah(75, 200, 90, 60) + pohon(130, s=.5) + harga(75, 50, '$$$$'), gedung(225, tingkat=6, lebar=80) + harga(225, 30, '$')) + lantai()
A['C09-L5c'] = dua_panel(rumah(75, 200, 90, 60) + pohon(130, s=.5) + harga(75, 50, '$$'), gedung(225, tingkat=6, lebar=80) + harga(225, 30, '$$')) + lantai()
A['C09-L6a'] = kota(0) + bus(150, 200, 150) + orang(270, tinggi=120, jenis='wanita', baju='a', wajah='tawa')
A['C09-L6b'] = desa() + angin(30, 40, .5)
A['C09-L6c'] = lantai() + toko(110, 200, 140, 110) + teks(110, 80, '超市', 20) + jalan_kaki(230, 'wanita', 150, 'a') + teks(230, 30, '5 min', 18, angka=True)
A['C09-L8a'] = lantai() + kotak(60, 110, 180, 90, 'p') + kotak(80, 40, 30, 70, 'h') + kotak(170, 60, 30, 50, 'h') + awan(95, 22, .4, 'a') + awan(190, 40, .4, 'a') + bentuk((60, 110), (100, 90), (100, 110), (140, 90), (140, 110), (180, 90), (180, 110), (240, 90), (240, 110), k='h')
A['C09-L8b'] = desa() + bunga(80, 196) + matahari(250, 30, 12)
A['C09-L8c'] = kota(0) + ''.join(mobil(x, 200, 46) for x in (40, 100, 160, 220, 280)) + teks(150, 30, '!!', 24, angka=True)
A['C09-L9'] = kota(1)
A['C09-L10'] = lantai() + gedung(60, tingkat=6, lebar=70) + toko(170, 200, 100, 90) + teks(170, 100, '超市', 18) + orang(260, tinggi=140, jenis='wanita', baju='a', wajah='tawa')
A['C09-T3a'] = kota()
A['C09-T3b'] = desa()
A['C09-T3c'] = lantai() + gedung(150, tingkat=4, lebar=160, tt=32) + teks(150, 30, '宿舍', 22)
A['C09-T4a'] = lantai() + gunung(150, 200, 280, 140, False) + matahari(250, 40, 14)
A['C09-T4b'] = lantai() + rumah(100, 200, 110, 80) + pohon(220) + matahari(250, 40, 14) + teks(100, 40, '?', 30, angka=True)
A['C09-T4c'] = lantai() + gedung(150, tingkat=10, lebar=60, tt=14) + gedung(70, tingkat=5, lebar=60) + gedung(230, tingkat=6, lebar=60) + matahari(260, 30, 16) + teks(150, 30, '臺北', 22)
A['C09-T6a'] = A['C09-L5a']
A['C09-T6b'] = A['C09-L5b']
A['C09-T6c'] = A['C09-L5c']
A['C09-T7'] = desa()
A['C09-T8'] = lantai() + gunung(150, 140, 280, 100, False) + rumah(90, 200, 90, 60) + orang(200, tinggi=150, jenis='wanita', baju='a', wajah='puas')

# --- C10 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
from adegan_vol2 import kue as kue_c10


def uang_besar(t):
    return uang_kertas(150, 105, t, 230, 100)


def adik(x=110, tinggi=110, wajah='senyum', gemuk=False, tangan=None):
    o = orang(x, tinggi=tinggi, jenis='gadis', baju='a', wajah=wajah, **({'tangan': tangan} if tangan else {}))
    return o


A['C10-L4a'] = uang_besar('$100')
A['C10-L4b'] = uang_besar('$1000')
A['C10-L4c'] = dompet(150, 70, 1.3) + uang_kertas(150, 60, '$$$', 120, 50) + uang_kertas(160, 80, '$$$', 120, 50)
A['C10-L5a'] = lantai() + meja(190, 150, 140) + kue_c10(170, 146, .5) + kue_c10(220, 146, .5) + adik(90, wajah='tawa', tangan={'ka': [(20, 10), (50, 4)]})
A['C10-L5b'] = lantai() + meja(200, 150, 120) + kue_c10(200, 146, .6) + adik(90, wajah='senyum', tangan={'ka': [(20, -10), (40, -30)]}) + silang(200, 100, 18, 5)
A['C10-L5c'] = lantai() + meja(200, 150, 120) + gelas(200, 146, 'teh', .8) + orang(110, tinggi=110, jenis='gadis', baju='a', wajah='senyum', tangan={'ka': [(20, 10), (50, 4)]})
A['C10-L6a'] = uang_besar('$12000')
A['C10-L6b'] = uang_besar('$15000')
A['C10-L6c'] = uang_besar('$3000')
A['C10-L8a'] = A['C10-L5a']
A['C10-L8b'] = lantai() + pelari(150, 'gadis') if False else lantai() + orang(150, tinggi=120, jenis='gadis', baju='h', wajah='tawa', tangan=LAMBAI) + bola(220, 186, 14)
A['C10-L8c'] = A['C10-L5b']
A['C10-L9'] = kotak(60, 50, 180, 120, 'a', 12) + kotak(60, 50, 180, 30, 'p', 12) + teks(150, 136, '$0', 40, angka=True) + garis((120, 180), (110, 200), lebar=3) + garis((180, 180), (190, 200), lebar=3)
A['C10-L10'] = lantai() + orang(50, tinggi=100, jenis='wanita', baju='a') + panah(70, 120, 100, 120, 3) + orang(120, tinggi=100, jenis='pria', baju='h') + orang(145, tinggi=100, jenis='wanita', baju='a') + panah(165, 120, 190, 120, 3) + ''.join(orang(205 + i * 22, tinggi=96 + (i % 2) * 8, jenis='pria' if i % 2 else 'wanita', baju='a' if i % 2 else 'h') for i in range(4))
A['C10-T3a'] = uang_besar('$8000')
A['C10-T3b'] = uang_besar('$10000')
A['C10-T3c'] = uang_besar('$18000')
A['C10-T4a'] = lantai() + kotak(30, 60, 240, 20, 'h') + ''.join(bulat(50 + i * 50, 92, 8, 'a') for i in range(5)) + ''.join(kotak(40 + i * 80, 110, 60, 90, 'p') for i in range(3)) + bulan_bintang(250, 30, .4) + teks(150, 54, '夜市', 18)
A['C10-T4b'] = lantai() + dapur(150) if False else lantai() + kompor(180, 130, 110) + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='tawa', tangan={'ka': [(20, 10), (50, 10)]})
A['C10-T4c'] = lantai() + meja(150, 150, 200) + piring(110, 144, 40, '') + piring(190, 144, 40, '') + kursi(60) + kursi(240) + teks(150, 40, '餐廳', 22)
A['C10-T6a'] = lantai() + matahari(240, 40, 18) + orang(110, tinggi=150, jenis='wanita', baju='a', wajah='lelah') + orang(190, tinggi=150, jenis='pria', baju='p') + keringat(84, 70)
A['C10-T6b'] = lantai() + ''.join(salju(x, y) for x, y in ((40, 40), (150, 30), (260, 50), (60, 120), (250, 130))) + orang(110, tinggi=150, jenis='wanita', baju='h') + orang(190, tinggi=150, jenis='pria', baju='h') + kotak(90, 70, 40, 14, 'p', 4) + kotak(170, 66, 40, 14, 'p', 4)
A['C10-T6c'] = lantai() + awan(150, 20, 1.0, 'a') + hujan(150, 30, 220, 40) + payung(110, 60) + orang(110, tinggi=150, jenis='wanita', baju='a') + orang(200, tinggi=150, jenis='pria', baju='p')
A['C10-T7'] = A['C10-3']
A['C10-T8'] = lantai() + ''.join(orang(60 + i * 90, tinggi=90 + i * 30, jenis='laki', baju='h') for i in range(3)) + panah(40, 30, 260, 30, 4)

# --- C11 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
from adegan_vol2 import jaket_item, topi_item


def jas_hujan(x, y, s=1.0):
    o = bentuk((x - 30 * s, y), (x + 30 * s, y), (x + 50 * s, y + 130 * s), (x - 50 * s, y + 130 * s), k='a')
    o += jalur(f'M{x - 26 * s} {y} q26 {-44 * s} {52 * s} 0', 'a') + garis((x, y + 8 * s), (x, y + 126 * s), k='t')
    return o + ''.join(bulat(x + 8 * s, y + (30 + i * 30) * s, 4 * s, 'h') for i in range(3))


def sepatu_bot(x, bawah, s=1.0):
    return bentuk((x - 20 * s, bawah - 90 * s), (x + 10 * s, bawah - 90 * s), (x + 10 * s, bawah - 20 * s), (x + 50 * s, bawah - 20 * s), (x + 50 * s, bawah), (x - 20 * s, bawah), k='h')


def hujan_orang(isi):
    return lantai() + awan(150, 16, 1.0, 'a') + hujan(150, 26, 260, 30) + isi


A['C11-L4a'] = payung(150, 110, 80)
A['C11-L4b'] = jas_hujan(150, 40, 1.1)
A['C11-L4c'] = topi_item(150, 110, 1.6)
A['C11-L5a'] = hujan_orang(payung(150, 70, 50) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='senyum'))
A['C11-L5b'] = hujan_orang(orang(150, tinggi=150, jenis='wanita', baju='a', wajah='sedih') + noda(130, 120, 6) + noda(170, 140, 6) + keringat(124, 70) + keringat(176, 74))
A['C11-L5c'] = hujan_orang(jas_hujan(150, 64, .9) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='senyum'))
A['C11-L6a'] = A['C11-L4a']
A['C11-L6b'] = A['C11-L4b']
A['C11-L6c'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', tangan={'ki': [(-20, 30), (-40, 40)], 'ka': [(20, 30), (40, 40)]}) + silang(240, 80, 22, 6)
A['C11-L8a'] = hujan_orang(payung(150, 70, 50) + orang(150, tinggi=150, jenis='gadis', baju='a'))
A['C11-L8b'] = hujan_orang(jas_hujan(150, 64, .9) + orang(150, tinggi=150, jenis='gadis', baju='a') + tas_buka(220, 196, 0, .6))
A['C11-L8c'] = lantai() + matahari(240, 40, 20) + orang(150, tinggi=150, jenis='gadis', baju='a', wajah='tawa')
A['C11-L9'] = A['C11-1']
A['C11-L10'] = jas_hujan(150, 40, 1.1)
A['C11-T3a'] = A['C11-L4b']
A['C11-T3b'] = A['C11-L4a']
A['C11-T3c'] = lantai() + jalur('M70 60 h40 v90 q0 10 10 12 l26 6 q10 4 8 22 h-84 z', 'h') + kotak(70 - 4, 52, 48, 16, 'p', 4) + garis((72, 188), (144, 188), k='p', lebar=6) + jalur('M170 60 h40 v90 q0 10 10 12 l26 6 q10 4 8 22 h-84 z', 'h') + kotak(170 - 4, 52, 48, 16, 'p', 4) + garis((172, 188), (244, 188), k='p', lebar=6)
A['C11-T4a'] = jaket_item(150, 40, 1.2)
A['C11-T4b'] = botol(150, 190, 1.6)
A['C11-T4c'] = A['C11-L4b']
A['C11-T6a'] = lantai() + kaos(130, 150, .6, 'a') + kaos(170, 146, .6, 'p') + keranjang(150, 200, 1.6)
A['C11-T6b'] = lantai() + lemari(150) if False else lantai() + meja(150, 150, 200) + kotak(100, 126, 100, 12, 'a', 3) + kotak(104, 114, 92, 12, 'p', 3) + matahari(250, 30, 14)
A['C11-T6c'] = lantai() + garis((30, 60), (270, 60), lebar=3) + kaos(110, 120, .7, 'a') + kaos(190, 120, .7, 'p') + ''.join(jalur(f'M{x} 160 q-4 8 0 12 q4 -4 0 -12', 'a') for x in (100, 120, 180, 200)) + pintu(280, 200, 140, 30)
A['C11-T7'] = A['C11-3']
A['C11-T8'] = lantai() + pintu(250, 200, 140, 60) + payung(180, 80, 40) + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -10)]}) + awan(80, 20, .7, 'a')

# --- C12 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kota_label(nama):
    return lantai() + gedung(70, tingkat=6, lebar=70) + gedung(150, tingkat=8, lebar=60, tt=22) + gedung(230, tingkat=5, lebar=70) + kotak(80, 14, 140, 40, 'a', 6) + teks(150, 42, nama, 24)


def alamat(no, lt):
    return lantai() + gedung(150, tingkat=6, lebar=120, tt=26) + kotak(40, 20, 90, 50, 'a', 6) + teks(85, 54, no, 28, angka=True) + kotak(200, 20, 80, 50, 'a', 6) + teks(240, 54, lt, 28, angka=True)


A['C12-L4a'] = lantai() + gedung(220, tingkat=3, lebar=120, tt=30) + orang(90, tinggi=140, jenis='laki', baju='h', tangan={'ka': [(18, 20), (30, 30)]}) + tas_buka(120, 150, 0, .5)
A['C12-L4b'] = foto_bayi()
A['C12-L4c'] = lantai() + gedung(220, tingkat=4, lebar=120, tt=28) + orang(90, tinggi=165, jenis='pria', baju='a') + buku_tumpuk(130, 120, 2, 40, 10)
A['C12-L5a'] = lantai() + pesawat(150, 70, 1.0) + orang(70, tinggi=110, jenis='gadis', baju='a')
A['C12-L5b'] = lantai() + rumah(240, 200, 80, 60) + jalan_kaki(90, 'wanita', 155, 'h') + jalan_kaki(140, 'gadis', 105, 'a') + kotak(170, 160, 40, 40, 'p', 4) + panah(30, 40, 200, 40, 4)
A['C12-L5c'] = lantai() + meja(160, 150, 160) + kotak(120, 100, 70, 50, 'h', 4) + kotak(126, 106, 58, 38, 'a', 2) + orang(250, tinggi=150, jenis='wanita', baju='h', duduk=150)
A['C12-L6a'] = kota_label('高雄')
A['C12-L6b'] = kota_label('臺北')
A['C12-L6c'] = kota_label('臺中')
A['C12-L8a'] = lantai() + orang(150, tinggi=150, jenis='pria', rambut='uban', baju='p', wajah='senyum')
A['C12-L8b'] = kotak(70, 20, 160, 180, 'a', 4) + kotak(84, 34, 132, 130, 'p') + orang(150, kaki=160, tinggi=90, jenis='laki', baju='h') + teks(150, 188, '5', 18, angka=True)
A['C12-L8c'] = foto_bayi()
A['C12-L9'] = lantai() + orang(150, tinggi=150, jenis='pria', rambut='uban', baju='p', wajah='senyum') + garis((190, 120), (196, 200), lebar=4)
A['C12-L10'] = foto_bayi()
A['C12-T3a'] = kota_label('臺北')
A['C12-T3b'] = kota_label('高雄')
A['C12-T3c'] = kota_label('臺中')
A['C12-T4a'] = alamat('30', '5F')
A['C12-T4b'] = alamat('20', '5F')
A['C12-T4c'] = alamat('30', '3F')
A['C12-T6a'] = lantai() + gedung(230, tingkat=4, lebar=100, tt=28) + orang(110, tinggi=165, jenis='pria', baju='a') + buku_tumpuk(150, 120, 2, 40, 10)
A['C12-T6b'] = lantai() + meja(170, 150, 160) + kotak(130, 100, 70, 50, 'h', 4) + kotak(136, 106, 58, 38, 'a', 2) + orang(260, tinggi=150, jenis='pria', baju='h', duduk=150)
A['C12-T6c'] = lantai() + gedung(220, tingkat=2, lebar=120, tt=30) + orang(100, tinggi=100, jenis='laki', baju='h') + tas_buka(130, 130, 0, .5) + teks(100, 30, '8', 24, angka=True)
A['C12-T7'] = foto_bayi()
A['C12-T8'] = A['C12-5']

# --- C13 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kakek(x, **kw):
    return orang(x, tinggi=150, jenis='nenek', rambut='pendek', rok=False, baju='p', kacamata=True, **kw) + garis((x + 24, 124), (x + 30, 200), lebar=4)


def kakek_cucu(n):
    o = lantai() + kakek(55)
    for i in range(n):
        o += orang(115 + i * (180 / max(n, 1)), tinggi=88 + (i % 2) * 8, jenis='gadis', baju='h' if i % 2 else 'a')
    return o


def silsilah(label, kiri_jenis, sorot_jenis, sorot_tinggi, kanan=True):
    """Orang tua berlabel + saudaranya yang dilingkari."""
    o = lantai() + orang(90, tinggi=150, jenis=kiri_jenis, baju='a') + kotak(56, 12, 68, 30, 'a', 6) + teks(90, 34, label, 18)
    x = 210
    o += elips(x, 200 - sorot_tinggi / 2, 52, sorot_tinggi / 2 + 20, 'g') + orang(x, tinggi=sorot_tinggi, jenis=sorot_jenis, baju='h')
    return o + garis((120, 120), (170, 120), lebar=3)


A['C13-L4a'] = kakek_cucu(1)
A['C13-L4b'] = kakek_cucu(5)
A['C13-L4c'] = kakek_cucu(3)
A['C13-L5a'] = silsilah('爸爸', 'pria', 'wanita', 135)
A['C13-L5b'] = silsilah('媽媽', 'wanita', 'wanita', 160)
A['C13-L5c'] = silsilah('爸爸', 'pria', 'pria', 165)
A['C13-L6a'] = A['C13-L5c']
A['C13-L6b'] = A['C13-L5a']
A['C13-L6c'] = silsilah('媽媽', 'wanita', 'pria', 165)
A['C13-L8a'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='nenek', rambut='uban', baju='a', duduk=150) + ''.join(orang(x, tinggi=95, jenis='laki', baju='h' if i % 2 else 'p') for i, x in enumerate((40, 80, 220, 260)))
A['C13-L8b'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='nenek', rambut='uban', baju='a', duduk=150)
A['C13-L8c'] = lantai() + kakek(110) + orang(190, tinggi=95, jenis='laki', baju='h')
A['C13-L9'] = lantai() + ''.join(orang(30 + i * 40, tinggi=(150, 160, 145, 100, 90, 155, 95, 150)[i], jenis=('nenek', 'pria', 'wanita', 'laki', 'gadis', 'pria', 'laki', 'wanita')[i], baju='ahpahapa'[i]) for i in range(8)) + teks(150, 30, '🧧', 20) if False else lantai() + ''.join(orang(30 + i * 40, tinggi=(150, 160, 145, 100, 90, 155, 95, 150)[i], jenis=('nenek', 'pria', 'wanita', 'laki', 'gadis', 'pria', 'laki', 'wanita')[i], baju='ahpahapa'[i]) for i in range(8))
A['C13-L10'] = lantai() + orang(110, tinggi=150, jenis='pria', baju='a') + kotak(76, 12, 68, 30, 'a', 6) + teks(110, 34, '爸爸', 18) + orang(200, tinggi=165, jenis='pria', baju='h') + teks(200, 30, '?', 26, angka=True)
A['C13-T3a'] = silsilah('爸爸', 'pria', 'pria', 165)
A['C13-T3b'] = silsilah('媽媽', 'wanita', 'pria', 150).replace('', '') if False else lantai() + orang(90, tinggi=150, jenis='wanita', baju='a') + kotak(56, 12, 68, 30, 'a', 6) + teks(90, 34, '媽媽', 18) + elips(210, 120, 52, 95, 'g') + kakek(210) + garis((120, 120), (170, 120), lebar=3)
A['C13-T3c'] = silsilah('爸爸', 'pria', 'wanita', 150)
A['C13-T4a'] = lantai() + orang(150, tinggi=130, jenis='wanita', baju='a') + orang(60, tinggi=165, jenis='pria', baju='h') + orang(220, tinggi=100, jenis='gadis', baju='p') + orang(265, tinggi=95, jenis='gadis', baju='h') + panah(150, 40, 150, 60, 4) + teks(150, 34, '我', 18)
A['C13-T4b'] = lantai() + orang(150, tinggi=130, jenis='wanita', baju='a') + orang(60, tinggi=165, jenis='pria', baju='h') + orang(220, tinggi=100, jenis='laki', baju='p') + orang(265, tinggi=145, jenis='wanita', baju='h') + panah(150, 40, 150, 60, 4) + teks(150, 34, '我', 18)
A['C13-T4c'] = lantai() + orang(110, tinggi=130, jenis='wanita', baju='a') + orang(190, tinggi=100, jenis='gadis', baju='p') + orang(240, tinggi=95, jenis='gadis', baju='h') + panah(110, 40, 110, 60, 4) + teks(110, 34, '我', 18)
A['C13-T6a'] = lantai() + orang(60, tinggi=165, jenis='pria', baju='h') + orang(110, tinggi=155, jenis='wanita', baju='a') + orang(190, tinggi=100, jenis='laki', baju='p') + orang(240, tinggi=95, jenis='laki', baju='h')
A['C13-T6b'] = lantai() + orang(60, tinggi=165, jenis='pria', baju='h') + orang(110, tinggi=155, jenis='wanita', baju='a') + orang(190, tinggi=100, jenis='laki', baju='p') + orang(240, tinggi=95, jenis='gadis', baju='h')
A['C13-T6c'] = lantai() + orang(80, tinggi=165, jenis='pria', baju='h') + orang(130, tinggi=155, jenis='wanita', baju='a') + orang(210, tinggi=95, jenis='gadis', baju='h')
A['C13-T7'] = lantai() + orang(150, tinggi=150, jenis='nenek', rambut='uban', baju='a', wajah='tawa') + meja(150, 200, 80)[:0] + kue_ultah(150, 60, '', .5)[:0] + ''.join(orang(x, tinggi=95, jenis='laki' if i % 2 else 'gadis', baju='h' if i % 2 else 'p') for i, x in enumerate((40, 85, 215, 260))) + kue_ultah(150, 196, '', .5)
A['C13-T8'] = lantai() + orang(70, tinggi=140, jenis='laki', baju='h') + orang(150, tinggi=120, jenis='laki', baju='p') + orang(230, tinggi=95, jenis='gadis', baju='a') + panah(230, 40, 230, 70, 4) + teks(230, 34, '我', 18)

# --- C14 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def keluarga_n(n):
    jenis = ('pria', 'wanita', 'gadis', 'laki', 'gadis')
    ting = (165, 155, 120, 100, 90)
    w = 240 / n
    return lantai() + ''.join(orang(30 + w * (i + .5), tinggi=ting[i], jenis=jenis[i], baju='hapah'[i]) for i in range(n))


A['C14-L4a'] = keluarga_n(4)
A['C14-L4b'] = keluarga_n(5)
A['C14-L4c'] = keluarga_n(3)
A['C14-L5a'] = lantai() + bioskop(90) + jalan_kaki(200, 'wanita', 150, 'a') + jalan_kaki(250, 'pria', 160, 'h') + panah(160, 40, 280, 40, 4)
A['C14-L5b'] = lantai() + bioskop(210) + jalan_kaki(80, 'wanita', 150, 'a') + panah(40, 40, 140, 40, 4) + jam_kecil(60, 40, 7, 58, 20)
A['C14-L5c'] = lantai() + bioskop(150) + silang(150, 160, 30, 8)
A['C14-L6a'] = kalender_senin(150, 60, 5, 5)
A['C14-L6b'] = kalender_senin(150, 60, 4, 4)
A['C14-L6c'] = kalender_senin(150, 60, 6, 6)
A['C14-L8a'] = lantai() + orang(150, tinggi=150, jenis='nenek', rambut='uban', baju='a', wajah='sedih')
A['C14-L8b'] = lantai() + orang(150, tinggi=150, jenis='nenek', rambut='pendek', rok=False, baju='p', kacamata=True, wajah='tawa') + garis((174, 124), (180, 200), lebar=4)
A['C14-L8c'] = lantai() + orang(70, tinggi=150, jenis='nenek', rambut='uban', baju='a', wajah='tawa') + gelembung(200, 70, 150, 110, pengantin(200, 110).replace('', '') if False else bulat(185, 70, 14, 't') + bulat(205, 70, 14, 't') + bintang(195, 50, 6), (-1, 1))
A['C14-L9'] = A['C14-1']
A['C14-L10'] = keluarga_n(5)
A['C14-T3a'] = jam_dinding(150, 105, 80, 8, 0)
A['C14-T3b'] = jam_dinding(150, 105, 80, 7, 55)
A['C14-T3c'] = jam_dinding(150, 105, 80, 7, 30)
A['C14-T4a'] = lantai() + sofa(170) + orang(80, tinggi=150, jenis='wanita', baju='a', wajah='senyum')
A['C14-T4b'] = lantai() + papan_tulis(95, 30, 150, 80) + orang(230, tinggi=160, jenis='wanita', baju='a', tangan={'ki': [(10, -10), (34, -40)]})
A['C14-T4c'] = lantai() + dokter2(150, 200, 160)
A['C14-T6a'] = lantai() + papan_tulis(150, 20, 140, 60) + orang(100, tinggi=160, jenis='pria', baju='a') + orang(200, tinggi=150, jenis='wanita', baju='h')
A['C14-T6b'] = lantai() + pengantin(150, 170)
A['C14-T6c'] = lantai() + orang(100, tinggi=150, jenis='nenek', rambut='pendek', rok=False, baju='p', kacamata=True) + orang(200, tinggi=145, jenis='nenek', rambut='uban', baju='a')
A['C14-T7'] = A['C14-3']
A['C14-T8'] = lantai() + pengantin(150, 170)

# --- C15 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def laptop(x, y, s=1.0):
    return kotak(x - 40 * s, y - 50 * s, 80 * s, 50 * s, 'h', 4) + kotak(x - 34 * s, y - 44 * s, 68 * s, 38 * s, 'a', 2) + kotak(x - 50 * s, y, 100 * s, 8 * s, 'p', 3)


def ponsel_c15(x, y, s=1.0):
    return kotak(x - 22 * s, y - 40 * s, 44 * s, 80 * s, 'h', 8) + kotak(x - 17 * s, y - 32 * s, 34 * s, 60 * s, 'a', 3)


def pekerja(x, kaki=200, tinggi=160):
    return orang(x, kaki=kaki, tinggi=tinggi, jenis='pria', baju='p', tangan={'ka': [(20, 16), (44, 4)]}) + jalur(f'M{x - 18} {kaki - tinggi + 14} q18 -26 36 0 z', 'a') + garis((x - 22, kaki - tinggi + 14), (x + 22, kaki - tinggi + 14), lebar=4)


A['C15-L4a'] = lantai() + meja(150, 150, 180) + laptop(150, 146, 1.1) + panah(60, 40, 110, 70, 4)
A['C15-L4b'] = ponsel_c15(150, 105, 1.6)
A['C15-L4c'] = lantai() + rumah(110, 200, 120, 90) + uang_kertas(230, 70, '$', 90, 44) + panah(200, 110, 160, 140, 4)
A['C15-L5a'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'sedih') + termometer(240, 40, 39, 42, 70)
A['C15-L5b'] = lantai() + orang(80, tinggi=150, jenis='wanita', baju='p', wajah='sedih') + termometer(30, 40, 39, 42, 70) + panah(120, 100, 180, 100, 4) + kotak(190, 120, 100, 80, 'a') + orang(240, kaki=200, tinggi=150, jenis='wanita', baju='h')
A['C15-L5c'] = lantai() + dokter2(220, 200, 160) + orang(90, tinggi=150, jenis='wanita', baju='a', wajah='sedih')
A['C15-L6a'] = lantai() + toko(110, 200, 140, 110) + teks(110, 80, '超市', 18) + orang(230, tinggi=150, jenis='pria', baju='h') + gelembung(250, 40, 70, 46, laptop(250, 54, .5), (-1, 1))
A['C15-L6b'] = lantai() + orang(80, tinggi=160, jenis='pria', baju='p', wajah='marah') + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='marah') + orang(230, tinggi=140, jenis='pria', baju='h', wajah='sedih') + silang(230, 40, 16, 5) + uang_kertas(180, 40, '$', 50, 24)
A['C15-L6c'] = lantai() + toko(150, 200, 170, 120) + teks(150, 70, '超市', 20) + bentuk((230, 30), (236, 44), (252, 44), (240, 54), (246, 70), (230, 60), (214, 70), (220, 54), (208, 44), (224, 44), k='h')
A['C15-L8a'] = lantai() + sofa(150) + ponsel_c15(150, 100, .6) + orang(150, tinggi=120, jenis='laki', baju='h', duduk=150, wajah='tawa')
A['C15-L8b'] = lantai() + toko(170, 200, 150, 110) + teks(170, 80, '超市', 18) + jalan_kaki(60, 'laki', 120, 'h') + keranjang(90, 200, .6)
A['C15-L8c'] = lantai() + kotak(120, 120, 164, 80, 'a') + kotak(200, 20, 80, 34, 'a', 6) + teks(240, 44, '超市', 18) + orang(170, kaki=200, tinggi=120, jenis='laki', baju='p') + kotak(60, 130, 50, 40, 'p', 3) + kotak(64, 110, 40, 22, 'a', 3)
A['C15-L9'] = lantai() + pekerja(120) + kotak(190, 150, 30, 50, 'p') + kotak(220, 150, 30, 50, 'p') + kotak(205, 100, 30, 50, 'p')
A['C15-L10'] = A['C15-5']
A['C15-T3a'] = uang_kertas(150, 105, '$', 200, 100)
A['C15-T3b'] = lantai() + meja(150, 150, 200) + piring(110, 144, 40, '') + piring(190, 144, 40, '') + kotak(100, 30, 100, 50, 'a', 6) + teks(150, 66, '$0', 32, angka=True)
A['C15-T3c'] = lantai() + kotak(150, 120, 134, 80, 'a') + orang(220, kaki=200, tinggi=145, jenis='wanita', baju='h') + orang(70, tinggi=140, jenis='pria', baju='a') + gelembung(150, 30, 90, 40, teks(150, 40, '你好', 20), (-1, 1))
A['C15-T4a'] = lantai() + pekerja(150)
A['C15-T4b'] = A['C15-2']
A['C15-T4c'] = lantai() + papan_tulis(80, 30, 120, 70) + orang(200, tinggi=160, jenis='pria', baju='a', tangan={'ki': [(10, -10), (30, -30)]})
A['C15-T6a'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + teks(130, 110, 'Z z', 18, angka=True)
A['C15-T6b'] = lantai() + meja(150, 150, 200) + buku_tumpuk(110, 150, 3, 50, 12) + orang(200, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C15-T6c'] = lantai() + bola(200, 186, 14) + orang(120, tinggi=150, jenis='wanita', baju='a', wajah='tawa', tangan=LAMBAI)
A['C15-T7'] = A['C15-2']
A['C15-T8'] = lantai() + orang(80, tinggi=150, jenis='pria', baju='a', wajah='sedih') + termometer(30, 40, 39, 42, 70) + panah(120, 100, 180, 100, 4) + kotak(190, 120, 100, 80, 'a') + orang(240, kaki=200, tinggi=150, jenis='wanita', baju='h')

# --- C16 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def ruang_rapat(jam_h=None):
    o = kotak(16, 16, 268, 188, 'p') + meja(150, 150, 220) + orang(60, tinggi=130, jenis='wanita', duduk=160, baju='a') + orang(240, tinggi=135, jenis='pria', duduk=160, baju='h') + kotak(100, 30, 100, 56, 'a', 4) + grafik([2, 4, 3, 6], 110, 80, 80, 44)
    return o + (jam_dinding(250, 50, 24, jam_h, 0) if jam_h is not None else '')


def tulis_laporan(x=150, jenis='wanita', malam=False):
    o = lantai() + meja(x + 40, 150, 160) + kertas(x + 40, 120, 60, 40, 0) + orang(x - 50, tinggi=150, jenis=jenis, baju='a', duduk=150, tangan={'ka': [(20, 10), (60, 4)]})
    return o + (jendela(240, 20, 50, 40) + bulan_bintang(236, 40, .35) if malam else '')


A['C16-L4a'] = lantai() + sofa(170) + meja(70, 150, 90) + kotak(40, 100, 60, 46, 'h', 4) + kotak(46, 106, 48, 34, 'a', 2) + orang(170, tinggi=150, jenis='pria', baju='a', duduk=150, tangan={'ka': [(20, 10), (40, 0)]}) + jendela(240, 20, 50, 40)
A['C16-L4b'] = ruang_rapat()
A['C16-L4c'] = A['C16-3']
A['C16-L5a'] = ruang_rapat()
A['C16-L5b'] = tulis_laporan()
A['C16-L5c'] = lantai() + orang_ponsel(150, 'wanita', 150, baju='a')
A['C16-L6a'] = jam_dinding(150, 105, 80, 9, 0)
A['C16-L6b'] = jam_dinding(150, 105, 80, 11, 0)
A['C16-L6c'] = jam_dinding(150, 105, 80, 10, 0)
A['C16-L8a'] = kotak(16, 16, 268, 188, 'p') + jendela(230, 30, 60, 46) + matahari(254, 52, 10) + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'a')
A['C16-L8b'] = kotak(16, 16, 268, 188, 'p') + jendela(230, 30, 60, 46) + bulan_bintang(226, 52, .4) + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'a') + jam_dinding(60, 40, 20, 10, 0)
A['C16-L8c'] = lantai() + jendela(230, 30, 60, 46) + bulan_bintang(226, 52, .4) + sofa(120) + tv(250, 150, 50) + orang(120, tinggi=140, jenis='pria', baju='a', duduk=150)
A['C16-L9'] = tulis_laporan(jenis='pria')
A['C16-L10'] = lantai() + sofa(150) + orang(150, tinggi=140, jenis='pria', baju='a', duduk=150, wajah='tawa') + kalender_senin(150, 10, 6, 6, 220)[:0]
A['C16-T3a'] = A['C16-L8b']
A['C16-T3b'] = lantai() + matahari(250, 40, 14) + kotak(16, 60, 110, 140, 'p') + teks(70, 90, '公司', 18) + jalan_kaki(190, 'pria', 160, 'h') + panah(140, 120, 260, 120, 4) + jam_kecil(40, 30, 5, 0, 18)
A['C16-T3c'] = tulis_laporan(jenis='pria')
A['C16-T4a'] = kalender_senin(150, 60, None, None).replace('', '') + ''.join(bulat(150 - 140 + 40 * (i + .5), 108, 10, 'h') for i in range(7))
A['C16-T4b'] = kalender_senin(150, 60, None, 4) + jam_kecil(150, 170, 3, 0, 22)
A['C16-T4c'] = kalender_senin(150, 60, None, 0) + jam_kecil(150, 170, 9, 0, 22)
A['C16-T6a'] = A['C16-T3b']
A['C16-T6b'] = A['C16-L8b']
A['C16-T6c'] = kotak(16, 16, 268, 188, 'p') + jendela(230, 30, 60, 46) + matahari(254, 52, 10) + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'a') + jam_dinding(60, 40, 20, 5, 0)
A['C16-T7'] = ruang_rapat()
A['C16-T8'] = lantai() + kertas(150, 80, 120, 140, 0) + ''.join(garis((110, 40 + i * 16), (190, 40 + i * 16), k='t') for i in range(5)) + panah(220, 120, 270, 120, 4) + orang(270, tinggi=150, jenis='pria', baju='h')[:0]

# --- C17 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kamera_c17(x, y, s=1.0):
    return kotak(x - 40 * s, y - 24 * s, 80 * s, 52 * s, 'h', 8) + kotak(x - 30 * s, y - 34 * s, 22 * s, 12 * s, 'h', 3) + bulat(x, y + 2 * s, 18 * s, 'a') + bulat(x, y + 2 * s, 9 * s, 'p')


def foto_orang(x=110, jenis='wanita', tinggi=150):
    return lantai() + orang(x, tinggi=tinggi, jenis=jenis, baju='a', tangan={'ka': [(16, -6), (34, -14)], 'ki': [(16, -6), (34, -14)]}) + kamera_c17(x + 40, 200 - tinggi + 40, .5) + pohon(250, s=.7)


def lukis(x=110, jenis='wanita', tinggi=150):
    return lantai() + orang(x, tinggi=tinggi, jenis=jenis, baju='a', tangan={'ka': [(20, -4), (46, -10)]}) + garis((190, 200), (210, 70), lebar=4) + garis((250, 200), (210, 70), lebar=4) + kotak(170, 60, 80, 70, 'a', 2) + jalur('M180 110 q20 -30 40 0 t30 -10', 'g', 3)


def nyanyi(x=150, jenis='wanita', tinggi=150):
    return lantai() + orang(x, tinggi=tinggi, jenis=jenis, baju='a', wajah='nyanyi', tangan={'ka': [(16, -6), (14, -24)]}) + not_musik(x + 50, 50) + not_musik(x + 80, 80)


A['C17-L4a'] = foto_orang(jenis='pria', tinggi=160)
A['C17-L4b'] = A['C17-3']
A['C17-L4c'] = lantai() + kotak(16, 130, 268, 70, 'p') + ''.join(jalur(f'M{x} 150 q10 -8 20 0 t20 0', 'g', 3) for x in (30, 150, 210)) + bulat(110, 140, 13) + muka(110, 140, 13, 'senyum') + garis((90, 150), (70, 132), lebar=4) + garis((130, 150), (150, 132), lebar=4)
A['C17-L5a'] = lantai() + orang(100, tinggi=160, jenis='pria', baju='a', wajah='marah', tangan={'ka': [(20, -6), (40, -20)]}) + orang(200, tinggi=155, jenis='wanita', baju='h', wajah='marah', tangan={'ki': [(20, -6), (40, -20)]}) + teks(150, 40, '!!', 26, angka=True)
A['C17-L5b'] = lantai() + orang(90, tinggi=155, jenis='wanita', baju='a', wajah='tawa') + orang(200, tinggi=160, jenis='pria', baju='h', wajah='tawa', tangan={'ki': [(16, 10), (44, 4)]}) + piring(140, 100, 40, kue(140, 98, .3) if False else bakpao(140, 96, .4))
A['C17-L5c'] = lantai() + rumah(100, 200, 110, 80) + pohon(230) + jalan_kaki(260, 'wanita', 100, 'a')[:0]
A['C17-L6a'] = A['C17-3']
A['C17-L6b'] = lantai() + sofa(150) + orang(150, tinggi=140, jenis='pria', baju='a', duduk=150) + orang(200, tinggi=135, jenis='wanita', baju='h', duduk=150)
A['C17-L6c'] = A['C17-5']
A['C17-L8a'] = foto_orang(jenis='gadis', tinggi=120)
A['C17-L8b'] = lukis(jenis='gadis', tinggi=120)
A['C17-L8c'] = nyanyi(jenis='gadis', tinggi=120)
A['C17-L9'] = A['C17-5']
A['C17-L10'] = lantai() + toko(220, 200, 140, 120) + orang(200, tinggi=150, jenis='pria', baju='h', wajah='tawa', tangan=LAMBAI) + orang(80, tinggi=150, jenis='wanita', baju='a', wajah='senyum')
A['C17-T3a'] = A['C17-3']
A['C17-T3b'] = foto_orang(jenis='pria', tinggi=160)
A['C17-T3c'] = A['C17-5']
A['C17-T4a'] = foto_orang(jenis='wanita', tinggi=150)
A['C17-T4b'] = lukis(jenis='wanita', tinggi=150)
A['C17-T4c'] = lantai() + pesawat(200, 50, .8) + orang(80, tinggi=150, jenis='wanita', baju='a') + koper(130, 200, .8)
A['C17-T6a'] = lantai() + gunung(170, 200, 260, 170, False) + orang(150, kaki=110, tinggi=90, jenis='nenek', rambut='pendek', rok=False, baju='p', kacamata=True)
A['C17-T6b'] = lantai() + sofa(150) + orang(150, tinggi=150, jenis='nenek', rambut='pendek', rok=False, baju='p', kacamata=True, duduk=150)
A['C17-T6c'] = lantai() + matahari(250, 40, 14) + pohon(50, s=.8) + bangku(200) + jalan_kaki(130, 'pria', 150, 'p')
A['C17-T7'] = A['C17-1']
A['C17-T8'] = lantai() + gunung(220, 200, 180, 110, False) + orang(80, tinggi=150, jenis='pria', baju='a', wajah='lelah') + ''.join(jalur(f'M{110 + i * 24} {196 - (i % 2) * 8} q6 -8 12 0 z', 'h') for i in range(4))

# --- C18 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def konsol(x, y, s=1.0):
    return kotak(x - 34 * s, y - 16 * s, 68 * s, 32 * s, 'h', 14) + bulat(x - 18 * s, y, 5 * s, 'a') + bulat(x + 18 * s, y, 5 * s, 'a')


def majalah(x, y, s=1.0, foto=True):
    o = kotak(x - 50 * s, y - 64 * s, 100 * s, 128 * s, 'a', 4) + kotak(x - 40 * s, y - 54 * s, 80 * s, 54 * s, 'p', 2)
    if foto:
        o += gunung(x, y, 70 * s, 40 * s, False)[:0] + bentuk((x - 36 * s, y), (x - 10 * s, y - 40 * s), (x + 10 * s, y - 16 * s), (x + 24 * s, y - 34 * s), (x + 36 * s, y), k='h') + bulat(x + 26 * s, y - 44 * s, 6 * s, 'a')
    return o + ''.join(garis((x - 40 * s, y + (14 + i * 12) * s), (x + 40 * s, y + (14 + i * 12) * s), k='t') for i in range(3))


def koran_c18(x, y, s=1.0):
    o = kotak(x - 60 * s, y - 60 * s, 120 * s, 120 * s, 'a', 2) + kotak(x - 50 * s, y - 50 * s, 100 * s, 20 * s, 'h', 2)
    return o + ''.join(garis((x - 50 * s, y + (-16 + i * 12) * s), (x + 50 * s, y + (-16 + i * 12) * s), k='t') for i in range(6))


A['C18-L4a'] = lantai() + sofa(150) + orang(150, tinggi=150, jenis='pria', baju='a', duduk=150, wajah='lelah') + konsol(230, 186, .6) + silang(230, 150, 12, 4)
A['C18-L4b'] = lantai() + sofa(150) + orang(150, tinggi=150, jenis='pria', baju='a', duduk=150, wajah='tawa', tangan={'ki': [(14, 20), (30, 16)], 'ka': [(14, 20), (30, 16)]}) + konsol(150, 116, .5) + not_musik(220, 50, .6)
A['C18-L4c'] = lantai() + orang(100, tinggi=160, jenis='pria', baju='a', wajah='marah', tangan={'ka': [(20, -6), (40, -20)]}) + orang(210, tinggi=155, jenis='pria', baju='h', wajah='sedih')
A['C18-L5a'] = lantai() + awan(150, 20, 1.0, 'a') + hujan(150, 30, 260, 40) + payung(150, 80, 46) + orang(150, tinggi=150, jenis='wanita', baju='a')
A['C18-L5b'] = lantai() + matahari(240, 50, 22) + orang(130, tinggi=150, jenis='wanita', baju='a', wajah='lelah') + keringat(104, 70) + keringat(156, 74)
A['C18-L5c'] = lantai() + ''.join(salju(x, y) for x, y in ((40, 40), (100, 70), (170, 40), (250, 60), (60, 120), (220, 120))) + orang(150, tinggi=150, jenis='wanita', baju='h', wajah='sedih')
A['C18-L6a'] = majalah(150, 105, 1.2)
A['C18-L6b'] = lantai() + kotak(30, 20, 240, 110, 'h', 4) + kotak(40, 30, 220, 90, 'p', 2) + ''.join(potret(x, 196, 18, 'pria' if i % 2 else 'wanita', 'senyum', 'a') for i, x in enumerate((70, 130, 190, 250)))
A['C18-L6c'] = A['C18-3']
A['C18-L8a'] = A['C18-4']
A['C18-L8b'] = lantai() + tv(200, 150, 120) + meja(200, 150, 110) + orang(80, tinggi=120, jenis='laki', duduk=160, baju='a', wajah='lelah') + konsol(130, 186, .5)
A['C18-L8c'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=120, jenis='laki', duduk=150, baju='a', tangan={'ki': [(20, 24), (34, 30)], 'ka': [(20, 24), (34, 30)]}) + buku(150, 116, 50, 10, 'a')
A['C18-L9'] = A['C18-3']
A['C18-L10'] = A['C18-L5b']
A['C18-T3a'] = lantai() + majalah(90, 100, .7) + orang(200, tinggi=150, jenis='pria', baju='a', wajah='tawa', tangan=LAMBAI)
A['C18-T3b'] = lantai() + majalah(90, 100, .7) + orang(200, tinggi=150, jenis='pria', baju='a', wajah='lelah') + teks(250, 60, 'Z z', 18, angka=True)
A['C18-T3c'] = lantai() + majalah(90, 100, .7) + orang(200, tinggi=150, jenis='pria', baju='a', wajah='marah', tangan={'ka': [(20, -6), (40, -20)]})
A['C18-T4a'] = lantai() + sofa(140) + tv(250, 150, 60) + orang(110, tinggi=140, jenis='pria', baju='a', duduk=150) + orang(170, tinggi=135, jenis='wanita', baju='h', duduk=150)
A['C18-T4b'] = lantai() + bioskop(150)
A['C18-T4c'] = lantai() + gedung(150, tingkat=3, lebar=160, tt=30) + teks(150, 30, '學校', 22)
A['C18-T6a'] = majalah(150, 105, 1.2)
A['C18-T6b'] = koran_c18(150, 105, 1.2)
A['C18-T6c'] = konsol(150, 105, 2.0)
A['C18-T7'] = lantai() + sofa(150) + tv(260, 150, 50) + orang(150, tinggi=150, jenis='pria', baju='a', duduk=150, wajah='lelah') + teks(200, 60, '...', 22, angka=True)
A['C18-T8'] = lantai() + koran_c18(80, 100, .6) + silang(80, 100, 30, 6) + majalah(220, 100, .6) + bentuk((220, 20), (226, 32), (240, 32), (230, 40), (234, 54), (220, 46), (206, 54), (210, 40), (200, 32), (214, 32), k='h')

# --- C19 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kamar_hotel(x, w=110):
    return kotak(x - w / 2, 40, w, 160, 'p') + ranjang(x, 200, w - 16) + kotak(x - 18, 50, 36, 22, 'a', 4)


def museum_c19(x=150, s=1.0):
    """Gedung museum generik (bukan bangunan tertentu): gedung lebar + bingkai lukisan di depan."""
    w, h = 220 * s, 130 * s
    o = kotak(x - w / 2, 200 - h, w, h, 'p') + kotak(x - w / 2 - 8 * s, 200 - h - 14 * s, w + 16 * s, 14 * s, 'h')
    o += kotak(x - 50 * s, 200 - h + 16 * s, 100 * s, 60 * s, 'h', 3) + kotak(x - 44 * s, 200 - h + 22 * s, 88 * s, 48 * s, 'a', 2)
    o += bentuk((x - 40 * s, 200 - h + 66 * s), (x - 10 * s, 200 - h + 34 * s), (x + 10 * s, 200 - h + 52 * s), (x + 24 * s, 200 - h + 40 * s), (x + 40 * s, 200 - h + 66 * s), k='p')
    return o + kotak(x - 18 * s, 200 - 44 * s, 36 * s, 44 * s, 'h')


def lukisan_dinding():
    return kotak(16, 16, 268, 188, 'p') + kotak(60, 40, 180, 110, 'h', 4) + kotak(70, 50, 160, 90, 'a', 2) + bentuk((80, 130), (130, 70), (160, 110), (190, 80), (220, 130), k='p') + bulat(200, 70, 9, 'p')


A['C19-L4a'] = lantai() + kamar_hotel(80) + kamar_hotel(220)
A['C19-L4b'] = A['C19-5']
A['C19-L4c'] = lantai() + kamar_hotel(150, 150)
A['C19-L5a'] = A['C19-3']
A['C19-L5b'] = lantai() + museum_c19()
A['C19-L5c'] = lantai() + gedung(150, tingkat=6, lebar=120, tt=24) + kotak(100, 14, 100, 30, 'a', 4) + teks(150, 36, 'HOTEL', 18, angka=True)
A['C19-L6a'] = lantai() + museum_c19()
A['C19-L6b'] = A['C19-3']
A['C19-L6c'] = lantai() + meja(150, 150, 220) + piring(100, 144, 50, nasi_goreng(100, 140, .5) if False else '') + piring(200, 144, 50, '') + orang(60, tinggi=130, jenis='wanita', duduk=150, baju='a') + orang(240, tinggi=135, jenis='pria', duduk=150, baju='h')
A['C19-L8a'] = dua_panel(lampion(75, 90, 1.2) + teks(75, 40, '1', 30, angka=True), teks(225, 40, '2', 30, angka=True) + museum_c19(225, .55)) + lantai()
A['C19-L8b'] = dua_panel(teks(75, 40, '1', 30, angka=True) + museum_c19(75, .55), lampion(225, 90, 1.2) + teks(225, 40, '2', 30, angka=True)) + lantai()
A['C19-L8c'] = lantai() + museum_c19()
A['C19-L9'] = A['C19-3']
A['C19-L10'] = lantai() + meja(150, 150, 200) + kotak(110, 90, 80, 60, 'h', 4) + kotak(116, 96, 68, 48, 'a', 2) + tiket(150, 120, 50, 24) + orang(240, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C19-T3a'] = A['C19-3']
A['C19-T3b'] = lantai() + gelas(150, 196, 'teh', 1.6) + orang(60, tinggi=150, jenis='pria', baju='h')
A['C19-T3c'] = lantai() + ''.join(garis((110 + i * 30, 60), (110 + i * 30, 180), lebar=3) + ''.join(bulat(110 + i * 30, 80 + j * 24, 9, 'p') for j in range(3)) for i in range(3))
A['C19-T4a'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(24, -20), (36, -56)]}, kaki_pose={'ki': (-8, 0), 'ka': (30, -24)})
A['C19-T4b'] = A['C19-3']
A['C19-T4c'] = lukisan_dinding() + orang(250, tinggi=120, jenis='wanita', baju='a')
A['C19-T6a'] = lantai() + meja(160, 140, 200) + kertas(170, 128, 70, 22) + orang(90, tinggi=140, jenis='laki', duduk=150, baju='a', tangan={'ka': [(22, 10), (60, 14)]})
A['C19-T6b'] = lantai() + ranjang(150, 200, 200) + orang(150, kaki=150, tinggi=60, jenis='laki', baju='a')[:0] + bulat(80, 136, 13) + muka(80, 136, 13, 'senyum') + not_musik(150, 80) + not_musik(190, 60)
A['C19-T6c'] = lantai() + meja(160, 140, 200) + kertas(170, 128, 70, 22) + orang(90, tinggi=140, jenis='laki', duduk=150, baju='a', tangan={'ka': [(22, 10), (60, 14)]}) + headphone(90, sendi(90, 150, 140, 'laki', 150)['cy'], sendi(90, 150, 140, 'laki', 150)['r']) + not_musik(240, 60)
A['C19-T7'] = lantai() + museum_c19() + tiket(240, 40, 70, 30)
A['C19-T8'] = A['C19-1']

# --- C20 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def gerbong_kosong(n_duduk=0, satu_kosong=False):
    o = gerbong_mrt(False)
    if satu_kosong:
        for i in range(6):
            if i != 3:
                o += orang(45 + i * 42, kaki=150, tinggi=110, jenis='pria' if i % 2 else 'wanita', baju='a', duduk=140)
        o += lingkaran_sorot(171, 130) if False else bulat(171, 130, 20, 'g')
    return o


def peron(penuh):
    o = kotak(16, 16, 268, 188, 'a') + kotak(16, 160, 268, 44, 'p') + garis((16, 160), (284, 160), lebar=5) + kotak(40, 40, 220, 26, 'h', 4) + teks(150, 60, '月臺', 18, warna='#fff')
    if penuh:
        o += ''.join(orang(40 + i * 37, kaki=160, tinggi=90 + (i % 3) * 6, jenis='pria' if i % 2 else 'wanita', baju='h' if i % 3 == 0 else 'a') for i in range(7))
    return o


def nomor_keluar(n):
    return kotak(16, 16, 268, 188, 'a') + papan_keluar(150, 70, str(n), 0, 190, 70)


A['C20-L4a'] = gerbong_mrt(False)
A['C20-L4b'] = gerbong_mrt(True)
A['C20-L4c'] = gerbong_kosong(satu_kosong=True)
A['C20-L5a'] = peron(True)
A['C20-L5b'] = gerbong_mrt(False) + orang(100, kaki=150, tinggi=110, jenis='wanita', baju='a', duduk=140) + orang(150, kaki=150, tinggi=115, jenis='pria', baju='h', duduk=140) + kotak(200, 40, 70, 30, 'h', 4) + panah(210, 55, 260, 55, 3)
A['C20-L5c'] = lantai() + kotak(30, 60, 120, 140, 'p') + papan_keluar(90, 70, '', 0, 100, 40) + jalan_kaki(200, 'wanita', 150, 'a') + jalan_kaki(250, 'pria', 160, 'h')
A['C20-L6a'] = nomor_keluar(2)
A['C20-L6b'] = nomor_keluar(3)
A['C20-L6c'] = nomor_keluar(5)
A['C20-L8a'] = peron(False)
A['C20-L8b'] = gerbong_mrt(True)
A['C20-L8c'] = peron(True)
A['C20-L9'] = gerbong_mrt(False) + orang(60, kaki=150, tinggi=110, jenis='pria', baju='a', duduk=140) + bulat(170, 130, 22, 'g')
A['C20-L10'] = A['C20-3']
A['C20-T3a'] = nomor_keluar(1)
A['C20-T3b'] = nomor_keluar(2)
A['C20-T3c'] = nomor_keluar(4)
A['C20-T4a'] = lantai() + gedung(170, tingkat=4, lebar=120, tt=28) + kotak(120, 14, 100, 30, 'a', 4) + teks(170, 36, '銀行', 18) + kotak(40, 120, 60, 80, 'h', 4) + teks(70, 152, '捷運', 18, warna='#fff')
A['C20-T4b'] = lantai() + sekolah(170, 200, 140, 100) + kotak(40, 120, 60, 80, 'h', 4) + teks(70, 152, '捷運', 18, warna='#fff')
A['C20-T4c'] = lantai() + rumah_sakit(170, 200, 140, 110) + kotak(40, 120, 60, 80, 'h', 4) + teks(70, 152, '捷運', 18, warna='#fff')
A['C20-T6a'] = peron(True)
A['C20-T6b'] = lantai() + bus(200, 200, 150)[:0] + garis((60, 70), (60, 200), lebar=5) + kotak(30, 40, 60, 30, 'a', 4) + teks(60, 62, 'BUS', 16, angka=True) + ''.join(orang(120 + i * 44, tinggi=150, jenis='pria' if i % 2 else 'wanita', baju='a') for i in range(4))
A['C20-T6c'] = lantai() + mobil(170, 200, 170, True) + orang(50, tinggi=150, jenis='wanita', baju='a', tangan=LAMBAI)
A['C20-T7'] = kotak(16, 16, 268, 188, 'a') + kereta(150, 160, 230) + jam_kecil(60, 50, 8, 0, 22) + jam_kecil(150, 50, 8, 5, 22) + jam_kecil(240, 50, 8, 10, 22)
A['C20-T8'] = lantai() + kotak(20, 60, 100, 140, 'p') + papan_keluar(70, 70, '', 1, 90, 40) + panah(130, 140, 180, 140, 4) + gedung(240, tingkat=4, lebar=90, tt=30) + teks(240, 50, '百貨', 16)

# --- C21 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def naik_motor(x=150, jenis='pria'):
    return lantai() + skuter(x, 200, 1.0) + orang(x - 10, kaki=160, tinggi=110, jenis=jenis, baju='a', duduk=150, tangan={'ka': [(20, 10), (50, 4)]})


def naik_sepeda(x=150, jenis='pria'):
    o = lantai() + bulat(x - 50, 176, 24, 't') + bulat(x + 50, 176, 24, 't') + bulat(x - 50, 176, 26, 'g') + bulat(x + 50, 176, 26, 'g')
    o += garis((x - 50, 176), (x - 6, 176), (x + 26, 130), (x - 26, 130), (x - 50, 176), lebar=4) + garis((x + 26, 130), (x + 50, 176), lebar=4) + garis((x + 20, 120), (x + 36, 120), lebar=4)
    return o + orang(x - 20, kaki=170, tinggi=120, jenis=jenis, baju='a', duduk=130, tangan={'ka': [(20, 10), (50, 0)]})


def kotak_berat(x, y, s=1.0):
    return kotak(x - 40 * s, y - 40 * s, 80 * s, 70 * s, 'p', 4) + garis((x - 40 * s, y - 20 * s), (x + 40 * s, y - 20 * s), k='t')


def rambu_kec(angka):
    return lantai() + garis((150, 200), (150, 130), lebar=6) + bulat(150, 80, 56, 'g') + bulat(150, 80, 46, 'a') + teks(150, 96, angka, 40, angka=True)


A['C21-L4a'] = naik_motor()
A['C21-L4b'] = naik_sepeda()
A['C21-L4c'] = kotak(16, 16, 268, 188, 'a') + kotak(16, 150, 268, 54, 'p') + garis((16, 150), (284, 150), lebar=5) + kereta(150, 146, 250) + orang(250, kaki=200, tinggi=60, jenis='pria', baju='h')
A['C21-L5a'] = lantai() + kotak_berat(190, 170, 1.0) + orang(110, tinggi=150, jenis='wanita', baju='a', wajah='lelah', tangan={'ka': [(20, 30), (44, 40)]}) + keringat(84, 60) + jalur('M180 120 l-6 -10 M200 120 l6 -10', 'g', 3)
A['C21-L5b'] = lantai() + orang(140, tinggi=155, jenis='wanita', baju='a', wajah='tawa', tangan={'ka': [(16, -20), (26, -50)]}) + kotak_berat(170, 50, .6)
A['C21-L5c'] = lantai() + orang(110, tinggi=150, jenis='wanita', baju='a', wajah='senyum', tangan={'ka': [(20, 10), (50, 4)]}) + kotak(170, 140, 40, 30, 'a', 4)
A['C21-L6a'] = naik_sepeda()
A['C21-L6b'] = naik_motor()
A['C21-L6c'] = A['C21-L4c']
A['C21-L8a'] = lantai() + skuter(110, 200, .9) + skuter(220, 200, .9) + kotak(20, 20, 50, 50, 'h', 6) + teks(45, 56, 'P', 34, angka=True, warna='#fff')
A['C21-L8b'] = lantai() + rambu(150, mobil(150, 70, 60), True, 200, 50)
A['C21-L8c'] = A['C21-1']
A['C21-L9'] = naik_sepeda(jenis='pria')
A['C21-L10'] = A['C21-L5a']
A['C21-T3a'] = lantai() + pintu(80, 200, 150, 70) + skuter(200, 200, .9)
A['C21-T3b'] = lantai() + sekolah(220, 200, 130, 90) + kotak(20, 20, 50, 50, 'h', 6) + teks(45, 56, 'P', 34, angka=True, warna='#fff') + skuter(80, 200, .7)
A['C21-T3c'] = lantai() + garis((16, 150), (284, 150), k='t') + ''.join(garis((30 + i * 60, 175), (60 + i * 60, 175), lebar=4) for i in range(5)) + skuter(150, 200, .8) + mobil(60, 150, 70)
A['C21-T4a'] = rambu_kec('100')
A['C21-T4b'] = rambu_kec('120')
A['C21-T4c'] = rambu_kec('80')
A['C21-T6a'] = lantai() + ''.join(skuter(60 + i * 90, 200 - (i % 2) * 40, .7) for i in range(3)) + ''.join(garis((30 + i * 90, 150 - (i % 2) * 40), (10 + i * 90, 150 - (i % 2) * 40), lebar=3) for i in range(3))
A['C21-T6b'] = A['C21-L8a']
A['C21-T6c'] = lantai() + garis((16, 150), (284, 150), k='t') + ''.join(garis((30 + i * 60, 175), (60 + i * 60, 175), lebar=4) for i in range(5)) + pohon(260, 150, .6)
A['C21-T7'] = A['C21-3']
A['C21-T8'] = lantai() + papan_tulis(80, 30, 120, 70) + orang(170, tinggi=150, jenis='wanita', baju='a', wajah='senyum') + orang(250, tinggi=140, jenis='pria', baju='h', wajah='tawa') + gelembung(250, 30, 50, 30, teks(250, 38, '!', 18, angka=True), (-1, 1))

# --- C22 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def dok_visa(x, y, s=1.0):
    o = kotak(x - 60 * s, y - 80 * s, 120 * s, 160 * s, 'a', 6) + kotak(x - 46 * s, y - 64 * s, 40 * s, 50 * s, 'p', 3) + bulat(x - 26 * s, y - 46 * s, 10 * s, 'a')
    o += teks(x + 24 * s, y - 34 * s, 'VISA', 18 * s, angka=True) + ''.join(garis((x - 46 * s, y + (6 + i * 16) * s), (x + 46 * s, y + (6 + i * 16) * s), k='t') for i in range(4))
    return o + bulat(x + 30 * s, y + 56 * s, 16 * s, 'g')


def tiket_pesawat(x, y, s=1.0):
    return tiket(x, y, 200 * s, 90 * s) + pesawat(x - 10 * s, y + 4 * s, .3 * s)


A['C22-L4a'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a') + koper(180, 196, .8)
A['C22-L4b'] = lantai() + orang(60, tinggi=160, jenis='pria', baju='a') + koper(130, 196, 1.2) + koper(190, 196, 1.2) + koper(250, 196, 1.2)
A['C22-L4c'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', tangan={'ki': [(-20, 30), (-40, 40)], 'ka': [(20, 30), (40, 40)]})
A['C22-L5a'] = tiket_pesawat(150, 105, 1.1)
A['C22-L5b'] = dok_visa(150, 105)
A['C22-L5c'] = lantai() + koper(150, 196, 1.6)
A['C22-L6a'] = lantai() + pesawat(170, 80, .7) + jam_dinding(60, 60, 34, 6, 0)
A['C22-L6b'] = lantai() + dok_visa(200, 100, .7) + orang(80, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (60, 0)]})
A['C22-L6c'] = lantai() + orang(60, tinggi=150, jenis='wanita', baju='a') + koper(130, 196, 1.1) + koper(190, 196, 1.1) + koper(250, 196, 1.1) + koper(160, 128, .7)
A['C22-L8a'] = lantai() + koper(80, 196, 1.1) + koper(150, 196, 1.1) + koper(220, 196, 1.1)
A['C22-L8b'] = lantai() + koper(150, 196, 1.3) + kaos(110, 70, .5, 'a') + kaos(150, 50, .5, 'p') + buku(190, 70, 30, 10, 'a') + sepatu(140, 30, .5, 'a') + teks(240, 50, '!!', 22, angka=True)
A['C22-L8c'] = lantai() + koper(150, 196, 1.3) + kaos(150, 70, .5, 'a')
A['C22-L9'] = dok_visa(150, 105)
A['C22-L10'] = jam_dinding(80, 90, 50, 9, 0) + teks(80, 175, '臺灣', 18) + jam_dinding(220, 90, 50, 10, 0) + teks(220, 175, '日本', 18)
A['C22-T3a'] = lantai() + koper(110, 196, 1.1) + koper(190, 196, 1.1)
A['C22-T3b'] = A['C22-L8a']
A['C22-T3c'] = lantai() + koper(150, 196, 1.3)
A['C22-T4a'] = jam_dinding(150, 105, 80, 9, 0) + bulan_bintang(260, 30, .4)
A['C22-T4b'] = jam_dinding(150, 105, 80, 10, 0) + bulan_bintang(260, 30, .4)
A['C22-T4c'] = jam_dinding(150, 105, 80, 11, 0) + bulan_bintang(260, 30, .4)
A['C22-T6a'] = lantai() + pesawat(170, 70, .7) + kalender_senin(150, 130, 2, 2, 260)
A['C22-T6b'] = dok_visa(150, 105) + silang(150, 105, 60, 10)
A['C22-T6c'] = dok_visa(80, 105, .6) + kalender_senin(210, 40, 3, 2, 150)[:0] + teks(80, 190, '昨天', 18) + pesawat(220, 90, .45) + teks(220, 190, '明天', 18)
A['C22-T7'] = A['C22-1']
A['C22-T8'] = lantai() + toko(150, 200, 230, 150) + ''.join(meja(80 + i * 70, 196, 40)[:0] for i in range(3)) + ''.join(kotak(60 + i * 70, 160, 40, 8, 'h') + garis((80 + i * 70, 168), (80 + i * 70, 196), lebar=4) for i in range(3))

# --- C23 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def hotel_c23(x, penuh, label=True):
    o = gedung(x, tingkat=5, lebar=110) + (kotak(x - 40, 14, 80, 26, 'a', 4) + teks(x, 34, 'HOTEL', 16, angka=True) if label else '')
    return o + (silang(x, 100, 30, 6) if penuh else '')


def kereta_dalam(berdiri):
    o = kotak(16, 16, 268, 188, 'p', 10) + kotak(30, 30, 240, 50, 'a', 6) + kotak(24, 140, 252, 18, 'a', 4)
    if berdiri:
        o += ''.join(orang(60 + i * 60, tinggi=150, jenis='pria' if i % 2 else 'wanita', baju='a', tangan={'ka': [(6, -30), (0, -60)]}) for i in range(4))
    else:
        o += ''.join(orang(60 + i * 60, kaki=150, tinggi=110, jenis='pria' if i % 2 else 'wanita', baju='a', duduk=140) for i in range(4)) + jam_kecil(250, 50, 3, 0, 18)
    return o


A['C23-L4a'] = lantai() + hotel_c23(80, True) + panah(140, 120, 180, 120, 4) + hotel_c23(230, False) + jalan_kaki(160, 'pria', 110, 'a')[:0]
A['C23-L4b'] = lantai() + hotel_c23(150, False) + orang(240, tinggi=150, jenis='pria', baju='a')
A['C23-L4c'] = lantai() + rumah(150, 200, 140, 100) + jalan_kaki(250, 'pria', 150, 'a')
A['C23-L5a'] = lantai() + jendela(60, 40, 60, 50) + awan(90, 50, .3, 'a') + sofa(170) + orang(170, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C23-L5b'] = lantai() + gunung(170, 200, 260, 170, False) + awan(150, 16, 1.0, 'a') + hujan(150, 26, 260, 40) + payung(150, 60, 30) + orang(150, kaki=120, tinggi=80, jenis='wanita', baju='a')
A['C23-L5c'] = A['C17-L4c'].replace("bulat(110, 140, 13)", "bulat(110, 140, 13)") if 'C17-L4c' in A else lantai()
A['C23-L6a'] = kereta_dalam(False)
A['C23-L6b'] = kereta_dalam(True)
A['C23-L6c'] = lantai() + rumah(100, 200, 120, 90) + orang(220, tinggi=150, jenis='pria', baju='a', wajah='sedih') + silang(260, 40, 16, 5)
A['C23-L8a'] = lantai() + pesawat(150, 90, .9)
A['C23-L8b'] = lantai() + kereta(150, 196, 260)
A['C23-L8c'] = A['C23-1']
A['C23-L9'] = lantai() + hotel_c23(150, True)
A['C23-L10'] = lantai() + jendela(40, 30, 70, 56) + hujan(75, 34, 60, 50) + sofa(170) + tv(270, 150, 40) + orang(170, tinggi=140, jenis='pria', baju='a', duduk=150, wajah='sedih')
A['C23-T3a'] = lantai() + toko(150, 200, 200, 120) + ''.join(orang(80 + i * 46, kaki=196, tinggi=90, jenis='pria' if i % 2 else 'wanita', baju='a') for i in range(4)) + silang(250, 40, 16, 5)
A['C23-T3b'] = lantai() + rumah(100, 200, 120, 90) + meja(220, 150, 100) + piring(220, 144, 40, '')
A['C23-T3c'] = lantai() + toko(80, 200, 120, 110) + silang(80, 40, 14, 4) + panah(150, 120, 190, 120, 4) + toko(240, 200, 100, 100) + jalan_kaki(170, 'wanita', 100, 'a')[:0]
A['C23-T4a'] = lantai() + sofa(150) + orang(150, tinggi=150, jenis='pria', baju='a', duduk=150) + teks(200, 60, 'Z z', 18, angka=True)
A['C23-T4b'] = A['C17-L4c'] if 'C17-L4c' in A else lantai()
A['C23-T4c'] = lantai() + gunung(170, 200, 260, 170, False) + orang(140, kaki=120, tinggi=90, jenis='pria', baju='a')
A['C23-T6a'] = lantai() + kotak(60, 40, 180, 110, 'a', 6) + kapal(150, 120, .6) + silang(150, 95, 50, 8)
A['C23-T6b'] = lantai() + kotak(60, 40, 180, 110, 'a', 6) + kapal(150, 120, .6) + tiket(150, 175, 100, 40)
A['C23-T6c'] = A['C23-4']
A['C23-T7'] = A['C23-5']
A['C23-T8'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='lelah', kaki_pose={'ki': (-14, 0), 'ka': (20, -20)}, tangan={'ka': [(16, 10), (30, -10)], 'ki': [(16, 30), (-6, 40)]}) + keringat(124, 50) + keringat(176, 56)

# --- C24 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def pantai_c24(orang_x=None):
    o = kotak(16, 90, 268, 70, 'a') + ''.join(jalur(f'M{x} 120 q10 -8 20 0 t20 0', 'g', 3) for x in (40, 140, 220)) + matahari(240, 40, 18) + lantai()
    return o + (orang(orang_x, tinggi=120, jenis='pria', baju='a', wajah='tawa') if orang_x else '')


def termo_besar(t):
    return termometer(150, 20, t, 40, 150) + teks(220, 110, f'{t}°', 36, angka=True)


A['C24-L4a'] = lantai() + jendela(30, 30, 70, 56) + hujan(65, 34, 60, 50) + sofa(160) + tv(270, 150, 40) + orang(140, tinggi=140, jenis='pria', baju='a', duduk=150) + orang(190, tinggi=135, jenis='wanita', baju='h', duduk=150)
A['C24-L4b'] = A['C24-3']
A['C24-L4c'] = pantai_c24(110)
A['C24-L5a'] = termo_besar(35)
A['C24-L5b'] = termo_besar(20)
A['C24-L5c'] = termo_besar(5)
A['C24-L6a'] = lantai() + matahari(240, 50, 24) + orang(120, tinggi=150, jenis='wanita', baju='a', wajah='lelah') + keringat(94, 70)
A['C24-L6b'] = lantai() + ''.join(salju(x, y) for x, y in ((40, 40), (100, 70), (170, 40), (250, 60), (60, 120), (220, 120))) + orang(150, tinggi=150, jenis='wanita', baju='h')
A['C24-L6c'] = kalender_bulan(150, 30, 3, '', 160, 150)
A['C24-L8a'] = pantai_c24(120)
A['C24-L8b'] = A['C24-L4a']
A['C24-L8c'] = topan() + orang(150, tinggi=150, jenis='pria', baju='a', wajah='takut', tangan={'ka': [(20, -10), (30, -30)]})
A['C24-L9'] = A['C24-5']
A['C24-L10'] = termo_besar(20)
A['C24-T3a'] = lantai() + awan(150, 30, 1.2, 'a') + hujan(150, 40, 260, 60) + rumah(150, 200, 100, 60)
A['C24-T3b'] = A['C24-1']
A['C24-T3c'] = lantai() + awan(110, 40, .8, 'p') + matahari(220, 50, 16) + rumah(150, 200, 100, 60)
A['C24-T4a'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '20 min', 40, angka=True)
A['C24-T4b'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '10 min', 40, angka=True)
A['C24-T4c'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '30 min', 40, angka=True)
A['C24-T6a'] = lantai() + matahari(250, 40, 16) + sekolah(150, 200, 150, 100) + jalan_kaki(260, 'laki', 100, 'h')
A['C24-T6b'] = dua_panel(topan().replace(lantai(), ''), sekolah(225, 200, 120, 90) + jalan_kaki(270, 'laki', 90, 'h')) + lantai()
A['C24-T6c'] = dua_panel(topan().replace(lantai(), ''), sekolah(225, 200, 120, 90) + silang(225, 130, 30, 6)) + lantai()
A['C24-T7'] = lantai() + pohon(80, s=.9) + bunga(150, 196) + bunga(180, 190) + bunga(210, 196) + matahari(250, 40, 14) + orang(240, tinggi=140, jenis='wanita', baju='a', wajah='puas')
A['C24-T8'] = kotak(40, 20, 220, 180, 'a', 6) + teks(150, 50, 'N', 22, angka=True) + panah(150, 170, 150, 70, 5) + jalur('M150 170 m-24 0 a24 10 0 1 1 48 0 a16 7 0 1 1 -32 0', 'g', 3)

# --- C25 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def buket_c25(x, y, s=1.0):
    o = bentuk((x - 26 * s, y), (x + 26 * s, y), (x + 8 * s, y + 70 * s), (x - 8 * s, y + 70 * s), k='a')
    return o + ''.join(bulat(x + dx * s, y + dy * s, 14 * s, 'p') + bulat(x + dx * s, y + dy * s, 5 * s, 'h') for dx, dy in ((-18, -10), (0, -22), (18, -10), (0, 0)))


def bertemu(tempat):
    return lantai() + tempat + orang(60, tinggi=150, jenis='wanita', baju='a', tangan=LAMBAI) + orang(110, tinggi=160, jenis='pria', baju='h', wajah='tawa')


A['C25-L4a'] = bertemu(bioskop(220))
A['C25-L4b'] = bertemu(stasiun(220, 200, 130, 90) + kotak(180, 20, 80, 30, 'a', 4) + teks(220, 42, '車站', 18))
A['C25-L4c'] = bertemu(sekolah(220, 200, 130, 90) + kotak(180, 20, 80, 30, 'a', 4) + teks(220, 42, '學校', 18))
A['C25-L5a'] = lantai() + buket_c25(150, 80, 1.6)
A['C25-L5b'] = lantai() + kue_c10(150, 196, 1.3)
A['C25-L5c'] = lantai() + buku_tumpuk(150, 196, 3, 90, 22)
A['C25-L6a'] = lantai() + meja(150, 150, 220) + orang(70, tinggi=140, jenis='wanita', baju='a', duduk=150, tangan={'ka': [(20, 0), (60, -4)]}) + uang_kertas(150, 110, '$', 50, 24) + orang(230, tinggi=140, jenis='pria', baju='h', duduk=150)
A['C25-L6b'] = lantai() + meja(150, 150, 220) + orang(70, tinggi=140, jenis='wanita', baju='a', duduk=150, tangan={'ka': [(20, 0), (40, -4)]}) + orang(230, tinggi=140, jenis='pria', baju='h', duduk=150, tangan={'ki': [(20, 0), (40, -4)]}) + uang_kertas(110, 110, '$', 40, 20) + uang_kertas(190, 110, '$', 40, 20)
A['C25-L6c'] = lantai() + meja(150, 150, 220) + orang(70, tinggi=140, jenis='wanita', baju='a', duduk=150) + orang(230, tinggi=140, jenis='pria', baju='h', duduk=150, tangan={'ki': [(20, 0), (60, -4)]}) + uang_kertas(150, 110, '$', 50, 24)
A['C25-L8a'] = lantai() + sofa(150) + tv(260, 150, 50) + orang(150, tinggi=140, jenis='pria', baju='a', duduk=150, wajah='lelah')
A['C25-L8b'] = lantai() + meja(150, 150, 220) + piring(110, 144, 40, '') + piring(190, 144, 40, '') + orang(60, tinggi=140, jenis='pria', baju='a', duduk=150) + orang(240, tinggi=135, jenis='wanita', baju='h', duduk=150)
A['C25-L8c'] = lantai() + bioskop(220) + orang(70, tinggi=160, jenis='pria', baju='a', wajah='tawa') + orang(120, tinggi=150, jenis='wanita', baju='h', wajah='tawa') + bentuk((95, 30), (101, 42), (114, 42), (104, 50), (108, 64), (95, 56), (82, 64), (86, 50), (76, 42), (89, 42), k='h')
A['C25-L9'] = lantai() + kado(150, 196, 1.4)
A['C25-L10'] = lantai() + awan(80, 20, .8, 'a') + hujan(80, 30, 120, 30) + pintu(250, 200, 140, 60) + payung(160, 80, 30) + orang(120, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 0), (40, -10)]})
A['C25-T3a'] = lantai() + kue_c10(150, 196, 1.3)
A['C25-T3b'] = lantai() + buket_c25(150, 80, 1.6)
A['C25-T3c'] = lantai() + anggur(150, 110, 1.6)
A['C25-T4a'] = kalender_senin(150, 60, 4, 4) + bulan_bintang(250, 30, .4)
A['C25-T4b'] = kalender_senin(150, 60, 6, 6)
A['C25-T4c'] = kalender_senin(150, 60, 5, 5)
A['C25-T6a'] = lantai() + kotak(20, 60, 100, 140, 'p') + papan_keluar(70, 70, '', 0, 90, 40) + orang(170, tinggi=150, jenis='wanita', baju='a', tangan=LAMBAI) + orang(230, tinggi=160, jenis='pria', baju='h', wajah='tawa')
A['C25-T6b'] = A['C25-L4c']
A['C25-T6c'] = lantai() + toko(220, 200, 130, 100) + teks(220, 70, '餐廳', 16) + orang(60, tinggi=150, jenis='wanita', baju='a', tangan=LAMBAI) + orang(110, tinggi=160, jenis='pria', baju='h', wajah='tawa')
A['C25-T7'] = A['C25-2']
A['C25-T8'] = A['C25-3']

# --- C26 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def piala_c26(x, y):
    return kertas(x, y, 70, 90, 0) + teks(x, y + 10, '100', 26, angka=True)


A['C26-L4a'] = A['C26-4']
A['C26-L4b'] = lantai() + rumah_sakit(220, 200, 120, 100) + orang(60, tinggi=160, jenis='wanita', baju='a', rambut='uban') + orang(115, tinggi=155, jenis='pria', baju='h')
A['C26-L4c'] = lantai() + gunung(170, 200, 260, 170, False) + orang(140, kaki=120, tinggi=90, jenis='pria', baju='a')
A['C26-L5a'] = lantai() + orang(100, tinggi=155, jenis='wanita', baju='a', wajah='tawa', tangan=LAMBAI) + piala_c26(210, 110)
A['C26-L5b'] = A['C26-5'] if False else lantai() + orang(90, tinggi=155, jenis='wanita', baju='a', wajah='tawa') + kado(150, 130, .6) + orang(220, tinggi=160, jenis='pria', baju='h', wajah='senyum', tangan={'ki': [(16, 10), (40, 10)]})
A['C26-L5c'] = lantai() + pesawat(190, 60, .7) + orang(80, tinggi=155, jenis='wanita', baju='a', wajah='tawa') + koper(140, 196, .8)
A['C26-L6a'] = lantai() + gunung(170, 200, 260, 170, False) + orang(140, kaki=120, tinggi=90, jenis='pria', baju='a', wajah='tawa', tangan=LAMBAI)
A['C26-L6b'] = lantai() + gunung(190, 200, 220, 150, False) + orang(90, tinggi=150, jenis='pria', rambut='uban', baju='p') + orang(140, tinggi=160, jenis='pria', baju='a')
A['C26-L6c'] = lantai() + gunung(190, 200, 220, 150, False) + orang(130, kaki=150, tinggi=90, jenis='pria', baju='a') + orang(50, tinggi=150, jenis='pria', rambut='uban', baju='p', tangan=LAMBAI)
A['C26-L8a'] = lantai() + meja(160, 140, 200) + kertas(170, 128, 70, 22) + orang(90, tinggi=110, jenis='laki', duduk=150, baju='a', tangan={'ka': [(22, 10), (60, 14)]})
A['C26-L8b'] = lantai() + sofa(150) + ponsel_c15(150, 100, .6) + orang(150, tinggi=110, jenis='laki', baju='h', duduk=150, wajah='tawa')
A['C26-L8c'] = lantai() + sofa(130) + tv(260, 150, 60) + orang(130, tinggi=110, jenis='laki', baju='h', duduk=150)
A['C26-L9'] = lantai() + sofa(150) + orang(120, tinggi=150, jenis='nenek', rambut='uban', baju='a', duduk=150, wajah='senyum') + orang(185, tinggi=110, jenis='gadis', baju='h', duduk=150, wajah='tawa')
A['C26-L10'] = lantai() + kado(160, 130, .6) + orang(90, tinggi=155, jenis='wanita', baju='a', wajah='tawa', tangan={'ka': [(20, 10), (50, 4)]})
A['C26-T3a'] = lantai() + rumah_sakit(220, 200, 120, 100) + orang(60, tinggi=150, jenis='wanita', baju='a') + orang(110, tinggi=160, jenis='pria', baju='h', wajah='sedih')
A['C26-T3b'] = lantai() + rumah_sakit(220, 200, 120, 100) + orang(60, tinggi=165, jenis='pria', baju='a') + orang(110, tinggi=160, jenis='pria', baju='h', wajah='sedih')
A['C26-T3c'] = lantai() + rumah_sakit(220, 200, 120, 100) + orang(60, tinggi=150, jenis='nenek', rambut='uban', baju='a') + orang(110, tinggi=160, jenis='pria', baju='h', wajah='sedih')
A['C26-T4a'] = kota_label('臺北')
A['C26-T4b'] = kota_label('臺中')
A['C26-T4c'] = kota_label('高雄')
A['C26-T6a'] = lantai() + pohon(240) + jalan_kaki(120, 'nenek', 150, 'a')
A['C26-T6b'] = kotak(16, 16, 268, 188, 'p') + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'a')
A['C26-T6c'] = lantai_kamar() + ranjang(120, 200, 170) + bulat(66, 132, 13) + muka(66, 132, 13, 'lelah') + orang(235, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 10), (40, 20)]})
A['C26-T7'] = A['C26-3']
A['C26-T8'] = lantai() + sofa(150) + orang(120, tinggi=150, jenis='wanita', baju='a', duduk=150, wajah='tawa') + orang(185, tinggi=140, jenis='wanita', baju='h', duduk=150, wajah='tawa') + gelembung(150, 30, 60, 30, teks(150, 38, '♪', 16, angka=True), (-1, 1))

# --- C27 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def layar_pesan(x=150, y=105, s=2.2):
    o = kotak(x - 26 * s, y - 44 * s, 52 * s, 88 * s, 'h', 8) + kotak(x - 21 * s, y - 36 * s, 42 * s, 70 * s, 'p', 3)
    return o + kotak(x - 16 * s, y - 28 * s, 30 * s, 12 * s, 'a', 4) + kotak(x - 12 * s, y - 10 * s, 28 * s, 12 * s, 'p', 4) + kotak(x - 16 * s, y + 8 * s, 30 * s, 12 * s, 'a', 4)


A['C27-L4a'] = layar_pesan()
A['C27-L4b'] = lantai() + papan_tulis(80, 30, 120, 70) + orang(200, tinggi=160, jenis='wanita', baju='a', tangan={'ki': [(10, -10), (30, -30)]})
A['C27-L4c'] = lantai() + tv(150, 196, 200)
A['C27-L5a'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='a', wajah='marah', tangan={'ka': [(20, -6), (40, -20)]}) + orang(210, tinggi=155, jenis='wanita', baju='h', wajah='marah', tangan={'ki': [(20, -6), (40, -20)]}) + teks(150, 40, '!!', 26, angka=True)
A['C27-L5b'] = lantai() + meja(150, 150, 220) + kertas(150, 120, 80, 40, 0) + orang(60, tinggi=140, jenis='wanita', baju='a', duduk=150, wajah='tawa', tangan={'ka': [(20, 10), (60, 4)]}) + orang(240, tinggi=140, jenis='pria', baju='h', duduk=150, wajah='tawa', tangan={'ki': [(20, 10), (60, 4)]})
A['C27-L5c'] = lantai() + orang(80, tinggi=160, jenis='pria', baju='a') + orang(220, tinggi=155, jenis='wanita', baju='h') + teks(150, 50, '?', 30, angka=True)
A['C27-L6a'] = A['C27-L5b']
A['C27-L6b'] = lantai() + meja(150, 150, 200) + kotak(110, 90, 80, 60, 'h', 4) + kotak(116, 96, 68, 48, 'a', 2) + kotak(130, 106, 40, 30, 'p', 3) + orang(240, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C27-L6c'] = lantai() + meja(150, 150, 200) + buku_tumpuk(120, 150, 3, 50, 12) + orang(220, tinggi=150, jenis='wanita', baju='a', duduk=150, wajah='lelah')
A['C27-L8a'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='puas') + headphone(110, sendi(110, 200, 160, 'pria')['cy'], sendi(110, 200, 160, 'pria')['r']) + meja(230, 150, 90) + ponsel_c15(230, 130, .4) + jalur('M250 110 l10 -10 M256 120 l14 -4 M210 110 l-10 -10', 'g', 3)
A['C27-L8b'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='senyum') + meja(230, 150, 90) + ponsel_c15(230, 130, .4)
A['C27-L8c'] = lantai() + orang_ponsel(150, 'pria', 160, baju='a')
A['C27-L9'] = lantai() + orang_ponsel(110, 'pria', 160, baju='a') + gelembung(220, 40, 90, 50, kotak(190, 30, 60, 10, 'a', 3) + kotak(190, 46, 40, 10, 'a', 3), (-1, 1))
A['C27-L10'] = lantai() + orang(100, tinggi=110, jenis='laki', baju='h', wajah='tawa', tangan=LAMBAI) + orang(210, tinggi=160, jenis='nenek', rambut='uban', baju='a', wajah='senyum') + gelembung(100, 40, 70, 34, teks(100, 48, '你好', 18), (1, 1))
A['C27-T3a'] = A['C27-L4a']
A['C27-T3b'] = A['C27-L4b']
A['C27-T3c'] = A['C27-L4c']
A['C27-T4a'] = lantai() + papan_tulis(70, 30, 100, 60) + orang(180, tinggi=160, jenis='wanita', baju='a', wajah='marah', tangan={'ki': [(20, -6), (40, -20)]})
A['C27-T4b'] = lantai() + papan_tulis(70, 30, 100, 60) + orang(180, tinggi=160, jenis='wanita', baju='a', wajah='tawa') + kertas(250, 110, 60, 70, 0) + teks(250, 120, 'A+', 20, angka=True)
A['C27-T4c'] = lantai() + papan_tulis(70, 30, 100, 60) + orang(180, tinggi=160, jenis='wanita', baju='a', wajah='sedih') + kertas(250, 110, 60, 70, 0) + silang(250, 110, 20, 5)
A['C27-T6a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='sedih')
A['C27-T6b'] = A['C27-5']
A['C27-T6c'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + teks(130, 110, 'Z z', 18, angka=True)
A['C27-T7'] = A['C27-L5b']
A['C27-T8'] = lantai() + orang(100, tinggi=140, jenis='pria', baju='a', wajah='tawa') + orang(210, tinggi=155, jenis='wanita', baju='h', wajah='marah') + gelembung(160, 26, 60, 30, teks(160, 34, '哈哈', 16), (-1, 1))

# --- C28 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def sakit_bagian(bagian, jenis='wanita'):
    o = lantai() + orang(150, tinggi=165, jenis=jenis, baju='a', wajah='sakit')
    titik = {'perut': (150, 130), 'kepala': (150, 50), 'kaki': (140, 186)}[bagian]
    return o + bulat(titik[0], titik[1], 26, 'g') + jalur(f'M{titik[0] + 30} {titik[1] - 20} l12 -10 M{titik[0] + 34} {titik[1]} l16 0 M{titik[0] + 30} {titik[1] + 20} l12 10', 'g', 3)


A['C28-L4a'] = lantai() + meja(200, 150, 120) + piring(200, 144, 50, '') + orang(90, tinggi=110, jenis='gadis', baju='a', wajah='tawa', tangan={'ka': [(20, 10), (40, 0)]}) + teks(200, 110, '0', 22, angka=True)
A['C28-L4b'] = lantai() + kue_c10(160, 200, 1.0) + garis_jatuh(170, 140) + orang(80, tinggi=150, jenis='pria', baju='a', wajah='sedih')
A['C28-L4c'] = lantai() + kotak(110, 40, 110, 160, 'p', 6) + garis((110, 100), (220, 100), lebar=3) + kue_c10(165, 160, .8)
A['C28-L5a'] = sakit_bagian('perut')
A['C28-L5b'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='sakit') + bulat(150, 50, 26, 'g') + tisu(196, 60, .9) + jalur('M150 62 q-3 8 0 12 q3 -4 0 -12', 'p')
A['C28-L5c'] = sakit_bagian('kaki')
A['C28-L6a'] = A['C28-2']
A['C28-L6b'] = A['C28-3']
A['C28-L6c'] = sakit_bagian('kepala', 'pria')
A['C28-L8a'] = lantai() + matahari(250, 40, 18) + pelari(140, 'pria') + keringat(110, 50) + keringat(160, 46)
A['C28-L8b'] = potret(150, 84, 44, 'pria', 'sakit', 'a') + teks(230, 80, '!', 30, angka=True) + jalur('M196 104 l24 -8 M198 116 l28 0', 'g', 4)
A['C28-L8c'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + teks(130, 110, 'Z z', 18, angka=True)
A['C28-L9'] = A['C28-2']
A['C28-L10'] = lantai() + meja(200, 150, 120) + piring(200, 144, 50, '') + orang(90, tinggi=110, jenis='laki', baju='a', wajah='tawa') + orang(250, tinggi=150, jenis='wanita', baju='h', wajah='marah')[:0]
A['C28-T3a'] = lantai() + orang(90, tinggi=110, jenis='laki', baju='a', wajah='tawa') + pil(170, 150, 1.2)
A['C28-T3b'] = lantai() + kotak(150, 130, 70, 70, 'a', 6) + pil(185, 110, 1.0) + panah(170, 60, 185, 100, 3) + orang(80, tinggi=150, jenis='pria', baju='a')
A['C28-T3c'] = lantai() + anjing(150, 198, 1.1) + pil(220, 180, 1.0)
A['C28-T4a'] = A['C28-2']
A['C28-T4b'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='sakit') + tisu(220, 120, 1.0) + teks(80, 60, 'khk', 16, angka=True)
A['C28-T4c'] = sakit_bagian('kaki', 'pria')
A['C28-T6a'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'sakit') + termometer(250, 40, 39, 42, 70)
A['C28-T6b'] = lantai() + meja(150, 150, 200) + buku_tumpuk(110, 150, 3, 50, 12) + orang(200, tinggi=110, jenis='laki', baju='a', duduk=150)
A['C28-T6c'] = lantai() + orang(130, tinggi=120, jenis='laki', baju='h', wajah='tawa', kaki_pose={'ki': (-14, 0), 'ka': (20, -20)}) + bola(200, 186, 14)
A['C28-T7'] = A['C28-1']
A['C28-T8'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'sakit') + orang(250, tinggi=160, jenis='pria', baju='p')

# --- C29 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def dosis(n):
    o = ''
    for i in range(3):
        x = 60 + i * 90
        o += kotak(x - 34, 60, 68, 90, 'p', 6) + (pil(x, 100, 1.0) if i < n else silang(x, 100, 16, 4))
    return o + teks(150, 190, f'× {n}', 26, angka=True)


A['C29-L4a'] = dosis(3)
A['C29-L4b'] = dosis(1)
A['C29-L4c'] = dosis(2)
A['C29-L5a'] = A['C29-5']
A['C29-L5b'] = lantai() + matahari(250, 40, 16) + orang(130, tinggi=160, jenis='wanita', baju='a', wajah='tawa', tangan={'ki': [(20, -20), (30, -50)], 'ka': [(20, -20), (30, -50)]})
A['C29-L5c'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + teks(130, 110, 'Z z', 18, angka=True)
A['C29-L6a'] = lantai() + papan_tulis(150, 20, 160, 70) + ''.join(murid_belakang(80 + i * 70, 200, 110) for i in range(3))
A['C29-L6b'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'sakit')
A['C29-L6c'] = lantai() + dokter2(220, 200, 160) + orang(90, tinggi=160, jenis='pria', baju='a')
A['C29-L8a'] = potret(150, 84, 44, 'pria', 'tawa', 'a')
A['C29-L8b'] = lantai() + meja(150, 150, 200) + piring(150, 144, 60, nasi_goreng(150, 140, .6) if False else '') + orang(60, tinggi=140, jenis='pria', baju='a', duduk=150)
A['C29-L8c'] = A['C29-5']
A['C29-L9'] = A['C29-3']
A['C29-L10'] = A['C29-L5b']
A['C29-T3a'] = jam_dinding(150, 105, 80, 9, 0)
A['C29-T3b'] = jam_dinding(150, 105, 80, 10, 0)
A['C29-T3c'] = jam_dinding(150, 105, 80, 8, 0)
A['C29-T4a'] = dosis(1)
A['C29-T4b'] = dosis(2)
A['C29-T4c'] = dosis(3)
A['C29-T6a'] = pil(70, 110, 1.2) + panah(126, 110, 176, 110, 5) + piring(230, 110, 50)
A['C29-T6b'] = A['C29-2']
A['C29-T6c'] = pil(70, 110, 1.2) + panah(126, 110, 176, 110, 5) + ranjang(230, 170, 100) + bulan_bintang(240, 40, .4)
A['C29-T7'] = A['C29-5']
A['C29-T8'] = termometer(120, 20, 36, 42, 160) + teks(210, 110, '36.5°', 34, angka=True)

# --- C30 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def tinggi_badan(cm):
    o = lantai() + kotak(40, 20, 30, 180, 'p') + ''.join(garis((40, 200 - i * 18), (52, 200 - i * 18), lebar=2) for i in range(10))
    t = 100 + (cm - 160) * 3
    return o + orang(140, tinggi=t, jenis='pria', baju='a') + garis((60, 200 - t), (200, 200 - t), k='t') + teks(240, 200 - t + 8, f'{cm}', 26, angka=True)


A['C30-L4a'] = tinggi_badan(175)
A['C30-L4b'] = tinggi_badan(180)
A['C30-L4c'] = tinggi_badan(170)
A['C30-L5a'] = lantai() + jendela(230, 30, 60, 46) + matahari(254, 52, 10) + sofa(140) + orang(140, tinggi=150, jenis='wanita', baju='a', duduk=150, wajah='lelah') + konsol(140, 116, .5)
A['C30-L5b'] = lantai() + jendela(230, 30, 60, 46) + bulan_bintang(254, 52, .4) + jam_dinding(60, 50, 24, 2, 0) + meja(160, 150, 160) + buku(160, 140, 60, 12, 'a') + orang(250, tinggi=150, jenis='wanita', baju='a', duduk=150, wajah='lelah')
A['C30-L5c'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='nangis')
A['C30-L6a'] = lantai() + matahari(60, 120, 16) + garis((16, 140), (284, 140), k='t') + pelari(160, 'pria')
A['C30-L6b'] = lantai() + bulan_bintang(250, 36, .5) + pohon(40, s=.8) + bangku(200) + jalan_kaki(130, 'pria', 160, 'h')
A['C30-L6c'] = lantai() + sofa(150) + ponsel_c15(150, 100, .6) + orang(150, tinggi=150, jenis='pria', baju='h', duduk=150, wajah='lelah')
A['C30-L8a'] = lantai() + pohon(50, s=.8) + bangku(170) + orang(170, tinggi=150, jenis='nenek', rambut='uban', baju='a', duduk=170)
A['C30-L8b'] = lantai() + jendela(60, 40, 60, 50) + sofa(240, w=90) + orang(150, tinggi=150, jenis='nenek', rambut='uban', baju='a', tangan={'ki': [(20, -20), (40, -40)], 'ka': [(20, -20), (40, -40)]})
A['C30-L8c'] = lantai() + pohon(50, s=.8) + pohon(260, s=.7) + matahari(200, 30, 12) + orang(150, tinggi=150, jenis='nenek', rambut='uban', baju='a', tangan={'ki': [(20, -20), (40, -40)], 'ka': [(20, -20), (40, -40)]})
A['C30-L9'] = lantai() + orang(150, tinggi=180, jenis='pria', baju='a', wajah='lelah', tangan={'ki': [(10, 24), (22, 14)], 'ka': [(10, 24), (22, 14)]}) + ponsel_c15(150, 88, .6) + garis((140, 46), (146, 62), k='t') + garis((160, 46), (154, 62), k='t')
A['C30-L10'] = lantai() + orang(150, kaki=200, tinggi=140, jenis='pria', baju='a', wajah='lelah', duduk=196, tangan={'ki': [(20, 30), (40, 50)], 'ka': [(20, 30), (40, 50)]}) + keringat(124, 80) + keringat(176, 84) + garis((16, 150), (284, 150), k='t')
A['C30-T3a'] = tinggi_badan(170)
A['C30-T3b'] = tinggi_badan(180)
A['C30-T3c'] = tinggi_badan(175)
A['C30-T4a'] = lantai() + orang(150, tinggi=180, jenis='wanita', baju='a', wajah='lelah', tangan={'ki': [(10, 24), (22, 14)], 'ka': [(10, 24), (22, 14)]}) + ponsel_c15(150, 88, .6) + garis((140, 46), (146, 62), k='t') + garis((160, 46), (154, 62), k='t')
A['C30-T4b'] = lantai() + jendela(230, 30, 60, 46) + bulan_bintang(254, 52, .4) + meja(160, 150, 160) + buku(160, 140, 60, 12, 'a') + orang(250, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C30-T4c'] = lantai() + sofa(140) + tv(260, 150, 60) + orang(140, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C30-T6a'] = lantai() + sekolah(220, 200, 130, 90) + kotak(180, 20, 80, 30, 'a', 4) + teks(220, 42, '學校', 18) + orang(80, tinggi=110, jenis='laki', baju='h') + tas_punggung(64, 120, .5)
A['C30-T6b'] = lantai() + pintu(230, 200, 150, 70) + orang(120, tinggi=110, jenis='laki', baju='h', tangan={'ki': [(20, 30), (34, 40)], 'ka': [(20, 30), (34, 40)]}) + kardus(120, 160, 50, 34)
A['C30-T6c'] = lantai() + pintu(230, 200, 150, 70) + orang(130, tinggi=110, jenis='laki', baju='h') + tas_punggung(114, 120, .5)
A['C30-T7'] = lantai() + kotak(50, 60, 200, 130, 'p', 10) + jalur('M80 130 q40 -40 100 0 q-40 40 -100 0 z', 'a') + jalur('M180 130 l30 -20 l0 40 z', 'a') + silang(110, 122, 6, 3)
A['C30-T8'] = lantai() + orang(150, tinggi=180, jenis='pria', baju='a', wajah='lelah', tangan={'ki': [(10, 24), (22, 14)], 'ka': [(10, 24), (22, 14)]}) + ponsel_c15(150, 88, .6) + garis((140, 46), (146, 62), k='t') + garis((160, 46), (154, 62), k='t')

# --- C31 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kelas_jam(h, m, terlambat):
    o = lantai() + papan_tulis(70, 26, 100, 60) + jam_dinding(255, 40, 26, h, m) + kursi_depan(110, 150)
    return o + (jalan_kaki(205, 'pria', 150, 'a', 'kaget') + keringat(225, 70) if terlambat else orang(110, tinggi=150, jenis='pria', baju='a', duduk=150, wajah='senyum'))


def soal_tulis(n_isi, n=20):
    o = kotak(70, 14, 160, 190, 'p', 4)
    for i in range(10):
        for j in range(2):
            k = i + j * 10
            x = 84 + j * 76
            y = 30 + i * 17
            o += teks(x, y + 5, str(k + 1), 10, angka=True) + (jalur(f'M{x + 12} {y + 4} l8 -6 l8 6 l8 -6 l8 6 l8 -6', 'g', 3) if k < n_isi else '')
    return o


A['C31-L4a'] = kelas_jam(7, 50, False)
A['C31-L4b'] = kelas_jam(8, 10, True)
A['C31-L4c'] = kelas_jam(8, 0, False)
A['C31-L5a'] = soal_tulis(20)
A['C31-L5b'] = soal_tulis(10)
A['C31-L5c'] = soal_tulis(0)
A['C31-L6a'] = soal_tulis(20)
A['C31-L6b'] = soal_tulis(10)
A['C31-L6c'] = soal_tulis(15)
A['C31-L8a'] = A['C31-3'] if False else lantai() + papan_tulis(80, 26, 120, 64) + orang(70, tinggi=160, jenis='wanita', baju='a') + orang(220, tinggi=130, jenis='laki', baju='h', wajah='tawa', tangan=ANGKAT) + teks(260, 40, '!', 26, angka=True)
A['C31-L8b'] = lantai() + meja(170, 150, 160) + orang(170, tinggi=120, jenis='laki', baju='h', duduk=150) + teks(220, 90, 'Z z', 18, angka=True)
A['C31-L8c'] = lantai() + papan_tulis(80, 26, 120, 64) + orang(220, tinggi=130, jenis='laki', baju='h', wajah='lelah', tangan={'ka': [(10, 10), (0, -14)]}) + teks(250, 50, '...?', 18, angka=True)
A['C31-L9'] = A['C31-1']
A['C31-L10'] = kotak(70, 20, 160, 170, 'p', 6) + teks(150, 80, '答案: B', 26) + teks(150, 160, '✔', 56, angka=True)
A['C31-T3a'] = kelas_jam(7, 55, False)
A['C31-T3b'] = lantai() + papan_tulis(80, 26, 110, 60) + jam_dinding(220, 50, 30, 8, 10) + kursi_depan(110, 150) + teks(110, 120, '?', 30, angka=True)
A['C31-T3c'] = kelas_jam(8, 10, True)
A['C31-T4a'] = lantai() + orang(80, tinggi=150, jenis='wanita', baju='a', tangan=ANGKAT) + orang(200, tinggi=165, jenis='wanita', baju='h', kacamata=True)
A['C31-T4b'] = lantai() + meja(150, 150, 200) + kotak(120, 60, 60, 80, 'p', 4) + teks(150, 110, '4', 30, angka=True) + orang(60, tinggi=140, jenis='wanita', baju='a', duduk=150) + orang(240, tinggi=140, jenis='pria', baju='h', duduk=150)
A['C31-T4c'] = lantai() + rumah(200, 200, 120, 90) + jalan_kaki(90, 'wanita', 150, 'a')
A['C31-T6a'] = lantai() + jalan_kaki(150, 'pria', 160, 'a')
A['C31-T6b'] = lantai() + papan_tulis(70, 26, 100, 60) + kursi_depan(200, 150) + orang(200, tinggi=150, jenis='pria', baju='a', duduk=150, wajah='kaget') + orang(70, tinggi=160, jenis='wanita', baju='h', tangan={'ka': [(20, -6), (50, -12)]})
A['C31-T6c'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur')
A['C31-T7'] = A['C31-5']
A['C31-T8'] = A['C31-L8a']

# --- C32 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kal_tgl(bulan, tgl):
    return kotak(70, 30, 160, 160, 'p', 8) + kotak(70, 30, 160, 44, 'h', 8) + teks(150, 62, f'{bulan}月', 26, warna='#fff') + teks(150, 150, str(tgl), 64, angka=True)


A['C32-L4a'] = dua_panel(kotak(16, 120, 118, 80, 'a') + bulat(75, 140, 12) + muka(75, 140, 12, 'senyum') + jalur('M30 150 q10 -8 20 0 t20 0', 'g', 3), sofa(225, 200, 100) + orang(225, tinggi=130, jenis='pria', baju='a', duduk=160) + buku(225, 120, 40, 10, 'a')) + lantai()
A['C32-L4b'] = lantai() + gunung(150, 200, 280, 150, False) + ''.join(salju(x, y, 6) for x, y in ((40, 40), (240, 50), (100, 30))) + orang(150, kaki=120, tinggi=80, jenis='pria', baju='h') + garis((120, 124), (190, 116), lebar=4)
A['C32-L4c'] = kotak(16, 16, 268, 188, 'p') + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'a')
A['C32-L5a'] = pantai_c24(150)
A['C32-L5b'] = dua_panel(kotak(16, 16, 118, 188, 'p') + kasir(75, 200) + orang(110, tinggi=140, jenis='wanita', baju='h'), meja(225, 150, 110) + buku_tumpuk(200, 150, 3, 40, 10) + orang(255, tinggi=130, jenis='wanita', baju='a', duduk=150, wajah='lelah')) + lantai()
A['C32-L5c'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'sakit')
A['C32-L6a'] = A['C32-4']
A['C32-L6b'] = lantai() + koper(80, 196, 1.0) + kamera_c17(170, 80, .7) + gunung(240, 200, 120, 80, False)
A['C32-L6c'] = lantai() + kotak(110, 120, 164, 80, 'a') + mesin_kopi(250, 120) + orang(170, kaki=200, tinggi=145, jenis='wanita', baju='h')
A['C32-L8a'] = A['C32-1']
A['C32-L8b'] = A['C32-L5b']
A['C32-L8c'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + teks(130, 110, 'Z z', 18, angka=True)
A['C32-L9'] = A['C32-2']
A['C32-L10'] = A['C32-3']
A['C32-T3a'] = kal_tgl(7, 8)
A['C32-T3b'] = kal_tgl(6, 1)
A['C32-T3c'] = kal_tgl(7, 1)
A['C32-T4a'] = lantai() + gunung(170, 200, 260, 170, False) + orang(140, kaki=120, tinggi=90, jenis='wanita', baju='a')
A['C32-T4b'] = lantai() + bioskop(200) + orang(80, tinggi=150, jenis='wanita', baju='a')
A['C32-T4c'] = lantai() + meja(150, 150, 200) + buku_tumpuk(110, 150, 3, 50, 12) + orang(200, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C32-T6a'] = A['C32-L4b']
A['C32-T6b'] = A['C32-L4a']
A['C32-T6c'] = lantai() + sekolah(200, 200, 140, 100) + kotak(160, 20, 80, 30, 'a', 4) + teks(200, 42, '學校', 18) + orang(80, tinggi=150, jenis='pria', baju='a') + tas_punggung(64, 100, .5)
A['C32-T7'] = A['C32-4']
A['C32-T8'] = kalender_senin(150, 30, 2, 3) + bunga(100, 180) + bunga(150, 186) + bunga(200, 180) + lantai()

# --- C33 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def juara(posisi):
    """posisi = peringkat (1, 2, 3)."""
    p, pos = podium(150)
    o = lantai() + p
    x, k = pos[posisi]
    return o + orang(x, kaki=k, tinggi=100, jenis='pria', baju='a', wajah='puas', tangan=ANGKAT) + bulat(x, k - 50, 8, 'a')


A['C33-L4a'] = juara(1)
A['C33-L4b'] = juara(2)
A['C33-L4c'] = juara(3)
A['C33-L5a'] = lantai() + meja(150, 150, 220) + piring(110, 144, 40, '') + orang(60, tinggi=140, jenis='pria', baju='a', duduk=150, kacamata=True) + orang(240, tinggi=135, jenis='wanita', baju='h', duduk=150)
A['C33-L5b'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', kacamata=True, tangan={'ka': [(20, 0), (40, -6)]}) + orang(200, tinggi=150, jenis='wanita', baju='h') + orang(250, tinggi=155, jenis='pria', baju='p') + gelembung(140, 30, 60, 30, teks(140, 38, '…', 18, angka=True), (-1, 1))
A['C33-L5c'] = A['C33-3']
A['C33-L6a'] = kalender_bulan(80, 40, 11, '', 110, 110) + teks(80, 175, '這個月', 18) + panah(140, 95, 160, 95, 4) + kalender_bulan(220, 40, 12, '', 110, 110) + bulat(220, 110, 40, 'g')
A['C33-L6b'] = kalender_tahun(95, 50, 2026) + teks(95, 146, '今年', 20) + kalender_tahun(205, 50, 2027, True)
A['C33-L6c'] = kalender_senin(150, 60, 2, 3)
A['C33-L8a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='lelah') + silang(220, 60, 20, 6) + garis((60, 190), (110, 190), lebar=4)
A['C33-L8b'] = lantai() + matahari(60, 40, 14) + kalender_senin(220, 14, 2, 3, 140) + pelari(130, 'pria')
A['C33-L8c'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + teks(130, 110, 'Z z', 18, angka=True)
A['C33-L9'] = A['C33-1']
A['C33-L10'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='tawa', tangan=ANGKAT) + piala(186, 60, .8)
A['C33-T3a'] = lantai() + sofa(150) + tv(260, 150, 50) + orang(150, tinggi=150, jenis='pria', baju='a', duduk=150) + silang(60, 60, 20, 6)
A['C33-T3b'] = kalender_bulan(80, 40, 6, '', 110, 110) + meja(220, 150, 110) + buku(220, 140, 60, 12, 'a') + orang(220, tinggi=140, jenis='pria', baju='a', duduk=150)[:0] + teks(80, 175, '✔✔✔', 18, angka=True)
A['C33-T3c'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur')
A['C33-T4a'] = lantai() + dokter2(150, 200, 160)
A['C33-T4b'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 16), (44, 20)]}) + tas_kerja(100, 196, .7) + uang_kertas(230, 60, '$', 60, 30)
A['C33-T4c'] = lantai() + sekolah(200, 200, 140, 100) + kotak(160, 20, 80, 30, 'a', 4) + teks(200, 42, '國小', 18) + orang(70, tinggi=110, jenis='laki', baju='h') + orang(110, tinggi=100, jenis='gadis', baju='a')
A['C33-T6a'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='sedih')
A['C33-T6b'] = A['C33-L10']
A['C33-T6c'] = lantai() + meja(150, 150, 200) + buku_tumpuk(110, 150, 3, 50, 12) + orang(200, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C33-T7'] = lantai() + papan_tulis(80, 26, 120, 64) + orang(200, tinggi=165, jenis='pria', baju='a', kacamata=True, tangan={'ki': [(10, -10), (34, -40)]}) + ''.join(murid_belakang(60 + i * 60, 200, 80) for i in range(2))
A['C33-T8'] = lantai() + meja(150, 150, 200) + buku(150, 140, 70, 16, 'a') + panah(150, 70, 150, 120, 4)

# --- C34 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def lembar_hanzi(x, y, n=10):
    o = kotak(x - 70, y - 50, 140, 100, 'p', 3)
    for i in range(n):
        o += teks(x - 56 + (i % 5) * 28, y - 16 + (i // 5) * 36, '字', 18)
    return o


A['C34-L4a'] = lantai() + meja(170, 150, 200) + lembar_hanzi(190, 110) + orang(70, tinggi=150, jenis='pria', baju='a', duduk=150, tangan={'ka': [(22, 0), (60, -10)]})
A['C34-L4b'] = A['C34-4']
A['C34-L4c'] = A['C34-1']
A['C34-L5a'] = lantai() + meja(170, 150, 200) + lembar_hanzi(190, 110, 6) + orang(70, tinggi=150, jenis='wanita', baju='a', duduk=150, tangan={'ka': [(22, 0), (60, -10)]}) + orang(260, tinggi=150, jenis='pria', baju='h')
A['C34-L5b'] = lantai() + meja(150, 150, 200) + cangkir(120, 146, .8) + cangkir(180, 146, .8) + orang(50, tinggi=140, jenis='wanita', baju='a', duduk=150, wajah='tawa') + orang(250, tinggi=145, jenis='pria', baju='h', duduk=150, wajah='tawa')
A['C34-L5c'] = lantai() + papan_tulis(150, 20, 140, 70) + jalan_kaki(80, 'wanita', 150, 'a') + jalan_kaki(130, 'pria', 160, 'h')
A['C34-L6a'] = lembar_hanzi(150, 105, 1) + teks(150, 190, '× 1', 24, angka=True)
A['C34-L6b'] = lembar_hanzi(150, 105, 10) + teks(150, 190, '× 10', 24, angka=True)
A['C34-L6c'] = kotak(40, 20, 220, 150, 'p', 3) + ''.join(teks(58 + (i % 10) * 20, 50 + (i // 10) * 40, '字', 14) for i in range(20)) + teks(150, 196, '× 20', 24, angka=True)
A['C34-L8a'] = lantai() + sofa(150) + orang(150, tinggi=120, jenis='gadis', baju='a', duduk=150) + buku(150, 116, 40, 10, 'a')
A['C34-L8b'] = lantai() + meja(170, 150, 200) + lembar_hanzi(190, 110) + orang(70, tinggi=120, jenis='gadis', baju='a', duduk=150, tangan={'ka': [(22, 0), (60, -10)]})
A['C34-L8c'] = lantai() + garis((190, 200), (210, 70), lebar=4) + garis((250, 200), (210, 70), lebar=4) + kotak(170, 60, 80, 70, 'a', 2) + jalur('M180 110 q20 -30 40 0 t30 -10', 'g', 3) + orang(100, tinggi=120, jenis='gadis', baju='a', tangan={'ka': [(20, -4), (46, -10)]})
A['C34-L9'] = A['C34-3']
A['C34-L10'] = A['C34-5']
A['C34-T3a'] = lantai() + meja(170, 150, 200) + kertas(190, 126, 80, 24) + orang(70, tinggi=150, jenis='pria', baju='a', duduk=150, tangan={'ka': [(22, 0), (60, -10)]})
A['C34-T3b'] = A['C34-4']
A['C34-T3c'] = lantai() + orang(120, tinggi=160, jenis='pria', baju='a', wajah='nyanyi') + buku(170, 80, 50, 12, 'a') + gelembung(220, 40, 60, 30, teks(220, 48, '字', 16), (-1, 1))
A['C34-T4a'] = kalender_bulan(150, 30, 6, '', 160, 150)[:0] + kotak(40, 60, 220, 90, 'p', 8) + ''.join(kotak(48 + i * 30, 70, 26, 70, 'a' if i < 3 else 'p', 3) for i in range(7)) + teks(150, 190, '3 週', 24)
A['C34-T4b'] = kalender_tahun(150, 50, 2026, True)
A['C34-T4c'] = ''.join(kalender_bulan(60 + i * 90, 50, i + 1, '', 80, 80) for i in range(3)) + teks(150, 180, '3 個月', 24)
A['C34-T6a'] = lantai() + pelari(150, 'pria')
A['C34-T6b'] = lantai() + meja(170, 150, 200) + lembar_hanzi(190, 110) + orang(70, tinggi=150, jenis='pria', baju='a', duduk=150, wajah='lelah') + teks(140, 40, 'Z z', 18, angka=True)
A['C34-T6c'] = lantai() + meja(150, 150, 220) + piring(150, 144, 60, '') + orang(60, tinggi=140, jenis='pria', baju='a', duduk=150)
A['C34-T7'] = A['C34-1']
A['C34-T8'] = lantai() + orang_ponsel(100, 'wanita', 150, baju='a')[:0] + kotak(100, 40, 100, 150, 'h', 12) + kotak(108, 52, 84, 120, 'p', 4) + teks(150, 110, 'pīn yīn', 18, angka=True) + orang(240, tinggi=150, jenis='wanita', baju='a')

# --- C35 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def koreksi(x=150, jenis='wanita', baju='a'):
    return lantai() + meja(x + 30, 150, 180) + kertas(x + 40, 126, 70, 24) + jalur(f'M{x + 20} 122 l10 8 l10 -12', 'g', 3) + orang(x - 60, tinggi=150, jenis=jenis, baju=baju, duduk=150, tangan={'ka': [(22, 0), (60, -10)]})


A['C35-L4a'] = lantai() + papan_tulis(130, 26, 170, 90) + teks(110, 80, '例', 28, warna='#fff') + orang(250, tinggi=150, jenis='pria', baju='h', tangan={'ki': [(10, -10), (30, -40)]})
A['C35-L4b'] = koreksi(jenis='pria', baju='h')
A['C35-L4c'] = lantai() + pintu(230, 200, 150, 70) + jalan_kaki(140, 'pria', 150, 'h') + panah(170, 60, 210, 60, 4)
A['C35-L5a'] = lantai() + papan_tulis(130, 26, 170, 90) + teks(110, 80, '文', 28, warna='#fff') + orang(250, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(10, -10), (30, -40)]})
A['C35-L5b'] = koreksi()
A['C35-L5c'] = A['C35-3']
A['C35-L6a'] = lantai() + meja(160, 150, 200) + kertas(170, 126, 70, 24) + orang(70, tinggi=140, jenis='pria', baju='a', duduk=150, tangan={'ka': [(22, 0), (60, -10)]})
A['C35-L6b'] = A['C35-3']
A['C35-L6c'] = lantai() + orang(90, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + kertas(150, 90, 40, 50, 0) + orang(220, tinggi=165, jenis='wanita', baju='h', kacamata=True) + kalender_senin(150, 10, 0, 0, 120)[:0]
A['C35-L8a'] = koreksi(jenis='pria', baju='a')
A['C35-L8b'] = A['C35-5']
A['C35-L8c'] = lantai() + cangkir(190, 120, 1.0) + orang(130, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, 0), (46, -10)]})
A['C35-L9'] = koreksi()
A['C35-L10'] = A['C35-3']
A['C35-T3a'] = A['C35-L6a']
A['C35-T3b'] = A['C35-L4a']
A['C35-T3c'] = lantai() + kotak(150, 40, 130, 160, 'p') + kotak(170, 100, 90, 40, 'a', 3) + kertas(215, 90, 50, 30, 0) + teks(215, 60, '辦公室', 14) + jalan_kaki(90, 'wanita', 150, 'a')
A['C35-T4a'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(20, 24), (34, 30)], 'ka': [(20, 24), (34, 30)]}) + buku(150, 100, 60, 14, 'a')
A['C35-T4b'] = lantai() + papan_tulis(110, 26, 170, 90) + teks(90, 66, '老師叫我', 16, warna='#fff') + teks(90, 92, '寫作文', 16, warna='#fff') + orang(250, tinggi=150, jenis='wanita', baju='a')
A['C35-T4c'] = lantai() + orang_ponsel(150, 'wanita', 150, baju='a')
A['C35-T6a'] = lantai() + papan_tulis(150, 26, 200, 100)
A['C35-T6b'] = lantai() + papan_tulis(150, 26, 200, 100) + teks(150, 56, '例 1', 18, warna='#fff') + teks(150, 82, '例 2', 18, warna='#fff') + teks(150, 108, '例 3', 18, warna='#fff')
A['C35-T6c'] = lantai() + meja(150, 150, 200) + buku(150, 140, 70, 16, 'a')
A['C35-T7'] = A['C35-4']
A['C35-T8'] = koreksi(jenis='pria', baju='a')

# --- C36 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def bicara(teks_list, jenis='pria'):
    o = lantai() + orang(150, tinggi=165, jenis=jenis, baju='a', wajah='nyanyi')
    pos = [(70, 50), (232, 50)]
    for (x, y), t in zip(pos, teks_list):
        o += gelembung(x, y, 110, 50, teks(x, y + 7, t, 22 if len(t) < 4 else 15), (1 if x < 150 else -1, 1))
    return o


def tenda_c36(x=150):
    return lantai() + bentuk((x - 90, 200), (x, 70), (x + 90, 200), k='a') + bentuk((x - 20, 200), (x, 140), (x + 20, 200), k='h')


def keluarga_baju(merah_kecuali_adik=True, semua=False, hanya_adik=False):
    o = lantai()
    data = [(50, 165, 'pria'), (105, 155, 'wanita'), (160, 130, 'gadis'), (215, 105, 'laki')]
    for i, (x, t, j) in enumerate(data):
        adik = (i == 3)
        if semua: b = 'h'
        elif hanya_adik: b = 'h' if adik else 'p'
        else: b = 'p' if adik else 'h'
        o += orang(x, tinggi=t, jenis=j, baju=b)
    return o + kotak(250, 20, 30, 30, 'h', 3) + teks(265, 70, '紅', 18)


A['C36-L4a'] = bicara(['你好', 'こんにちは'])
A['C36-L4b'] = bicara(['你好'])
A['C36-L4c'] = bicara(['こんにちは'])
A['C36-L5a'] = lantai() + gunung(170, 200, 260, 170, False) + ''.join(orang(110 + i * 30, kaki=150 - i * 20, tinggi=70, jenis='pria' if i % 2 else 'wanita', baju='a') for i in range(4))
A['C36-L5b'] = lantai() + gunung(200, 200, 200, 150, False) + orang(60, tinggi=110, jenis='laki', baju='h', wajah='sedih') + kotak(30, 20, 60, 30, 'a', 4) + teks(60, 42, '小明', 16)
A['C36-L5c'] = lantai() + gunung(200, 200, 200, 150, False) + orang(60, tinggi=150, jenis='wanita', baju='a', wajah='sedih')
A['C36-L6a'] = majalah(150, 105, 1.2)
A['C36-L6b'] = lantai() + buku_tumpuk(150, 196, 1, 110, 30) + teks(150, 120, '小說', 24)
A['C36-L6c'] = lantai() + kotak(30, 20, 240, 110, 'h', 4) + kotak(40, 30, 220, 90, 'p', 2) + ''.join(potret(x, 196, 18, 'pria' if i % 2 else 'wanita', 'senyum', 'a') for i, x in enumerate((70, 130, 190, 250)))
A['C36-L8a'] = lantai() + rumah(150, 200, 160, 100) + jalur('M80 140 l20 10 M200 120 l20 -6 M110 170 l14 6', 'g', 3)
A['C36-L8b'] = A['C36-5']
A['C36-L8c'] = tenda_c36()
A['C36-L9'] = A['C36-4']
A['C36-L10'] = lantai() + ''.join(jalan_kaki(160 + i * 40, 'pria' if i % 2 else 'wanita', 150, 'a') for i in range(3)) + panah(150, 40, 280, 40, 4) + orang(60, tinggi=120, jenis='laki', baju='h', wajah='sedih')
A['C36-T3a'] = bicara(['Lí hó'])
A['C36-T3b'] = bicara(['Lí hó', 'こんにちは'])
A['C36-T3c'] = bicara(['こんにちは'])
A['C36-T4a'] = lantai() + gunung(170, 200, 260, 170, False) + orang(140, kaki=120, tinggi=90, jenis='wanita', baju='a')
A['C36-T4b'] = lantai() + sofa(150) + orang(150, tinggi=150, jenis='wanita', baju='a', duduk=150)
A['C36-T4c'] = lantai() + meja(150, 150, 220) + orang(60, tinggi=150, jenis='wanita', baju='a', duduk=150) + orang(150, tinggi=160, jenis='pria', baju='h', duduk=150) + orang(240, tinggi=155, jenis='pria', baju='h', duduk=150) + kotak(100, 20, 100, 30, 'a', 4) + teks(150, 42, '會', 18)
A['C36-T6a'] = keluarga_baju(semua=True)
A['C36-T6b'] = keluarga_baju(hanya_adik=True)
A['C36-T6c'] = keluarga_baju()
A['C36-T7'] = A['C36-2']
A['C36-T8'] = lantai() + orang(100, tinggi=165, jenis='pria', baju='h', wajah='senyum') + jaket_di(100, 165, 'pria') + orang(200, tinggi=155, jenis='wanita', baju='h') + kotak(150, 14, 100, 30, 'a', 4) + teks(200, 36, '會', 18)

# --- C37 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def nilai_c37(t):
    return kertas(150, 110, 150, 180, 0) + teks(150, 84, t, 48, angka=True) + bulat(150, 70, 56, 'g')


A['C37-L4a'] = lantai() + papan_isi('6 × 2 = 12', 42)
A['C37-L4b'] = lantai() + papan_isi('6 + 2 = 8', 44)
A['C37-L4c'] = lantai() + papan_isi('6 ÷ 2 = 3', 44)
A['C37-L5a'] = nilai_c37('89.5')
A['C37-L5b'] = nilai_c37('98.5')
A['C37-L5c'] = nilai_c37('95.8')
A['C37-L6a'] = uang_kertas(150, 105, '$60', 220, 100)
A['C37-L6b'] = uang_kertas(150, 105, '$20', 220, 100)
A['C37-L6c'] = uang_kertas(150, 105, '$40', 220, 100)
A['C37-L8a'] = lantai() + papan_isi('2 × 6 = 12', 42)
A['C37-L8b'] = lantai() + papan_isi('2 + 6 = 8', 44)
A['C37-L8c'] = lantai() + papan_isi('6 ÷ 2 = 3', 44)
A['C37-L9'] = lantai() + meja(150, 150, 240) + ''.join(buah_apel(70 + i * 40, 140, .55) for i in range(5))
A['C37-L10'] = lantai() + meja(160, 150, 200) + kertas(170, 126, 70, 24) + orang(70, tinggi=130, jenis='laki', baju='a', duduk=150, wajah='senyum', tangan={'ka': [(22, 0), (60, -10)]}) + teks(240, 60, '100', 26, angka=True)
A['C37-T3a'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '30 min', 40, angka=True)
A['C37-T3b'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '15 min', 40, angka=True)
A['C37-T3c'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '60 min', 40, angka=True)
A['C37-T4a'] = kotak(70, 40, 160, 130, 'p', 8) + teks(150, 130, '26', 60, angka=True)
A['C37-T4b'] = kotak(70, 40, 160, 130, 'p', 8) + teks(150, 130, '24', 60, angka=True)
A['C37-T4c'] = kotak(70, 40, 160, 130, 'p', 8) + teks(150, 130, '25', 60, angka=True)
A['C37-T6a'] = lantai() + sofa(150) + konsol(150, 116, .5) + orang(150, tinggi=140, jenis='pria', baju='a', duduk=150, wajah='tawa')
A['C37-T6b'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur') + teks(130, 110, 'Z z', 18, angka=True)
A['C37-T6c'] = lantai() + meja(160, 150, 200) + kertas(170, 126, 70, 24) + teks(170, 132, '1+2', 12, angka=True) + jam_dinding(250, 40, 22, 2, 0) + orang(70, tinggi=150, jenis='pria', baju='a', duduk=150, tangan={'ka': [(22, 0), (60, -10)]})
A['C37-T7'] = A['C37-5']
A['C37-T8'] = lantai() + papan_isi('20 ÷ 4 = 5', 42)

# --- C38 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kelas_pecahan(n_perempuan, n=6):
    o = lantai()
    for i in range(n):
        o += orang(40 + i * 44, tinggi=110, jenis='gadis' if i < n_perempuan else 'laki', baju='a' if i < n_perempuan else 'h')
    return o


A['C38-L4a'] = kelas_pecahan(4)
A['C38-L4b'] = kelas_pecahan(2)
A['C38-L4c'] = kelas_pecahan(3)
A['C38-L5a'] = lantai() + ranjang(150, 200, 180) + kotak(30, 20, 90, 40, 'a', 4) + teks(75, 48, '$1000', 18, angka=True)
A['C38-L5b'] = lantai() + ranjang(110, 200, 150) + meja(240, 150, 80) + piring(240, 144, 40, '') + cangkir(260, 146, .5) + kotak(30, 20, 90, 40, 'a', 4) + teks(75, 48, '$1000', 18, angka=True)
A['C38-L5c'] = lantai() + meja(150, 150, 140) + piring(140, 144, 50, '') + cangkir(180, 146, .6) + kotak(30, 20, 90, 40, 'a', 4) + teks(75, 48, '$1000', 18, angka=True)
A['C38-L6a'] = kotak(70, 40, 160, 130, 'p', 8) + teks(150, 130, '70', 60, angka=True)
A['C38-L6b'] = kotak(70, 40, 160, 130, 'p', 8) + teks(150, 130, '30', 60, angka=True)
A['C38-L6c'] = kotak(70, 40, 160, 130, 'p', 8) + teks(150, 130, '100', 60, angka=True)
A['C38-L8a'] = kelas_pecahan(4)
A['C38-L8b'] = kelas_pecahan(3)
A['C38-L8c'] = kelas_pecahan(2)
A['C38-L9'] = diagram(25)
A['C38-L10'] = lantai() + ''.join(orang(30 + i * 27, tinggi=100 + (i % 2) * 10, jenis='pria' if i % 2 else 'wanita', baju='a' if i != 4 else 'h', kacamata=(i == 4)) for i in range(10)) + teks(138, 30, '10', 22, angka=True)
A['C38-T3a'] = diagram(80)
A['C38-T3b'] = diagram(20)
A['C38-T3c'] = diagram(2)
A['C38-T4a'] = diagram(25)
A['C38-T4b'] = diagram(100 / 3)
A['C38-T4c'] = diagram(50)
A['C38-T6a'] = lantai() + bioskop(150)
A['C38-T6b'] = lantai() + bioskop(200) + orang(80, tinggi=150, jenis='wanita', baju='a')
A['C38-T6c'] = lantai() + bioskop(240) + ''.join(orang(30 + i * 34, tinggi=140 + (i % 2) * 10, jenis='pria' if i % 2 else 'wanita', baju='a' if i % 3 else 'h') for i in range(5))
A['C38-T7'] = diagram(75)
A['C38-T8'] = lantai() + ''.join(orang(40 + i * 44, tinggi=110, jenis='laki' if i % 2 else 'gadis', baju='a', tangan={'ka': [(14, 20), (26, 10)]}) + kotak(54 + i * 44, 80, 10, 16, 'h', 2) for i in range(6))

# --- C39 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def sewa_banding(t_tpe, t_jkt):
    return lantai() + gedung(80, tingkat=5, lebar=80) + kotak(40, 14, 80, 30, 'a', 4) + teks(80, 36, '臺北', 16) + uang_kertas(80, 190, t_tpe, 100, 30)[:0] + teks(80, 210, '', 1) + \
        rumah(220, 200, 100, 70) + kotak(180, 60, 80, 30, 'a', 4) + teks(220, 82, '雅加達', 14) + \
        kotak(30, 50, 100, 30, 'p', 4)[:0]


def dua_kantong(kiri, kanan):
    o = lantai() + kotak(30, 30, 110, 40, 'a', 4) + teks(85, 56, '臺北', 18) + kotak(160, 30, 110, 40, 'a', 4) + teks(215, 56, '雅加達', 16)
    for x, n in ((85, kiri), (215, kanan)):
        for i in range(n):
            o += uang_kertas(x, 180 - i * 22, '$', 80, 20)
    return o


A['C39-L4a'] = dua_kantong(4, 2)
A['C39-L4b'] = dua_kantong(2, 2)
A['C39-L4c'] = dua_kantong(1, 2)
A['C39-L5a'] = lantai() + pohon(260, s=.7) + orang(120, tinggi=165, jenis='pria', baju='a') + uang_kertas(190, 80, '$', 50, 24)
A['C39-L5b'] = lantai() + pohon(260, s=.7) + orang(120, tinggi=100, jenis='laki', baju='h', wajah='tawa') + teks(190, 80, '0', 30, angka=True) + teks(120, 40, '≤12', 20, angka=True)
A['C39-L5c'] = lantai() + pohon(260, s=.7) + orang(120, tinggi=150, jenis='nenek', rambut='uban', baju='a') + garis((144, 124), (150, 200), lebar=4) + teks(120, 30, '65+', 20, angka=True)
A['C39-L6a'] = uang_kertas(150, 105, '±4000', 220, 100)
A['C39-L6b'] = uang_kertas(150, 105, '±8000', 220, 100)
A['C39-L6c'] = uang_kertas(150, 105, '±16000', 230, 100)
A['C39-L8a'] = lantai() + meja(150, 150, 240) + kue_c10(100, 146, .8) + kue_c10(200, 146, .8) + teks(100, 70, '$100', 18, angka=True) + teks(200, 70, '$100', 18, angka=True)
A['C39-L8b'] = lantai() + meja(150, 150, 240) + kue_c10(100, 146, .6) + kue_c10(200, 146, .8) + teks(100, 70, '$50', 18, angka=True) + teks(200, 70, '$100', 18, angka=True)
A['C39-L8c'] = lantai() + meja(150, 150, 240) + kue_c10(100, 146, 1.1) + kue_c10(200, 146, .8) + teks(100, 50, '$200', 18, angka=True) + teks(200, 70, '$100', 18, angka=True)
A['C39-L9'] = termometer(150, 30, 35, 40, 140) + teks(215, 110, '35°', 30, angka=True) + matahari(60, 50, 20)
A['C39-L10'] = A['C39-5']
A['C39-T3a'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '5 min', 40, angka=True)
A['C39-T3b'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '±20 min', 36, angka=True)
A['C39-T3c'] = kotak(40, 60, 220, 90, 'h', 12) + kotak(52, 72, 196, 66, 'a', 6) + teks(150, 120, '2 h', 40, angka=True)
A['C39-T4a'] = lantai() + toko(150, 200, 200, 120) + teks(150, 50, '$500+', 22, angka=True)
A['C39-T4b'] = lantai() + toko(150, 200, 200, 120) + teks(150, 50, '$1000', 22, angka=True)
A['C39-T4c'] = lantai() + toko(150, 200, 200, 120) + teks(150, 50, '±$200', 22, angka=True)
A['C39-T6a'] = lantai() + bus(170, 200, 200) + orang(40, tinggi=100, jenis='laki', baju='h')
A['C39-T6b'] = lantai() + bus(170, 200, 200) + orang(40, tinggi=150, jenis='nenek', rambut='uban', baju='a') + teks(40, 30, '$0', 20, angka=True)
A['C39-T6c'] = lantai() + mobil(180, 200, 170, True) + orang(50, tinggi=150, jenis='nenek', rambut='uban', baju='a')
A['C39-T7'] = kotak(16, 16, 268, 188, 'h', 4) + kotak(24, 24, 252, 172, 'p') + ''.join(orang(40 + (i % 8) * 31, kaki=100 + (i // 8) * 90, tinggi=60, jenis='laki' if i % 2 else 'gadis', baju='a') for i in range(16)) + teks(150, 214, '', 1)
A['C39-T8'] = lantai() + bus(190, 200, 180) + orang(60, tinggi=100, jenis='laki', baju='h', wajah='tawa') + teks(60, 40, '≤12', 22, angka=True)

# --- C40 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def coba_baju(ukuran):
    """ukuran: 'besar' (kebesaran), 'kecil' (kekecilan), 'pas'."""
    o = lantai() + orang(150, tinggi=165, jenis='pria', baju='a')
    if ukuran == 'besar':
        o += bentuk((96, 56), (204, 56), (214, 150), (86, 150), k='a') + jalur('M90 150 l-10 20 M210 150 l10 20', 'g', 3)
    elif ukuran == 'kecil':
        o += bentuk((126, 56), (174, 56), (172, 100), (128, 100), k='a') + jalur('M120 70 l-10 -4 M180 70 l10 -4', 'g', 3)
    else:
        o += centang(230, 50, 1.0)
    return o


def label_diskon(t):
    return kotak(70, 50, 160, 110, 'p', 10) + bulat(96, 76, 8, 'a') + teks(160, 125, t, 40)


A['C40-L4a'] = coba_baju('besar')
A['C40-L4b'] = coba_baju('kecil')
A['C40-L4c'] = coba_baju('pas')
A['C40-L5a'] = lantai() + gedung(150, tingkat=4, lebar=200, tt=30) + kotak(90, 14, 120, 30, 'a', 4) + teks(150, 36, '百貨公司', 16)
A['C40-L5b'] = A['C40-4']
A['C40-L5c'] = lantai() + rumah(150, 200, 160, 110)
A['C40-L6a'] = lantai() + toko(80, 200, 120, 100) + panah(150, 120, 190, 120, 4) + toko(240, 200, 100, 100) + jalan_kaki(160, 'wanita', 110, 'a')[:0]
A['C40-L6b'] = A['C40-1']
A['C40-L6c'] = lantai() + rumah(200, 200, 120, 90) + jalan_kaki(90, 'wanita', 150, 'a') + jalan_kaki(130, 'pria', 160, 'h')
A['C40-L8a'] = lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(150, 198, 1.2) + jalur('M54 150 l-14 -6 M52 170 l-16 0', 'g')
A['C40-L8b'] = lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(170, 198, 2.6) + teks(230, 100, '↔', 30, angka=True)
A['C40-L8c'] = lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(160, 198, 1.9) + centang(230, 60, 1.0)
A['C40-L9'] = A['C40-4']
A['C40-L10'] = label_diskon('50%')
A['C40-T3a'] = label_diskon('九折')
A['C40-T3b'] = label_diskon('七折')
A['C40-T3c'] = label_diskon('五折')
A['C40-T4a'] = A['C40-4']
A['C40-T4b'] = A['C40-L5a']
A['C40-T4c'] = A['C40-L5c']
A['C40-T6a'] = lantai() + toko(150, 200, 200, 120)
A['C40-T6b'] = A['C40-3']
A['C40-T6c'] = lantai() + toko(150, 200, 200, 120) + silang(150, 150, 30, 8)
A['C40-T7'] = coba_baju('besar')
A['C40-T8'] = lantai() + gedung(240, tingkat=4, lebar=90, tt=30) + jalan_kaki(80, 'wanita', 150, 'a') + jalan_kaki(130, 'wanita', 145, 'h') + kotak(150, 120, 26, 30, 'a', 3)

# --- C41 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kaus_kaki_c41(x, y, s=1.0, k='a'):
    return jalur(f'M{x - 14 * s} {y - 50 * s} h28 v44 l24 10 q10 6 4 18 h-56 z', k)


def piyama_c41(x, y, s=1.0):
    return sweter(x, y - 30 * s, .9 * s) + celana(x, y + 10 * s, .45 * s, 'a')


A['C41-L4a'] = lantai() + sarung_tangan(110, 120, 1.2, 'a') + sarung_tangan(190, 120, 1.2, 'h')
A['C41-L4b'] = lantai() + sweter(150, 110, 1.6)
A['C41-L4c'] = lantai() + kaus_kaki_c41(110, 170, 1.2, 'a') + kaus_kaki_c41(190, 170, 1.2, 'p')
A['C41-L5a'] = lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(170, 198, 2.6) + teks(230, 100, '↔', 30, angka=True)
A['C41-L5b'] = lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(160, 198, 1.9) + centang(230, 60, 1.0)
A['C41-L5c'] = lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(150, 198, 1.2) + jalur('M54 150 l-14 -6 M52 170 l-16 0', 'g')
A['C41-L6a'] = uang_kertas(150, 105, '$100', 220, 100)
A['C41-L6b'] = uang_kertas(150, 105, '$2100', 220, 100)
A['C41-L6c'] = uang_kertas(150, 105, '$2000', 220, 100)
A['C41-L8a'] = lantai() + orang(150, tinggi=120, jenis='gadis', baju='p', tangan={'ki': [(20, 20), (30, 0)], 'ka': [(20, 20), (30, 0)]}) + sarung_tangan(112, 104, .4, 'h') + sarung_tangan(188, 104, .4, 'h') + kotak(250, 20, 30, 30, 'h', 3) + teks(265, 70, '紅', 18)
A['C41-L8b'] = lantai() + orang(150, tinggi=120, jenis='gadis', baju='h', tangan={'ki': [(20, 20), (30, 0)], 'ka': [(20, 20), (30, 0)]}) + sarung_tangan(112, 104, .4, 'p') + sarung_tangan(188, 104, .4, 'p') + kotak(250, 20, 30, 30, 'h', 3) + teks(265, 70, '紅', 18)
A['C41-L8c'] = lantai() + matahari(250, 40, 16) + kaos(150, 110, 1.2, 'h') + kotak(250, 120, 30, 30, 'h', 3) + teks(265, 170, '紅', 18)
A['C41-L9'] = A['C41-3']
A['C41-L10'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='tawa') + bintang(220, 40, 10) + bintang(90, 50, 8)
A['C41-T3a'] = lantai() + kaos(150, 110, 1.4, 'a')
A['C41-T3b'] = lantai() + sweter(150, 110, 1.6)
A['C41-T3c'] = lantai() + sarung_tangan(110, 120, 1.2, 'a') + sarung_tangan(190, 120, 1.2, 'h')
A['C41-T4a'] = piyama_c41(100, 100) + uang_kertas(220, 60, '$800', 90, 40)
A['C41-T4b'] = piyama_c41(100, 100) + uang_kertas(220, 60, '$1200', 90, 40)
A['C41-T4c'] = piyama_c41(100, 100) + uang_kertas(220, 60, '$2000', 90, 40)
A['C41-T6a'] = lantai() + sarung_tangan(90, 90, 1.0, 'h') + sarung_tangan(150, 90, 1.0, 'h') + kaus_kaki_c41(110, 196, .9, 'h') + kaus_kaki_c41(190, 196, .9, 'h')
A['C41-T6b'] = lantai() + sarung_tangan(90, 90, 1.0, 'h') + sarung_tangan(150, 90, 1.0, 'h') + kaus_kaki_c41(110, 196, .9, 'p') + kaus_kaki_c41(190, 196, .9, 'p')
A['C41-T6c'] = lantai() + sarung_tangan(90, 90, 1.0, 'p') + sarung_tangan(150, 90, 1.0, 'p') + kaus_kaki_c41(110, 196, .9, 'h') + kaus_kaki_c41(190, 196, .9, 'h')
A['C41-T7'] = lantai() + sepatu(110, 190, 1.4, 'h') + sepatu(200, 190, 1.4, 'h')
A['C41-T8'] = lantai() + kaos(150, 110, 1.4, 'a') + bintang(80, 50, 10) + bintang(230, 60, 10) + teks(150, 196, '金', 20)

# --- C42 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def koin_banyak(x, y):
    return ''.join(koin(x + dx, y + dy, 13) for dx, dy in ((-30, 0), (0, -8), (30, 0), (-15, 18), (15, 18), (0, 30)))


A['C42-L4a'] = uang_kertas(150, 105, '1000', 220, 100)
A['C42-L4b'] = koin_banyak(150, 90)
A['C42-L4c'] = kartu_kredit(150, 105, 2.0)
A['C42-L5a'] = lantai() + kasir(200) + jalan_kaki(60, 'wanita', 150, 'a') + panah(110, 120, 30, 120, 4)
A['C42-L5b'] = lantai() + kasir(200) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (50, 10)]}) + koin(150, 110, 10) + teks(150, 70, '?', 26, angka=True)
A['C42-L5c'] = lantai() + kasir(210) + mesin_edc(180, 90, .7) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -10), (40, -20)]}) + kartu_kredit(136, 60, .55)
A['C42-L6a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='kaget', tangan={'ki': [(-20, 30), (-40, 40)], 'ka': [(20, 30), (40, 40)]}) + dompet(240, 80, .6) + silang(240, 80, 24, 6)
A['C42-L6b'] = lantai() + kasir(220) + mesin_edc(190, 90, .6) + silang(190, 80, 20, 5) + orang(80, tinggi=160, jenis='pria', baju='a', wajah='sedih') + uang_kertas(140, 60, '1000', 60, 30)
A['C42-L6c'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='sedih') + uang_kertas(200, 80, '$10', 60, 30) + label_harga(240, 150, '100', 80, 40)
A['C42-L8a'] = A['C42-L4a']
A['C42-L8b'] = A['C42-L4b']
A['C42-L8c'] = kotak(90, 60, 120, 90, 'p', 12) + kotak(98, 68, 104, 74, 'a', 8) + teks(150, 116, '0', 34, angka=True)
A['C42-L9'] = A['C42-1']
A['C42-L10'] = uang_kertas(100, 70, '100', 120, 60) + teks(220, 80, '=', 40, angka=True) + label_harga(220, 150, '100', 90, 40)
A['C42-T3a'] = lantai() + kasir(200) + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='tawa') + centang(150, 50, .8)
A['C42-T3b'] = A['C42-L5b']
A['C42-T3c'] = A['C42-L5a']
A['C42-T4a'] = kartu_kredit(150, 105, 2.0)
A['C42-T4b'] = koin_banyak(150, 90)
A['C42-T4c'] = kotak(110, 30, 80, 150, 'h', 12) + kotak(118, 42, 64, 120, 'p', 4)
A['C42-T6a'] = lantai() + kasir(200) + orang(200, tinggi=150, jenis='wanita', baju='h') + koin_banyak(110, 110)[:0] + koin(120, 120, 10) + koin(140, 124, 10)
A['C42-T6b'] = lantai() + kasir(200) + orang(200, tinggi=150, jenis='wanita', baju='h') + kardus(110, 130, 50, 34)
A['C42-T6c'] = lantai() + kasir(200) + orang(200, tinggi=150, jenis='wanita', baju='h', tangan={'ki': [(20, 0), (50, -6)]}) + mesin_edc(140, 90, .7) + kartu_kredit(150, 66, .5)
A['C42-T7'] = koin_banyak(150, 90)
A['C42-T8'] = A['C42-3']

# --- C43 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def pemilik_toko(jenis, tinggi=150, rambut=None, kacamata=False):
    kw = {'rambut': rambut} if rambut else {}
    if jenis == 'kakek':
        return lantai() + kios_buah(150, 200, 200) + orang(150, tinggi=150, jenis='nenek', rambut='pendek', rok=False, baju='h', kacamata=True, wajah='senyum')
    return lantai() + kios_buah(150, 200, 200) + orang(150, tinggi=tinggi, jenis=jenis, baju='h', wajah='senyum', kacamata=kacamata, **kw)


A['C43-L4a'] = pemilik_toko('kakek')
A['C43-L4b'] = pemilik_toko('nenek', rambut='uban')
A['C43-L4c'] = pemilik_toko('pria', tinggi=165)
A['C43-L5a'] = lantai() + pelari(150, 'pria')
A['C43-L5b'] = A['C43-5']
A['C43-L5c'] = naik_sepeda(jenis='pria')
A['C43-L6a'] = keranjang(150, 190, 2.0) + ''.join(buah_apel(110 + i * 26, 120, .6) for i in range(4)) + teks(150, 40, '$150', 26, angka=True)
A['C43-L6b'] = keranjang(150, 190, 1.4) + buah_apel(130, 140, .6) + buah_apel(165, 140, .6) + teks(150, 60, '$80', 26, angka=True)
A['C43-L6c'] = keranjang(150, 190, 1.4) + buah_apel(130, 140, .6) + buah_apel(165, 140, .6) + teks(150, 60, '$75', 26, angka=True)
A['C43-L8a'] = lantai() + kios_buah(150, 200, 200) + orang(150, tinggi=150, jenis='wanita', baju='h', rambut='uban', wajah='sedih')
A['C43-L8b'] = A['C43-4']
A['C43-L8c'] = lantai() + kios_buah(220, 200, 140) + orang(70, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(12, 30), (22, 50)]}) + keranjang(100, 170, .7)
A['C43-L9'] = keranjang(150, 196, 2.2) + ''.join(buah_apel(110 + i * 27, 120 + (i % 2) * 8, .7) for i in range(4)) + lantai()
A['C43-L10'] = A['C43-5']
A['C43-T3a'] = keranjang(150, 190, 1.8) + teks(150, 50, '$200', 28, angka=True)
A['C43-T3b'] = keranjang(110, 190, 1.4) + keranjang(200, 190, 1.4) + teks(150, 50, '$350', 28, angka=True)
A['C43-T3c'] = keranjang(150, 190, 1.8) + teks(150, 50, '$150', 28, angka=True)
A['C43-T4a'] = pemilik_toko('nenek', rambut='uban')
A['C43-T4b'] = lantai() + kios_buah(150, 200, 200) + orang(150, tinggi=165, jenis='pria', baju='h', kacamata=True)
A['C43-T4c'] = lantai() + kios_buah(190, 200, 180) + orang(190, tinggi=150, jenis='wanita', baju='h') + orang(60, tinggi=150, jenis='wanita', baju='a', wajah='tawa') + garis((90, 60), (150, 60), k='t') + teks(120, 50, '媽媽的朋友', 12)
A['C43-T6a'] = lantai() + pelari(140, 'pria') + keranjang(200, 120, .6)
A['C43-T6b'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, -10), (40, -20)]}) + keranjang(200, 140, .6) + garis_jatuh(210, 120)
A['C43-T6c'] = lantai() + keranjang(200, 196, 1.2) + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 30), (50, 40)]}) + buah_apel(180, 150, .6)
A['C43-T7'] = A['C43-3']
A['C43-T8'] = pemilik_toko('nenek', rambut='uban')

# --- C44 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def warna_baju(k, label):
    return kaos(150, 100, 1.6, k) + teks(150, 200, label, 20)


A['C44-L4a'] = warna_baju('h', '深')
A['C44-L4b'] = warna_baju('p', '淺')
A['C44-L4c'] = kaos(150, 100, 1.6, 'a') + kotak(250, 20, 30, 30, 'a', 3) + teks(265, 70, '紅', 18)
A['C44-L5a'] = jam_dinding(150, 105, 80, 4, 0)
A['C44-L5b'] = jam_dinding(150, 105, 80, 4, 30)
A['C44-L5c'] = jam_dinding(150, 105, 80, 5, 0)
A['C44-L6a'] = lantai() + meja(150, 150, 200) + kue_c10(130, 146, .8) + teks(200, 120, '甜', 24) + silang(150, 60, 24, 6)
A['C44-L6b'] = lantai() + meja(150, 150, 220) + piring(100, 144, 50, '') + piring(200, 144, 50, '') + teks(150, 80, '臺灣菜', 20)
A['C44-L6c'] = lantai() + meja(150, 150, 200) + piring(150, 144, 60, '') + teks(150, 100, '鹹', 26) + silang(150, 50, 20, 5)
A['C44-L8a'] = lantai() + jam_dinding(200, 80, 50, 10, 0) + orang(80, tinggi=150, jenis='pria', baju='a')
A['C44-L8b'] = lantai() + jam_dinding(200, 80, 50, 3, 0) + orang(80, tinggi=150, jenis='pria', baju='a')
A['C44-L8c'] = lantai_kamar() + ranjang(140, 200, 170) + bulat(86, 136, 13) + muka(86, 136, 13, 'tidur') + jam_dinding(250, 50, 26, 10, 0)
A['C44-L9'] = lantai() + bulat(150, 120, 60, 'a')
A['C44-L10'] = A['C44-L6a']
A['C44-T3a'] = warna_baju('p', '淺')
A['C44-T3b'] = kaos(150, 100, 1.6, 'a') + kotak(250, 20, 30, 30, 'a', 3) + teks(265, 70, '紅', 18)
A['C44-T3c'] = warna_baju('h', '深')
A['C44-T4a'] = jam_dinding(150, 105, 80, 4, 30)
A['C44-T4b'] = jam_dinding(150, 105, 80, 4, 0)
A['C44-T4c'] = jam_dinding(150, 105, 80, 5, 0)
A['C44-T6a'] = kaos(90, 100, 1.0, 'a') + panah(140, 100, 170, 100, 4) + kaos(220, 100, 1.0, 'p')
A['C44-T6b'] = kaos(90, 100, 1.0, 'a') + panah(140, 100, 170, 100, 4) + kaos(220, 100, 1.0, 'h')
A['C44-T6c'] = kaos(90, 100, .8, 'a') + panah(140, 100, 170, 100, 4) + kaos(220, 100, 1.2, 'a')
A['C44-T7'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='h', wajah='tawa') + bintang(90, 40, 10) + bintang(220, 50, 10) + bintang(240, 120, 8)
A['C44-T8'] = A['C44-4']

# --- C45 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def mangkuk_nasi_c45(x, y, s=1.0):
    return jalur(f'M{x - 50 * s} {y} q{50 * s} {70 * s} {100 * s} 0 z', 'p') + jalur(f'M{x - 46 * s} {y} q{46 * s} {-40 * s} {92 * s} 0', 'p') + ''.join(bulat(x + dx * s, y - 12 * s + abs(dx) * .1 * s, 3 * s, 'a') for dx in (-24, -8, 8, 24))


def botol_kecap_c45(x, bawah, s=1.0):
    return kotak(x - 18 * s, bawah - 90 * s, 36 * s, 90 * s, 'h', 6) + kotak(x - 8 * s, bawah - 110 * s, 16 * s, 20 * s, 'h', 2) + kotak(x - 14 * s, bawah - 60 * s, 28 * s, 24 * s, 'p', 2)


def karung_beras_c45(x, bawah, s=1.0):
    return jalur(f'M{x - 40 * s} {bawah} l{6 * s} {-90 * s} l{68 * s} 0 l{6 * s} {90 * s} z', 'p') + garis((x - 30 * s, bawah - 86 * s), (x + 30 * s, bawah - 86 * s), lebar=4) + teks(x, bawah - 36 * s, '米', 28 * s)


A['C45-L4a'] = lantai() + bento(150, 120, 1.2) + tahu(150, 116, .6)
A['C45-L4b'] = lantai() + bento(150, 120, 1.2)
A['C45-L4c'] = lantai() + mangkuk_mi(150, 120, 1.2)
A['C45-L5a'] = lantai() + meja(150, 150, 200) + piring(150, 144, 60, '') + garam(220, 146, .7) + orang(60, tinggi=140, jenis='wanita', baju='a', duduk=150, wajah='sedih')
A['C45-L5b'] = lantai() + meja(150, 150, 200) + piring(150, 144, 60, '') + noda(150, 130, 8) + noda(170, 124, 6) + orang(60, tinggi=140, jenis='wanita', baju='a', duduk=150, wajah='senyum') + jempol(240, 70, .8)
A['C45-L5c'] = lantai() + meja(150, 150, 200) + piring(150, 144, 60, '') + orang(60, tinggi=140, jenis='wanita', baju='a', duduk=150, wajah='sedih') + silang(240, 70, 20, 6)
A['C45-L6a'] = lantai() + piring(150, 150, 90, tahu(150, 140, 1.0))
A['C45-L6b'] = lantai() + piring(150, 160, 120, '') + jalur('M90 140 q70 -50 130 -30 q-60 40 -130 30 z', 'h') + jalur('M220 110 q14 -6 16 -24', 'g', 4) + jalur('M120 90 q10 -20 0 -40 M160 80 q10 -20 0 -40', 'g', 3)
A['C45-L6c'] = lantai() + mangkuk_nasi_c45(150, 140, 1.4)
A['C45-L8a'] = lantai() + piring(150, 150, 90, tahu(150, 140, 1.0))
A['C45-L8b'] = lantai() + piring(150, 150, 90, tahu(150, 140, 1.0).replace("class=\"p\"", "class=\"h\"")) + botol_kecap_c45(240, 196, .6)
A['C45-L8c'] = lantai() + mangkuk_nasi_c45(150, 140, 1.4)
A['C45-L9'] = A['C45-2']
A['C45-L10'] = lantai() + meja(150, 150, 220) + mangkuk_mi(130, 116, .5, sumpit=False) + garam(220, 146, .9) + panah(210, 90, 160, 104, 3)
A['C45-T3a'] = lantai() + bento(150, 120, 1.2) + teks(150, 60, '雞', 24)
A['C45-T3b'] = lantai() + bento(150, 120, 1.2) + tahu(150, 116, .6)
A['C45-T3c'] = lantai() + mangkuk_mi(150, 120, 1.2)
A['C45-T4a'] = lantai() + garam(150, 196, 2.0)
A['C45-T4b'] = lantai() + botol_kecap_c45(150, 196, 1.3)
A['C45-T4c'] = lantai() + karung_beras_c45(150, 196, 1.3)
A['C45-T6a'] = lantai() + piring(150, 150, 90, '') + jempol(240, 70, .6)[:0]
A['C45-T6b'] = lantai() + piring(150, 150, 90, '') + garam(240, 196, .9)
A['C45-T6c'] = lantai() + piring(150, 150, 90, '') + noda(150, 136, 8) + noda(172, 130, 6) + noda(128, 130, 6)
A['C45-T7'] = lantai() + mangkuk_nasi_c45(150, 140, 1.4)
A['C45-T8'] = lantai() + meja(150, 150, 240) + piring(150, 144, 60, '') + ''.join(orang(x, tinggi=140, jenis=j, baju='a', duduk=150, wajah='tawa') for x, j in ((40, 'pria'), (260, 'wanita'))) + orang(150, tinggi=150, jenis='wanita', baju='h', rambut='uban', wajah='tawa')[:0]

# --- C46 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def nanas_c46(x, y, s=1.0):
    o = elips(x, y, 26 * s, 38 * s, 'a') + ''.join(garis((x - 20 * s, y - 20 * s + i * 14 * s), (x + 20 * s, y + i * 14 * s), k='t') for i in range(3))
    return o + bentuk((x, y - 36 * s), (x - 18 * s, y - 70 * s), (x - 4 * s, y - 50 * s), (x, y - 76 * s), (x + 4 * s, y - 50 * s), (x + 18 * s, y - 70 * s), k='h')


def pepaya_c46(x, y, s=1.0):
    return elips(x, y, 24 * s, 40 * s, 'p') + elips(x, y + 6 * s, 12 * s, 22 * s, 'a') + ''.join(bulat(x + dx * s, y + dy * s, 2.5 * s, 'h') for dx, dy in ((-4, 0), (4, 6), (-2, 14), (3, -6)))


def stroberi_c46(x, y, s=1.0):
    return jalur(f'M{x - 24 * s} {y - 14 * s} q{24 * s} {-12 * s} {48 * s} 0 q{-4 * s} {40 * s} {-24 * s} {50 * s} q{-20 * s} {-10 * s} {-24 * s} {-50 * s} z', 'a') + bentuk((x - 18 * s, y - 16 * s), (x, y - 30 * s), (x + 18 * s, y - 16 * s), (x, y - 8 * s), k='h') + ''.join(bulat(x + dx * s, y + dy * s, 2 * s, 'p') for dx, dy in ((-8, 0), (8, 2), (0, 14), (-6, 22), (6, 24)))


A['C46-L4a'] = lantai() + nanas_c46(70, 150, 1.0) + nanas_c46(140, 150, 1.0) + pepaya_c46(225, 150, 1.0)
A['C46-L4b'] = lantai() + nanas_c46(70, 150, 1.0) + pepaya_c46(150, 150, 1.0) + pepaya_c46(225, 150, 1.0)
A['C46-L4c'] = lantai() + nanas_c46(110, 150, 1.0) + nanas_c46(190, 150, 1.0)
A['C46-L5a'] = anggur(150, 120, 2.2)
A['C46-L5b'] = stroberi_c46(150, 110, 2.2)
A['C46-L5c'] = lantai() + jeruk(110, 170, 1.4) + jeruk(190, 170, 1.4)
A['C46-L6a'] = stroberi_c46(150, 110, 2.2)
A['C46-L6b'] = anggur(150, 120, 2.2)
A['C46-L6c'] = lantai() + jeruk(110, 170, 1.4) + jeruk(190, 170, 1.4)
A['C46-L8a'] = lantai() + ''.join(nanas_c46(40 + i * 50, 150, .8) for i in range(3)) + mangga(200, 170, .9) + mangga(250, 170, .9)
A['C46-L8b'] = lantai() + nanas_c46(50, 150, .8) + nanas_c46(100, 150, .8) + mangga(160, 170, .9) + mangga(210, 170, .9) + mangga(260, 170, .9)
A['C46-L8c'] = lantai() + mangga(100, 170, 1.0) + mangga(160, 170, 1.0) + mangga(220, 170, 1.0)
A['C46-L9'] = stroberi_c46(150, 110, 2.2)
A['C46-L10'] = lantai() + mangga(150, 140, 1.6) + bintang(90, 50, 10) + bintang(210, 50, 10) + nanas_c46(60, 160, .6) + pepaya_c46(250, 160, .6)
A['C46-T3a'] = pepaya_c46(150, 110, 2.0)
A['C46-T3b'] = nanas_c46(150, 140, 1.5)
A['C46-T3c'] = anggur(150, 120, 2.2)
A['C46-T4a'] = stroberi_c46(150, 110, 2.2)
A['C46-T4b'] = lantai() + jeruk(110, 170, 1.4) + jeruk(190, 170, 1.4)
A['C46-T4c'] = anggur(150, 120, 2.2)
A['C46-T6a'] = keranjang(150, 196, 2.2) + ''.join(mangga(105 + i * 30, 120 + (i % 2) * 8, .5) for i in range(4))
A['C46-T6b'] = lantai() + jeruk(150, 170, 1.6)
A['C46-T6c'] = keranjang(150, 196, 2.2) + ''.join(jeruk(100 + i * 25, 125 + (i % 2) * 8, .5) for i in range(4)) + mangga(205, 116, .5)
A['C46-T7'] = nanas_c46(150, 140, 1.5)
A['C46-T8'] = lantai() + kios_buah(150, 200, 200) + mangga(150, 80, 1.0) + jalur('M120 60 l-10 -10 M180 60 l10 -10', 'g', 3)

# --- C47 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def gelas_jus(x, bawah, buah, s=1.0):
    return gelas(x, bawah, 'jus', 1.4 * s) + buah


def bawang_c47(x, y, s=1.0):
    return jalur(f'M{x} {y - 40 * s} q{40 * s} {20 * s} {30 * s} {50 * s} q{-30 * s} {14 * s} {-60 * s} 0 q{-10 * s} {-30 * s} {30 * s} {-50 * s} z', 'p') + jalur(f'M{x} {y - 40 * s} q{-10 * s} {30 * s} 0 {64 * s} M{x} {y - 40 * s} q{14 * s} {30 * s} 0 {64 * s}', 'g', 2) + garis((x, y - 40 * s), (x, y - 56 * s), lebar=3)


def kacang_c47(x, y, s=1.0):
    return ''.join(elips(x + dx * s, y + dy * s, 12 * s, 8 * s, 'h') for dx, dy in ((-30, 0), (0, -6), (30, 0), (-16, 14), (16, 14), (0, 22)))


def potongan_steak(tingkat):
    """tingkat: 7, 5, 3 → bagian merah (abu) makin besar."""
    w = {7: 12, 5: 26, 3: 40}[tingkat]
    return lantai() + piring(150, 160, 120, '') + kotak(90, 110, 120, 44, 'h', 10) + kotak(150 - w, 118, 2 * w, 28, 'a', 6) + teks(150, 60, f'{tingkat}分', 24)


A['C47-L4a'] = lantai() + gelas_jus(150, 196, jeruk(210, 80, .8))
A['C47-L4b'] = lantai() + gelas_jus(150, 196, buah_apel(210, 80, .8))
A['C47-L4c'] = lantai() + cangkir(150, 196, 1.6)
A['C47-L5a'] = lantai() + piring(150, 150, 110, steak(150, 138, 1.3, False))
A['C47-L5b'] = A['C47-4']
A['C47-L5c'] = lantai() + piring(150, 150, 110, steak(150, 138, 1.3)) + awan(130, 40, .5, 'h') + awan(180, 30, .4, 'h') + jalur('M130 90 q10 -14 0 -28 M170 90 q10 -14 0 -28', 'g', 3)
A['C47-L6a'] = potongan_steak(7)
A['C47-L6b'] = potongan_steak(5)
A['C47-L6c'] = potongan_steak(3)
A['C47-L8a'] = lantai() + meja(150, 150, 200) + cangkir(150, 146, .9)
A['C47-L8b'] = lantai() + meja(150, 150, 200) + cangkir(120, 146, .9) + pintu(260, 200, 150, 50) + jalan_kaki(220, 'wanita', 140, 'a')
A['C47-L8c'] = lantai() + meja(150, 150, 200) + gelas(150, 146, 'bir', 1.0) if False else lantai() + meja(150, 150, 200) + botol(150, 146, 1.0, 'h')
A['C47-L9'] = lantai() + bawang_c47(150, 140, 1.6)
A['C47-L10'] = A['C47-4']
A['C47-T3a'] = lantai() + gelas_jus(150, 196, buah_apel(210, 80, .8))
A['C47-T3b'] = lantai() + cangkir(150, 196, 1.6)
A['C47-T3c'] = lantai() + gelas_jus(150, 196, jeruk(210, 80, .8))
A['C47-T4a'] = lantai() + mangkuk_nasi_c45(150, 140, 1.4)[:0] + kacang_c47(150, 120, 1.4)
A['C47-T4b'] = A['C47-1']
A['C47-T4c'] = lantai() + mangkuk_mi(150, 120, 1.2)
A['C47-T6a'] = lantai() + kompor(150, 140, 160) + steak(150, 126, .8)
A['C47-T6b'] = A['C47-2']
A['C47-T6c'] = lantai() + kotak(110, 40, 110, 160, 'p', 6) + garis((110, 100), (220, 100), lebar=3) + steak(165, 150, .6, False)
A['C47-T7'] = lantai() + kacang_c47(150, 120, 1.6)
A['C47-T8'] = A['C47-5']

# --- C48 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def udang_c48(x, y, s=1.0):
    return jalur(f'M{x - 40 * s} {y} q{10 * s} {-40 * s} {50 * s} {-30 * s} q{30 * s} {10 * s} {20 * s} {40 * s} q{-14 * s} {-20 * s} {-34 * s} {-16 * s} q{-20 * s} {4 * s} {-36 * s} {6 * s} z', 'a') + garis((x + 10 * s, y - 30 * s), (x + 40 * s, y - 50 * s), lebar=2) + garis((x + 4 * s, y - 30 * s), (x + 30 * s, y - 56 * s), lebar=2)


def ikan_piring_c48(x, y, s=1.0):
    return piring(x, y, 90 * s, ikan(x, y - 8 * s, .8 * s))


A['C48-L4a'] = jam_dinding(150, 105, 80, 7, 30)
A['C48-L4b'] = jam_dinding(150, 105, 80, 7, 0)
A['C48-L4c'] = jam_dinding(150, 105, 80, 8, 0)
A['C48-L5a'] = lantai() + ikan_piring_c48(90, 150) + udang_c48(220, 150, .8)
A['C48-L5b'] = lantai() + piring(80, 150, 80, steak(80, 140, .6)) + piring(170, 150, 80, steak(170, 140, .6)) + salad(250, 140, .6)
A['C48-L5c'] = lantai() + salad(100, 140, .9) + salad(210, 140, .9)
A['C48-L6a'] = lantai() + udang_c48(120, 130, 1.0) + uang_kertas(230, 70, '$$$', 90, 40)
A['C48-L6b'] = lantai() + udang_c48(220, 140, .7) + orang(100, tinggi=150, jenis='wanita', baju='a', wajah='sakit') + keringat(76, 70)
A['C48-L6c'] = lantai() + meja(150, 150, 200) + piring(150, 144, 60, '') + orang(60, tinggi=140, jenis='wanita', baju='a', duduk=150, wajah='puas') + centang(240, 60, .8)
A['C48-L8a'] = lantai(196, 40, 260) + salad(150, 120, 1.6)
A['C48-L8b'] = lantai() + jalur('M90 130 q60 -60 120 0 z', 'a') + kotak(90, 130, 120, 14, 'h', 4) + jalur('M90 144 q60 30 120 0 z', 'a') + ''.join(kotak(220 + i * 10, 90, 6, 60, 'a', 2) for i in range(4))
A['C48-L8c'] = A['C48-5']
A['C48-L9'] = lantai() + ikan_piring_c48(110, 150) + udang_c48(220, 150, .8)
A['C48-L10'] = A['C48-4']
A['C48-T3a'] = jam_dinding(150, 105, 80, 7, 0)
A['C48-T3b'] = jam_dinding(150, 105, 80, 7, 30)
A['C48-T3c'] = jam_dinding(150, 105, 80, 8, 0)
A['C48-T4a'] = A['C48-L5b']
A['C48-T4b'] = A['C48-L5c']
A['C48-T4c'] = A['C48-L5a']
A['C48-T6a'] = kotak(16, 16, 268, 188, 'p') + pintu(60, 200, 150, 60) + meja(110, 150, 90) + panah(110, 110, 110, 136, 3)
A['C48-T6b'] = kotak(16, 16, 268, 188, 'p') + kompor(230, 130, 90) + meja(140, 150, 90) + panah(140, 110, 140, 136, 3)
A['C48-T6c'] = kotak(16, 16, 268, 188, 'p') + jendela(90, 40, 100, 80) + meja(90, 150, 110) + panah(90, 110, 90, 136, 3)
A['C48-T7'] = lantai(196, 40, 260) + salad(150, 120, 1.6)
A['C48-T8'] = lantai() + meja(150, 150, 240) + piring(100, 144, 60, steak(100, 134, .5)) + salad(200, 134, .5) + orang(40, tinggi=140, jenis='pria', baju='a', duduk=150, wajah='tawa') + orang(260, tinggi=135, jenis='wanita', baju='h', duduk=150, wajah='tawa')

# --- C49 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def biskuit_c49(x, y, s=1.0):
    return bulat(x, y, 26 * s, 'a') + ''.join(bulat(x + dx * s, y + dy * s, 3 * s, 'h') for dx, dy in ((-10, -8), (8, -10), (0, 6), (12, 8), (-12, 10)))


def permen_c49(x, y, s=1.0):
    return elips(x, y, 22 * s, 16 * s, 'a') + bentuk((x - 22 * s, y), (x - 40 * s, y - 14 * s), (x - 40 * s, y + 14 * s), k='p') + bentuk((x + 22 * s, y), (x + 40 * s, y - 14 * s), (x + 40 * s, y + 14 * s), k='p')


def cokelat_c49(x, y, s=1.0):
    return kotak(x - 50 * s, y - 30 * s, 100 * s, 60 * s, 'h', 4) + ''.join(garis((x - 50 * s + i * 25 * s, y - 30 * s), (x - 50 * s + i * 25 * s, y + 30 * s), k='w') for i in range(1, 4)) + garis((x - 50 * s, y), (x + 50 * s, y), k='w')


def kopi_c49(x, bawah, s=1.0):
    return cangkir(x, bawah, s) + bulat(x + 70 * s, bawah - 20 * s, 18 * s, 'a') + bulat(x + 70 * s, bawah - 20 * s, 6 * s, 'p')


A['C49-L4a'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(22, -10), (40, -20)]}) + biskuit_c49(200, 90, .7) + permen_c49(250, 140, .7) + silang(225, 115, 40, 7)
A['C49-L4b'] = lantai() + biskuit_c49(110, 120, 1.4) + biskuit_c49(190, 120, 1.4)
A['C49-L4c'] = lantai() + permen_c49(110, 120, 1.3) + permen_c49(200, 120, 1.3)
A['C49-L5a'] = lantai() + cangkir(150, 196, 1.6)
A['C49-L5b'] = lantai() + roti(150, 130, 2.0) + jalur('M120 70 q10 -20 0 -40 M170 70 q10 -20 0 -40', 'g', 3)
A['C49-L5c'] = lantai() + cokelat_c49(150, 120, 1.4)
A['C49-L6a'] = lantai() + cangkir(150, 196, 1.6) + teks(150, 60, '烏龍', 22)
A['C49-L6b'] = lantai() + kaleng(150, 196, 1.6)
A['C49-L6c'] = A['C49-3']
A['C49-L8a'] = lantai() + orang(110, tinggi=120, jenis='gadis', baju='a', tangan={'ka': [(22, -10), (40, -20)]}) + permen_c49(200, 90, .7) + cokelat_c49(240, 150, .5) + silang(220, 120, 40, 7)
A['C49-L8b'] = lantai() + orang(110, tinggi=120, jenis='gadis', baju='a', wajah='tawa', tangan={'ka': [(22, -10), (34, -26)]}) + permen_c49(160, 70, .6)
A['C49-L8c'] = lantai() + orang(110, tinggi=120, jenis='gadis', baju='a', wajah='tawa', tangan={'ka': [(22, -10), (34, -26)]}) + cokelat_c49(170, 70, .4)
A['C49-L9'] = lantai() + mi_cup(150, 196, 1.8)
A['C49-L10'] = lantai() + orang(100, tinggi=160, jenis='wanita', baju='a', wajah='puas') + cangkir(190, 120, .9) + jalur('M180 70 q10 -20 0 -40 M200 70 q10 -20 0 -40', 'g', 3) + jalur('M130 56 q20 -6 40 4', 'g', 2)
A['C49-T3a'] = lantai() + biskuit_c49(110, 120, 1.4) + biskuit_c49(190, 120, 1.4)
A['C49-T3b'] = lantai() + permen_c49(110, 120, 1.3) + permen_c49(200, 120, 1.3)
A['C49-T3c'] = A['C49-L4a']
A['C49-T4a'] = A['C49-L5b']
A['C49-T4b'] = lantai() + cangkir(150, 196, 1.6) + jalur('M130 80 q10 -20 0 -40 M170 80 q10 -20 0 -40', 'g', 3)
A['C49-T4c'] = lantai() + cokelat_c49(150, 120, 1.4)
A['C49-T6a'] = lantai() + kopi_c49(110, 196, 1.2)
A['C49-T6b'] = lantai() + gelas(110, 196, 'susu', 1.2) + kedelai(110, 70, 3, 1.0) + roti(220, 160, 1.0)
A['C49-T6c'] = lantai() + kaleng(100, 196, 1.2) + hamburger(210, 150, .8)
A['C49-T7'] = lantai() + cokelat_c49(150, 120, 1.4)
A['C49-T8'] = A['C49-2']

# --- C50 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def foto_c50(x, y, s=1.0):
    return kotak(x - 26 * s, y - 34 * s, 52 * s, 68 * s, 'p', 3) + bulat(x, y - 8 * s, 12 * s, 'a') + jalur(f'M{x - 18 * s} {y + 28 * s} q{18 * s} {-24 * s} {36 * s} 0', 'a')


A['C50-L4a'] = foto_c50(110, 110, 1.6) + foto_c50(190, 110, 1.6)
A['C50-L4b'] = kotak(70, 50, 80, 110, 'h', 6) + teks(110, 100, 'PASS', 14, angka=True, warna='#fff') + uang_kertas(210, 100, '$', 90, 44)
A['C50-L4c'] = foto_c50(150, 110, 1.8)
A['C50-L5a'] = kota_label('臺中')
A['C50-L5b'] = kota_label('臺北')
A['C50-L5c'] = kota_label('高雄')
A['C50-L6a'] = uang_kertas(150, 105, '$2000', 220, 100)
A['C50-L6b'] = uang_kertas(150, 105, '$1000', 220, 100)
A['C50-L6c'] = uang_kertas(150, 105, '$0', 220, 100)
A['C50-L8a'] = lantai() + awan(150, 16, 1.0, 'a') + hujan(150, 26, 260, 30) + bus(170, 200, 180) + orang(40, tinggi=130, jenis='pria', baju='a')
A['C50-L8b'] = lantai() + matahari(250, 40, 16) + bus(160, 200, 180) + orang(40, tinggi=130, jenis='pria', baju='a')
A['C50-L8c'] = lantai() + awan(150, 16, 1.0, 'a') + hujan(150, 26, 260, 30) + payung(140, 70, 40) + jalan_kaki(140, 'pria', 150, 'a')
A['C50-L9'] = A['C50-4']
A['C50-L10'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='lelah', tangan={'ki': [(16, 30), (30, 56)], 'ka': [(16, 30), (30, 56)]}) + koper(100, 196, 1.1) + koper(200, 196, 1.1)
A['C50-T3a'] = kota_label('臺中')
A['C50-T3b'] = kota_label('高雄')
A['C50-T3c'] = kota_label('臺北')
A['C50-T4a'] = lantai() + kardus(150, 196, 140, 90) + kaos(150, 90, .8, 'a')
A['C50-T4b'] = lantai() + kardus(150, 196, 140, 90) + buah_apel(130, 92, .7) + jeruk(170, 92, .7)
A['C50-T4c'] = lantai() + kardus(150, 196, 140, 90) + buku_tumpuk(150, 110, 3, 70, 14)
A['C50-T6a'] = lantai() + awan(150, 16, 1.0, 'a') + hujan(150, 26, 260, 30) + pelari(150, 'pria')
A['C50-T6b'] = lantai() + matahari(250, 40, 16) + lantai_kamar()[:0] + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'tidur')
A['C50-T6c'] = lantai() + matahari(250, 40, 16) + pohon(50, s=.7) + pelari(150, 'pria')
A['C50-T7'] = A['C50-2']
A['C50-T8'] = lantai() + loket(200) + orang(80, tinggi=160, jenis='pria', baju='h') + kotak(150, 14, 100, 30, 'a', 4) + teks(200, 36, '居留證', 16)

# --- C51 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
A['C51-L4a'] = lantai() + loket(200) + orang(80, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + uang_kertas(150, 90, '$', 50, 24) + panah(150, 60, 180, 60, 3) + panah(180, 70, 150, 70, 3)
A['C51-L4b'] = lantai() + celengan(150, 196, 1.6)
A['C51-L4c'] = lantai() + kotak_pos(200) + orang(100, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(22, -4), (46, -14)]}) + amplop(152, 72, 42, 28, 0)
A['C51-L5a'] = kotak(70, 40, 160, 120, 'p', 4) + bulat(120, 90, 14, 'a') + jalur('M90 150 q30 -40 60 0', 'a') + jalur('M200 50 l-20 30 l14 10 l-20 30', 'g', 4)
A['C51-L5b'] = amplop(150, 110, 200, 130, 0) + jalur('M210 70 l-14 20 l12 8 l-14 22', 'g', 4)
A['C51-L5c'] = lantai() + kotak_pos(150) + jalur('M170 60 l-14 20 l12 8 l-14 22', 'g', 4)
A['C51-L6a'] = kalender_senin(150, 60, 2, 2)
A['C51-L6b'] = kalender_senin(150, 60, 2, 5)
A['C51-L6c'] = kalender_bulan(80, 40, 11, '', 100, 100) + panah(140, 90, 160, 90, 4) + kalender_bulan(220, 40, 12, '', 100, 100) + bulat(220, 100, 36, 'g')
A['C51-L8a'] = lantai() + kotak_pos(210) + orang(100, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, -4), (46, -14)]}) + amplop(152, 72, 42, 28, 0) + panah(160, 50, 190, 60, 3)
A['C51-L8b'] = lantai() + orang(100, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, -4), (46, -14)]}) + amplop(170, 90, 60, 40, 0) + kertas(190, 60, 40, 50, 10)
A['C51-L8c'] = lantai() + orang(100, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, 20), (50, 20)]}) + kardus(190, 196, 90, 60)
A['C51-L9'] = lantai() + celengan(150, 196, 1.6)
A['C51-L10'] = amplop(110, 100, 120, 80, -8) + amplop(190, 120, 120, 80, 8)
A['C51-T3a'] = lantai() + celengan(150, 196, 1.6)
A['C51-T3b'] = A['C51-L4a']
A['C51-T3c'] = lantai() + loket(200) + orang(80, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + kotak(140, 70, 50, 34, 'p', 3) + teks(165, 94, '新', 14)
A['C51-T4a'] = A['C51-L5a']
A['C51-T4b'] = A['C51-L5b']
A['C51-T4c'] = kertas(150, 105, 140, 170, 0) + ''.join(garis((96, 50 + i * 20), (204, 50 + i * 20), k='t') for i in range(6)) + jalur('M210 40 l-14 20 l12 8 l-14 22', 'g', 4)
A['C51-T6a'] = lantai() + loket(200) + orang(80, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + uang_kertas(160, 100, '$', 60, 30) + panah(140, 70, 190, 70, 3)
A['C51-T6b'] = lantai() + toko(200, 200, 140, 100) + jalan_kaki(80, 'pria', 160, 'a') + tas_belanja(110, 190, .6)
A['C51-T6c'] = lantai() + loket(200) + orang(80, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, -4)]}) + uang_kertas(160, 100, '$', 60, 30) + panah(190, 70, 140, 70, 3)
A['C51-T7'] = lantai() + meja(170, 150, 180) + kertas(180, 126, 70, 24) + amplop(240, 140, 40, 26, 0) + orang(70, tinggi=150, jenis='pria', baju='a', duduk=150, tangan={'ka': [(22, 0), (60, -10)]})
A['C51-T8'] = lantai() + kertas(110, 110, 70, 90, -10) + panah(150, 110, 180, 110, 4) + amplop(230, 110, 90, 60, 0)

# --- C52 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def tidur_c52(wajah, jam_h, malam=True):
    o = lantai_kamar() + jam_kecil(70, 56, jam_h, 0, 26) + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, wajah)
    return o + (jendela(230, 30, 60, 46) + bulan_bintang(226, 52, .4) if malam else jendela(230, 30, 60, 46) + matahari(254, 52, 10))


A['C52-L4a'] = lantai() + orang(90, tinggi=110, jenis='laki', baju='h', wajah='tawa', tangan={'ka': [(20, 0), (40, -4)]}) + tas_buka(140, 120, 0, .6) + orang(220, tinggi=160, jenis='pria', baju='a', wajah='kaget')
A['C52-L4b'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='sedih') + tas_buka(230, 196, 0, .7) + teks(230, 120, '?', 30, angka=True)
A['C52-L4c'] = lantai() + pencuri(200, 150) + tas_buka(250, 120, 0, .5) + orang(70, tinggi=160, jenis='pria', baju='a', wajah='kaget')
A['C52-L5a'] = tidur_c52('tidur', 10) + teks(130, 110, 'Z z', 18, angka=True)
A['C52-L5b'] = A['C52-5']
A['C52-L5c'] = tidur_c52('kaget', 10, malam=False)
A['C52-L6a'] = kunci(150, 110, 2.0, 0)
A['C52-L6b'] = dompet(150, 100, 1.8)
A['C52-L6c'] = kotak(110, 30, 80, 150, 'h', 12) + kotak(118, 42, 64, 120, 'p', 4)
A['C52-L8a'] = lantai() + pencuri(120, 150) + garis((150, 120), (190, 120), k='t') + panah(170, 60, 260, 60, 4)
A['C52-L8b'] = lantai() + skuter(170, 200, 1.0) + pencuri(150, 120)
A['C52-L8c'] = lantai() + pencuri(150, 150) + orang(70, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 0), (50, 0)]}) + orang(230, tinggi=155, jenis='wanita', baju='h', tangan={'ki': [(20, 0), (50, 0)]})
A['C52-L9'] = A['C52-5']
A['C52-L10'] = A['C52-1']
A['C52-T3a'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='sedih') + tas_buka(230, 196, 0, .7) + teks(230, 120, '?', 30, angka=True)
A['C52-T3b'] = lantai() + pencuri(200, 150) + tas_buka(250, 120, 0, .5) + orang(70, tinggi=160, jenis='wanita', baju='a', wajah='kaget')
A['C52-T3c'] = lantai() + orang(90, tinggi=110, jenis='gadis', baju='h', wajah='tawa', tangan={'ka': [(20, 0), (40, -4)]}) + tas_buka(140, 120, 0, .6) + orang(220, tinggi=155, jenis='wanita', baju='a', wajah='kaget')
A['C52-T4a'] = lantai() + kotak(20, 20, 50, 50, 'h', 6) + teks(45, 56, 'P', 34, angka=True, warna='#fff') + skuter(160, 200, .9)
A['C52-T4b'] = lantai() + pintu(80, 200, 150, 70) + skuter(200, 200, .9)
A['C52-T4c'] = lantai() + sekolah(200, 200, 130, 90) + kotak(160, 20, 80, 30, 'a', 4) + teks(200, 42, '學校', 18) + skuter(70, 200, .7)
A['C52-T6a'] = lantai() + kado(110, 196, 1.0) + dompet(200, 120, 1.0)
A['C52-T6b'] = lantai() + pencuri(170, 150) + dompet(220, 110, .6) + orang(60, tinggi=160, jenis='pria', baju='a', wajah='kaget')
A['C52-T6c'] = lantai() + loket(200) + dompet(150, 110, .7) + orang(70, tinggi=160, jenis='pria', baju='a')
A['C52-T7'] = A['C52-2']
A['C52-T8'] = lantai() + sofa(150) + dompet(150, 190, .5) + panah(150, 140, 150, 176, 3) + orang(260, tinggi=150, jenis='wanita', baju='a', wajah='tawa')

# --- C53 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def jalan_besar_c53():
    return lantai() + bulan_bintang(250, 30, .4) + garis((16, 150), (284, 150), k='t') + ''.join(garis((30 + i * 60, 175), (60 + i * 60, 175), lebar=4) for i in range(5)) + ''.join(garis((40 + i * 110, 150), (40 + i * 110, 60), lebar=4) + bulat(40 + i * 110, 56, 8, 'p') for i in range(3)) + jalan_kaki(160, 'pria', 110, 'a')


def jalan_gelap_c53():
    return kotak(16, 16, 268, 188, 'h') + garis((16, 200), (284, 200), k='w') + jalan_kaki(150, 'pria', 110, 'a').replace('class="h"', 'class="a"')


A['C53-L4a'] = jalan_besar_c53()
A['C53-L4b'] = jalan_gelap_c53()
A['C53-L4c'] = lantai() + mobil(170, 200, 170, True) + orang(50, tinggi=150, jenis='pria', baju='a', tangan=LAMBAI)
A['C53-L5a'] = lantai() + jalan_kaki(150, 'wanita', 150, 'a') + centang(230, 50, 1.2)
A['C53-L5b'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a') + teks(220, 60, '?', 40, angka=True) + awan(80, 30, .5, 'a')
A['C53-L5c'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a') + silang(230, 60, 24, 6)
A['C53-L6a'] = lantai() + jam_dinding(60, 50, 26, 7, 0) + pintu(220, 200, 150, 60) + jalan_kaki(150, 'pria', 150, 'a')
A['C53-L6b'] = lantai() + sekolah(150, 200, 140, 100) + silang(150, 150, 30, 8)
A['C53-L6c'] = lantai() + jam_dinding(60, 50, 26, 9, 0) + pintu(220, 200, 150, 60) + jalan_kaki(150, 'pria', 150, 'a', 'kaget')
A['C53-L8a'] = topan() + jalan_kaki(150, 'laki', 100, 'a', 'takut')
A['C53-L8b'] = dua_panel(topan().replace(lantai(), ''), rumah(225, 200, 110, 70) + orang(210, kaki=196, tinggi=60, jenis='wanita', baju='a') + orang(240, kaki=196, tinggi=40, jenis='laki', baju='h')) + lantai()
A['C53-L8c'] = lantai() + matahari(240, 40, 18) + orang(120, tinggi=150, jenis='wanita', baju='a', wajah='tawa')
A['C53-L9'] = A['C53-4']
A['C53-L10'] = lantai() + meja(170, 150, 160) + hamburger(170, 136, .6) + silang(170, 120, 30, 6) + orang(60, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(22, -10), (40, -20)]})
A['C53-T3a'] = A['C53-L5a']
A['C53-T3b'] = A['C53-L5c']
A['C53-T3c'] = A['C53-L5b']
A['C53-T4a'] = jalan_gelap_c53()
A['C53-T4b'] = jalan_besar_c53()
A['C53-T4c'] = A['C53-L4c']
A['C53-T6a'] = lantai() + matahari(150, 60, 30)
A['C53-T6b'] = lantai() + ''.join(salju(40 + (i * 67) % 230, 20 + (i * 31) % 100, 8) for i in range(10))
A['C53-T6c'] = lantai() + awan(150, 30, 1.0, 'a') + payung(150, 120, 50) + teks(240, 60, '?', 30, angka=True)
A['C53-T7'] = A['C53-1']
A['C53-T8'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='senyum', tangan={'ki': [(16, 30), (34, 30)], 'ka': [(16, 30), (34, 30)]}) + orang(150, kaki=110, tinggi=30, jenis='bayi', baju='p')

# --- C54 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def langit_malam_c54(n_bintang=12, mendung=False, bulan=False):
    o = kotak(16, 16, 268, 188, 'h', 6)
    pos = ((40, 40), (90, 70), (140, 30), (200, 60), (250, 40), (60, 120), (120, 100), (180, 130), (240, 110), (100, 160), (210, 170), (160, 80))
    o += ''.join(bintang(x, y, 6).replace('class="h"', 'class="n"') for x, y in pos[:n_bintang])
    if bulan: o += bulat(150, 100, 50, 'n')
    if mendung: o += awan(110, 70, 1.0, 'a') + awan(200, 110, 1.0, 'a')
    return o


def musim_c54(jenis):
    if jenis == 'panas': return lantai() + matahari(220, 50, 24) + orang(110, tinggi=150, jenis='wanita', baju='a', wajah='lelah') + keringat(84, 70)
    if jenis == 'gugur': return lantai() + pohon(150, s=1.2) + ''.join(jalur(f'M{x} {y} q6 -8 12 0 q-6 8 -12 0', 'a') for x, y in ((80, 170), (200, 150), (240, 185), (110, 120)))
    return lantai() + ''.join(salju(40 + (i * 67) % 230, 20 + (i * 31) % 120, 8) for i in range(10)) + orang(150, tinggi=150, jenis='wanita', baju='h')


A['C54-L4a'] = lantai() + bunga(150, 150, 2.0)
A['C54-L4b'] = lantai() + buku_tumpuk(150, 196, 1, 120, 30)
A['C54-L4c'] = lantai() + kue_c10(150, 196, 1.4)
A['C54-L5a'] = langit_malam_c54(12)
A['C54-L5b'] = langit_malam_c54(2, mendung=True)
A['C54-L5c'] = A['C54-3']
A['C54-L6a'] = musim_c54('panas')
A['C54-L6b'] = musim_c54('gugur')
A['C54-L6c'] = musim_c54('dingin')
A['C54-L8a'] = lantai() + pagar(16, 284) + ''.join(bunga(40 + i * 45, 180, 1.0) for i in range(6)) + kotak(250, 20, 30, 30, 'h', 3) + teks(265, 70, '紅', 18)
A['C54-L8b'] = lantai() + pagar(16, 284) + bunga(150, 180, 1.2) + teks(150, 60, '黃', 20)
A['C54-L8c'] = lantai() + pagar(16, 284) + pohon(220, s=.7)
A['C54-L9'] = lantai() + matahari(150, 70, 44)
A['C54-L10'] = lantai() + bangku(150) + orang(130, tinggi=140, jenis='pria', baju='a', duduk=170, wajah='lelah') + orang(175, tinggi=135, jenis='wanita', baju='h', duduk=170, wajah='lelah')
A['C54-T3a'] = musim_c54('panas')
A['C54-T3b'] = musim_c54('dingin')
A['C54-T3c'] = musim_c54('gugur')
A['C54-T4a'] = kalender_senin(150, 60, 2, 3)
A['C54-T4b'] = langit_malam_c54(2, mendung=True)
A['C54-T4c'] = kalender_senin(150, 30, 2, 2)[:0] + kalender_bulan(80, 40, 11, '', 100, 100) + kalender_bulan(220, 40, 11, '', 100, 100) + panah(140, 90, 160, 90, 4) + teks(220, 160, '+7', 20, angka=True)
A['C54-T6a'] = lantai() + matahari(220, 50, 26) + pohon(80, s=.9)
A['C54-T6b'] = langit_malam_c54(12)
A['C54-T6c'] = lantai() + awan(110, 40, 1.2, 'a') + awan(210, 60, 1.2, 'a')
A['C54-T7'] = A['C54-3']
A['C54-T8'] = A['C54-5']

from adegan_vol2 import mantou
# --- C55 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def air_c55(isi=''):
    return bentuk((16, 120), (284, 120), (284, 204), (16, 204), k='a') + ''.join(jalur(f'M{x} 140 q10 -8 20 0 t20 0', 'w', 3) for x in (40, 140, 220)) + isi


A['C55-L4a'] = lantai() + roti(110, 130, 1.2) + mantou(210, 196, 1.2)
A['C55-L4b'] = lantai() + mangkuk_nasi_c45(150, 140, 1.4)
A['C55-L4c'] = lantai() + mangkuk_mi(150, 120, 1.2)
A['C55-L5a'] = air_c55(''.join(salju(x, 60, 8) for x in (60, 150, 240))) + orang(150, kaki=120, tinggi=90, jenis='pria', baju='h', wajah='sedih')
A['C55-L5b'] = air_c55(kantong_sampah(80, 170, .4) + botol(160, 170, .4) + ikan(230, 180, .4, 'a')) + tanda_bahaya(240, 40, .6)
A['C55-L5c'] = air_c55(panah(150, 130, 150, 196, 4) + teks(190, 180, '5m', 18, angka=True))
A['C55-L6a'] = lantai() + gunung(170, 200, 260, 170, False) + orang(140, kaki=120, tinggi=90, jenis='pria', baju='a')
A['C55-L6b'] = lantai() + jendela(40, 30, 70, 56) + hujan(75, 34, 60, 50) + sofa(170) + orang(170, tinggi=140, jenis='pria', baju='a', duduk=150) + buku(170, 116, 40, 10, 'a')
A['C55-L6c'] = lantai() + kotak(110, 120, 164, 80, 'a') + mesin_kopi(250, 120) + orang(170, kaki=200, tinggi=145, jenis='pria', baju='h')
A['C55-L8a'] = air_c55(kantong_sampah(80, 170, .4) + botol(150, 150, .4) + kaleng(220, 170, .5)) + lantai()[:0] + kertas(120, 100, 20, 14, 20) + botol(200, 100, .4)
A['C55-L8b'] = air_c55() + matahari(240, 50, 18) + pohon(60, 110, .6)
A['C55-L8c'] = air_c55(ikan(100, 170, .6, 'p') + ikan(200, 160, .6, 'p'))
A['C55-L9'] = A['C55-5']
A['C55-L10'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='tawa', tangan={'ki': [(20, -20), (30, -50)], 'ka': [(20, -20), (30, -50)]}) + burung(70, 50) + burung(230, 40)
A['C55-T3a'] = lantai() + mangkuk_nasi_c45(150, 140, 1.4)
A['C55-T3b'] = lantai() + roti(110, 130, 1.2) + mantou(210, 196, 1.2)
A['C55-T3c'] = lantai() + mangkuk_mi(150, 120, 1.2)
A['C55-T4a'] = A['C55-L5b']
A['C55-T4b'] = air_c55(bentuk((130, 120), (150, 70), (170, 120), k='h'))
A['C55-T4c'] = A['C55-L5a']
A['C55-T6a'] = air_c55(ikan(80, 170, .5, 'p') + ikan(150, 180, .5, 'p') + ikan(220, 165, .5, 'p'))
A['C55-T6b'] = air_c55(silang(150, 160, 30, 6))
A['C55-T6c'] = air_c55(elips(150, 124, 30, 14, 'p') + bulat(176, 108, 10, 'p') + bentuk((184, 106), (198, 110), (184, 114), k='h'))
A['C55-T7'] = lantai() + kotak(60, 110, 160, 90, 'p') + kotak(80, 40, 30, 70, 'h') + kotak(170, 60, 30, 50, 'h') + awan(95, 22, .5, 'h') + awan(185, 40, .5, 'h') + awan(240, 30, .6, 'a')
A['C55-T8'] = A['C55-5']

# --- C56 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
from adegan_vol2 import resto
def ikan_piring_c56(x, y, s=1.0):
    return ikan_piring_c48(x, y, s)


def pizza_c56(x, y, s=1.0):
    r = 50 * s
    return bulat(x, y, r, 'a') + bulat(x, y, r - 6 * s, 'n') + ''.join(garis((x, y), (x + r * c, y + r * d), lebar=2) for c, d in ((1, 0), (-1, 0), (0, 1), (0, -1))) + ''.join(bulat(x + a * s, y + b * s, 5 * s, 'h') for a, b in ((-20, -18), (18, -24), (22, 16), (-16, 22)))


def pohon_natal_c56(x, bawah, s=1.0):
    return kotak(x - 8 * s, bawah - 20 * s, 16 * s, 20 * s, 'h') + bentuk((x - 60 * s, bawah - 20 * s), (x + 60 * s, bawah - 20 * s), (x, bawah - 90 * s), k='a') + bentuk((x - 46 * s, bawah - 70 * s), (x + 46 * s, bawah - 70 * s), (x, bawah - 140 * s), k='a') + bintang(x, bawah - 146 * s, 10 * s)


def sumpit_c56(x, y, s=1.0):
    return garis((x - 30 * s, y + 20 * s), (x + 30 * s, y - 20 * s), lebar=3) + garis((x - 24 * s, y + 26 * s), (x + 36 * s, y - 14 * s), lebar=3)


A['C56-L4a'] = lantai() + meja(150, 150, 200) + ikan_piring_c56(150, 126) + orang(50, tinggi=140, jenis='pria', baju='a', wajah='senyum') + orang(250, tinggi=140, jenis='wanita', baju='h', wajah='senyum') + centang(150, 40, 1.0)
A['C56-L4b'] = lantai() + meja(150, 150, 200) + ikan_piring_c56(150, 126) + orang(250, tinggi=140, jenis='wanita', baju='h') + teks(150, 50, '1', 36, angka=True)
A['C56-L4c'] = lantai() + meja(150, 150, 200) + piring(150, 130, 120, '') + ''.join(garis((130 + i * 14, 124), (136 + i * 14, 130), lebar=2) for i in range(3)) + teks(150, 60, '0', 36, angka=True)
A['C56-L5a'] = lantai() + ikan_piring_c56(150, 150, 1.4)
A['C56-L5b'] = lantai() + hewan_sapi(150, 140, 1.2) + silang(240, 50, 24, 6)
A['C56-L5c'] = lantai() + paha_ayam(150, 140, 1.6)
A['C56-L6a'] = lantai() + orang(70, tinggi=150, jenis='wanita', baju='a', wajah='senyum', tangan={'ka': [(22, -6), (50, -10)]}) + meja_bundar(200, 150, 140) + ikan_piring_c48(170, 128, .6) + mangkuk_nasi_c45(235, 124, .6)
A['C56-L6b'] = lantai() + hamburger(110, 130, 1.0) + kentang_goreng(210, 160, 1.0)
A['C56-L6c'] = lantai() + resto(150)
A['C56-L8a'] = A['C56-2']
A['C56-L8b'] = lantai() + pohon_natal_c56(150, 196, 1.2) + kado(80, 180, .6) + kado(220, 180, .5)
A['C56-L8c'] = pantai_c24()
A['C56-L9'] = A['C56-4']
A['C56-L10'] = lantai() + meja(150, 160, 220) + ikan_piring_c56(100, 136, .7) + mangkuk_nasi_c45(200, 130, .8) + sumpit_c56(150, 116, .9)
A['C56-T3a'] = A['C56-L4a']
A['C56-T3b'] = A['C56-L4c']
A['C56-T3c'] = A['C56-L4b']
A['C56-T4a'] = A['C56-L5a']
A['C56-T4b'] = A['C56-L5c']
A['C56-T4c'] = A['C56-L5b']
A['C56-T6a'] = lantai() + meja(150, 160, 160) + hamburger(150, 136, 1.0) + teks(150, 50, '1', 30, angka=True)
A['C56-T6b'] = lantai() + meja(150, 160, 240) + ikan_piring_c56(70, 136, .6) + mangkuk_mi(150, 112, .7) + hamburger(230, 136, .7) + mangkuk_nasi_c45(110, 70, .5) + pizza_c56(200, 70, .5)
A['C56-T6c'] = lantai() + meja(150, 160, 160) + pizza_c56(150, 130, 1.0)
A['C56-T7'] = A['C56-5']
A['C56-T8'] = lantai() + meja(170, 160, 180) + mangkuk_nasi_c45(150, 136, .7) + orang(60, tinggi=150, jenis='pria', baju='a', wajah='senyum', tangan={'ka': [(20, -6), (44, -4)]}) + teks(60, 40, '1', 30, angka=True) + orang(270, tinggi=150, jenis='wanita', baju='h') + teks(270, 40, '2', 30, angka=True)

# --- C57 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def hilang_c57(*isi):
    return lantai() + ''.join(i for i in isi) + teks(150, 40, '?', 40, angka=True)


A['C57-L4a'] = lantai() + meja(150, 150, 180) + laptop(150, 120, 1.2) + silang(150, 96, 24, 6) + orang(260, tinggi=150, jenis='wanita', baju='a', wajah='marah')
A['C57-L4b'] = hilang_c57(orang(90, tinggi=150, jenis='wanita', baju='a', wajah='sedih'), ponsel(210, 110, 1.2), silang(210, 110, 34, 6))
A['C57-L4c'] = lantai() + meja(150, 150, 180) + kertas(130, 110, 46, 60) + centang(200, 100, 1.2) + orang(260, tinggi=150, jenis='wanita', baju='a', wajah='senyum')
A['C57-L5a'] = lantai() + ponsel(110, 110, 1.2) + silang(110, 110, 34, 6) + dompet(210, 120, .8)
A['C57-L5b'] = lantai() + ponsel(110, 110, 1.2) + silang(110, 110, 34, 6) + dompet(210, 120, .8) + silang(210, 120, 60, 8)
A['C57-L5c'] = lantai() + ponsel(110, 110, 1.2) + dompet(210, 120, .8) + silang(210, 120, 60, 8)
A['C57-L6a'] = lantai() + jam_dinding(230, 60, 36, 9, 30) + jalan_kaki(110, 'pria', 150, 'a', 'gugup') + teks(230, 130, '8:00', 22, angka=True)
A['C57-L6b'] = lantai() + kereta(190, 200, 180) + jam_kecil(250, 40, 9, 50, 24) + jalan_kaki(50, 'pria', 120, 'a', 'gugup')
A['C57-L6c'] = lantai() + mobil(150, 200, 170) + silang(150, 110, 30, 7)
A['C57-L8a'] = potret(150, 96, 50, 'laki', 'tawa', 'a')
A['C57-L8b'] = A['C57-5']
A['C57-L8c'] = tidur_c52('tidur', 2, False)
A['C57-L9'] = lantai() + meja(170, 150, 180) + buku_tumpuk(170, 150, 6, 80, 16) + orang(60, tinggi=150, jenis='pria', baju='a', wajah='marah')
A['C57-L10'] = potret(150, 84, 44, 'wanita', 'senyum', 'a')
A['C57-T3a'] = lantai() + kertas(150, 60, 70, 90) + teks(150, 100, '考', 30)
A['C57-T3b'] = lantai() + kertas(90, 60, 70, 90) + teks(90, 100, '考', 30) + teks(150, 104, '+', 30, angka=True) + kertas(210, 60, 70, 90) + teks(210, 100, '報', 30)
A['C57-T3c'] = lantai() + kertas(150, 60, 70, 90) + teks(150, 100, '報', 30)
A['C57-T4a'] = lantai() + rumah_sakit(150)
A['C57-T4b'] = lantai() + rumah(150, 200, 140, 100) + jalan_kaki(60, 'pria', 120, 'a')
A['C57-T4c'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(16, -20), (8, -50)]}) + ponsel(162, 60, .6)
A['C57-T6a'] = lantai() + meja(150, 150, 180) + orang(110, tinggi=140, jenis='pria', baju='a', wajah='tawa', duduk=170, tangan={'ki': [(16, 10), (30, 0)], 'ka': [(16, 10), (30, 0)]}) + konsol(200, 136, .8)
A['C57-T6b'] = tidur_c52('tidur', 10, True)
A['C57-T6c'] = lantai() + meja(150, 150, 180) + orang(110, tinggi=140, jenis='pria', baju='a', wajah='gugup', duduk=170) + buku(200, 136, 60, 20, 'a') + keringat(86, 60)
A['C57-T7'] = A['C57-4']
A['C57-T8'] = lantai() + papan_tulis(60, 40, 90, 60) + orang(150, tinggi=165, jenis='pria', baju='h', wajah='marah', tangan={'ka': [(20, -6), (44, -10)]}) + orang(240, tinggi=150, jenis='laki', baju='a', wajah='gugup') + jam_dinding(270, 30, 18, 8, 20)

# --- C58 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kopi_c58(x, y, s=1.0):
    return cangkir_kopi(x, y + 60 * s, s * 1.4)


A['C58-L4a'] = lantai() + pintu(60, 200, 150, 60) + orang(130, tinggi=150, jenis='wanita', baju='h', wajah='senyum', tangan=LAMBAI) + koper(160, 196, .6) + orang(240, tinggi=150, jenis='wanita', baju='a', wajah='tawa') + teks(60, 30, '日本 →', 16)
A['C58-L4b'] = lantai() + pesawat(210, 40, .6) + jalan_kaki(80, 'wanita', 140, 'a') + koper(120, 196, .6) + teks(230, 110, '→ 日本', 18)
A['C58-L4c'] = lantai() + orang(110, tinggi=150, jenis='wanita', baju='a', wajah='tawa', tangan={'ka': [(20, -6), (40, -10)]}) + kado(170, 120, .7)
A['C58-L5a'] = lantai() + kopi_c58(110, 100, 1.4) + centang(190, 100, 1.0)
A['C58-L5b'] = lantai() + kopi_c58(80, 100, 1.2) + centang(130, 60, .8) + teks(170, 120, '+', 30, angka=True) + koin(240, 110, 22) + centang(240, 60, .8)
A['C58-L5c'] = lantai() + koin(150, 110, 30) + centang(220, 80, 1.0)
A['C58-L6a'] = lantai() + meja_kantor(150) + orang(150, tinggi=150, jenis='pria', baju='a', wajah='lelah') + keringat(124, 60)
A['C58-L6b'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='tawa') + koin_banyak(210, 150)
A['C58-L6c'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah='sedih') + koin(210, 170, 14)
A['C58-L8a'] = lantai() + meja(170, 150, 180) + buku(170, 136, 60, 20, 'a') + orang(110, tinggi=140, jenis='pria', baju='a', wajah='gugup', duduk=170) + keringat(86, 60)
A['C58-L8b'] = A['C58-4']
A['C58-L8c'] = tidur_c52('tidur', 10, True)
A['C58-L9'] = A['C58-5']
A['C58-L10'] = A['C58-3']
A['C58-T3a'] = lantai() + koin(150, 110, 30)
A['C58-T3b'] = lantai() + koin_banyak(80, 150) + teks(150, 120, '+', 30, angka=True) + rumah(230, 200, 90, 70) + jalan_kaki(180, 'wanita', 70, 'a')
A['C58-T3c'] = lantai() + rumah(200, 200, 110, 80) + jalan_kaki(120, 'wanita', 110, 'a')
A['C58-T4a'] = lantai() + kertas(150, 80, 80, 110) + teks(150, 140, '考', 34)
A['C58-T4b'] = lantai() + anjing(150, 196, 1.4)
A['C58-T4c'] = lantai() + dompet(150, 110, 1.2) + teks(150, 180, '0', 30, angka=True)
A['C58-T6a'] = potret(150, 84, 44, 'wanita', 'tawa', 'a')
A['C58-T6b'] = potret(150, 84, 44, 'wanita', 'sedih', 'a')
A['C58-T6c'] = potret(150, 84, 44, 'wanita', 'marah', 'a') + ''.join(garis((230 + a, 40 + b), (230 + 2 * a, 40 + 2 * b), lebar=5) for a, b in ((10, 0), (-10, 0), (0, 10), (0, -10)))
A['C58-T7'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='kaget', tangan={'ki': [(20, -20), (30, -40)], 'ka': [(20, -20), (30, -40)]}) + orang(60, tinggi=150, jenis='wanita', baju='h', wajah='tawa') + orang(240, tinggi=150, jenis='wanita', baju='a', wajah='tawa') + balon(60, 30) + balon(240, 30)
A['C58-T8'] = pantai_c24(150)

# --- C59 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
from adegan_vol2 import baju_gantung
def jabat_c59(wajah='senyum'):
    return lantai() + orang(110, tinggi=160, jenis='pria', baju='a', wajah=wajah, tangan={'ka': [(20, -4), (36, 10)]}) + orang(190, tinggi=155, jenis='wanita', baju='h', wajah=wajah, tangan={'ki': [(20, -4), (36, 10)]})


A['C59-1'] = jabat_c59() + centang(150, 40, 1.0)
A['C59-L4a'] = lantai() + kotak_berat(150, 150, 1.0) + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='senyum') + orang(225, tinggi=160, jenis='pria', baju='h', wajah='senyum')
A['C59-L4b'] = lantai() + jalan_kaki(110, 'wanita', 160, 'a') + tas_belanja(180, 196, 1.0) + tas_belanja(220, 196, .8)
A['C59-L4c'] = lantai() + sofa(150) + orang(150, tinggi=140, jenis='wanita', baju='a', duduk=160, wajah='senyum')
A['C59-L5a'] = lantai() + mangkuk_nasi_c45(150, 140, 1.4)
A['C59-L5b'] = lantai() + mangkuk_mi(150, 120, 1.2) + daging(120, 100, .5) + daging(180, 100, .5)
A['C59-L5c'] = lantai() + roti(150, 130, 1.4)
A['C59-L6a'] = kota_label('韓國')
A['C59-L6b'] = kota_label('日本')
A['C59-L6c'] = kota_label('臺灣')
A['C59-L8a'] = lantai() + ''.join(orang(60 + i * 90, tinggi=150, jenis=j, baju=b) for i, (j, b) in enumerate((('pria', 'a'), ('wanita', 'h'), ('pria', 'p')))) + ''.join(teks(60 + i * 90, 30, '…', 24, angka=True) for i in range(3))
A['C59-L8b'] = lantai() + ''.join(orang(60 + i * 90, tinggi=150, jenis=j, baju=b) for i, (j, b) in enumerate((('pria', 'a'), ('wanita', 'h'), ('pria', 'p')))) + gelembung(60, 30, 50, 34, teks(60, 38, 'A', 20, angka=True)) + gelembung(150, 30, 50, 34, teks(150, 38, 'B', 20, angka=True)) + gelembung(240, 30, 50, 34, teks(240, 38, 'C', 20, angka=True))
A['C59-L8c'] = lantai() + ''.join(orang(60 + i * 90, tinggi=150, jenis=j, baju=b, wajah='senyum') for i, (j, b) in enumerate((('pria', 'a'), ('wanita', 'h'), ('pria', 'p')))) + gelembung(60, 30, 50, 34, teks(60, 38, 'A', 20, angka=True)) + gelembung(150, 30, 50, 34, teks(150, 38, 'A', 20, angka=True)) + gelembung(240, 30, 50, 34, teks(240, 38, 'A', 20, angka=True))
A['C59-L9'] = lantai() + orang(80, tinggi=160, jenis='wanita', baju='a', wajah=None) + teks(80, 30, '?', 30, angka=True) + meja(210, 150, 140) + mangkuk_mi(180, 116, .5) + mangkuk_nasi_c45(240, 126, .5)
A['C59-L10'] = jabat_c59() + jempol(150, 50)
A['C59-T3a'] = lantai() + kereta(150, 200, 250)
A['C59-T3b'] = lantai() + pesawat(150, 90, 1.2)
A['C59-T3c'] = lantai() + bus(150, 200, 230)
A['C59-T4a'] = lantai() + jam_dinding(150, 100, 70, 8, 0) + matahari(260, 40, 14)
A['C59-T4b'] = lantai() + jam_dinding(150, 100, 70, 6, 0) + matahari(260, 40, 14)
A['C59-T4c'] = lantai() + jam_dinding(150, 100, 70, 10, 0) + matahari(260, 40, 14)
A['C59-T6a'] = A['C59-L8a']
A['C59-T6b'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='a', wajah='marah') + orang(210, tinggi=155, jenis='wanita', baju='h', wajah='marah') + silang(150, 50, 24, 6)
A['C59-T6c'] = A['C59-L8c']
A['C59-T7'] = A['C59-2']
A['C59-T8'] = lantai() + baju_gantung(100, 40, 'a') + baju_gantung(200, 40, 'h') + panah(200, 170, 200, 130, 4) + teks(200, 190, '1', 20, angka=True)

# --- C60 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
A['C60-1'] = lantai() + papan_tulis(90, 30, 120, 50) + meja_kelas(150) + orang(150, tinggi=120, jenis='pria', baju='a', duduk=180, wajah='tidur') + teks(180, 80, 'z', 18, angka=True) + teks(194, 66, 'Z', 22, angka=True) + gelembung(240, 50, 80, 60, tv(240, 70, 46))
A['C60-L4a'] = lantai() + tv(80, 160, 90) + sofa(200) + orang(200, tinggi=140, jenis='wanita', baju='a', duduk=160, wajah='senyum') + jendela(250, 30, 50, 40) + hujan(275, 34, 40, 30, 4)
A['C60-L4b'] = pantai_c24(150)
A['C60-L4c'] = lantai() + jalan_kaki(110, 'wanita', 160, 'a') + tas_belanja(180, 196, 1.0) + tas_belanja(220, 196, .8)
A['C60-L5a'] = lantai() + rumah(150, 200, 230, 150)
A['C60-L5b'] = lantai() + rumah(80, 200, 110, 80) + stasiun(220, 200, 110, 80) + papan_angka(220, 70, '捷運', 80, 34, False, 20) + panah(140, 180, 160, 180, 3)
A['C60-L5c'] = lantai() + rumah(110, 200, 120, 90) + koin(230, 150, 16) + teks(230, 110, '1', 26, angka=True)
A['C60-L6a'] = lantai() + orang(90, tinggi=170, jenis='pria', baju='h', tangan={'ka': [(20, -6), (44, -14)]}) + orang(200, tinggi=150, jenis='wanita', baju='a', wajah='sedih') + buku(250, 110, 40, 50, 'a') + teks(250, 146, '法', 20)
A['C60-L6b'] = lantai() + kota_label('臺灣') + orang(240, tinggi=120, jenis='wanita', baju='a', wajah='tawa') + koper(270, 196, .5)
A['C60-L6c'] = lantai() + buku_tumpuk(170, 196, 5, 90, 20) + teks(170, 70, '法', 24) + orang(70, tinggi=150, jenis='wanita', baju='a', wajah='lelah') + keringat(50, 70)
A['C60-L8a'] = lantai() + papan_tulis(190, 30, 150, 80) + orang(80, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, -10), (50, -30)]})
A['C60-L8b'] = lantai() + meja_kantor(150) + orang(150, tinggi=150, jenis='pria', baju='h')
A['C60-L8c'] = lantai() + meja_kelas(150) + orang(150, tinggi=120, jenis='pria', baju='a', duduk=180) + tas_punggung(210, 170, .6)
A['C60-L9'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='sakit', tangan={'ka': [(16, -10), (8, -40)]}) + ponsel(170, 60, .6) + ''.join(jalur(f'M{x} 30 q6 -6 12 0', 'p', 2) for x in (110, 130, 200))
A['C60-L10'] = lantai() + awan(150, 20, 1.0, 'a') + hujan(150, 40, 220, 40, 9) + orang(150, tinggi=150, jenis='pria', baju='a', wajah='senyum', tangan={'ka': [(16, -10), (20, -40)]}) + payung(160, 70, 50)
A['C60-T3a'] = lantai() + awan(150, 20, 1.0, 'a') + hujan(150, 40, 220, 40, 9) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='senyum', tangan={'ka': [(16, -10), (20, -40)]}) + payung(160, 70, 50)
A['C60-T3b'] = lantai() + awan(150, 20, 1.0, 'a') + hujan(150, 40, 240, 120, 14) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='sedih', tangan={'ki': [(16, -20), (6, -46)], 'ka': [(16, -20), (6, -46)]})
A['C60-T3c'] = lantai() + matahari(240, 40, 22) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='senyum')
A['C60-T4a'] = lantai() + gedung(110, tingkat=4, lebar=110) + koin_banyak(230, 160)
A['C60-T4b'] = lantai() + gedung(50, tingkat=4, lebar=60) + garis((90, 196), (250, 196), k='t') + panah(90, 170, 240, 170, 4) + sekolah(260, 200, 60, 50)
A['C60-T4c'] = lantai() + gedung(150, tingkat=4, lebar=130) + ''.join(teks(x, y, '♪', 22, angka=True) for x, y in ((40, 50), (260, 40), (60, 120), (250, 120))) + orang(240, tinggi=80, jenis='pria', baju='a', wajah='marah')
A['C60-T6a'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'lelah') + ponsel(120, 110, .5) + jam_kecil(240, 50, 1, 0, 22)
A['C60-T6b'] = lantai_kamar() + ranjang(150, 200, 180) + bulat(96, 136, 13) + muka(96, 136, 13, 'senyum') + buku(124, 112, 30, 24, 'a') + jam_kecil(240, 50, 10, 0, 22)
A['C60-T6c'] = tidur_c52('tidur', 11, True)
A['C60-T7'] = lantai() + gunung(170, 200, 240, 140) + bentuk((16, 200), (120, 160), (160, 160), (80, 200), k='a') + pohon(50, s=.8)
A['C60-T8'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='senyum', tangan={'ka': [(20, -6), (44, -14)]}) + orang(200, tinggi=150, jenis='wanita', baju='h', wajah='sedih')

# --- C61 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
from adegan_vol2 import resto, sayur
def layar_film_c61(wajah):
    return lantai() + kotak(40, 20, 220, 130, 'h', 6) + kotak(50, 30, 200, 110, 'n', 4) + bulat(150, 85, 40, 'w') + muka(150, 85, 40, wajah) + ''.join(kotak(60 + i * 45, 160, 30, 24, 'a', 4) for i in range(5))


def resto_c61(isi=''):
    return lantai() + resto(150) + isi


A['C61-L4a'] = lantai() + buku(150, 190, 100, 140, 'a') + teks(150, 130, '小說', 26)
A['C61-L4b'] = lantai() + majalah(150, 110, 1.4)
A['C61-L4c'] = lantai() + koran_c18(150, 110, 1.4)
A['C61-L5a'] = pegang_perut(150, 'pria', 160, 'a', 'lapar') + meja(240, 150, 80)
A['C61-L5b'] = lantai() + meja(170, 150, 180) + mangkuk_nasi_c45(130, 130, .6) + mangkuk_mi(210, 120, .5) + orang(60, tinggi=160, jenis='pria', baju='a', wajah='puas', tangan={'ki': [(16, 20), (30, 24)], 'ka': [(16, 20), (30, 24)]}) + jalur('M44 110 q16 20 32 0', 'p', 3)
A['C61-L5c'] = lantai() + kompor(190, 150, 120) + orang(90, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, -6), (50, 0)]})
A['C61-L6a'] = lantai() + kursi(150, s=1.2) + orang(150, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='lelah') + buku(200, 120, 40, 50, 'a') + teks(150, 30, '…', 30, angka=True)
A['C61-L6b'] = lantai() + kursi(150, s=1.2) + orang(150, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='tawa') + buku(200, 120, 40, 50, 'a') + jempol(240, 50)
A['C61-L6c'] = lantai() + kursi(150, s=1.2) + orang(150, tinggi=150, jenis='pria', duduk=160, baju='a', wajah=None) + buku(200, 120, 40, 50, 'a') + teks(150, 30, '???', 28, angka=True)
A['C61-L8a'] = resto_c61(teks(240, 40, '?', 34, angka=True))
A['C61-L8b'] = resto_c61(kotak(100, 30, 100, 36, 'w', 4) + garis((100, 30), (200, 30), lebar=3) + garis((100, 66), (200, 66), lebar=3) + garis((100, 30), (100, 66), lebar=3) + garis((200, 30), (200, 66), lebar=3) + teks(150, 56, '休息', 22))
A['C61-L8c'] = resto_c61(''.join(orang(x, tinggi=110, jenis=j, baju='a', wajah='senyum') for x, j in ((40, 'pria'), (60, 'wanita'), (250, 'pria'), (270, 'wanita'))))
A['C61-L9'] = lantai() + kotak(70, 80, 140, 116, 'w', 12) + garis((70, 80), (210, 80), lebar=4) + garis((70, 80), (70, 196), lebar=4) + garis((210, 80), (210, 196), lebar=4) + garis((70, 196), (210, 196), lebar=4) + buku(100, 194, 26, 50, 'a') + buku(130, 194, 26, 50, 'h') + panah(260, 50, 180, 120, 4) + buku(262, 70, 26, 40, 'a')
A['C61-L10'] = lantai() + kaos(100, 90, 1.2) + teks(160, 100, '+', 30, angka=True) + sepatu_pasang(200, 150, .9)
A['C61-T3a'] = layar_film_c61('tawa')
A['C61-T3b'] = layar_film_c61('sedih')
A['C61-T3c'] = layar_film_c61('takut')
A['C61-T4a'] = lantai() + buku(135, 120, 26, 50, 'a') + buku(165, 120, 26, 50, 'h') + tas_belanja(150, 196, 1.8)
A['C61-T4b'] = lantai() + tong_daur(150, 200, 'a') + buku(150, 100, 30, 40, 'a') + panah(150, 50, 150, 80, 4)
A['C61-T4c'] = lantai() + kardus(90, 200, 100, 70) + buku_tumpuk(90, 130, 3, 70, 16) + teks(170, 160, '+', 30, angka=True) + kardus(230, 200, 100, 70)
A['C61-T6a'] = A['C61-L8b']
A['C61-T6b'] = resto_c61(koin(250, 60, 14))
A['C61-T6c'] = resto_c61(koin_banyak(255, 70))
A['C61-T7'] = lantai() + buah_apel(50, 150, .8) + pisang(100, 160, .7) + garis((150, 60), (150, 200), lebar=4) + sayur(225, 150, 1.0)
A['C61-T8'] = lantai() + meja_kantor(150) + orang(150, tinggi=150, jenis='pria', baju='a', wajah='lelah') + keringat(124, 60) + koin(250, 60, 12)

# --- C62 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
from adegan_vol2 import pelari
A['C62-L4a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='senyum', tangan={'ki': [(14, 20), (24, 40)], 'ka': [(14, 20), (24, 40)]}) + kotak_berat(150, 110, .8)
A['C62-L4b'] = lantai() + kotak_berat(230, 170, .8) + orang(100, tinggi=160, jenis='pria', baju='a', tangan=LAMBAI) + gelembung(170, 40, 70, 40, teks(170, 48, '來！', 18))
A['C62-L4c'] = lantai() + kotak_berat(80, 170, .8) + jalan_kaki(200, 'pria', 160, 'a')
A['C62-L5a'] = lantai() + jalan_kaki(110, 'wanita', 160, 'a') + jalan_kaki(190, 'pria', 160, 'h') + panah(230, 60, 280, 60, 4)
A['C62-L5b'] = lantai() + bangku(150, 200, 160) + orang(120, tinggi=140, jenis='wanita', baju='a', duduk=168, wajah='lelah') + orang(180, tinggi=145, jenis='pria', baju='h', duduk=168)
A['C62-L5c'] = lantai() + mobil(170, 200, 170, True) + orang(50, tinggi=150, jenis='wanita', baju='a', tangan=LAMBAI)
A['C62-L6a'] = A['C62-2']
A['C62-L6b'] = lantai() + ranjang(120, 200, 180) + bulat(60, 130, 14) + muka(60, 130, 14, 'sakit') + termometer(265, 50, 39, 40, 100)
A['C62-L6c'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='sakit', tangan={'ka': [(20, 0), (30, 20)]}) + perban(184, 120)
A['C62-L8a'] = lantai() + kota_label('臺灣')[len(lantai()):] + tas_belanja(250, 196, .8)
A['C62-L8b'] = lantai() + kotak_pos(220) + kardus(100, 200, 90, 70) + panah(150, 150, 190, 150, 4)
A['C62-L8c'] = lantai() + koper(80, 196, 1.2) + kado(160, 196, .7) + kado(220, 196, .6) + orang(270, tinggi=150, jenis='wanita', baju='a', wajah='senyum') + pesawat(150, 40, .5)
A['C62-L9'] = lantai() + meja(170, 140, 160) + orang(70, tinggi=160, jenis='pria', baju='a', wajah='sakit', tangan={'ka': [(22, 10), (40, 30)]}) + keringat(48, 60)
A['C62-L10'] = A['C62-5']
A['C62-T3a'] = lantai() + tas_belanja(200, 196, 1.2) + orang(100, tinggi=160, jenis='wanita', baju='a', wajah='marah') + silang(200, 100, 20, 5)
A['C62-T3b'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='lelah', tangan={'ki': [(20, 30), (60, 70)], 'ka': [(20, 30), (60, 70)]}) + kardus(200, 200, 90, 60) + keringat(86, 60) + teks(200, 110, '!!', 26, angka=True)
A['C62-T3c'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='senyum', tangan={'ki': [(14, 20), (24, 40)], 'ka': [(14, 20), (24, 40)]}) + kardus(150, 130, 70, 40)
A['C62-T4a'] = lantai() + piring(150, 150, 100, ''.join(bulat(100 + i * 33, 140, 13, 'a') + bulat(100 + i * 33, 140, 4, 'h') for i in range(4)))
A['C62-T4b'] = lantai() + buku_tumpuk(150, 196, 4, 110, 24)
A['C62-T4c'] = lantai() + kaos(150, 90, 1.5)
A['C62-T6a'] = lantai() + kakek(150, wajah='lelah') + keringat(124, 60) + bangku(240, 200, 70)
A['C62-T6b'] = lantai() + pelari(170, 'pria', 'h', 150) + ''.join(garis((60, y), (110, y), lebar=3) for y in (80, 110, 140))
A['C62-T6c'] = tidur_c52('tidur', 10, True)
A['C62-T7'] = lantai() + koper(80, 196, 1.3) + koper(150, 196, 1.3) + koper(220, 196, 1.3) + orang(270, tinggi=150, jenis='pria', baju='a', wajah='lelah')
A['C62-T8'] = lantai() + ponsel(110, 100, 1.4) + teks(110, 180, '30000', 18, angka=True) + dompet(220, 120, 1.0) + teks(220, 180, '500', 18, angka=True)

# --- C63 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
A['C63-L4a'] = lantai() + tv(200, 160, 120) + meja(200, 160, 100)[:0] + sofa(90, 200, 120) + orang(90, tinggi=140, jenis='wanita', baju='a', duduk=166, wajah='tawa')
A['C63-L4b'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='sedih') + keringat(138, 66) + keringat(162, 66) + keringat(140, 84)
A['C63-L4c'] = tidur_c52('tidur', 10, True)
A['C63-L5a'] = lantai() + tas_belanja(150, 196, 1.6) + kunci(150, 90)
A['C63-L5b'] = lantai() + meja(150, 140, 180) + kunci(150, 126)
A['C63-L5c'] = lantai() + sofa(150, 200, 200) + kunci(150, 192)
A['C63-L6a'] = lantai() + jam_dinding(150, 100, 70, 3, 0)
A['C63-L6b'] = lantai() + jam_dinding(150, 100, 70, 3, 30)
A['C63-L6c'] = lantai() + jam_dinding(150, 100, 70, 4, 0)
A['C63-L8a'] = lantai() + polisi(150)
A['C63-L8b'] = lantai() + meja_kelas(150) + orang(150, tinggi=120, jenis='pria', baju='a', duduk=180) + tas_punggung(210, 170, .6)
A['C63-L8c'] = lantai() + meja_kantor(150) + orang(150, tinggi=160, jenis='pria', baju='h') + orang(260, tinggi=150, jenis='wanita', baju='a', wajah='kaget')
A['C63-L9'] = A['C63-4']
A['C63-L10'] = lantai() + meja(170, 150, 180) + mangkuk_nasi_c45(140, 130, .6) + mangkuk_nasi_c45(200, 130, .6) + jam_dinding(240, 40, 24, 7, 0) + orang(60, tinggi=110, jenis='laki', baju='a', wajah='lapar') + pintu(280, 200, 120, 30)
A['C63-T3a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='senyum') + lampu_ide(200, 50, .8)
A['C63-T3b'] = A['C63-5']
A['C63-T3c'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(16, -20), (8, -50)]}) + ponsel(162, 60, .6)
A['C63-T4a'] = lantai() + jalan_kaki(110, 'wanita', 160, 'a') + tas_belanja(180, 196, 1.0) + tas_belanja(220, 196, .8)
A['C63-T4b'] = lantai() + meja(170, 150, 160) + mangkuk_mi(170, 120, .6) + orang(70, tinggi=150, jenis='wanita', baju='a', duduk=180)
A['C63-T4c'] = lantai() + jam_dinding(240, 50, 26, 3, 30) + orang(120, tinggi=160, jenis='wanita', baju='a', wajah='marah', tangan={'ka': [(16, 6), (10, 30)]})
A['C63-T6a'] = lantai() + pelari(140, 'pria', 'a', 150) + pelari(220, 'wanita', 'h', 140) + ''.join(garis((30, y), (80, y), lebar=3) for y in (80, 110, 140))
A['C63-T6b'] = lantai() + orang(100, tinggi=160, jenis='pria', baju='a', wajah='tawa', tangan={'ka': [(20, -6), (40, -14)]}) + orang(200, tinggi=155, jenis='wanita', baju='h', wajah='tawa') + gelembung(150, 30, 60, 30, teks(150, 38, '…', 18, angka=True))
A['C63-T6c'] = tidur_c52('tidur', 11, True)
A['C63-T7'] = lantai() + papan_tulis(240, 20, 90, 60) + orang(170, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, -10), (40, -30)]}) + orang(70, tinggi=150, jenis='wanita', baju='a', wajah='kaget')
A['C63-T8'] = lantai() + meja_kelas(150) + orang(150, tinggi=120, jenis='laki', baju='a', duduk=180, wajah='sedih') + gelembung_pikiran(230, 40, 70, 50, buku(230, 64, 30, 36, 'a') + silang(230, 46, 22, 5))

# --- C64 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def univ_c64(isi=''):
    return lantai() + gedung(200, tingkat=4, lebar=150) + papan_angka(200, 40, '大學', 80, 30, False, 18) + isi


A['C64-L4a'] = univ_c64(orang(70, tinggi=160, jenis='pria', baju='a', wajah='tawa', tangan={'ki': [(20, -20), (30, -50)], 'ka': [(20, -20), (30, -50)]}) + centang(265, 40, .7))
A['C64-L4b'] = univ_c64(orang(70, tinggi=160, jenis='pria', baju='a', wajah='sedih') + silang(265, 40, 14, 4))
A['C64-L4c'] = lantai() + meja_kantor(150) + orang(150, tinggi=150, jenis='pria', baju='h')
A['C64-L5a'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (50, 10)]}) + jaket_item(235, 130, .5) + panah(175, 120, 205, 130, 3)
A['C64-L5b'] = lantai() + orang(150, tinggi=170, jenis='wanita', baju='h', wajah='senyum') + jaket_di(150, 170, 'wanita')
A['C64-L5c'] = lantai() + ''.join(salju(40 + (i * 67) % 230, 20 + (i * 31) % 100, 7) for i in range(8)) + jalan_kaki(150, 'wanita', 160, 'a', 'sakit')
A['C64-L6a'] = lantai() + meja_kantor(150) + orang(150, tinggi=150, jenis='pria', baju='h')
A['C64-L6b'] = lantai() + bioskop(150)
A['C64-L6c'] = lantai() + papan_tulis(190, 30, 150, 80) + orang(80, tinggi=165, jenis='pria', baju='h', kacamata=True, tangan={'ka': [(20, -10), (50, -30)]})
A['C64-L8a'] = lantai() + sekolah(170, 200, 160, 100) + orang(60, tinggi=90, jenis='laki', baju='a', wajah='senyum') + tas_punggung(80, 150, .5)
A['C64-L8b'] = A['C64-L4a']
A['C64-L8c'] = A['C64-L4b']
A['C64-L9'] = lantai() + orang(100, tinggi=160, jenis='pria', baju='a', wajah='tawa') + orang(210, tinggi=155, jenis='wanita', baju='h', wajah='senyum') + jalur('M150 70 c-24 -30 -50 0 0 34 c50 -34 24 -64 0 -34 z', 'h', 2)
A['C64-L10'] = lantai() + meja(150, 150, 120) + cangkir_kopi(130, 146, .6) + cangkir_kopi(170, 146, .6) + orang(60, tinggi=140, jenis='pria', baju='a', duduk=180, wajah='tawa') + orang(240, tinggi=140, jenis='pria', baju='h', duduk=180, wajah='tawa')
A['C64-T3a'] = lantai() + sekolah(170, 200, 160, 100) + papan_angka(170, 30, '高中', 80, 30, False, 18) + orang(60, tinggi=140, jenis='wanita', baju='a')
A['C64-T3b'] = A['C64-L4b'].replace("jenis='pria'", "jenis='wanita'")
A['C64-T3c'] = univ_c64(orang(70, tinggi=160, jenis='wanita', baju='a', wajah='tawa', tangan={'ki': [(20, -20), (30, -50)], 'ka': [(20, -20), (30, -50)]}) + centang(265, 40, .7))
A['C64-T4a'] = lantai() + sekolah(150, 200, 200, 110) + papan_angka(150, 30, '學校', 80, 30, False, 18)
A['C64-T4b'] = lantai() + pesawat(150, 90, 1.3)
A['C64-T4c'] = lantai() + kereta(150, 200, 250)
A['C64-T6a'] = lantai() + sekolah(220, 200, 120, 80) + orang(60, tinggi=150, jenis='pria', baju='a', wajah='tawa', tangan={'ka': [(20, -6), (40, -14)]}) + orang(140, tinggi=150, jenis='wanita', baju='h', wajah='tawa')
A['C64-T6b'] = lantai() + pelari(110, 'pria', 'a', 150) + bola(210, 180, 16, 'sepak')
A['C64-T6c'] = lantai() + meja(150, 150, 180) + mangkuk_nasi_c45(110, 130, .6) + mangkuk_mi(190, 120, .5) + orang(60, tinggi=140, jenis='pria', baju='a', duduk=180)
A['C64-T7'] = lantai() + pintu(150, 200, 160, 80)
A['C64-T8'] = lantai() + ''.join(salju(40 + (i * 67) % 230, 20 + (i * 31) % 100, 7) for i in range(8)) + orang(150, tinggi=170, jenis='pria', baju='h', wajah='senyum') + jaket_di(150, 170, 'pria')

# --- C65 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def tas_c65(isi=''):
    return lantai() + jalur('M90 196 L100 90 L200 90 L210 196 Z', 'p', 4) + jalur('M125 90 q25 -40 50 0', 'p', 5) + isi


def kursi_baris_c65(isi_list):
    o = lantai() + kotak(30, 20, 240, 60, 'h', 4)
    for i, ada in enumerate(isi_list):
        x = 50 + i * 50
        o += kursi_depan(x, 170)
        if ada: o += orang(x, tinggi=110, jenis='pria' if i % 2 else 'wanita', duduk=170, baju='a' if i % 2 else 'h')
    return o


A['C65-L4a'] = kursi_baris_c65([1, 1, 1, 1, 1])
A['C65-L4b'] = kursi_baris_c65([0, 1, 0, 0, 0])
A['C65-L4c'] = lantai() + bioskop(150) + papan_angka(150, 30, '休息', 80, 30, False, 18)
A['C65-L5a'] = lantai() + pohon(240, s=.8) + matahari(60, 40, 18) + orang(140, tinggi=150, jenis='wanita', baju='a', wajah='tawa', tangan=LAMBAI)
A['C65-L5b'] = lantai() + tv(80, 160, 90) + sofa(200) + orang(200, tinggi=140, jenis='wanita', baju='a', duduk=160, wajah='tawa')
A['C65-L5c'] = lantai() + meja_kantor(150) + orang(150, tinggi=150, jenis='wanita', baju='h')
A['C65-L6a'] = lantai() + resto(150) + papan_angka(150, 30, '休息', 80, 30, False, 18)
A['C65-L6b'] = pegang_perut(150, 'wanita', 160, 'a', 'lapar')
A['C65-L6c'] = lantai() + resto(170, w=140) + jam_kecil(260, 40, 12, 0, 20) + jalan_kaki(60, 'pria', 130, 'a', 'gugup') + jalan_kaki(100, 'wanita', 120, 'h', 'gugup')
A['C65-L8a'] = tas_c65()
A['C65-L8b'] = tas_c65(''.join(buku(124 + i * 19, 192, 16, 130, 'a' if i % 2 else 'h') for i in range(4)))
A['C65-L8c'] = lantai() + tas_tangan(150, 196, 1.6)
A['C65-L9'] = A['C65-5']
A['C65-L10'] = A['C65-4']
A['C65-T3a'] = lantai() + meja_belajar(150) + orang(150, tinggi=140, jenis='pria', baju='a', duduk=170) + buku(170, 120, 40, 14, 'a')
A['C65-T3b'] = lantai() + bola(200, 176, 18, 'sepak') + pelari(110, 'pria', 'a', 150) + matahari(250, 40, 16)
A['C65-T3c'] = tidur_c52('tidur', 10, True)
A['C65-T4a'] = lantai() + meja(150, 150, 240) + ''.join(piring(x, 144, 26, '') for x in (60, 110, 160, 210, 250)) + mangkuk_nasi_c45(110, 124, .5) + ikan_piring_c48(210, 140, .4)
A['C65-T4b'] = lantai() + koin_banyak(150, 150)
A['C65-T4c'] = lantai() + meja(150, 150, 160) + piring(150, 140, 60, bulat(150, 134, 8, 'a'))
A['C65-T6a'] = lantai() + kotak(80, 40, 140, 156, 'w', 2) + garis((80, 92), (220, 92), lebar=4) + garis((80, 144), (220, 144), lebar=4) + garis((80, 40), (80, 196), lebar=4) + garis((220, 40), (220, 196), lebar=4)
A['C65-T6b'] = lantai() + kotak(80, 40, 140, 156, 'w', 2) + garis((80, 92), (220, 92), lebar=4) + garis((80, 144), (220, 144), lebar=4) + garis((80, 40), (80, 196), lebar=4) + garis((220, 40), (220, 196), lebar=4) + ''.join(buku(88 + i * 16, y, 14, 46, 'a' if i % 2 else 'h') for y in (90, 142, 194) for i in range(8))
A['C65-T6c'] = lantai() + kotak(80, 40, 140, 156, 'w', 2) + garis((80, 92), (220, 92), lebar=4) + garis((80, 144), (220, 144), lebar=4) + garis((80, 40), (80, 196), lebar=4) + garis((220, 40), (220, 196), lebar=4) + buku(100, 142, 14, 46, 'a') + buku(118, 142, 14, 46, 'h')
A['C65-T7'] = lantai() + ''.join(orang(30 + i * 40, tinggi=140 - (i % 2) * 10, jenis='pria' if i % 2 else 'wanita', baju='a' if i % 3 else 'h') for i in range(7))
A['C65-T8'] = lantai() + gelas(110, 196, 'air', 1.8) + teko(220, 196, 1.2) + panah(190, 100, 140, 110, 3)

# --- C66 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def label_c66(nama, isi):
    return isi + papan_angka(150, 30, nama, 90, 30, False, 18)


def kelas_c66():
    return lantai() + papan_tulis(150, 30, 160, 70) + meja_kelas(90) + meja_kelas(210)


A['C66-L4a'] = A['C66-4']
A['C66-L4b'] = lantai() + resto(150)
A['C66-L4c'] = lantai() + rumah(150, 200, 180, 120)
A['C66-L5a'] = lantai() + buku(150, 190, 90, 130, 'a') + teks(150, 120, '中文', 26)
A['C66-L5b'] = lantai() + buku(90, 190, 80, 120, 'a') + teks(90, 126, '歷史', 22) + teks(150, 130, '+', 30, angka=True) + komputer(220, 196, 100)
A['C66-L5c'] = lantai() + buku(150, 190, 90, 130, 'a') + teks(150, 120, '法律', 26)
A['C66-L6a'] = label_c66('圖書館', lantai() + rak_buku(90, w=90, h=130) + rak_buku(210, w=90, h=130))
A['C66-L6b'] = kelas_c66()
A['C66-L6c'] = label_c66('宿舍', lantai() + gedung(150, tingkat=4, lebar=130)) + jalan_kaki(260, 'pria', 120, 'a')
A['C66-L8a'] = lantai() + toko(150)
A['C66-L8b'] = lantai() + pohon(40, s=.7) + gedung(110, tingkat=3, lebar=70) + gedung(200, tingkat=4, lebar=80) + pohon(270, s=.7) + papan_angka(150, 30, '大學', 80, 30, False, 18)
A['C66-L8c'] = lantai() + rumah(150, 200, 100, 70)
A['C66-L9'] = lantai_kamar() + jendela(230, 30, 60, 46) + bulan_bintang(230, 52, .4) + jam_dinding(70, 56, 26, 11, 0) + meja(150, 160, 160) + buku(150, 150, 50, 16, 'a') + orang(150, tinggi=130, jenis='pria', baju='a', duduk=190, wajah='lelah')
A['C66-L10'] = lantai() + kertas(150, 110, 120, 170) + ''.join(kotak(110, 60 + i * 34, 16, 16, 'w', 2) + garis((110, 60 + i * 34), (126, 60 + i * 34), lebar=2) + garis((136, 68 + i * 34), (200, 68 + i * 34), lebar=3) for i in range(4)) + centang(118, 66, .5) + centang(118, 134, .5)
A['C66-T3a'] = A['C66-L5c']
A['C66-T3b'] = A['C66-L5a']
A['C66-T3c'] = lantai() + buku(90, 190, 80, 120, 'a') + teks(90, 126, '中文', 22) + teks(150, 130, '+', 30, angka=True) + buku(210, 190, 80, 120, 'a') + teks(210, 126, '歷史', 22)
A['C66-T4a'] = label_c66('圖書館', lantai() + rak_buku(150, w=90, h=130)) + teks(30, 70, '1', 40, angka=True)
A['C66-T4b'] = label_c66('圖書館', lantai() + rak_buku(60, w=60, h=120) + rak_buku(140, w=60, h=120) + rak_buku(220, w=60, h=120)) + teks(30, 70, '3', 40, angka=True)
A['C66-T4c'] = label_c66('圖書館', lantai() + rak_buku(100, w=80, h=130) + rak_buku(200, w=80, h=130)) + teks(30, 70, '2', 40, angka=True)
A['C66-T6a'] = A['C66-1']
A['C66-T6b'] = lantai() + tiket(150, 110, 200, 90) + teks(110, 160, '票', 34)
A['C66-T6c'] = lantai() + kartu_kredit(150, 110, 1.5)
A['C66-T7'] = lantai() + pohon(40, s=.8) + pohon(100, s=.6) + gedung(180, tingkat=3, lebar=90) + pohon(260, s=.8) + papan_angka(180, 30, '大學', 80, 30, False, 18)
A['C66-T8'] = lantai() + kertas(80, 90, 80, 110) + teks(80, 100, 'A', 30, angka=True) + kertas(220, 90, 80, 110) + teks(220, 100, 'B', 30, angka=True) + panah(220, 190, 220, 160, 4) + centang(260, 50, .7)

# --- C67 tulis ulang 2026-11-17: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def bento_c67(x, y, s=1.0):
    return kotak(x - 50 * s, y - 30 * s, 100 * s, 60 * s, 'a', 6) + garis((x, y - 30 * s), (x, y + 30 * s), lebar=3) + garis((x - 50 * s, y), (x, y), lebar=3) + bulat(x + 25 * s, y, 14 * s, 'w')


def warna_c67(nama, k):
    return lantai() + kotak(100, 60, 100, 100, k, 8) + teks(150, 190, nama, 22)


A['C67-L4a'] = lantai() + cangkir(150, 196, 1.6, True, 'a') + teks(150, 60, '茶', 26)
A['C67-L4b'] = lantai() + cangkir_kopi(150, 196, 1.6)
A['C67-L4c'] = lantai() + bento_c67(150, 140, 1.2)
A['C67-L5a'] = lantai() + tv(200, 160, 110) + sofa(90, 200, 120) + orang(90, tinggi=140, jenis='pria', baju='a', duduk=166)
A['C67-L5b'] = tulis_laporan(150, 'pria', True)
A['C67-L5c'] = tidur_c52('tidur', 10, True)
A['C67-L6a'] = lantai() + jam_dinding(150, 100, 70, 8, 0)
A['C67-L6b'] = lantai() + jam_dinding(150, 100, 70, 6, 0)
A['C67-L6c'] = lantai() + jam_dinding(150, 100, 70, 7, 0)
A['C67-L8a'] = lantai() + sofa(150) + orang(150, tinggi=140, jenis='pria', baju='a', duduk=160)
A['C67-L8b'] = lantai() + jalan_kaki(150, 'pria', 160, 'a') + panah(200, 80, 270, 80, 4)
A['C67-L8c'] = lantai() + pintu(80, 200, 150, 70) + orang(190, tinggi=160, jenis='pria', baju='h', wajah='senyum') + bento_c67(230, 130, .4)
A['C67-L9'] = lantai() + pintu(70, 200, 150, 60) + kardus(170, 200, 90, 60) + orang(250, tinggi=150, jenis='wanita', baju='a', wajah='tawa') + centang(170, 110, .8)
A['C67-L10'] = A['C67-4']
A['C67-T3a'] = lantai() + jam_sektor(150, 95, 70, 59.9) + teks(150, 196, '60', 22, angka=True)
A['C67-T3b'] = lantai() + jam_sektor(150, 95, 70, 10) + teks(150, 196, '10', 22, angka=True)
A['C67-T3c'] = lantai() + jam_sektor(80, 95, 50, 59.9) + teks(150, 105, '+', 30, angka=True) + jam_sektor(220, 95, 50, 59.9) + teks(150, 196, '120', 22, angka=True)
A['C67-T4a'] = warna_c67('紅色', 'p')
A['C67-T4b'] = warna_c67('黑色', 'h')
A['C67-T4c'] = warna_c67('藍色', 'a')
A['C67-T6a'] = tulis_laporan(150, 'pria', False)
A['C67-T6b'] = tidur_c52('tidur', 11, True)
A['C67-T6c'] = lantai() + meja(170, 150, 160) + mangkuk_nasi_c45(170, 130, .7) + orang(70, tinggi=140, jenis='pria', baju='a', duduk=180, wajah='senyum')
A['C67-T7'] = lantai() + rumah(200, 200, 140, 110) + orang(70, tinggi=160, jenis='pria', baju='a', wajah='senyum')
A['C67-T8'] = A['C67-3']

