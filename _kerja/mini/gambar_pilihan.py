"""Ilustrasi pilihan bergambar (聽力 Part 2–3, 閱讀 Part 1) & gambar soal 閱讀 Part 2–3 tes awal/akhir modul mini.

Kunci: T<level><paket>-<no><a|b|c> = pilihan A/B/C → option.img; T<level><paket>-<no> = gambar soal → picture.img
(dipasang otomatis oleh buat_mini.py bila file img/soal/<kunci>.svg ada). Dipakai gambar_tes.py.
Gaya sama dengan 聽力 Part 1: garis hitam, isian hitam/putih/abu, kanvas 300×220.
"""
from svg_adegan import *

P = {}


# ---------- komponen bersama ----------
def tiang(x, y): return garis((x, y), (x, LANTAI), lebar=4)
def bendera_jepang(x, y, w=110, h=74): return kotak(x, y, w, h, 'p') + bulat(x + w / 2, y + h / 2, h * .3, 'a') + tiang(x, y)
def bendera_indonesia(x, y, w=110, h=74): return kotak(x, y, w, h / 2, 'a') + kotak(x, y + h / 2, w, h / 2, 'p') + tiang(x, y)
BENDERA = {'jp': bendera_jepang, 'tw': bendera_taiwan, 'id': bendera_indonesia}

def orang_bendera(jenis, b):
    return lantai() + orang(80, tinggi=165, jenis=jenis, baju='a') + BENDERA[b](160, 36, 110, 74)

def harga(benda, angka): return benda + label_harga(214, 64, angka, 150, 64)

def jam(h, m): return jam_dinding(150, 110, 88, h, m)

TINGGI = {'pria': 172, 'wanita': 158, 'laki': 112, 'gadis': 104}
def barisan(jenis, label=None, x1=40, x2=260, tinggi=None):
    """Orang berjajar di lantai; label = teks di bawah tiap orang."""
    n = len(jenis); o = lantai()
    for i, j in enumerate(jenis):
        x = (x1 + x2) / 2 if n == 1 else x1 + (x2 - x1) * i / (n - 1)
        o += orang(x, tinggi=(tinggi or TINGGI)[i] if isinstance(tinggi, list) else TINGGI[j], jenis=j, baju='hap'[i % 3])
        if label: o += teks(x, 218, label[i], 20)
    return o

def peluk(): return {'ki': [(-8, 22), (-26, 14)], 'ka': [(-8, 22), (-26, 14)]}   # tangan menyilang di dada (kedinginan)

def panas(x=170, jenis='pria'):
    return (lantai() + matahari(60, 50, 26, 'h') + orang(x, tinggi=160, jenis=jenis, baju='p', wajah='lelah', tangan={'ka': [(14, -6), (10, -26)]})
            + keringat(x - 25, 44) + keringat(x + 25, 52) + keringat(x - 20, 92, .8))

def dingin_angin(x=190, jenis='pria'):
    return (lantai() + angin(24, 52, 1.1) + angin(30, 118, .8) + daun(120, 40) + daun(96, 150, .8)
            + orang(x, tinggi=160, jenis=jenis, baju='a', wajah='gugup', tangan=peluk()))

def hujan_deras():
    return lantai() + awan(110, 40, 1.4, 'a') + awan(210, 50, 1.2, 'a') + hujan(150, 70, 250, 110, 18)

def hujan_dingin(jenis='pria'):
    return (lantai() + awan(150, 34, 1.6, 'a') + hujan(150, 60, 250, 40, 14)
            + orang(150, tinggi=135, jenis=jenis, baju='a', wajah='gugup', tangan=peluk()) + hujan(60, 120, 60, 60, 5) + hujan(240, 120, 60, 60, 5))

def cerah(): return lantai() + matahari(150, 80, 40, 'p') + pohon(50, s=.8) + pohon(250, s=.8)

def berangin_cerah(): return lantai() + matahari(56, 44, 22, 'p') + angin(40, 96, 1.2) + angin(54, 146, .9) + daun(196, 92) + daun(206, 150, .8) + pohon(252, s=.75)

