"""Ilustrasi SVG untuk 溝通任務 (tasks) & Tes Bab (bank soal) di 18 bab modul mini — pengganti ikon emoji.

Kunci: M<kode>-t<n> = soal ke-n di tasks bab itu, M<kode>-b<n> = soal ke-n di bank Tes Bab (mulai 1);
akhiran a/b/c = pilihan A/B/C; tanpa akhiran = gambar soal (picture). LABEL[kunci] = keterangan saat digambar:
buat_mini.py hanya memasang gambar bila keterangan di data masih sama (soal diedit → kembali ke ikon + peringatan).
Gaya sama dengan gambar_pilihan.py (garis hitam, isian hitam/putih/abu, kanvas 300×220).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # _kerja/ (svg_lib, svg_adegan)
from gambar_pilihan import *          # komponen bersama (orang, jam, harga, cuaca, rute, …) + svg_adegan/svg_lib

G, LABEL = {}, {}


def opsi(kunci, *gambar):
    for k, g in zip('abc', gambar): G[kunci + k] = g

def soal(kunci, g): G[kunci] = g


# ---------- komponen tambahan ----------
def tulisan(x, y, s, uk=26, k=''): return teks(x, y, s, uk, angka=k == 'd')

def ngomong(jenis, isi, uk=26, x=80):
    """Orang berbicara + balon kata berisi teks (mis. 你好 / Hello)."""
    return (lantai() + orang(x, tinggi=160, jenis=jenis, baju='a', wajah='senyum', tangan={'ka': [(16, 10), (26, -14)]})
            + gelembung(205, 66, 140, 64, teks(205, 66 + uk * .36, isi, uk, angka=isi.isascii()), (-1, 1)))

def bendera_amerika(x, y, w=110, h=74):
    o = ''.join(kotak(x, y + i * h / 7, w, h / 7, 'a' if i % 2 == 0 else 'p') for i in range(7))
    o += kotak(x, y, w * .42, h * 4 / 7, 'h') + ''.join(bulat(x + 9 + i * 10, y + 9 + j * 10, 2, 'n') for i in range(4) for j in range(4))
    return o + tiang(x, y)

def bendera_saja(b):
    f = {'jp': bendera_jepang, 'us': bendera_amerika, 'id': bendera_indonesia, 'tw': bendera_taiwan}[b]
    return lantai() + f(95, 40, 130, 88)

def kelompok(jenis, x1=40, x2=260, tinggi=None):
    return barisan(jenis, x1=x1, x2=x2, tinggi=tinggi)

def bola_di(tempat):
    o = lantai()
    if tempat == 'samping_kursi': return o + meja(110, 130, 150) + kursi(230, 200, 1, 1.0) + bola(270, 186, 14)
    if tempat == 'atas_meja': return o + meja(140, 130, 190) + bola(140, 116, 14) + kursi(262, 200, 1, .8)
    return o + meja(140, 130, 190) + bola(140, 186, 14) + kursi(262, 200, 1, .8)

def kursi_meja(posisi):
    """kursi di atas / belakang / depan meja (meja tampak samping, kursi menghadap kanan)."""
    if posisi == 'atas': return lantai() + meja(150, 140, 200) + kursi(150, 140, 1, .9)
    if posisi == 'belakang': return lantai() + kursi(150, 200, 1, 1.15) + meja(150, 130, 200)
    return lantai() + meja(150, 110, 170) + kursi(150, 200, 1, 1.25)

def uang(x, y, angka, w=96, h=48):
    return kotak(x - w / 2, y - h / 2, w, h, 'p', 4) + kotak(x - w / 2 + 5, y - h / 2 + 5, w - 10, h - 10, 't', 3) + teks(x, y + 9, angka, 24, angka=True)

def koin(x, y, angka='10', r=22): return bulat(x, y, r, 'a') + bulat(x, y, r - 5, 't') + teks(x, y + 7, angka, 18, angka=True)

def tumpuk_uang(n=4):
    return ''.join(uang(150 + (i % 2) * 14, 160 - i * 22, '1000', 140, 56) for i in range(n))

def tidur_jam(h, m, bangun=False):
    o = lantai() + ranjang(120, 200, 200) + jam_dinding(248, 64, 36, h, m)
    if bangun:   # duduk di ranjang, weker berbunyi
        return (o + orang(70, tinggi=120, jenis='pria', duduk=148, baju='a', wajah='lelah', tangan={'ki': [(14, -20), (6, -46)]})
                + jalur('M226 30 l-8 -8 M270 30 l8 -8 M248 20 l0 -10', 'g'))
    return (o + bulat(46, 132, 15) + muka(46, 132, 15, 'tidur') + jalur('M31 127 q2 -20 16 -20 q14 0 15 16', 'h')
            + kotak(62, 132, 150, 18, 'p', 6) + teks(82, 104, 'z z', 20, angka=True))

def kalender(isi, x=150, y=40, w=130, h=130):
    return (kotak(x - w / 2, y, w, h, 'p', 6) + kotak(x - w / 2, y, w, 30, 'h', 6) + bulat(x - 30, y, 5, 'p') + bulat(x + 30, y, 5, 'p')
            + teks(x, y + h / 2 + 34, isi, 44))

def jendela_web(isi=''):
    return (kotak(40, 30, 220, 160, 'p', 8) + kotak(40, 30, 220, 26, 'a', 8) + bulat(56, 43, 5, 'p') + bulat(72, 43, 5, 'p')
            + kotak(90, 36, 160, 14, 'p', 6) + kotak(56, 70, 90, 60, 'a') + ''.join(garis((160, 76 + i * 16), (244, 76 + i * 16), k='t') for i in range(4))
            + ''.join(garis((56, 146 + i * 14), (244, 146 + i * 14), k='t') for i in range(3)) + isi)

def kompas(x=150, y=110, r=80):
    return (bulat(x, y, r, 'p') + bentuk((x, y - r + 10), (x + 14, y), (x - 14, y), k='h') + bentuk((x, y + r - 10), (x + 14, y), (x - 14, y), k='p')
            + teks(x, y - r - 6, '北', 22) + teks(x, y + r + 22, '南', 22))

def dunia(x=150, y=110, r=86):
    return (bulat(x, y, r, 'p') + jalur(f'M{x - 60} {y - 30} q20 -30 50 -20 q10 20 -10 40 q-30 10 -40 -20 Z', 'a')
            + jalur(f'M{x + 10} {y - 50} q40 0 50 30 q-10 30 -30 20 q-20 -10 -20 -50 Z', 'a')
            + jalur(f'M{x - 20} {y + 20} q30 -10 40 20 q-10 30 -30 30 q-20 -20 -10 -50 Z', 'a')
            + jalur(f'M{x + 40} {y + 30} q20 0 20 20 q-20 10 -20 -20 Z', 'a') + jalur(f'M{x - r} {y} Q{x} {y + 26} {x + r} {y}', 't'))

def termo_dua(a, b, la, lb):
    return (teks(90, 30, la, 24) + termometer(90, 44, a) + teks(210, 30, lb, 24) + termometer(210, 44, b))

def jaket(x, y, s=1.0, k='a'):
    return (kaos(x, y, s, k) + garis((x, y - 44 * s), (x, y + 30 * s), k='t') + jalur(f'M{x - 50 * s} {y - 36 * s} L{x - 58 * s} {y + 24 * s} L{x - 44 * s} {y + 26 * s} L{x - 42 * s} {y - 18 * s}', k)
            + jalur(f'M{x + 50 * s} {y - 36 * s} L{x + 58 * s} {y + 24 * s} L{x + 44 * s} {y + 26 * s} L{x + 42 * s} {y - 18 * s}', k))

def pakai_jaket(lepas=False):
    s_ = sendi(130, tinggi=165, jenis='pria')
    if lepas:
        return (lantai() + orang(130, tinggi=165, jenis='pria', baju='p', tangan={'ka': [(30, 0), (60, -10)]}) + jaket(232, 90, .62, 'a')
                + jalur('M200 150 l-12 10 M214 160 l-6 14', 'g'))
    return lantai() + orang(150, tinggi=165, jenis='pria', baju='p') + jaket(150, s_['bahu'] + 40, .62, 'a')

def pakai_topi():
    s_ = sendi(150, tinggi=165, jenis='pria')
    return lantai() + orang(150, tinggi=165, jenis='pria', baju='p') + topi_di(150, s_['cy'], s_['r'])

def celana(x=150, y=40, s=1.0, k='p'):
    return (bentuk((x - 40 * s, y), (x + 40 * s, y), (x + 46 * s, y + 160 * s), (x + 10 * s, y + 160 * s), (x, y + 50 * s), (x - 10 * s, y + 160 * s),
                   (x - 46 * s, y + 160 * s), k=k) + garis((x - 40 * s, y + 12 * s), (x + 40 * s, y + 12 * s), k='t'))

def celana_orang(panjang):
    """Laki-laki memakai celana terlalu panjang (menyentuh lantai) / terlalu pendek (di atas betis)."""
    s_ = sendi(150, tinggi=170, jenis='pria'); p = s_['pinggang'] - 4
    bawah = 204 if panjang else p + 44
    o = lantai() + orang(150, tinggi=170, jenis='pria', baju='p', wajah='sedih')
    o += bentuk((150 - 15, p), (150 + 15, p), (150 + 22, bawah), (150 + 3, bawah), (150, p + 14), (150 - 3, bawah), (150 - 22, bawah), k='a')
    if panjang: o += jalur(f'M118 204 q-10 -4 -14 2 M182 204 q10 -4 14 2', 'g')
    else: o += panah(206, p + 46, 206, 196, 4) + panah(206, 196, 206, p + 46, 4)
    return o

def rok(panjang):
    s_ = sendi(150, tinggi=165, jenis='wanita'); p = s_['pinggang']
    hem = {'pendek': p + 26, 'panjang': 196, 'pas': p + 52}[panjang]
    return (lantai() + orang(150, tinggi=165, jenis='wanita', baju='p', wajah='senyum' if panjang == 'pas' else 'sedih')
            + bentuk((150 - 22, p - 2), (150 + 22, p - 2), (150 + 40, hem), (150 - 40, hem), k='a'))

def aksesori(kacamata=False, jam_=False, topi=False):
    s_ = sendi(150, tinggi=165, jenis='pria')
    o = lantai() + orang(150, tinggi=165, jenis='pria', baju='p', kacamata=kacamata, tangan={'ka': [(14, 24), (26, 0)]})
    if topi: o += topi_di(150, s_['cy'], s_['r'])
    if jam_:
        tx, ty = 150 + s_['lb'] / 2 + 22, s_['bahu'] + 10
        o += kotak(tx - 9, ty - 7, 18, 14, 'p', 3) + bulat(tx, ty, 4, 't') + garis((tx + 26, ty - 10), (tx + 36, ty - 16), k='g')
    return o

def kamar_banding(punyaku):
    """Dua kamar berdampingan berlabel 我 / 你; punyaku = 'besar' | 'kecil' | 'sama'."""
    w = {'besar': (130, 80), 'kecil': (80, 130), 'sama': (105, 105)}[punyaku]
    o = ''
    for i, (lab, lebar) in enumerate(zip(['我', '你'], w)):
        x = 80 if i == 0 else 220
        o += kotak(x - lebar / 2, 200 - lebar * .9, lebar, lebar * .9, 'p') + ranjang(x, 200, 60) + teks(x, 218, lab, 20)
    return o

def peta_kota(rumah_di):
    """臺北 di tengah + rumah di timur / utara / barat."""
    o = bulat(150, 110, 34, 'a') + teks(150, 118, '臺北', 22)
    pos = {'timur': (250, 110), 'utara': (150, 30), 'barat': (50, 110)}[rumah_di]
    o += rumah(pos[0], pos[1] + 30, 60, 34) + panah(150 + (pos[0] - 150) * .3, 110 + (pos[1] - 110) * .35, 150 + (pos[0] - 150) * .62, 110 + (pos[1] - 110) * .62, 4)
    return o + teks(270, 210, '北↑', 16)

def utara_selatan(utara_dingin):
    o = kotak(110, 16, 80, 188, 'p', 30) + garis((110, 110), (190, 110), k='t') + teks(150, 60, '北', 24) + teks(150, 162, '南', 24)
    atas, bawah = (salju(52, 60, 16), matahari(52, 160, 18, 'p')) if utara_dingin else (matahari(52, 60, 18, 'p'), salju(52, 160, 16))
    return o + atas + bawah + termometer(250, 26, 5 if utara_dingin else 38, h=56) + termometer(250, 126, 38 if utara_dingin else 5, h=56)

def sama_tanda(): return lantai() + tas(80) + teks(150, 172, '=', 60, angka=True) + tas(220)


def laptop(x, bawah, w=90):
    """Laptop: layar terbuka + papan ketik (beda jelas dengan TV)."""
    return (kotak(x - w / 2, bawah - w * .62 - 8, w, w * .62, 'p', 4) + kotak(x - w / 2 + 6, bawah - w * .62 - 2, w - 12, w * .62 - 12, 'a', 2)
            + bentuk((x - w / 2 - 6, bawah - 8), (x + w / 2 + 6, bawah - 8), (x + w / 2 + 16, bawah), (x - w / 2 - 16, bawah), k='p')
            + ''.join(garis((x - w / 2 + i * w / 6, bawah - 4), (x - w / 2 + i * w / 6 + 6, bawah - 4), k='t') for i in range(1, 6)))

def tv_antena(x, bawah, w=90):
    t = w * .64
    return tv(x, bawah, w) + garis((x, bawah - t - 10), (x - 22, bawah - t - 40), k='g') + garis((x, bawah - t - 10), (x + 22, bawah - t - 40), k='g')

def buku_buka(x, y, w=70, h=40):
    return (bentuk((x, y + 6), (x - w / 2, y), (x - w / 2, y + h), (x, y + h + 6), k='p') + bentuk((x, y + 6), (x + w / 2, y), (x + w / 2, y + h), (x, y + h + 6), k='p')
            + ''.join(garis((x - w / 2 + 6, y + 10 + i * 8), (x - 6, y + 14 + i * 8), k='t') + garis((x + 6, y + 14 + i * 8), (x + w / 2 - 6, y + 10 + i * 8), k='t') for i in range(3)))

def kertas_laporan(x=130, y=24, w=120, h=168):
    return (kotak(x - w / 2, y, w, h, 'p', 4) + teks(x, y + 30, '報告', 22)
            + ''.join(garis((x - w / 2 + 14, y + 52 + i * 18), (x + w / 2 - 14, y + 52 + i * 18), k='t') for i in range(6)))


# =================== A0 ===================
opsi('MA02-t8', ngomong('pria', '你好'), ngomong('pria', 'Hello'), ngomong('wanita', 'Hello'))
soal('MA02-t9', ngomong('wanita', '你好'))
soal('MA02-t10', lantai() + orang(90, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(16, -20), (24, -50)]}) + orang(220, tinggi=150, jenis='wanita', baju='p')
     + gelembung(150, 50, 90, 50, teks(150, 62, '？', 34), (-1, 1)))
opsi('MA02-b3', bendera_saja('jp'), bendera_saja('us'), bendera_saja('id'))
opsi('MA02-b4', bendera_saja('jp'), bendera_saja('us'), bendera_saja('id'))
opsi('MA02-b6', ngomong('pria', 'Hello'), ngomong('wanita', '你好'), ngomong('wanita', 'Hello'))
soal('MA02-b7', lantai() + orang(80, tinggi=158, jenis='wanita', baju='a', tangan={'ka': [(16, -20), (24, -50)]}) + orang(210, tinggi=165, jenis='pria', baju='p')
     + gelembung(150, 46, 90, 50, teks(150, 58, '？', 34), (-1, 1)))
soal('MA02-b8', ngomong('pria', '你好'))

opsi('MA04-t8', keluarga_n(5), keluarga_n(4), kelompok(['pria', 'wanita', 'gadis'], 70, 230))
soal('MA04-t9', kelompok(['wanita', 'gadis', 'gadis', 'gadis'], 50, 250))
soal('MA04-t10', kelompok(['pria', 'laki'], 100, 200))
opsi('MA04-b3', keluarga_n(6), keluarga_n(5), keluarga_n(4))
opsi('MA04-b4', anak(['gadis', 'gadis', 'gadis']), anak(['gadis', 'gadis']), kelompok(['gadis'], 150, 150, [112]))
opsi('MA04-b6', anak(['laki', 'gadis']), kelompok(['laki'], 150, 150, [120]), anak(['laki', 'gadis', 'laki']))
soal('MA04-b7', kelompok(['pria', 'wanita', 'laki', 'laki'], 50, 250))
soal('MA04-b8', kelompok(['gadis'], 150, 150, [120]))

opsi('MA09-t8', bola_di('samping_kursi'), bola_di('atas_meja'), bola_di('bawah_meja'))
soal('MA09-t9', lantai() + meja(150, 130, 130) + kursi(50, 200, 1, .9) + kursi(256, 200, -1, .9))
soal('MA09-t10', lantai() + orang(110, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(26, -10), (50, -30)], 'ki': [(-6, 20), (-2, 40)]}) + kursi(200, 120, 1, .7))
opsi('MA09-b3', lantai() + meja(150, 140, 160) + tv(150, 140, 100), lantai() + ranjang(110, 200, 170) + tv(250, 200, 70),
     lantai() + kursi(90, 200, 1, 1.0) + meja(220, 150, 80) + tv(220, 150, 80))
opsi('MA09-b4', lantai() + kursi(150, 200, 1, 1.25) + bola(140, 108, 14), lantai() + ranjang(150, 200, 220) + bola(150, 186, 13), bola_di('atas_meja'))
opsi('MA09-b6', kursi_meja('atas'), kursi_meja('belakang'), kursi_meja('depan'))
soal('MA09-b7', lantai() + ranjang(150, 200, 220) + bola(160, 134, 14))
soal('MA09-b8', lantai() + meja(150, 130, 130) + kursi(50, 200, 1, .9) + kursi(256, 200, -1, .9))

opsi('MA10-t8', jam(2, 0), jam(2, 30), jam(8, 30))
soal('MA10-t9', tidur_jam(7, 0, bangun=True) + matahari(150, 30, 14, 'p'))
soal('MA10-t10', jam(7, 0))
opsi('MA10-b3', tidur_jam(10, 0), tidur_jam(11, 0), tidur_jam(10, 0, bangun=True))
opsi('MA10-b4', jam(9, 50), jam(10, 0), jam(10, 30))
opsi('MA10-b6', tidur_jam(10, 0) + bulan_bintang(150, 34, .6), tidur_jam(2, 0) + matahari(150, 34, 14, 'p'), tidur_jam(2, 0, bangun=True))
soal('MA10-b7', tidur_jam(11, 0) + bulan_bintang(150, 34, .6))
soal('MA10-b8', jam_sektor(150, 110, 88, 30))

opsi('MA18-t8', harga(lantai() + cangkir(80, 196, 1.3), '15'), harga(lantai() + cangkir(80, 196, 1.3), '50'),
     harga(lantai() + cangkir(80, 196, 1.3, uap=False) + kantong_teh(96, 150), '50'))
soal('MA18-t9', lantai() + orang(70, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(26, 0), (60, -6)]}) + uang(160, 100, '20', 70, 36)
     + orang(240, tinggi=165, jenis='pria', baju='p', tangan={'ki': [(20, 0), (40, -4)]}))
soal('MA18-t10', label_harga(150, 70, '10', 180, 80))
opsi('MA18-b3', uang(150, 110, '2,100', 200, 100), uang(150, 110, '1,200', 200, 100), uang(150, 110, '1,002', 200, 100))
opsi('MA18-b4', uang(150, 110, '200', 200, 100), uang(150, 110, '100', 200, 100), uang(150, 110, '50', 200, 100))
opsi('MA18-b6', tumpuk_uang(4), koin(150, 110, '10', 60), uang(150, 110, '100', 200, 100))
soal('MA18-b7', lantai() + toko(110, 200, 170, 120) + orang(240, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(16, 30), (20, 50)]}) + tas_belanja(262, 196, .8))
soal('MA18-b8', label_harga(150, 70, '5', 180, 80))

opsi('MA24-t8', cerah(), hujan_deras(), berangin_cerah().replace(matahari(56, 44, 22, 'p'), '') + awan(70, 40, .9, 'p'))
soal('MA24-t9', panas())
soal('MA24-t10', hujan_dingin())
opsi('MA24-b3', cerah(), hujan_deras(), lantai() + ''.join(salju(x, y, 10) for x, y in ((60, 40), (140, 60), (230, 36), (90, 110), (200, 120), (150, 170), (260, 160))))
opsi('MA24-b4', dingin_angin(), hujan_deras(), panas())
opsi('MA24-b6', hujan_deras(), dingin_angin(), panas() + kalender('7月', 240, 120, 70, 70).replace('font-size="44"', 'font-size="24"'))
soal('MA24-b7', gunung_() + ''.join(bunga(x, 176, 1.1) for x in (60, 100, 200, 240)))
soal('MA24-b8', lantai() + gunung(150, 200, 260, 70, salju=False) + pohon(60, s=.5) + orang(240, tinggi=120, jenis='pria', baju='a'))


# =================== A1 ===================
def aktivitas(apa, jenis='pria'):
    """Orang duduk: main internet (laptop) / nonton TV / membaca buku."""
    o = lantai() + kursi_depan(110, 140) + orang(110, tinggi=150, jenis=jenis, duduk=140, baju='a',
                                                  tangan={'ki': [(4, 30), (-10, 20)], 'ka': [(4, 30), (-10, 20)]})
    if apa == 'internet': return o + meja(210, 150, 120) + laptop(210, 150, 90)
    return o + buku_buka(110, 96, 74, 40)

def nonton(jenis): return lantai() + sofa(95, 200, 140) + orang(95, tinggi=140, jenis=jenis, duduk=152, baju='a') + meja(235, 150, 80) + tv_antena(235, 150, 90)

def ponsel_ngobrol():
    return (lantai() + orang(70, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(10, -10), (-2, -36)]}) + ponsel(84, 54, .7)
            + orang(230, tinggi=165, jenis='pria', baju='p', tangan={'ki': [(10, -10), (-2, -36)]}) + ponsel(216, 52, .7)
            + titik_obrolan(150, 50, 70, 40))

def tunggu(): return lantai() + jam_pasir(150, 110, 2.2) + orang(250, tinggi=150, jenis='pria', baju='a')

def tidur_saja(): return tidur_rumah()
def kerja(): return lantai() + meja_kantor(150) + orang_duduk_kerja(150, 'pria', 'a')
def ngobrol2(): return lantai() + orang(90, tinggi=160, jenis='pria', baju='a', wajah='tawa') + orang(210, tinggi=150, jenis='wanita', baju='p', wajah='tawa') + titik_obrolan(150, 50, 70, 40)

def dua_layar(ibu, ayah):
    """Ibu & ayah: masing-masing di depan TV atau komputer."""
    o = lantai() + garis((150, 20), (150, 200), k='t')
    for x, jenis, alat in ((75, 'wanita', ibu), (225, 'pria', ayah)):
        o += orang(x - 30, tinggi=140, jenis=jenis, baju='a')
        o += meja(x + 34, 150, 70) + (tv_antena(x + 34, 150, 62) if alat == 'tv' else laptop(x + 34, 150, 56))
    return o

opsi('MB04-t8', aktivitas('internet'), nonton('pria'), aktivitas('buku'))
soal('MB04-t9', ponsel_ngobrol())
soal('MB04-t10', tunggu())
opsi('MB04-b3', aktivitas('buku', 'wanita'), nonton('wanita'), aktivitas('internet', 'wanita'))
opsi('MB04-b4', tidur_rumah(), kerja(), ngobrol2())
opsi('MB04-b6', dua_layar('tv', 'tv'), dua_layar('tv', 'pc'), dua_layar('pc', 'tv'))
soal('MB04-b7', jendela_web(sekolah(101, 130, 70, 46)))
soal('MB04-b8', tunggu())

opsi('MB19-t8', kamar_banding('kecil'), kamar_banding('besar'), kamar_banding('sama'))
soal('MB19-t9', kompas())
soal('MB19-t10', dunia())
opsi('MB19-b3', termo_dua(36, 20, '臺北', '高雄'), termo_dua(10, 30, '臺北', '高雄'), termo_dua(22, 22, '臺北', '高雄'))
opsi('MB19-b4', peta_kota('timur'), peta_kota('utara'), peta_kota('barat'))
opsi('MB19-b6', lantai() + termo_dua(22, 22, '北', '南'), utara_selatan(False), utara_selatan(True))
soal('MB19-b7', dunia())
soal('MB19-b8', sama_tanda())

opsi('MB20-t8', pakai_jaket(), pakai_jaket(lepas=True), pakai_topi())
soal('MB20-t9', celana_orang(panjang=True))
soal('MB20-t10', lantai() + kotak(60, 100, 180, 40, 'a', 20) + kotak(118, 70, 64, 100, 'p', 12) + bulat(150, 120, 24, 't')
     + garis((150, 120), (150, 104), k='g') + garis((150, 120), (162, 126), k='g'))
opsi('MB20-b3', lantai() + celana(), pakai_topi(), lantai() + jaket(150, 100, 1.2))
opsi('MB20-b4', rok('pendek'), rok('panjang'), rok('pas'))
opsi('MB20-b6', aksesori(kacamata=True, jam_=True), aksesori(kacamata=True), aksesori(jam_=True, topi=True))
soal('MB20-b7', celana_orang(panjang=False))
soal('MB20-b8', pakai_jaket(lepas=True) + matahari(60, 40, 16, 'p') + keringat(110, 50))

def peta_lurus(lewat_taman=True):
    o = kotak(126, 8, 48, 204, 'a') + bulat(150, 204, 7, 'h') + panah(150, 196, 150, 50, 7) + gedung_bank(150, 40, 120, 30).replace('$', '')
    if lewat_taman: o += pohon(90, 150, .6) + pohon(210, 120, .6)
    return o

opsi('MB30-t8', perempatan('lurus'), perempatan('kanan'), perempatan('kiri'))
soal('MB30-t9', lantai() + jalan_kaki(130) + panah(190, 120, 270, 120, 6))
soal('MB30-t10', lantai() + rumah(200, 200, 140, 100) + jalan_kaki(70) + bulan_bintang(60, 30, .6))
opsi('MB30-b3', rute('kiri', 1), peta_lurus(), lantai() + bus(150, 200, 230))
opsi('MB30-b4', rute('kiri', 1), rute('kiri', 2), rute('kanan', 2))
opsi('MB30-b6', buku_di('meja'), buku_di('ranjang'), lantai() + buku_tumpuk(150, 132, 2, 58, 16) + tas(150))
soal('MB30-b7', perempatan('lurus').replace(panah(150, 200, 150, 24, 8), '') + kotak(196, 50, 22, 50, 'h', 4) + bulat(207, 62, 6, 'p') + bulat(207, 76, 6, 'n') + bulat(207, 90, 6, 'n'))
soal('MB30-b8', lantai() + jalan_kaki(110) + panah(170, 110, 260, 110, 7))

def bakpau_n(n): return lantai() + meja(150, 150, 220) + piring(150, 144, 90) + ''.join(bakpao(150 + (i - (n - 1) / 2) * 52, 140, .9) for i in range(n))

opsi('MB33-t8', bakpau_n(1), bakpau_n(3), lantai() + meja(150, 150, 200) + mangkuk_mi(150, 110, .5))
soal('MB33-t9', lantai() + pesawat(190, 70, .8) + orang(70, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(12, 30), (20, 56)]}) + koper(98, 200, .6))
soal('MB33-t10', lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='kaget') + teks(210, 60, '!', 44, angka=True))
opsi('MB33-b3', kelompok(['wanita', 'pria'], 100, 200), kelompok(['wanita'], 150, 150, [160]), kelompok(['wanita', 'wanita'], 100, 200, [152, 166]))
opsi('MB33-b4', kalender('15天'), kalender('5天'), kalender('2天'))
opsi('MB33-b6', bakpau_n(1), bakpau_n(3), bakpau_n(2))
soal('MB33-b7', lantai() + koper(110, 200, 1.0) + peta(210, 70, 120, 90))
soal('MB33-b8', lantai() + orang(110, tinggi=165, jenis='pria', baju='a', wajah='kaget') + kalender('五', 230, 50, 90, 90).replace('font-size="44"', 'font-size="36"'))

def hujan_ke(tempat):
    o = lantai() + awan(150, 30, 1.4, 'a') + hujan(150, 54, 260, 40, 12)
    if tempat == 'taman': return o + pohon(80, s=.7) + pohon(230, s=.6) + jalan_kaki(150, wajah='sedih')
    return o + rumah(150, 200, 170, 110) + kotak(126, 130, 48, 40, 'p') + bulat(150, 148, 10) + muka(150, 148, 10, 'senyum')

opsi('MB40-t8', hujan_ke('taman'), hujan_ke('rumah'), lantai() + matahari(60, 46, 26, 'p') + pohon(250, s=.8) + jalan_kaki(150))
soal('MB40-t9', lantai() + meja(66, 150, 100) + piring(66, 144, 44) + buah_apel(54, 136, .55) + buah_apel(78, 136, .55) + pohon(266, s=.6) + orang(180, tinggi=160, jenis='pria', baju='a', kaki_pose={'ki': (-34, -8), 'ka': (28, 0)}, tangan={'ki': [(14, 18), (34, 4)], 'ka': [(-4, 26), (-22, 38)]}))
soal('MB40-t10', lantai() + awan(150, 30, 1.4, 'a') + hujan(150, 54, 260, 40, 12) + jalan_kaki(110) + payung(110, 50, 44) + sekolah(230, 200, 100, 70))
opsi('MB40-b3', lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='lelah') + keringat(186, 50),
     lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='tawa', tangan={'ki': [(20, -10), (10, -40)], 'ka': [(20, -10), (10, -40)]}),
     lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='sakit') + termometer(210, 30, 38, h=80))
opsi('MB40-b4', lantai() + ranjang(150, 200, 220) + bulat(62, 132, 15) + muka(62, 132, 15, 'sakit') + kotak(78, 132, 150, 18, 'p', 6) + termometer(250, 30, 39, h=70),
     lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='tawa', tangan={'ki': [(20, -10), (10, -40)], 'ka': [(20, -10), (10, -40)]}),
     lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='lelah') + keringat(186, 52))
opsi('MB40-b6', lantai() + rumah(200, 200, 140, 100) + orang(70, tinggi=130, jenis='laki', baju='a', wajah='sakit') + termometer(110, 40, 38, h=50),
     lantai() + orang(110, tinggi=130, jenis='laki', baju='a', kaki_pose={'ki': (-14, 0), 'ka': (30, -20)}) + bola(170, 182, 14),
     lantai() + sekolah(180, 200, 150, 100) + jalan_kaki(50, tinggi=120))
soal('MB40-b7', lantai() + piring(80, 160, 56) + buah_apel(64, 148, .7) + buah_apel(96, 148, .7) + meja(80, 166, 110)
     + orang(220, tinggi=165, jenis='pria', baju='a', wajah='tawa', tangan={'ki': [(20, -10), (10, -40)], 'ka': [(20, -10), (10, -40)]}))
soal('MB40-b8', lantai() + jam_dinding(80, 80, 56, 10, 0) + sekolah(220, 200, 130, 90) + jalan_kaki(160, tinggi=120))


# =================== A2 ===================
def meja_di(tempat):
    if tempat == 'rumah': return lantai() + kotak(16, 20, 268, 180, 'p') + jendela(220, 50, 70, 56) + meja(130, 140, 160) + kursi(240, 200, 1, .8)
    if tempat == 'halaman':
        return (lantai() + pohon(260, s=.8) + rumah(50, 200, 80, 70) + meja(170, 160, 90)
                + orang(110, tinggi=140, jenis='pria', baju='a', tangan={'ka': [(20, 10), (40, 24)]}) + orang(230, tinggi=140, jenis='pria', baju='h', tangan={'ki': [(20, 10), (40, 24)]}))
    return lantai() + ranjang(90, 200, 150) + meja(230, 150, 90)

def sepatu_di(tempat):
    if tempat == 'pintu': return lantai() + pintu(150, 200, 150, 70) + sepatu(210, 200, .7, 'h')
    if tempat == 'ranjang': return lantai() + ranjang(150, 200, 220) + sepatu(150, 198, .5, 'h')
    return lantai() + sofa(150, 200, 180) + sepatu(150, 150, .6, 'h')

def sofa_di(tempat):
    if tempat == 'tamu': return lantai() + sofa(120, 200, 170) + meja(255, 160, 50) + tv(255, 160, 56)
    if tempat == 'kamar': return lantai() + ranjang(90, 200, 150) + sofa(240, 200, 90)
    return lantai() + pohon(60, s=.8) + bunga(120, 176, 1.0) + sofa(210, 200, 150) + matahari(260, 30, 14, 'p')

def kantor(waktu, isi):
    o = lantai() + kotak(16, 20, 268, 180, 'p') + jendela(70, 40, 80, 60)
    o += matahari(70, 70, 14, 'p') if waktu == 'siang' else bulan_bintang(70, 62, .5)
    if isi == 'menulis': return o + meja_kantor(180) + orang_duduk_kerja(180, 'pria', 'a') + kertas(220, 120, 30, 20)
    return o + meja_kantor(180) + orang_duduk_kerja(180, 'pria', 'a')

def laporan(tanda=''):
    o = lantai() + kertas_laporan() + pulpen(214, 170, 90, -50)
    return o + (teks(250, 100, '!', 64, angka=True) if tanda else '')

def kalender_hari(hari):
    """Kalender 一 … 五 dengan satu hari disorot (hari = indeks 0–4, None = semua)."""
    o = kotak(30, 50, 240, 120, 'p', 6) + kotak(30, 50, 240, 26, 'h', 6)
    for i, h in enumerate('一二三四五'):
        x = 54 + i * 48
        o += kotak(x - 20, 90, 40, 60, 'a' if hari is None or hari == i else 'p', 4) + teks(x, 130, h, 24)
    return lantai() + o

def rapat(): return lantai() + papan_tulis(150, 20, 140, 70) + garis((100, 75), (130, 55), (160, 65), (190, 40), k='t', lebar=3) + meja(150, 150, 220) + orang(70, tinggi=110, jenis='pria', duduk=150, baju='a') + orang(150, tinggi=110, jenis='wanita', duduk=150, baju='p') + orang(230, tinggi=110, jenis='pria', duduk=150, baju='h')

def topan(x=150, y=100, r=60):
    return jalur(f'M{x} {y} m{-r} 0 a{r} {r} 0 1 1 {r} {r} a{r * .6} {r * .6} 0 1 1 {-r * .6} {-r * .6} a{r * .25} {r * .25} 0 1 1 {r * .25} {r * .25}', 'g', 6)

def onsen():
    return (lantai() + gunung(150, 120, 280, 80, salju=False) + elips(150, 166, 128, 30, 'a') + ''.join(bulat(x, y, r, 'p') for x, y, r in ((30, 172, 14), (60, 192, 12), (250, 190, 13), (276, 168, 12)))
            + bulat(150, 152, 14) + muka(150, 152, 14, 'puas') + ''.join(jalur(f'M{x} 130 q-10 -14 0 -28 q10 -14 0 -28', 'g', 4) for x in (90, 210)))

def sekolah_status(libur, ramai=False):
    o = lantai() + sekolah(150, 200, 170, 110)
    if libur: return o + topan(240, 60, 26) + silang(150, 160, 30, 8)
    if ramai: return o + topan(240, 60, 26) + kelompok(['laki', 'gadis'], 60, 250, [90, 86]).replace(lantai(), '')
    return o + matahari(250, 40, 18, 'p')

def bersin():
    return lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='kaget', tangan={'ka': [(10, -10), (-14, -46)]}) + jalur('M180 50 l14 -6 M182 62 l18 0 M180 74 l14 6', 'g')

def kue_habis(): return lantai() + meja(160, 140, 200) + piring(160, 134, 50) + bulat(140, 130, 3, 'h') + bulat(160, 128, 2.5, 'h') + bulat(178, 131, 3, 'h') + orang(60, tinggi=120, jenis='laki', baju='a', wajah='tawa')

def obat_oleh(siapa):
    if siapa == 'adik': return obat('adik')
    if siapa == 'anjing': return lantai() + anjing(150, 196, 1.3) + botol_obat(240, 196, .6) + f'<g transform="rotate(80 240 170)">{kotak(230, 160, 20, 20, "t")}</g>'
    return obat('buang')

def sakit_di(apa):
    if apa == 'demam': return lantai() + orang(130, tinggi=165, jenis='pria', baju='a', wajah='sakit') + termometer(210, 30, 39, h=90)
    if apa == 'pilek': return bersin() + kotak(124, 60, 18, 14, 'p', 3)
    return pegang(150, 'pria', 'lutut')

def kaki_sepatu(ukuran):
    """Telapak kaki (abu) dibandingkan sepatu: kaki jauh lebih besar / sepatu jauh lebih besar / pas."""
    s, kaki = {'kecil': (.75, 64), 'besar': (2.0, 40), 'pas': (1.25, 46)}[ukuran]
    o = lantai() + sepatu(150, 196, s, 'p') + elips(150, 130, kaki, 16, 'a') + panah(150, 150, 150, 168, 4)
    if ukuran == 'pas': return o + centang(240, 80, 1.4)
    return o + teks(250, 100, '!', 50, angka=True)

def pasar_malam(): return lantai() + lampion(50, 30, .8) + lampion(150, 24, .8) + lampion(250, 30, .8) + kios_buah(150, 200, 200) + kelompok(['pria', 'wanita', 'laki', 'gadis'], 40, 260, [110, 104, 80, 76]).replace(lantai(), '')

def mal(): return lantai() + gedung(150, 200, 5, None, 220, 30) + kotak(126, 160, 48, 40, 'h')

def antre(n):
    o = lantai() + toko(110, 200, 170, 120)
    if n == 'tutup': return o + kotak(96, 140, 28, 22, 'h', 3) + jalur('M102 140 q8 -16 16 0', 'g', 4) + silang(240, 120, 24, 6)
    if n == 'kosong': return o
    return o + kelompok(['pria', 'wanita', 'laki', 'pria'], 200, 290, [110, 104, 84, 112]).replace(lantai(), '')

opsi('MC04-t8', meja_di('rumah'), meja_di('halaman'), meja_di('kamar'))
soal('MC04-t9', lantai() + kursi(150, 200, 1, 1.3) + kucing(130, 198, .8))
soal('MC04-t10', lantai() + gedung(150, 200, 7, None, 100, 26) + pohon(50, s=.6) + pohon(250, s=.6))
opsi('MC04-b3', sepatu_di('pintu'), sepatu_di('ranjang'), sepatu_di('sofa'))
opsi('MC04-b4', lantai() + ranjang(150, 200, 230), lantai() + sofa(80, 200, 120) + kompor(220, 120, 100) + wajan(220, 104, .8), lantai() + pohon(80, s=.9) + bunga(170, 176, 1.2) + bunga(220, 176, 1.2))
opsi('MC04-b6', sofa_di('tamu'), sofa_di('kamar'), sofa_di('halaman'))
soal('MC04-b7', lantai() + rumah(110, 200, 140, 100) + pohon(240, s=.8) + ''.join(garis((200 + i * 16, 200), (200 + i * 16, 168)) for i in range(6)) + garis((196, 176), (284, 176)))
soal('MC04-b8', lantai() + ranjang(90, 200, 150) + sepatu(92, 198, .45, 'p') + panah(140, 190, 186, 190, 4) + pintu(256, 200, 150, 56) + sepatu(214, 198, .5, 'h'))

opsi('MC16-t8', kantor('siang', 'kerja'), kantor('malam', 'menulis'), lantai() + kotak(16, 20, 268, 180, 'p') + jendela(70, 40, 80, 60) + bulan_bintang(70, 62, .5) + sofa(190, 200, 130) + orang(190, tinggi=130, jenis='pria', duduk=152, baju='a') + meja(60, 160, 60) + tv(60, 160, 60))
soal('MC16-t9', laporan())
soal('MC16-t10', lantai() + kotak(16, 20, 268, 180, 'p') + jendela(56, 44, 56, 46) + sofa(110, 200, 150) + orang(110, tinggi=130, jenis='pria', duduk=152, baju='a', wajah='puas') + gelembung_pikiran(220, 120, 80, 64, gedung(220, 140, 3, None, 40, 14) + silang(220, 120, 22, 5)))
opsi('MC16-b3', kantor('malam', 'kerja'), lantai() + rumah(170, 200, 160, 100) + jalan_kaki(60) + matahari(260, 30, 16, 'p'), laporan())
opsi('MC16-b4', kalender_hari(None), kalender_hari(4), kalender_hari(0))
opsi('MC16-b6', lantai() + jam_dinding(70, 70, 50, 5, 0) + rumah(210, 200, 140, 100) + jalan_kaki(140, tinggi=120),
     kantor('malam', 'kerja'), lantai() + jam_dinding(70, 70, 50, 5, 0) + meja_kantor(200) + orang_duduk_kerja(200, 'pria', 'a'))
soal('MC16-b7', rapat())
soal('MC16-b8', laporan('!'))

opsi('MC24-t8', pantai(), lantai() + topan(80, 60, 30) + sofa(170, 200, 130) + orang(170, tinggi=130, jenis='pria', duduk=152, baju='a') + tv(270, 200, 40),
     lantai() + topan(150, 60, 34) + jalan_kaki(150, wajah='gugup') + angin(30, 120, .8))
soal('MC24-t9', onsen())
soal('MC24-t10', termometer(150, 30, 20, h=140) + teks(210, 110, '20°', 36, angka=True))
opsi('MC24-b3', hujan_deras(), lantai() + matahari(110, 70, 30, 'p') + awan(190, 80, 1.3, 'p'), lantai() + topan(150, 90, 70))
opsi('MC24-b4', lantai() + bus(110, 200, 150) + jam_sektor(240, 80, 50, 20), lantai() + bus(110, 200, 150) + jam_sektor(240, 80, 50, 10), lantai() + bus(110, 200, 150) + jam_sektor(240, 80, 50, 30))
opsi('MC24-b6', sekolah_status(False), sekolah_status(False, ramai=True), sekolah_status(True))
soal('MC24-b7', lantai() + pohon(70, s=.8) + ''.join(bunga(x, 176, 1.1) for x in (130, 170, 210)) + termometer(260, 40, 22, h=100))
soal('MC24-b8', bentuk((40, 20), (160, 10), (170, 200), (44, 210), k='p') + topan(100, 150, 30) + panah(100, 110, 100, 40, 6) + teks(230, 60, '北↑', 30))

opsi('MC28-t8', bersin(), lari_taman().replace(bunga(210, 176, .8), '') + keringat(120, 40) + keringat(186, 50), tidur_rumah())
soal('MC28-t9', sakit_di('demam'))
soal('MC28-t10', kue_habis())
opsi('MC28-b3', obat_oleh('adik'), obat_oleh('buang'), obat_oleh('anjing'))
opsi('MC28-b4', sakit_di('demam'), sakit_di('pilek'), sakit_di('kaki'))
opsi('MC28-b6', lantai() + orang(110, tinggi=130, jenis='laki', baju='a', kaki_pose={'ki': (-14, 0), 'ka': (30, -20)}) + bola(170, 182, 14),
     lantai() + meja(170, 150, 160) + buku(170, 150, 50, 34, 'h') + orang(80, tinggi=110, jenis='laki', duduk=150, baju='a'),
     lantai() + ranjang(150, 200, 220) + bulat(62, 132, 15) + muka(62, 132, 15, 'sakit') + kotak(78, 132, 150, 18, 'p', 6) + termometer(250, 30, 39, h=70))
soal('MC28-b7', sakit_di('pilek'))
soal('MC28-b8', lantai() + rumah_sakit(190, 200, 160, 110) + orang(60, tinggi=150, jenis='pria', baju='a', wajah='sakit'))

opsi('MC40-t8', kaki_sepatu('kecil'), kaki_sepatu('besar'), kaki_sepatu('pas'))
soal('MC40-t9', pasar_malam())
soal('MC40-t10', lantai() + toko(110, 200, 170, 120) + papan_angka(245, 60, '50%', 90, 46, uk=24))
opsi('MC40-b3', lantai() + toko(110, 200, 170, 120) + papan_angka(245, 60, '九折', 90, 46, uk=24),
     lantai() + toko(110, 200, 170, 120) + papan_angka(245, 60, '七折', 90, 46, uk=24),
     lantai() + toko(110, 200, 170, 120) + papan_angka(245, 60, '五折', 90, 46, uk=24))
opsi('MC40-b4', mal(), pasar_malam(), lantai() + rumah(150, 200, 170, 110) + bulan_bintang(250, 30, .6))
opsi('MC40-b6', antre('kosong'), antre('banyak'), antre('tutup'))
soal('MC40-b7', baju_besar())
soal('MC40-b8', lantai() + toko(220, 200, 140, 110) + orang(70, tinggi=155, jenis='wanita', baju='a', tangan={'ka': [(16, 30), (20, 50)]}) + tas_belanja(96, 196, .8)
     + orang(130, tinggi=150, jenis='wanita', baju='p', tangan={'ka': [(16, 30), (20, 50)]}) + tas_belanja(154, 196, .8))

opsi('MC58-t8', lantai() + meja(170, 150, 160) + buku_tumpuk(170, 150, 3, 60, 18) + orang(80, tinggi=120, jenis='pria', duduk=150, baju='a', wajah='gugup') + keringat(110, 70),
     lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='puas', tangan={'ki': [(20, -10), (10, -40)], 'ka': [(20, -10), (10, -40)]}) + kertas(240, 120, 50, 64) + teks(240, 160, '100', 18, angka=True),
     tidur_rumah())
soal('MC58-t9', lantai() + gunung(190, 200, 220, 140) + pohon(270, s=.5) + orang(60, tinggi=150, jenis='wanita', baju='a', wajah='kaget', tangan={'ka': [(20, -20), (34, -40)]}))
soal('MC58-t10', lantai() + kotak(170, 110, 80, 70, 'a', 4) + kotak(162, 100, 96, 16, 'p', 3) + garis((210, 100), (210, 180), lebar=8) + jalur('M210 100 q-24 -26 -30 -4 q14 6 30 4 q24 -26 30 -4 q-14 6 -30 4', 'p')
     + orang(80, tinggi=160, jenis='wanita', baju='p', wajah='tawa'))
opsi('MC58-b3', lantai() + ''.join(uang(150, 170 - i * 26, '1000', 150, 60) for i in range(3)),
     lantai() + ''.join(uang(80, 170 - i * 26, '1000', 110, 48) for i in range(3)) + gedung(170, 200, 3, None, 50, 22) + garis((200, 196), (226, 196), k='t') + rumah(250, 200, 60, 50),
     lantai() + gedung(110, 200, 3, None, 60, 26) + garis((146, 196), (190, 196), k='t') + rumah(230, 200, 80, 60))
opsi('MC58-b4', lantai() + meja(170, 150, 160) + kertas(170, 110, 60, 40) + orang(80, tinggi=120, jenis='pria', duduk=150, baju='a', wajah='gugup'),
     lantai() + orang(110, tinggi=165, jenis='pria', baju='a', wajah='sedih', tangan={'ka': [(26, 0), (56, -6)]}) + dompet(200, 90, 1.2),
     lantai() + anjing(170, 196, 1.2) + termometer(260, 50, 39, h=70) + orang(60, tinggi=150, jenis='pria', baju='a', wajah='sedih'))
opsi('MC58-b6', lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='nangis'), lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='tawa'),
     lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='marah'))
soal('MC58-b7', lantai() + meja(200, 150, 140) + kue_ultah(200, 150, '', .8) + orang(70, tinggi=160, jenis='pria', baju='a', wajah='kaget')
     + ''.join(bulat(x, y, 3, 'h') for x, y in ((140, 30), (170, 50), (220, 26), (250, 60), (120, 70))))
soal('MC58-b8', lantai() + sofa(150, 200, 180) + orang(150, tinggi=140, jenis='pria', duduk=152, baju='a', wajah='puas') + matahari(260, 30, 14, 'p'))


def main():
    """Tulis img/soal/<kunci>.svg + _kerja/mini/gambar_bab_label.json (keterangan saat digambar) + lembar periksa."""
    import json, os
    from svg_lib import bungkus
    K = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); R = os.path.dirname(K)
    bank = json.load(open(f'{R}/data/bank_soal.json', encoding='utf-8'))
    label, kartu = {}, ''
    for v in (1, 2, 3):
        for m in json.load(open(f'{R}/data/modul_vol{v}.json', encoding='utf-8'))['modules']:
            for k, daftar in (('t', m['tasks']), ('b', bank.get(m['code'], []))):
                for i, t in enumerate(daftar, 1):
                    kunci = f'M{m["code"]}-{k}{i}'
                    if kunci not in G and kunci + 'a' not in G:
                        continue
                    naskah = ' '.join(l['zh'] for l in t.get('lines', [])) + (f' 問：{t["question"]}' if t.get('question') else '') + ' ' + t.get('text', '')
                    isi = ''
                    if t.get('picture') and not t['picture'].get('img'):
                        if kunci not in G: print('BELUM ADA GAMBAR', kunci)
                        label[kunci] = t['picture']['label']
                        isi += f'<figure><img src="../../img/soal/{kunci}.svg"><figcaption>gambar soal · {t["picture"]["label"]}</figcaption></figure>'
                    pil = [o for o in t.get('options', []) if isinstance(o, dict)]
                    for j, o in enumerate(pil):
                        kk = kunci + 'abc'[j]
                        if kk not in G: print('BELUM ADA GAMBAR', kk)
                        label[kk] = o['label']
                        isi += (f'<figure class="{"ok" if j == t.get("answer") else ""}"><img src="../../img/soal/{kk}.svg">'
                                f'<figcaption>{"ABC"[j]}{" ✔" if j == t.get("answer") else ""} · {o["label"]}</figcaption></figure>')
                    if not pil:
                        isi += f'<p>{" / ".join(("✔ " if j == t["answer"] else "") + o for j, o in enumerate(t["options"]))}</p>'
                    kartu += f'<section><h4>{kunci} · {t["type"]} — {naskah}</h4><div>{isi}</div></section>'
    for kunci, isi in G.items():
        open(f'{R}/img/soal/{kunci}.svg', 'w', encoding='utf-8').write(bungkus(isi))
    json.dump(label, open(f'{K}/mini/gambar_bab_label.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    open(f'{K}/gambar/periksa_bab_mini.html', 'w', encoding='utf-8').write(
        '<!doctype html><meta charset="utf-8"><style>body{font-family:sans-serif;margin:10px}section{border-top:2px solid #888}'
        'section h4{margin:6px 0;font-size:13px}section div{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}'
        'figure{margin:0;border:1px solid #ccc;padding:4px}figure.ok{border:3px solid #1e9e62}img{width:100%}figcaption{font-size:12px}</style>' + kartu)
    print(f'{len(G)} gambar ditulis; keterangan: _kerja/mini/gambar_bab_label.json; lembar periksa: _kerja/gambar/periksa_bab_mini.html')


if __name__ == '__main__':
    main()
