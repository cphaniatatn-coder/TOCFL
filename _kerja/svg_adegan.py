"""Komponen adegan bersama untuk ilustrasi soal (di atas svg_lib): pose tangan, ruang kelas, keluarga, kalender…"""
from svg_lib import *

TA = {'ki': [(18, -4), (2, -24)], 'ka': [(18, -4), (2, -24)]}   # dua tangan memegang kepala
LAMBAI = {'ka': [(14, -30), (6, -58)]}                            # melambai tangan kanan
ANGKAT = {'ka': [(6, -36), (2, -72)]}                             # mengangkat tangan kanan


def bingkai(x, y, w, h, isi):
    return kotak(x - w / 2 - 8, y - 8, w + 16, h + 16, 'h', 3) + kotak(x - w / 2, y, w, h, 'p') + isi


def lantai_kamar():
    return garis((16, 200), (284, 200)) + garis((16, 150), (60, 118), (240, 118), (284, 150), k='t') + garis((60, 118), (60, 20), k='t') + garis((240, 118), (240, 20), k='t')


def meja_kelas(x, y=200):
    return kotak(x - 36, y - 62, 72, 9, 'h') + garis((x - 30, y - 53), (x - 30, y)) + garis((x + 30, y - 53), (x + 30, y))


def murid_belakang(x, kaki=200, tinggi=120, jenis='laki'):
    """Murid duduk dilihat dari belakang (kepala + punggung)."""
    s_ = sendi(x, kaki, tinggi, jenis)
    r = s_['r']
    rambut = 'h'
    return (bentuk((x - r * 1.2, s_['bahu']), (x + r * 1.2, s_['bahu']), (x + r * 1.05, s_['bahu'] + r * 2.4), (x - r * 1.05, s_['bahu'] + r * 2.4), k='p')
            + bulat(x, s_['cy'], r, rambut))


def ruang_kelas(guru=True, murid=2, papan_x=110):
    o = lantai() + papan_tulis(papan_x, 18, 140, 56)
    if guru:
        o += orang(230, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(10, -10), (34, -40)]})
    for i in range(murid):
        mx = 70 + i * 90
        o += murid_belakang(mx, 200, 100, 'laki' if i % 2 == 0 else 'gadis') + meja_kelas(mx)
    return o


def bioskop(x, lantai_y=200):
    return (kotak(x - 70, lantai_y - 140, 140, 140, 'p') + kotak(x - 70, lantai_y - 150, 140, 14, 'h') + gulungan_film(x, lantai_y - 104, 24)
            + kotak(x - 24, lantai_y - 62, 48, 62, 'h'))


def dua_panel(kiri, kanan):
    return kiri + garis((150, 20), (150, 200), k='t') + kanan


def sinyal(x, y, arah=1):
    return jalur(f'M{f(x)} {f(y - 8)} q{f(8 * arah)} 8 0 16 M{f(x + 7 * arah)} {f(y - 15)} q{f(14 * arah)} 15 0 30', 'g')


def orang_ponsel(x, jenis='wanita', tinggi=150, wajah='senyum', baju='p', layar='h'):
    s_ = sendi(x, 200, tinggi, jenis)
    hx, hy = tangan_di(x, s_, 1, -6, -22)
    return orang(x, tinggi=tinggi, jenis=jenis, wajah=wajah, baju=baju, tangan={'ka': [(12, 16), (-6, -22)]}) + ponsel(hx + 4, hy - 4, .75, layar)


def jalan_kaki(x, jenis='pria', tinggi=150, baju='p', wajah='senyum'):
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, wajah=wajah, kaki_pose={'ki': (-18, 0), 'ka': (16, 0)},
                 tangan={'ki': [(14, 26), (26, 40)], 'ka': [(-2, 26), (-12, 44)]})


def tas_punggung(x, y, s=1.0):
    return kotak(x - 14 * s, y, 28 * s, 36 * s, 'h', 6 * s)



