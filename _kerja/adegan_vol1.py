"""Adegan ilustrasi 聽力 Part 1 — Volume 1 (A01–A25). ID = <modul>-<n> (listen_pic ke-n, urut isi → soal → bank)."""
from svg_adegan import *

A = {}

# A01 — sapaan & nama (tulis ulang 2026-11-13: A01-1..3 latihan; A01-4/5 Tes Bab tetap; L* = opsi/gambar latihan, T* = Tes Bab)
def tanda_nama(x, atas, nama, uk=18):
    """Papan nama tergantung di leher (atas = y tepi atas papan)."""
    w, h = len(nama) * uk + 14, uk + 12
    return (garis((x - 5, atas - 12), (x - w / 3, atas), k='t') + garis((x + 5, atas - 12), (x + w / 3, atas), k='t')
            + kotak(x - w / 2, atas, w, h, 'p', 3) + teks(x, atas + h - 8, nama, uk))


def formulir(x, y, nama, w=150, h=74):
    return (kotak(x - w / 2, y, w, h, 'p', 4) + teks(x - w / 2 + 10, y + 30, '姓名：', 20, anchor='start')
            + teks(x - w / 2 + 70, y + 30, nama, 22, anchor='start')
            + garis((x - w / 2 + 64, y + 36), (x + w / 2 - 8, y + 36), k='t')
            + garis((x - w / 2 + 10, y + 52), (x + w / 2 - 10, y + 52), k='t') + garis((x - w / 2 + 10, y + 64), (x + w / 2 - 40, y + 64), k='t'))


def orang_bernama(x, nama, jenis='pria', tangan=None, uk=18, baju=None, tinggi=160):
    baju = baju or ('a' if jenis in ('wanita', 'gadis') else 'h')
    atas = 200 - tinggi + tinggi * .085 * 2.35 + 24
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan=tangan) + tanda_nama(x, atas, nama, uk)


PEGANG = {'ka': [(22, 18), (48, 4)]}
A['A01-1'] = lantai() + matahari(235, 55, 24) + garis((200, 110), (270, 110), k='t') + orang_bernama(115, '陳', tangan=LAMBAI, uk=22)
A['A01-2'] = lantai() + orang(95, tinggi=160, jenis='wanita', baju='a', tangan=PEGANG) + kartu_nama(205, 70, '林安妮', 150, 84)
A['A01-3'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='h', tangan=PEGANG) + formulir(205, 60, '張志明')
A['A01-4'] = lantai() + jalur('M16 200 Q150 190 284 200', 't') + matahari(230, 70, 22) + garis((190, 118), (270, 118), k='t') + orang(110, tinggi=160, jenis='pria', baju='h', tangan=LAMBAI)
A['A01-5'] = (lantai() + orang(95, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, 18), (48, 4)]})
              + kartu_nama(205, 70, '陳', 130, 80))
# latihan 聽力 Part 2 (opsi gambar)
A['A01-L4a'] = lantai() + orang_bernama(150, '張安妮', 'pria')
A['A01-L4b'] = lantai() + orang_bernama(150, '張安安', 'wanita')
A['A01-L4c'] = lantai() + orang_bernama(150, '張安妮', 'wanita')
A['A01-L5a'] = lantai() + orang_bernama(150, '林', 'pria', uk=24)
A['A01-L5b'] = lantai() + orang_bernama(150, '林', 'wanita', uk=24)
A['A01-L5c'] = lantai() + orang_bernama(150, '李', 'pria', uk=24)
# latihan 聽力 Part 3
A['A01-L6a'] = kartu_nama(150, 62, '王安妮', 210, 100)
A['A01-L6b'] = kartu_nama(150, 62, '李安妮', 210, 100)
A['A01-L6c'] = kartu_nama(150, 62, '李大文', 210, 100)
# latihan 閱讀 Part 1: malam/pagi × nona/bapak, melambai di pintu (berpisah)
def pisah(jenis, malam):
    langit = bulan_bintang(245, 45, .7) if malam else matahari(245, 50, 22)
    return lantai() + pintu(70) + langit + orang(150, tinggi=155, jenis=jenis, baju='a' if jenis == 'wanita' else 'h', tangan=LAMBAI)
A['A01-L8a'] = pisah('wanita', True)
A['A01-L8b'] = pisah('wanita', False)
A['A01-L8c'] = pisah('pria', True)
# latihan 閱讀 Part 2 & 3
A['A01-L9'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan=PEGANG) + formulir(205, 60, '林美美')
A['A01-L10'] = (lantai() + orang(95, tinggi=165, jenis='wanita', baju='a', tangan={'ka': [(20, 14), (44, 4)]})
                + orang(215, tinggi=100, jenis='laki', baju='h') + gelembung(170, 45, 70, 50, teks(170, 58, '？', 34), (-1, 1)))
# Tes Bab 聽力 Part 2 & 3 (opsi gambar)
A['A01-T3a'] = kartu_nama(150, 62, '李', 170, 100)
A['A01-T3b'] = kartu_nama(150, 62, '林', 170, 100)
A['A01-T3c'] = kartu_nama(150, 62, '王', 170, 100)
for s, m in zip('abc', '陳林王'):
    A[f'A01-T4{s}'] = lantai() + orang_bernama(150, m, 'pria', uk=24)
# Tes Bab 閱讀 Part 1: berpisah nona / berkenalan (jabat tangan) bapak / berpisah bapak
A['A01-T6a'] = pisah('wanita', False)
A['A01-T6b'] = (lantai() + orang(105, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(16, 26), (40, 34)]})
                + orang(195, tinggi=155, jenis='pria', baju='p', tangan={'ki': [(16, 26), (40, 34)]}))
A['A01-T6c'] = pisah('pria', False)
# Tes Bab 閱讀 Part 2: Pak Wang memberi buku, nona menerima
A['A01-T7'] = (lantai() + orang_bernama(95, '王', 'pria', tangan={'ka': [(22, 20), (52, 22)]}, uk=22)
               + orang(215, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(20, 22), (46, 26)]}) + buku(155, 118, 34, 40))
A['A01-T8'] = kartu_nama(150, 62, '王大文', 210, 100)

# A02 — asal & bahasa (tulis ulang 2026-11-13: A02-1..3 latihan; A02-4/5 = Tes Bab lama A02-2/3; L* latihan, T* Tes Bab)
# Paspor = buku generik bertuliskan nama negara (Inggris), BUKAN tiruan sampul paspor asli.
def paspor(x, y, negara, w=64, h=86):
    uk = 13 if len(negara) <= 6 else 10
    return (kotak(x - w / 2, y, w, h, 'h', 4) + teks(x, y + 24, 'PASSPORT', 9, angka=True, warna='#fff')
            + bulat(x, y + 46, 11, 'w') + teks(x, y + h - 10, negara, uk, angka=True, warna='#fff'))


def ucap(x, y, s, w=130, h=62, ekor=(-1, 1)):
    latin = s.isascii()
    uk = min(28, (w - 18) / (len(s) * .62)) if latin else min(30, (w - 18) / len(s))
    return gelembung(x, y, w, h, teks(x, y + uk * .38, s, round(uk), angka=latin), ekor)


PEGANG_P = {'ka': [(20, 20), (42, 14)]}


def orang_paspor(x, negara, jenis='pria', tinggi=160, kata=None):
    baju = 'a' if jenis == 'wanita' else 'h'
    o = lantai() + orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan=PEGANG_P) + paspor(x + 66, 200 - tinggi + 44, negara)
    if kata:
        o += ucap(x + 120, 48, kata, 110, 54)
    return o


def bicara(x, kata, jenis='pria', tinggi=160, kanan=True):
    baju = 'a' if jenis == 'wanita' else 'h'
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju) + ucap(x + (70 if kanan else -70), 40, kata, 128, 54, (-1 if kanan else 1, 1))


def dua_bicara(kiri, kanan):
    """Dua orang berjauhan, gelembung masing-masing di atas kepala ke arah tengah. kiri/kanan = (jenis, kata)."""
    o = lantai()
    for (jenis, kata), x, bx, ek in ((kiri, 40, 98, (-1, 1)), (kanan, 260, 202, (1, 1))):
        o += orang(x, tinggi=140 if jenis == 'pria' else 134, jenis=jenis, baju='a' if jenis == 'wanita' else 'h')
        o += ucap(bx, 30, kata, 96, 46, ek)
    return o


A['A02-1'] = dua_bicara(('wanita', 'Hello!'), ('pria', '你好！'))
A['A02-2'] = orang_paspor(110, 'INDONESIA')
A['A02-3'] = orang_paspor(110, 'JAPAN', 'wanita', 155)
A['A02-4'] = lantai() + orang(90, tinggi=155, jenis='wanita', wajah='kaget', baju='a') + gelembung(205, 70, 140, 70, teks(205, 82, 'Hello!', 30, angka=True), (-1, 1))
A['A02-5'] = lantai() + orang(110, tinggi=160, jenis='pria', tangan={'ka': [(16, -8), (22, -40)]}) + bendera_taiwan(146, 24, 126, 84)
# latihan
A['A02-L4a'] = orang_paspor(110, 'USA', 'wanita', 155)
A['A02-L4b'] = orang_paspor(110, 'JAPAN')
A['A02-L4c'] = orang_paspor(110, 'USA')
A['A02-L5a'] = lantai() + bicara(90, 'こんにちは', 'wanita', 155)
A['A02-L5b'] = lantai() + bicara(90, 'Hello!', 'wanita', 155)
A['A02-L5c'] = lantai() + bicara(90, 'こんにちは', 'pria', 160)
A['A02-L6a'] = paspor(150, 40, 'TAIWAN', 110, 150)
A['A02-L6b'] = paspor(150, 40, 'INDONESIA', 110, 150)
A['A02-L6c'] = paspor(150, 40, 'USA', 110, 150)
A['A02-L8a'] = dua_bicara(('pria', '你好！'), ('wanita', 'Hello!'))
A['A02-L8b'] = dua_bicara(('pria', '你好！'), ('wanita', '你好！'))
A['A02-L8c'] = dua_bicara(('pria', '你好！'), ('pria', '你好！'))
A['A02-L9'] = orang_paspor(70, 'KOREA', 'wanita', 155, 'Hello!')
A['A02-L10'] = (lantai() + orang(60, tinggi=165, jenis='pria', baju='h')
                + orang(190, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(18, 4), (46, -6)]})
                + orang(262, tinggi=146, jenis='wanita', baju='p') + gelembung(226, 30, 56, 40, teks(226, 42, '？', 28), (-1, 1)))
# Tes Bab
A['A02-T3a'] = paspor(150, 40, 'INDONESIA', 110, 150)
A['A02-T3b'] = paspor(150, 40, 'USA', 110, 150)
A['A02-T3c'] = paspor(150, 40, 'JAPAN', 110, 150)
A['A02-T6a'] = lantai() + bicara(90, 'Hello!', 'pria', 160)
A['A02-T6b'] = lantai() + bicara(90, '你好！', 'wanita', 155)
A['A02-T6c'] = lantai() + bicara(90, 'Hello!', 'wanita', 155)
A['A02-T7'] = orang_paspor(70, 'JAPAN', 'pria', 160, 'こんにちは')
A['A02-T8'] = orang_paspor(70, 'USA', 'pria', 160, '你好！')

# A03 — keluarga
A['A03-1'] = (kotak(40, 186, 220, 10, 'h') + garis((40, 196), (40, 210)) + garis((260, 196), (260, 210))
              + bingkai(150, 34, 120, 140, orang(150, kaki=174, tinggi=120, jenis='wanita', baju='a')))
A['A03-2'] = keluarga('adik_lk')
A['A03-3'] = keluarga('kakak_pr')
A['A03-4'] = keluarga('ibu')
A['A03-5'] = (lantai() + orang(150, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 30), (40, 54)], 'ka': [(20, 30), (40, 54)]})
              + orang(78, tinggi=90, jenis='gadis', tangan={'ka': [(8, -2), (20, -8)]}) + orang(222, tinggi=90, jenis='laki', baju='a', tangan={'ki': [(8, -2), (20, -8)]}))

# --- A03 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
ANGGOTA = {'ayah': (170, 'pria', 'h', None), 'ibu': (160, 'wanita', 'a', 'uban'), 'kakak_lk': (148, 'pria', 'a', None),
           'kakak_pr': (140, 'wanita', 'h', None), 'adik_lk': (88, 'laki', 'p', None), 'adik_pr': (86, 'gadis', 'a', None)}


def anggota(k, x, kaki=200, tangan=None, skala=1.0):
    t, j, b, rb = ANGGOTA[k]
    return orang(x, kaki=kaki, tinggi=t * skala, jenis=j, baju=b, rambut=rb, tangan=tangan)


def foto6(tunjuk):
    """Foto keluarga 6 orang dalam bingkai, panah ke satu anggota."""
    xs = dict(zip(ANGGOTA, (36, 84, 132, 180, 228, 268)))
    o = kotak(10, 8, 280, 204, 'p', 6) + garis((20, 196), (280, 196), k='t')
    for k, x in xs.items():
        o += anggota(k, x, kaki=196, skala=.9)
    t = ANGGOTA[tunjuk][0] * .9
    return o + panah(xs[tunjuk], 196 - t - 30, xs[tunjuk], 196 - t - 6, 5)


def pasangan(a, b):
    """Foto dua anggota keluarga berdampingan."""
    return kotak(40, 8, 220, 204, 'p', 6) + garis((50, 196), (250, 196), k='t') + anggota(a, 110, 196) + anggota(b, 190, 196)


for s, k in zip('abc', ('kakak_pr', 'adik_lk', 'adik_pr')):
    A[f'A03-L4{s}'] = foto6(k)
for s, (a, b) in zip('abc', (('ayah', 'ibu'), ('kakak_lk', 'kakak_pr'), ('ayah', 'adik_lk'))):
    A[f'A03-L5{s}'] = pasangan(a, b)
for s, k in zip('abc', ('ayah', 'kakak_lk', 'adik_lk')):
    A[f'A03-L6{s}'] = foto6(k)
for s, (a, b) in zip('abc', (('kakak_lk', 'kakak_pr'), ('kakak_lk', 'adik_pr'), ('ayah', 'ibu'))):
    A[f'A03-L8{s}'] = pasangan(a, b)
A['A03-L9'] = (lantai() + anggota('kakak_pr', 120, tangan={'ka': [(14, 28), (30, 46)]})
               + anggota('adik_lk', 175, tangan={'ki': [(10, 6), (20, 10)]}))
A['A03-L10'] = (lantai() + anggota('adik_pr', 50, tangan={'ka': [(14, 0), (34, -10)]}) + anggota('kakak_lk', 160) + anggota('kakak_lk', 235))
for s, k in zip('abc', ('kakak_pr', 'adik_pr', 'adik_lk')):
    A[f'A03-T3{s}'] = foto6(k)
for s, k in zip('abc', ('ibu', 'adik_pr', 'kakak_pr')):
    A[f'A03-T4{s}'] = foto6(k)
for s, (a, b) in zip('abc', (('ayah', 'ibu'), ('adik_lk', 'adik_pr'), ('kakak_lk', 'kakak_pr'))):
    A[f'A03-T6{s}'] = pasangan(a, b)
A['A03-T7'] = (lantai() + anggota('ibu', 120, tangan={'ka': [(14, 28), (30, 52)]}) + anggota('adik_lk', 175, tangan={'ki': [(10, 6), (20, 10)]}))
A['A03-T8'] = (lantai() + anggota('adik_lk', 60, tangan={'ka': [(14, 0), (34, -10)]}) + anggota('kakak_pr', 220)
               + gelembung(80, 60, 50, 38, teks(80, 71, '？', 26), (-1, 1)))

# A04 — jumlah anggota keluarga
A['A04-1'] = (lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', tangan={'ki': [(20, 30), (40, 56)], 'ka': [(20, 30), (40, 56)]})
              + orang(86, tinggi=92, jenis='laki', tangan={'ka': [(8, -2), (18, -10)]}) + orang(214, tinggi=92, jenis='gadis', baju='h', tangan={'ki': [(8, -2), (18, -10)]}))