def anak(jenis): return barisan(jenis, tinggi=[120 if j == 'laki' else 112 for j in jenis], x1=70 if len(jenis) == 2 else 40, x2=230 if len(jenis) == 2 else 260)

def keluarga_n(n):
    j = ['pria', 'wanita', 'laki', 'gadis', 'gadis', 'laki'][:n]
    return barisan(j, x1=34, x2=266)


def pegang(x, jenis, bagian, wajah='sakit'):
    """Orang memegang kepala / perut / lutut (sakit). Titik tangan ditulis absolut lalu diubah ke format orang()."""
    t = 168
    s_ = sendi(x, tinggi=t, jenis=jenis)
    bx, by, r = s_['lb'] / 2, s_['bahu'] + 3, s_['r']
    rel = lambda sisi, ax, ay: (sisi * (ax - (x + sisi * bx)), ay - by)
    if bagian == 'kepala':
        ki = [(x - bx - 14, by - 8), (x - r * 1.05, s_['cy'])]; ka = [(x + bx + 14, by - 8), (x + r * 1.05, s_['cy'])]
        tambah = jalur(f'M{x - 40} {s_["cy"] - 30} l-8 -8 M{x + 40} {s_["cy"] - 30} l8 -8 M{x} {s_["cy"] - r - 14} l0 -10', 'g')
    elif bagian == 'perut':
        py_ = s_['pinggang'] - 8
        ki = [(x - bx - 12, py_ - 22), (x - 7, py_)]; ka = [(x + bx + 12, py_ - 22), (x + 7, py_)]
        tambah = (bulat(x - 7, py_, 5, 'h') + bulat(x + 7, py_, 5, 'h')
                  + jalur(f'M{x - 48} {py_} l-10 0 M{x + 48} {py_} l10 0 M{x - 44} {py_ - 16} l-8 -6 M{x + 44} {py_ - 16} l8 -6', 'g'))
    else:   # lutut kanan
        kx, ky = x + r * .55, (s_['pinggang'] + LANTAI) / 2
        ki = [(x - bx + 2, by + 30), (kx - 6, ky)]; ka = [(x + bx + 18, by + 34), (kx + 8, ky + 4)]
        tambah = (bulat(kx - 6, ky, 5, 'h') + bulat(kx + 8, ky + 4, 5, 'h')
                  + jalur(f'M{kx + 22} {ky - 10} l12 -6 M{kx + 24} {ky + 4} l14 0 M{kx + 22} {ky + 16} l12 6', 'g'))
    tangan = {'ki': [rel(-1, *p_) for p_ in ki], 'ka': [rel(1, *p_) for p_ in ka]}
    return lantai() + orang(x, tinggi=t, jenis=jenis, baju='p', wajah=wajah, tangan=tangan) + tambah


def rute(belok, simpang):
    """Peta tampak atas: jalan utama vertikal + 2 persimpangan; panah dari bawah, belok di simpang ke-1/2."""
    ys = {1: 146, 2: 70}
    o = kotak(126, 8, 48, 204, 'a') + kotak(16, ys[1] - 20, 268, 40, 'a') + kotak(16, ys[2] - 20, 268, 40, 'a')
    o += bulat(150, 204, 7, 'h')                      # posisi awal
    y = ys[simpang]
    ujung = 40 if belok == 'kiri' else 260
    return o + garis((150, 200), (150, y), lebar=8) + panah(150, y, ujung, y, 8)


def papan(x, y, isi, w=70, uk=17): return kotak(x - w / 2, y - 14, w, 28, 'p', 4) + teks(x, y + 6, isi, uk)

def skala(isi, x, y, k): return f'<g transform="translate({x} {y}) scale({k}) translate({-x} {-y})">{isi}</g>'

def peta_stasiun(letak):
    """Jalan vertikal dari posisi kita (titik bawah); 銀行 & 車站: stasiun sesudah / sebelum bank / jauh (perlu bus)."""
    o = kotak(130, 8, 40, 204, 'a') + bulat(150, 204, 7, 'h')
    if letak == 'jauh':
        o += ''.join(garis((150, 190 - i * 20), (150, 180 - i * 20), k='w') for i in range(9))
        o += kotak(184, 150, 64, 44, 'p') + papan(216, 140, '銀行') + kotak(46, 30, 64, 40, 'p') + papan(78, 22, '車站')
        return o + skala(bus(150, 200, 170), 70, 190, .42) + teks(78, 110, '⋮', 34, angka=True)
    o += kotak(184, 96, 70, 46, 'p') + papan(219, 86, '銀行')
    ys = 34 if letak == 'sesudah' else 150
    o += kotak(46, ys, 70, 44, 'p') + papan(81, ys - 10, '車站')
    return o + garis((150, 200), (150, ys + 24), lebar=6) + panah(150, ys + 24, 120, ys + 24, 6)