def keluarga(tunjuk):
    '''Foto keluarga: ayah, ibu (sanggul), kakak laki-laki, kakak perempuan (remaja), adik laki-laki kecil. Panah ke 'tunjuk'.'''
    org = {'ayah': (40, 170, 'pria', 'h', None), 'ibu': (95, 160, 'wanita', 'a', 'uban'), 'kakak_lk': (150, 150, 'pria', 'a', None),
           'kakak_pr': (205, 140, 'wanita', 'h', None), 'adik_lk': (258, 88, 'laki', 'p', None)}
    o = lantai()
    for k, (x, t, j, b, rb) in org.items():
        o += orang(x, tinggi=t, jenis=j, baju=b, rambut=rb)
    x, t = org[tunjuk][0], org[tunjuk][1]
    return o + panah(x, 200 - t - 34, x, 200 - t - 8, 5)


def kalender_senin(x, y, hari_ini, sorot, w=280):
    nama = '一二三四五六日'
    lw = w / 7
    o = kotak(x - w / 2, y, w, 70, 'p', 4) + kotak(x - w / 2, y, w, 24, 'h', 4)
    for i, n in enumerate(nama):
        cx = x - w / 2 + lw * (i + .5)
        o += teks(cx, y + 18, n, 15, warna='#fff')
        if i:
            o += garis((x - w / 2 + lw * i, y + 24), (x - w / 2 + lw * i, y + 70), k='t')
        if i == hari_ini:
            o += teks(cx, y + 54, '今天', 15)
        if i == sorot:
            o += bulat(cx, y + 48, 17, 't') + bulat(cx, y + 48, 21, 'g')
    return o


# ================= komponen tambahan (Volume 2) =================
def ring_basket(x, lantai_y=LANTAI):
    return (garis((x, lantai_y), (x, lantai_y - 150), lebar=6) + kotak(x - 34, lantai_y - 172, 44, 34, 'p')
            + kotak(x - 22, lantai_y - 156, 18, 12, 't') + jalur(f'M{f(x - 34)} {f(lantai_y - 142)} l-26 0', 'g', 4)
            + jalur(f'M{f(x - 60)} {f(lantai_y - 142)} l6 20 l14 0 l6 -20 M{f(x - 57)} {f(lantai_y - 132)} l20 0', 't'))


def tongkat_bisbol(x1, y1, x2, y2):
    return garis((x1, y1), (x2, y2), lebar=5) + garis(((x1 + x2 * 2) / 3, (y1 + y2 * 2) / 3), (x2, y2), lebar=10)


def gawang(x, lantai_y=LANTAI, w=110, h=70):
    o = garis((x - w / 2, lantai_y), (x - w / 2, lantai_y - h), (x + w / 2, lantai_y - h), (x + w / 2, lantai_y), lebar=5)
    for i in range(1, 6):
        o += garis((x - w / 2 + i * w / 6, lantai_y - h), (x - w / 2 + i * w / 6, lantai_y), k='t')
    for j in range(1, 4):
        o += garis((x - w / 2, lantai_y - j * h / 4), (x + w / 2, lantai_y - j * h / 4), k='t')
    return o


def podium(x, lantai_y=LANTAI):
    """Podium 2-1-3 (kiri-tengah-kanan). Kembalikan (svg, {juara: (x, y_atas)})."""
    o = kotak(x - 30, lantai_y - 70, 60, 70, 'p') + kotak(x - 90, lantai_y - 46, 60, 46, 'a') + kotak(x + 30, lantai_y - 30, 60, 30, 'a')
    o += teks(x, lantai_y - 30, '1', 26, angka=True) + teks(x - 60, lantai_y - 14, '2', 22, angka=True) + teks(x + 60, lantai_y - 6, '3', 20, angka=True)
    return o, {1: (x, lantai_y - 70), 2: (x - 60, lantai_y - 46), 3: (x + 60, lantai_y - 30)}


def headphone(x, cy, r):
    return (jalur(f'M{f(x - r * 1.05)} {f(cy)} A{f(r * 1.1)} {f(r * 1.1)} 0 0 1 {f(x + r * 1.05)} {f(cy)}', 'g', 4)
            + kotak(x - r * 1.3, cy - r * .35, r * .5, r * .8, 'h', 3) + kotak(x + r * .8, cy - r * .35, r * .5, r * .8, 'h', 3))