A['A04-2'] = lantai() + orang(70, tinggi=100, jenis='laki', baju='h') + orang(150, tinggi=92, jenis='gadis') + orang(230, tinggi=100, jenis='laki', baju='a')
A['A04-3'] = (lantai() + orang(150, tinggi=165, jenis='pria', baju='a', tangan={'ki': [(20, 30), (40, 56)], 'ka': [(20, 30), (40, 56)]})
              + orang(84, tinggi=92, jenis='gadis', tangan={'ka': [(8, -2), (18, -10)]}) + orang(216, tinggi=92, jenis='gadis', baju='h', tangan={'ki': [(8, -2), (18, -10)]}))
A['A04-4'] = lantai() + orang(70, tinggi=150, jenis='wanita', baju='a') + orang(150, tinggi=88, jenis='laki', baju='h') + orang(230, tinggi=150, jenis='wanita', baju='a')
A['A04-5'] = (lantai() + orang(120, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 30), (40, 56)]})
              + orang(190, tinggi=92, jenis='gadis', baju='h', tangan={'ki': [(8, -2), (18, -10)]}))

# --- A04 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kelompok(*org, lebar=260):
    """org = jenis: 'pria','wanita','laki','gadis','kakak_lk','kakak_pr' — berjajar rata."""
    T = {'pria': (165, 'pria', 'h'), 'wanita': (155, 'wanita', 'a'), 'laki': (90, 'laki', 'p'), 'gadis': (88, 'gadis', 'a'),
         'kakak_lk': (140, 'pria', 'a'), 'kakak_pr': (135, 'wanita', 'h')}
    n = len(org)
    jarak = min(70, lebar / max(1, n))
    x0 = 150 - jarak * (n - 1) / 2
    o = lantai()
    for i, j in enumerate(org):
        t, jen, b = T[j]
        o += orang(x0 + i * jarak, tinggi=t, jenis=jen, baju=b)
    return o


A['A04-L4a'] = kelompok('wanita', 'gadis', 'gadis')
A['A04-L4b'] = kelompok('wanita', 'gadis', 'gadis', 'gadis')
A['A04-L4c'] = kelompok('wanita', 'laki', 'laki', 'laki')
A['A04-L5a'] = kelompok('kakak_lk', 'laki')
A['A04-L5b'] = kelompok('kakak_lk', 'gadis', 'gadis')
A['A04-L5c'] = kelompok('kakak_lk', 'laki', 'laki')
A['A04-L6a'] = kelompok('kakak_pr', 'kakak_pr', 'kakak_pr')
A['A04-L6b'] = kelompok('kakak_lk', 'kakak_lk', 'kakak_lk')
A['A04-L6c'] = kelompok('pria', 'wanita', 'kakak_pr', 'kakak_pr', 'kakak_pr', 'gadis', lebar=270)
A['A04-L8a'] = kelompok('pria', 'laki', 'laki')
A['A04-L8b'] = kelompok('wanita', 'gadis', 'gadis')
A['A04-L8c'] = kelompok('wanita', 'laki', 'laki')
A['A04-L9'] = kelompok('pria', 'wanita', 'laki', 'gadis', 'gadis')
A['A04-L10'] = kelompok('gadis', 'gadis', 'gadis')
A['A04-T3a'] = kelompok('pria', 'wanita', 'kakak_lk', 'kakak_pr', 'laki', 'gadis', lebar=270)
A['A04-T3b'] = kelompok('pria', 'wanita', 'kakak_pr', 'laki', 'gadis')
A['A04-T3c'] = kelompok('pria', 'wanita', 'laki', 'gadis')
A['A04-T4a'] = kelompok('gadis', 'gadis', 'gadis')
A['A04-T4b'] = kelompok('gadis', 'gadis')
A['A04-T4c'] = kelompok('gadis')
A['A04-T6a'] = kelompok('laki', 'gadis')
A['A04-T6b'] = kelompok('laki', 'gadis', 'laki')
A['A04-T6c'] = kelompok('gadis')
A['A04-T7'] = kelompok('pria', 'wanita', 'laki', 'laki')
A['A04-T8'] = kelompok('pria', 'gadis')

# A05 — tanggal, umur
A['A05-1'] = kalender_bulan(150, 40, 5, 3, 150, 150) + kue_ultah(235, 196, s=.4)
A['A05-2'] = kue_ultah(150, 192, '18', 1.1)
A['A05-3'] = lantai() + orang(95, tinggi=165, jenis='pria', baju='h', wajah='senyum') + meja(210, 150, 120) + kue_ultah(210, 150, '40', .7)
A['A05-4'] = lantai() + orang(90, tinggi=100, jenis='gadis', baju='a', wajah='senyum') + meja(200, 150, 120) + kue_ultah(200, 150, '5', .6)
A['A05-5'] = kalender_bulan(150, 40, 10, 10, 150, 150)

# --- A05 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
kal5 = lambda b, h: kalender_bulan(150, 30, b, h, 150, 160)
kue5 = lambda n: kue_ultah(150, 190, n, 1.4)


def orang_kue(jenis, n, tinggi):
    baju = {'laki': 'p', 'gadis': 'a', 'pria': 'h', 'nenek': 'a'}[jenis]
    return lantai() + orang(85, tinggi=tinggi, jenis=jenis, baju=baju) + meja(205, 150, 130) + kue_ultah(205, 150, n, .75)


for s, n in zip('abc', ('16', '6', '60')):
    A[f'A05-L4{s}'] = kue5(n)
for s, (b, h) in zip('abc', ((10, 4), (4, 1), (4, 10))):
    A[f'A05-L5{s}'] = kal5(b, h)
for s, (b, h) in zip('abc', ((3, 20), (8, 20), (3, 10))):
    A[f'A05-L6{s}'] = kal5(b, h)
A['A05-L8a'] = orang_kue('laki', '7', 100)
A['A05-L8b'] = orang_kue('gadis', '17', 135)
A['A05-L8c'] = orang_kue('gadis', '7', 100)
A['A05-L9'] = orang_kue('pria', '21', 160)
A['A05-L10'] = (lantai() + orang(90, tinggi=155, jenis='wanita', baju='a') + orang(210, tinggi=150, jenis='wanita', baju='p')
                + gelembung(140, 40, 60, 42, teks(140, 52, '？', 28), (-1, 1)))
for s, (b, h) in zip('abc', ((8, 17), (8, 7), (7, 8))):
    A[f'A05-T3{s}'] = kal5(b, h)
for s, n in zip('abc', ('19', '21', '20')):
    A[f'A05-T4{s}'] = kue5(n)
for s, (b, h) in zip('abc', ((12, 25), (1, 1), (10, 31))):
    A[f'A05-T6{s}'] = kal5(b, h)
A['A05-T7'] = (lantai() + orang(85, tinggi=150, jenis='pria', rambut='uban', baju='a', wajah='senyum')
               + meja(205, 150, 130) + kue_ultah(205, 150, '80', .75))
A['A05-T8'] = (panah(30, 110, 272, 110, 5) + ''.join(kotak(x - 32, 74, 64, 72, 'p', 6) for x in (55, 150, 245))
               + teks(55, 120, '去年', 24) + teks(150, 120, '今年', 24) + teks(245, 124, '？', 36))

# A06 — hobi
A['A06-1'] = lantai() + orang(100, tinggi=160, jenis='pria', wajah='nyanyi', tangan={'ka': [(12, 30), (-8, -8)]}) + mikrofon(132, 62) + not_musik(190, 60) + not_musik(230, 100)
A['A06-2'] = (lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(24, -20), (36, -56)]},
                              kaki_pose={'ki': (-8, 0), 'ka': (30, -26)}) + jalur('M96 70 q-10 10 0 20 M204 70 q10 10 0 20', 't'))
A['A06-3'] = (lantai() + orang(80, tinggi=110, jenis='laki', baju='h', kaki_pose={'ki': (-12, 0), 'ka': (26, -14)}) + bola(150, 186, 14)
              + orang(225, tinggi=105, jenis='gadis', baju='a', tangan={'ki': [(20, -6), (30, -30)], 'ka': [(20, -6), (30, -30)]}))
A['A06-4'] = (lantai() + tv(250, 150, 70) + meja(250, 150, 70) + sofa(115) + orang(110, tinggi=150, jenis='pria', wajah='lelah', duduk=150, baju='a',
                                                                                    tangan={'ki': [(4, 30), (-2, 44)], 'ka': [(4, 30), (-2, 44)]}) + bola(40, 188, 12))
A['A06-5'] = lantai() + kuda_gambar(210) + orang(105, tinggi=100, jenis='gadis', baju='a', tangan={'ka': [(20, -4), (46, -14)]}) + garis((166, 90), (180, 80), lebar=3)

# --- A06 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
TB = {'pria': (160, 'h'), 'wanita': (152, 'a'), 'laki': (100, 'h'), 'gadis': (98, 'a')}


def nyanyi(x, j):
    t, b = TB[j]
    return (orang(x, tinggi=t, jenis=j, baju=b, wajah='nyanyi', tangan={'ka': [(12, t * .19), (-8, -t * .05)]})
            + mikrofon(x + 30, 200 - t * .62) + not_musik(x + 70, 200 - t * .85) + not_musik(x + 100, 200 - t * .6))


def tari(x, j):
    t, b = TB[j]
    return orang(x, tinggi=t, jenis=j, baju=b, wajah='puas', tangan={'ki': [(24, -t * .12), (36, -t * .35)], 'ka': [(24, -t * .12), (36, -t * .35)]},
                 kaki_pose={'ki': (-8, 0), 'ka': (t * .19, -t * .16)})


def main_bola(x, j):
    t, b = TB[j]
    return orang(x, tinggi=t, jenis=j, baju=b, kaki_pose={'ki': (-12, 0), 'ka': (t * .16, -t * .1)}) + bola(x + t * .32, 186, 14)


def menggambar(x, j):
    t, b = TB[j]
    return kuda_gambar(x + 95) + orang(x, tinggi=t, jenis=j, baju=b, tangan={'ka': [(20, -4), (46, -14)]}) + garis((x + 56, 200 - t * .62), (x + 70, 200 - t * .7), lebar=3)


def dengar(x, j):
    t, b = TB[j]
    r = t * .085
    cy = 200 - t + r
    return (orang(x, tinggi=t, jenis=j, baju=b, wajah='puas') + jalur(f'M{f(x - r * 1.15)} {f(cy)} Q{f(x)} {f(cy - r * 2.3)} {f(x + r * 1.15)} {f(cy)}', 'g', 4)
            + kotak(x - r * 1.4, cy - 6, 8, 14, 'h', 3) + kotak(x + r * 1.4 - 8, cy - 6, 8, 14, 'h', 3) + not_musik(x + 50, cy - 10) + not_musik(x + 80, cy + 20))


def nonton(x, j):
    t, b = TB[j]
    return tv(x + 100, 150, 90) + meja(x + 100, 150, 90) + orang(x, tinggi=t, jenis=j, baju=b, wajah='senyum')


satu = lambda fn, j, x=110: lantai() + fn(x, j)
A['A06-L4a'] = satu(nyanyi, 'pria', 90)
A['A06-L4b'] = satu(main_bola, 'pria')
A['A06-L4c'] = satu(main_bola, 'wanita')
A['A06-L5a'] = satu(menggambar, 'gadis', 90)
A['A06-L5b'] = satu(tari, 'laki', 150)
A['A06-L5c'] = satu(tari, 'gadis', 150)
A['A06-L6a'] = lantai() + nyanyi(60, 'pria') + orang(200, tinggi=150, jenis='wanita', baju='a', wajah='nyanyi') + mikrofon(226, 108)
A['A06-L6b'] = lantai() + tv(150, 110, 150) + orang(95, tinggi=120, jenis='pria', baju='h', duduk=170) + orang(205, tinggi=115, jenis='wanita', baju='a', duduk=170) + garis((60, 170), (240, 170), lebar=6)
A['A06-L6c'] = lantai() + main_bola(70, 'pria') + orang(225, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(20, -6), (30, -30)], 'ka': [(20, -6), (30, -30)]})
A['A06-L8a'] = satu(nyanyi, 'laki', 90)
A['A06-L8b'] = satu(menggambar, 'gadis', 90)
A['A06-L8c'] = satu(menggambar, 'laki', 90)
A['A06-L9'] = A['A06-L6b']
A['A06-L10'] = lantai() + tari(85, 'pria') + tari(215, 'wanita')
A['A06-T3a'] = satu(nyanyi, 'wanita', 90)
A['A06-T3b'] = satu(nonton, 'wanita', 80)
A['A06-T3c'] = satu(main_bola, 'wanita')
A['A06-T4a'] = satu(tari, 'pria', 150)
A['A06-T4b'] = satu(nyanyi, 'pria', 90)
A['A06-T4c'] = satu(dengar, 'pria', 120)
A['A06-T6a'] = lantai() + nyanyi(50, 'laki') + nyanyi(170, 'gadis')
A['A06-T6b'] = lantai() + tari(70, 'gadis') + orang(160, tinggi=100, jenis='laki', baju='h') + orang(240, tinggi=98, jenis='gadis', baju='a')
A['A06-T6c'] = lantai() + tari(55, 'gadis') + tari(150, 'laki') + tari(245, 'gadis')
A['A06-T7'] = satu(nyanyi, 'gadis', 90)
A['A06-T8'] = bola(150, 110, 60)

# A07 — rupa
A['A07-1'] = lantai() + orang(150, tinggi=170, jenis='pria', badan=.62, baju='p')
A['A07-2'] = (lantai() + orang(110, tinggi=165, jenis='pria', kacamata=True, baju='h') + orang(200, tinggi=100, jenis='laki', kacamata=True, baju='h'))
A['A07-4'] = lantai() + orang(115, tinggi=182, jenis='wanita', baju='a') + orang(205, tinggi=128, jenis='pria', baju='p')
A['A07-5'] = (lantai() + orang(105, tinggi=160, jenis='pria', baju='h') + orang(195, tinggi=160, jenis='pria', baju='a')
              + jalur('M60 40 L240 40', 't') + garis((60, 34), (60, 46), k='t') + garis((240, 34), (240, 46), k='t'))

# --- A07 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def sosok(x, jenis, tinggi, badan=1.0, baju=None, **kw):
    baju = baju or ('a' if jenis in ('wanita', 'gadis') else 'h')
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, badan=badan, **kw)


satu7 = lambda *a, **k: lantai() + pintu(245, t=140, lebar=56) + sosok(130, *a, **k)   # pintu = patokan tinggi
A['A07-3'] = lantai() + sosok(105, 'gadis', 110, baju='h') + sosok(195, 'gadis', 110, baju='h')
A['A07-L4a'] = satu7('pria', 165, .6)
A['A07-L4b'] = satu7('pria', 165, 1.8)
A['A07-L4c'] = satu7('wanita', 160, .6)
A['A07-L5a'] = satu7('gadis', 110, 1.8)
A['A07-L5b'] = satu7('gadis', 110, 1.0)
A['A07-L5c'] = satu7('gadis', 110, .55)
A['A07-L6a'] = satu7('pria', 175)
A['A07-L6b'] = satu7('laki', 90)
A['A07-L6c'] = satu7('gadis', 90)
A['A07-L8a'] = satu7('pria', 175, 1.8)
A['A07-L8b'] = satu7('pria', 175, .6)
A['A07-L8c'] = satu7('pria', 115, .6)
A['A07-L9'] = lantai() + sosok(110, 'gadis', 140) + sosok(190, 'laki', 90)
A['A07-L10'] = lantai() + sosok(110, 'wanita', 155, kacamata=True) + sosok(195, 'gadis', 100, kacamata=True)
A['A07-T3a'] = satu7('pria', 120)
A['A07-T3b'] = satu7('wanita', 115)
A['A07-T3c'] = satu7('wanita', 180)
A['A07-T4a'] = satu7('pria', 170)
A['A07-T4b'] = satu7('gadis', 95)
A['A07-T4c'] = satu7('wanita', 160, rambut='uban')
A['A07-T6a'] = satu7('gadis', 100, 1.8)
A['A07-T6b'] = satu7('gadis', 100, .55)
A['A07-T6c'] = satu7('wanita', 175, .55)
A['A07-T7'] = lantai() + sosok(110, 'pria', 180) + sosok(195, 'wanita', 120)
A['A07-T8'] = (satu7('wanita', 165, wajah='puas') + bintang(80, 60, 10) + bintang(225, 50, 12) + bintang(235, 110, 8))