def baca_perpus():
    return (lantai() + rak_buku(235, 200, 100, 170) + kursi_depan(110, 140) + orang(110, tinggi=150, jenis='wanita', duduk=140, baju='a',
            tangan={'ki': [(4, 30), (-10, 20)], 'ka': [(4, 30), (-10, 20)]}) + buku(110, 140, 46, 30, 'h'))

def nonton_tv():
    return (lantai() + sofa(95, 200, 140) + orang(95, tinggi=140, jenis='wanita', duduk=152, baju='a') + meja(235, 150, 80) + tv(235, 150, 90))

def makan_restoran():
    return (lantai() + lampion(60, 40, .8) + lampion(240, 40, .8) + orang(150, tinggi=150, jenis='wanita', duduk=150, baju='a',
            tangan={'ka': [(10, 20), (0, -4)]}) + meja(150, 140, 190) + mangkuk_mi(196, 111, .38))

def lari_taman(jenis='pria'):
    return (lantai() + pohon(50, s=.85) + pohon(255, s=.7) + bunga(210, 176, .8)
            + orang(150, tinggi=160, jenis=jenis, baju='a', kaki_pose={'ki': (-34, -8), 'ka': (28, 0)},
                    tangan={'ki': [(14, 18), (34, 4)], 'ka': [(-4, 26), (-22, 38)]}))

def renang(jenis='pria'):
    o = kotak(16, 120, 268, 84, 'a') + ''.join(jalur(f'M{24 + i * 46} {136 + (i % 2) * 22} q11 -8 22 0 t22 0', 'w') for i in range(6))
    o += bulat(140, 112, 18) + muka(140, 112, 18, 'senyum') + jalur('M122 108 Q124 88 140 89 Q156 88 158 108 Q148 98 122 108 Z', 'h')
    return o + jalur('M164 122 Q184 70 214 96', 'g', 7) + jalur('M112 124 l-26 6', 'g', 7)

def tidur_rumah(jenis='pria'):
    return (lantai() + jendela(240, 40, 60, 50) + bulan_bintang(240, 60, .5) + ranjang(140, 200, 220)
            + bulat(62, 132, 15) + muka(62, 132, 15, 'tidur') + jalur('M47 127 q2 -20 16 -20 q14 0 15 16', 'h')
            + kotak(78, 132, 160, 18, 'p', 6) + teks(98, 104, 'z z', 20, angka=True))


def sepatu_sempit():
    return (lantai() + kursi_depan(100, 140) + orang(100, tinggi=150, jenis='pria', duduk=140, baju='a', wajah='sakit',
            tangan={'ka': [(20, 6), (60, -24)]}) + sepatu(196, 112, .42, 'h') + elips(78, 198, 16, 6, 'p') + elips(122, 198, 16, 6, 'p')
            + jalur('M214 84 l8 -8 M220 98 l10 -2', 'g') + teks(196, 70, '?', 26, angka=True))

def sepatu_besar():
    return (lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='kaget', kaki_pose={'ki': (-26, 0), 'ka': (26, 0)})
            + sepatu(112, 200, 1.05, 'h') + sepatu(196, 200, 1.05, 'h'))

def pilih_kemeja():
    return (lantai() + garis((200, 40), (290, 40), lebar=4) + kaos(220, 100, .45, 'a') + kaos(268, 100, .45, 'p')
            + orang(100, tinggi=165, jenis='pria', baju='p', tangan={'ka': [(26, 0), (62, -16)]}) + kaos(170, 82, .5, 'h'))