def tikar(x, y, w=190, h=46):
    o = bentuk((x - w / 2 + 20, y), (x + w / 2 - 20, y), (x + w / 2, y + h), (x - w / 2, y + h), k='p')
    for i in range(1, 6):
        o += garis((x - w / 2 + 20 + i * (w - 40) / 6, y), (x - w / 2 + i * w / 6, y + h), k='t')
    return o + garis((x - w / 2 + 10, y + h / 2), (x + w / 2 - 10, y + h / 2), k='t')


def keranjang(x, bawah, s=1.0):
    return (jalur(f'M{f(x - 26 * s)} {f(bawah - 30 * s)} Q{f(x)} {f(bawah - 64 * s)} {f(x + 26 * s)} {f(bawah - 30 * s)}', 'g', 4)
            + bentuk((x - 30 * s, bawah - 30 * s), (x + 30 * s, bawah - 30 * s), (x + 24 * s, bawah), (x - 24 * s, bawah), k='a')
            + ''.join(garis((x - 22 * s + i * 11 * s, bawah - 28 * s), (x - 20 * s + i * 10 * s, bawah - 2 * s), k='t') for i in range(5)))


def tiket(x, y, w=150, h=76):
    o = jalur(f'M{f(x - w / 2)} {f(y)} L{f(x + w / 2)} {f(y)} L{f(x + w / 2)} {f(y + h / 2 - 9)} A9 9 0 0 0 {f(x + w / 2)} {f(y + h / 2 + 9)} '
              f'L{f(x + w / 2)} {f(y + h)} L{f(x - w / 2)} {f(y + h)} L{f(x - w / 2)} {f(y + h / 2 + 9)} A9 9 0 0 0 {f(x - w / 2)} {f(y + h / 2 - 9)} Z', 'p')
    return o + garis((x + w / 4, y + 8), (x + w / 4, y + h - 8), k='t')


def kardus(x, bawah, w=70, h=56, k='a'):
    return (kotak(x - w / 2, bawah - h, w, h, k) + garis((x - w / 2, bawah - h + 12), (x + w / 2, bawah - h + 12), k='t')
            + kotak(x - 8, bawah - h, 16, h * .45, 'p'))


def penampang_rumah(x=150, lantai_y=LANTAI, w=230, h=150):
    """Rumah 2 lantai tampak potong: atap, lantai atas & bawah, tangga di kanan. Kembalikan (svg, y_lantai_atas)."""
    ya = lantai_y - h / 2
    o = bentuk((x - w / 2 - 10, lantai_y - h), (x, lantai_y - h - 40), (x + w / 2 + 10, lantai_y - h), k='h')
    o += kotak(x - w / 2, lantai_y - h, w, h, 'p') + kotak(x - w / 2, ya - 4, w, 8, 'h')
    tx = x + w / 2 - 50
    o += ''.join(garis((tx + i * 8, ya + 4 + i * 11), (tx + i * 8 + 8, ya + 4 + i * 11), k='t') for i in range(7))
    o += garis((tx, ya + 4), (tx + 56, lantai_y), k='t')
    return o, ya


def lemari_buku(x, bawah, w=60, h=70):
    o = kotak(x - w / 2, bawah - h, w, h, 'p')
    for j in range(3):
        y = bawah - h + 4 + j * (h / 3)
        o += garis((x - w / 2, y + h / 3 - 4), (x + w / 2, y + h / 3 - 4), k='g')
        o += ''.join(kotak(x - w / 2 + 5 + i * 9, y + 4, 7, h / 3 - 12, 'h' if (i + j) % 2 else 'a', 1) for i in range(5))
    return o


def kloset(x, bawah, s=1.0):
    return (kotak(x + 4 * s, bawah - 52 * s, 20 * s, 30 * s, 'p', 3)
            + jalur(f'M{f(x - 26 * s)} {f(bawah - 24 * s)} L{f(x + 24 * s)} {f(bawah - 24 * s)} Q{f(x + 22 * s)} {f(bawah - 6 * s)} {f(x + 6 * s)} {f(bawah - 4 * s)} '
                    f'L{f(x + 6 * s)} {f(bawah)} L{f(x - 12 * s)} {f(bawah)} L{f(x - 12 * s)} {f(bawah - 6 * s)} Q{f(x - 26 * s)} {f(bawah - 10 * s)} {f(x - 26 * s)} {f(bawah - 24 * s)} Z', 'p'))