# A08 — tempat tinggal
A['A08-1'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(125, tinggi=145, jenis='wanita', baju='a') + orang(178, tinggi=150, jenis='pria', baju='h')
A['A08-2'] = lantai_kamar() + jendela(150, 40, 70, 50) + ranjang(95, 200, 130) + orang(215, tinggi=145, jenis='pria', baju='a')
A['A08-3'] = lantai() + gedung(120, tingkat=7, sorot=5) + panah(222, 200 - 5 * 24 + 11, 172, 200 - 5 * 24 + 11, 4) + teks(252, 200 - 5 * 24 + 20, '5F', 26, angka=True)
A['A08-4'] = lantai() + gedung(120, tingkat=10, sorot=10, tt=18) + panah(222, 200 - 10 * 18 + 9, 172, 200 - 10 * 18 + 9, 4) + teks(256, 200 - 10 * 18 + 18, '10F', 24, angka=True)
A['A08-5'] = lantai() + rumah(95) + pohon(250) + matahari(250, 40, 14) + orang(190, tinggi=140, jenis='wanita', baju='a')

# --- A08 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def lantai_n(n):
    tk = min(max(n + 1, 6), 20)
    tt = min(24, 180 / tk)
    y = 200 - n * tt + tt / 2
    return (lantai() + gedung(120, tingkat=tk, sorot=n, tt=tt) + panah(222, y, 172, y, 4) + teks(254, y + 9, f'{n}F', 24, angka=True))


def taman(*isi):
    return lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + ''.join(isi)


kamar = lambda *isi: lantai_kamar() + jendela(150, 40, 70, 50) + ranjang(90, 200, 120) + ''.join(isi)
for s, n in zip('abc', (7, 19, 9)):
    A[f'A08-L4{s}'] = lantai_n(n)
A['A08-L5a'] = lantai() + pintu(110, t=150, lebar=70) + orang(190, tinggi=100, jenis='gadis', baju='a')
A['A08-L5b'] = kamar(orang(215, tinggi=100, jenis='gadis', baju='a'))
A['A08-L5c'] = taman(orang(200, tinggi=100, jenis='gadis', baju='a'))
A['A08-L6a'] = taman(orang(195, tinggi=145, jenis='wanita', baju='a'))
A['A08-L6b'] = lantai() + rumah(100) + orang(190, tinggi=145, jenis='wanita', baju='a', tangan={'ki': [(14, -20), (24, -50)]})
A['A08-L6c'] = lantai_kamar() + sofa(110) + tv(240, 150, 60) + meja(240, 150, 60) + orang(110, tinggi=135, jenis='wanita', baju='a', duduk=160)
A['A08-L8a'] = lantai() + pintu(100, t=150, lebar=70) + teks(100, 70, '房間', 20) + orang(190, tinggi=100, jenis='gadis', baju='a')
A['A08-L8b'] = kamar(orang(215, tinggi=100, jenis='gadis', baju='a'))
A['A08-L8c'] = lantai() + pintu(100, t=150, lebar=70) + teks(100, 70, '房間', 20) + orang(190, tinggi=102, jenis='laki', baju='h')
A['A08-L9'] = taman(orang(205, tinggi=100, jenis='gadis', baju='a', tangan={'ki': [(20, -6), (30, -30)], 'ka': [(20, -6), (30, -30)]}))
A['A08-L10'] = (lantai() + gedung(85, tingkat=7, lebar=100) + orang(210, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(18, 0), (40, -16)]})
                + gelembung(250, 40, 56, 40, teks(250, 52, '？', 28), (-1, 1)))
A['A08-T3a'] = lantai() + gedung(150, tingkat=8, lebar=110, tt=22)
A['A08-T3b'] = lantai() + rumah(85) + gedung(225, tingkat=3, lebar=110) + kotak(190, 108, 70, 18, 'p') + teks(225, 122, 'SCHOOL', 13, angka=True) + garis((225, 108), (225, 92), (245, 98), (225, 104))
A['A08-T3c'] = lantai() + rumah(85) + pohon(212, s=.9) + pohon(268, s=.8)
for s, n in zip('abc', (2, 3, 13)):
    A[f'A08-T4{s}'] = lantai_n(n)
A['A08-T6a'] = lantai() + rumah(90) + pohon(212, s=.9) + pohon(268, s=.8)
A['A08-T6b'] = lantai() + rumah(150)
A['A08-T6c'] = kamar()
A['A08-T7'] = lantai() + pintu(150, t=150, lebar=72) + jalan_kaki(120, 'pria', 150, 'h')
A['A08-T8'] = (lantai() + rumah(220) + orang(80, tinggi=150, jenis='pria', baju='h')
               + gelembung(120, 40, 56, 40, teks(120, 52, '？', 28), (-1, 1)))

# A09 — letak benda
A['A09-1'] = lantai() + meja(150, 128, 160) + tv(150, 128, 116)
A['A09-2'] = lantai() + meja(110, 120, 140) + kursi(242)
A['A09-3'] = lantai() + ranjang(105, 200, 170) + meja(245, 158, 70) + tv(245, 158, 76)
A['A09-4'] = lantai() + meja(150, 110, 200) + bola(125, 186, 13) + bola(170, 186, 13)
A['A09-5'] = (lantai() + kursi(186, 176, arah=-1, s=.75) + orang(120, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(22, 14), (46, 18)]}))

# --- A09 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
# "di depan" = digambar belakangan & menutupi sebagian (lebih dekat ke penonton); "di belakang" = tertutup sebagian.
MJ = lambda x=150, w=130: meja(x, 140, w)           # meja: permukaan y=140
KS = lambda x, s=.8, arah=1: kursi(x, arah=arah, s=s)  # kursi: dudukan y≈152
RJ = lambda x=150, w=180: ranjang(x, lebar=w)      # ranjang: kasur y≈148
TVo = lambda x, bawah, w=70: tv(x, bawah, w)
A['A09-L4a'] = lantai() + KS(150, 1) + bola(150, 186, 13)
A['A09-L4b'] = lantai() + KS(150, 1) + bola(150, 126, 13)
A['A09-L4c'] = lantai() + MJ() + bola(150, 186, 13)
A['A09-L5a'] = lantai() + pintu(150, t=160, lebar=80) + orang(150, kaki=205, tinggi=95, jenis='laki', baju='h')
A['A09-L5b'] = (lantai() + orang(198, tinggi=95, jenis='laki', baju='h') + kotak(70, 40, 80, 160, 'p') + jalur('M150 40 L200 30 L200 210 L150 200 Z', 'p')
                + bulat(188, 120, 3.5, 'h'))
A['A09-L5c'] = lantai() + RJ(120, 170) + orang(245, tinggi=95, jenis='laki', baju='h')
A['A09-L6a'] = lantai() + MJ() + TVo(150, 140)
A['A09-L6b'] = lantai() + MJ() + TVo(150, 200, 64)
A['A09-L6c'] = lantai() + RJ(110, 170) + TVo(245, 200, 64)
A['A09-L8a'] = lantai() + RJ(150, 170) + kursi(160, lantai_y=214, s=.95)
A['A09-L8b'] = lantai() + RJ() + KS(150, .55)
A['A09-L8b'] = lantai() + RJ() + kursi(150, lantai_y=150, s=.55)
A['A09-L8c'] = lantai() + RJ(150, 170) + meja(160, 160, 110, tinggi=54)
A['A09-L9'] = lantai() + MJ(130) + TVo(130, 140) + KS(245, .8, -1)
A['A09-L10'] = lantai() + MJ(120, 140) + orang(240, tinggi=100, jenis='laki', baju='h')
A['A09-T3a'] = lantai() + RJ(130, 180) + TVo(140, 216, 70)
A['A09-T3b'] = lantai() + MJ() + TVo(150, 140)
A['A09-T3c'] = lantai() + KS(90, .8) + TVo(200, 200, 64)
A['A09-T4a'] = lantai() + KS(150, 1) + bola(150, 126, 13)
A['A09-T4b'] = lantai() + RJ() + bola(150, 186, 13)
A['A09-T4c'] = lantai() + MJ() + bola(150, 126, 13)
A['A09-T6a'] = lantai() + KS(150, .8) + MJ(150, 120)
A['A09-T6b'] = lantai() + MJ(150, 120) + kursi(150, lantai_y=140, s=.55)
A['A09-T6c'] = lantai() + MJ(150, 120) + kursi(150, lantai_y=212, s=.8)
A['A09-T7'] = lantai() + RJ() + bola(150, 134, 13)
A['A09-T8'] = lantai() + KS(55, .8, -1) + MJ(150, 120) + KS(245, .8, 1)

# A10 — jam
A['A10-1'] = jam_dinding(150, 110, 88, 7, 30)
A['A10-2'] = jam_dinding(150, 110, 88, 10, 0)
A['A10-3'] = (lantai_kamar() + jendela(215, 36, 60, 46) + bulan_bintang(212, 58, .45) + ranjang(110, 200, 170)
              + bulat(56, 136, 13) + muka(56, 136, 13, 'tidur') + jalur('M42 131 q2 -18 16 -18 q12 0 13 14', 'h') + jam_dinding(230, 150, 30, 11, 0) + teks(92, 110, 'z z', 18, angka=True))
A['A10-4'] = weker(120, 110, 70, 6, 0) + matahari(245, 60, 18)
A['A10-5'] = jam_dinding(150, 110, 88, 12, 30)

# --- A10 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def jam10(j, m, langit=None):
    o = jam_dinding(150, 110, 88, j, m) + teks(150, 69, '12', 17, angka=True) + teks(150, 165, '6', 17, angka=True) + teks(199, 116, '3', 17, angka=True) + teks(101, 116, '9', 17, angka=True)
    if langit == 'malam':
        o += bulan_bintang(262, 36, .6)
    elif langit == 'pagi':
        o += matahari(262, 36, 16)
    return o


def tidur(jenis='gadis', malam=True, j=10, m=0):
    t = 100 if jenis in ('gadis', 'laki') else 150
    o = lantai_kamar() + jendela(115, 40, 66, 48) + (bulan_bintang(115, 64, .45) if malam else matahari(115, 64, 12)) + ranjang(110, 200, 170)
    o += (jalur('M60 128 Q58 146 50 150 L94 150 Q86 146 84 128 Z', 'h') if jenis in ('wanita', 'gadis') else '')
    o += kotak(84, 134, 104, 16, 'a', 7) + bulat(72, 132, 12) + jalur('M60 130 Q62 116 72 118 Q84 116 84 128', 'h') + muka(72, 132, 12, 'tidur')
    o += teks(96, 112, 'z', 16, angka=True) + teks(108, 98, 'Z', 20, angka=True)
    return o + jam_dinding(228, 72, 36, j, m)


def bangun(jenis='pria', malam=False, j=2, m=0):
    return (lantai_kamar() + jendela(115, 40, 66, 48) + (bulan_bintang(115, 64, .45) if malam else matahari(115, 64, 12)) + ranjang(110, 200, 170)
            + orang(110, kaki=170, tinggi=100, jenis=jenis, baju='a' if jenis == 'wanita' else 'h', wajah='lelah', tangan={'ki': [(14, -24), (20, -50)], 'ka': [(14, -24), (20, -50)]})
            + jam_dinding(228, 72, 36, j, m))


A['A10-L4a'] = jam10(6, 0)
A['A10-L4b'] = jam10(7, 30)
A['A10-L4c'] = jam10(6, 30)
A['A10-L5a'] = jam10(3, 15)
A['A10-L5b'] = jam10(3, 50)
A['A10-L5c'] = jam10(5, 15)
A['A10-L6a'] = jam10(7, 0)
A['A10-L6b'] = jam10(8, 0)
A['A10-L6c'] = jam10(7, 30)
A['A10-L8a'] = jam10(8, 10, 'malam')
A['A10-L8b'] = jam10(8, 10, 'pagi')
A['A10-L8c'] = jam10(10, 8, 'malam')
A['A10-L9'] = tidur('gadis', True, 10, 0)
A['A10-L10'] = jam10(4, 30)
A['A10-T3a'] = tidur('wanita', True, 10, 0)
A['A10-T3b'] = tidur('wanita', True, 11, 0)
A['A10-T3c'] = bangun('wanita', False, 10, 0)
A['A10-T4a'] = jam10(10, 30)
A['A10-T4b'] = jam10(10, 0)
A['A10-T4c'] = jam10(9, 50)
A['A10-T6a'] = tidur('pria', True, 10, 0)
A['A10-T6b'] = tidur('pria', False, 2, 0)
A['A10-T6c'] = bangun('pria', False, 2, 0)
A['A10-T7'] = tidur('pria', True, 11, 0)
A['A10-T8'] = jam10(12, 30) + jalur('M150 110 L150 32 A78 78 0 0 1 150 188 Z', 'a')

# A11 — hari
A['A11-1'] = kalender_minggu(150, 70, 5, 6, 280).replace('>日<', '>日<')   # urutan diganti di bawah
A['A11-2'] = lantai() + bioskop(200) + orang(70, tinggi=140, jenis='wanita', baju='a') + orang(120, tinggi=150, jenis='pria', baju='h')
A['A11-3'] = kalender_minggu(150, 70, 2, 3, 280)
A['A11-4'] = kalender_minggu(150, 70, 1, 0, 280)
A['A11-5'] = lantai() + pohon(215) + pohon(270, s=.8) + bangku(240) + jalan_kaki(70, 'wanita', 140, 'a') + jalan_kaki(125, 'pria', 150, 'h') + panah(150, 60, 196, 60, 4)

# --- A11 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
NM = '一二三四五六日'


def minggu(y, hari_ini=None, sorot=(), ikon=None, tanda=(), judul=None, w=280, x=150):
    """Satu baris minggu (Senin dulu). sorot = indeks dilingkari; tanda = indeks diberi ikon film kecil."""
    lw = w / 7
    o = kotak(x - w / 2, y, w, 64, 'p', 4) + kotak(x - w / 2, y, w, 22, 'h', 4)
    if judul:
        o += teks(x - w / 2 + 2, y - 7, judul, 15, anchor='start')
    for i, n in enumerate(NM):
        cx = x - w / 2 + lw * (i + .5)
        o += teks(cx, y + 17, n, 15, warna='#fff')
        if i:
            o += garis((x - w / 2 + lw * i, y + 22), (x - w / 2 + lw * i, y + 64), k='t')
        if i == hari_ini:
            o += teks(cx, y + 50, '今天', 14)
        if i in sorot:
            o += bulat(cx, y + 43, 17, 't') + bulat(cx, y + 43, 19, 'g')
        if i in tanda:
            o += gulungan_film(cx, y + 43, 11)
    return o