def baju_besar():
    s_ = sendi(150, tinggi=165, jenis='wanita')
    return (lantai() + orang(150, tinggi=165, jenis='wanita', baju='p', wajah='kaget', tangan={'ki': [(30, 50)], 'ka': [(30, 50)]})
            + kaos(150, s_['bahu'] + 52, 1.25, 'a'))

def baju_kecil():
    s_ = sendi(150, tinggi=165, jenis='wanita')
    return (lantai() + orang(150, tinggi=165, jenis='wanita', baju='p', wajah='sedih') + kaos(150, s_['bahu'] + 14, .5, 'a'))

def coba_celana():
    return (lantai() + orang(100, tinggi=165, jenis='wanita', baju='a', tangan={'ka': [(26, 0), (60, -10)]})
            + bentuk((160, 70), (214, 70), (220, 168), (196, 168), (187, 100), (178, 168), (154, 168), k='p') + garis((160, 80), (214, 80), k='t'))


def pantai():
    return (matahari(240, 44, 22, 'p') + kotak(16, 104, 268, 50, 'a') + ''.join(jalur(f'M{26 + i * 44} {118 + (i % 2) * 18} q11 -8 22 0 t22 0', 'w') for i in range(6))
            + jalur('M16 154 Q150 140 284 154 L284 204 L16 204 Z', 'p') + payung(90, 132, 52)
            + bentuk((176, 186), (230, 186), (226, 196), (180, 196), k='a'))

def gunung_(): return lantai() + gunung(150, 200, 250, 160) + pohon(40, s=.6) + pohon(266, s=.55)
def bioskop_(): return lantai() + bioskop(150, 200) + orang(60, tinggi=120, jenis='wanita', baju='a') + orang(240, tinggi=124, jenis='pria', baju='h')

def anak_anjing(): return lantai() + anjing(140, 196, 1.45)

def kue(): return lantai() + meja(150, 150, 200) + kue_ultah(150, 150, '', 1.2) + ''.join(kotak(122 + i * 22, 70, 6, 22, 'p') + jalur(f'M{125 + i * 22} 70 q-4 -6 0 -12 q4 6 0 12', 'h') for i in range(3))

def buket():
    o = ''.join(bunga(x, y, 1.6) for x, y in ((120, 70), (150, 52), (180, 70), (135, 92), (167, 92)))
    return o + bentuk((108, 104), (192, 104), (156, 196), (144, 196), k='a') + garis((122, 130), (178, 130), k='t')


def ruang_sofa(sisi):
    o = lantai(200) + garis((16, 30), (284, 30), k='t')
    if sisi == 'jendela': o += jendela(195, 54, 100, 70) + sofa(195, 200, 150) + tv(50, 200, 60)
    elif sisi == 'kamar': o += ranjang(90, 200, 150) + sofa(230, 200, 90)
    else: o += pintu(240, 200, 150, 64) + sofa(115, 200, 150)
    return o

def kamar(besar, jendela_=True):
    if besar:
        o = kotak(14, 18, 272, 190, 'p') + ranjang(110, 200, 120)
        if jendela_: o += jendela(214, 76, 100, 80)
    else:
        o = kotak(86, 36, 128, 172, 'p') + ranjang(150, 200, 118)
        if jendela_: o += jendela(150, 76, 100, 80)
    return o

def buku_di(tempat):
    if tempat == 'rak': return lantai() + rak_buku(150, 200, 130, 170)
    if tempat == 'meja': return lantai() + meja(150, 140, 190) + buku_tumpuk(150, 140, 3, 70, 22) + kursi(260, 200, 1, .8)
    return lantai() + ranjang(150, 200, 230) + buku_tumpuk(160, 148, 3, 64, 20)

def dua_kaos(angka): return harga(kaos(54, 110, .55, 'a') + kaos(108, 120, .55, 'p'), angka)
def dua_sepatu(angka): return harga(lantai() + sepatu(66, 118, .9, 'h') + sepatu(90, 126, .9, 'h') + sepatu(66, 176, .9, 'p') + sepatu(90, 184, .9, 'p'), angka)