def jendela_buka(x, y, w=90, h=70):
    return (kotak(x - w / 2, y, w, h, 'a') + bentuk((x - w / 2, y), (x - w / 2 - 24, y + 10), (x - w / 2 - 24, y + h - 10), (x - w / 2, y + h), k='p')
            + bentuk((x + w / 2, y), (x + w / 2 + 24, y + 10), (x + w / 2 + 24, y + h - 10), (x + w / 2, y + h), k='p')
            + awan(x, y + h / 2 - 4, .35, 'p'))


def lampu(x, y, nyala=True, pj=50):
    o = garis((x, y - pj), (x, y - 14)) + jalur(f'M{f(x - 30)} {f(y)} Q{f(x)} {f(y - 30)} {f(x + 30)} {f(y)} Z', 'h') + bulat(x, y + 6, 9, 'p')
    if nyala:
        for a in (20, 55, 90, 125, 160):
            r = math.radians(a)
            o += garis((x + math.cos(r) * 24, y + 8 + math.sin(r) * 24), (x + math.cos(r) * 40, y + 8 + math.sin(r) * 40), lebar=2.4)
    return o


def ac(x, y, nyala=True, rusak=False, w=130):
    o = kotak(x - w / 2, y, w, 40, 'p', 8) + garis((x - w / 2 + 10, y + 30), (x + w / 2 - 10, y + 30), k='t') + bulat(x + w / 2 - 14, y + 12, 3, 'h')
    if nyala and not rusak:
        o += jalur(f'M{f(x - 40)} {f(y + 52)} q10 14 0 28 M{f(x)} {f(y + 52)} q10 14 0 28 M{f(x + 40)} {f(y + 52)} q10 14 0 28', 'g')
        o += salju(x - 20, y + 96, 7) + salju(x + 24, y + 102, 6)
    if rusak:
        o += awan(x + 20, y - 22, .35, 'a') + awan(x - 26, y - 34, .28, 'a') + silang(x, y + 70, 16, 6)
    return o


def tv_retak(x, bawah, lebar=140):
    return tv(x, bawah, lebar) + jalur(f'M{f(x - 10)} {f(bawah - 70)} l14 12 l-10 10 l18 14 M{f(x + 4)} {f(bawah - 58)} l20 -10 M{f(x + 8)} {f(bawah - 36)} l-22 8', 'w')


def baskom_cuci(x, bawah):
    return (bentuk((x - 50, bawah - 34), (x + 50, bawah - 34), (x + 40, bawah), (x - 40, bawah), k='a') + elips(x, bawah - 34, 50, 8, 'p')
            + kaos(x - 14, bawah - 44, .35, 'p') + jalur(f'M{f(x - 44)} {f(bawah - 40)} q6 -8 12 0 M{f(x + 26)} {f(bawah - 42)} q6 -8 12 0', 't'))


def pancuran(x, y):
    return (garis((x + 40, y - 30), (x + 40, y - 50), (x, y - 50), (x, y - 38), lebar=5)
            + jalur(f'M{f(x - 20)} {f(y - 38)} L{f(x + 20)} {f(y - 38)} L{f(x + 12)} {f(y - 28)} L{f(x - 12)} {f(y - 28)} Z', 'h')
            + ''.join(garis((x - 10 + i * 5, y - 22), (x - 16 + i * 8, y + 10), lebar=2) for i in range(5)))


def jam_sektor(x, y, r, menit):
    """Jam dengan sektor abu dari angka 12 sampai 'menit' (menunjukkan lamanya)."""
    a = math.radians(menit * 6)
    besar = 1 if menit > 30 else 0
    return (bulat(x, y, r, 'p') + jalur(f'M{f(x)} {f(y)} L{f(x)} {f(y - r * .88)} A{f(r * .88)} {f(r * .88)} 0 {besar} 1 {f(x + math.sin(a) * r * .88)} {f(y - math.cos(a) * r * .88)} Z', 'a')
            + ''.join(garis((x + math.sin(math.radians(i * 30)) * r * .74, y - math.cos(math.radians(i * 30)) * r * .74),
                            (x + math.sin(math.radians(i * 30)) * r * .88, y - math.cos(math.radians(i * 30)) * r * .88), lebar=4 if i % 3 == 0 else 2.2) for i in range(12))
            + garis((x, y), (x + math.sin(a) * r * .8, y - math.cos(a) * r * .8), lebar=r * .06) + bulat(x, y, r * .06, 'h'))