satu11 = lambda **k: minggu(78, **k)
A['A11-L4a'] = satu11(sorot=(1, 3))
A['A11-L4b'] = satu11(sorot=(0, 2))
A['A11-L4c'] = satu11(sorot=(1, 5))
A['A11-L5a'] = lantai() + tv(225, 150, 80) + meja(225, 150, 80) + orang(100, tinggi=150, jenis='wanita', baju='a')
A['A11-L5b'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(150, tinggi=150, jenis='wanita', baju='a')
A['A11-L5c'] = (lantai_kamar() + ranjang(150, 200, 190) + kotak(110, 134, 104, 16, 'a', 7) + jalur('M86 128 Q84 146 76 150 L120 150 Q112 146 110 128 Z', 'h')
                + bulat(98, 132, 12) + muka(98, 132, 12, 'tidur') + teks(122, 110, 'Z', 20, angka=True))
A['A11-L6a'] = minggu(30, hari_ini=3, sorot=(5,), judul='這個星期') + minggu(122, judul='下星期')
A['A11-L6b'] = minggu(30, hari_ini=3, sorot=(6,), judul='這個星期') + minggu(122, judul='下星期')
A['A11-L6c'] = minggu(30, hari_ini=3, judul='這個星期') + minggu(122, sorot=(5,), judul='下星期')
A['A11-L8a'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(150, tinggi=100, jenis='gadis', baju='a')
A['A11-L8b'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(120, tinggi=128, jenis='gadis', baju='h') + orang(175, tinggi=98, jenis='gadis', baju='a')
A['A11-L8c'] = lantai() + bioskop(205) + orang(80, tinggi=128, jenis='gadis', baju='h') + orang(125, tinggi=98, jenis='gadis', baju='a')
A['A11-L9'] = satu11(hari_ini=0, sorot=(2,), tanda=(2,))
A['A11-L10'] = satu11() + teks(150, 190, '？', 40)
A['A11-T3a'] = satu11(tanda=(1, 4, 6))
A['A11-T3b'] = satu11(tanda=(0, 1, 2, 3, 4, 5, 6))
A['A11-T3c'] = satu11()
A['A11-T4a'] = satu11(hari_ini=3, sorot=(4,))
A['A11-T4b'] = satu11(hari_ini=3, sorot=(3,))
A['A11-T4c'] = satu11(hari_ini=3, sorot=(5,))
A['A11-T6a'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(120, tinggi=150, jenis='pria', baju='h') + orang(178, tinggi=145, jenis='wanita', baju='a')
A['A11-T6b'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(150, tinggi=150, jenis='pria', baju='h')
A['A11-T6c'] = lantai() + bioskop(205) + orang(80, tinggi=150, jenis='pria', baju='h')
A['A11-T7'] = minggu(30, hari_ini=2, judul='這個星期') + minggu(122, sorot=(4,), tanda=(4,), judul='下星期')
A['A11-T8'] = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a') + orang(210, tinggi=155, jenis='pria', baju='h') + gelembung(140, 40, 56, 40, teks(140, 52, '？', 28), (-1, 1))

# A12 — sekolah
A['A12-1'] = ruang_kelas(guru=True)
A['A12-2'] = (lantai() + papan_tulis(150, 16, 170, 56) + murid_belakang(60, 200, 100) + meja_kelas(60) + murid_belakang(150, 200, 100, 'gadis') + meja_kelas(150)
              + murid_belakang(240, 200, 100) + meja_kelas(240))
A['A12-3'] = lantai() + orang(150, tinggi=140, jenis='laki', baju='a', tangan={'ka': [(10, 20), (-6, 34)]}) + buku(170, 146, 28, 38, 'h') + tas_punggung(116, 100)
A['A12-4'] = (lantai() + papan_tulis(95, 30, 150, 80) + mimbar(225) + orang(225, kaki=200, tinggi=175, jenis='wanita', baju='a', tangan={'ki': [(14, -14), (40, -34)]}, kacamata=True)
              + mimbar(225))
A['A12-5'] = (lantai() + pintu(60, 200, 140, 64) + lonceng(220, 58, .7) + tas_punggung(128, 116, .8) + jalan_kaki(150, 'laki', 110, 'h')
              + tas_punggung(200, 118, .8) + jalan_kaki(222, 'gadis', 105, 'a'))

# --- A12 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def jam12(j, m, langit=None):
    o = jam_dinding(150, 110, 88, j, m) + teks(150, 69, '12', 17, angka=True) + teks(150, 165, '6', 17, angka=True) + teks(199, 116, '3', 17, angka=True) + teks(101, 116, '9', 17, angka=True)
    return o + (matahari(262, 36, 16) if langit == 'pagi' else '')


def guru(x, jenis='wanita', papan=True):
    return (papan_tulis(x + 70, 30, 120, 70) if papan else '') + orang(x, tinggi=155, jenis=jenis, baju='a' if jenis == 'wanita' else 'h', tangan={'ka': [(20, -10), (44, -30)]})


def murid(x, jenis='laki', buku_=False):
    return orang(x, tinggi=105, jenis=jenis, baju='a' if jenis == 'gadis' else 'h') + (tas_punggung(x - 22, 140, .7) if not buku_ else buku(x + 22, 160, 22, 28))


A['A12-L4a'] = lantai() + murid(150, 'gadis')
A['A12-L4b'] = (lantai() + kotak(170, 60, 110, 140, 'p') + kotak(170, 46, 110, 16, 'h') + teks(225, 58, '大學', 13, warna='#fff')
                + orang(100, tinggi=148, jenis='wanita', baju='a', tangan={'ka': [(16, 26), (30, 30)]}) + buku(132, 136, 26, 34))
A['A12-L4c'] = lantai() + guru(80)
A['A12-L5a'] = jam12(10, 0)
A['A12-L5b'] = jam12(4, 30)
A['A12-L5c'] = jam12(4, 0)
A['A12-L6a'] = jam12(2, 0)
A['A12-L6b'] = jam12(9, 0, 'pagi')
A['A12-L6c'] = jam12(5, 0)


def kelas(guru_di_dalam=True, murid_di_dalam=True):
    o = lantai() + kotak(20, 40, 170, 160, 'p') + teks(105, 60, '教室', 18) + papan_tulis(105, 72, 110, 50)
    if guru_di_dalam:
        o += orang(60, tinggi=130, jenis='wanita', baju='a')
    else:
        o += orang(230, tinggi=130, jenis='wanita', baju='a')
    if murid_di_dalam:
        o += orang(110, tinggi=80, jenis='laki', baju='h') + orang(155, tinggi=80, jenis='gadis', baju='a')
    else:
        o += orang(220, tinggi=80, jenis='laki', baju='h') + orang(262, tinggi=80, jenis='gadis', baju='a')
    return o


A['A12-L8a'] = kelas(True, False)
A['A12-L8b'] = kelas(True, True)
A['A12-L8c'] = kelas(False, True)
A['A12-L9'] = (lantai_kamar() + jendela(80, 40, 66, 48) + bulan_bintang(80, 64, .45) + meja(185, 140, 130)
               + orang(185, tinggi=110, jenis='laki', baju='h', duduk=160, tangan={'ka': [(10, 20), (24, 24)]}) + kertas(205, 132, 34, 14) + pulpen(214, 128, 26, -30))
A['A12-L10'] = ruang_kelas(True, 2)
A['A12-T3a'] = lantai() + guru(80, 'pria')
A['A12-T3b'] = lantai() + meja(200, 140, 120) + komputer(200, 140, 90) + orang(90, tinggi=160, jenis='pria', baju='h')
A['A12-T3c'] = lantai() + murid(150, 'laki', True)
A['A12-T4a'] = jam12(12, 0)
A['A12-T4b'] = jam12(9, 0)
A['A12-T4c'] = jam12(2, 0)
A['A12-T6a'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(150, tinggi=100, jenis='laki', baju='h')
A['A12-T6b'] = lantai() + rumah(210) + orang(80, tinggi=150, jenis='wanita', baju='a')
A['A12-T6c'] = ruang_kelas(False, 2)
A['A12-T7'] = ruang_kelas(True, 2)
A['A12-T8'] = lantai() + meja(150, 140, 160) + buku_tumpuk(150, 138, 4, 90, 18)

# A13 — alat tulis
A['A13-1'] = pulpen(150, 90, 150, -8) + pulpen(150, 140, 150, -8)
A['A13-2'] = lantai() + meja(150, 130, 200) + komputer(170, 130, 96) + orang(75, tinggi=150, jenis='wanita', baju='a', duduk=140, tangan={'ka': [(26, 4), (56, -2)]})
A['A13-3'] = lantai() + meja(150, 150, 240) + kertas(80, 118, 44, 56, -8) + kertas(150, 116, 44, 56, 4) + kertas(220, 118, 44, 56, -3)
A['A13-4'] = lantai(186, 60, 240) + buku_tumpuk(150, 186, 3, 130, 30)
A['A13-5'] = lantai() + papan_tulis(210, 28, 140, 70) + meja_kelas(95) + orang(95, tinggi=125, jenis='laki', baju='a', duduk=150, tangan=ANGKAT, wajah='senyum')

# --- A13 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def deret(benda, n, y=150, jarak=None):
    """n benda berjajar di atas meja: benda ∈ buku/pena/kertas."""
    jarak = jarak or min(52, 230 / max(n, 1))
    x0 = 150 - jarak * (n - 1) / 2
    o = ''
    for i in range(n):
        x = x0 + i * jarak
        o += {'buku': lambda: buku(x, y, 34, 46), 'pena': lambda: pulpen(x, y - 30, 58, 90),
              'kertas': lambda: kertas(x, y - 30, 38, 52, (i - n / 2) * 4)}[benda]()
    return o


atas_meja = lambda *isi: lantai() + meja(150, 150, 250) + ''.join(isi)


def mengetik(x, jenis):
    return meja(x + 70, 140, 110) + komputer(x + 70, 140, 80) + orang(x, tinggi=150 if jenis == 'pria' else 145, jenis=jenis, baju='h' if jenis == 'pria' else 'a',
                                                                       tangan={'ka': [(20, 24), (46, 28)]})


def menulis(x, jenis):
    return meja(x + 70, 140, 110) + kertas(x + 80, 128, 50, 20, 0) + pulpen(x + 62, 120, 30, 60) + orang(x, tinggi=145, jenis=jenis, baju='a' if jenis == 'wanita' else 'h', tangan={'ka': [(20, 24), (48, 30)]})


def membaca(x, jenis):
    return orang(x, tinggi=150, jenis=jenis, baju='h', tangan={'ki': [(18, 24), (36, 4)], 'ka': [(18, 24), (36, 4)]}) + kotak(x - 26, 70, 52, 34, 'p', 2) + garis((x, 70), (x, 104))


A['A13-L4a'] = atas_meja(deret('buku', 4))
A['A13-L4b'] = atas_meja(deret('buku', 5))
A['A13-L4c'] = atas_meja(deret('pena', 5))
A['A13-L5a'] = lantai() + menulis(80, 'wanita')
A['A13-L5b'] = lantai() + mengetik(80, 'pria')
A['A13-L5c'] = lantai() + mengetik(80, 'wanita')
A['A13-L6a'] = lantai() + papan_tulis(210, 40, 120, 60) + orang(110, tinggi=155, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (40, -24)]}) + pulpen(145, 60, 34, 20)
A['A13-L6b'] = lantai() + orang(150, tinggi=150, jenis='pria', baju='h') + tas_punggung(122, 72, .8)
A['A13-L6c'] = lantai() + orang(150, tinggi=145, jenis='wanita', baju='p') + tas_punggung(122, 76, .8)
A['A13-L8a'] = atas_meja(deret('buku', 3, jarak=44).replace('', '') , pulpen(225, 104, 56, 80))
A['A13-L8a'] = lantai() + meja(150, 150, 250) + buku(70, 150, 34, 46) + buku(110, 150, 34, 46) + buku(150, 150, 34, 46) + pulpen(214, 120, 58, 90)
A['A13-L8b'] = lantai() + meja(150, 150, 250) + buku(80, 150, 34, 46) + pulpen(144, 120, 58, 90) + pulpen(184, 120, 58, 90) + pulpen(224, 120, 58, 90)
A['A13-L8c'] = lantai() + meja(150, 150, 250) + buku(60, 150, 34, 46) + buku(100, 150, 34, 46) + buku(140, 150, 34, 46) + kertas(190, 122, 34, 46, -4) + kertas(220, 122, 34, 46, 2) + kertas(250, 122, 34, 46, 6)
A['A13-L9'] = lantai() + membaca(130, 'gadis') + teks(130, 32, '？', 30) + teks(170, 48, '？', 22)
A['A13-L10'] = atas_meja(deret('kertas', 3, jarak=70))
A['A13-T3a'] = lantai() + membaca(150, 'wanita')
A['A13-T3b'] = lantai() + mengetik(80, 'wanita')
A['A13-T3c'] = lantai() + menulis(80, 'wanita')
A['A13-T4a'] = pulpen(150, 110, 170, 40)
A['A13-T4b'] = buku(150, 170, 110, 140)
A['A13-T4c'] = kertas(150, 110, 120, 160, -4)
A['A13-T6a'] = atas_meja(deret('kertas', 2, jarak=80))
A['A13-T6b'] = atas_meja(deret('pena', 2, jarak=80))
A['A13-T6c'] = atas_meja(deret('buku', 2, jarak=80))
A['A13-T7'] = lantai() + meja(150, 150, 180) + komputer(150, 150, 130)
A['A13-T8'] = pulpen(150, 110, 170, 40)

# A14 — ujian
A['A14-1'] = (lantai() + meja(150, 140, 200) + kertas(185, 118, 50, 40, 0) + orang(110, tinggi=150, jenis='pria', baju='a', duduk=146, wajah='sedih', tangan=TA)
              + keringat(140, 60) + keringat(78, 70, .8))
A['A14-2'] = kertas(150, 110, 150, 170, 0) + teks(150, 140, '字', 88) + silang(150, 110, 58, 10)
A['A14-4'] = (lantai() + orang(110, tinggi=150, jenis='gadis', baju='a', wajah='puas', tangan={'ka': [(24, -6), (44, -30)]}) + kertas(205, 80, 70, 90, 6)
              + centang(195, 62) + centang(200, 92) + centang(205, 118, .8))
A['A14-5'] = lantai() + papan_tulis(95, 30, 150, 70) + orang(70, tinggi=160, jenis='wanita', baju='a') + orang(210, tinggi=125, jenis='laki', baju='h', tangan=ANGKAT)

# --- A14 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def ujian(x, y, w=80, h=100, tanda=None):
    """Kertas ujian; tanda = daftar 'v'/'x' per baris."""
    o = kotak(x - w / 2, y, w, h, 'p', 3) + teks(x, y + 18, '考試', 14)
    for i, t in enumerate(tanda or []):
        yy = y + 34 + i * 20
        o += garis((x - w / 2 + 8, yy), (x + w / 2 - 26, yy), k='t')
        o += centang(x + w / 2 - 14, yy - 2, .45, 3) if t == 'v' else silang(x + w / 2 - 14, yy - 2, 6, 3)
    return o


def takut(x, jenis, tinggi=150):
    return orang(x, tinggi=tinggi, jenis=jenis, baju='a' if jenis in ('wanita', 'gadis') else 'h', wajah='kaget', tangan={'ki': [(14, 20), (6, 40)], 'ka': [(14, 20), (6, 40)]}) + keringat(x + 22, 200 - tinggi + 10)


def huruf(tanda):
    o = kotak(70, 40, 120, 120, 'p', 4) + teks(130, 132, '書', 90)
    return o + {'v': centang(230, 100, 1.4, 8), 'x': silang(230, 100, 34, 8), '?': teks(230, 128, '？', 80)}[tanda]


A['A14-3'] = lantai() + takut(90, 'laki', 110) + meja(205, 150, 110) + ujian(205, 60, 70, 90)
A['A14-L4a'] = lantai() + takut(90, 'wanita') + ujian(215, 50)
A['A14-L4b'] = (lantai() + takut(90, 'wanita') + elips(225, 170, 36, 18, 'a') + bulat(258, 150, 14, 'a') + garis((236, 186), (236, 200), lebar=6)
                + garis((210, 186), (210, 200), lebar=6) + jalur('M262 140 l8 -10 l2 12', 'a'))
A['A14-L4c'] = lantai() + takut(90, 'pria') + ujian(215, 50)
A['A14-L5a'] = lantai() + meja(205, 140, 110) + kertas(215, 128, 50, 20, 0) + pulpen(200, 120, 30, 60) + orang(120, tinggi=145, jenis='wanita', baju='a', tangan={'ka': [(20, 24), (48, 30)]})
A['A14-L5b'] = lantai() + meja(205, 140, 110) + komputer(205, 140, 80) + orang(120, tinggi=145, jenis='wanita', baju='a', tangan={'ka': [(20, 24), (46, 28)]})
A['A14-L5c'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(18, 24), (36, 4)], 'ka': [(18, 24), (36, 4)]}) + kotak(124, 70, 52, 34, 'p', 2) + garis((150, 70), (150, 104))
A['A14-L6a'] = lantai() + meja(205, 140, 110) + kertas(215, 128, 50, 20, 0) + pulpen(200, 120, 30, 60) + orang(120, tinggi=145, jenis='wanita', baju='a', tangan={'ka': [(20, 24), (48, 30)]})
A['A14-L6b'] = lantai() + orang(100, tinggi=150, jenis='wanita', baju='a', wajah='nyanyi') + gelembung(205, 60, 110, 56, teks(205, 72, '你好！', 28))
A['A14-L6c'] = (lantai() + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='puas') + jalur('M135 58 Q150 30 165 58', 'g', 4)
                + kotak(128, 52, 8, 14, 'h', 3) + kotak(164, 52, 8, 14, 'h', 3) + not_musik(200, 50) + not_musik(230, 80))
A['A14-L8a'] = ujian(150, 30, 150, 160, 'vvvvvv')
A['A14-L8b'] = ujian(150, 30, 150, 160, 'xxxxxx')
A['A14-L8c'] = ujian(150, 30, 150, 160, 'vxvxxv')
A['A14-L9'] = (lantai_kamar() + jendela(80, 40, 66, 48) + bulan_bintang(80, 64, .45) + kotak(200, 24, 76, 50, 'p', 4) + teks(238, 56, '明天考試', 16)
               + meja(130, 150, 120) + buku(105, 150, 30, 36)
               + orang(150, tinggi=110, jenis='laki', baju='h', wajah='kaget', duduk=165) + keringat(170, 100))
A['A14-L10'] = lantai() + takut(90, 'laki', 110) + meja(205, 150, 110) + ujian(205, 60, 70, 90)
A['A14-T3a'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='puas')
A['A14-T3b'] = lantai() + takut(150, 'wanita', 160)
A['A14-T3c'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='senyum')
A['A14-T4a'] = huruf('v')
A['A14-T4b'] = huruf('x')
A['A14-T4c'] = huruf('?')
A['A14-T6a'] = (lantai_kamar() + ranjang(150, 200, 190) + kotak(110, 134, 104, 16, 'a', 7) + jalur('M86 128 Q84 146 76 150 L120 150 Q112 146 110 128 Z', 'h')
                + bulat(98, 132, 12) + muka(98, 132, 12, 'tidur') + teks(122, 110, 'Z', 20, angka=True))
A['A14-T6b'] = lantai() + takut(90, 'wanita') + ujian(215, 50)
A['A14-T6c'] = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(20, -10), (30, -40)]}) + ujian(215, 50, tanda='vvv')
A['A14-T7'] = huruf('v')
A['A14-T8'] = lantai() + orang(90, tinggi=150, jenis='laki', baju='h', wajah='lelah', tangan={'ka': [(16, 10), (6, -18)]}) + ujian(215, 50) + teks(90, 30, '？', 30)