def obat(isi):
    if isi == 'adik':
        return (lantai() + orang(150, tinggi=118, jenis='laki', baju='a', wajah='senyum', kaki_pose={'ki': (-16, 0), 'ka': (14, 0)},
                tangan={'ka': [(16, 6), (34, -14)]}) + botol_obat(206, 98, .6))
    if isi == 'meja': return lantai() + meja(150, 140, 190) + botol_obat(150, 140, 1.0)
    tong = bentuk((166, 120), (250, 120), (240, 200), (176, 200), k='a') + kotak(160, 112, 96, 10, 'h', 3)
    return lantai() + tong + f'<g transform="rotate(40 150 70)">{botol_obat(150, 90, .6)}</g>' + jalur('M100 50 q20 -10 34 6 M96 76 q16 -6 28 4', 'g') + panah(176, 92, 198, 116, 4)


def kantong(x, y, s=1.0): return jalur(f'M{x - 20 * s} {y} Q{x - 26 * s} {y + 40 * s} {x} {y + 42 * s} Q{x + 26 * s} {y + 40 * s} {x + 20 * s} {y} L{x + 8 * s} {y - 4 * s} L{x + 4 * s} {y - 14 * s} L{x - 4 * s} {y - 4 * s} Z', 'h')
def tong_sampah(x, s=1.0): return bentuk((x - 26 * s, LANTAI - 60 * s), (x + 26 * s, LANTAI - 60 * s), (x + 20 * s, LANTAI), (x - 20 * s, LANTAI), k='a') + kotak(x - 30 * s, LANTAI - 68 * s, 60 * s, 9 * s, 'h', 3)

def buang_sampah(isi):
    if isi == 'keluar':
        return (lantai() + kotak(16, 40, 90, 160, 'p') + pintu(60, 200, 130, 56, buka=True) + pohon(272, s=.55)
                + orang(160, tinggi=150, jenis='pria', baju='a', kaki_pose={'ki': (-16, 0), 'ka': (16, 0)}, tangan={'ka': [(16, 30), (24, 44)]}) + kantong(196, 128, .9) + panah(200, 196, 240, 196, 4))
    if isi == 'dapur':
        return lantai() + kompor(64, 130, 96) + api(52, 128, .4) + tong_sampah(220) + orang(150, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(20, 20), (40, 26)]}) + kantong(214, 100, .6)
    return (lantai() + meja(170, 140, 190) + orang(70, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(30, 14), (64, 22)]})
            + kotak(122, 128, 40, 12, 'a', 3) + jalur('M170 120 q10 -10 20 0 M196 116 q10 -10 20 0', 'g'))


def sepeda_(isi):
    if isi == 'kakak': return lantai() + pengendara_sepeda(150, 'pria', 'a', 150) + jalur('M40 120 l30 0 M30 140 l40 0 M44 160 l26 0', 'g')
    if isi == 'pencuri':
        s_ = sendi(80, tinggi=160, jenis='pria')
        return (lantai() + sepeda(190, 200, 1.0) + orang(80, tinggi=160, jenis='pria', baju='h', wajah='marah', tangan={'ka': [(30, 30), (66, 40)]})
                + kotak(80 - s_['r'] * 1.05, s_['cy'] - s_['r'] * .38, s_['r'] * 2.1, s_['r'] * .6, 'h', 3))
    return (lantai() + sepeda(190, 200, 1.0) + bulat(234, 176, 28, 'n') + f'<g transform="rotate(30 236 178)">{elips(236, 178, 26, 12, "g")}</g>'
            + jalur('M262 150 l8 -8 M268 168 l12 -2 M206 146 l-6 -8', 'g') + orang(70, tinggi=160, jenis='pria', baju='a', wajah='sedih'))


def jendela_aksi(aksi):
    """tutup = daun jendela terbuka lebar + panah ke bingkai; buka = baru sedikit terbuka + panah keluar; bersih = lap & busa."""
    o = lantai() + kotak(150, 40, 120, 96, 'a') + kotak(146, 36, 128, 104, 't') + kotak(210, 40, 60, 96, 'p')
    if aksi == 'tutup':
        o += bentuk((150, 40), (108, 56), (108, 120), (150, 136), k='p') + panah(116, 88, 146, 88, 5)
        tg = {'ka': [(20, -16), (38, -34)]}
    elif aksi == 'buka':
        o += bentuk((150, 40), (136, 50), (136, 126), (150, 136), k='p') + panah(132, 88, 104, 88, 5)
        tg = {'ka': [(22, -10), (42, -30)]}
    else:
        o += kotak(150, 40, 60, 96, 'p') + ''.join(bulat(x, y, r, 't') for x, y, r in ((176, 60, 6), (190, 74, 4), (234, 66, 5), (248, 96, 4)))
        tg = {'ka': [(26, -20), (52, -46)]}
    o += orang(70, tinggi=160, jenis='wanita', baju='a', tangan=tg)
    if aksi == 'bersih': o += kotak(152, 46, 22, 16, 'h', 3)
    return o