def tas_kerja(x, bawah, s=1.0):
    return (kotak(x - 30 * s, bawah - 40 * s, 60 * s, 40 * s, 'h', 5) + jalur(f'M{f(x - 12 * s)} {f(bawah - 40 * s)} l0 {f(-8 * s)} l{f(24 * s)} 0 l0 {f(8 * s)}', 'g')
            + garis((x - 30 * s, bawah - 26 * s), (x + 30 * s, bawah - 26 * s), k='w'))


def gelembung_pikiran(x, y, w, h, isi, ekor_x=None, ekor_y=None):
    ex = x - w * .3 if ekor_x is None else ekor_x
    ey = y + h / 2 if ekor_y is None else ekor_y
    return elips(x, y, w / 2, h / 2, 'p') + bulat(ex, ey + 12, 7) + bulat(ex - 8, ey + 28, 4.5) + isi


def kucing(x, bawah, s=1.0, k='p'):
    mata = 'h' if k != 'h' else 'n'
    return (elips(x, bawah - 22 * s, 30 * s, 20 * s, k) + bulat(x + 30 * s, bawah - 44 * s, 16 * s, k)
            + bentuk((x + 18 * s, bawah - 54 * s), (x + 20 * s, bawah - 70 * s), (x + 30 * s, bawah - 58 * s), k=k)
            + bentuk((x + 32 * s, bawah - 58 * s), (x + 42 * s, bawah - 70 * s), (x + 44 * s, bawah - 54 * s), k=k)
            + jalur(f'M{f(x - 28 * s)} {f(bawah - 26 * s)} q{f(-22 * s)} {f(-10 * s)} {f(-14 * s)} {f(-34 * s)}', 'g', 5 * s)
            + bulat(x + 25 * s, bawah - 46 * s, 2.2 * s, mata) + bulat(x + 36 * s, bawah - 46 * s, 2.2 * s, mata)
            + garis((x - 16 * s, bawah - 6 * s), (x - 16 * s, bawah), lebar=5 * s) + garis((x + 16 * s, bawah - 6 * s), (x + 16 * s, bawah), lebar=5 * s))


def anjing(x, bawah, s=1.0, k='p'):
    return (kotak(x - 40 * s, bawah - 50 * s, 70 * s, 30 * s, k, 14 * s) + bulat(x + 34 * s, bawah - 62 * s, 18 * s, k)
            + elips(x + 50 * s, bawah - 56 * s, 12 * s, 8 * s, k) + bulat(x + 60 * s, bawah - 58 * s, 3.5 * s, 'h')
            + jalur(f'M{f(x + 22 * s)} {f(bawah - 74 * s)} q{f(-14 * s)} {f(4 * s)} {f(-10 * s)} {f(28 * s)} q{f(8 * s)} {f(-4 * s)} {f(12 * s)} {f(-18 * s)} Z', 'h')
            + bulat(x + 36 * s, bawah - 66 * s, 2.4 * s, 'h')
            + ''.join(garis((x + dx * s, bawah - 22 * s), (x + dx * s, bawah), lebar=6 * s) for dx in (-32, -18, 12, 24))
            + jalur(f'M{f(x - 40 * s)} {f(bawah - 44 * s)} q{f(-14 * s)} {f(-6 * s)} {f(-10 * s)} {f(-24 * s)}', 'g', 5 * s))


def meja_kantor(x, lantai_y=LANTAI):
    return meja(x, lantai_y - 70, 150) + komputer(x + 10, lantai_y - 70, 70)


def orang_duduk_kerja(x, jenis='pria', baju='a'):
    return kursi_depan(x, 150) + orang(x, tinggi=150, jenis=jenis, duduk=150, baju=baju, tangan={'ki': [(20, 6), (44, 2)], 'ka': [(-2, 20), (18, 30)]})


def titik_obrolan(x, y, w=60, h=38, ekor=(-1, 1)):
    return gelembung(x, y, w, h, bulat(x - 14, y, 3.5, 'h') + bulat(x, y, 3.5, 'h') + bulat(x + 14, y, 3.5, 'h'), ekor)