# A15 — minuman
A['A15-1'] = lantai() + gelas(125, 200, 'susu', 1.6) + kotak_susu(210, 200, 1.1)
A['A15-2'] = lantai() + gelas(150, 200, 'air', 2, es=True)
A['A15-3'] = lantai() + orang(130, tinggi=165, jenis='pria', baju='a', wajah='puas', tangan={'ka': [(14, 26), (-4, -6)]}) + cangkir(160, 66, .55)
A['A15-4'] = lantai() + teko(110, 200, 1.2) + cangkir(220, 196, 1.0)
A['A15-5'] = lantai() + gelas(150, 196, 'air', 1.8, es=True) + larangan(150, 130, 70)

# --- A15 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def gelas15(x, isi, s=1.6, es=0, bawah=200):
    """isi: kopi (hitam) / teh (abu) / susu (putih) / air (garis). es = jumlah es batu."""
    top = bawah - 60 * s
    o = bentuk((x - 22 * s, top), (x + 22 * s, top), (x + 17 * s, bawah), (x - 17 * s, bawah), k='p')
    k = {'kopi': 'h', 'teh': 'a', 'susu': 'p', 'air': None}[isi]
    if k:
        o += bentuk((x - 20.5 * s, top + 10 * s), (x + 20.5 * s, top + 10 * s), (x + 17 * s, bawah), (x - 17 * s, bawah), k=k)
    else:
        o += garis((x - 20 * s, top + 12 * s), (x + 20 * s, top + 12 * s), k='t')
    pos = [(-12, 14), (2, 20), (-6, 32), (6, 40), (-12, 44)][:es]
    for dx, dy in pos:
        o += kotak(x + dx * s, top + dy * s, 11 * s, 11 * s, 'p', 2)
    if isi == 'teh':
        o += garis((x + 10 * s, top - 2), (x + 18 * s, top - 22 * s), k='t') + kotak(x + 14 * s, top - 30 * s, 12 * s, 9 * s, 'p', 1)
    return o


def panas(x, isi, s=1.4, bawah=196):
    o = cangkir(x, bawah, s, uap=True)
    k = {'kopi': 'h', 'teh': 'a'}[isi]
    return o + elips(x, bawah - 40 * s + 4, 21 * s, 4 * s, k)


biji = lambda x, y: elips(x, y, 9, 6, 'h') + garis((x - 6, y), (x + 6, y), k='w')
A['A15-L4a'] = lantai() + panas(150, 'kopi') + biji(230, 192) + biji(245, 186)
A['A15-L4b'] = lantai() + gelas15(150, 'teh', es=4)
A['A15-L4c'] = lantai() + gelas15(150, 'kopi', es=4) + biji(230, 192) + biji(245, 186)
A['A15-L5a'] = lantai() + gelas15(110, 'teh', 1.4) + gelas15(190, 'teh', 1.4)
A['A15-L5b'] = lantai() + gelas15(110, 'kopi', 1.4) + gelas15(190, 'kopi', 1.4) + biji(250, 192)
A['A15-L5c'] = lantai() + gelas15(150, 'teh', 1.4)
A['A15-L6a'] = lantai() + panas(150, 'kopi') + biji(230, 192) + biji(245, 186)
A['A15-L6b'] = lantai() + gelas15(125, 'susu') + kotak_susu(210, 200, 1.1)
A['A15-L6c'] = lantai() + teko(110, 200, 1.2) + panas(220, 'teh', 1.0)
A['A15-L8a'] = lantai() + gelas15(150, 'teh', 1.8, es=2)
A['A15-L8b'] = lantai() + gelas15(150, 'teh', 1.8, es=5)
A['A15-L8c'] = lantai() + gelas15(150, 'kopi', 1.8, es=2) + biji(235, 192)
A['A15-L9'] = lantai() + meja(150, 150, 220) + panas(105, 'kopi', .9, bawah=144) + gelas15(195, 'air', 1.1, bawah=150)
A['A15-L10'] = lantai() + panas(95, 'kopi', 1.1) + teks(150, 150, '？', 40) + panas(205, 'teh', 1.1)
A['A15-T3a'] = lantai() + teko(110, 200, 1.2) + panas(220, 'teh', 1.0)
A['A15-T3b'] = lantai() + panas(150, 'kopi') + biji(230, 192) + biji(245, 186)
A['A15-T3c'] = lantai() + gelas15(125, 'susu') + kotak_susu(210, 200, 1.1)
A['A15-T4a'] = lantai() + gelas15(150, 'kopi', es=4) + biji(230, 192)
A['A15-T4b'] = lantai() + panas(150, 'kopi') + biji(230, 192)
A['A15-T4c'] = lantai() + gelas15(150, 'teh', es=4)
A['A15-T6a'] = lantai() + panas(130, 'teh') + orang(225, tinggi=150, jenis='pria', baju='h', wajah='puas')
A['A15-T6b'] = lantai() + panas(130, 'kopi') + orang(225, tinggi=150, jenis='pria', baju='h', wajah='sakit')
A['A15-T6c'] = lantai() + panas(130, 'kopi') + orang(225, tinggi=150, jenis='pria', baju='h', wajah='puas')
A['A15-T7'] = lantai() + gelas15(110, 'teh', 1.4) + gelas15(190, 'teh', 1.4)
A['A15-T8'] = lantai() + gelas15(150, 'air', 2.2)

# A16 — makanan
A['A16-1'] = lantai() + jendela(230, 30, 80, 64) + matahari(230, 62, 10) + meja(130, 150, 200) + piring(130, 144, 70, telur_ceplok(130, 142, .9))
A['A16-2'] = lantai() + jendela(230, 30, 80, 64) + bulan_bintang(222, 60, .5) + meja(130, 150, 200) + piring(130, 144, 76, ikan(128, 136, .9))
A['A16-3'] = (lantai() + orang(150, tinggi=160, jenis='pria', baju='a', wajah='puas', badan=1.35) + elips(150, 118, 30, 24, 'a')
              + garis((122, 90), (112, 112), (140, 120), lebar=4.6) + garis((178, 90), (188, 112), (160, 120), lebar=4.6)
              + meja(150, 150, 260) + piring(55, 146, 36) + piring(245, 146, 36) + elips(150, 144, 22, 6, 'p'))
A['A16-4'] = lantai() + jam_dinding(235, 54, 34, 12, 0) + meja(125, 150, 200) + piring(125, 144, 76, ikan(123, 136, .9))
A['A16-5'] = lantai() + meja(150, 150, 240) + piring(150, 144, 60) + orang(150, tinggi=150, jenis='laki', baju='a', wajah='lapar', tangan={'ki': [(0, 24), (-10, 44)], 'ka': [(0, 24), (-10, 44)]}) + piring(150, 144, 60)

# --- A16 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def lauk(jenis, x=150, y=150, s=1.0):
    """Piring berisi lauk; hewan kecil di pojok sebagai penanda jenis daging."""
    o = piring(x, y + 10 * s, 80 * s)
    if jenis == 'ikan':
        o += ikan(x, y, 1.3 * s)
    elif jenis in ('sapi', 'babi', 'ayam'):
        o += daging(x, y, 1.2 * s) + {'sapi': hewan_sapi, 'babi': hewan_babi, 'ayam': hewan_ayam}[jenis](x + 95 * s, y - 70 * s, .55 * s)
    return o


def nasi(x, y, s=1.0):
    return elips(x, y, 34 * s, 18 * s, 'p') + ''.join(bulat(x + dx * s, y - 4 * s + dy * s, 3, 'g') for dx, dy in ((-14, 0), (0, -6), (12, 2), (-4, 8), (8, -10)))


def sayur(x, y, s=1.0):
    return ''.join(elips(x + dx * s, y + dy * s, 12 * s, 7 * s, 'a') for dx, dy in ((-10, 0), (8, -6), (4, 6)))


def sup(x, y, s=1.0):
    return mangkuk_mi(x, y, s, sumpit=False)


A['A16-L4a'] = lauk('ikan', y=130)
A['A16-L4b'] = lauk('ayam', 120, 140)
A['A16-L4c'] = lauk('babi', 120, 140)
A['A16-L5a'] = piring(150, 140, 90) + telur_ceplok(115, 130, 1.0) + telur_ceplok(185, 130, 1.0)
A['A16-L5b'] = piring(150, 140, 90) + telur_ceplok(150, 130, 1.0)
A['A16-L5c'] = piring(150, 140, 90) + ikan(110, 132, .8) + ikan(190, 132, .8)
A['A16-L6a'] = lauk('sapi', 120, 140)
A['A16-L6b'] = lauk('babi', 120, 140)
A['A16-L6c'] = lauk('ayam', 120, 140)
A['A16-L8a'] = piring(150, 140, 110) + nasi(115, 130) + sayur(190, 130)
A['A16-L8b'] = piring(150, 140, 110) + nasi(115, 130) + daging(190, 128, .9)
A['A16-L8c'] = piring(150, 140, 120) + nasi(100, 130) + sayur(155, 130, .9) + daging(205, 128, .8)
A['A16-L9'] = (lantai() + meja(200, 150, 140) + piring(175, 146, 30) + piring(230, 146, 30)
               + orang(85, tinggi=160, jenis='pria', baju='h', badan=1.3, wajah='puas', tangan={'ki': [(10, 30), (24, 44)], 'ka': [(10, 30), (24, 44)]}))
A['A16-L10'] = sup(150, 110, .8)
A['A16-T3a'] = piring(150, 150, 80) + telur_ceplok(130, 140, 1.0) + gelas(215, 190, 'susu', 1.0)
A['A16-T3b'] = piring(150, 150, 80) + telur_ceplok(130, 140, 1.0) + cangkir(220, 190, .9) + elips(220, 158, 19, 4, 'h')
A['A16-T3c'] = piring(150, 150, 80) + roti(130, 140, 1.0) + gelas(215, 190, 'susu', 1.0)
A['A16-T4a'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='lapar', tangan={'ki': [(10, 30), (24, 44)], 'ka': [(10, 30), (24, 44)]})
A['A16-T4b'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='lelah') + teks(185, 50, 'Z', 22, angka=True)
A['A16-T4c'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='puas', badan=1.2, tangan={'ki': [(10, 30), (24, 44)], 'ka': [(10, 30), (24, 44)]})
A['A16-T6a'] = lantai() + mangkuk_mi(130, 120, .7) + orang(255, tinggi=120, jenis='pria', baju='h')
A['A16-T6b'] = lantai() + sup(130, 120, .7) + orang(255, tinggi=120, jenis='pria', baju='h')
A['A16-T6c'] = lantai() + cangkir(150, 196, 1.3) + elips(150, 148, 28, 5, 'a') + orang(255, tinggi=120, jenis='pria', baju='h')
A['A16-T7'] = buah_apel(100, 120, 1.4) + buah_apel(170, 110, 1.2) + jalur('M200 150 Q240 90 268 120 Q240 110 214 160 Z', 'a')
A['A16-T8'] = piring(150, 150, 90) + daging(150, 138, 1.4)

# A17 — restoran
A['A17-1'] = mangkuk_mi(150, 100, 1.1)
A['A17-2'] = (lantai() + meja(150, 150, 240) + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='senyum', tangan={'ka': [(20, 20), (4, -6)]})
              + garis((158, 72), (190, 128), lebar=3) + garis((164, 70), (196, 126), lebar=3) + mangkuk_mi(160, 128, .45, sumpit=False))
A['A17-3'] = piring(150, 160, 110, bakpao(110, 160, 1.3) + bakpao(190, 160, 1.3))
A['A17-4'] = (lantai() + kotak(170, 40, 114, 160, 'p') + kotak(200, 90, 56, 110, 'h') + kotak(176, 48, 102, 32, 'h') + mangkuk_mi(227, 62, .18, sumpit=False, uap=False)
              + orang(50, tinggi=140, jenis='wanita', baju='a') + orang(100, tinggi=155, jenis='pria', baju='h') + orang(148, tinggi=110, jenis='laki', baju='p'))
A['A17-5'] = piring(150, 160, 110, roti(150, 156, 1.2))

# --- A17 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
mi = lambda x, y=150, s=.7: mangkuk_mi(x, y, s)
bp = lambda x, y=170, s=1.0: bakpao(x, y, s)
meja17 = lambda *isi: lantai() + meja(150, 160, 250) + ''.join(isi)


def makan(x, jenis, apa, tinggi=None):
    tinggi = tinggi or (145 if jenis in ('wanita', 'pria') else 100)
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    o = orang(x, tinggi=tinggi, jenis=jenis, baju=baju, wajah='puas', tangan={'ka': [(16, 18), (30, 6)]})
    tx = x + 40
    ty = 200 - tinggi * .55
    return o + {'mi': mangkuk_mi(tx + 10, ty + 10, .45), 'sup': mangkuk_mi(tx + 10, ty + 10, .45, sumpit=False),
                'bakpao': bakpao(tx + 6, ty + 14, .7)}[apa]