# ---------- A0 ----------
for k, b in zip('abc', ['650', '560', '605']): P[f'TA0A-5{k}'] = harga(lantai() + kaos(80, 128, .9, 'a'), b)
for k, b in zip('abc', ['jp', 'tw', 'id']): P[f'TA0A-6{k}'] = orang_bendera('wanita', b)
P['TA0A-7a'] = lantai() + ranjang(150, 200, 220) + kotak(150, 136, 40, 12, 'h', 3)
P['TA0A-7b'] = lantai() + ranjang(150, 200, 220) + kotak(150, 186, 40, 12, 'h', 3)
P['TA0A-7c'] = lantai() + meja(150, 130, 190) + kotak(130, 118, 40, 12, 'h', 3) + kursi(260, 200, 1, .8)
for k, (h, m) in zip('abc', [(6, 0), (8, 0), (11, 0)]): P[f'TA0A-8{k}'] = jam(h, m)
for k, n in zip('abc', [4, 5, 6]): P[f'TA0A-9{k}'] = keluarga_n(n)
P['TA0A-11a'] = dingin_angin(); P['TA0A-11b'] = panas(); P['TA0A-11c'] = hujan_deras()
P['TA0A-12a'] = barisan(['pria', 'pria'], ['哥哥', '我'], 100, 200, [182, 120])
P['TA0A-12b'] = barisan(['pria', 'pria'], ['哥哥', '我'], 100, 200, [160, 160])
P['TA0A-12c'] = barisan(['pria', 'pria'], ['哥哥', '我'], 100, 200, [120, 182])
P['TA0A-13'] = (lantai() + jam_dinding(240, 52, 34, 7, 0) + jendela(80, 30, 80, 60) + matahari(80, 66, 14, 'p')
                + orang(150, tinggi=120, jenis='gadis', duduk=150, baju='a', tangan={'ka': [(10, 18), (4, 0)]}) + meja(150, 140, 170) + mangkuk_mi(196, 113, .35))
P['TA0A-14'] = lantai() + ranjang(110, 200, 180) + meja(250, 150, 64) + tv(250, 150, 80)
P['TA0A-15'] = lantai() + roti(90, 190, 1.0) + label_harga(214, 90, '50', 120, 60)
P['TA0A-16'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='a', wajah='tawa', tangan={'ka': [(20, -30), (30, -60)]}) + gelembung(210, 60, 120, 60, teks(210, 70, '你好！', 26), (-1, 1))
for k, b in zip('abc', ['85', '58', '805']): P[f'TA0B-5{k}'] = harga(lantai() + cangkir(80, 196, 1.3), b)
for k, b in zip('abc', ['tw', 'jp', 'id']): P[f'TA0B-6{k}'] = orang_bendera('pria', b)
P['TA0B-7a'] = lantai() + kursi(150, 200, 1, 1.3) + buku(140, 122, 44, 34, 'h')
P['TA0B-7b'] = lantai() + kursi(150, 200, 1, 1.3) + kotak(118, 186, 50, 14, 'h', 2)
P['TA0B-7c'] = lantai() + meja(150, 130, 190) + buku(150, 130, 44, 34, 'h') + kursi(262, 200, 1, .8)
for k, (h, m) in zip('abc', [(7, 30), (8, 0), (9, 0)]): P[f'TA0B-8{k}'] = jam(h, m)
P['TA0B-9a'] = anak(['laki', 'gadis']); P['TA0B-9b'] = anak(['laki', 'laki', 'gadis']); P['TA0B-9c'] = anak(['laki', 'laki', 'gadis', 'laki'])
P['TA0B-11a'] = hujan_dingin(); P['TA0B-11b'] = panas(); P['TA0B-11c'] = berangin_cerah()
P['TA0B-12a'] = anak(['laki', 'laki', 'gadis']); P['TA0B-12b'] = anak(['laki', 'gadis', 'gadis']); P['TA0B-12c'] = anak(['laki', 'laki', 'laki'])
P['TA0B-13'] = (lantai() + jam_dinding(240, 52, 34, 12, 0) + matahari(70, 40, 20, 'p')
                + orang(150, tinggi=150, jenis='pria', duduk=150, baju='a', tangan={'ka': [(10, 18), (4, 0)]}) + meja(150, 140, 170) + mangkuk_mi(196, 113, .35))
