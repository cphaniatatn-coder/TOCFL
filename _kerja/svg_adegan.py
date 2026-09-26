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