A['A17-L4a'] = meja17(mi(150, 124, .5))
A['A17-L4b'] = meja17(mi(85, 124, .5), mi(215, 124, .5))
A['A17-L4c'] = meja17(bp(110, 152), bp(190, 152))
A['A17-L5a'] = lantai() + makan(120, 'wanita', 'mi')
A['A17-L5b'] = lantai() + makan(120, 'wanita', 'bakpao')
A['A17-L5c'] = lantai() + makan(120, 'wanita', 'sup')
A['A17-L6a'] = bp(150, 150, 1.8)
A['A17-L6b'] = mi(150, 100, 1.0)
A['A17-L6c'] = roti(150, 140, 2.0)
A['A17-L8a'] = lantai() + makan(90, 'gadis', 'bakpao', 125) + makan(200, 'laki', 'bakpao', 95)
A['A17-L8b'] = lantai() + makan(120, 'gadis', 'bakpao', 125)
A['A17-L8c'] = lantai() + makan(90, 'gadis', 'mi', 125) + makan(200, 'laki', 'mi', 95)
A['A17-L9'] = (lantai() + kotak(30, 60, 240, 14, 'h') + garis((40, 74), (40, 200)) + garis((260, 74), (260, 200)) + meja(150, 140, 230)
               + bp(70, 140, .8) + bp(105, 140, .8) + mi(160, 104, .45) + mi(215, 104, .45) + bp(245, 140, .7))
A['A17-L10'] = lantai() + makan(110, 'pria', 'mi') + garis((180, 60), (215, 60), k='t') + garis((185, 74), (225, 74), k='t') + garis((180, 88), (212, 88), k='t')
A['A17-T3a'] = meja17(mi(70, 124, .48), mi(160, 124, .48), bp(240, 152, .8))
A['A17-T3b'] = meja17(bp(110, 152), bp(190, 152))
A['A17-T3c'] = meja17(mi(80, 124, .48), bp(175, 152, .8), bp(235, 152, .8))
A['A17-T4a'] = lantai() + bioskop(200) + orang(70, tinggi=140, jenis='wanita', baju='a') + orang(120, tinggi=150, jenis='pria', baju='h')
A['A17-T4b'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(125, tinggi=145, jenis='wanita', baju='a') + orang(178, tinggi=150, jenis='pria', baju='h')
A['A17-T4c'] = lantai() + rumah(200) + orang(70, tinggi=140, jenis='wanita', baju='a') + orang(115, tinggi=150, jenis='pria', baju='h')
restoran = lambda: kotak(150, 50, 130, 150, 'p') + kotak(150, 36, 130, 18, 'h') + mi(215, 120, .5)
A['A17-T6a'] = lantai() + pohon(215) + pohon(265, s=.8) + orang(60, tinggi=150, jenis='wanita', baju='a', rambut='uban') + orang(115, tinggi=100, jenis='gadis', baju='h')
A['A17-T6b'] = lantai() + restoran() + orang(60, tinggi=150, jenis='wanita', baju='a', rambut='uban') + orang(115, tinggi=100, jenis='gadis', baju='h')
A['A17-T6c'] = lantai() + restoran() + orang(60, tinggi=165, jenis='pria', baju='a') + orang(115, tinggi=100, jenis='gadis', baju='h')
A['A17-T7'] = garis((70, 60), (240, 170), lebar=8) + garis((90, 50), (250, 160), lebar=8)
A['A17-T8'] = mi(150, 100, 1.0)

# A18 — belanja
A['A18-1'] = struk(150, 30, '350', 140, 170)
A['A18-2'] = label_harga(150, 78, '120', 180, 76)
A['A18-3'] = lantai() + toko(95) + orang(222, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(8, 30), (4, 50)], 'ka': [(8, 30), (4, 50)]}) + tas_belanja(196, 190, .8) + tas_belanja(250, 190, .8)
A['A18-4'] = label_harga(150, 78, '300', 180, 76)
A['A18-5'] = (lantai() + orang(95, tinggi=160, jenis='pria', baju='a', wajah='sedih', tangan={'ka': [(20, 16), (40, 0)]}) + keringat(118, 44) + dompet(200, 92, .9)
              + bulat(230, 142, 7, 'p'))

# --- A18 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def uang(x, y, n, w=150, h=72):
    """Uang kertas generik bertuliskan nominal (bukan tiruan uang asli)."""
    return kotak(x - w / 2, y, w, h, 'p', 6) + kotak(x - w / 2 + 8, y + 8, w - 16, h - 16, 't', 4) + teks(x, y + h / 2 + 10, f'${n}', round(min(30, (w - 24) / (len(str(n)) + 1) * 1.7)), angka=True)


hg18 = lambda n, benda=None: label_harga(150, 120, n, 190, 72) + ({'buku': buku(150, 100, 60, 80), 'pena': pulpen(150, 70, 120, -20)}.get(benda, ''))
A['A18-L4a'] = hg18('250', 'buku')
A['A18-L4b'] = hg18('205', 'buku')
A['A18-L4c'] = hg18('520', 'buku')
A['A18-L5a'] = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 20), (40, 10)]}) + buku(170, 150, 30, 40) + buku(205, 150, 30, 40)
A['A18-L5b'] = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 20), (40, 10)]}) + pulpen(185, 110, 70, -15) + pulpen(190, 125, 70, -15)
A['A18-L5c'] = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 20), (40, 10)]}) + pulpen(185, 115, 70, -15)
A['A18-L6a'] = uang(150, 74, 50)
A['A18-L6b'] = uang(150, 74, 80)
A['A18-L6c'] = uang(150, 74, 30)
A['A18-L8a'] = hg18('300', 'buku')
A['A18-L8b'] = hg18('30', 'buku')
A['A18-L8c'] = hg18('300', 'pena')
A['A18-L9'] = dompet(80, 120, .9) + uang(80, 160, 100, 100, 46) + label_harga(220, 90, '500', 130, 60) + kaos(220, 40, .5)
A['A18-L10'] = (lantai() + meja(110, 130, 140) + kotak(70, 92, 70, 38, 'h', 4) + kotak(80, 98, 50, 14, 'p', 2)
                + orang(225, tinggi=150, jenis='wanita', baju='a') + gelembung(185, 40, 60, 40, teks(185, 52, '？', 28), (1, 1)))
A['A18-T3a'] = label_harga(150, 80, '1,200', 220, 76)
A['A18-T3b'] = label_harga(150, 80, '2,100', 220, 76)
A['A18-T3c'] = label_harga(150, 80, '1,002', 220, 76)
A['A18-T4a'] = uang(150, 74, 200)
A['A18-T4b'] = uang(150, 74, 50)
A['A18-T4c'] = uang(150, 74, 100)
A['A18-T6a'] = dompet(150, 110, 1.2) + uang(110, 40, 1000, 110, 46) + uang(190, 30, 1000, 110, 46)
A['A18-T6b'] = dompet(150, 130, 1.2) + uang(150, 30, 100, 130, 56)
A['A18-T6c'] = dompet(150, 130, 1.2) + bulat(150, 60, 24, 'p') + teks(150, 69, '10', 20, angka=True)
A['A18-T7'] = A['A18-3']
A['A18-T8'] = label_harga(150, 80, '10', 190, 76)

# A19 — pakaian (soal warna diberi warna)
A['A19-1'] = lantai() + sepatu(110, 196, 1.5) + sepatu(210, 196, 1.5)
A['A19-2'] = kaos(150, 110, 1.9, 'm')
A['A19-3'] = (lantai() + jalur('M72 30 L72 160 Q72 196 96 196 L130 196 L110 150 L110 30', 'p') + sepatu(160, 198, 1.9)
              + jalur('M54 150 l-14 -6 M52 170 l-16 0 M56 188 l-14 6', 'g'))   # tumit menyembul keluar dari sepatu yang kecil
A['A19-4'] = lantai() + orang(150, tinggi=175, jenis='wanita', baju='m')
A['A19-5'] = (lantai() + sepatu(160, 198, 2.5) + jalur('M84 30 L84 150 Q84 178 104 180 L158 182 Q170 182 170 172 L150 150 L112 138 L112 30', 'p')
              + panah(190, 165, 232, 165, 3) + panah(232, 165, 190, 165, 3))   # celah di ujung sepatu yang kebesaran

# --- A19 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---  (warna: m = merah, h = hitam, p = putih)
baju = lambda k, x=150, y=120, s=1.9: kaos(x, y, s, k)
spt = lambda k, x=150, y=150, s=1.6: sepatu(x - 60 * s / 1.6, y, s, k) + sepatu(x + 50 * s / 1.6, y, s, k)


def pakai(x, jenis, kb, ks, tinggi=None):
    """Orang memakai baju warna kb dan sepatu warna ks."""
    tinggi = tinggi or (100 if jenis in ('gadis', 'laki') else 150)
    o = orang(x, tinggi=tinggi, jenis=jenis, baju=kb)
    return o + sepatu(x - 9, 199, .5 * tinggi / 100, ks) + sepatu(x + 9, 199, .5 * tinggi / 100, ks)


A['A19-L4a'] = spt('h')
A['A19-L4b'] = baju('p')
A['A19-L4c'] = baju('h')
A['A19-L5a'] = baju('p', s=1.1, y=120)
A['A19-L5b'] = baju('p', s=2.3, y=128)
A['A19-L5c'] = spt('p', s=1.0, y=150)
A['A19-L6a'] = baju('m')
A['A19-L6b'] = baju('h')
A['A19-L6c'] = baju('p')
A['A19-L8a'] = lantai() + pakai(150, 'gadis', 'm', 'p', 130)
A['A19-L8b'] = lantai() + pakai(150, 'gadis', 'p', 'm', 130)
A['A19-L8c'] = lantai() + pakai(150, 'gadis', 'm', 'h', 130)
A['A19-L9'] = (lantai() + orang(130, tinggi=130, jenis='gadis', baju='m', wajah='puas') + garis((146, 112), (170, 128), k='t') + label_harga(190, 120, '', 40, 24)
               + bintang(70, 60, 10) + bintang(220, 50, 8))
A['A19-L10'] = (lantai() + garis((140, 46), (290, 46), lebar=5) + kaos(170, 100, .85, 'm') + kaos(218, 100, .85, 'p') + kaos(264, 100, .85, 'h')
                + orang(80, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, -4), (60, -26)]}))
A['A19-T3a'] = baju('m')
A['A19-T3b'] = baju('h')
A['A19-T3c'] = baju('p')
A['A19-T4a'] = spt('a', s=1.2) + garis((70, 120), (90, 112), k='t') + garis((205, 116), (225, 124), k='t')
A['A19-T4b'] = spt('h', s=1.6) + bintang(60, 70, 9) + bintang(250, 60, 9)
A['A19-T4c'] = spt('h', s=2.0, y=160)
A['A19-T6a'] = baju('p', x=85, s=1.25, y=115) + baju('m', x=215, s=1.25, y=115)
A['A19-T6b'] = baju('h', x=85, s=1.25, y=115) + baju('h', x=215, s=1.25, y=115)
A['A19-T6c'] = baju('p', x=85, s=1.25, y=115) + baju('h', x=215, s=1.25, y=115)
A['A19-T7'] = spt('a', s=1.6) + garis((80, 128), (100, 120), k='t') + garis((190, 124), (214, 132), k='t') + bulat(120, 140, 5, 'g')
A['A19-T8'] = baju('p')

# A20 — kendaraan
A['A20-1'] = lantai() + kereta(160, 196, 250) + orang(40, tinggi=130, jenis='wanita', baju='a') + tas_punggung(58, 110, .8)
A['A20-2'] = awan(60, 50, .6) + awan(240, 160, .5) + pesawat(150, 110, 1.1)
A['A20-3'] = lantai() + kotak(170, 60, 114, 140, 'p') + bentuk((160, 60), (227, 20), (294, 60), k='h') + lonceng(227, 50, .22) + pintu(227, 200, 70, 40) + jalan_kaki(90, 'laki', 110, 'h') + tas_punggung(70, 112, .7)
A['A20-4'] = lantai() + mobil(150, 200, 230, taksi=True, k='a')
A['A20-5'] = lantai() + mobil(80, 200, 140) + mobil(225, 200, 140, k='a')

# --- A20 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def sopir(xm, jenis, w=190, taksi=False, penumpang=None):
    """Mobil dengan pengemudi: badan tertutup mobil, kepala terlihat di atas atap (seperti duduk di dalam)."""
    o = lantai() + orang(xm - 20, kaki=178, tinggi=104, jenis=jenis, baju='a' if jenis == 'wanita' else 'h')
    if penumpang:
        o += orang(xm + 30, kaki=178, tinggi=96, jenis=penumpang, baju='a' if penumpang in ('wanita', 'gadis') else 'h')
    return o + mobil(xm, w=w, taksi=taksi)


def naik_bus(*orang_):
    o = lantai() + bus(150)
    for i, (j, t) in enumerate(orang_):
        o += bulat(95 + i * 40, 118, 10) + jalur(f'M{85 + i * 40} 118 Q{85 + i * 40} 104 {95 + i * 40} 106 Q{105 + i * 40} 104 {105 + i * 40} 118', 'h')
    return o


A['A20-L4a'] = lantai() + bus(150) + bulat(110, 118, 10) + jalur('M100 118 Q100 104 110 106 Q120 104 120 118', 'h')
A['A20-L4b'] = sopir(150, 'wanita')
A['A20-L4c'] = sopir(150, 'pria')
A['A20-L5a'] = lantai() + rumah(95) + rambu_halte(215)
A['A20-L5b'] = lantai() + rumah(80) + stasiun(220, w=120, h=90)
A['A20-L5c'] = lantai() + rumah(80) + mobil(215, w=130, taksi=True)
A['A20-L6a'] = lantai() + mobil(150, w=190, taksi=True)
A['A20-L6b'] = lantai() + jalan_kaki(110, 'wanita', 145, 'a') + jalan_kaki(175, 'pria', 155, 'h')
A['A20-L6c'] = lantai() + bus(150)
A['A20-L8a'] = naik_bus(('gadis', 0), ('laki', 0))
A['A20-L8b'] = naik_bus(('gadis', 0))
A['A20-L8c'] = lantai() + jalan_kaki(110, 'gadis', 115, 'a') + jalan_kaki(170, 'laki', 95, 'h')
A['A20-L9'] = sopir(150, 'pria', penumpang='gadis')
A['A20-L10'] = lantai() + rumah(100) + rambu_halte(215)
A['A20-T3a'] = pesawat(150, 100, .95)
A['A20-T3b'] = lantai() + kereta(150)
A['A20-T3c'] = lantai() + bus(150)
A['A20-T4a'] = lantai() + jalan_kaki(150, 'wanita', 150, 'a')
A['A20-T4b'] = lantai() + mobil(150, w=190)
A['A20-T4c'] = lantai() + bus(150)
A['A20-T6a'] = (jalur('M40 150 L260 150 L230 190 L70 190 Z', 'p') + kotak(110, 110, 80, 40, 'p') + garis((150, 110), (150, 60))
                + jalur('M152 62 L200 100 L152 100 Z', 'p') + jalur('M20 200 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0', 'g'))
A['A20-T6b'] = lantai() + kereta(150)
A['A20-T6c'] = pesawat(150, 100, .95)
A['A20-T7'] = lantai() + stasiun(150, w=170, h=110)
A['A20-T8'] = sopir(150, 'pria')

# A21 — arah
A['A21-1'] = lantai() + stasiun(70, 200, 110, 80) + orang(215, tinggi=150, jenis='pria', baju='a', tangan={'ki': [(20, -10), (48, -18)]}) + panah(170, 40, 120, 40, 5)
A['A21-2'] = lantai() + stasiun(230, 200, 110, 80) + orang(85, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(20, -10), (48, -18)]}) + panah(130, 40, 180, 40, 5)
A['A21-3'] = (lantai() + jalan_kaki(90, 'wanita', 150, 'a') + jam_dinding(215, 90, 56, 0, 0, False)
              + jalur(f'M215 90 L215 34 A56 56 0 0 1 {f(215 + 56 * math.sin(math.radians(30)))} {f(90 - 56 * math.cos(math.radians(30)))} Z', 'a'))