P['TA0B-14'] = lantai() + meja(110, 130, 160) + kursi(232, 200, 1, 1.1)
P['TA0B-15'] = lantai() + kaos(90, 120, .9, 'a') + label_harga(212, 80, '5000', 150, 64)
P['TA0B-16'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='tawa', tangan={'ka': [(20, -30), (30, -60)]}) + gelembung(210, 60, 130, 60, teks(210, 70, 'Hello!', 26, angka=True), (-1, 1))

# ---------- A1 ----------
P['TA1A-5a'] = rute('kiri', 2); P['TA1A-5b'] = rute('kanan', 2); P['TA1A-5c'] = rute('kiri', 1)
P['TA1A-6a'] = pegang(150, 'pria', 'kepala'); P['TA1A-6b'] = pegang(150, 'pria', 'perut'); P['TA1A-6c'] = pegang(150, 'pria', 'lutut')
P['TA1A-7a'] = baca_perpus(); P['TA1A-7b'] = nonton_tv(); P['TA1A-7c'] = makan_restoran()
P['TA1A-8a'] = panas(); P['TA1A-8b'] = dingin_angin(); P['TA1A-8c'] = hujan_deras()
P['TA1A-9a'] = peta_stasiun('sesudah'); P['TA1A-9b'] = peta_stasiun('sebelum'); P['TA1A-9c'] = peta_stasiun('jauh')
P['TA1A-11a'] = sepatu_sempit(); P['TA1A-11b'] = sepatu_besar(); P['TA1A-11c'] = pilih_kemeja()
P['TA1A-12'] = barisan(['pria', 'wanita', 'gadis'], x1=28, x2=96, tinggi=[118, 108, 74]) + kereta(200, 196, 180)
P['TA1A-13'] = (lantai() + kue_ultah(80, 196, '15', .9) + kue_ultah(220, 196, '12', .9) + teks(80, 218, '哥哥', 20) + teks(220, 218, '弟弟', 20))
P['TA1B-5a'] = rute('kanan', 1); P['TA1B-5b'] = rute('kiri', 1); P['TA1B-5c'] = rute('kanan', 2)
P['TA1B-6a'] = pegang(150, 'wanita', 'perut'); P['TA1B-6b'] = pegang(150, 'wanita', 'kepala'); P['TA1B-6c'] = pegang(150, 'wanita', 'lutut')
P['TA1B-7a'] = lari_taman(); P['TA1B-7b'] = renang(); P['TA1B-7c'] = tidur_rumah()
P['TA1B-8a'] = hujan_dingin('wanita'); P['TA1B-8b'] = panas(170, 'wanita'); P['TA1B-8c'] = dingin_angin(190, 'wanita')
P['TA1B-9a'] = lantai() + bus(100, 200, 170) + jam_sektor(240, 80, 50, 20)
P['TA1B-9b'] = lantai() + bus(100, 200, 170) + jam_sektor(240, 80, 50, 59.5)
P['TA1B-9c'] = lantai() + bus(100, 200, 170) + jam_sektor(240, 80, 50, 10)
P['TA1B-11a'] = baju_besar(); P['TA1B-11b'] = baju_kecil(); P['TA1B-11c'] = coba_celana()
P['TA1B-12'] = lantai() + sekolah(200, 200, 150, 100) + pengendara_sepeda(70, 'pria', 'a', 120)
tas = lambda x: (jalur(f'M{x - 18} 120 q18 -30 36 0', 'g', 5) + kotak(x - 36, 120, 72, 80, 'a', 12) + kotak(x - 36, 120, 72, 30, 'p', 10)
                 + kotak(x - 20, 162, 40, 26, 'p', 5))
P['TA1B-13'] = (lantai() + tas(80) + tas(200)
                + label_harga(84, 40, '300', 110, 48).replace('font-size="32"', 'font-size="22"') + label_harga(204, 40, '300', 110, 48).replace('font-size="32"', 'font-size="22"'))

# ---------- A2 ----------
P['TA2A-5a'] = bioskop_(); P['TA2A-5b'] = gunung_(); P['TA2A-5c'] = pantai()
P['TA2A-6a'] = anak_anjing(); P['TA2A-6b'] = kue(); P['TA2A-6c'] = buket()
P['TA2A-7a'] = ruang_sofa('jendela'); P['TA2A-7b'] = ruang_sofa('kamar'); P['TA2A-7c'] = ruang_sofa('pintu')
P['TA2A-8a'] = dua_kaos('1,500'); P['TA2A-8b'] = dua_kaos('1,600'); P['TA2A-8c'] = dua_kaos('2,000')
P['TA2A-9a'] = obat('adik'); P['TA2A-9b'] = obat('meja'); P['TA2A-9c'] = obat('buang')
P['TA2A-11a'] = buang_sampah('keluar'); P['TA2A-11b'] = buang_sampah('dapur'); P['TA2A-11c'] = buang_sampah('meja')
P['TA2A-12'] = (bentuk((20, 30), (140, 20), (150, 190), (24, 200), k='p') + jalur('M84 110 m-30 0 a30 30 0 1 1 30 30 a18 18 0 1 1 -18 -18 a8 8 0 1 1 8 8', 'g', 5)
                + lantai(200, 160, 284) + sekolah(222, 200, 110, 80) + silang(222, 172, 18, 6))
P['TA2A-13'] = (lantai() + kompor(210, 130) + meja(210, 130, 120) + wajan(210, 112, 1.0)
                + orang(100, tinggi=160, jenis='wanita', baju='a', wajah='nyanyi', tangan={'ka': [(30, 10), (66, 14)]}) + not_musik(60, 50) + not_musik(146, 36, .8))
P['TA2B-5a'] = pantai(); P['TA2B-5b'] = gunung_(); P['TA2B-5c'] = bioskop_()
P['TA2B-6a'] = kamar(True); P['TA2B-6b'] = kamar(False); P['TA2B-6c'] = kamar(True, False)
P['TA2B-7a'] = buku_di('rak'); P['TA2B-7b'] = buku_di('meja'); P['TA2B-7c'] = buku_di('ranjang')
P['TA2B-8a'] = dua_sepatu('1,300'); P['TA2B-8b'] = dua_sepatu('1,400'); P['TA2B-8c'] = dua_sepatu('2,000')
P['TA2B-9a'] = sepeda_('kakak'); P['TA2B-9b'] = sepeda_('pencuri'); P['TA2B-9c'] = sepeda_('rusak')
P['TA2B-11a'] = jendela_aksi('tutup'); P['TA2B-11b'] = jendela_aksi('buka'); P['TA2B-11c'] = jendela_aksi('bersih')
P['TA2B-12'] = lantai() + awan(110, 46, 1.5, 'h') + awan(200, 56, 1.3, 'h') + papan_angka(150, 110, '可能下大雨', 170, 44, uk=24)
P['TA2B-13'] = dua_panel(lantai(200, 16, 146) + ring_basket(120) + orang(60, tinggi=140, jenis='pria', baju='a', tangan={'ka': [(10, -30), (16, -60)]}) + bola(84, 54, 13, 'basket'),
                         kotak(154, 110, 130, 90, 'a') + bulat(214, 104, 14) + muka(214, 104, 14, 'senyum') + jalur('M200 102 q2 -18 14 -18 q12 0 14 16', 'h') + jalur('M232 116 Q248 74 270 96', 'g', 6)
                         + ''.join(jalur(f'M{160 + i * 40} {130 + (i % 2) * 20} q10 -8 20 0 t20 0', 'w') for i in range(3)))