A['A21-4'] = lantai() + pohon(225) + pohon(275, s=.8) + bangku(240) + orang(80, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, -10), (48, -18)]}) + panah(130, 40, 180, 40, 5)
A['A21-5'] = lantai() + rambu_halte(180) + bangku(90, 200, 90)

# --- A21 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
# Peta tampak atas: titik mulai (orang kecil) di bawah tengah, jalan lurus ke atas, persimpangan di y=105.
POS = {'kiri': (65, 58), 'kanan': (235, 58), 'depan': (150, 40), 'tengah': (150, 105), 'belakang': (150, 200), 'atas': (150, 40)}


def ikon(jenis, x, y, s=1.0):
    if jenis == 'taman':
        return (bulat(x - 14 * s, y - 6 * s, 13 * s, 'p') + bulat(x + 12 * s, y - 2 * s, 11 * s, 'p')
                + garis((x - 14 * s, y + 7 * s), (x - 14 * s, y + 16 * s)) + garis((x + 12 * s, y + 9 * s), (x + 12 * s, y + 16 * s)))
    if jenis == 'sekolah':
        return kotak(x - 26 * s, y - 14 * s, 52 * s, 32 * s, 'p') + bentuk((x - 30 * s, y - 14 * s), (x, y - 32 * s), (x + 30 * s, y - 14 * s), k='h') + lonceng(x, y - 20 * s, .14 * s) + kotak(x - 6 * s, y + 4 * s, 12 * s, 14 * s, 'h')
    if jenis == 'stasiun':
        return (kotak(x - 24 * s, y - 20 * s, 48 * s, 38 * s, 'p', 8 * s) + kotak(x - 16 * s, y - 13 * s, 32 * s, 12 * s, 'h', 3)
                + bulat(x - 12 * s, y + 9 * s, 4 * s, 'h') + bulat(x + 12 * s, y + 9 * s, 4 * s, 'h') + garis((x - 30 * s, y + 22 * s), (x + 30 * s, y + 22 * s)))
    if jenis == 'halte':
        return kotak(x - 18 * s, y - 26 * s, 36 * s, 26 * s, 'p', 4) + kotak(x - 11 * s, y - 20 * s, 22 * s, 12 * s, 'h', 3) + garis((x, y), (x, y + 18 * s), lebar=4)
    return ''


def peta(isi, rute=None):
    """isi: {posisi: jenis}; rute: daftar titik untuk panah putus-putus dari titik mulai."""
    o = kotak(10, 6, 280, 208, 'p', 8)
    o += kotak(132, 6, 36, 208, 'a') + kotak(10, 90, 280, 32, 'a')            # jalan
    for pos, j in isi.items():
        x, y = POS.get(pos, pos) if isinstance(pos, str) else pos
        o += ikon(j, x, y, 1.35)
    o += orang(150, kaki=208 if 'belakang' not in isi and (150, 196) not in isi else 150, tinggi=40, jenis='pria', baju='h')   # titik mulai
    if rute:
        pts_ = [(150, 168)] + rute
        o += jalur('M' + ' L'.join(f'{f(a)} {f(b)}' for a, b in pts_), 'g', 3).replace('class="g"', 'class="g" stroke-dasharray="7 6"')
        (a1, b1), (a2, b2) = pts_[-2], pts_[-1]
        o += panah(a1 + (a2 - a1) * .6, b1 + (b2 - b1) * .6, a2, b2, 4)
    return o


A['A21-L4a'] = peta({(150, 105): 'taman', (150, 40): 'sekolah'}, [(150, 62)])
A['A21-L4b'] = peta({(150, 105): 'sekolah', (150, 40): 'taman'}, [(150, 130)])
A['A21-L4c'] = peta({(150, 105): 'taman', (70, 165): 'sekolah'}, [(150, 150), (105, 160)])
A['A21-L5a'] = lantai() + rambu_halte(190) + orang(60, tinggi=140, jenis='wanita', baju='a')
A['A21-L5b'] = lantai() + stasiun(190, w=150, h=100) + orang(60, tinggi=140, jenis='wanita', baju='a')
A['A21-L5c'] = lantai() + pohon(170) + pohon(240, s=.9) + bangku(205, lebar=60) + orang(60, tinggi=140, jenis='wanita', baju='a')
A['A21-L6a'] = peta({'kiri': 'stasiun'})
A['A21-L6b'] = peta({'depan': 'stasiun'})
A['A21-L6c'] = peta({'kanan': 'stasiun'})
A['A21-L8a'] = peta({(150, 105): 'stasiun', 'kanan': 'taman'})
A['A21-L8b'] = peta({(150, 105): 'stasiun', 'kiri': 'taman'})
A['A21-L8c'] = peta({(150, 105): 'stasiun', 'depan': 'taman'})
A['A21-L9'] = (lantai_kamar() + ranjang(120, 200, 170) + weker(240, 120, 18, 7, 0) + teks(240, 92, '!', 22, angka=True)
               + orang(120, kaki=152, tinggi=110, jenis='pria', baju='h', wajah='kaget', tangan={'ki': [(14, -24), (20, -50)], 'ka': [(14, -24), (20, -50)]}))
A['A21-L10'] = peta({(150, 105): 'taman', (150, 40): 'sekolah'}, [(150, 62)])
A['A21-T3a'] = peta({(150, 196): 'stasiun'})
A['A21-T3b'] = peta({'kanan': 'stasiun'})
A['A21-T3c'] = peta({'kiri': 'stasiun'})
A['A21-T4a'] = peta({(150, 105): 'taman', 'kiri': 'sekolah'})
A['A21-T4b'] = peta({(150, 105): 'taman'}) + ikon('sekolah', 150, 112, .5)
A['A21-T4c'] = peta({(150, 105): 'taman', (150, 40): 'sekolah'}, [(150, 62)])
A['A21-T6a'] = (lantai_kamar() + ranjang(150, 200, 190) + kotak(110, 134, 104, 16, 'a', 7) + bulat(98, 132, 12) + muka(98, 132, 12, 'tidur') + teks(122, 110, 'Z', 20, angka=True))
A['A21-T6b'] = lantai() + rumah(100) + jalan_kaki(200, 'pria', 150, 'h') + panah(230, 60, 275, 60, 4)
A['A21-T6c'] = lantai() + rumah(190) + jalan_kaki(90, 'pria', 150, 'h') + panah(110, 60, 150, 60, 4)
A['A21-T7'] = peta({'kiri': 'taman'})
A['A21-T8'] = lantai() + jalan_kaki(130, 'pria', 150, 'h') + garis((60, 80), (95, 80), k='t') + garis((50, 100), (95, 100), k='t') + garis((60, 120), (95, 120), k='t')

# A22 — tubuh & sakit
A['A22-1'] = lantai() + orang(150, tinggi=165, jenis='pria', wajah='sakit', baju='a', tangan=TA) + jalur('M120 22 l-8 -8 M150 16 l0 -10 M180 22 l8 -8', 'g')
A['A22-2'] = (lantai() + kursi_depan(150, 140) + orang(150, tinggi=150, jenis='wanita', duduk=140, wajah='sakit', baju='a', tangan={'ki': [(4, 40), (-8, 60)], 'ka': [(4, 40), (4, 60)]})
              + jalur('M112 180 l-12 -4 M110 192 l-14 2 M122 172 l-8 -10', 'g'))
A['A22-3'] = lantai() + orang(130, tinggi=165, jenis='pria', wajah='sakit', baju='a', tangan={'ka': [(14, 20), (-4, -6)]}) + kertas(140, 60, 22, 18, 10) + jalur('M170 50 l20 -8 M172 60 l24 0 M170 70 l20 8', 'g')
A['A22-4'] = (lantai() + orang(150, tinggi=165, jenis='pria', wajah='sakit', baju='a', tangan={'ki': [(14, 20), (40, 24)], 'ka': [(12, 20), (-30, 26)]})
              + kotak(98, 88, 16, 14, 'a', 3) + jalur('M86 80 l-10 -8 M84 96 l-12 0 M90 110 l-8 8', 'g'))
A['A22-5'] = (lantai() + kursi_depan(150, 140) + orang(150, tinggi=150, jenis='pria', duduk=140, wajah='lelah', baju='a', tangan={'ki': [(2, 40), (-4, 60)], 'ka': [(2, 40), (-4, 60)]})
              + keringat(178, 30) + keringat(122, 38, .8))

# --- A22 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def zoom(bagian, x=235, y=58, r=34):
    """Lingkaran perbesaran berisi bagian tubuh."""
    o = bulat(x, y, r, 'p')
    if bagian == 'mata':
        o += elips(x, y, 20, 11, 'p') + bulat(x, y, 7, 'h') + jalur(f'M{x - 22} {y - 16} Q{x} {y - 26} {x + 22} {y - 16}', 'g')
    elif bagian == 'telinga':
        o += jalur(f'M{x - 8} {y - 22} Q{x + 18} {y - 26} {x + 16} {y + 2} Q{x + 14} {y + 22} {x - 2} {y + 24} Q{x - 10} {y + 22} {x - 6} {y + 12} Q{x + 6} {y + 4} {x + 2} {y - 6} Q{x - 4} {y - 10} {x - 8} {y - 4}', 'p')
    elif bagian == 'mulut':
        o += jalur(f'M{x - 20} {y} Q{x} {y - 14} {x + 20} {y} Q{x} {y + 16} {x - 20} {y} Z', 'p') + garis((x - 18, y), (x + 18, y), k='t')
    elif bagian == 'hidung':
        o += jalur(f'M{x} {y - 22} L{x - 8} {y + 8} Q{x} {y + 14} {x + 10} {y + 8}', 'g', 3) + bulat(x - 14, y + 16, 3, 'a') + bulat(x - 10, y + 24, 3, 'a')
    elif bagian == 'kepala':
        o += bulat(x, y + 4, 18, 'p') + jalur(f'M{x - 18} {y + 2} Q{x} {y - 26} {x + 18} {y + 2}', 'h')
    return o


def sakit(bagian, jenis='pria', x=150, tinggi=None):
    """Orang memegang bagian tubuh yang sakit + tanda nyeri."""
    tinggi = tinggi or (165 if jenis in ('pria', 'wanita') else 110)
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    r = tinggi * (0.12 if jenis in ('laki', 'gadis') else 0.085)
    cy = 200 - tinggi + r
    tangan = {'kepala': {'ki': [(14, -r * 1.2), (6, -r * 2.6)], 'ka': [(14, -r * 1.2), (6, -r * 2.6)]},
              'mata': {'ka': [(12, -r * .6), (-6, -r * 1.7)]},
              'telinga': {'ka': [(14, -r * .5), (2, -r * 1.6)]},
              'mulut': {'ka': [(12, -r * .3), (-4, -r * 1.0)]},
              'hidung': {'ka': [(12, -r * .4), (-8, -r * 1.3)]}}.get(bagian)
    o = orang(x, tinggi=tinggi, jenis=jenis, baju=baju, wajah='sakit', tangan=tangan)
    tanda = {'kepala': (x, cy - r * 1.9), 'mata': (x - r * 1.6, cy - r * .3), 'telinga': (x + r * 2.0, cy), 'mulut': (x - r * 1.6, cy + r * .6),
             'hidung': (x - r * 1.6, cy + r * .1)}.get(bagian)
    if bagian == 'hidung':
        o += kertas(x - r * .5, cy + r * .2, r * .9, r * .8, 10)
    if tanda:
        tx, ty = tanda
        o += jalur(f'M{f(tx - 8)} {f(ty - 6)} l-7 -5 M{f(tx)} {f(ty - 9)} l0 -8 M{f(tx + 8)} {f(ty - 6)} l7 -5', 'g')
    if bagian in ('mata', 'telinga', 'mulut', 'hidung') and x < 200:
        zx = x + 85
        o += garis((x + r * 1.2, cy - r * .2), (zx - 34, 62), k='t') + zoom(bagian, zx, 58)
    return o


def sakit_tangan(jenis='pria', x=150):
    return orang(x, tinggi=165, jenis=jenis, wajah='sakit', baju='a' if jenis == 'wanita' else 'h', tangan={'ki': [(14, 20), (40, 24)], 'ka': [(12, 20), (-30, 26)]}) + jalur(f'M{x + 40} 92 l8 -6 M{x + 44} 100 l10 0', 'g')


def sakit_kaki(jenis='pria', x=150):
    return (kursi_depan(x, 140) + orang(x, tinggi=150, jenis=jenis, duduk=140, wajah='sakit', baju='a' if jenis == 'wanita' else 'h',
                                         tangan={'ki': [(4, 40), (-8, 60)], 'ka': [(4, 40), (4, 60)]}) + jalur(f'M{x + 26} 186 l10 -6 M{x + 28} 196 l12 0', 'g'))


A['A22-L4a'] = lantai() + sakit('mata', 'pria')
A['A22-L4b'] = lantai() + sakit('telinga', 'wanita')
A['A22-L4c'] = lantai() + sakit('telinga', 'pria')
A['A22-L5a'] = lantai() + sakit('hidung', 'gadis')
A['A22-L5b'] = lantai() + sakit('kepala', 'gadis')
A['A22-L5c'] = lantai() + orang(150, tinggi=110, jenis='gadis', baju='a', wajah='lelah') + teks(185, 80, 'Z', 18, angka=True) + teks(198, 64, 'Z', 22, angka=True)
A['A22-L6a'] = lantai() + sakit_tangan('wanita')
A['A22-L6b'] = lantai() + sakit('mulut', 'wanita')
A['A22-L6c'] = lantai() + sakit_kaki('wanita')
A['A22-L8a'] = lantai() + sakit('mata', 'laki')
A['A22-L8b'] = lantai() + sakit('mata', 'gadis')
A['A22-L8c'] = lantai() + sakit('telinga', 'laki')
A['A22-L9'] = lantai() + sakit('mulut', 'wanita')
A['A22-L10'] = lantai() + sakit('kepala', 'pria', 200) + orang(80, tinggi=150, jenis='wanita', baju='a') + gelembung(110, 34, 52, 38, teks(110, 45, '？', 26), (1, 1))
A['A22-T3a'] = lantai() + sakit('kepala', 'pria') + kertas(110, 120, 16, 14, 10)
A['A22-T3b'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(14, -30), (6, -58)]})
A['A22-T3c'] = lantai() + sakit_kaki('pria')
A['A22-T4a'] = lantai() + sakit('hidung', 'wanita')
A['A22-T4b'] = lantai() + sakit('telinga', 'wanita')
A['A22-T4c'] = lantai() + sakit('mata', 'wanita')
A['A22-T6a'] = lantai() + sakit('hidung', 'wanita')
A['A22-T6b'] = lantai() + sakit('telinga', 'wanita')
A['A22-T6c'] = lantai() + sakit('mulut', 'wanita')
A['A22-T7'] = lantai() + kursi_depan(150, 140) + orang(150, tinggi=150, jenis='pria', duduk=140, wajah='lelah', baju='a', tangan={'ki': [(2, 40), (-4, 60)], 'ka': [(2, 40), (-4, 60)]}) + keringat(176, 66)
A['A22-T8'] = (jalur('M120 50 Q190 30 200 100 Q205 150 160 175 Q150 180 150 165 Q150 140 170 120 Q180 90 150 80 Q130 78 128 95', 'p')
               + jalur('M150 100 Q170 100 165 125', 'g'))

# A23 — dokter & obat
A['A23-1'] = lantai() + orang(120, tinggi=165, jenis='pria', baju='a', tangan={'ka': [(14, 26), (-4, -6)]}) + pil(146, 58, .6) + gelas(215, 196, 'air', 1.2)
A['A23-2'] = (lantai() + orang(90, tinggi=165, jenis='wanita', baju='p', kacamata=True, tangan={'ka': [(20, 20), (46, 10)]}) + jalur('M80 70 q10 22 20 0', 't')
              + botol_obat(148, 108, .7) + orang(225, tinggi=150, jenis='pria', baju='a', wajah='sakit', tangan={'ki': [(20, 20), (40, 10)]}))
A['A23-3'] = lantai_kamar() + ranjang(150, 200, 220) + bulat(60, 128, 13) + muka(60, 128, 13, 'tidur') + jalur('M46 123 q2 -18 16 -18 q12 0 13 14', 'h') + teks(96, 104, 'z z', 18, angka=True)
A['A23-4'] = lantai() + rumah_sakit(200) + jalan_kaki(75, 'pria', 150, 'a', 'sakit')
A['A23-5'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', wajah=None) + muka(110, 200 - 160 + 13.6, 13.6, 'senyum') + jam_pasir(215, 110, 1.4)

# --- A23 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def dokter(x, jenis='pria'):
    return orang(x, tinggi=160, jenis=jenis, baju='p') + jalur(f'M{x - 10} 66 Q{x - 14} 96 {x} 100 Q{x + 14} 96 {x + 10} 66', 'g', 2.5) + bulat(x, 102, 4, 'h') + palang(x + 14, 84, .35)


def sakit_ranjang(jenis='wanita', obat=False):
    rambut = jalur('M86 128 Q84 146 76 150 L120 150 Q112 146 110 128 Z', 'h') if jenis in ('wanita', 'gadis') else ''
    o = lantai_kamar() + ranjang(150, 200, 190) + kotak(110, 134, 104, 16, 'a', 7) + rambut + bulat(98, 132, 12) + muka(98, 132, 12, 'sakit')
    if obat:
        o += meja(250, 150, 50) + pil(240, 140, .8) + gelas(262, 150, 'air', .5)
    return o


def sekolah23(x, w=140):
    return (kotak(x - w / 2, 90, w, 110, 'p') + bentuk((x - w / 2 - 10, 90), (x, 52), (x + w / 2 + 10, 90), k='h')
            + garis((x, 52), (x, 14)) + bentuk((x, 14), (x + 30, 22), (x, 30), k='a') + jendela(x - w / 2 + 28, 110, 30, 26) + jendela(x + w / 2 - 28, 110, 30, 26)
            + pintu(x, 200, 60, 36) + lonceng(x, 98, .18))


obat = lambda x=150, y=110, s=2.0: botol_obat(x - 40, y + 50, s * .6) + pil(x + 30, y + 30, s * .9) + pil(x + 60, y + 40, s * .9)
A['A23-L4a'] = buku(150, 170, 90, 120)
A['A23-L4b'] = lantai() + gelas(150, 200, 'air', 2.2)
A['A23-L4c'] = obat()
A['A23-L5a'] = sakit_ranjang('wanita')
A['A23-L5b'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='puas', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(24, -20), (36, -56)]}, kaki_pose={'ki': (-8, 0), 'ka': (30, -26)})
A['A23-L5c'] = lantai() + bioskop(200) + orang(80, tinggi=150, jenis='wanita', baju='a')
A['A23-L6a'] = lantai() + rumah_sakit(150, w=180, h=120)
A['A23-L6b'] = lantai() + sekolah23(150)
A['A23-L6c'] = lantai() + rumah(150, lebar=170, t=120)
A['A23-L8a'] = lantai() + bangku(110, lebar=150) + orang(70, tinggi=120, jenis='pria', baju='h', duduk=172) + orang(110, tinggi=115, jenis='wanita', baju='a', duduk=172) + orang(150, tinggi=100, jenis='laki', baju='h', duduk=172) + palang(250, 60, 1.0)
A['A23-L8b'] = lantai() + bangku(110, lebar=150) + orang(110, tinggi=115, jenis='wanita', baju='a', duduk=172) + palang(250, 60, 1.0)
A['A23-L8c'] = lantai() + meja(150, 150, 220) + mangkuk_mi(90, 128, .4) + mangkuk_mi(210, 128, .4) + orang(60, tinggi=120, jenis='pria', baju='h') + orang(150, tinggi=115, jenis='wanita', baju='a') + orang(250, tinggi=100, jenis='laki', baju='h')
A['A23-L9'] = sakit_ranjang('gadis', True)
A['A23-L10'] = lantai() + rumah_sakit(215, w=140, h=110) + jalan_kaki(80, 'pria', 150, 'h')
A['A23-T3a'] = matahari(80, 70, 22) + pil(80, 140, 1.4) + bulan_bintang(220, 70, .7) + pil(220, 140, 1.4)
A['A23-T3b'] = bulan_bintang(150, 70, .7) + pil(150, 140, 1.4)
A['A23-T3c'] = matahari(150, 70, 22) + pil(150, 140, 1.4)
A['A23-T4a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h', kaki_pose={'ki': (-12, 0), 'ka': (26, -14)}) + bola(205, 186, 14)
A['A23-T4b'] = sakit_ranjang('pria')
A['A23-T4c'] = lantai() + sekolah23(215, 120) + jalan_kaki(70, 'pria', 150, 'h')
A['A23-T6a'] = sakit_ranjang('pria').replace(muka(98, 132, 12, 'sakit'), muka(98, 132, 12, 'tidur'))
A['A23-T6b'] = lantai() + rumah_sakit(215, w=140, h=110) + jalan_kaki(80, 'pria', 150, 'h')
A['A23-T6c'] = lantai() + rumah_sakit(225, w=120, h=110) + jalan_kaki(45, 'pria', 160, 'h') + jalan_kaki(95, 'wanita', 150, 'a') + jalan_kaki(140, 'laki', 100, 'h')
A['A23-T7'] = sakit_ranjang('wanita', True)
A['A23-T8'] = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a') + orang(210, tinggi=145, jenis='pria', baju='h', wajah='sakit') + pil(250, 150, 1.0) + gelembung(130, 40, 56, 40, teks(130, 52, '？', 28), (-1, 1))

# A24 — cuaca
A['A24-1'] = lantai() + awan(150, 30, 1.2, 'a') + hujan(150, 58, 240, 60, 11) + orang(150, tinggi=145, jenis='wanita', baju='h', tangan={'ka': [(8, -6), (-14, -30)]}) + payung(150, 72, 58)
A['A24-2'] = (lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='sedih', tangan={'ki': [(20, 12), (-10, 26)], 'ka': [(20, 12), (-10, 26)]})
              + kotak(134, 68, 32, 10, 'a', 4) + kotak(150, 72, 10, 28, 'a', 3) + jalur('M110 90 l-8 4 l8 4 l-8 4 M190 90 l8 4 l-8 4 l8 4', 'g')
              + salju(60, 60, 10) + salju(240, 50, 8) + salju(250, 120, 9) + salju(50, 130, 7) + salju(92, 30, 6) + salju(212, 150, 6))
A['A24-3'] = lantai() + gunung(150, 200, 260, 150, salju=False) + bunga(70, 150) + bunga(110, 160) + bunga(190, 158) + bunga(230, 150) + bunga(150, 168)
A['A24-4'] = lantai() + matahari(60, 50, 22, 'h') + orang(170, tinggi=160, jenis='pria', baju='p', wajah='lelah', tangan={'ka': [(14, -6), (10, -26)]}) + keringat(145, 44) + keringat(196, 52) + keringat(150, 90, .8)
A['A24-5'] = (lantai() + gunung(120, 200, 220, 140) + angin(170, 60, .9)
              + f'<g transform="rotate(22 252 200)">{pohon(252, 200, .7)}</g>')

# --- A24 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def dingin(x, jenis='pria', tinggi=150):
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    r = tinggi * (0.12 if jenis in ('laki', 'gadis') else 0.085)
    o = orang(x, tinggi=tinggi, jenis=jenis, baju=baju, wajah='sedih', tangan={'ki': [(8, 18), (30, 22)], 'ka': [(8, 18), (-30, 22)]})
    y = 200 - tinggi + r * 2.6
    return o + garis((x - r * 2.2, y), (x - r * 2.8, y + 6), k='t') + garis((x + r * 2.2, y), (x + r * 2.8, y + 6), k='t') + garis((x - r * 2.4, y + 14), (x - r * 3, y + 20), k='t') + garis((x + r * 2.4, y + 14), (x + r * 3, y + 20), k='t')


def panas(x, jenis='pria', tinggi=150):
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, wajah='lelah', tangan={'ka': [(14, -20), (-2, -40)]}) + keringat(x + 22, 200 - tinggi + 8) + keringat(x - 20, 200 - tinggi + 22)


hujan24 = lambda: awan(150, 40, 1.0) + hujan(150, 60, 160, 70)
A['A24-L4a'] = lantai() + matahari(240, 50, 26) + panas(120)
A['A24-L4b'] = lantai() + awan(230, 40, .6) + dingin(120)
A['A24-L4c'] = lantai() + hujan24() + orang(150, tinggi=120, jenis='pria', baju='h')
A['A24-L5a'] = lantai() + matahari(240, 50, 26) + panas(120, 'wanita')
A['A24-L5b'] = lantai() + salju(60, 40) + salju(210, 30) + salju(250, 80) + salju(90, 90) + dingin(150, 'wanita')
A['A24-L5c'] = lantai() + matahari(245, 45, 16) + bunga(70, 175) + bunga(230, 180) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='puas')
A['A24-L6a'] = lantai() + sofa(110) + orang(100, tinggi=140, jenis='pria', baju='h', duduk=150) + orang(140, tinggi=130, jenis='wanita', baju='a', duduk=150) + tv(250, 150, 70) + meja(250, 150, 70)
A['A24-L6b'] = lantai() + gunung(170, w=240, h=150, salju=False) + jalan_kaki(60, 'wanita', 120, 'a') + jalan_kaki(95, 'pria', 130, 'h')
A['A24-L6c'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(125, tinggi=145, jenis='wanita', baju='a') + orang(178, tinggi=150, jenis='pria', baju='h')
A['A24-L8a'] = lantai() + hujan24() + dingin(150, 'pria', 120)
A['A24-L8b'] = lantai() + hujan24() + panas(150, 'pria', 120)
A['A24-L8c'] = lantai() + matahari(240, 50, 22) + dingin(130, 'pria', 120)
A['A24-L9'] = lantai() + gunung(150, w=260, h=160, salju=False) + matahari(250, 40, 20) + bunga(80, 190, .7) + bunga(230, 192, .7)
A['A24-L10'] = kalender_bulan(110, 40, 7, '', 130, 140).replace('>None<', '><') + matahari(235, 100, 36)
A['A24-T3a'] = matahari(150, 110, 50)
A['A24-T3b'] = awan(150, 50, 1.2) + salju(90, 110, 16) + salju(200, 100, 14) + salju(150, 160, 18) + salju(240, 170, 13) + salju(70, 180, 14)
A['A24-T3c'] = awan(150, 70, 1.6) + hujan(150, 110, 200, 90, 13)
A['A24-T4a'] = lantai() + hujan24() + orang(150, tinggi=120, jenis='wanita', baju='a')
A['A24-T4b'] = lantai() + angin(220, 70, 1.4) + dingin(110, 'wanita')
A['A24-T4c'] = lantai() + matahari(240, 50, 26) + panas(120, 'wanita')
A['A24-T6a'] = kalender_bulan(110, 40, 7, '', 130, 140) + matahari(235, 100, 36)
A['A24-T6b'] = awan(150, 70, 1.6) + hujan(150, 110, 200, 90, 13)
A['A24-T6c'] = lantai() + dingin(150, 'pria')
A['A24-T7'] = lantai() + gunung(150, w=260, h=150, salju=False) + bunga(70, 192, .8) + bunga(120, 196, .7) + bunga(190, 194, .8) + bunga(240, 192, .7)
A['A24-T8'] = lantai() + jalur('M20 200 Q90 130 150 140 Q210 130 280 200 Z', 'a') + orang(150, kaki=142, tinggi=60, jenis='laki', baju='h')

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

# --- A25 tulis ulang 2026-11-13: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def telepon(jenis_penelepon, siapa, x=80):
    """Orang menelepon; gelembung menunjukkan orang yang ditelepon."""
    o = lantai() + orang_ponsel(x, jenis_penelepon, 150, baju='h' if jenis_penelepon == 'pria' else 'a')
    isi = {'kakak_lk': orang(215, kaki=118, tinggi=80, jenis='pria', baju='a'),
           'ibu': orang(215, kaki=118, tinggi=78, jenis='wanita', baju='a', rambut='uban'),
           'guru': papan_tulis(232, 46, 46, 30) + orang(200, kaki=118, tinggi=78, jenis='wanita', baju='a')}[siapa]
    return o + gelembung(215, 72, 110, 96, isi, (-1, 1))


def bawa(*benda):
    o = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 20), (40, 10)]})
    xs = 170
    for b in benda:
        o += {'ponsel': ponsel(xs, 100, 1.4), 'buku': buku(xs, 140, 36, 48), 'pena': pulpen(xs, 110, 60, 70)}[b]
        xs += 50
    return o


def waktu(langit):
    o = {'malam': bulan_bintang(80, 70, 1.0), 'sore': matahari(80, 50, 24),
         'pagi': matahari(80, 140, 26) + kotak(20, 140, 130, 60, 'n') + garis((20, 140), (140, 140))}[langit]
    return o + ponsel(200, 100, 2.4)


A['A25-L4a'] = telepon('pria', 'kakak_lk')
A['A25-L4b'] = telepon('pria', 'ibu')
A['A25-L4c'] = telepon('pria', 'guru')
A['A25-L5a'] = bawa('ponsel')
A['A25-L5b'] = bawa('ponsel', 'buku')
A['A25-L5c'] = bawa('buku', 'pena')
A['A25-L6a'] = waktu('malam')
A['A25-L6b'] = waktu('sore')
A['A25-L6c'] = waktu('pagi')
A['A25-L8a'] = lantai() + orang(110, tinggi=150, jenis='wanita', baju='a', wajah='sedih', tangan={'ka': [(20, 24), (40, 30)]}) + tas_belanja(175, 190, 1.2) + teks(175, 120, '？', 30)
A['A25-L8b'] = lantai() + orang_ponsel(130, 'wanita', 150, baju='a')
A['A25-L8c'] = lantai() + orang(110, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 20), (40, 10)]}) + buku(175, 140, 40, 52)
A['A25-L9'] = (lantai() + kotak(20, 60, 40, 140, 'p') + kotak(240, 60, 40, 140, 'p') + garis((60, 70), (240, 70), lebar=5)
               + orang(110, tinggi=145, jenis='wanita', baju='a', tangan=LAMBAI) + orang(190, tinggi=150, jenis='pria', baju='h', tangan={'ki': [(14, -30), (6, -58)]}))
A['A25-L10'] = lantai() + orang(150, tinggi=155, jenis='pria', baju='h', tangan={'ka': [(20, 10), (44, 0)], 'ki': [(20, 10), (44, 0)]}) + orang(60, tinggi=148, jenis='wanita', baju='a') + orang(240, tinggi=150, jenis='pria', baju='a')
A['A25-T3a'] = lantai() + meja(150, 150, 160) + komputer(150, 150, 120)
A['A25-T3b'] = ponsel(150, 110, 3.0)
A['A25-T3c'] = lantai() + tv(150, 150, 140) + meja(150, 150, 140)
A['A25-T4a'] = A['A25-L10']
A['A25-T4b'] = lantai() + orang_ponsel(130, 'pria', 155, baju='h')
A['A25-T4c'] = A['A25-L9']
A['A25-T6a'] = lantai() + rumah(90) + meja(225, 160, 70) + ponsel(225, 150, .9) + teks(225, 110, '！', 26)
A['A25-T6b'] = lantai() + jalan_kaki(130, 'pria', 150, 'h') + buku(165, 120, 26, 34)
A['A25-T6c'] = lantai() + orang_ponsel(130, 'pria', 155, baju='h') + tas_punggung(105, 70, .8)
A['A25-T7'] = A['A25-L10']
A['A25-T8'] = lantai() + orang_ponsel(130, 'pria', 155, baju='h') + sinyal(175, 50)

