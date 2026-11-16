"""Adegan ilustrasi 聽力 Part 1 — Volume 2 (B01–B46). ID = <modul>-<n> (listen_pic ke-n, urut isi → soal → bank)."""
from svg_adegan import *

A = {}
JOG = {'ki': [(16, 20), (30, 4)], 'ka': [(10, 28), (-6, 44)]}   # tangan berayun saat lari
LARI = {'ki': (-26, 0), 'ka': (22, -10)}


def pelari(x, jenis='pria', baju='a', tinggi=150):
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan=JOG, kaki_pose=LARI)


def tunjuk_ke(x, jenis, tinggi, sisi=1, baju='a', wajah='senyum'):
    """Orang menunjuk ke samping (sisi 1 = kanan)."""
    t = {'ka' if sisi == 1 else 'ki': [(20, -6), (46, -14)]}
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan=t, wajah=wajah)


# B01 — olahraga
A['B01-1'] = (lantai() + ring_basket(255) + orang(110, tinggi=165, jenis='pria', baju='a', tangan={'ki': [(10, -30), (4, -64)], 'ka': [(10, -30), (4, -64)]})
              + bola(110, 18, 14, 'basket'))
A['B01-2'] = lantai() + matahari(245, 52, 16) + jalur('M200 118 Q245 96 290 118', 't') + pelari(120, 'pria', 'a', 160)
A['B01-3'] = lantai() + gawang(235, 200, 100, 70) + orang(90, tinggi=120, jenis='laki', baju='h', kaki_pose={'ki': (-10, 0), 'ka': (30, -18)}) + bola(145, 184, 14)
A['B01-4'] = (lantai() + orang(130, tinggi=165, jenis='pria', baju='a', tangan={'ki': [(4, 24), (30, 18)], 'ka': [(-14, 24), (6, 18)]})
              + tongkat_bisbol(150, 92, 215, 40) + bola(250, 66, 9))
A['B01-5'] = lantai() + matahari(60, 60, 18) + jalur('M16 120 Q60 96 104 120', 't') + pelari(170, 'wanita', 'a', 155)

# --- B01 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def raket(x, y, s=1.0):
    return garis((x, y + 26 * s), (x, y + 52 * s), lebar=4) + elips(x, y, 15 * s, 22 * s, 'p') + garis((x - 10 * s, y), (x + 10 * s, y), k='t') + garis((x, y - 16 * s), (x, y + 16 * s), k='t')


def olahraga(jenis_olahraga, x=120, jenis='pria', tinggi=150):
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    if jenis_olahraga == 'tenis':
        return lantai() + orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan={'ka': [(22, -10), (40, -36)]}) + raket(x + 46, 200 - tinggi * .9, .9) + bola(x + 90, 60, 8, 'basket')
    if jenis_olahraga == 'basket':
        return lantai() + ring_basket(240) + orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan={'ki': [(20, -10), (28, -40)], 'ka': [(20, -10), (28, -40)]}) + bola(x, 200 - tinggi - 20, 13, 'basket')
    if jenis_olahraga == 'sepak':
        return lantai() + gawang(235) + orang(x, tinggi=tinggi, jenis=jenis, baju=baju, kaki_pose={'ki': (-12, 0), 'ka': (tinggi * .2, -tinggi * .12)}) + bola(x + tinggi * .32, 186, 13)
    if jenis_olahraga == 'renang':
        r, cy = 14, 132
        rambut = (jalur(f'M{x - r} {cy} Q{x - r} {cy - r * 1.3} {x} {cy - r * 1.2} Q{x + r} {cy - r * 1.3} {x + r} {cy}', 'h') if jenis in ('pria', 'laki')
                  else jalur(f'M{x - r - 2} {cy + 12} Q{x - r - 3} {cy - r * 1.3} {x} {cy - r * 1.2} Q{x + r + 3} {cy - r * 1.3} {x + r + 2} {cy + 12}', 'h'))
        return (kotak(10, 150, 280, 60, 'a') + rambut + bulat(x, cy, r) + muka(x, cy, r, 'senyum')
                + jalur('M10 150 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0', 'g')
                + garis((x + 16, 146), (x + 44, 116), (x + 62, 134), lebar=5))
    if jenis_olahraga == 'lari':
        return lantai() + pelari(x, jenis, baju, tinggi)
    return ''


A['B01-L4a'] = olahraga('tenis', jenis='wanita')
A['B01-L4b'] = olahraga('basket', jenis='pria')
A['B01-L4c'] = olahraga('tenis', jenis='pria')
A['B01-L5a'] = olahraga('renang', jenis='wanita')
A['B01-L5b'] = olahraga('lari', 140, jenis='wanita')
A['B01-L5c'] = olahraga('sepak', 100, jenis='wanita')
A['B01-L6a'] = olahraga('sepak', 100, jenis='pria')
A['B01-L6b'] = olahraga('renang', 120, jenis='pria')
A['B01-L6c'] = olahraga('basket', jenis='pria')
A['B01-L8a'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, -6), (36, -20)]}) + tongkat_bisbol(140, 90, 200, 40) + bola(190, 186, 14)
A['B01-L8b'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, -6), (36, -20)]}) + tongkat_bisbol(140, 90, 200, 40) + bola(190, 184, 15, 'basket')
A['B01-L8c'] = lantai() + orang(110, tinggi=155, jenis='wanita', baju='a', tangan={'ka': [(20, -6), (36, -20)]}) + tongkat_bisbol(140, 92, 200, 42) + bola(190, 186, 14)
A['B01-L9'] = lantai() + matahari(250, 45, 18) + pohon(45) + pelari(150, 'wanita', 'a', 150)
A['B01-L10'] = (lantai() + orang(110, tinggi=105, jenis='laki', baju='h', wajah='sedih') + kotak(118, 160, 14, 36, 'p', 4) + bola(210, 186, 14)
                + gelembung_pikiran(190, 50, 70, 50, bola(190, 50, 14)))
A['B01-T3a'] = olahraga('tenis', jenis='pria')
A['B01-T3b'] = olahraga('sepak', 100, jenis='pria')
A['B01-T3c'] = olahraga('basket', jenis='pria')
A['B01-T4a'] = olahraga('renang', 120, jenis='wanita')
A['B01-T4b'] = olahraga('tenis', jenis='wanita')
A['B01-T4c'] = olahraga('lari', 140, jenis='wanita')
A['B01-T6a'] = lantai() + ring_basket(250) + orang(90, tinggi=110, jenis='laki', baju='h') + orang(160, tinggi=105, jenis='laki', baju='a', tangan={'ki': [(20, -10), (28, -40)], 'ka': [(20, -10), (28, -40)]}) + bola(160, 70, 12, 'basket')
A['B01-T6b'] = lantai() + gawang(240) + orang(80, tinggi=110, jenis='laki', baju='h') + orang(150, tinggi=105, jenis='laki', baju='a', kaki_pose={'ki': (-12, 0), 'ka': (22, -14)}) + bola(185, 186, 12)
A['B01-T6c'] = lantai() + orang(100, tinggi=110, jenis='laki', baju='h', tangan={'ka': [(20, -6), (36, -20)]}) + tongkat_bisbol(125, 130, 175, 90) + orang(220, tinggi=105, jenis='laki', baju='a') + bola(170, 120, 8)
A['B01-T7'] = olahraga('renang', 120, jenis='pria')
A['B01-T8'] = olahraga('renang', 120, jenis='laki')

# B02 — rencana akhir pekan
A['B02-1'] = lantai() + pohon(250, s=.9) + tikar(120, 150, 200, 44) + keranjang(90, 164, 1.1) + buah_apel(150, 166, .6) + roti(190, 168, .45)
A['B02-2'] = (lantai() + pohon(40, s=.9) + pohon(262, s=.8) + tikar(150, 164, 200, 36) + keranjang(215, 176, .8)
              + orang(118, tinggi=130, jenis='wanita', duduk=176, baju='a') + orang(170, tinggi=100, jenis='gadis', duduk=176, baju='h'))
A['B02-3'] = (lantai() + orang(130, tinggi=165, jenis='pria', baju='a', wajah='puas') + headphone(130, 49, 14)
              + not_musik(200, 70) + not_musik(236, 110) + not_musik(60, 96))
A['B02-4'] = (lantai() + garis((20, 40), (280, 40), k='t') + ''.join(bentuk((30 + i * 36, 40), (48 + i * 36, 40), (39 + i * 36, 58), k='h' if i % 2 else 'a') for i in range(7))
              + orang(70, tinggi=140, jenis='wanita', baju='a', tangan=LAMBAI) + orang(150, tinggi=150, jenis='pria', baju='h', tangan={'ki': [(14, -30), (6, -58)]})
              + orang(230, tinggi=110, jenis='laki', baju='a', tangan=LAMBAI))
A['B02-5'] = garis((16, 196), (284, 196), k='t') + bingkai(150, 34, 170, 120, gunung(150, 154, 160, 90) + matahari(200, 64, 10) + pohon(98, 154, .5))

# --- B02 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kamera(x, y, s=1.0):
    return kotak(x - 22 * s, y - 14 * s, 44 * s, 30 * s, 'h', 4 * s) + bulat(x, y + 1 * s, 10 * s, 'p') + bulat(x, y + 1 * s, 5 * s, 'h') + kotak(x - 16 * s, y - 20 * s, 12 * s, 7 * s, 'h')


def memotret(x, jenis):
    baju = 'a' if jenis == 'wanita' else 'h'
    return orang(x, tinggi=150, jenis=jenis, baju=baju, tangan={'ki': [(16, 12), (8, -14)], 'ka': [(16, 12), (8, -14)]}) + kamera(x, 200 - 150 + 22, .9)


def buku_buka(x, y, w=90, h=60, gambar=True):
    o = jalur(f'M{x} {y} L{x - w / 2} {y - 6} L{x - w / 2} {y + h} L{x} {y + h + 6} Z', 'p') + jalur(f'M{x} {y} L{x + w / 2} {y - 6} L{x + w / 2} {y + h} L{x} {y + h + 6} Z', 'p')
    if gambar:
        o += matahari(x - w / 4, y + h / 3, 7) + jalur(f'M{x + 8} {y + h * .8} l12 -20 l10 12 l8 -8 l8 16', 'g')
    return o


def pegang_buku(x, jenis, isi='cerita'):
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    o = orang(x, tinggi=150, jenis=jenis, baju=baju, tangan={'ki': [(18, 24), (40, 30)], 'ka': [(18, 24), (40, 30)]})
    if isi == 'cerita':
        return o + buku_buka(x, 90, 70, 46)
    if isi == 'foto':
        return o + kotak(x - 34, 86, 68, 46, 'p', 3) + kotak(x - 28, 92, 26, 18, 'a') + kotak(x + 2, 92, 26, 18, 'a') + kotak(x - 28, 112, 26, 16, 'a') + kotak(x + 2, 112, 26, 16, 'a')
    return o


def menggambar2(x, jenis='gadis'):
    return kuda_gambar(x + 95) + orang(x, tinggi=105 if jenis == 'gadis' else 145, jenis=jenis, baju='a', wajah='puas', tangan={'ka': [(20, -4), (46, -14)]})


piknik = lambda *org: lantai() + pohon(260, s=.9) + tikar(130, 176) + keranjang(150, 176, .8) + ''.join(org)
A['B02-L4a'] = lantai() + pohon(250) + memotret(120, 'pria')
A['B02-L4b'] = lantai() + orang(120, tinggi=150, jenis='pria', baju='h', wajah='puas') + headphone(120, 200 - 150 + 13, 13) + not_musik(170, 60) + not_musik(200, 90)
A['B02-L4c'] = lantai() + pohon(250) + memotret(120, 'wanita')
A['B02-L5a'] = lantai() + menggambar2(80, 'wanita')
A['B02-L5b'] = lantai() + pegang_buku(150, 'wanita', 'cerita')
A['B02-L5c'] = lantai() + pegang_buku(150, 'wanita', 'foto')
A['B02-L6a'] = piknik(orang(70, tinggi=120, jenis='wanita', baju='a', duduk=176), orang(225, tinggi=125, jenis='pria', baju='h', duduk=176))
A['B02-L6b'] = lantai() + orang(80, tinggi=150, jenis='wanita', baju='a') + buku_buka(80, 92, 60, 40) + orang(170, tinggi=95, jenis='laki', baju='h') + orang(240, tinggi=92, jenis='gadis', baju='a')
A['B02-L6c'] = lantai() + bulan_bintang(40, 40, .6) + mimbar(150) + orang(150, tinggi=150, jenis='wanita', baju='a', wajah='nyanyi') + mikrofon(176, 92) + not_musik(220, 60) + not_musik(250, 90)
A['B02-L8a'] = piknik(orang(70, tinggi=120, jenis='wanita', baju='a', duduk=176), memotret(220, 'pria'))
A['B02-L8b'] = piknik(orang(70, tinggi=120, jenis='wanita', baju='a', duduk=176), orang(225, tinggi=125, jenis='pria', baju='h', duduk=176))
A['B02-L8c'] = (jalur('M10 170 q20 -10 40 0 q20 10 40 0 q20 -10 40 0 q20 10 40 0 q20 -10 40 0 q20 10 40 0 q20 -10 40 0', 'g') + matahari(250, 45, 18)
                + memotret(120, 'pria').replace('', ''))
A['B02-L9'] = lantai() + menggambar2(80, 'gadis')
A['B02-L10'] = lantai() + orang(120, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(16, 30), (26, 50)]}) + tas_kerja(150, 196) + kalender_bulan(240, 30, 6, 6, 70, 70)
A['B02-T3a'] = lantai() + bioskop(200) + orang(80, tinggi=150, jenis='wanita', baju='a')
A['B02-T3b'] = olahraga('renang', 120, jenis='pria')
A['B02-T3c'] = piknik(orang(70, tinggi=120, jenis='wanita', baju='a', duduk=176))
A['B02-T4a'] = lantai() + mimbar(150) + orang(90, tinggi=140, jenis='wanita', baju='a', wajah='nyanyi') + orang(210, tinggi=150, jenis='pria', baju='h', wajah='nyanyi') + not_musik(150, 50) + not_musik(180, 70)
A['B02-T4b'] = piknik(orang(70, tinggi=120, jenis='wanita', baju='a', duduk=176), orang(225, tinggi=125, jenis='pria', baju='h', duduk=176))
A['B02-T4c'] = lantai() + pelari(100, 'pria', 'h', 150) + pelari(200, 'wanita', 'a', 145)
A['B02-T6a'] = lantai() + orang(90, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(20, 10), (44, 0)]}) + ponsel(150, 82, 1.2) + orang(220, tinggi=150, jenis='wanita', baju='a', rambut='uban')
A['B02-T6b'] = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a', rambut='uban') + buku_buka(90, 92, 60, 40) + orang(210, tinggi=95, jenis='gadis', baju='a')
A['B02-T6c'] = lantai() + orang(110, tinggi=150, jenis='pria', baju='h', wajah='nyanyi') + mikrofon(138, 90) + not_musik(190, 60) + not_musik(230, 90)
A['B02-T7'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='h') + buku_buka(90, 92, 60, 40) + orang(210, tinggi=95, jenis='laki', baju='h')
A['B02-T8'] = not_musik(110, 90, 2.2) + not_musik(190, 70, 2.2)

# B03 — pertandingan
_p, _pos = podium(150)
A['B03-1'] = lantai() + _p + orang(_pos[1][0], kaki=_pos[1][1], tinggi=100, jenis='pria', baju='a', tangan=ANGKAT) + orang(_pos[2][0], kaki=_pos[2][1], tinggi=100, jenis='pria', baju='a') + orang(_pos[3][0], kaki=_pos[3][1], tinggi=100, jenis='pria', baju='h') + panah(_pos[3][0], _pos[3][1] - 140, _pos[3][0], _pos[3][1] - 106, 5)
A['B03-2'] = lantai() + _p + orang(_pos[1][0], kaki=_pos[1][1], tinggi=100, jenis='pria', baju='h', tangan=ANGKAT) + panah(_pos[1][0], 12, _pos[1][0], 26, 5)
A['B03-3'] = (lantai() + orang(60, tinggi=140, jenis='wanita', baju='a', wajah='nyanyi', tangan={'ki': [(14, -30), (6, -58)], 'ka': [(14, -30), (6, -58)]})
              + orang(150, tinggi=150, jenis='pria', baju='h', wajah='nyanyi', tangan={'ki': [(14, -30), (6, -58)], 'ka': [(14, -30), (6, -58)]})
              + orang(240, tinggi=135, jenis='wanita', baju='p', wajah='nyanyi', tangan={'ki': [(14, -30), (6, -58)], 'ka': [(14, -30), (6, -58)]}))
A['B03-4'] = tiket(150, 60, 220, 110) + tongkat_bisbol(80, 150, 150, 80) + bola(170, 110, 16) + teks(236, 124, 'VS', 20, angka=True)
A['B03-5'] = lantai() + _p + orang(_pos[1][0], kaki=_pos[1][1], tinggi=100, jenis='pria', baju='a', tangan=ANGKAT) + orang(_pos[2][0], kaki=_pos[2][1], tinggi=100, jenis='pria', baju='h') + panah(_pos[2][0], _pos[2][1] - 140, _pos[2][0], _pos[2][1] - 106, 5)

# --- B03 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def tiket_olahraga(x, y, jenis='bisbol', w=120, h=60):
    ikon = {'bisbol': tongkat_bisbol(x - w / 2 + 14, y + h - 12, x - w / 2 + 44, y + 12) + bola(x - w / 2 + 50, y + 20, 7),
            'basket': bola(x - w / 2 + 32, y + h / 2, 16, 'basket')}[jenis]
    return tiket(x, y, w, h) + ikon + teks(x + w / 4 + 14, y + h / 2 + 7, 'VS', 15, angka=True)


def tumpuk_tiket(n, jenis='bisbol'):
    return ''.join(tiket_olahraga(150 + (i - (n - 1) / 2) * 18, 50 + i * 34, jenis) for i in range(n))


def juara(n, piala=False):
    p, pos = podium(150)
    o = lantai() + p
    for k in (1, 2, 3):
        o += orang(pos[k][0], kaki=pos[k][1], tinggi=95, jenis='pria', baju='h' if k == n else 'a', tangan=ANGKAT if k == n else None)
    if piala:
        o += jalur(f'M{pos[n][0] + 18} 30 L{pos[n][0] + 42} 30 L{pos[n][0] + 36} 52 L{pos[n][0] + 24} 52 Z', 'a') + garis((pos[n][0] + 30, 52), (pos[n][0] + 30, 62))
    else:
        o += panah(pos[n][0], pos[n][1] - 140, pos[n][0], pos[n][1] - 106, 5)
    return o


def pertandingan(jenis):
    if jenis == 'sepak':
        return lantai() + gawang(240) + orang(80, tinggi=120, jenis='pria', baju='h') + orang(150, tinggi=118, jenis='pria', baju='a', kaki_pose={'ki': (-12, 0), 'ka': (24, -14)}) + bola(190, 186, 12)
    if jenis == 'basket':
        return lantai() + ring_basket(250) + orang(90, tinggi=120, jenis='pria', baju='h') + orang(165, tinggi=118, jenis='pria', baju='a', tangan={'ki': [(20, -10), (28, -40)], 'ka': [(20, -10), (28, -40)]}) + bola(165, 64, 12, 'basket')
    return lantai() + orang(100, tinggi=125, jenis='pria', baju='h', tangan={'ka': [(20, -6), (36, -20)]}) + tongkat_bisbol(125, 125, 175, 85) + orang(230, tinggi=118, jenis='pria', baju='a') + bola(170, 110, 8)


A['B03-L4a'] = tumpuk_tiket(2)
A['B03-L4b'] = tumpuk_tiket(3)
A['B03-L4c'] = buku_tumpuk(150, 180, 3, 110, 30)
A['B03-L5a'] = juara(1)
A['B03-L5b'] = juara(3)
A['B03-L5c'] = juara(2)
A['B03-L6a'] = pertandingan('sepak')
A['B03-L6b'] = pertandingan('basket')
A['B03-L6c'] = pertandingan('bisbol')
A['B03-L8a'] = tumpuk_tiket(2)
A['B03-L8b'] = tumpuk_tiket(1)
A['B03-L8c'] = tumpuk_tiket(2, 'basket')
A['B03-L9'] = juara(1, True)
A['B03-L10'] = (lantai() + jalur('M20 120 Q150 40 280 120 L280 200 L20 200 Z', 'a') + kotak(100, 150, 100, 50, 'p')
                + orang(150, tinggi=140, jenis='pria', baju='h', wajah='kaget', tangan={'ki': [(14, -30), (6, -58)], 'ka': [(14, -30), (6, -58)]}))
A['B03-T3a'] = label_harga(150, 80, '300', 200, 76)
A['B03-T3b'] = label_harga(150, 80, '30', 200, 76)
A['B03-T3c'] = label_harga(150, 80, '3,000', 200, 76)
A['B03-T4a'] = jam_dinding(150, 110, 80, 8, 0) + bulan_bintang(255, 40, .6)
A['B03-T4b'] = jam_dinding(150, 110, 80, 7, 0) + bulan_bintang(255, 40, .6)
A['B03-T4c'] = jam_dinding(150, 110, 80, 2, 0) + matahari(255, 40, 16)
A['B03-T6a'] = lantai() + orang(110, tinggi=150, jenis='pria', baju='h', wajah='sedih') + orang(190, tinggi=150, jenis='pria', baju='a', wajah='sedih')
A['B03-T6b'] = juara(1, True)
A['B03-T6c'] = juara(2)
A['B03-T7'] = tumpuk_tiket(3)
A['B03-T8'] = A['B03-3'] + teks(150, 22, '加油！', 22)

# B04 — sedang apa
A['B04-1'] = lantai() + meja(170, 130, 180) + komputer(185, 130, 90) + orang(85, tinggi=150, jenis='pria', duduk=140, baju='h', tangan={'ka': [(26, 4), (56, -2)]}) + sinyal(250, 40)
A['B04-2'] = lantai() + meja(170, 130, 180) + komputer(185, 130, 90) + orang(85, tinggi=150, jenis='wanita', duduk=140, baju='a', tangan={'ka': [(26, 4), (56, -2)]}) + sinyal(250, 40)
A['B04-3'] = (lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (38, -4)]}) + orang(210, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 10), (38, -4)]})
              + titik_obrolan(120, 24, 56, 32, (-1, 1)) + titik_obrolan(186, 30, 56, 32, (1, 1)))
A['B04-4'] = lantai() + orang_ponsel(150, 'pria', 165, baju='a') + sinyal(190, 60)
A['B04-5'] = dua_panel(orang(75, kaki=200, tinggi=150, jenis='wanita', baju='a') + komputer(75, 190, 96) + titik_obrolan(112, 36, 56, 32, (-1, 1)),
                       orang(225, kaki=200, tinggi=155, jenis='pria', baju='h') + komputer(225, 190, 96) + titik_obrolan(188, 36, 56, 32, (1, 1)))

# --- B04 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def di_komputer(x, jenis, tinggi=None):
    tinggi = tinggi or (150 if jenis in ('pria', 'wanita') else 100)
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    return meja(x + 80, 140, 120) + komputer(x + 80, 140, 90) + orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan={'ka': [(20, 24), (46, 28)]})


def nonton_tv(x, jenis, tinggi=None):
    tinggi = tinggi or (150 if jenis in ('pria', 'wanita') else 100)
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    return tv(x + 90, 150, 80) + meja(x + 90, 150, 80) + orang(x, tinggi=tinggi, jenis=jenis, baju=baju)


def komp_kecil(x, jenis, tinggi=None):
    tinggi = tinggi or (140 if jenis in ('pria', 'wanita') else 95)
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    return meja(x + 52, 150, 70) + komputer(x + 52, 150, 54) + orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan={'ka': [(18, 24), (36, 28)]})


def tv_kecil(x, jenis, tinggi=None):
    tinggi = tinggi or (140 if jenis in ('pria', 'wanita') else 95)
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    return tv(x + 55, 160, 54) + meja(x + 55, 160, 54) + orang(x, tinggi=tinggi, jenis=jenis, baju=baju)


def mengobrol(x1, j1, x2, j2, t=100):
    return (orang(x1, tinggi=t, jenis=j1, baju='a' if j1 in ('wanita', 'gadis') else 'h', wajah='puas') + orang(x2, tinggi=t, jenis=j2, baju='h' if j2 in ('pria', 'laki') else 'p', wajah='puas')
            + titik_obrolan((x1 + x2) / 2, 200 - t - 30, 54, 34))


A['B04-L4a'] = lantai() + di_komputer(80, 'pria')
A['B04-L4b'] = lantai() + nonton_tv(80, 'pria')
A['B04-L4c'] = lantai() + di_komputer(80, 'wanita')
A['B04-L5a'] = lantai() + orang(150, tinggi=105, jenis='gadis', baju='a', tangan={'ki': [(18, 24), (36, 4)], 'ka': [(18, 24), (36, 4)]}) + kotak(124, 108, 52, 30, 'p', 2) + garis((150, 108), (150, 138))
A['B04-L5b'] = lantai() + mengobrol(100, 'gadis', 200, 'gadis')
A['B04-L5c'] = lantai() + di_komputer(80, 'gadis')
A['B04-L6a'] = lantai() + di_komputer(80, 'wanita')
A['B04-L6b'] = lantai() + orang_ponsel(150, 'wanita', 150, baju='a')
A['B04-L6c'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(18, 24), (36, 4)], 'ka': [(18, 24), (36, 4)]}) + kotak(124, 86, 52, 34, 'p', 2) + garis((150, 86), (150, 120))
A['B04-L8a'] = lantai() + komp_kecil(30, 'wanita') + tv_kecil(175, 'laki')
A['B04-L8b'] = lantai() + tv_kecil(30, 'wanita') + komp_kecil(175, 'laki')
A['B04-L8c'] = lantai() + tv(150, 150, 90) + meja(150, 150, 90) + orang(60, tinggi=145, jenis='wanita', baju='a') + orang(250, tinggi=95, jenis='laki', baju='h')
A['B04-L9'] = ponsel(150, 110, 2.6) + kotak(110, 30, 70, 32, 'p', 4) + kotak(180, 38, 8, 16, 'h') + kotak(114, 34, 12, 24, 'h') + teks(218, 54, '!', 30, angka=True)
A['B04-L10'] = lantai() + di_komputer(80, 'pria')
A['B04-T3a'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(18, 24), (36, 4)], 'ka': [(18, 24), (36, 4)]}) + kotak(124, 86, 52, 34, 'p', 2) + garis((150, 86), (150, 120))
A['B04-T3b'] = lantai() + nonton_tv(80, 'wanita')
A['B04-T3c'] = lantai() + di_komputer(80, 'wanita')
A['B04-T4a'] = (lantai_kamar() + ranjang(150, 200, 190) + kotak(110, 134, 104, 16, 'a', 7) + bulat(98, 132, 12) + muka(98, 132, 12, 'tidur') + teks(122, 110, 'Z', 20, angka=True))
A['B04-T4b'] = lantai() + meja_kantor(180) + orang(100, tinggi=155, jenis='pria', baju='h') + tas_kerja(130, 196)
A['B04-T4c'] = lantai() + mengobrol(100, 'wanita', 200, 'pria', 150)
A['B04-T6a'] = lantai() + tv(150, 150, 90) + meja(150, 150, 90) + orang(60, tinggi=150, jenis='wanita', baju='a', rambut='uban') + orang(250, tinggi=165, jenis='pria', baju='h')
A['B04-T6b'] = lantai() + tv_kecil(30, 'wanita') + komp_kecil(175, 'pria')
A['B04-T6c'] = lantai() + komp_kecil(30, 'wanita') + tv_kecil(175, 'pria')
A['B04-T7'] = lantai() + meja(150, 150, 200) + komputer(150, 150, 170) + teks(150, 76, 'www', 22, angka=True, warna='#fff') + kotak(100, 84, 100, 8, 'p') + kotak(100, 98, 70, 8, 'p')
A['B04-T8'] = lantai() + orang(120, tinggi=155, jenis='wanita', baju='a', tangan={'ka': [(14, -30), (6, -58)]}) + jam_dinding(230, 80, 34, 3, 5)

# B05 — tamu
A['B05-1'] = (lantai() + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 16), (46, 10)]}) + cangkir(172, 100, .6) + meja(230, 150, 90)
              + orang(250, tinggi=110, jenis='wanita', duduk=150, baju='h'))
A['B05-2'] = (lantai() + meja(150, 150, 220) + kue_ultah(150, 150, '', .75) + ''.join(garis((110 + i * 20, 112), (110 + i * 20, 96), lebar=4) for i in range(5))
              + orang(60, tinggi=140, jenis='wanita', baju='a', tangan=LAMBAI) + orang(245, tinggi=145, jenis='pria', baju='h', tangan={'ki': [(14, -30), (6, -58)]})
              + ''.join(bentuk((96 + i * 28, 40), (108 + i * 28, 40), (102 + i * 28, 30), k='h') for i in range(4)))
A['B05-4'] = lantai() + sofa(110) + kotak(200, 40, 80, 110, 'p', 6) + roti(240, 110, .45) + larangan(240, 96, 32)
A['B05-5'] = (lantai() + kardus(80, 124, 64, 40) + kardus(80, 162, 70, 40) + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='sedih', tangan={'ki': [(10, 20), (4, 60)], 'ka': [(10, 20), (4, 60)]})
              + kardus(80, 124, 64, 40) + orang(215, tinggi=165, jenis='pria', baju='h'))

# --- B05 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def ruang_tamu(*isi):
    return lantai_kamar() + sofa(120) + meja(230, 160, 60) + cangkir(230, 160, .5) + ''.join(isi)


def ruang_makan(*isi):
    return lantai_kamar() + meja(150, 140, 180) + mangkuk_mi(110, 120, .35, sumpit=False) + mangkuk_mi(190, 120, .35, sumpit=False) + kursi(60, s=.7) + kursi(240, arah=-1, s=.7) + ''.join(isi)


def dapur(*isi):
    return lantai_kamar() + kotak(40, 120, 220, 80, 'p') + kotak(60, 108, 50, 12, 'h') + bulat(85, 104, 4, 'h') + kotak(180, 60, 60, 60, 'p') + ''.join(isi)


def tuan_rumah(x=70, arah=1, **kw):
    return orang(x, tinggi=150, jenis='wanita', baju='a', rambut='uban', tangan={'ka' if arah == 1 else 'ki': [(20, 6), (46, -6)]}, **kw)


bunga_ikat = lambda x, y, s=1.0: bunga(x - 8 * s, y, .6 * s) + bunga(x + 8 * s, y - 4 * s, .6 * s) + bunga(x, y - 12 * s, .6 * s)
A['B05-3'] = (lantai() + pintu(250, t=150, lebar=60) + orang(90, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (44, 0)]}) + bunga_ikat(150, 100)
               + orang(200, tinggi=150, jenis='wanita', baju='p', wajah='puas', tangan={'ki': [(20, 10), (40, 4)]}))
A['B05-L4a'] = lantai() + teko(110, 200, 1.2) + cangkir(220, 196, 1.0) + elips(220, 158, 20, 4, 'a')
A['B05-L4b'] = lantai() + cangkir(150, 196, 1.4) + elips(150, 144, 28, 5, 'h')
A['B05-L4c'] = lantai() + gelas(150, 200, 'air', 2.0)
A['B05-L5a'] = ruang_makan()
A['B05-L5b'] = ruang_tamu()
A['B05-L5c'] = dapur()
A['B05-L6a'] = ruang_tamu()
A['B05-L6b'] = ruang_makan()
A['B05-L6c'] = lantai() + pintu(150, t=160, lebar=80) + kotak(100, 196, 100, 6, 'a')
A['B05-L8a'] = ruang_tamu(tuan_rumah(60, wajah='puas'))
A['B05-L8b'] = ruang_makan() + tuan_rumah(40, wajah='puas')
A['B05-L8c'] = lantai() + pintu(120, t=160, lebar=70) + tuan_rumah(60, tangan_lambai=None) if False else lantai() + pintu(200, t=160, lebar=70) + orang(80, tinggi=150, jenis='wanita', baju='a', rambut='uban', tangan=LAMBAI) + orang(250, tinggi=155, jenis='pria', baju='h', tangan={'ki': [(14, -30), (6, -58)]})
A['B05-L9'] = lantai() + meja(150, 150, 220) + kue_ultah(110, 150, '', .8) + kotak(190, 106, 50, 44, 'p', 2) + garis((215, 106), (215, 150)) + garis((190, 128), (240, 128)) + jalur('M215 106 q-12 -14 -18 0 M215 106 q12 -14 18 0', 'g')
A['B05-L10'] = ruang_makan() + orang(40, tinggi=150, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(20, 6), (46, -6)]})
A['B05-T3a'] = lantai() + orang(90, tinggi=155, jenis='pria', baju='h', tangan={'ka': [(20, 10), (44, 0)]}) + kotak(140, 92, 36, 30, 'p', 2) + garis((158, 92), (158, 122)) + orang(220, tinggi=150, jenis='wanita', baju='a', wajah='puas')
A['B05-T3b'] = lantai() + meja(160, 140, 140) + mangkuk_mi(160, 118, .4) + orang(70, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(16, 18), (30, 6)]})
A['B05-T3c'] = lantai() + orang_ponsel(150, 'pria', 155, baju='h')
A['B05-T4a'] = lantai() + cangkir(150, 196, 1.4) + elips(150, 144, 28, 5, 'h')
A['B05-T4b'] = lantai() + teko(110, 200, 1.2) + cangkir(220, 196, 1.0) + elips(220, 158, 20, 4, 'a')
A['B05-T4c'] = lantai() + botol(120, 200, 1.4) + gelas(200, 200, 'susu', 1.2)
A['B05-T6a'] = ruang_makan()
A['B05-T6b'] = ruang_tamu()
A['B05-T6c'] = lantai_kamar() + ranjang(150, 200, 190)
A['B05-T7'] = lantai() + pintu(80, t=160, lebar=70) + sepatu(190, 160, 1.6) + silang(205, 140, 44, 9)
A['B05-T8'] = lantai() + orang(100, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(14, 20), (2, 0)], 'ka': [(14, 20), (-2, 0)]}) + orang(210, tinggi=155, jenis='pria', baju='h') + ponsel(240, 110, .8)

# B06 — kenalan
A['B06-1'] = (lantai() + orang(60, tinggi=150, jenis='nenek', baju='a', rambut='uban', tangan={'ka': [(6, 30), (14, 60)]}) + garis((80, 110), (84, 200), lebar=4)
              + orang(150, tinggi=165, jenis='pria', baju='h') + orang(240, tinggi=90, jenis='gadis') + panah(150, 8, 150, 26, 5))
A['B06-2'] = lantai() + orang(100, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 16), (44, 20)]}) + orang(200, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(20, 16), (44, 20)]})
A['B06-3'] = lantai() + pohon(260, s=.8) + orang(50, tinggi=90, jenis='laki', baju='h', tangan=LAMBAI) + orang(110, tinggi=85, jenis='gadis', baju='a') + bola(150, 188, 12) + orang(190, tinggi=90, jenis='laki', baju='a', kaki_pose={'ki': (-10, 0), 'ka': (20, -12)})
A['B06-4'] = kalender_senin(150, 30, 2, 3) + lantai() + orang(100, tinggi=90, jenis='wanita', baju='a', tangan={'ka': [(14, 10), (30, 12)]}) + orang(200, tinggi=95, jenis='pria', baju='h', tangan={'ki': [(14, 10), (30, 12)]})
A['B06-5'] = lantai() + orang(150, tinggi=160, jenis='nenek', rambut='uban', baju='a', wajah='puas', rok=False)

# --- B06 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def paspor2(x, y, negara, w=64, h=86):
    """Buku paspor generik bertuliskan nama negara (bukan tiruan sampul asli)."""
    uk = 13 if len(negara) <= 6 else 10
    return (kotak(x - w / 2, y, w, h, 'h', 4) + teks(x, y + 24, 'PASSPORT', 9, angka=True, warna='#fff')
            + bulat(x, y + 46, 11, 'w') + teks(x, y + h - 10, negara, uk, angka=True, warna='#fff'))


def tongkat(x, tinggi=145):
    return garis((x + 26, 200 - tinggi * .45), (x + 30, 200), lebar=4) + jalur(f'M{x + 26} {200 - tinggi * .45} q-2 -10 -10 -8', 'g', 4)


def org_paspor(x, negara, jenis='pria', tinggi=160, **kw):
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan={'ka': [(20, 20), (42, 14)]}, **kw) + paspor2(x + 66, 200 - tinggi + 44, negara)


A['B06-L4a'] = lantai() + org_paspor(100, 'JAPAN', 'pria', 150, rambut='uban', wajah='senyum') + tongkat(70, 150)
A['B06-L4b'] = lantai() + org_paspor(100, 'JAPAN', 'pria', 160)
A['B06-L4c'] = lantai() + org_paspor(100, 'KOREA', 'pria', 160)
A['B06-L5a'] = lantai() + orang(50, tinggi=155, jenis='pria', baju='h') + orang(110, tinggi=150, jenis='wanita', baju='a') + orang(180, tinggi=90, jenis='laki', baju='h') + orang(240, tinggi=88, jenis='gadis', baju='a')
A['B06-L5b'] = lantai() + orang(70, tinggi=90, jenis='laki', baju='h') + orang(150, tinggi=88, jenis='gadis', baju='a') + orang(230, tinggi=92, jenis='laki', baju='a')
A['B06-L5c'] = lantai() + orang(70, tinggi=160, jenis='pria', baju='h') + orang(150, tinggi=150, jenis='wanita', baju='a') + orang(230, tinggi=158, jenis='pria', baju='a')
A['B06-L6a'] = paspor2(150, 40, 'TAIWAN', 110, 150)
A['B06-L6b'] = paspor2(150, 40, 'JAPAN', 110, 150)
A['B06-L6c'] = paspor2(150, 40, 'INDONESIA', 110, 150)
A['B06-L8a'] = lantai() + orang(100, tinggi=160, jenis='pria', baju='h', wajah='puas') + orang(200, tinggi=145, jenis='pria', baju='a', rambut='uban', wajah='puas') + tongkat(200) + titik_obrolan(150, 30, 54, 34)
A['B06-L8b'] = lantai() + orang(100, tinggi=160, jenis='pria', baju='h', wajah='puas') + orang(200, tinggi=158, jenis='pria', baju='a', wajah='puas') + titik_obrolan(150, 30, 54, 34)
A['B06-L8c'] = lantai() + orang(110, tinggi=145, jenis='pria', baju='a', rambut='uban', wajah='puas') + tongkat(110) + orang(200, tinggi=90, jenis='laki', baju='h', wajah='puas') + titik_obrolan(155, 50, 54, 34)
A['B06-L9'] = (lantai() + garis((20, 30), (280, 30), k='t') + ''.join(kotak(30 + i * 45, 30, 26, 20, 'a' if i % 2 else 'p') for i in range(6))
               + orang(50, tinggi=140, jenis='wanita', baju='a', rambut='uban', wajah='puas') + orang(115, tinggi=155, jenis='pria', baju='h', wajah='puas')
               + orang(180, tinggi=150, jenis='wanita', baju='p', wajah='puas') + orang(240, tinggi=90, jenis='gadis', baju='a', wajah='puas'))
A['B06-L10'] = lantai() + org_paspor(60, 'INDONESIA', 'pria', 150) + orang(220, tinggi=155, jenis='pria', baju='a', tangan={'ki': [(20, 20), (40, 24)]})
A['B06-T3a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='p') + jalur('M140 66 Q136 96 150 100 Q164 96 160 66', 'g', 2.5) + palang(166, 84, .35)
A['B06-T3b'] = lantai() + orang(150, tinggi=150, jenis='pria', baju='h') + tas_punggung(122, 76, .8) + buku(180, 150, 22, 30)
A['B06-T3c'] = lantai() + papan_tulis(220, 40, 110, 60) + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, -10), (44, -30)]})
A['B06-T4a'] = paspor2(150, 40, 'JAPAN', 110, 150)
A['B06-T4b'] = paspor2(150, 40, 'USA', 110, 150)
A['B06-T4c'] = paspor2(150, 40, 'INDONESIA', 110, 150)
A['B06-T6a'] = lantai() + pohon(40) + orang(110, tinggi=90, jenis='laki', baju='h') + orang(180, tinggi=88, jenis='gadis', baju='a') + pohon(260)
A['B06-T6b'] = lantai() + meja_kantor(200) + orang(80, tinggi=160, jenis='pria', baju='h') + orang(130, tinggi=150, jenis='wanita', baju='a')
A['B06-T6c'] = lantai() + pohon(30) + orang(90, tinggi=160, jenis='pria', baju='h') + orang(150, tinggi=150, jenis='wanita', baju='a') + orang(210, tinggi=90, jenis='laki', baju='h') + pohon(270, s=.9)
A['B06-T7'] = A['B06-2']
A['B06-T8'] = lantai() + orang(150, tinggi=150, jenis='pria', baju='a', rambut='uban', wajah='senyum') + tongkat(150, 150)

# B07 — rumah baru
A['B07-1'] = lantai() + meja(160, 130, 160) + buku(140, 130, 40, 30, 'h') + buku(175, 200, 40, 26, 'a') + tunjuk_ke(55, 'pria', 160, 1, 'a')
A['B07-2'] = lantai() + kardus(80, 200, 90, 60) + kardus(80, 140, 76, 50) + kardus(180, 200, 90, 70) + kardus(250, 200, 50, 40, 'p')
A['B07-3'] = (lantai() + gedung(95, tingkat=6, lebar=110) + gedung(215, tingkat=5, lebar=90) + kotak(40, 42, 110, 22, 'h') + buku(95, 60, 20, 14, 'p')
              + orang(160, tinggi=120, jenis='laki', baju='a'))
A['B07-4'] = (lantai_kamar() + ranjang(60, 200, 90) + ranjang(240, 200, 90) + orang(125, tinggi=150, jenis='pria', baju='a')
              + orang(180, tinggi=155, jenis='pria', baju='h', kacamata=True))
A['B07-5'] = lantai() + rumah(150, 200, 230, 110) + orang(275, tinggi=60, jenis='pria', baju='a')

# --- B07 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def lantai_ke(n, orang_=False):
    tk = min(max(n + 1, 6), 20)
    tt = min(24, 180 / tk)
    y = 200 - n * tt + tt / 2
    o = lantai() + gedung(120, tingkat=tk, sorot=n, tt=tt) + panah(222, y, 172, y, 4) + teks(254, y + 9, f'{n}F', 24, angka=True)
    if orang_:
        o += orang(50, tinggi=110, jenis='pria', baju='a', rambut='uban')
    return o


kunci = lambda x, y: bulat(x, y, 7, 'p') + garis((x + 7, y), (x + 26, y), lebar=3) + garis((x + 20, y), (x + 20, y + 6), lebar=3)
A['B07-L4a'] = lantai_ke(7)
A['B07-L4b'] = lantai_ke(17)
A['B07-L4c'] = lantai_ke(1)
A['B07-L5a'] = lantai() + orang(150, tinggi=150, jenis='pria', baju='a', rambut='uban', tangan={'ka': [(20, 10), (40, 0)]}) + kunci(194, 98)
A['B07-L5b'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h') + tas_punggung(122, 72, .8) + buku_tumpuk(220, 196, 2, 50, 16)
A['B07-L5c'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(14, 20), (2, 4)]})
A['B07-L6a'] = lantai() + gedung(150, tingkat=4, lebar=170, tt=30) + kotak(110, 54, 80, 18, 'h') + teks(150, 68, '宿舍', 14, warna='#fff')
A['B07-L6b'] = lantai() + rumah(150, lebar=170, t=110)
A['B07-L6c'] = lantai() + gedung(110, tingkat=7, lebar=100) + pohon(220) + pohon(268, s=.8) + bangku(244, lebar=50)
A['B07-L8a'] = lantai_ke(7)
A['B07-L8b'] = lantai() + gedung(150, tingkat=7, sorot=1, lebar=110) + panah(252, 188, 210, 188, 4) + teks(274, 196, '1F', 20, angka=True) + orang(60, tinggi=110, jenis='pria', baju='a', rambut='uban')
A['B07-L8c'] = lantai() + rumah(150, lebar=170, t=110)
A['B07-L9'] = lantai() + pintu(150, t=170, lebar=110) + kotak(110, 60, 80, 56, 'p', 3) + teks(150, 80, '房租', 16) + teks(150, 106, '$8,000/月', 14, angka=True)
A['B07-L10'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 6), (44, -4)]}) + buku(160, 112, 30, 40) + orang(225, tinggi=158, jenis='pria', baju='a', wajah='puas')
A['B07-T3a'] = (jalur('M10 150 q20 -10 40 0 q20 10 40 0 q20 -10 40 0 q20 10 40 0 q20 -10 40 0 q20 10 40 0 q20 -10 40 0', 'g') + matahari(250, 40, 18)
                + gedung(90, tingkat=4, lebar=80, lantai_y=140))
A['B07-T3b'] = lantai() + gedung(70, tingkat=5, lebar=90) + sekolah(210, w=130, h=90)
A['B07-T3c'] = lantai() + gedung(50, tingkat=7, lebar=70) + gedung(130, tingkat=5, lebar=70) + gedung(210, tingkat=8, lebar=70, tt=22) + mobil(150, w=120)
A['B07-T4a'] = label_harga(150, 80, '10,000', 220, 76)
A['B07-T4b'] = label_harga(150, 80, '1,000', 220, 76)
A['B07-T4c'] = label_harga(150, 80, '4,000', 220, 76)
A['B07-T6a'] = lantai() + rumah(150, lebar=170, t=110)
A['B07-T6b'] = lantai() + gedung(170, tingkat=6, lebar=150) + kotak(102, 150, 30, 50, 'h') + panah(117, 120, 117, 146, 4)
A['B07-T6c'] = lantai() + gedung(130, tingkat=6, lebar=150) + kotak(168, 150, 30, 50, 'h') + panah(183, 120, 183, 146, 4)
A['B07-T7'] = lantai() + orang(80, tinggi=155, jenis='pria', baju='h', tangan={'ki': [(20, 6), (36, -4)], 'ka': [(20, 6), (36, -4)]}) + kardus(150, 120, 70, 56) + orang(220, tinggi=155, jenis='pria', baju='a', tangan={'ki': [(20, 6), (36, -4)], 'ka': [(20, 6), (36, -4)]})
A['B07-T8'] = lantai() + orang(110, tinggi=150, jenis='pria', baju='a', rambut='uban', tangan={'ka': [(20, 10), (40, 0)]}) + kunci(154, 98) + kunci(160, 112) + gedung(240, tingkat=5, lebar=70)

# B08 — ruangan
A['B08-1'] = kotak(20, 20, 260, 180, 'p') + jendela_buka(150, 60, 110, 90)
A['B08-2'] = kotak(20, 16, 260, 188, 'p') + lampu(150, 70, True) + meja(150, 160, 150, 40)
_r, _ya = penampang_rumah()
A['B08-3'] = lantai() + _r + kloset(90, 200, 1.1) + kotak(54, 118, 70, 12, 'p', 3) + panah(165, 150, 118, 170, 5)
A['B08-4'] = kotak(20, 16, 260, 188, 'p') + ac(150, 40, True)
A['B08-5'] = lantai() + _r + lemari_buku(90, _ya - 4, 70, 56) + meja(150, _ya - 30, 50, 26) + panah(190, 36, 132, 70, 5)

# --- B08 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def rumah2(atas=(), bawah=()):
    """Rumah 2 lantai tampak potong; atas/bawah: daftar isi ('baca', 'toilet', 'org_wanita', ...) dengan posisi kiri→kanan."""
    o, ya = penampang_rumah(150)
    def isi(jenis, x, alas):
        return {'baca': lemari_buku(x, alas - 4, 50, 44) + teks(x, alas - 54, '書', 12),
                'toilet': kloset(x, alas, .8) + kotak(x - 22, alas - 64, 44, 14, 'p', 3),
                'wanita': orang(x, kaki=alas, tinggi=62, jenis='wanita', baju='a'),
                'kosong': ''}[jenis]
    for j, x in atas:
        o += isi(j, x, ya - 4)
    for j, x in bawah:
        o += isi(j, x, LANTAI)
    return lantai() + o


def lift_silang(x=70):
    return kotak(x - 34, 60, 68, 140, 'p') + garis((x, 60), (x, 200)) + silang(x, 120, 26, 7)


def naik_tangga():
    return ''.join(kotak(130 + i * 26, 186 - i * 14, 26, 14 + i * 14, 'p') for i in range(6))


A['B08-L4a'] = rumah2(atas=[('toilet', 70)], bawah=[('baca', 70)])
A['B08-L4b'] = rumah2(atas=[('toilet', 70), ('baca', 160)])
A['B08-L4c'] = rumah2(atas=[('baca', 70), ('toilet', 130)])
A['B08-L5a'] = rumah2(bawah=[('wanita', 90)])
A['B08-L5b'] = rumah2(atas=[('wanita', 90)])
A['B08-L5c'] = rumah2() + orang(225, kaki=150, tinggi=60, jenis='wanita', baju='a')
A['B08-L6a'] = lantai() + kotak(110, 50, 80, 150, 'p') + kotak(114, 54, 34, 142, 'a') + kotak(152, 54, 34, 142, 'a') + garis((150, 54), (150, 196)) + orang(60, tinggi=150, jenis='wanita', baju='a') + orang(240, tinggi=158, jenis='pria', baju='h')
A['B08-L6b'] = lantai() + naik_tangga() + orang(170, kaki=158, tinggi=100, jenis='wanita', baju='a') + orang(222, kaki=130, tinggi=104, jenis='pria', baju='h')
A['B08-L6c'] = lantai() + mobil(150, w=190, taksi=True)
A['B08-L8a'] = rumah2(atas=[('baca', 70)], bawah=[('toilet', 70)])
A['B08-L8b'] = rumah2(atas=[('toilet', 70)], bawah=[('baca', 70)])
A['B08-L8c'] = rumah2(atas=[('baca', 70), ('toilet', 140)])
A['B08-L9'] = lantai() + lift_silang(60) + naik_tangga() + orang(170, kaki=158, tinggi=100, jenis='wanita', baju='a') + orang(222, kaki=130, tinggi=104, jenis='pria', baju='h')
A['B08-L10'] = kotak(20, 16, 260, 188, 'p') + lemari_buku(60, 200, 60, 120) + meja(185, 140, 150) + orang(150, tinggi=110, jenis='wanita', baju='a', duduk=160) + orang(220, tinggi=115, jenis='pria', baju='h', duduk=160) + buku(170, 140, 20, 24) + buku(200, 140, 20, 24)
A['B08-T3a'] = rumah2(atas=[('toilet', 70)])
A['B08-T3b'] = lantai() + kotak(40, 50, 70, 150, 'p') + garis((75, 50), (75, 200)) + teks(75, 44, '▲▼', 14) + panah(150, 125, 120, 125, 4) + kloset(220, 200, 1.0) + kotak(190, 120, 60, 14, 'p', 3)
A['B08-T3c'] = lantai() + naik_tangga() + kloset(70, 200, 1.0) + kotak(40, 120, 60, 14, 'p', 3)
A['B08-T4a'] = lantai() + kotak(110, 50, 80, 150, 'p') + kotak(114, 54, 34, 142, 'a') + kotak(152, 54, 34, 142, 'a') + garis((150, 54), (150, 196))
A['B08-T4b'] = lantai() + naik_tangga().replace('', '')
A['B08-T4c'] = kotak(10, 120, 280, 90, 'a') + jalur('M10 120 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0', 'g') + garis((230, 120), (230, 40)) + garis((260, 120), (260, 40)) + garis((230, 70), (260, 70)) + garis((230, 95), (260, 95))
A['B08-T6a'] = kotak(20, 16, 260, 188, 'p') + lampu(150, 70, True) + pintu(240, 200, 120, 50)
A['B08-T6b'] = kotak(20, 16, 260, 188, 'p') + lampu(150, 70, True) + pintu(240, 200, 120, 50, buka=True) + jalur('M215 80 L265 70 L265 200 L215 200', 'p')
A['B08-T6c'] = kotak(20, 16, 260, 188, 'p') + lampu(150, 70, False) + jalur('M215 80 L265 70 L265 200 L215 200', 'p')
A['B08-T7'] = lantai() + rumah(80) + garis((150, 196), (150, 200)) + kotak(146, 120, 8, 80, 'a') + sekolah(225, w=120, h=90)
A['B08-T8'] = kotak(20, 16, 260, 188, 'p') + lampu(150, 70, True)

# B09 — bantu-bantu
A['B09-1'] = kotak(20, 16, 260, 188, 'p') + ac(150, 70, rusak=True)
A['B09-2'] = lantai() + meja(170, 150, 160) + baskom_cuci(170, 150) + orang(90, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(24, 26), (60, 36)]})
A['B09-3'] = kotak(20, 16, 260, 188, 'p') + lampu(200, 70, True) + orang(90, kaki=200, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -20), (52, -48)]})
A['B09-4'] = lantai() + meja(150, 150, 170) + tv_retak(150, 150, 150)
A['B09-5'] = (kotak(20, 16, 260, 188, 'p') + kotak(175, 50, 70, 150, 'h') + bentuk((245, 50), (272, 38), (272, 204), (245, 200), k='p')
              + bulat(264, 124, 3, 'h') + tunjuk_ke(90, 'pria', 160, 1, 'h'))   # pintu terbuka

# --- B09 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def cuci_piring(x, jenis, tinggi=None):
    tinggi = tinggi or (150 if jenis in ('pria', 'wanita') else 100)
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    by = 200 - tinggi * .45
    sx = x + 58
    return (kotak(sx - 34, by, 68, 200 - by, 'p') + kotak(sx - 30, by - 6, 60, 10, 'a', 3)
            + ''.join(elips(sx + 4, by - 10 - i * 6, 22, 5, 'p') for i in range(4)) + bulat(sx - 22, by - 30, 4, 't') + bulat(sx - 14, by - 40, 3, 't')
            + orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan={'ka': [(18, 22), (40, 26)]}))


def cuci_baju(x, jenis, tinggi=None):
    tinggi = tinggi or (150 if jenis in ('pria', 'wanita') else 100)
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    by = 200 - tinggi * .45
    return baskom_cuci(x + 55, by + 40) + kaos(x + 55, by - 6, .35, 'a') + orang(x, tinggi=tinggi, jenis=jenis, baju=baju, tangan={'ka': [(18, 22), (40, 26)]})


def jemur(x, jenis='wanita'):
    return garis((150, 50), (290, 50), lebar=3) + kaos(190, 80, .5, 'p') + kaos(250, 80, .5, 'a') + orang(x, tinggi=150, jenis=jenis, baju='a' if jenis == 'wanita' else 'h', tangan={'ka': [(20, -10), (40, -40)]})


def ac_rusak(x=150, y=40):
    return ac(x, y, False, True)


A['B09-L4a'] = lantai() + cuci_piring(90, 'wanita')
A['B09-L4b'] = lantai() + jemur(110, 'wanita')
A['B09-L4c'] = lantai() + cuci_baju(90, 'wanita')
A['B09-L5a'] = kotak(20, 16, 260, 188, 'p') + ac(150, 40, True)
A['B09-L5b'] = lantai() + tv_retak(150, 160) + meja(150, 160, 140)
A['B09-L5c'] = kotak(20, 16, 260, 188, 'p') + ac(150, 40, False, True)
A['B09-L6a'] = lantai() + cuci_baju(90, 'wanita')
A['B09-L6b'] = lantai() + cuci_piring(90, 'wanita')
A['B09-L6c'] = kotak(20, 16, 260, 188, 'p') + kotak(150, 50, 70, 50, 'p', 2) + kotak(158, 58, 54, 34, 'a') + orang(100, kaki=200, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(20, -10), (46, -34)]})
A['B09-L8a'] = lantai() + cuci_piring(40, 'gadis', 110) + cuci_baju(180, 'laki', 95)
A['B09-L8b'] = lantai() + cuci_baju(40, 'gadis', 110) + cuci_piring(180, 'laki', 95)
A['B09-L8c'] = lantai() + cuci_piring(40, 'gadis', 110) + cuci_piring(180, 'laki', 95)
A['B09-L9'] = A['B09-L6c']
A['B09-L10'] = lantai() + cuci_baju(60, 'pria') + orang(230, tinggi=150, jenis='wanita', baju='a', wajah='puas', tangan={'ki': [(14, -30), (6, -58)]})
A['B09-T3a'] = lantai() + cuci_piring(90, 'wanita')
A['B09-T3b'] = lantai() + cuci_baju(90, 'wanita')
A['B09-T3c'] = lantai() + orang(110, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(16, 30), (30, 60)]}) + garis((140, 90), (190, 196), lebar=4) + jalur('M175 190 L210 200 L170 200 Z', 'h')
A['B09-T4a'] = kotak(20, 16, 260, 188, 'p') + ranjang(100, 200, 140) + orang(220, tinggi=150, jenis='pria', baju='h', wajah='puas') + bintang(60, 60, 8) + bintang(160, 50, 8)
A['B09-T4b'] = lantai() + meja(170, 140, 140) + mangkuk_mi(170, 110, .4, sumpit=False) + orang(80, tinggi=155, jenis='pria', baju='h', tangan={'ka': [(16, 18), (40, 10)]})
A['B09-T4c'] = lantai() + cuci_baju(90, 'pria')
A['B09-T6a'] = lantai() + pintu(110, t=160, lebar=70, buka=True) + jalur('M75 40 L125 30 L125 200 L75 200', 'p') + jendela(230, 60, 70, 60)
A['B09-T6b'] = lantai() + pintu(110, t=160, lebar=70) + jendela(230, 60, 70, 60)
A['B09-T6c'] = lantai() + pintu(110, t=160, lebar=70) + jendela_buka(230, 60, 80, 60)
A['B09-T7'] = garis((40, 50), (260, 50), lebar=3) + kaos(100, 110, .8, 'p') + kaos(200, 110, .8, 'p') + bintang(150, 160, 8) + bintang(60, 170, 6) + bintang(250, 170, 6)
A['B09-T8'] = lantai() + orang(90, tinggi=150, jenis='wanita', baju='a', wajah='puas', tangan={'ki': [(14, 20), (2, 4)], 'ka': [(14, 20), (-2, 4)]}) + orang(210, tinggi=155, jenis='pria', baju='h', wajah='puas')

# B10 — kebiasaan
A['B10-1'] = kotak(20, 16, 150, 188, 'p') + pancuran(95, 80) + orang(95, tinggi=110, jenis='pria', baju='p', wajah='puas') + jam_sektor(228, 100, 56, 20)
A['B10-2'] = kotak(20, 16, 150, 188, 'p') + pancuran(95, 80) + orang(95, tinggi=110, jenis='wanita', baju='p', wajah='puas') + jam_sektor(228, 100, 56, 15)
A['B10-3'] = lantai() + kalender_minggu(150, 12, 0, 0, 260).replace('>今天<', '>週日<') + sofa(150, 200, 170) + orang(150, tinggi=150, jenis='pria', duduk=160, baju='a', wajah='puas')
A['B10-4'] = kotak(20, 16, 260, 188, 'p') + jendela(230, 30, 70, 56) + bulan_bintang(225, 58, .45) + pancuran(110, 90) + orang(110, tinggi=120, jenis='wanita', baju='p', wajah='puas')
A['B10-5'] = lantai_kamar() + jendela(215, 36, 60, 46) + matahari(215, 58, 9) + ranjang(110, 200, 170) + bulat(56, 136, 13) + muka(56, 136, 13, 'tidur') + jalur('M42 131 q2 -18 16 -18 q12 0 13 14', 'h') + teks(92, 110, 'z z', 18, angka=True)

# --- B10 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def jam_penuh(x, y, r, menit):
    if menit < 60:
        return jam_sektor(x, y, r, menit)
    return jam_sektor(x, y, r, 1).replace('class="a"', 'class="p"') + bulat(x, y, r * .88, 'a') + ''.join(
        garis((x + math.sin(math.radians(i * 30)) * r * .74, y - math.cos(math.radians(i * 30)) * r * .74),
              (x + math.sin(math.radians(i * 30)) * r * .88, y - math.cos(math.radians(i * 30)) * r * .88), lebar=4 if i % 3 == 0 else 2.2) for i in range(12)) + garis((x, y), (x, y - r * .8), lebar=r * .06)


def sekolah_b(x, w=140):
    return (kotak(x - w / 2, 90, w, 110, 'p') + bentuk((x - w / 2 - 10, 90), (x, 52), (x + w / 2 + 10, 90), k='h')
            + garis((x, 52), (x, 14)) + bentuk((x, 14), (x + 30, 22), (x, 30), k='a') + jendela(x - w / 2 + 28, 110, 30, 26) + jendela(x + w / 2 - 28, 110, 30, 26)
            + pintu(x, 200, 60, 36) + lonceng(x, 98, .18))


def durasi(menit, apa=None):
    o = jam_penuh(110 if apa else 150, 105, 80, menit)
    if menit >= 60:
        o += teks(110 if apa else 150, 205, f'{menit // 60}h', 18, angka=True) if menit > 60 else ''
    if apa == 'renang':
        o += kotak(200, 150, 90, 50, 'a') + bulat(240, 140, 11) + muka(240, 140, 11, 'senyum') + jalur('M228 140 Q228 126 240 128 Q252 126 252 140', 'h') + garis((254, 150), (276, 124), (290, 140), lebar=4)
    elif apa == 'lari':
        o += pelari(250, 'pria', 'h', 120).replace('', '')
    return o


def mandi(waktu, jenis='wanita'):
    o = lantai() + pancuran(150, 30) + orang(150, tinggi=140, jenis=jenis, baju='p', wajah='puas')
    return o + (matahari(250, 45, 18) if waktu == 'pagi' else bulan_bintang(250, 45, .7))


A['B10-L4a'] = durasi(15)
A['B10-L4b'] = durasi(60)
A['B10-L4c'] = durasi(30)
A['B10-L5a'] = mandi('pagi')
A['B10-L5b'] = mandi('malam')
A['B10-L5c'] = lantai() + matahari(250, 45, 18) + pelari(140, 'wanita', 'a', 150)
A['B10-L6a'] = lantai() + papan_tulis(210, 40, 120, 60) + orang(90, tinggi=150, jenis='wanita', baju='a') + tas_punggung(66, 70, .8)
A['B10-L6b'] = lantai() + sofa(150) + orang(150, tinggi=140, jenis='wanita', baju='a', duduk=150, wajah='puas')
A['B10-L6c'] = olahraga('renang', 120, jenis='wanita')
A['B10-L8a'] = durasi(45, 'renang')
A['B10-L8b'] = durasi(15, 'renang')
A['B10-L8c'] = durasi(45, 'lari')
A['B10-L9'] = (orang(40, kaki=150, tinggi=90, jenis='pria', baju='h', tangan={'ki': [(10, -14), (14, -30)], 'ka': [(10, -14), (14, -30)]}) + panah(70, 100, 95, 100, 3)
               + pancuran(130, 30) + orang(130, kaki=150, tinggi=90, jenis='pria', baju='p') + panah(160, 100, 185, 100, 3)
               + meja(245, 120, 80, 30) + roti(235, 112, .6) + gelas(262, 120, 'susu', .5) + garis((10, 150), (290, 150)))
A['B10-L10'] = lantai() + orang(80, tinggi=100, jenis='laki', baju='h', duduk=170) + tv(200, 150, 90) + meja(200, 150, 90) + jam_penuh(260, 40, 30, 60)
A['B10-T3a'] = jam_dinding(110, 105, 70, 4, 0) + teks(230, 120, '4h', 40, angka=True)
A['B10-T3b'] = jam_dinding(110, 105, 70, 1, 0) + teks(230, 120, '1h', 40, angka=True)
A['B10-T3c'] = durasi(10)
A['B10-T4a'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(150, tinggi=145, jenis='wanita', baju='a')
A['B10-T4b'] = lantai() + sekolah_b(200) + orang(70, tinggi=145, jenis='wanita', baju='a')
A['B10-T4c'] = lantai() + rumah(200) + sofa(70, w=110) + orang(70, tinggi=130, jenis='wanita', baju='a', duduk=150)
A['B10-T6a'] = lantai() + tv(220, 150, 90) + meja(220, 150, 90) + orang(90, tinggi=150, jenis='pria', baju='h')
A['B10-T6b'] = lantai() + orang_ponsel(150, 'pria', 155, baju='h') + jam_sektor(250, 50, 30, 50)
A['B10-T6c'] = lantai_kamar() + ranjang(150, 200, 190) + kotak(110, 134, 104, 16, 'a', 7) + bulat(98, 132, 12) + muka(98, 132, 12, 'tidur')
A['B10-T7'] = kalender_minggu(150, 70, 6, 6, 280) if False else ''.join(kotak(15 + i * 39, 70, 37, 70, 'p', 3) + teks(33 + i * 39, 92, '一二三四五六日'[i], 16) for i in range(7)) + bulat(267, 120, 16, 'g') + panah(267, 40, 267, 62, 4)
A['B10-T8'] = lantai() + papan_tulis(220, 40, 110, 60) + jam_dinding(220, 140, 26, 9, 0) + orang(90, tinggi=155, jenis='pria', baju='h')

# B11 — kerja
A['B11-1'] = jam_dinding(75, 100, 58, 9, 0) + panah(140, 100, 160, 100, 6) + jam_dinding(225, 100, 58, 5, 0)
A['B11-2'] = lantai() + meja_kantor(150) + orang_duduk_kerja(60, 'pria', 'h') + orang(250, tinggi=160, jenis='wanita', baju='a', tangan={'ki': [(10, 24), (20, 30)]}) + tas_kerja(230, 196, .6)
A['B11-3'] = lantai() + gedung(70, tingkat=5, lebar=90) + jam_dinding(225, 50, 30, 5, 0) + jalan_kaki(200, 'pria', 140, 'h') + tas_kerja(178, 156, .45)
A['B11-4'] = kalender_senin(150, 24, 2, 3) + tas_kerja(150, 190, 1.2)
A['B11-5'] = lantai() + orang(80, tinggi=110, jenis='laki', baju='a') + gelembung_pikiran(195, 70, 150, 110, orang(195, kaki=118, tinggi=90, jenis='pria', baju='p', kacamata=True) + jalur('M187 64 q8 18 16 0', 't') + palang(222, 60, .3), 118, 110)

# --- B11 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def dua_jam(a, b, malam_b=False):
    ja, ma = a
    jb, mb = b
    return (jam_dinding(70, 100, 50, ja, ma) + panah(130, 100, 168, 100, 5) + jam_dinding(230, 100, 50, jb, mb)
            + (bulan_bintang(270, 35, .5) if malam_b else ''))


def kal_bulan(bulan_ini, tgl):
    return kalender_bulan(150, 30, '下個' if not bulan_ini else '這個', tgl, 170, 160)


A['B11-L4a'] = kalender_bulan(150, 30, '這個', 1, 170, 160).replace('這個月', '這個月')
A['B11-L4b'] = kalender_bulan(150, 30, '下個', 1, 170, 160)
A['B11-L4c'] = kalender_bulan(150, 30, '下個', 10, 170, 160)
A['B11-L5a'] = lantai() + gedung(90, tingkat=6, lebar=90) + sekolah_b(225, 110)
A['B11-L5b'] = lantai() + gedung(90, tingkat=6, lebar=90) + pohon(200) + pohon(260, s=.8)
A['B11-L5c'] = lantai() + toko(150)
A['B11-L6a'] = jam_dinding(150, 105, 80, 6, 0)
A['B11-L6b'] = jam_dinding(150, 105, 80, 9, 0)
A['B11-L6c'] = jam_dinding(150, 105, 80, 3, 0)
A['B11-L8a'] = dua_jam((8, 0), (4, 0))
A['B11-L8b'] = dua_jam((8, 0), (5, 0))
A['B11-L8c'] = dua_jam((9, 0), (4, 0))
A['B11-L9'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(20, 10), (40, 0)]}) + tas_belanja(140, 110, .8) + teks(140, 96, '$', 20, angka=True) + mobil(225, w=120)
A['B11-L10'] = lantai() + orang(80, tinggi=100, jenis='gadis', baju='a', wajah='puas') + gelembung_pikiran(200, 70, 130, 100, papan_tulis(215, 40, 60, 36) + orang(180, kaki=118, tinggi=70, jenis='wanita', baju='a'))
A['B11-T3a'] = jam_dinding(150, 105, 80, 9, 0) + matahari(255, 40, 16)
A['B11-T3b'] = jam_dinding(150, 105, 80, 6, 0) + bulan_bintang(255, 40, .6)
A['B11-T3c'] = jam_dinding(150, 105, 80, 5, 0) + matahari(255, 40, 16)
A['B11-T4a'] = lantai_ke(20)
A['B11-T4b'] = lantai_ke(2)
A['B11-T4c'] = lantai_ke(12)
A['B11-T6a'] = dua_jam((9, 0), (6, 0))
A['B11-T6b'] = dua_jam((8, 0), (5, 0))
A['B11-T6c'] = dua_jam((8, 0), (8, 0), True)
A['B11-T7'] = kertas(150, 110, 170, 170, -2) + teks(150, 50, '計畫', 22) + ''.join(centang(85, 80 + i * 32, .5, 4) + garis((100, 80 + i * 32), (210, 80 + i * 32), k='t') for i in range(4))
A['B11-T8'] = lantai() + orang(120, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(20, -10), (36, -40)]}) + jalur('M160 26 L188 26 L183 46 L165 46 Z', 'a') + garis((174, 46), (174, 56)) + teks(174, 42, '1', 14, angka=True)

# B12 — keluarga & hewan
A['B12-1'] = lantai() + kucing(95, 196, 1.2) + kucing(210, 196, 1.2, 'a')
A['B12-2'] = lantai() + anjing(140, 198, 1.4)
A['B12-3'] = kotak(18, 18, 264, 184, 'h', 4) + kotak(26, 26, 248, 168, 'p') + rumah(95, 184, 100, 70) + orang(200, kaki=184, tinggi=140, jenis='nenek', rambut='pendek', baju='a', rok=False) + orang(250, kaki=184, tinggi=78, jenis='laki')
A['B12-4'] = lantai() + orang(60, tinggi=150, jenis='nenek', rambut='uban', baju='a') + kucing(135, 198, .8) + kucing(195, 198, .8, 'a') + kucing(255, 198, .8, 'h')
A['B12-5'] = kotak(18, 18, 264, 184, 'h', 4) + kotak(26, 26, 248, 168, 'p') + papan_tulis(110, 44, 140, 70) + orang(225, kaki=184, tinggi=140, jenis='pria', baju='a', kacamata=True, tangan={'ki': [(10, -10), (34, -40)]})


def biji_kopi(x, y, s=1.0):
    return elips(x, y, 8 * s, 11 * s, 'h') + jalur(f'M{f(x)} {f(y - 10 * s)} q{f(-4 * s)} {f(10 * s)} 0 {f(20 * s)}', 'w')


# ---------------- B13–B24 ----------------
def _kepala(x, tinggi, jenis):
    s_ = sendi(x, LANTAI, tinggi, jenis)
    return s_['cy'], s_['r']


def kelas_murid(jenis_list, y=200):
    o = lantai()
    n = len(jenis_list)
    for i, j in enumerate(jenis_list):
        o += orang(40 + i * (220 / max(n - 1, 1)), tinggi=100, jenis=j, baju='a' if j == 'gadis' else 'h')
    return o


# --- B12 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kuda(x, bawah, s=1.0, k='p'):
    """Kuda dilihat dari samping, kepala di kanan."""
    P = lambda dx, dy: (x + dx * s, bawah - dy * s)
    return (''.join(garis(P(dx, 50), P(dx, 0), lebar=7 * s) for dx in (-34, -22, 22, 34))
            + bentuk(P(26, 74), P(42, 122), P(60, 118), P(52, 66), k=k)
            + elips(x, bawah - 62 * s, 46 * s, 20 * s, k)
            + bentuk(P(40, 126), P(56, 132), P(92, 104), P(88, 94), P(76, 92), P(48, 108), k=k)
            + bentuk(P(44, 126), P(46, 140), P(54, 128), k=k)
            + jalur(f'M{f(x + 42 * s)} {f(bawah - 124 * s)} L{f(x + 26 * s)} {f(bawah - 76 * s)}', 'g', 7 * s)
            + bulat(x + 60 * s, bawah - 116 * s, 2.8 * s, 'h') + bulat(x + 86 * s, bawah - 100 * s, 1.8 * s, 'h')
            + jalur(f'M{f(x - 44 * s)} {f(bawah - 70 * s)} Q{f(x - 62 * s)} {f(bawah - 50 * s)} {f(x - 56 * s)} {f(bawah - 26 * s)}', 'g', 7 * s))


def kakek(x, tinggi=145, kaki=LANTAI, tongkat_=True, **kw):
    t = sendi(x, kaki, tinggi, 'nenek')
    r, cy = t['r'], t['cy']
    o = orang(x, kaki=kaki, tinggi=tinggi, jenis='nenek', rambut='bayi', rok=False, kacamata=True, baju=kw.pop('baju', 'h'), **kw)
    o += jalur(f'M{f(x - r * 1.02)} {f(cy + r * .1)} Q{f(x - r * 1.1)} {f(cy - r * .7)} {f(x - r * .6)} {f(cy - r * .85)}', 'g', r * .3).replace('stroke-width', 'stroke:#999;stroke-width')
    o += jalur(f'M{f(x + r * 1.02)} {f(cy + r * .1)} Q{f(x + r * 1.1)} {f(cy - r * .7)} {f(x + r * .6)} {f(cy - r * .85)}', 'g', r * .3).replace('stroke-width', 'stroke:#999;stroke-width')
    return o + (tongkat(x, tinggi) if tongkat_ and kaki == LANTAI else '')


def foto_lama(isi):
    return kotak(18, 18, 264, 184, 'h', 4) + kotak(26, 26, 248, 168, 'p') + isi


def dokter2(x, kaki=184, tinggi=140):
    y = kaki - tinggi
    return (orang(x, kaki=kaki, tinggi=tinggi, jenis='pria', baju='p') + jalur(f'M{x - 9} {y + 42} Q{x - 13} {y + 70} {x} {y + 74} Q{x + 13} {y + 70} {x + 9} {y + 42}', 'g', 2.5)
            + bulat(x, y + 76, 4, 'h') + kotak(x + 8, y + 56, 14, 14, 'p') + garis((x + 15, y + 59), (x + 15, y + 67), lebar=2.5) + garis((x + 11, y + 63), (x + 19, y + 63), lebar=2.5))


A['B12-L4a'] = lantai() + anjing(95, 196, 1.0) + anjing(215, 196, 1.0, 'a')
A['B12-L4b'] = lantai() + kucing(140, 196, 1.3)
A['B12-L4c'] = lantai() + kucing(95, 196, 1.2) + kucing(210, 196, 1.2, 'a')
A['B12-L5a'] = foto_lama(dokter2(150))
A['B12-L5b'] = foto_lama(papan_tulis(110, 44, 140, 70) + orang(225, kaki=184, tinggi=140, jenis='pria', baju='a', tangan={'ki': [(10, -10), (34, -40)]}))
A['B12-L5c'] = foto_lama(mobil(175, lantai_y=184, w=170, taksi=True) + orang(60, kaki=184, tinggi=120, jenis='pria', baju='h'))
A['B12-L6a'] = lantai() + anjing(140, 198, 1.4)
A['B12-L6b'] = lantai() + kucing(95, 196, 1.2) + kucing(210, 196, 1.2, 'a')
A['B12-L6c'] = lantai() + kuda(140, 200, 1.3)
A['B12-L8a'] = lantai() + kucing(45, 198, .7) + kucing(105, 198, .7, 'a') + kucing(165, 198, .7, 'h') + anjing(245, 198, .8)
A['B12-L8b'] = lantai() + kucing(40, 198, .7) + anjing(115, 198, .7) + anjing(185, 198, .7, 'a') + anjing(255, 198, .7, 'h')
A['B12-L8c'] = lantai() + kucing(70, 198, .8) + kucing(150, 198, .8, 'a') + kucing(230, 198, .8, 'h')
A['B12-L9'] = lantai() + orang(70, tinggi=155, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (44, 4)]}) + kuda(180, 200, 1.1)
A['B12-L10'] = (kotak(10, 40, 130, 120, 'h', 3) + kotak(16, 46, 118, 108, 'p') + rumah(75, 140, 80, 56) + teks(75, 175, '臺南', 16)
                + panah(146, 100, 166, 100, 4)
                + kotak(170, 40, 120, 120, 'h', 3) + kotak(176, 46, 108, 108, 'p') + gedung(230, 150, tingkat=5, lebar=50, tt=18) + teks(230, 175, '臺北', 16))
A['B12-T3a'] = lantai() + rumah(205) + kakek(70, tinggi=140)
A['B12-T3b'] = lantai() + sekolah_b(205) + orang(70, tinggi=150, jenis='pria', baju='h')
A['B12-T3c'] = lantai() + pohon(45) + pohon(255, s=1.1) + bangku(150) + orang(150, tinggi=150, jenis='pria', baju='h')
A['B12-T4a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h')
A['B12-T4b'] = lantai() + kakek(150, tinggi=150) 
A['B12-T4c'] = lantai() + orang(150, tinggi=155, jenis='wanita', baju='a')
A['B12-T6a'] = lantai() + anjing(70, 198, .9) + kucing(170, 198, .8) + kucing(245, 198, .8, 'a')
A['B12-T6b'] = lantai() + anjing(60, 198, .8) + anjing(150, 198, .8, 'a') + kucing(245, 198, .8)
A['B12-T6c'] = lantai() + kucing(95, 196, 1.2) + kucing(210, 196, 1.2, 'a')
A['B12-T7'] = foto_lama(kakek(50, kaki=184, tinggi=120, tongkat_=False) + orang(95, kaki=184, tinggi=115, jenis='nenek', rambut='uban', baju='a')
                        + orang(145, kaki=184, tinggi=130, jenis='pria', baju='h') + orang(190, kaki=184, tinggi=122, jenis='wanita', baju='a') + orang(240, kaki=184, tinggi=70, jenis='gadis', baju='p'))
A['B12-T8'] = foto_lama(orang(150, kaki=184, tinggi=80, jenis='laki', baju='h') + teks(240, 50, '1998', 14, angka=True))

# B13 — angka & jumlah
A['B13-1'] = lantai() + sekolah(95, 200, 150, 100) + papan_angka(230, 70, '215人', 100, 46)
A['B13-2'] = lantai() + sekolah(95, 200, 150, 100) + papan_angka(230, 70, '320人', 100, 46)
A['B13-3'] = (lantai() + garis((150, 60), (150, 200), k='t') + orang(45, tinggi=110, jenis='laki', baju='h') + orang(100, tinggi=115, jenis='laki', baju='a')
              + orang(200, tinggi=108, jenis='gadis', baju='a') + orang(255, tinggi=112, jenis='gadis', baju='h'))
A['B13-4'] = layar_ponsel(150, 110, '', 2.6) + teks(150, 100, '0912-', 22, angka=True) + teks(150, 130, '345-678', 22, angka=True)
A['B13-5'] = kelas_murid(['gadis'] * 5)

# --- B13 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def hp_nomor(a, b):
    return layar_ponsel(150, 110, '', 2.6) + teks(150, 100, a, 22, angka=True) + teks(150, 130, b, 22, angka=True)


def papan_alamat(baris):
    n = len(baris)
    h = 30 + n * 34
    y = 105 - h / 2
    o = kotak(40, y, 220, h, 'h', 8) + kotak(48, y + 8, 204, h - 16, 'p', 5)
    return o + ''.join(teks(150, y + 42 + i * 34, s, 24) for i, s in enumerate(baris))


def kelas_campur(lk, pr):
    js = ['laki'] * lk + ['gadis'] * pr
    return kelas_murid(js)


def deret_label(hs):
    return ''.join(label_harga(60 + i * 90, 50 + (i % 2) * 80, h, 104, 50).replace('font-size="32"', 'font-size="22"') for i, h in enumerate(hs))


A['B13-L4a'] = hp_nomor('0977-', '280-115')
A['B13-L4b'] = hp_nomor('0977-', '208-115')
A['B13-L4c'] = hp_nomor('0911-', '208-115')
A['B13-L5a'] = lantai() + papan_tulis(150, 30, 160, 70) + papan_angka(150, 120, '34人', 100, 46, tiang=False)
A['B13-L5b'] = lantai() + papan_tulis(150, 30, 160, 70) + papan_angka(150, 120, '13人', 100, 46, tiang=False)
A['B13-L5c'] = lantai() + papan_tulis(150, 30, 160, 70) + papan_angka(150, 120, '300人', 100, 46, tiang=False)
A['B13-L6a'] = papan_alamat(['臺北市', '中山路20號'])
A['B13-L6b'] = papan_alamat(['臺中市', '中山路2號'])
A['B13-L6c'] = papan_alamat(['臺中市', '中山路20號'])
A['B13-L8a'] = kelas_murid(['laki', 'gadis', 'laki', 'gadis', 'laki'])
A['B13-L8b'] = kelas_murid(['gadis'] * 5)
A['B13-L8c'] = kelas_murid(['laki'] * 5)
A['B13-L9'] = papan_alamat(['臺北市', '中山路15號'])
A['B13-L10'] = lantai() + sekolah(150, 200, 170, 100) + ''.join(orang(30 + i * 30, tinggi=60, jenis='laki' if i % 2 else 'gadis', baju='h' if i % 2 else 'a') for i in range(9)).replace('', '') if False else (
    lantai() + sekolah(150, 150, 170, 90) + ''.join(orang(28 + i * 30.5, kaki=200, tinggi=46, jenis='laki' if i % 2 else 'gadis', baju='h' if i % 2 else 'a') for i in range(9)))
A['B13-T3a'] = papan_alamat(['臺中市', '中山路5號'])
A['B13-T3b'] = papan_alamat(['臺北市', '中山路15號'])
A['B13-T3c'] = papan_alamat(['臺北市', '中山路5號'])
A['B13-T4a'] = kelas_murid(['laki', 'laki', 'gadis', 'laki', 'laki'])
A['B13-T4b'] = kelas_murid(['gadis', 'gadis', 'laki', 'gadis', 'gadis'])
A['B13-T4c'] = kelas_murid(['laki', 'gadis', 'laki', 'gadis'])
A['B13-T6a'] = deret_label([10, 10, 10])
A['B13-T6b'] = deret_label([10, 25, 60])
A['B13-T6c'] = deret_label([100, 100, 100])
A['B13-T7'] = kertas(150, 105, 190, 180, -1) + ''.join(teks(105, 88 + i * 42, s, 20) + garis((140, 92 + i * 42), (225, 92 + i * 42), k='t') for i, s in enumerate(['姓名', '地址', '電話']))
A['B13-T8'] = lantai() + orang(90, tinggi=155, jenis='wanita', baju='h', tangan={'ka': [(26, -6), (52, -14)]}) + orang(220, tinggi=150, jenis='wanita', baju='a')

# B14 — sekolah
A['B14-1'] = lantai() + tas_buka(150, 196, 13, 1.6)
A['B14-2'] = lantai() + sekolah(210, 200, 130, 90) + orang(80, tinggi=90, jenis='gadis', baju='a') + tas_punggung(58, 138, .75)
A['B14-3'] = lantai() + tas_buka(150, 196, 12, 1.6)
A['B14-4'] = lantai() + sekolah(200, 200, 150, 100, '高中') + orang(70, tinggi=150, jenis='laki', baju='h') + tas_punggung(46, 104, .9)
A['B14-5'] = kalender_bulan(95, 34, 9, '', 130, 130) + lantai() + jalan_kaki(230, 'laki', 110, 'a') + tas_punggung(210, 124, .7)

# --- B14 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def tas_isi(buku_n=0, pena_n=0):
    o = ''
    o = tas_buka(150, 196, buku_n, 1.6)
    for i in range(pena_n):
        o += pulpen(150 + (i - (pena_n - 1) / 2) * 26 + (40 if buku_n else 0), 70, 84, -80 + i * 8)
    return o


def anak_sekolah(papan, jenis='gadis', tinggi=90, papan2=None):
    baju = 'a' if jenis in ('gadis', 'wanita') else 'h'
    o = lantai() + sekolah(205, 200, 150, 100, papan) + orang(70, tinggi=tinggi, jenis=jenis, baju=baju) + tas_punggung(70 - tinggi * .24, 200 - tinggi * .6, tinggi / 120)
    return o + (papan_angka(70, 30, papan2, 90, 36, tiang=False, uk=20) if papan2 else '')


def nilai(n):
    return kertas(150, 105, 170, 180, -2) + teks(150, 130, str(n), 70, angka=True) + teks(150, 175, '分', 22)


A['B14-L4a'] = tas_isi(12)
A['B14-L4b'] = tas_isi(0, 3)
A['B14-L4c'] = tas_isi(3, 1)
A['B14-L5a'] = anak_sekolah('小學', 'laki', 90)
A['B14-L5b'] = anak_sekolah('高中', 'pria', 140)
A['B14-L5c'] = anak_sekolah('大學', 'pria', 165)
A['B14-L6a'] = kalender_bulan(150, 30, 9, 1, 170, 160)
A['B14-L6b'] = kalender_bulan(150, 30, 3, 1, 170, 160)
A['B14-L6c'] = kalender_bulan(150, 30, 10, 1, 170, 160)
A['B14-L8a'] = kelas_murid(['laki', 'laki', 'gadis', 'laki', 'laki', 'laki'])
A['B14-L8b'] = kelas_murid(['laki', 'gadis', 'laki', 'gadis', 'laki', 'gadis'])
A['B14-L8c'] = kelas_murid(['gadis'] * 6)
A['B14-L9'] = nilai(95)
A['B14-L10'] = lantai() + papan_tulis(150, 20, 150, 56) + papan_angka(150, 84, '25人', 90, 36, tiang=False, uk=20) + ''.join(orang(25 + i * 31, tinggi=70, jenis='laki' if i % 2 else 'gadis', baju='h' if i % 2 else 'a') for i in range(9))
A['B14-T3a'] = lantai() + papan_tulis(150, 30, 160, 70) + papan_angka(150, 120, '12人', 100, 46, tiang=False)
A['B14-T3b'] = lantai() + papan_tulis(150, 30, 160, 70) + papan_angka(150, 120, '230人', 100, 46, tiang=False)
A['B14-T3c'] = lantai() + papan_tulis(150, 30, 160, 70) + papan_angka(150, 120, '25人', 100, 46, tiang=False)
A['B14-T4a'] = anak_sekolah('小學', 'gadis', 90, '三年級')
A['B14-T4b'] = anak_sekolah('高中', 'wanita', 135, '三年級')
A['B14-T4c'] = anak_sekolah('大學', 'wanita', 160)
A['B14-T6a'] = lantai() + kakek(150, tinggi=150)
A['B14-T6b'] = lantai() + gedung(220, tingkat=6, lebar=90) + orang(90, tinggi=160, jenis='pria', baju='h', kacamata=True, tangan={'ka': [(16, 40), (20, 56)]}) + kotak(98, 124, 40, 30, 'h', 3)
A['B14-T6c'] = anak_sekolah('小學', 'laki', 90)
A['B14-T7'] = kertas(150, 105, 170, 180, -1) + teks(150, 50, '成績', 22) + ''.join(teks(110, 90 + i * 34, s, 18) + teks(200, 90 + i * 34, n, 20, angka=True) for i, (s, n) in enumerate([('中文', '98'), ('英文', '95'), ('數學', '100')]))
A['B14-T8'] = tas_isi(8)

# B15 — bahasa
A['B15-1'] = lantai() + meja(150, 150, 240) + kertas(185, 132, 70, 30, 0) + orang(110, tinggi=150, jenis='wanita', duduk=156, baju='a', tangan={'ka': [(20, 20), (54, 26)]}) + pulpen(186, 128, 40, -40)
A['B15-2'] = lantai() + orang(85, tinggi=160, jenis='wanita', baju='a', wajah='nyanyi') + gelembung(200, 70, 150, 70, teks(200, 80, 'こんにちは', 22, angka=True), (-1, 1))
A['B15-3'] = kertas_kotak(150, 40, 180, 150)
A['B15-4'] = (lantai() + orang(80, tinggi=160, jenis='pria', baju='h', wajah='kaget', tangan={'ka': [(20, -4), (40, -20)]}) + orang(190, tinggi=150, jenis='wanita', baju='a')
              + orang(250, tinggi=145, jenis='pria', baju='a') + centang(220, 22, 1.2) + jalur('M110 36 q10 4 16 0 M110 48 q10 4 16 0', 'g'))
A['B15-5'] = lantai() + kamus(150, 196)

# --- B15 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kamus2(x, bawah, label, w=120, h=150, uk=20):
    o = kotak(x - w / 2, bawah - h, w, h, 'h', 6) + kotak(x - w / 2 + 10, bawah - h + 16, w - 26, 34, 'p', 3) + teks(x - 4, bawah - h + 40, label, uk, angka=True)
    for i in range(int(h / 25)):
        o += kotak(x + w / 2 - 2, bawah - h + 14 + i * 22, 10, 16, 'a' if i % 2 else 'p', 2)
    return o + garis((x - w / 2 + 8, bawah - 12), (x + w / 2 - 8, bawah - 12), k='w')


def penutur(kata, jenis='wanita'):
    baju = 'a' if jenis == 'wanita' else 'h'
    o = lantai() + orang(70, tinggi=160, jenis=jenis, baju=baju, wajah='nyanyi')
    if len(kata) == 1:
        return o + gelembung(200, 70, 150, 70, teks(200, 80, kata[0], 22, angka=True), (-1, 1))
    return o + gelembung(200, 40, 150, 56, teks(200, 48, kata[0], 22, angka=True), (-1, 1)) + gelembung(200, 128, 150, 56, teks(200, 136, kata[1], 22, angka=True), (-1, 1))


def cerita(kata):
    return (lantai() + orang(70, tinggi=160, jenis='pria', baju='h', wajah='nyanyi', tangan={'ka': [(20, 10), (40, 0)]}) + buku(112, 104, 30, 38)
            + orang(200, tinggi=80, jenis='laki', baju='a') + orang(255, tinggi=82, jenis='gadis', baju='h') + gelembung(195, 40, 110, 52, teks(195, 48, kata, 22, angka=True), (-1, 1)))


A['B15-L4a'] = layar_ponsel(150, 105, '', 2.4)
A['B15-L4b'] = lantai() + kamus(150, 196)
A['B15-L4c'] = lantai() + meja(150, 200, 200) + komputer(150, 130, 120) if False else komputer(150, 190, 150)
A['B15-L5a'] = penutur(['Hello', 'こんにちは'])
A['B15-L5b'] = penutur(['Bonjour'])
A['B15-L5c'] = penutur(['Hello', 'Bonjour'])
A['B15-L6a'] = lantai() + kamus2(150, 196, 'English', 140, 170)
A['B15-L6b'] = lantai() + kamus2(150, 196, '日本語', 140, 170)
A['B15-L6c'] = lantai() + kamus2(150, 196, '日本語', 80, 90, 14)
A['B15-L8a'] = lantai() + papan_tulis(195, 40, 150, 80) + teks(195, 92, 'Hello', 28, warna='#fff', angka=True) + orang(70, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, -10), (46, -40)]})
A['B15-L8b'] = cerita('你好')
A['B15-L8c'] = cerita('Hello')
A['B15-L9'] = lantai() + meja(160, 150, 230) + kertas_kotak(200, 92, 90, 54, '字') + orang(90, tinggi=110, jenis='gadis', baju='a', duduk=156, tangan={'ka': [(20, 16), (60, 20)]}) + pulpen(210, 118, 40, -40)
A['B15-L10'] = lantai() + orang(70, tinggi=160, jenis='pria', baju='h', wajah='nyanyi') + orang(240, tinggi=155, jenis='pria', baju='a') + gelembung(155, 45, 130, 54, teks(155, 52, 'Guten Tag', 20, angka=True), (-1, 1))
A['B15-T3a'] = penutur(['你好', 'こんにちは'], 'pria')
A['B15-T3b'] = penutur(['Hello', 'こんにちは'], 'pria')
A['B15-T3c'] = penutur(['Hello'], 'pria')
A['B15-T4a'] = penutur(['Guten Tag'])
A['B15-T4b'] = penutur(['こんにちは'])
A['B15-T4c'] = penutur(['Bonjour'])
A['B15-T6a'] = kertas(150, 105, 200, 150, -1) + teks(150, 115, 'Hello!', 40, angka=True)
A['B15-T6b'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='nyanyi') + orang(220, tinggi=150, jenis='pria', baju='h') + gelembung(160, 30, 70, 40, teks(160, 36, '…', 22, angka=True), (-1, 1))
A['B15-T6c'] = kertas(150, 105, 200, 150, -1) + teks(150, 115, 'ありがとう', 34, angka=True) + bintang(250, 50, 10) + bintang(60, 160, 8)
A['B15-T7'] = lantai() + orang(80, tinggi=155, jenis='pria', baju='h', wajah='nyanyi') + gelembung(200, 50, 140, 64, teks(200, 59, '你好！', 26), (-1, 1)) + kertas(220, 150, 60, 40, 0)
A['B15-T8'] = (lantai() + papan_tulis(70, 30, 110, 60) + orang(70, tinggi=155, jenis='wanita', baju='a', wajah='nyanyi', tangan={'ka': [(20, -4), (40, -20)]})
               + orang(190, tinggi=110, jenis='laki', baju='h') + orang(250, tinggi=110, jenis='gadis', baju='a') + centang(220, 40, 1.2))

# B16 — belajar
A['B16-1'] = lantai() + meja(160, 140, 220) + buku_tumpuk(230, 140, 2, 50, 14) + kertas(160, 128, 60, 20) + lampu(250, 70) + orang(95, tinggi=150, jenis='laki', duduk=146, baju='a', wajah='senyum', tangan={'ka': [(24, 16), (54, 22)]})
A['B16-2'] = kalender_senin(150, 14, 2, 3) + lantai() + meja(150, 150, 200) + kertas(170, 136, 60, 24) + orang(110, tinggi=140, jenis='gadis', duduk=154, baju='a', tangan={'ka': [(22, 16), (52, 20)]})
A['B16-3'] = (lantai() + tas_buka(90, 196, 0, 1.0) + orang(190, tinggi=150, jenis='laki', baju='a', wajah='kaget')
              + gelembung_pikiran(235, 50, 90, 64, buku(235, 66, 30, 32, 'h') + silang(235, 50, 20, 5), 205, 84))
A['B16-4'] = lantai() + meja(160, 140, 220) + buku(200, 140, 40, 26, 'a') + kertas(160, 128, 60, 20) + orang(95, tinggi=150, jenis='pria', duduk=146, baju='h', tangan={'ka': [(24, 16), (54, 22)]})
A['B16-5'] = kotak(70, 90, 160, 60, 'p', 10) + kotak(78, 98, 144, 44, 'a', 6) + gelembung_pikiran(220, 44, 90, 60, pulpen(220, 44, 60, -20) + silang(220, 44, 22, 5), 190, 74)

# --- B16 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kamus_kecil(x, bawah, w, h):
    return (kotak(x - w / 2, bawah - h, w, h, 'h', w * .08) + kotak(x - w * .36, bawah - h * .8, w * .72, h * .3, 'p', 2)
            + teks(x, bawah - h * .58, 'A–Z', w * .22, angka=True) + kotak(x + w / 2 - 2, bawah - h * .85, w * .1, h * .7, 'a', 2))


def lupa(benda, jenis='pria'):
    return (lantai() + tas_buka(80, 196, 0, 1.0) + orang(170, tinggi=150, jenis=jenis, baju='h' if jenis == 'pria' else 'a', wajah='kaget')
            + gelembung_pikiran(240, 50, 100, 70, benda, 200, 80))


def ujian_kertas(isi, uk=30):
    return kertas(150, 105, 200, 170, -1) + teks(150, 40, '考試', 20) + teks(150, 120, isi, uk, angka=True) + ''.join(garis((80, 150 + i * 16), (220, 150 + i * 16), k='t') for i in range(2))


def kotak_pensil(isi=False):
    o = kotak(50, 90, 200, 70, 'p', 12) + kotak(58, 98, 184, 54, 'a', 8)
    return o + (pulpen(150, 125, 150, 0) if isi else '')


def belajar_meja(jenis='wanita', extra=''):
    baju = 'a' if jenis in ('wanita', 'gadis') else 'h'
    return lantai() + meja(160, 140, 220) + buku(200, 140, 40, 26, 'a') + kertas(160, 128, 60, 20) + orang(95, tinggi=150, jenis=jenis, duduk=146, baju=baju, tangan={'ka': [(24, 16), (54, 22)]}) + extra


A['B16-L4a'] = kalender_senin(150, 14, 2, 3) + belajar_meja('wanita')[len(lantai()):] + lantai() if False else belajar_meja('wanita', kalender_senin(200, 4, 2, 3, 180))
A['B16-L4b'] = lantai_kamar() + ranjang(150, 200, 190) + kotak(110, 134, 104, 16, 'a', 7) + jalur('M86 128 Q84 146 76 150 L120 150 Q112 146 110 128 Z', 'h') + bulat(98, 132, 12) + muka(98, 132, 12, 'tidur')
A['B16-L4c'] = (lantai() + papan_tulis(150, 14, 150, 50) + teks(150, 48, '考試', 22, warna='#fff') + meja_kelas(90) + meja_kelas(210)
                + orang(90, tinggi=120, jenis='wanita', baju='a', duduk=150) + orang(210, tinggi=115, jenis='pria', baju='h', duduk=150) + kertas(90, 132, 40, 14) + kertas(210, 132, 40, 14))
A['B16-L5a'] = lupa(pulpen(240, 50, 60, -20))
A['B16-L5b'] = lupa(layar_ponsel(240, 50, '', .7))
A['B16-L5c'] = lupa(kamus_kecil(240, 76, 44, 54))
A['B16-L6a'] = lantai() + papan_tulis(55, 20, 90, 50) + orang(120, tinggi=155, jenis='wanita', baju='a') + orang(205, tinggi=150, jenis='pria', baju='h', tangan={'ki': [(-14, -10), (-34, -30)]}) + orang(262, tinggi=145, jenis='wanita', baju='a') + teks(175, 40, '?', 30, angka=True)
A['B16-L6b'] = lantai() + meja(150, 150, 200) + kamus_kecil(150, 150, 64, 74) + orang(70, tinggi=150, jenis='pria', baju='h', duduk=156) + orang(235, tinggi=145, jenis='wanita', baju='a', duduk=156)
A['B16-L6c'] = lantai() + orang(110, tinggi=155, jenis='pria', baju='h', tangan={'ka': [(16, 20), (30, 4)]}) + layar_ponsel(150, 110, '', .5) + orang(210, tinggi=150, jenis='wanita', baju='a')
A['B16-L8a'] = kotak_pensil(True)
A['B16-L8b'] = lantai() + tas_buka(150, 196, 0, 1.6)
A['B16-L8c'] = kotak_pensil(False)
A['B16-L9'] = ujian_kertas('1+1=2') + muka_besar(240, 170, 22) if False else ujian_kertas('1+1=2') + bulat(240, 175, 20, 'p') + muka(240, 175, 20, 'senyum')
A['B16-L10'] = lantai() + papan_tulis(170, 24, 140, 70) + teks(170, 76, '書', 44, warna='#fff') + orang(250, tinggi=150, jenis='wanita', baju='a') + orang(70, tinggi=110, jenis='laki', baju='h', tangan={'ka': [(16, -14), (40, -40)]}) + teks(110, 40, '?', 30, angka=True)
A['B16-T3a'] = ujian_kertas('English', 30)
A['B16-T3b'] = ujian_kertas('中文', 40)
A['B16-T3c'] = ujian_kertas('3+4=?', 32)
A['B16-T4a'] = A['B16-L6b']
A['B16-T4b'] = A['B16-L6c']
A['B16-T4c'] = A['B16-L6a']
A['B16-T6a'] = belajar_meja('pria', kalender_senin(200, 4, 2, 3, 180))
A['B16-T6b'] = lantai() + meja(150, 150, 120) + kue_ultah(150, 150) + orang(60, tinggi=145, jenis='pria', baju='h', tangan={'ka': [(20, -20), (30, -50)]}) + orang(245, tinggi=140, jenis='wanita', baju='a', tangan={'ki': [(20, -20), (30, -50)]})
A['B16-T6c'] = lantai_kamar() + ranjang(150, 200, 190) + kotak(110, 134, 104, 16, 'a', 7) + bulat(98, 132, 12) + muka(98, 132, 12, 'tidur')
A['B16-T7'] = belajar_meja('laki', bulan_bintang(255, 40, .7) + buku_tumpuk(230, 140, 4, 50, 12))
A['B16-T8'] = lantai() + orang(80, tinggi=155, jenis='wanita', baju='a', wajah='puas') + gelembung_pikiran(170, 45, 130, 64, kotak(120, 28, 100, 34, 'p', 4) + teks(170, 52, '林安妮', 20), 120, 90) + orang(262, tinggi=130, jenis='wanita', baju='h')

# B17 — perpustakaan & buku
A['B17-1'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='pria', duduk=150, baju='a', tangan={'ki': [(20, 0), (30, -20)], 'ka': [(20, 0), (30, -20)]}) + koran(150, 60, 150, 90)
A['B17-2'] = lantai() + rak_buku(55, 200, 90, 160) + rak_buku(250, 200, 80, 160) + meja(150, 140, 110) + buku(150, 140, 34, 20, 'a') + orang(150, tinggi=130, jenis='gadis', duduk=150, baju='a')
A['B17-3'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(20, -14), (30, -48)]}) + buku(200, 58, 38, 48, 'h') + bintang(236, 30, 8) + bintang(170, 20, 6)
A['B17-4'] = lantai() + rak_buku(60, 200, 100, 160) + kasir(215) + label_harga(232, 24, '120', 100, 40) + orang(140, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(16, 16), (30, 20)]}) + buku(186, 116, 24, 30, 'a')
A['B17-5'] = lantai() + lonceng(230, 60, .6) + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='kaget', tangan={'ka': [(16, -4), (2, -26)]}) + jalur('M150 36 q10 12 0 24 M162 28 q16 20 0 40', 'g')

# --- B17 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def perpus(isi=''):
    return lantai() + rak_buku(45, 200, 70, 160) + rak_buku(255, 200, 70, 160) + kotak(110, 20, 80, 26, 'p', 3) + teks(150, 40, '圖書館', 16) + isi


def toko_buku(isi=''):
    return lantai() + rak_buku(55, 200, 90, 160) + kasir(240) + kotak(205, 20, 70, 26, 'p', 3) + teks(240, 40, '書店', 16) + isi


def catatan(x, y, s=1.0):
    w, h = 44 * s, 56 * s
    return kotak(x - w / 2, y - h, w, h, 'p', 3) + ''.join(bulat(x - w / 2, y - h + 8 * s + i * 10 * s, 3 * s, 'p') for i in range(5)) + ''.join(garis((x - w / 2 + 8 * s, y - h + 14 * s + i * 10 * s), (x + w / 2 - 6 * s, y - h + 14 * s + i * 10 * s), k='t') for i in range(4))


def baris_kertas(n):
    o = kertas(150, 105, 170, 190, 0)
    gap = 160 / (n + 1)
    return o + ''.join(garis((86, 20 + gap * (i + 1)), (214, 20 + gap * (i + 1))) + jalur(f'M92 {20 + gap * (i + 1) - 4} q20 -8 40 0 q20 8 40 0 q20 -8 30 0', 'g', 2) for i in range(n))


A['B17-L4a'] = toko_buku()
A['B17-L4b'] = perpus(meja(150, 150, 90))
A['B17-L4c'] = lantai() + rumah(150, lebar=160, t=110)
A['B17-L5a'] = lantai() + meja(150, 130, 180) + catatan(150, 130, 1.2)
A['B17-L5b'] = lantai() + catatan(150, 120, 1.2) + tas_buka(150, 196, 0, 1.6)
A['B17-L5c'] = lantai() + kursi(150, s=1.3) + catatan(160, 145, 1.0)
A['B17-L6a'] = perpus(meja(150, 150, 90))
A['B17-L6b'] = A['B17-L4c']
A['B17-L6c'] = toko_buku()
A['B17-L8a'] = toko_buku(orang(110, tinggi=110, jenis='laki', baju='h', wajah='kaget') + orang(170, tinggi=155, jenis='pria', baju='a', kacamata=True))
A['B17-L8b'] = perpus(orang(115, tinggi=110, jenis='laki', baju='h', wajah='kaget') + orang(180, tinggi=155, jenis='pria', baju='a', kacamata=True))
A['B17-L8c'] = lantai() + papan_tulis(200, 24, 150, 70) + orang(220, tinggi=155, jenis='pria', baju='a', kacamata=True) + orang(80, tinggi=110, jenis='laki', baju='h', wajah='kaget')
A['B17-L9'] = perpus(meja(150, 150, 100) + kertas(165, 140, 40, 14) + orang(120, tinggi=140, jenis='wanita', duduk=156, baju='a', tangan={'ka': [(20, 16), (44, 20)]}) + pulpen(170, 136, 30, -40))
A['B17-L10'] = (lantai() + orang(70, tinggi=155, jenis='wanita', baju='a', kacamata=True, wajah='nyanyi') + gelembung(140, 34, 90, 44, teks(140, 41, '小明！', 18), (-1, 1))
                + kursi_depan(225, 150) + orang(225, tinggi=110, jenis='laki', duduk=150, baju='h', tangan={'ki': [(16, 0), (24, -14)], 'ka': [(16, 0), (24, -14)]}) + buku(225, 146, 46, 26, 'a'))
A['B17-T3a'] = lantai_kamar() + ranjang(150, 200, 190) + catatan(170, 145, 1.0)
A['B17-T3b'] = A['B17-L5c']
A['B17-T3c'] = A['B17-L5b']
A['B17-T4a'] = baris_kertas(15)
A['B17-T4b'] = baris_kertas(5)
A['B17-T4c'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='wanita', duduk=150, baju='a', tangan={'ki': [(20, 0), (30, -20)], 'ka': [(20, 0), (30, -20)]}) + buku(150, 140, 70, 36, 'a')
A['B17-T6a'] = lantai() + rumah(225, lebar=110, t=90) + meja(90, 150, 120) + kertas(100, 140, 40, 14) + orang(70, tinggi=130, jenis='laki', duduk=156, baju='h', tangan={'ka': [(16, 16), (34, 20)]})
A['B17-T6b'] = perpus(meja(150, 150, 100) + orang(150, tinggi=130, jenis='laki', duduk=156, baju='h', wajah='tidur') + teks(190, 70, 'z z', 18, angka=True))
A['B17-T6c'] = perpus(meja(150, 150, 100) + kertas(165, 140, 40, 14) + orang(120, tinggi=130, jenis='laki', duduk=156, baju='h', tangan={'ka': [(20, 16), (44, 20)]}))
A['B17-T7'] = lantai() + meja(150, 150, 200) + catatan(130, 150, 1.4) + jalur('M180 140 L250 110 L256 116 L186 146 Z', 'a') + bentuk((250, 110), (262, 106), (256, 116), k='h')
A['B17-T8'] = lantai() + orang(150, tinggi=110, jenis='laki', baju='h', wajah='puas', tangan={'ka': [(20, -14), (30, -40)]}) + buku(190, 90, 36, 44, 'h') + bintang(226, 60, 8) + bintang(160, 50, 6)

# B18 — musim & cuaca
A['B18-1'] = lantai() + gunung(150, 200, 260, 150) + ''.join(salju(40 + (i * 53) % 230, 20 + (i * 37) % 120, 7) for i in range(10))
A['B18-2'] = lantai() + gedung(70, tingkat=5, lebar=80) + rumah(210, 200, 110, 70) + ''.join(salju(30 + (i * 61) % 250, 18 + (i * 29) % 90, 6) for i in range(12))
A['B18-3'] = lantai() + pohon(250) + ''.join(bunga(30 + i * 40, 150 + (i % 2) * 12, .9) for i in range(5)) + kupu(80, 80) + kupu(170, 60, .8)
A['B18-4'] = (lantai() + manusia_salju(220) + orang(90, tinggi=160, jenis='pria', baju='h', wajah='sedih') + syal(90, 72, 14)
              + ''.join(salju(30 + (i * 67) % 250, 20 + (i * 31) % 70, 6) for i in range(8)))
A['B18-5'] = lantai() + pohon_gugur(150, 200, 1.2)

# --- B18 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def langit_salju(n=10, y0=20, h=110):
    return ''.join(salju(30 + (i * 53) % 240, y0 + (i * 37) % h, 6) for i in range(n))


def gemetar(x):
    return jalur(f'M{x - 36} 90 q-6 6 0 12 q6 6 0 12 M{x + 36} 90 q6 6 0 12 q-6 6 0 12', 'g', 3)


A['B18-L4a'] = lantai() + matahari(220, 50, 24) + orang(100, tinggi=160, jenis='pria', baju='p', wajah='puas')
A['B18-L4b'] = lantai() + langit_salju(12) + orang(100, tinggi=160, jenis='pria', baju='h', wajah='sedih') + syal(100, 72, 14)
A['B18-L4c'] = lantai() + awan(170, 40, 1.2, 'a') + hujan(170, 70, 160, 80) + orang(100, tinggi=160, jenis='pria', baju='h', wajah='sedih') + gemetar(100)
A['B18-L5a'] = lantai() + manusia_salju(220) + langit_salju(8, 20, 70) + orang(90, tinggi=160, jenis='wanita', baju='h') + syal(90, 72, 14)
A['B18-L5b'] = lantai() + matahari(230, 50, 24) + orang(90, tinggi=160, jenis='wanita', baju='p', wajah='puas') + jalur('M200 200 q20 -16 40 0 q20 16 40 0', 'g') + jalur('M190 186 q20 -16 40 0 q20 16 40 0 q20 -16 40 0', 'g')
A['B18-L5c'] = lantai() + pohon(250) + ''.join(bunga(30 + i * 40, 150 + (i % 2) * 12, .9) for i in range(5)) + kupu(80, 70) + kupu(170, 50, .8)
A['B18-L6a'] = lantai() + awan(150, 40, 1.4, 'a') + hujan(150, 70, 200, 100)
A['B18-L6b'] = lantai() + rumah(150, 200, 130, 80) + langit_salju(14, 14, 90)
A['B18-L6c'] = lantai() + matahari(150, 70, 34)
A['B18-L8a'] = lantai() + matahari(260, 34, 18) + gunung(150, 200, 260, 150, salju=False) + orang(110, tinggi=70, jenis='pria', baju='h') + orang(150, tinggi=66, jenis='wanita', baju='a')
A['B18-L8b'] = lantai() + langit_salju(10, 14, 50) + jendela(230, 70, 70, 60) + sofa(110, w=150) + orang(80, tinggi=130, jenis='pria', baju='h', duduk=150) + orang(140, tinggi=125, jenis='wanita', baju='a', duduk=150)
A['B18-L8c'] = lantai() + gunung(150, 200, 260, 150) + langit_salju(10) + orang(110, tinggi=70, jenis='pria', baju='h') + orang(150, tinggi=66, jenis='wanita', baju='a')
A['B18-L9'] = lantai() + pohon_gugur(200, 200, 1.1) + orang(80, tinggi=160, jenis='wanita', baju='h') + syal(80, 72, 14)
A['B18-L10'] = koran(150, 50, 200, 130) + awan(150, 120, .8, 'a') + hujan(150, 140, 70, 30, 5) + teks(150, 44, '明天', 18)
A['B18-T3a'] = A['B18-L6b']
A['B18-T3b'] = A['B18-L6c']
A['B18-T3c'] = A['B18-L6a']
A['B18-T4a'] = lantai() + gunung(150, 200, 260, 150) + orang(120, tinggi=70, jenis='pria', baju='h') + orang(160, tinggi=66, jenis='wanita', baju='a')
A['B18-T4b'] = lantai() + gunung(150, 200, 260, 150) + langit_salju(8) + orang(150, tinggi=90, jenis='pria', baju='h', tangan={'ki': [(10, 20), (20, 40)], 'ka': [(10, 20), (20, 40)]}) + garis((100, 196), (200, 186), lebar=5) + garis((110, 200), (210, 190), lebar=5)
A['B18-T4c'] = lantai() + tv(225, 150, 90) + meja(225, 150, 90) + sofa(85, w=130) + orang(60, tinggi=125, jenis='wanita', baju='a', duduk=150) + orang(110, tinggi=130, jenis='pria', baju='h', duduk=150)
A['B18-T6a'] = lantai() + matahari(230, 50, 26) + orang(100, tinggi=160, jenis='pria', baju='p', wajah='lelah')
A['B18-T6b'] = A['B18-L6a']
A['B18-T6c'] = lantai() + pohon_gugur(220, 200, 1.0) + orang(90, tinggi=160, jenis='pria', baju='h', wajah='sedih') + syal(90, 72, 14) + gemetar(90)
A['B18-T7'] = A['B18-L5c']
A['B18-T8'] = lantai() + jendela(200, 40, 120, 100) + hujan(200, 50, 100, 80, 7) + orang(80, tinggi=160, jenis='pria', baju='h', wajah='sedih')

# B19 — perbandingan
A['B19-1'] = lantai() + orang(110, tinggi=175, jenis='pria', baju='h') + orang(200, tinggi=110, jenis='laki', baju='a') + garis((150, 25), (240, 25), k='t') + garis((150, 90), (240, 90), k='t')
A['B19-2'] = (teks(80, 30, '臺北', 26) + termometer(80, 44, 12) + salju(40, 90, 10) + teks(128, 150, '12°', 24, angka=True)
              + teks(220, 30, '高雄', 26) + termometer(220, 44, 28) + matahari(262, 76, 12) + teks(268, 150, '28°', 24, angka=True))
A['B19-3'] = (lantai() + orang(90, tinggi=165, jenis='pria', baju='h', wajah='nyanyi', tangan={'ka': [(16, -10), (8, -30)]}) + jalur('M120 40 l40 -14 M122 52 l46 0 M120 64 l40 14', 'g', 4)
              + orang(230, tinggi=150, jenis='wanita', baju='a', wajah='sakit', tangan={'ki': [(16, -4), (0, -24)], 'ka': [(16, -4), (0, -24)]}))
A['B19-4'] = lantai() + orang(110, tinggi=175, jenis='pria', baju='a') + orang(200, tinggi=100, jenis='laki', baju='h') + panah(200, 58, 200, 84, 4) + teks(200, 50, '我', 18)
A['B19-5'] = lantai() + orang(110, tinggi=155, jenis='wanita', baju='a', tangan={'ka': [(16, -2), (-2, -24)]}) + bibir_bisik(128, 60) + orang(210, tinggi=160, jenis='pria', baju='h')

# --- B19 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def dua_termo(l1, s1, l2, s2, uk=24):
    return (teks(80, 30, l1, uk) + termometer(80, 44, s1) + teks(128, 150, f'{s1}°', 24, angka=True)
            + teks(220, 30, l2, uk) + termometer(220, 44, s2) + teks(268, 150, f'{s2}°', 24, angka=True))


def kompas(sorot=None, label='', ikon=None):
    """Arah mata angin skematis (bukan peta). sorot: '北','南','東','西' → rumah + label di arah itu.
    ikon: dict arah → svg tambahan."""
    cx, cy = 150, 105
    o = garis((cx, cy - 60), (cx, cy + 60), k='t') + garis((cx - 80, cy), (cx + 80, cy), k='t') + bulat(cx, cy, 5, 'h')
    pos = {'北': (cx, cy - 82), '南': (cx, cy + 92), '東': (cx + 104, cy + 8), '西': (cx - 104, cy + 8)}
    for k, (x, y) in pos.items():
        o += teks(x, y, k, 22)
    titik = {'北': (cx, cy - 40), '南': (cx, cy + 40), '東': (cx + 50, cy), '西': (cx - 50, cy)}
    if sorot:
        x, y = titik[sorot]
        o += bulat(x, y, 13, 'h') + teks(x + (34 if sorot in '北南' else 0), y + (6 if sorot in '北南' else -20), label, 16)
    for k, s in (ikon or {}).items():
        o += s(*titik[k])
    return o


def tas_milik(jenis, besar):
    baju = 'a' if jenis == 'wanita' else 'h'
    x = 80 if jenis == 'pria' else 220
    return orang(x - 20, tinggi=150, jenis=jenis, baju=baju) + kotak(x + 6, 200 - 30 * besar, 34 * besar, 30 * besar, 'h' if jenis == 'pria' else 'a', 6)


def kakak_adik(t1, t2):
    return lantai() + orang(100, tinggi=t1, jenis='wanita', baju='a') + orang(200, tinggi=t2, jenis='gadis' if t2 < 130 else 'wanita', baju='h') + garis((60, 200 - max(t1, t2)), (240, 200 - max(t1, t2)), k='t')


A['B19-L4a'] = lantai() + tas_milik('pria', 1.4) + tas_milik('wanita', 1.4)
A['B19-L4b'] = lantai() + tas_milik('pria', 2.0) + tas_milik('wanita', 1.0)
A['B19-L4c'] = lantai() + tas_milik('pria', 1.0) + tas_milik('wanita', 2.0)
A['B19-L5a'] = dua_termo('昨天', 30, '今天', 30)
A['B19-L5b'] = dua_termo('昨天', 32, '今天', 28)
A['B19-L5c'] = dua_termo('昨天', 30, '今天', 35)
A['B19-L6a'] = kompas('南', '高雄')
A['B19-L6b'] = kompas('北', '臺北')
A['B19-L6c'] = kompas('東')
A['B19-L8a'] = kakak_adik(165, 125)
A['B19-L8b'] = kakak_adik(155, 155)
A['B19-L8c'] = kakak_adik(140, 170)
A['B19-L9'] = dua_termo('臺北', 15, '高雄', 25)
A['B19-L10'] = ''.join(teks(45 + i * 92, 30, c, 22) + termometer(45 + i * 92, 44, s) + teks(45 + i * 92 + 40, 150, f'{s}°', 20, angka=True) for i, (c, s) in enumerate([('臺北', 15), ('臺中', 20), ('高雄', 25)]))
A['B19-T3a'] = dua_termo('臺北', 30, '高雄', 20)
A['B19-T3b'] = dua_termo('臺北', 25, '高雄', 25)
A['B19-T3c'] = dua_termo('臺北', 15, '高雄', 28)
A['B19-T4a'] = kompas('西')
A['B19-T4b'] = kompas('北')
A['B19-T4c'] = kompas('東')
sun = lambda x, y: matahari(x + 40, y, 14)
snow = lambda x, y: salju(x + 40, y, 12)
A['B19-T6a'] = kompas(ikon={'北': sun, '南': sun})
A['B19-T6b'] = kompas(ikon={'北': sun, '南': snow})
A['B19-T6c'] = kompas(ikon={'北': snow, '南': sun})
A['B19-T7'] = (bulat(150, 95, 70, 'p') + jalur('M150 25 Q105 95 150 165 M150 25 Q195 95 150 165', 'g', 2.5) + garis((150, 25), (150, 165), k='t') + garis((80, 95), (220, 95), k='t')
               + jalur('M94 60 Q150 70 206 60 M94 130 Q150 120 206 130', 'g', 2.5) + garis((150, 165), (150, 185), lebar=6) + kotak(110, 185, 80, 12, 'h', 4))
A['B19-T8'] = lantai() + tas_buka(85, 196, 0, 1.0) + tas_buka(215, 196, 0, 1.0) + teks(150, 120, '=', 40, angka=True)

# B20 — pakaian & aksesori
_cy, _r = _kepala(150, 165, 'pria')
A['B20-1'] = (lantai() + orang(150, tinggi=165, jenis='pria', baju='p', tangan={'ki': [(14, 40), (30, 74)], 'ka': [(14, 40), (30, 74)]}, badan=1.5)
              + bentuk((150 - _r * 2, _cy + _r * 1.3), (150 + _r * 2, _cy + _r * 1.3), (150 + _r * 2.8, 150), (150 - _r * 2.8, 150), k='a')
              + garis((150, _cy + _r * 1.3), (150, 150), k='t'))
_cy2, _r2 = _kepala(150, 165, 'wanita')
A['B20-2'] = orang(150, kaki=92 - 50 + 50 / .085, tinggi=50 / .085, jenis='wanita', baju='a') + kacamata_di(150, 92, 50)   # potret besar (potret() didefinisikan di bawah)
A['B20-3'] = (lantai() + garis((30, 40), (270, 40), lebar=4) + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -20), (40, -50)]})
              + bentuk((150, 50), (190, 50), (200, 170), (140, 170), k='a') + garis((170, 42), (170, 50)) + garis((170, 50), (170, 170), k='t'))
A['B20-4'] = (lantai() + orang(150, tinggi=150, jenis='wanita', baju='p', tangan={'ki': [(14, 40), (26, 76)], 'ka': [(14, 40), (26, 76)]})
              + bentuk((150 - 22, 80), (150 + 22, 80), (150 + 46, 202), (150 - 46, 202), k='a') + garis((150, 80), (150, 202), k='t'))
A['B20-5'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a') + topi_di(150, _cy2, _r2)

# --- B20 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def jaket_item(x, y, s=1.0, panjang=1.0, k='a'):
    h = 90 * s * panjang
    return (bentuk((x - 30 * s, y), (x + 30 * s, y), (x + 62 * s, y + 20 * s), (x + 70 * s, y + 80 * s * panjang), (x + 52 * s, y + 82 * s * panjang), (x + 40 * s, y + 36 * s),
                   (x + 36 * s, y + h), (x - 36 * s, y + h), (x - 40 * s, y + 36 * s), (x - 52 * s, y + 82 * s * panjang), (x - 70 * s, y + 80 * s * panjang), (x - 62 * s, y + 20 * s), k=k)
            + garis((x, y + 6 * s), (x, y + h), k='t') + jalur(f'M{f(x - 14 * s)} {f(y)} L{f(x)} {f(y + 18 * s)} L{f(x + 14 * s)} {f(y)}', 'g', 2.5))


def topi_item(x, y, s=1.0):
    return elips(x, y, 70 * s, 14 * s, 'h') + jalur(f'M{f(x - 36 * s)} {f(y - 4 * s)} Q{f(x - 38 * s)} {f(y - 56 * s)} {f(x)} {f(y - 56 * s)} Q{f(x + 38 * s)} {f(y - 56 * s)} {f(x + 36 * s)} {f(y - 4 * s)} Z', 'h')


def rok_item(x, y, s=1.0, panjang=1.0):
    return kotak(x - 30 * s, y, 60 * s, 12 * s, 'h', 3) + bentuk((x - 30 * s, y + 12 * s), (x + 30 * s, y + 12 * s), (x + 56 * s, y + 12 * s + 110 * s * panjang), (x - 56 * s, y + 12 * s + 110 * s * panjang), k='a')


def kacamata_item(x, y, s=1.0):
    return (bulat(x - 34 * s, y, 26 * s, 'p') + bulat(x + 34 * s, y, 26 * s, 'p') + garis((x - 8 * s, y - 4 * s), (x + 8 * s, y - 4 * s), lebar=5 * s)
            + garis((x - 60 * s, y - 6 * s), (x - 84 * s, y - 14 * s), lebar=5 * s) + garis((x + 60 * s, y - 6 * s), (x + 84 * s, y - 14 * s), lebar=5 * s))


def jam_item(x, y, s=1.0):
    return kotak(x - 16 * s, y - 70 * s, 32 * s, 140 * s, 'h', 8 * s) + jam_dinding(x, y, 34 * s, 10, 10)


def orang_celana(x, akhir, jenis='pria'):
    """Orang bercelana; akhir = ujung bawah celana (y). >200 = menumpuk di lantai."""
    t = sendi(x, LANTAI, 160, jenis)
    p = t['pinggang']
    o = orang(x, tinggi=160, jenis=jenis, baju='h' if jenis == 'pria' else 'a', rok=False)
    lb = t['lb']
    o += kotak(x - lb / 2 - 2, p - 4, lb + 4, min(akhir, 200) - p + 4, 'a', 3) + garis((x, p + 10), (x, min(akhir, 200)), k='t')
    if akhir > 200:
        o += elips(x - lb / 4, 199, lb * .6, 6, 'a') + elips(x + lb / 4, 199, lb * .6, 6, 'a')
    return o


def orang_jaket(x, ukuran, jenis='pria'):
    t = sendi(x, LANTAI, 160, jenis)
    b, p, lb = t['bahu'], t['pinggang'], t['lb']
    o = orang(x, tinggi=160, jenis=jenis, baju='p')
    if ukuran == 'pas':
        o += bentuk((x - lb / 2 - 4, b), (x + lb / 2 + 4, b), (x + lb / 2 + 6, p + 8), (x - lb / 2 - 6, p + 8), k='a') + garis((x, b + 4), (x, p + 8), k='t')
    elif ukuran == 'kecil':
        o += bentuk((x - lb / 2 + 2, b), (x + lb / 2 - 2, b), (x + lb / 2 - 2, p - 24), (x - lb / 2 + 2, p - 24), k='a') + garis((x, b + 4), (x, p - 24), k='t') + jalur(f'M{x - 12} {p - 30} l24 0', 't')
    else:
        o += bentuk((x - lb, b), (x + lb, b), (x + lb * 1.5, p + 50), (x - lb * 1.5, p + 50), k='a') + garis((x, b + 4), (x, p + 50), k='t')
    return o


A['B20-L4a'] = lantai() + orang_celana(150, 160)
A['B20-L4b'] = lantai() + orang_celana(150, 196)
A['B20-L4c'] = lantai() + orang_celana(150, 210)
A['B20-L5a'] = topi_item(150, 140, 1.4)
A['B20-L5b'] = jaket_item(150, 30, 1.4)
A['B20-L5c'] = rok_item(150, 30, 1.2)
A['B20-L6a'] = kacamata_item(150, 105, 1.3)
A['B20-L6b'] = jam_item(150, 105, 1.2)
A['B20-L6c'] = topi_item(150, 140, 1.4)
A['B20-L8a'] = lantai() + orang_jaket(150, 'pas')
A['B20-L8b'] = lantai() + orang_jaket(150, 'kecil')
A['B20-L8c'] = lantai() + orang_jaket(150, 'besar')
A['B20-L9'] = lantai() + matahari(260, 34, 16) + orang(110, tinggi=160, jenis='pria', baju='p', wajah='lelah', tangan={'ka': [(26, 20), (60, 24)]}) + jaket_item(200, 90, .7) + jalur('M70 40 q-6 8 0 16 M150 40 q6 8 0 16', 'g', 3)
A['B20-L10'] = lantai() + ''.join(salju(30 + (i * 61) % 240, 18 + (i * 29) % 50, 6) for i in range(7)) + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -10), (34, -30)]}) + orang(200, tinggi=100, jenis='gadis', baju='h') + topi_item(160, 90, .5)
A['B20-T3a'] = jaket_item(150, 30, 1.4)
A['B20-T3b'] = topi_item(150, 140, 1.4)
A['B20-T3c'] = kotak(120, 24, 60, 14, 'h', 3) + bentuk((120, 38), (180, 38), (196, 190), (156, 190), (150, 80), (144, 190), (104, 190), k='a')
A['B20-T4a'] = lantai() + rok_item(150, 30, 1.0, 1.4)
A['B20-T4b'] = lantai() + rok_item(150, 50, 1.0, .55)
A['B20-T4c'] = lantai() + rok_item(150, 40, 1.0, 1.0)
A['B20-T6a'] = kacamata_item(150, 70, .9) + jam_item(150, 155, .55).replace('', '')
A['B20-T6b'] = kacamata_item(150, 105, 1.2)
A['B20-T6c'] = topi_item(150, 90, 1.0) + jam_item(150, 155, .55)
A['B20-T7'] = lantai() + orang_celana(150, 150)
A['B20-T8'] = A['B20-L9']

# B21 — warna, berat (soal warna DIBERI WARNA)
A['B21-1'] = lantai() + sepatu(105, 196, 1.4, 'hijau') + sepatu(205, 196, 1.4, 'hijau')
A['B21-2'] = (jalur('M110 30 L190 30 L205 196 L160 196 L150 90 L140 196 L95 196 Z', 'biru') + garis((110, 44), (190, 44), k='t'))
A['B21-3'] = lantai() + orang(110, tinggi=160, jenis='gadis', baju='a', wajah='puas', tangan={'ka': [(20, -10), (30, -40)]}) + tas_punggung(170, 24, 1.1) + garis((148, 42), (170, 24), k='t')
A['B21-4'] = lantai() + sepatu(105, 196, 1.4, 'biru') + sepatu(205, 196, 1.4, 'biru')
A['B21-5'] = lantai() + orang(130, tinggi=150, jenis='laki', baju='a', wajah='sakit', tangan={'ka': [(14, 30), (30, 60)]}) + tas_punggung(170, 150, 1.4) + keringat(160, 50) + keringat(100, 60, .8)

# --- B21 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) — soal warna DIBERI WARNA ---
def pena_w(x, y, k, pj=150, sudut=-60):
    return (f'<g transform="rotate({sudut} {f(x)} {f(y)})">' + kotak(x - pj / 2, y - 9, pj - 26, 18, k, 4)
            + bentuk((x + pj / 2 - 26, y - 9), (x + pj / 2, y), (x + pj / 2 - 26, y + 9), k='p') + kotak(x - pj / 2 + 14, y - 13, 36, 5, 'h') + '</g>')


def rok_w(x, y, k, s=1.0):
    return kotak(x - 30 * s, y, 60 * s, 12 * s, 'h', 3) + bentuk((x - 30 * s, y + 12 * s), (x + 30 * s, y + 12 * s), (x + 56 * s, y + 122 * s), (x - 56 * s, y + 122 * s), k=k)


def celana_w(x, y, k, s=1.0):
    return jalur(f'M{f(x - 40 * s)} {f(y)} L{f(x + 40 * s)} {f(y)} L{f(x + 55 * s)} {f(y + 166 * s)} L{f(x + 10 * s)} {f(y + 166 * s)} L{f(x)} {f(y + 60 * s)} L{f(x - 10 * s)} {f(y + 166 * s)} L{f(x - 55 * s)} {f(y + 166 * s)} Z', k) + garis((x - 40 * s, y + 14 * s), (x + 40 * s, y + 14 * s), k='t')


def tas_timbang(k, kg):
    return (kotak(80, 150, 140, 40, 'p', 6) + kotak(120, 160, 60, 22, 'h', 3) + teks(150, 178, f'{kg} kg', 16, warna='#fff', angka=True)
            + kotak(105, 66, 90, 84, k, 12) + jalur('M125 66 Q125 40 150 40 Q175 40 175 66', 'g', 6) + kotak(125, 90, 50, 20, 'p', 4))


A['B21-L4a'] = pena_w(150, 105, 'kuning')
A['B21-L4b'] = pena_w(150, 105, 'hijau')
A['B21-L4c'] = pena_w(150, 105, 'biru')
A['B21-L5a'] = celana_w(150, 20, 'a')
A['B21-L5b'] = lantai() + sepatu(105, 196, 1.4, 'a') + sepatu(205, 196, 1.4, 'a')
A['B21-L5c'] = rok_w(150, 30, 'a', 1.2)
A['B21-L6a'] = tas_timbang('biru', 5)
A['B21-L6b'] = tas_timbang('biru', 1)
A['B21-L6c'] = tas_timbang('kuning', 1)
A['B21-L8a'] = rok_w(150, 30, 'kuning', 1.2)
A['B21-L8b'] = rok_w(85, 40, 'hijau', 1.0) + rok_w(215, 40, 'hijau', 1.0)
A['B21-L8c'] = rok_w(85, 40, 'kuning', 1.0) + rok_w(215, 40, 'kuning', 1.0)
A['B21-L9'] = pena_w(90, 105, 'hijau', 130, -70) + pena_w(150, 105, 'hijau', 130, -70) + pena_w(210, 105, 'hijau', 130, -70)
A['B21-L10'] = (lantai() + orang(80, tinggi=160, jenis='pria', baju='p', tangan={'ka': [(20, 10), (50, 4)]}) + kotak(126, 110, 120, 10, 'h', 3)
                + cangkir(155, 110, .8) + cangkir_kopi(215, 110, .8) + orang(270, tinggi=150, jenis='wanita', baju='a') + teks(240, 40, '?', 30, angka=True))
A['B21-T3a'] = lantai() + sepatu(105, 196, 1.4, 'hijau') + sepatu(205, 196, 1.4, 'hijau')
A['B21-T3b'] = lantai() + sepatu(105, 196, 1.4, 'kuning') + sepatu(205, 196, 1.4, 'kuning')
A['B21-T3c'] = lantai() + sepatu(105, 196, 1.4, 'biru') + sepatu(205, 196, 1.4, 'biru')
A['B21-T4a'] = celana_w(150, 20, 'biru')
A['B21-T4b'] = celana_w(150, 5, 'h', 1.15) + teks(260, 40, 'XL', 22, angka=True)
A['B21-T4c'] = celana_w(150, 30, 'h', .9) + teks(260, 40, 'S', 22, angka=True)
A['B21-T6a'] = rok_w(150, 30, 'hijau', 1.2)
A['B21-T6b'] = rok_w(150, 30, 'm', 1.2)
A['B21-T6c'] = rok_w(150, 30, 'kuning', 1.2)
A['B21-T7'] = cabai(100, 70, 3.2).replace('class="h"', 'class="m"', 1)
A['B21-T8'] = lantai() + sepatu(105, 196, 1.4, 'a') + sepatu(205, 196, 1.4, 'a')

# B22 — belanja
A['B22-1'] = lantai() + botol(80, 196, 1.3) + botol(140, 196, 1.3) + kaleng(220, 196, 1.4)
A['B22-2'] = lantai() + minimarket(150)
A['B22-3'] = lantai() + kasir(200) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 0), (46, -8)]}) + tas_belanja(150, 118, .9) + orang(250, tinggi=150, jenis='pria', baju='h')
A['B22-4'] = lantai() + kios_buah(95, 200, 150) + troli(225, 200, 1.0) + buah_apel(225, 108, .6) + buah_apel(208, 112, .5)
A['B22-5'] = lantai() + botol(115, 196, 1.5) + botol(185, 196, 1.5)

# --- B22 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kotak_telur(x, bawah, s=1.0):
    w = 100 * s
    o = kotak(x - w / 2, bawah - 30 * s, w, 30 * s, 'a', 4)
    return o + ''.join(elips(x - w / 2 + 14 * s + i * 24 * s, bawah - 34 * s, 10 * s, 12 * s, 'p') for i in range(4))


def toko_label(x, label, w=150, h=120, isi=''):
    return kotak(x - w / 2, 200 - h, w, h, 'p') + kotak(x - w / 2, 200 - h, w, 30, 'h') + teks(x, 200 - h + 22, label, 18, warna='#fff') + isi


def mal(x=150):
    o = kotak(x - 120, 40, 240, 160, 'p') + kotak(x - 120, 40, 240, 32, 'h') + teks(x, 64, '百貨公司', 20, warna='#fff')
    for r in range(2):
        for c in range(4):
            o += kotak(x - 104 + c * 54, 84 + r * 50, 44, 36, 'a', 2)
    return o + kotak(x - 24, 170, 48, 30, 'p') + garis((x, 170), (x, 200))


def supermarket(x=150):
    return (kotak(x - 120, 50, 240, 150, 'p') + kotak(x - 120, 50, 240, 30, 'h') + teks(x, 72, '超市', 20, warna='#fff')
            + kios_buah(x - 50, 200, 120).replace('', '') + troli(x + 80, 200, .8))


A['B22-L4a'] = lantai() + botol(80, 196, 1.2) + botol(150, 196, 1.2) + botol(220, 196, 1.2)
A['B22-L4b'] = lantai() + kaleng(110, 196, 1.5) + kaleng(190, 196, 1.5)
A['B22-L4c'] = lantai() + kaleng(80, 196, 1.4) + kaleng(150, 196, 1.4) + kaleng(220, 196, 1.4)
A['B22-L5a'] = lantai() + mal()
A['B22-L5b'] = lantai() + kios_buah(95, 200, 150) + troli(225, 200, 1.0)
A['B22-L5c'] = lantai() + minimarket(150)
A['B22-L6a'] = lantai() + tas_belanja(150, 196, 2.0)
A['B22-L6b'] = lantai() + tas_belanja(80, 196, 1.6) + tas_belanja(150, 196, 1.6) + tas_belanja(220, 196, 1.6)
A['B22-L6c'] = lantai() + kardus(80, 196) + kardus(150, 196) + kardus(220, 196)
A['B22-L8a'] = lantai() + kotak_telur(80, 196, .8) + kotak_telur(80, 160, .8) + botol(210, 196, 1.2)
A['B22-L8b'] = lantai() + kotak_telur(80, 196, .9) + botol(180, 196, 1.2) + botol(240, 196, 1.2)
A['B22-L8c'] = lantai() + kotak_telur(80, 196, .9) + kaleng(180, 196, 1.3) + kaleng(240, 196, 1.3)
A['B22-L9'] = lantai() + bulan_bintang(260, 30, .7) + minimarket(140)
A['B22-L10'] = (lantai() + dokter2(80, kaki=200, tinggi=160) + gelas(170, 110, 'air', .9) + cangkir_kopi(240, 110, .8) + silang(240, 80, 22, 5)
                + garis((140, 110), (270, 110), lebar=5) + panah(170, 40, 170, 62, 4))
A['B22-T3a'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (40, 0)]}) + kardus(180, 120, 60, 46)
A['B22-T3b'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(16, 30), (26, 50)]}) + kotak(100, 120, 50, 50, 'p', 6) + jalur('M110 120 q0 -16 15 -16 q15 0 15 16', 'g') + teks(125, 154, '♥', 18, angka=True)
A['B22-T3c'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (40, 0)]}) + tas_belanja(180, 120, 1.2) + kasir(250)
A['B22-T4a'] = lantai() + kios_buah(95, 200, 150) + troli(225, 200, 1.0)
A['B22-T4b'] = lantai() + mal()
A['B22-T4c'] = lantai() + minimarket(150)
A['B22-T6a'] = lantai() + botol(80, 196, 1.2) + botol(150, 196, 1.2) + botol(220, 196, 1.2)
A['B22-T6b'] = A['B22-L4c']
A['B22-T6c'] = lantai() + kardus(80, 196) + kardus(150, 196) + kardus(220, 196)
A['B22-T7'] = lantai() + mal() + label_harga(230, 6, '9999', 110, 34).replace('font-size="32"', 'font-size="20"')
A['B22-T8'] = lantai() + tas_belanja(150, 196, 2.4)

# B23 — tas & pembayaran
A['B23-1'] = lantai() + orang(130, tinggi=165, jenis='wanita', baju='a', tangan={'ka': [(12, 30), (22, 60)]}) + tas_tangan(160, 170, 1.0)
A['B23-2'] = lantai() + kasir(210) + orang(90, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 0), (46, -10)]}) + kartu_kredit(150, 62, .8)
A['B23-3'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a') + kotak(96, 60, 20, 44, 'h', 6) + tas_punggung(116, 70, .6)
A['B23-4'] = lantai() + kios_buah(150, 200, 200) + orang(150, tinggi=150, jenis='pria', baju='h', rambut='pendek').replace('class="p"', 'class="p"')
A['B23-5'] = kotak(80, 40, 140, 150, 'p', 26) + kotak(95, 55, 110, 120, 'a', 16) + dompet(150, 118, .7) + garis((80, 90), (220, 90), k='t')

# --- B23 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def uang_kertas(x, y, s=1.0):
    return kotak(x - 40 * s, y - 20 * s, 80 * s, 40 * s, 'a', 4) + bulat(x, y, 12 * s, 'p') + teks(x, y + 6 * s, '$', 16 * s, angka=True)


def ransel(isi=''):
    return (jalur('M112 40 Q112 14 150 14 Q188 14 188 40', 'g', 6) + kotak(84, 36, 132, 160, 'a', 30) + isi
            + kotak(104, 130, 92, 54, 'p', 12) + garis((104, 146), (196, 146), k='t') + garis((96, 60), (96, 180), lebar=5) + garis((204, 60), (204, 180), lebar=5))


def bayar(benda, jenis='wanita'):
    baju = 'a' if jenis == 'wanita' else 'h'
    return lantai() + kasir(220) + orang(90, tinggi=160, jenis=jenis, baju=baju, tangan={'ka': [(20, 0), (46, -10)]}) + benda


def kios_ramai(n):
    o = lantai() + kios_buah(150, 200, 200)
    for i in range(n):
        o += orang(30 + i * 60, tinggi=110, jenis='wanita' if i % 2 else 'pria', baju='a' if i % 2 else 'h')
    return o


A['B23-L4a'] = ransel(kotak(108, 50, 84, 70, 'h', 8) + dompet(150, 92, .6))
A['B23-L4b'] = tas_tangan(150, 190, 2.0, 'p') + dompet(150, 130, .6)
A['B23-L4c'] = (jalur('M110 30 L190 30 L205 196 L160 196 L150 90 L140 196 L95 196 Z', 'a') + garis((110, 44), (190, 44), k='t')
                + jalur('M114 56 Q130 80 146 56', 'g', 3) + dompet(130, 62, .4))
A['B23-L5a'] = bayar(uang_kertas(150, 64, .8))
A['B23-L5b'] = bayar(kartu_kredit(150, 62, .8))
A['B23-L5c'] = bayar(layar_ponsel(148, 64, '', .5))
A['B23-L6a'] = label_harga(150, 70, '1200', 180, 70)
A['B23-L6b'] = label_harga(150, 70, '1000', 180, 70)
A['B23-L6c'] = label_harga(150, 70, '200', 180, 70)
A['B23-L8a'] = lantai() + kasir(150) + orang(80, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(20, -4), (44, -10)]}) + orang(240, tinggi=150, jenis='wanita', baju='a') + tas_belanja(150, 92, .9) + panah(170, 60, 205, 60, 3)
A['B23-L8b'] = lantai() + kasir(150) + orang(80, tinggi=150, jenis='pria', baju='h') + orang(240, tinggi=150, jenis='wanita', baju='a', tangan={'ki': [(20, -4), (44, -10)]}) + uang_kertas(160, 76, .6) + panah(130, 50, 95, 50, 3)
A['B23-L8c'] = lantai() + kasir(150) + orang(80, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(20, -4), (44, -10)]}) + orang(240, tinggi=150, jenis='wanita', baju='a') + kardus(150, 92, 50, 40) + panah(170, 60, 205, 60, 3)
A['B23-L9'] = kios_ramai(5)
A['B23-L10'] = bayar(kartu_kredit(150, 62, .8), 'pria') + teks(150, 30, '?', 26, angka=True)
A['B23-T3a'] = bayar(uang_kertas(150, 64, .8))
A['B23-T3b'] = bayar(kartu_kredit(150, 62, .8))
A['B23-T3c'] = bayar(layar_ponsel(148, 64, '', .5))
A['B23-T4a'] = uang_kertas(150, 105, 2.4).replace('>$<', '>$1000<') if False else kotak(50, 60, 200, 90, 'a', 6) + teks(150, 120, '$1000', 40, angka=True)
A['B23-T4b'] = kotak(50, 60, 200, 90, 'a', 6) + teks(150, 120, '$200', 40, angka=True)
A['B23-T4c'] = kotak(50, 60, 200, 90, 'a', 6) + teks(150, 120, '$800', 40, angka=True)
A['B23-T6a'] = lantai() + toko(150) + kotak(110, 90, 80, 30, 'p', 4) + teks(150, 112, 'CLOSED', 15, angka=True)
A['B23-T6b'] = kios_ramai(5)
A['B23-T6c'] = lantai() + kios_buah(150, 200, 200) + orang(150, tinggi=150, jenis='pria', baju='h', wajah='lelah')
A['B23-T7'] = ransel()
A['B23-T8'] = bayar(kartu_kredit(150, 62, .8))

# B24 — makanan
A['B24-1'] = lantai() + es_krim(95, 196, 1.2) + piring(205, 190, 60, potong_kue(205, 186, .9))
A['B24-2'] = (lantai() + meja(150, 150, 240) + piring(200, 144, 50, cabai(185, 128, .7) + cabai(200, 134, .6)) + orang(95, tinggi=150, jenis='pria', baju='a', wajah='sakit')
              + keringat(120, 40) + jalur('M84 70 l-12 10 M94 76 l-2 14 M104 70 l10 10', 'g'))
A['B24-3'] = lantai() + es_krim(150, 196, 1.6)
A['B24-4'] = lantai() + meja(150, 150, 240) + mangkuk_mi(190, 120, .4, sumpit=False) + garam(240, 110, .8) + orang(90, tinggi=150, jenis='wanita', baju='a', wajah='sakit')
A['B24-5'] = lantai() + meja(150, 150, 240) + piring(100, 144, 50, potong_kue(100, 140, .75)) + cangkir_kopi(200, 146, .9) + biji_kopi(258, 134) + biji_kopi(272, 142, .8)



# ---------------- B25–B36 ----------------
MASAK = {'ka': [(22, 10), (50, 4)]}


def burung(x, y, arah=1, s=1.0):
    a = arah
    return (elips(x, y, 18 * s, 11 * s, 'a') + bulat(x + a * 16 * s, y - 8 * s, 8 * s, 'a') + bentuk((x + a * 23 * s, y - 9 * s), (x + a * 32 * s, y - 6 * s), (x + a * 23 * s, y - 4 * s), k='h')
            + bulat(x + a * 18 * s, y - 10 * s, 1.8 * s, 'h') + bentuk((x - a * 14 * s, y), (x - a * 30 * s, y - 8 * s), (x - a * 28 * s, y + 4 * s), k='h')
            + jalur(f'M{f(x - a * 4 * s)} {f(y - 2 * s)} q{f(-a * 8 * s)} {f(-14 * s)} {f(-a * 18 * s)} {f(-10 * s)}', 'g') + garis((x, y + 10 * s), (x, y + 18 * s), k='t'))

# --- B24 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def lemon(x, y, s=1.0):
    return elips(x, y, 30 * s, 20 * s, 'p') + elips(x, y, 22 * s, 13 * s, 'a') + garis((x - 22 * s, y), (x + 22 * s, y), k='t') + garis((x, y - 13 * s), (x, y + 13 * s), k='t')


def gula(x, bawah, s=1.0):
    return kotak(x - 24 * s, bawah - 50 * s, 48 * s, 50 * s, 'p', 4) + teks(x, bawah - 18 * s, '糖', 20 * s) + kotak(x - 12 * s, bawah - 62 * s, 12 * s, 12 * s, 'p', 1) + kotak(x + 2 * s, bawah - 70 * s, 12 * s, 12 * s, 'p', 1)


def cicip(rasa, wajah='sakit'):
    o = lantai() + meja(150, 150, 240) + mangkuk_mi(180, 120, .4, sumpit=False) + orang(80, tinggi=150, jenis='wanita', baju='a', wajah=wajah)
    return o + {'asam': lemon(245, 128, .9), 'pedas': cabai(230, 120, .8), 'asin': garam(245, 150, .8)}[rasa]


def kue(x, bawah, s=1.0):
    return piring(x, bawah, 50 * s, potong_kue(x, bawah - 4 * s, .8 * s))


A['B24-L4a'] = lantai() + kue(95, 190, 1.1) + es_krim(210, 196, 1.2)
A['B24-L4b'] = lantai() + kue(60, 190, .9) + kue(150, 190, .9) + es_krim(240, 196, 1.1)
A['B24-L4c'] = lantai() + kue(80, 190, 1.0) + es_krim(180, 196, 1.1) + es_krim(250, 196, 1.1)
A['B24-L5a'] = cicip('asam')
A['B24-L5b'] = cicip('pedas')
A['B24-L5c'] = cicip('asin')
A['B24-L6a'] = lantai() + kue(150, 190, 1.6)
A['B24-L6b'] = lantai() + es_krim(150, 196, 1.6)
A['B24-L6c'] = lantai() + piring(150, 170, 80, cabai(120, 150, 1.0) + cabai(150, 156, .9) + cabai(175, 146, .8))
A['B24-L8a'] = lantai() + meja(150, 150, 220) + cangkir_kopi(110, 146, 1.0) + kue(200, 146, .9)
A['B24-L8b'] = lantai() + meja(150, 150, 220) + cangkir(110, 146, 1.0) + jalur('M96 116 l0 -14 l8 0', 'g', 2) + kotak(98, 96, 14, 10, 'p', 1) + kue(200, 146, .9)
A['B24-L8c'] = lantai() + meja(150, 150, 220) + cangkir_kopi(150, 146, 1.1)
A['B24-L9'] = (lantai() + meja(200, 150, 140) + piring(200, 140, 50, kotak(176, 116, 22, 18, 'a', 3) + kotak(202, 116, 22, 18, 'a', 3))
               + jalur('M190 100 q-6 -12 0 -24 q6 -12 0 -24 M210 100 q6 -12 0 -24 q-6 -12 0 -24', 'g', 3)
               + orang(80, tinggi=160, jenis='pria', baju='h', wajah='sakit', tangan={'ka': [(12, -10), (2, -34)]}))
A['B24-L10'] = lantai() + es_krim(150, 196, 1.7) + bintang(220, 50, 8) + bintang(80, 70, 6)
A['B24-T3a'] = lemon(150, 105, 2.4)
A['B24-T3b'] = lantai() + kue(150, 190, 1.6)
A['B24-T3c'] = cabai(90, 70, 3.0)
A['B24-T4a'] = lantai() + kue(150, 190, 1.6) + jalur('M130 90 q-6 -12 0 -24 M150 90 q-6 -12 0 -24 M170 90 q-6 -12 0 -24', 'g', 3)
A['B24-T4b'] = lantai() + garam(150, 196, 2.2)
A['B24-T4c'] = cabai(90, 70, 3.0)
A['B24-T6a'] = lantai() + es_krim(150, 196, 1.0)
A['B24-T6b'] = lantai() + es_krim(150, 196, 1.7)
A['B24-T6c'] = lemon(150, 105, 2.4)
A['B24-T7'] = cabai(90, 70, 3.0)
A['B24-T8'] = lantai() + gula(150, 196, 2.2)

# B25 — memasak & alat makan
A['B25-1'] = lantai() + kompor(185, 130) + api(185, 128, .8) + wajan(185, 112, 1.0) + orang(80, tinggi=160, jenis='pria', baju='a', tangan=MASAK)
A['B25-2'] = lantai() + panggangan(185, 110) + daging(160, 104, .6) + daging(210, 104, .55) + api(185, 120, .6) + orang(70, tinggi=160, jenis='pria', baju='h', tangan=MASAK)
A['B25-3'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, 6), (48, -2)]}) + sendok(190, 86, 120, -20)
A['B25-4'] = lantai() + kompor(190, 140) + api(190, 138, .8) + panci_goreng(190, 90, 120) + paha_ayam(175, 80, .8) + orang(80, tinggi=160, jenis='wanita', baju='h', tangan=MASAK)
A['B25-5'] = garpu(150, 110, 170, -25)

# --- B25 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def sayur(x, y, s=1.0):
    return ''.join(jalur(f'M{f(x + dx * s)} {f(y)} q{f(-14 * s)} {f(-20 * s)} {f(2 * s)} {f(-34 * s)} q{f(14 * s)} {f(14 * s)} {f(-2 * s)} {f(34 * s)} Z', 'a') for dx in (-24, -8, 8, 24))


def piring_isi(isi, rx=80):
    return lantai() + meja(150, 170, 240) + piring(150, 160, rx, isi)


def atas(ki, ka):
    return bulat(150, 105, 70, 'p') + bulat(150, 105, 50, 't') + ki + ka


def gelas_es(x, bawah, s=1.0):
    return (jalur(f'M{f(x - 30 * s)} {f(bawah - 90 * s)} L{f(x - 24 * s)} {f(bawah)} L{f(x + 24 * s)} {f(bawah)} L{f(x + 30 * s)} {f(bawah - 90 * s)}', 'g', 3)
            + jalur(f'M{f(x - 28 * s)} {f(bawah - 70 * s)} L{f(x + 28 * s)} {f(bawah - 70 * s)}', 't')
            + ''.join(kotak(x + dx * s, bawah + dy * s, 16 * s, 16 * s, 'p', 3) for dx, dy in ((-20, -60), (2, -52), (-12, -38), (6, -28))))


A['B25-L4a'] = garpu(150, 110, 170, -25)
A['B25-L4b'] = pisau(150, 110, 180, -25)
A['B25-L4c'] = sendok(150, 110, 170, -25)
A['B25-L5a'] = lantai() + kompor(190, 140) + api(190, 138, .8) + panci_goreng(190, 90, 120) + ikan(190, 82, .6) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan=MASAK)
A['B25-L5b'] = lantai() + panggangan(185, 110) + ikan(185, 100, .7) + api(185, 120, .6) + orang(70, tinggi=160, jenis='wanita', baju='a', tangan=MASAK)
A['B25-L5c'] = lantai() + kompor(185, 130) + api(185, 128, .8) + wajan(185, 112, 1.0) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan=MASAK)
A['B25-L6a'] = lantai() + meja(150, 170, 200) + mangkuk_mi(150, 140, .55, sumpit=False)
A['B25-L6b'] = lantai() + meja(150, 170, 200) + cangkir(150, 166, 1.3)
A['B25-L6c'] = lantai() + meja(150, 170, 200) + gelas_es(150, 166, 1.1)
A['B25-L8a'] = atas(sendok(55, 105, 150, -90), garpu(245, 105, 150, -90))
A['B25-L8b'] = atas('', pisau(245, 105, 160, -90))
A['B25-L8c'] = atas(garpu(55, 105, 150, -90), pisau(245, 105, 160, -90))
A['B25-L9'] = lantai() + meja(150, 170, 200) + gelas_es(150, 166, 1.3)
A['B25-L10'] = lantai() + kotak(60, 120, 180, 50, 'p', 6) + sayur(150, 118, 1.3) + bintang(90, 70, 7) + bintang(210, 60, 8) + bintang(170, 40, 5) + ''.join(garis((110 + i * 30, 40), (106 + i * 30, 60), lebar=2.4) for i in range(3))
A['B25-T3a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='lelah') + teks(200, 50, 'z z', 20, angka=True)
A['B25-T3b'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='lapar', tangan={'ka': [(14, 30), (-4, 40)]})
A['B25-T3c'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(14, 30), (-4, 40)]}) + piring(240, 190, 40)
A['B25-T4a'] = lantai() + panggangan(185, 110) + daging(160, 104, .6) + daging(210, 104, .55) + api(185, 120, .6) + orang(70, tinggi=160, jenis='pria', baju='h', tangan=MASAK)
A['B25-T4b'] = lantai() + kompor(185, 130) + api(185, 128, .8) + wajan(185, 112, 1.0) + orang(80, tinggi=160, jenis='pria', baju='h', tangan=MASAK)
A['B25-T4c'] = lantai() + kompor(190, 140) + api(190, 138, .8) + panci_goreng(190, 90, 120) + paha_ayam(175, 80, .8) + orang(80, tinggi=160, jenis='pria', baju='h', tangan=MASAK)
A['B25-T6a'] = piring_isi(sayur(150, 150, 1.2))
A['B25-T6b'] = piring_isi(daging(130, 150, .7) + daging(175, 150, .6))
A['B25-T6c'] = piring_isi(kotak(100, 128, 50, 26, 'a', 6) + jalur('M104 136 l40 0 M104 144 l40 0', 't') + telur_ceplok(190, 142, .8))
A['B25-T7'] = pisau(150, 110, 180, -25)
A['B25-T8'] = lantai() + meja(150, 170, 200) + gelas_es(150, 166, 1.3)

# B26 — minuman & buah
A['B26-1'] = lantai() + gelas_isi(110, 196, 1.6, 'a', True) + buah_apel(210, 190, 1.4)
A['B26-2'] = lantai() + orang(120, tinggi=165, jenis='pria', baju='a', wajah='puas', tangan={'ka': [(14, 26), (-4, -6)]}) + kaleng_soda(148, 70, .8) + keringat(96, 40)
A['B26-3'] = lantai() + matahari(240, 50, 20) + semangka(130, 110, 1.3)
A['B26-4'] = lantai() + cangkir(150, 190, 1.8, True) + elips(150, 190 - 72, 36, 6, 'a') + kantong_teh(172, 120)
A['B26-5'] = pisang(150, 120, 1.6)

# --- B26 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def gelas_label(x, bawah, s, k, label=''):
    return gelas_isi(x, bawah, s, k, True) + (teks(x, bawah - 30 * s, label, 14 * s) if label else '')


def kotak_susu(x, bawah, s=1.0):
    return (kotak(x - 22 * s, bawah - 70 * s, 44 * s, 70 * s, 'p', 3) + bentuk((x - 22 * s, bawah - 70 * s), (x, bawah - 88 * s), (x + 22 * s, bawah - 70 * s), k='p')
            + teks(x, bawah - 28 * s, '牛奶', 13 * s))


def bir(x, bawah, s=1.0):
    return (kotak(x - 26 * s, bawah - 90 * s, 52 * s, 90 * s, 'a', 6) + jalur(f'M{f(x + 26 * s)} {f(bawah - 70 * s)} q{f(24 * s)} 0 {f(24 * s)} {f(25 * s)} q0 {f(25 * s)} {f(-24 * s)} {f(25 * s)}', 'g', 5 * s)
            + jalur(f'M{f(x - 30 * s)} {f(bawah - 88 * s)} q{f(10 * s)} {f(-16 * s)} {f(20 * s)} {f(-4 * s)} q{f(10 * s)} {f(-14 * s)} {f(20 * s)} {f(-2 * s)} q{f(10 * s)} {f(-12 * s)} {f(20 * s)} {f(2 * s)} Z', 'p'))


A['B26-L4a'] = lantai() + gelas_label(130, 196, 2.0, 'h') + kantong_teh(235, 150)
A['B26-L4b'] = lantai() + gelas_label(130, 196, 2.0, 'a') + kotak_susu(240, 196)
A['B26-L4c'] = lantai() + gelas_label(130, 196, 1.1, 'a') + kotak_susu(240, 196)
A['B26-L5a'] = lantai() + buah_apel(150, 150, 2.4)
A['B26-L5b'] = pisang(150, 120, 1.6)
A['B26-L5c'] = lantai() + semangka(150, 110, 1.4)
A['B26-L6a'] = lantai() + gelas_isi(150, 196, 1.8, 'a', True) + buah_apel(230, 190, .9)
A['B26-L6b'] = lantai() + kaleng_soda(150, 196, 1.8)
A['B26-L6c'] = lantai() + bir(140, 196, 1.4)
A['B26-L8a'] = lantai() + buah_apel(60, 190, 1.0) + buah_apel(120, 190, 1.0) + semangka(220, 150, .8)
A['B26-L8b'] = lantai() + buah_apel(60, 190, 1.0) + semangka(150, 150, .7) + semangka(240, 150, .7)
A['B26-L8c'] = lantai() + pisang(80, 160, .8) + pisang(80, 120, .8) + semangka(220, 150, .8)
A['B26-L9'] = lantai() + orang(110, tinggi=165, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(14, 26), (-4, -6)]}) + kaleng_soda(138, 70, .8) + bintang(190, 40, 8) + bintang(215, 70, 6)
A['B26-L10'] = lantai() + orang(90, tinggi=185, jenis='pria', baju='h') + orang(210, tinggi=140, jenis='wanita', baju='a') + garis((50, 15), (130, 15), k='t') + teks(250, 40, '?', 30, angka=True)
A['B26-T3a'] = A['B26-L6a']
A['B26-T3b'] = lantai() + cangkir_kopi(150, 190, 1.6)
A['B26-T3c'] = A['B26-L6c']
A['B26-T4a'] = A['B26-L6c']
A['B26-T4b'] = lantai() + kaleng_soda(100, 196, .8) + gelas_isi(190, 196, 2.0, 'h', True)
A['B26-T4c'] = lantai() + kaleng_soda(100, 196, .8) + gelas_isi(190, 196, 1.0, 'h', True)
A['B26-T6a'] = lantai() + buah_apel(150, 150, 2.4)
A['B26-T6b'] = pisang(80, 120, 1.0) + pisang(150, 140, 1.0) + pisang(220, 120, 1.0)
A['B26-T6c'] = lantai() + buah_apel(70, 180, 1.4) + buah_apel(150, 180, 1.4) + buah_apel(230, 180, 1.4)
A['B26-T7'] = lantai() + gelas_isi(150, 196, 2.0, 'a', True)
A['B26-T8'] = lantai() + botol_obat(110, 196, 1.6) + sendok(210, 150, 110, -10) + orang(250, tinggi=110, jenis='laki', baju='h', wajah='sakit')

# B27 — jajanan
A['B27-1'] = piring(150, 160, 120, pangsit(100, 152, 1.1) + pangsit(150, 150, 1.1) + pangsit(200, 152, 1.1) + pangsit(125, 136, 1.0) + pangsit(175, 136, 1.0))
A['B27-2'] = lantai(196, 60, 240) + hamburger(150, 180, 1.3)
_nightm = (lantai() + bulan_bintang(250, 30, .5) + garis((20, 60), (280, 60), k='t') + ''.join(lampion(40 + i * 44, 72, .7) for i in range(6))
           + kotak(20, 130, 110, 70, 'a') + kotak(170, 130, 110, 70, 'a') + kotak(14, 118, 122, 14, 'h') + kotak(164, 118, 122, 14, 'h'))
A['B27-3'] = _nightm + orang(150, tinggi=112, jenis='wanita', baju='p')
A['B27-4'] = _nightm + orang(130, tinggi=110, jenis='wanita', baju='p', tangan={'ka': [(12, 20), (-4, -2)]}) + orang(175, tinggi=116, jenis='pria', baju='h')
A['B27-5'] = lantai() + meja(150, 150, 240) + piring(190, 144, 56, mangkuk_mi(190, 120, .3, sumpit=False)) + orang(90, tinggi=150, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(16, -4), (26, -30)]}) + jempol(130, 64, 1.0)

# --- B27 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def mantou(x, bawah, s=1.0):
    return jalur(f'M{f(x - 30 * s)} {f(bawah)} Q{f(x - 34 * s)} {f(bawah - 42 * s)} {f(x)} {f(bawah - 44 * s)} Q{f(x + 34 * s)} {f(bawah - 42 * s)} {f(x + 30 * s)} {f(bawah)} Z', 'p') + garis((x - 30 * s, bawah), (x + 30 * s, bawah))


def hotdog(x, y, s=1.0):
    return (kotak(x - 74 * s, y - 10 * s, 148 * s, 22 * s, 'h', 11 * s)
            + jalur(f'M{f(x - 62 * s)} {f(y)} Q{f(x - 64 * s)} {f(y + 30 * s)} {f(x - 40 * s)} {f(y + 30 * s)} L{f(x + 40 * s)} {f(y + 30 * s)} Q{f(x + 64 * s)} {f(y + 30 * s)} {f(x + 62 * s)} {f(y)} Z', 'a')
            + jalur(f'M{f(x - 50 * s)} {f(y - 12 * s)} q{f(10 * s)} {f(-8 * s)} {f(20 * s)} 0 q{f(10 * s)} {f(8 * s)} {f(20 * s)} 0 q{f(10 * s)} {f(-8 * s)} {f(20 * s)} 0 q{f(10 * s)} {f(8 * s)} {f(20 * s)} 0 q{f(10 * s)} {f(-8 * s)} {f(20 * s)} 0', 'g', 3))


def sandwich(x, y, s=1.0):
    return (bentuk((x - 64 * s, y + 20 * s), (x + 64 * s, y + 20 * s), (x, y - 70 * s), k='p')
            + bentuk((x - 50 * s, y + 6 * s), (x + 50 * s, y + 6 * s), (x, y - 56 * s), k='a')
            + bentuk((x - 40 * s, y - 2 * s), (x + 40 * s, y - 2 * s), (x, y - 46 * s), k='p'))


def porsi(x, n=4, s=.8):
    return piring(x, 160, 60 * s / .8, ''.join(pangsit(x - 26 * s + (i % 3) * 26 * s, 152 - (i // 3) * 14, s) for i in range(n)))


A['B27-L4a'] = lantai() + mantou(100, 190, 1.4) + mantou(200, 190, 1.4)
A['B27-L4b'] = lantai() + mantou(60, 190, 1.2) + mantou(150, 190, 1.2) + mantou(240, 190, 1.2)
A['B27-L4c'] = lantai() + pangsit(70, 170, 1.5) + pangsit(150, 170, 1.5) + pangsit(230, 170, 1.5)
A['B27-L5a'] = _nightm
A['B27-L5b'] = lantai() + kios_buah(95, 200, 150) + troli(225, 200, 1.0)
A['B27-L5c'] = lantai() + bioskop(150)
A['B27-L6a'] = _nightm + meja(110, 165, 130) + porsi(110, 4, .6).replace('160', '158') + orang(210, tinggi=130, jenis='wanita', baju='p', duduk=170)
A['B27-L6b'] = lantai() + rumah(110, lebar=150, t=100) + porsi(240, 4, .6)
A['B27-L6c'] = lantai() + gedung(90, tingkat=6, lebar=90) + kotak(150, 40, 60, 24, 'p', 3) + teks(180, 58, '公司', 16) + orang(230, tinggi=150, jenis='wanita', baju='a', duduk=None) + tas_belanja(260, 160, .8)
A['B27-L8a'] = lantai() + porsi(80) + hotdog(200, 150, .7) + hotdog(200, 110, .7)
A['B27-L8b'] = lantai() + porsi(70, 4, .7) + porsi(160, 4, .7) + hamburger(250, 190, .7)
A['B27-L8c'] = lantai() + porsi(70, 4, .7) + porsi(160, 4, .7) + hotdog(250, 150, .55)
A['B27-L9'] = lantai() + kios_buah(200, 200, 150) + orang(70, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(16, 30), (24, 40)]}) + tas_belanja(96, 150, .9) + matahari(270, 30, 14)
A['B27-L10'] = (lantai() + kotak(10, 80, 90, 120, 'p') + kotak(10, 80, 90, 24, 'h') + teks(55, 98, '饅頭', 14, warna='#fff')
                + orang(130, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(16, 30), (24, 40)]}) + tas_belanja(156, 150, .8) + panah(170, 120, 210, 120, 4) + sekolah_b(255, 80))
A['B27-T3a'] = lantai(196, 60, 240) + hamburger(150, 180, 1.3)
A['B27-T3b'] = sandwich(150, 140, 1.4)
A['B27-T3c'] = hotdog(150, 120, 1.6)
A['B27-T4a'] = hotdog(150, 120, 1.6)
A['B27-T4b'] = lantai(196, 60, 240) + hamburger(150, 180, 1.3)
A['B27-T4c'] = A['B27-1']
A['B27-T6a'] = lantai() + mantou(150, 190, 2.0)
A['B27-T6b'] = A['B27-L4a']
A['B27-T6c'] = lantai() + pangsit(100, 170, 1.8) + pangsit(200, 170, 1.8)
A['B27-T7'] = lantai(196, 60, 240) + hamburger(150, 180, 1.3)
A['B27-T8'] = lantai() + orang(220, tinggi=120, jenis='pria', baju='h') + panah(200, 150, 120, 150, 4) + orang(60, tinggi=170, jenis='wanita', baju='a') + teks(60, 14, '我', 16)

# B28 — restoran & kedai teh
A['B28-2'] = lantai() + meja(150, 150, 240) + orang(80, tinggi=150, jenis='wanita', baju='a', duduk=156, tangan={'ka': [(20, -6), (40, -16)]}) + orang(225, tinggi=165, jenis='pria', baju='h', tangan={'ki': [(16, 10), (34, 14)]}) + buku_menu(175, 110, .9)
A['B28-3'] = lantai() + kedai_teh(150)
A['B28-4'] = (lantai() + kotak(150, 50, 134, 150, 'p') + kotak(186, 100, 56, 100, 'h') + ''.join(bintang(172 + i * 24, 70, 9) for i in range(4))
              + orang(40, tinggi=140, jenis='wanita', baju='a') + orang(80, tinggi=150, jenis='pria', baju='h') + orang(118, tinggi=145, jenis='wanita', baju='p'))
A['B28-5'] = (kotak(20, 16, 260, 188, 'p') + lampion(60, 50, .8) + lampion(240, 50, .8) + meja(150, 150, 200) + teko(150, 146, .5) + cangkir(100, 146, .4, False) + cangkir(200, 146, .4, False)
              + orang(60, tinggi=130, jenis='wanita', baju='a', duduk=160) + orang(240, tinggi=135, jenis='pria', baju='h', duduk=160))

# --- B28 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def resto(x, label='餐廳', w=130, h=120):
    return kotak(x - w / 2, 200 - h, w, h, 'p') + kotak(x - w / 2, 200 - h, w, 28, 'h') + teks(x, 200 - h + 21, label, 16, warna='#fff') + pintu(x, 200, 56, 34) + jendela(x - w / 2 + 24, 200 - h + 40, 30, 24) + jendela(x + w / 2 - 24, 200 - h + 40, 30, 24)


def antre(x0, n, dx=26):
    return ''.join(orang(x0 + i * dx, tinggi=90, jenis='wanita' if i % 2 else 'pria', baju='a' if i % 2 else 'h') for i in range(n))


def pikir(isi):
    return lantai() + orang(70, tinggi=160, jenis='wanita', baju='a') + gelembung_pikiran(195, 70, 150, 100, isi, 110, 110)


def mi(x, y, s=1.0):
    return mangkuk_mi(x, y, s, sumpit=False)


def nasi_goreng(x, y, s=1.0):
    return piring(x, y + 20 * s, 50 * s, jalur(f'M{f(x - 34 * s)} {f(y + 14 * s)} Q{f(x)} {f(y - 30 * s)} {f(x + 34 * s)} {f(y + 14 * s)} Z', 'a') + ''.join(bulat(x + dx * s, y + dy * s, 2.5 * s, 'h') for dx, dy in ((-14, 4), (0, -6), (12, 6), (6, -14))))


A['B28-1'] = lantai() + gedung(170, tingkat=6, lebar=130) + kotak(115, 14, 110, 24, 'h') + teks(170, 32, '飯店', 16, warna='#fff') + orang(50, tinggi=140, jenis='pria', baju='h') + koper(80, 200, .8) + orang(270, tinggi=130, jenis='wanita', baju='a') + koper(245, 200, .7)
A['B28-L4a'] = lantai() + mi(150, 120, .7)
A['B28-L4b'] = lantai() + mi(80, 120, .55) + teks(150, 130, '/', 40, angka=True) + nasi_goreng(225, 120, 1.0)
A['B28-L4c'] = A['B27-1']
A['B28-L5a'] = lantai() + resto(150)
A['B28-L5b'] = lantai() + gedung(150, tingkat=6, lebar=130) + kotak(95, 14, 110, 24, 'h') + teks(150, 32, '飯店', 16, warna='#fff')
A['B28-L5c'] = lantai() + kedai_teh(150)
A['B28-L6a'] = lantai() + resto(80, '餐廳', 120, 110) + resto(225, '餐廳', 120, 110) + antre(30, 4, 30).replace('', '') if False else lantai() + resto(70, '餐廳', 120, 110) + resto(225, '餐廳', 120, 110) + antre(150, 1) + panah(225, 30, 225, 70, 5) + orang(200, tinggi=90, jenis='pria', baju='h') + orang(250, tinggi=86, jenis='wanita', baju='a')
A['B28-L6b'] = lantai() + resto(170, '餐廳', 150, 120) + ''.join(bintang(120 + i * 30, 66, 7) for i in range(4)) + antre(20, 6, 26) + panah(170, 20, 170, 56, 5)
A['B28-L6c'] = lantai() + rumah(150, lebar=150, t=100)
A['B28-L8a'] = pikir(mi(195, 76, .45))
A['B28-L8b'] = pikir(mi(160, 76, .32) + pangsit(235, 80, .9))
A['B28-L8c'] = pikir(hamburger(195, 100, .6))
A['B28-L9'] = lantai() + resto(200, '餐廳', 150, 120) + antre(20, 5, 26)
A['B28-L10'] = lantai() + kedai_teh(200, w=170) + orang(40, tinggi=150, jenis='wanita', baju='a', wajah='nyanyi', tangan={'ka': [(20, -10), (40, -30)]}) + orang(90, tinggi=155, jenis='pria', baju='h') + teks(70, 30, '?', 26, angka=True)
A['B28-T3a'] = lantai() + resto(150, '麵店')
A['B28-T3b'] = A['B28-L5b']
A['B28-T3c'] = A['B28-L5c']
A['B28-T4a'] = lantai(196, 60, 240) + hamburger(150, 180, 1.3)
A['B28-T4b'] = lantai() + mi(150, 120, .7)
A['B28-T4c'] = A['B27-1']
A['B28-T6a'] = lantai() + orang_ponsel(150, 'pria', 155, baju='h')
A['B28-T6b'] = lantai() + meja(150, 150, 200) + orang(90, tinggi=150, jenis='pria', baju='h', duduk=156, tangan={'ka': [(20, -6), (40, -16)]}) + kotak(126, 70, 50, 64, 'p', 3) + teks(151, 96, '菜單', 13) + garis((134, 110), (168, 110), k='t') + garis((134, 120), (168, 120), k='t')
A['B28-T6c'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='pria', duduk=150, baju='a', tangan={'ki': [(20, 0), (30, -20)], 'ka': [(20, 0), (30, -20)]}) + koran(150, 60, 150, 90)
A['B28-T7'] = kertas(150, 105, 190, 180, 0) + teks(150, 44, '特別餐', 20) + mi(110, 92, .3) + pangsit(190, 92, .9) + nasi_goreng(150, 140, .7)
A['B28-T8'] = lantai() + kedai_teh(150)

# B29 — jarak
A['B29-1'] = lantai() + rumah(95) + pohon(200) + pohon(250, s=.8) + bangku(225)
A['B29-2'] = rumah(50, 200, 70, 50) + jalan_panjang(70, 196, 230, 60) + sekolah(245, 90, 70, 50)
A['B29-3'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='a', tangan={'ki': [(10, 24), (30, 10)], 'ka': [(10, 24), (30, 10)]}) + peta(110, 92, 120, 70)
A['B29-4'] = lantai() + stasiun(210, 200, 130, 90) + orang(95, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -6), (46, -14)]})
A['B29-5'] = lantai() + rumah(80, 200, 110, 80) + jalan_kaki(210, 'pria', 150, 'h') + koper(250, 196, .8)

# --- B29 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def bld(x, label, w=110, h=90, lantai_y=200, s=1.0):
    w, h = w * s, h * s
    return (kotak(x - w / 2, lantai_y - h, w, h, 'p') + kotak(x - w / 2, lantai_y - h, w, 22 * s, 'h') + teks(x, lantai_y - h + 16 * s, label, 14 * s, warna='#fff')
            + kotak(x - 14 * s, lantai_y - 40 * s, 28 * s, 40 * s, 'a') + jendela(x - w / 2 + 20 * s, lantai_y - h + 34 * s, 22 * s, 18 * s) + jendela(x + w / 2 - 20 * s, lantai_y - h + 34 * s, 22 * s, 18 * s))


def jalan_raya(y=150, h=40, zebra_x=None):
    o = kotak(0, y, 300, h, 'a') + ''.join(kotak(10 + i * 50, y + h / 2 - 2, 26, 4, 'p') for i in range(6))
    if zebra_x:
        o += kotak(zebra_x - 26, y, 52, h, 'a') + ''.join(kotak(zebra_x - 24 + i * 12, y + 2, 7, h - 4, 'p') for i in range(4))
    return o


def jauh(label):
    return rumah(50, 200, 70, 50) + jalan_panjang(70, 196, 230, 70) + bld(240, label, 80, 60, 74, 1.0)


def dari(tempat):
    return lantai() + tempat + panah(140, 140, 200, 140, 5) + orang(250, tinggi=140, jenis='wanita', baju='a')


def toko_buku_kecil(x, y):
    return kotak(x - 40, y, 80, 60, 'p') + kotak(x - 40, y, 80, 20, 'h') + teks(x, y + 15, '書店', 14, warna='#fff')


def sisi_ini(jenis='wanita'):
    return lantai() + jalan_raya(165, 35) + toko_buku_kecil(235, 103) + orang(60, kaki=163, tinggi=120, jenis=jenis, baju='a' if jenis == 'wanita' else 'h') + panah(90, 120, 185, 120, 4)


def seberang(jenis='wanita'):
    return lantai() + toko_buku_kecil(235, 8) + jalan_raya(70, 50, 150) + orang(110, kaki=200, tinggi=70, jenis=jenis, baju='a' if jenis == 'wanita' else 'h') + panah(130, 150, 150, 126, 4)


A['B29-L4a'] = lantai() + rumah(80, 200, 100, 80) + bld(215, '車站')
A['B29-L4b'] = jauh('車站')
A['B29-L4c'] = lantai() + rumah(80, 200, 100, 80) + bld(215, '學校')
A['B29-L5a'] = dari(bld(70, '學校'))
A['B29-L5b'] = dari(bld(70, '車站'))
A['B29-L5c'] = dari(rumah(70, 200, 100, 80))
A['B29-L6a'] = sisi_ini()
A['B29-L6b'] = lantai() + bus(150, w=220) + orang(30, tinggi=110, jenis='wanita', baju='a')
A['B29-L6c'] = seberang()
A['B29-L8a'] = lantai() + rumah(60, 200, 90, 70) + pohon(150, s=.9) + jalan_panjang(170, 196, 260, 110) + bld(268, '學校', 50, 40, 110)
A['B29-L8b'] = lantai() + rumah(60, 200, 90, 70) + bld(160, '學校', 90, 80) + jalan_panjang(205, 196, 265, 120) + pohon(268, 120, .35)
A['B29-L8c'] = lantai() + rumah(150, 200, 90, 70) + jalan_panjang(105, 196, 30, 110) + pohon(30, 110, .35) + jalan_panjang(195, 196, 268, 110) + bld(268, '學校', 50, 40, 110)
A['B29-L9'] = A['B29-5']
A['B29-L10'] = lantai() + jalan_panjang(100, 196, 280, 70) + orang(50, tinggi=150, jenis='pria', baju='h', tangan={'ka': [(20, -6), (50, -10)]}) + orang(100, tinggi=140, jenis='wanita', baju='a')
A['B29-T3a'] = jauh('學校') + jam_dinding(255, 150, 26, 1, 0) + teks(255, 196, '1h', 16, angka=True)
A['B29-T3b'] = lantai() + rumah(60, 200, 90, 70) + bld(235, '學校', 100, 80) + jalan_kaki(150, 'pria', 110, 'h')
A['B29-T3c'] = lantai() + sepeda(150, s=1.2) + jam_sektor(250, 50, 30, 10)
A['B29-T4a'] = sisi_ini('pria') + jam_sektor(40, 30, 20, 5)
A['B29-T4b'] = lantai() + bus(150, w=220) + orang(30, tinggi=110, jenis='pria', baju='h')
A['B29-T4c'] = seberang('pria')
A['B29-T6a'] = lantai() + bld(150, '學校', 150, 100)
A['B29-T6b'] = lantai() + bld(60, '學校', 100, 90) + jalan_panjang(110, 196, 265, 120) + pohon(268, 120, .4)
A['B29-T6c'] = lantai() + bld(90, '學校', 120, 90) + pohon(210) + pohon(265, s=.8)
A['B29-T7'] = peta(150, 30, 220, 150)
A['B29-T8'] = lantai() + jalan_raya(120, 75) + mobil(55, 180, 90) + bus(165, 192, 110) + mobil(262, 180, 64)

# B30 — arah
A['B30-1'] = perempatan('kanan')
A['B30-2'] = perempatan('kiri')
A['B30-3'] = lantai() + rumah(225, 200, 110, 80) + jalan_kaki(60, 'wanita', 150, 'a') + jalan_kaki(120, 'laki', 100, 'h') + panah(140, 40, 175, 40, 4)
A['B30-4'] = perempatan('kanan')
A['B30-5'] = lantai() + rumah(200, 200, 140, 90) + jam_dinding(60, 60, 36, 6, 0) + jalan_kaki(110, 'pria', 140, 'a')

# --- B30 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def denah(belok_ke, arah, tanda=None, sebelum=False):
    """Denah dari atas: jalan vertikal dari bawah (orang) ke atas; 2 perempatan (y=130, y=60).
    belok_ke: 1/2 = perempatan ke berapa (0 = lurus terus); arah: 'kiri'/'kanan'. tanda: (label, y) bangunan di kiri jalan."""
    o = kotak(130, 0, 40, 210, 'a') + kotak(0, 112, 300, 36, 'a') + kotak(0, 42, 300, 36, 'a')
    o += kotak(130, 112, 40, 36, 'a') + kotak(130, 42, 40, 36, 'a')
    o += bulat(150, 195, 9, 'h')
    yb = {1: 130, 2: 60}.get(belok_ke)
    if belok_ke:
        xe = 30 if arah == 'kiri' else 270
        o += jalur(f'M150 186 L150 {yb} L{xe} {yb}', 'g', 6) + panah(xe + (14 if arah == 'kiri' else -14), yb, xe, yb, 5)
    else:
        o += jalur('M150 186 L150 20', 'g', 6) + panah(150, 30, 150, 12, 5)
    if tanda:
        lab, y = tanda
        o += kotak(186, y - 16, 70, 30, 'p', 3) + teks(221, y + 5, lab, 14)
    return o


def taman_denah(y):
    return pohon(215, y + 22, .32) + pohon(245, y + 22, .3)


A['B30-L4a'] = denah(1, 'kiri')
A['B30-L4b'] = denah(2, 'kanan')
A['B30-L4c'] = denah(2, 'kiri')
A['B30-L5a'] = lantai() + rumah(200, 200, 140, 90) + jam_dinding(60, 60, 36, 8, 0) + jalan_kaki(110, 'wanita', 140, 'a')
A['B30-L5b'] = lantai() + bld(200, '學校', 140, 100) + jam_dinding(60, 60, 36, 8, 0) + jalan_kaki(110, 'wanita', 140, 'a')
A['B30-L5c'] = lantai() + rumah(200, 200, 140, 90) + jam_dinding(60, 60, 36, 6, 0) + jalan_kaki(110, 'wanita', 140, 'a')
A['B30-L6a'] = denah(1, 'kiri')
A['B30-L6b'] = denah(0, '')
A['B30-L6c'] = denah(1, 'kanan')
A['B30-L8a'] = denah(1, 'kiri') + taman_denah(160)
A['B30-L8b'] = denah(1, 'kiri') + taman_denah(70)
A['B30-L8c'] = denah(1, 'kanan') + taman_denah(160)
A['B30-L9'] = lantai() + meja(150, 140, 200) + buku(130, 140, 50, 22, 'a') + buku(175, 140, 40, 18, 'h')
A['B30-L10'] = lantai() + bentuk((185, 200), (255, 200), (232, 40), (208, 40), k='a') + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, -14), (40, -40)]}) + panah(220, 120, 220, 50, 5)
A['B30-T3a'] = denah(1, 'kiri')
A['B30-T3b'] = denah(0, '') + taman_denah(70)
A['B30-T3c'] = lantai() + bus(150, w=220) + orang(30, tinggi=110, jenis='pria', baju='h')
A['B30-T4a'] = denah(1, 'kiri')
A['B30-T4b'] = denah(2, 'kiri')
A['B30-T4c'] = denah(2, 'kanan')
A['B30-T6a'] = A['B30-L9']
A['B30-T6b'] = lantai_kamar() + ranjang(150, 200, 190) + buku(170, 140, 50, 20, 'a')
A['B30-T6c'] = lantai() + buku(150, 120, 50, 60, 'a') + tas_buka(150, 196, 0, 1.6)
A['B30-T7'] = perempatan('lurus') if False else kotak(130, 0, 40, 210, 'a') + kotak(0, 85, 300, 40, 'a') + ''.join(kotak(126 + i * 12, 92, 6, 26, 'p') for i in range(0)) + ''.join(kotak(134 + i * 0, 129 + i * 9, 32, 5, 'p') for i in range(4))
A['B30-T8'] = lantai() + bentuk((110, 200), (190, 200), (165, 30), (135, 30), k='a') + panah(150, 180, 150, 50, 7)

# B31 — kendaraan
A['B31-1'] = lantai() + sekolah(235, 200, 100, 80) + pengendara_sepeda(110, 'laki', 'a', 110)
A['B31-2'] = (lantai() + kotak(40, 40, 220, 160, 'p', 14) + kotak(60, 60, 180, 70, 'h', 6) + bulat(90, 186, 16, 'h') + bulat(210, 186, 16, 'h')
              + orang(150, kaki=150, tinggi=100, jenis='pria', baju='a', tangan={'ki': [(10, 20), (20, 24)], 'ka': [(10, 20), (20, 24)]}) + elips(150, 124, 30, 8, 'g') + kotak(40, 140, 220, 12, 'a'))
A['B31-3'] = lantai() + sekolah(70, 200, 110, 80) + mobil(200, 200, 150) + orang(275, tinggi=90, jenis='laki', baju='h', tangan=LAMBAI)
A['B31-4'] = lantai() + gedung(245, tingkat=6, lebar=80) + pengendara_sepeda(110, 'pria', 'h', 130) + tas_kerja(86, 138, .45)
A['B31-5'] = (lantai() + kereta(170, 196, 220) + orang(40, tinggi=150, jenis='wanita', baju='a', rambut='uban', tangan=LAMBAI)
              + orang(100, tinggi=120, jenis='gadis', baju='h', tangan={'ki': [(14, -30), (6, -58)]}))

# --- B31 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
A['B31-L4a'] = lantai() + kereta(150, 196, 260)
A['B31-L4b'] = lantai() + mobil(150, 200, 200)
A['B31-L4c'] = lantai() + bus(150, w=240)
A['B31-L5a'] = lantai() + pengendara_sepeda(150, 'pria', 'h', 130)
A['B31-L5b'] = lantai() + mobil(170, 200, 170) + orang(50, tinggi=165, jenis='pria', baju='a', kacamata=True)
A['B31-L5c'] = lantai() + jalan_kaki(150, 'pria', 150, 'h')
A['B31-L6a'] = lantai() + sepeda(90, s=.8) + sepeda(210, s=.8)
A['B31-L6b'] = lantai() + sepeda(55, s=.6) + sepeda(150, s=.6) + sepeda(245, s=.6)
A['B31-L6c'] = lantai() + sepeda(40, s=.45) + sepeda(113, s=.45) + sepeda(186, s=.45) + sepeda(259, s=.45)
A['B31-L8a'] = lantai() + bld(240, '學校', 100, 90) + bus(100, w=170)
A['B31-L8b'] = lantai() + bld(240, '學校', 100, 90) + pengendara_sepeda(100, 'laki', 'a', 110)
A['B31-L8c'] = lantai() + pohon(240) + bangku(240) + pengendara_sepeda(100, 'laki', 'a', 110)
A['B31-L9'] = lantai() + mobil(80, 200, 140) + mobil(225, 200, 140)
A['B31-L10'] = lantai() + bld(150, '學校', 200, 150) + kotak(45, 110, 40, 90, 'a') + panah(20, 160, 50, 160, 4) + silang(150, 175, 18, 5) + orang(18, tinggi=110, jenis='wanita', baju='a')
A['B31-T3a'] = jam_penuh(90, 90, 55, 60) + jam_penuh(210, 90, 55, 60) + teks(150, 190, '2h', 30, angka=True)
A['B31-T3b'] = jam_penuh(90, 90, 55, 60) + jam_penuh(210, 90, 55, 30) + teks(150, 190, '1.5h', 30, angka=True)
A['B31-T3c'] = ''.join(jam_penuh(40 + i * 55, 90, 25, 60) for i in range(5)) + teks(150, 190, '5h', 30, angka=True)
A['B31-T4a'] = lantai() + mobil(150, 200, 200)
A['B31-T4b'] = A['B31-L9']
A['B31-T4c'] = lantai() + mobil(55, 200, 100) + mobil(150, 200, 100) + mobil(245, 200, 100)
A['B31-T6a'] = lantai() + mobil(150, 200, 220, taksi=True)
A['B31-T6b'] = A['B31-2']
A['B31-T6c'] = pesawat(150, 100, 1.0)
A['B31-T7'] = A['B31-L6b']
A['B31-T8'] = lantai() + mobil(170, 200, 170) + orang(50, tinggi=160, jenis='wanita', baju='a', tangan=LAMBAI) + orang(270, tinggi=90, jenis='laki', baju='h', tangan=LAMBAI)

# B32 — arah gerak
A['B32-1'] = kotak(90, 30, 120, 170, 'h') + orang(150, kaki=208, tinggi=175, jenis='pria', baju='a') + panah(250, 90, 250, 170, 6) + lantai()
A['B32-2'] = lantai() + pesawat_depan(150, 60, .8) + panah(150, 118, 150, 140, 5) + orang(150, tinggi=60, jenis='pria', baju='h', tangan={'ka': [(8, -10), (8, -24)]})
A['B32-3'] = lantai() + menara_bandara(250) + pesawat(115, 150, .8) + garis((16, 190), (200, 190), k='t')
A['B32-4'] = lantai() + gedung(150, tingkat=5, lebar=170) + kotak(120, 130, 60, 70, 'h') + orang(150, kaki=208, tinggi=150, jenis='wanita', baju='a') + panah(40, 130, 40, 190, 6)
A['B32-5'] = awan(60, 150, .5) + awan(240, 40, .45) + pesawat(130, 100, .8) + panah(40, 160, 270, 160, 6)

# --- B32 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kal_hari(hari, malam):
    o = kotak(70, 30, 160, 150, 'p', 6) + kotak(70, 30, 160, 34, 'h', 6) + teks(150, 54, '星期' + hari, 20, warna='#fff')
    return o + (bulan_bintang(150, 120, 1.0) if malam else matahari(150, 120, 26))


def jam_x(h):
    return jam_dinding(150, 105, 80, h, 0)


A['B32-L4a'] = lantai() + rumah(190, 200, 140, 100) + jalan_kaki(80, 'pria', 150, 'h') + panah(110, 150, 150, 150, 5)
A['B32-L4b'] = lantai() + garis((60, 200), (60, 160), (110, 160), (110, 120), (160, 120), (160, 80), (210, 80), (210, 40), (280, 40), lebar=4) + orang(130, kaki=120, tinggi=110, jenis='pria', baju='h') + panah(200, 110, 230, 70, 4)
A['B32-L4c'] = lantai() + mobil(110, 200, 170) + orang(240, tinggi=150, jenis='pria', baju='h', tangan={'ki': [(16, 20), (34, 30)]}) + tas_punggung(190, 120, .7)
A['B32-L5a'] = kal_hari('日', True)
A['B32-L5b'] = kal_hari('六', True)
A['B32-L5c'] = kal_hari('日', False)
A['B32-L6a'] = jam_x(10)
A['B32-L6b'] = jam_x(12)
A['B32-L6c'] = jam_x(2)
A['B32-L8a'] = lantai() + anjing(200, 190, .8) + panah(240, 150, 290, 150, 5) + orang(50, tinggi=150, jenis='wanita', baju='a')
A['B32-L8b'] = lantai() + anjing(170, 190, .9) + panah(150, 120, 100, 120, 5) + orang(50, tinggi=150, jenis='wanita', baju='a')
A['B32-L8c'] = lantai() + kucing(170, 190, .9) + panah(150, 120, 100, 120, 5) + orang(50, tinggi=150, jenis='wanita', baju='a')
A['B32-L9'] = lantai() + gedung(110, tingkat=5, lebar=150) + kotak(80, 130, 60, 70, 'h') + orang(210, tinggi=150, jenis='pria', baju='p') + panah(150, 170, 185, 180, 5)
A['B32-L10'] = lantai() + rumah(100, 200, 160, 110) + orang(90, tinggi=120, jenis='wanita', baju='a', tangan=LAMBAI) + orang(240, tinggi=100, jenis='laki', baju='h', wajah='sedih') + ''.join(salju(200 + i * 25, 30 + (i % 2) * 20, 6) for i in range(4))
A['B32-T3a'] = kalender_bulan(150, 30, '下個', '', 170, 160)
A['B32-T3b'] = kotak(70, 30, 160, 150, 'p', 6) + kotak(70, 30, 160, 34, 'h', 6) + teks(150, 54, '明天', 20, warna='#fff') + matahari(150, 120, 26)
A['B32-T3c'] = kotak(70, 30, 160, 150, 'p', 6) + kotak(70, 30, 160, 34, 'h', 6) + teks(150, 54, '下個星期', 18, warna='#fff') + ''.join(kotak(84 + i * 19, 100, 15, 15, 'a', 2) for i in range(7))
A['B32-T4a'] = jam_penuh(60, 90, 40, 60) + jam_penuh(150, 90, 40, 60) + jam_penuh(240, 90, 40, 60) + jam_penuh(150, 175, 0.1, 60) + teks(150, 180, '4h', 26, angka=True) if False else ''.join(jam_penuh(42 + i * 72, 90, 32, 60) for i in range(4)) + teks(150, 180, '4h', 28, angka=True)
A['B32-T4b'] = jam_penuh(90, 90, 50, 60) + jam_penuh(210, 90, 50, 60) + teks(150, 180, '2h', 28, angka=True)
A['B32-T4c'] = jam_sektor(150, 95, 70, 40) + teks(150, 190, '40min', 22, angka=True)
A['B32-T6a'] = lantai() + bld(80, '教室', 120, 100) + jalan_kaki(220, 'laki', 110, 'h') + panah(160, 120, 200, 120, 4)
A['B32-T6b'] = lantai() + meja_kelas(150) + orang(150, tinggi=110, jenis='laki', baju='h', duduk=156)
A['B32-T6c'] = lantai() + bld(200, '教室', 120, 100) + jalan_kaki(70, 'laki', 110, 'h') + panah(100, 120, 140, 120, 4)
A['B32-T7'] = A['B32-3']
A['B32-T8'] = lantai() + meja(150, 150, 200) + gelas_isi(130, 150, 1.3, 'a', True) + gula(220, 150, .8) + panah(205, 70, 160, 90, 4)

# B33 — datang & pergi
A['B33-1'] = lantai() + garis((16, 190), (284, 190), k='t') + pesawat(170, 150, .8) + teks(60, 60, '臺灣', 34) + panah(250, 110, 230, 130, 4)
A['B33-2'] = lantai() + kereta(170, 196, 220) + orang(38, tinggi=150, jenis='pria', baju='h') + koper(62, 196, .6)
A['B33-3'] = kotak(20, 16, 260, 188, 'p') + kursi_depan(90, 150) + kotak(170, 40, 70, 160, 'h') + bentuk((240, 40), (262, 30), (262, 206), (240, 200), k='p') + jalan_kaki(215, 'pria', 140, 'a')
A['B33-4'] = kalender_tahun(55, 60, 2024) + kalender_tahun(150, 60, 2025, True) + kalender_tahun(245, 60, 2026) + teks(245, 160, '今年', 20) + pesawat(150, 94, .22)
A['B33-5'] = kotak(20, 16, 260, 188, 'p') + kursi_depan(100, 150) + meja(180, 150, 90) + kotak(222, 40, 50, 160, 'h') + bentuk((272, 40), (284, 34), (284, 206), (272, 200), k='p')

# --- B33 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kal_teks(judul, malam):
    o = kotak(70, 30, 160, 150, 'p', 6) + kotak(70, 30, 160, 34, 'h', 6) + teks(150, 54, judul, 20, warna='#fff')
    return o + (bulan_bintang(150, 120, 1.0) if malam else matahari(150, 120, 26))


def sisa_apel(x, y, s=1.0):
    return (jalur(f'M{f(x - 14 * s)} {f(y - 30 * s)} Q{f(x - 2 * s)} {f(y - 10 * s)} {f(x - 14 * s)} {f(y + 10 * s)} L{f(x + 14 * s)} {f(y + 10 * s)} Q{f(x + 2 * s)} {f(y - 10 * s)} {f(x + 14 * s)} {f(y - 30 * s)} Z', 'p')
            + garis((x, y - 30 * s), (x, y - 42 * s), lebar=3))


def bakpau(x, y, s=1.0):
    return mantou(x, y, s) + jalur(f'M{f(x - 8 * s)} {f(y - 40 * s)} q{f(8 * s)} {f(-8 * s)} {f(16 * s)} 0', 'g', 2)


A['B33-L4a'] = kal_teks('昨天', True)
A['B33-L4b'] = kal_teks('今天', False)
A['B33-L4c'] = kal_teks('昨天', False)
A['B33-L5a'] = lantai() + orang(110, tinggi=170, jenis='pria', baju='h') + orang(190, tinggi=150, jenis='wanita', baju='a') + koper(250, 196, .7)
A['B33-L5b'] = lantai() + orang(110, tinggi=160, jenis='wanita', rambut='uban', baju='a') + orang(190, tinggi=150, jenis='wanita', baju='p') + koper(250, 196, .7)
A['B33-L5c'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a') + koper(210, 196, .7)
A['B33-L6a'] = lantai() + kereta(150, 196, 260)
A['B33-L6b'] = lantai() + bus(150, w=240)
A['B33-L6c'] = lantai() + pengendara_sepeda(150, 'pria', 'h', 130)
A['B33-L8a'] = lantai() + buah_apel(100, 160, 1.4) + buah_apel(200, 160, 1.4)
A['B33-L8b'] = lantai() + piring(150, 180, 70, sisa_apel(150, 166, 1.3))
A['B33-L8c'] = lantai() + piring(150, 180, 90, sisa_apel(115, 166, 1.2) + sisa_apel(185, 166, 1.2))
A['B33-L9'] = lantai() + meja(150, 150, 220) + kotak(170, 128, 50, 20, 'p', 8) + orang(80, tinggi=150, jenis='pria', baju='h', duduk=156, wajah='puas', tangan={'ka': [(14, 30), (-4, 40)]})
A['B33-L10'] = lantai() + papan_tulis(200, 24, 140, 70) + orang(200, tinggi=160, jenis='pria', baju='a', wajah='senyum') + orang(60, tinggi=110, jenis='gadis', baju='a', wajah='kaget') + gelembung_pikiran(80, 30, 60, 40, teks(80, 38, '老師?', 13), 70, 60)
A['B33-T3a'] = lantai() + orang(110, tinggi=170, jenis='pria', baju='h') + orang(190, tinggi=150, jenis='wanita', baju='a')
A['B33-T3b'] = lantai() + orang(150, tinggi=150, jenis='wanita', baju='a') + koper(210, 196, .7)
A['B33-T3c'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='h') + orang(190, tinggi=145, jenis='wanita', baju='a')
A['B33-T4a'] = kalender_bulan(150, 30, '日', 15, 170, 160).replace('日月', '天')
A['B33-T4b'] = kalender_bulan(150, 30, '日', 5, 170, 160).replace('日月', '天')
A['B33-T4c'] = kalender_bulan(150, 30, '日', 2, 170, 160).replace('日月', '天')
A['B33-T6a'] = lantai() + bakpau(150, 190, 1.8)
A['B33-T6b'] = lantai() + bakpau(70, 190, 1.2) + bakpau(150, 190, 1.2) + bakpau(230, 190, 1.2)
A['B33-T6c'] = lantai() + orang(60, tinggi=150, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(14, 30), (-4, 40)]}) + piring(200, 190, 80, sisa_apel(0, 0, 0)[:0] + jalur('M160 180 q8 -6 16 0 M200 182 q6 -4 12 0 M230 180 q8 -6 14 0', 'g', 3))
A['B33-T7'] = lantai() + orang(80, tinggi=170, jenis='pria', baju='h') + orang(140, tinggi=150, jenis='wanita', baju='a') + koper(200, 196, .8) + koper(250, 196, .7) + pesawat(220, 50, .4)
A['B33-T8'] = lantai() + orang(80, tinggi=160, jenis='wanita', baju='a', wajah='kaget') + kalender_minggu(200, 60, 5, 5, 170)

# B34 — alam
A['B34-1'] = (bentuk((16, 150), (284, 150), (284, 204), (16, 204), k='a') + ''.join(jalur(f'M{24 + i * 20} 150 l4 -10 l4 10', 't') for i in range(13)) + pohon(260, 150, .8)
              + orang(100, tinggi=120, jenis='wanita', duduk=172, baju='p') + orang(170, tinggi=125, jenis='pria', duduk=172, baju='h'))
A['B34-2'] = lantai_kamar() + pintu(250, 200, 140, 60) + ranjang(110, 200, 170) + bulat(56, 136, 13) + muka(56, 136, 13, 'tidur') + jalur('M42 131 q2 -18 16 -18 q12 0 13 14', 'h') + tas_kerja(200, 196, .6)
A['B34-3'] = lantai() + pohon(150, s=1.5) + burung(125, 60) + burung(180, 80, -1)
A['B34-4'] = lantai() + lonceng(60, 50, .5) + rumah(225, 200, 110, 80) + jalan_kaki(130, 'laki', 110, 'a') + tas_punggung(110, 120, .7) + panah(150, 40, 190, 40, 4)
A['B34-5'] = gunung(90, 150, 180, 110) + gunung(220, 150, 170, 90, False) + jalur('M16 200 C80 150 180 190 284 160 L284 180 C180 210 80 170 16 216 Z', 'a') + garis((16, 150), (284, 150), k='t') + pohon(40, 190, .5) + matahari(250, 36, 12)

# --- B34 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def bangun(benda):
    return lantai_kamar() + ranjang(80, 200, 120) + orang(200, tinggi=150, jenis='pria', baju='p', tangan={'ka': [(16, 20), (34, 4)]}) + benda + matahari(270, 30, 14)


def sungai(isi=''):
    return jalur('M16 200 C80 150 180 190 284 160 L284 190 C180 216 80 176 16 216 Z', 'a') + garis((16, 150), (284, 150), k='t') + isi


def tangga(turun=True):
    o = garis((40, 200), (40, 160), (90, 160), (90, 120), (140, 120), (140, 80), (190, 80), (190, 40), (280, 40), lebar=4)
    return lantai() + o + orang(115, kaki=120, tinggi=110, jenis='wanita', baju='a') + (panah(170, 70, 130, 110, 4) if turun else panah(140, 110, 180, 70, 4))


def laut():
    return jalur('M16 120 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 28 0 L284 200 L16 200 Z', 'a') + matahari(240, 50, 18)


A['B34-L4a'] = bangun(cangkir_kopi(250, 120, .6))
A['B34-L4b'] = lantai_kamar() + ranjang(80, 200, 120) + pancuran(210, 30) + orang(210, tinggi=150, jenis='pria', baju='p') + matahari(270, 30, 14)
A['B34-L4c'] = bangun(koran(240, 80, 70, 50))
A['B34-L5a'] = sungai(ikan(100, 185, .5) + ikan(200, 180, .5))
A['B34-L5b'] = sungai(pohon(80, 150, .8) + pohon(220, 150, .9))
A['B34-L5c'] = sungai(''.join(jalur(f'M{24 + i * 22} 150 l4 -10 l4 10', 't') for i in range(12)) + burung(100, 80) + burung(190, 60, -1) + burung(240, 100))
A['B34-L6a'] = laut()
A['B34-L6b'] = sungai(pohon(60, 150, .6) + pohon(250, 150, .7))
A['B34-L6c'] = lantai() + gunung(150, 200, 260, 160)
A['B34-L8a'] = lantai() + pohon(100, s=1.3) + burung(200, 60) + panah(200, 130, 220, 80, 4)
A['B34-L8b'] = lantai() + pohon(150, s=1.5) + burung(150, 60)
A['B34-L8c'] = lantai() + pohon(100, s=1.3) + burung(200, 150) + panah(170, 60, 195, 125, 4)
A['B34-L9'] = tangga(True)
A['B34-L10'] = lantai() + rumah(80, 200, 110, 80) + panah(140, 120, 170, 120, 4) + pancuran(230, 30) + orang(230, tinggi=150, jenis='pria', baju='p')
A['B34-T3a'] = lantai() + anjing(150, 196, 1.4)
A['B34-T3b'] = ikan(150, 105, 1.8)
A['B34-T3c'] = lantai() + pohon(150, s=1.5) + burung(140, 70, 1, 1.6)
A['B34-T4a'] = A['B34-1']
A['B34-T4b'] = lantai() + bangku(150, lebar=160) + orang(120, tinggi=120, jenis='pria', baju='h', duduk=165) + orang(180, tinggi=115, jenis='wanita', baju='a', duduk=165)
A['B34-T4c'] = laut().replace('L284 200 L16 200 Z', 'L284 150 L16 150 Z') + kotak(16, 150, 268, 50, 'p') + ''.join(bulat(30 + i * 23, 175 + (i % 3) * 6, 2, 'h') for i in range(12)) + orang(150, tinggi=90, jenis='pria', baju='h', duduk=190)
A['B34-T6a'] = laut() + ikan(100, 160, .6) + ikan(200, 175, .6)
A['B34-T6b'] = lantai() + burung(100, 80, 1, 1.4) + burung(200, 110, -1, 1.4)
A['B34-T6c'] = sungai(ikan(100, 185, .5) + ikan(200, 180, .5)) + pohon(250, 150, .6)
A['B34-T7'] = tangga(True)
A['B34-T8'] = laut()

# B35 — penginapan & izin
A['B35-1'] = (lantai() + gedung(150, tingkat=5, lebar=160) + kotak(95, 30, 110, 44, 'h', 4) + kotak(112, 52, 76, 10, 'n') + kotak(112, 40, 6, 22, 'n')
              + kotak(182, 52, 6, 12, 'n') + elips(130, 47, 9, 5, 'n'))   # papan bergambar tempat tidur
A['B35-2'] = lantai() + gedung(95, tingkat=5, lebar=120) + papan_angka(230, 80, '$500', 110, 50)
A['B35-3'] = (lantai() + orang(90, tinggi=165, jenis='wanita', baju='a', rambut='uban', tangan={'ka': [(22, 0), (48, -6)]}) + orang(210, tinggi=100, jenis='laki', baju='h', tangan={'ki': [(14, 6), (30, -4)]})
              + cangkir(170, 118, .5) + silang(150, 70, 14, 5))
A['B35-4'] = lantai_kamar() + ranjang(150, 200, 200) + orang(110, tinggi=150, jenis='wanita', baju='a') + orang(190, tinggi=125, jenis='gadis', baju='h')
A['B35-5'] = lantai() + orang(90, tinggi=165, jenis='wanita', baju='a', rambut='uban', wajah='puas') + centang(90, 16, 1.2) + orang(200, tinggi=110, jenis='gadis', baju='h', tangan=LAMBAI) + koper(245, 196, .8)

# --- B35 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def hotel(x=150, w=150):
    return gedung(x, tingkat=5, lebar=w) + kotak(x - 50, 30, 100, 40, 'h', 4) + teks(x, 56, '旅館', 18, warna='#fff')


def bersama(org2):
    return lantai() + orang(80, tinggi=160, jenis='pria', baju='h') + org2 + koper(250, 196, .7)


A['B35-L4a'] = bersama(orang(170, tinggi=155, jenis='wanita', baju='a'))
A['B35-L4b'] = bersama(orang(170, tinggi=170, jenis='pria', baju='a', kacamata=True))
A['B35-L4c'] = bersama(orang(170, tinggi=105, jenis='laki', baju='a'))
A['B35-L5a'] = jalur('M16 150 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 L136 200 L16 200 Z', 'a') + hotel(220, 120) + lantai()
A['B35-L5b'] = gunung(80, 200, 160, 140) + hotel(220, 120) + lantai()
A['B35-L5c'] = lantai() + rumah(170, 200, 160, 110) + orang(60, tinggi=150, jenis='wanita', baju='a', tangan=LAMBAI)
A['B35-L6a'] = lantai_ke(5)
A['B35-L6b'] = lantai_ke(3)
A['B35-L6c'] = lantai_ke(20).replace('>20F<', '>30F<')
A['B35-L8a'] = lantai() + kios_buah(200, 200, 150) + orang(70, tinggi=160, jenis='wanita', rambut='uban', baju='a') + tas_belanja(96, 150, .9)
A['B35-L8b'] = lantai() + kios_buah(210, 200, 140) + orang(80, tinggi=105, jenis='laki', baju='h') + tas_belanja(104, 160, .7) + gelembung_pikiran(80, 30, 60, 46, orang(80, kaki=50, tinggi=36, jenis='wanita', rambut='uban', baju='a'), 80, 70)
A['B35-L8c'] = lantai() + kompor(190, 130) + wajan(190, 112, .9) + orang(90, tinggi=110, jenis='laki', baju='h', tangan=MASAK)
A['B35-L9'] = lantai() + tv(240, 150, 90) + meja(240, 150, 90) + orang(140, tinggi=100, jenis='laki', baju='h', duduk=165) + orang(50, tinggi=170, jenis='pria', baju='a', wajah='puas') + centang(50, 14, 1.0)
A['B35-L10'] = lantai() + kursi(110, s=1.1) + kursi(200, s=1.1) + orang(200, tinggi=130, jenis='wanita', baju='a', duduk=160) + orang(60, tinggi=160, jenis='pria', baju='h') + teks(100, 30, '?', 26, angka=True)
A['B35-T3a'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='h') + koper(140, 196, .8) + orang(220, tinggi=155, jenis='wanita', baju='a')
A['B35-T3b'] = lantai() + kasir(200) + orang(90, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 0), (46, -10)]}) + kartu_kredit(150, 62, .8)
A['B35-T3c'] = lantai() + orang_ponsel(150, 'pria', 160, baju='h')
A['B35-T4a'] = lantai() + rumah(170, 200, 160, 110)
A['B35-T4b'] = gunung(150, 200, 260, 160) + lantai()
A['B35-T4c'] = A['B35-L5a']
A['B35-T6a'] = lantai() + orang(150, tinggi=160, jenis='laki', baju='h', tangan={'ka': [(20, -30), (30, -60)]}) + layar_ponsel(185, 30, '', .4)
A['B35-T6b'] = lantai() + orang(70, tinggi=170, jenis='pria', baju='a', tangan={'ka': [(16, -10), (30, -14)]}) + kotak(100, 56, 30, 22, 'h', 4) + orang(220, tinggi=110, jenis='laki', baju='h', wajah='puas') + pohon(270, s=.7)
A['B35-T6c'] = lantai() + orang(220, tinggi=170, jenis='pria', baju='a', wajah='puas') + orang(80, tinggi=110, jenis='laki', baju='h', tangan={'ka': [(16, -10), (30, -14)]}) + kotak(104, 96, 30, 22, 'h', 4) + pohon(270, s=.7)
A['B35-T7'] = lantai() + hotel(150, 200)
A['B35-T8'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, -6), (40, -14)]}) + pulpen(150, 70, 60, -30) + orang(220, tinggi=155, jenis='wanita', baju='a', wajah='puas') + centang(220, 20, 1.0)

# B36 — pos & bank
A['B36-1'] = lembar_prangko(150, 70, 3, 2, 48)
A['B36-2'] = lantai() + loket(200) + kotak(172, 34, 56, 40, 'p', 4) + amplop(200, 54, 40, 26) + orang(80, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, 0), (46, -8)]}) + amplop(140, 80, 44, 30, -10)
A['B36-3'] = (lantai() + meja(150, 150, 220) + pulpen(190, 138, 60, 0) + orang(70, tinggi=150, jenis='wanita', baju='a', tangan={'ka': [(26, 8), (58, 14)]})
              + orang(240, tinggi=150, jenis='pria', baju='h'))
A['B36-4'] = lantai() + gedung_bank(150)
A['B36-5'] = lantai() + kotak_pos(200) + orang(100, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, 0), (48, -6)]}) + amplop(166, 82, 40, 26, 20)


# ---------------- B37–B46 ----------------
def garis_jatuh(x, y, n=3):
    return ''.join(garis((x - 12 + i * 12, y - 26), (x - 12 + i * 12, y - 12), k='t') for i in range(n))


def rambut_panjang(x, cy, r, pj=70):
    """Rambut sangat panjang di belakang punggung (digambar sebelum orang)."""
    return jalur(f'M{f(x - r * 1.1)} {f(cy)} L{f(x - r * 1.3)} {f(cy + pj)} L{f(x + r * 1.3)} {f(cy + pj)} L{f(x + r * 1.1)} {f(cy)} Z', 'h')


def topi_perawat(x, cy, r):
    return kotak(x - r * .9, cy - r * 1.55, r * 1.8, r * .6, 'p', 2) + palang(x, cy - r * 1.25, r * .012)


def piala(x, bawah, s=1.0):
    return (jalur(f'M{f(x - 24 * s)} {f(bawah - 70 * s)} L{f(x + 24 * s)} {f(bawah - 70 * s)} Q{f(x + 22 * s)} {f(bawah - 36 * s)} {f(x)} {f(bawah - 32 * s)} Q{f(x - 22 * s)} {f(bawah - 36 * s)} {f(x - 24 * s)} {f(bawah - 70 * s)} Z', 'a')
            + kotak(x - 4 * s, bawah - 32 * s, 8 * s, 18 * s, 'h') + kotak(x - 16 * s, bawah - 14 * s, 32 * s, 14 * s, 'h', 2)
            + jalur(f'M{f(x - 24 * s)} {f(bawah - 64 * s)} q{f(-16 * s)} 0 {f(-12 * s)} {f(16 * s)} M{f(x + 24 * s)} {f(bawah - 64 * s)} q{f(16 * s)} 0 {f(12 * s)} {f(16 * s)}', 'g'))


def kembang_api(x, y, r=40):
    o = ''
    for i in range(12):
        a = math.radians(i * 30)
        o += garis((x + math.cos(a) * r * .3, y + math.sin(a) * r * .3), (x + math.cos(a) * r, y + math.sin(a) * r), lebar=2.6)
        o += bulat(x + math.cos(a) * (r + 6), y + math.sin(a) * (r + 6), 2.6, 'h')
    return o


def meja_bundar(x, atas, w=200):
    return elips(x, atas, w / 2, 16, 'a') + kotak(x - 8, atas + 10, 16, LANTAI - atas - 10, 'h') + kotak(x - 40, LANTAI - 8, 80, 8, 'h')


def undangan(x, y, s=1.0):
    return kotak(x - 28 * s, y - 20 * s, 56 * s, 40 * s, 'p', 3) + garis((x - 28 * s, y - 20 * s), (x, y + 2 * s), (x + 28 * s, y - 20 * s), k='t') + bintang(x, y + 8 * s, 6 * s)


def pegang_perut(x, jenis='pria', tinggi=160, baju='a', wajah='sakit'):
    return orang(x, tinggi=tinggi, jenis=jenis, baju=baju, wajah=wajah, tangan={'ki': [(6, 26), (-10, 44)], 'ka': [(6, 26), (-10, 44)]})


def pipi_merah(x, cy, r):
    return elips(x - r * .55, cy + r * .28, r * .22, r * .14, 'm') + elips(x + r * .55, cy + r * .28, r * .22, r * .14, 'm')


def jam_kecil(x, y, jam, menit=0, r=26):
    return jam_dinding(x, y, r, jam, menit, False)


# --- B36 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def pos(x, w=110, h=90, lantai_y=200):
    return bld(x, '郵局', w, h, lantai_y)


def bank_b(x, w=110, h=90, lantai_y=200):
    return bld(x, '銀行', w, h, lantai_y)


def kotak_teh(x, bawah, s=1.0):
    return kotak(x - 30 * s, bawah - 50 * s, 60 * s, 50 * s, 'a', 4) + teks(x, bawah - 18 * s, '茶', 20 * s)


A['B36-L4a'] = lantai() + bank_b(70) + jalan_raya(165, 35) + pos(230, 90, 70, 120) if False else lantai(200) + bank_b(75, 110, 80, 110) + kotak(0, 115, 300, 40, 'a') + ''.join(kotak(10 + i * 50, 133, 26, 4, 'p') for i in range(6)) + pos(225, 110, 70, 200)
A['B36-L4b'] = lantai() + pohon(60) + pohon(250, s=.9) + bangku(160) + pos(160, 90, 70, 120)
A['B36-L4c'] = lantai() + bank_b(85) + pos(215)
A['B36-L5a'] = lantai() + amplop(110, 150, 90, 60) + kotak_teh(220, 196, 1.4)
A['B36-L5b'] = lantai() + amplop(150, 140, 120, 80)
A['B36-L5c'] = lantai() + buku(150, 196, 80, 100, 'a')
A['B36-L6a'] = lantai() + amplop(150, 140, 120, 80)
A['B36-L6b'] = lantai() + buku(110, 196, 70, 90, 'a') + buku(200, 196, 70, 90, 'h')
A['B36-L6c'] = lantai() + kotak_teh(150, 196, 2.0)
A['B36-L8a'] = lantai() + sepeda(200, s=.8) + orang(80, tinggi=110, jenis='laki', baju='h', tangan={'ka': [(16, 20), (40, 24)]}) + orang(270, tinggi=150, jenis='pria', baju='a') + panah(230, 40, 270, 40, 4) + teks(80, 30, '我', 16)
A['B36-L8b'] = lantai() + sepeda(110, s=.8) + orang(240, tinggi=110, jenis='laki', baju='h') + orang(30, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(16, 20), (40, 24)]}) + panah(170, 40, 210, 40, 4) + teks(240, 50, '我', 16)
A['B36-L8c'] = lantai() + toko(220) + sepeda(110, s=.8) + orang(40, tinggi=110, jenis='laki', baju='h') + kotak_teh(0, 0, 0)[:0]
A['B36-L9'] = A['B36-2'].replace('', '') if False else lantai() + loket(200) + lembar_prangko(200, 40, 2, 1, 26) + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(22, 0), (48, -6)]})
A['B36-L10'] = lantai() + orang(80, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(16, -20), (24, -50)]}) + koper(120, 196, .6) + orang(220, tinggi=165, jenis='pria', baju='h', kacamata=True) + teks(150, 40, '?', 26, angka=True)
A['B36-T3a'] = A['B36-L4a']
A['B36-T3b'] = lantai() + bld(85, '學校') + pos(215)
A['B36-T3c'] = A['B36-L4b']
A['B36-T4a'] = label_harga(150, 70, '30', 160, 70)
A['B36-T4b'] = label_harga(150, 70, '60', 160, 70)
A['B36-T4c'] = label_harga(150, 70, '2', 160, 70)
A['B36-T6a'] = lantai() + bank_b(190, 150, 110) + orang(60, tinggi=160, jenis='wanita', baju='a')
A['B36-T6b'] = lantai() + bld(190, '學校', 150, 110) + orang(60, tinggi=160, jenis='wanita', baju='a')
A['B36-T6c'] = lantai() + pos(190, 150, 110) + orang(60, tinggi=160, jenis='wanita', baju='a')
A['B36-T7'] = amplop(150, 70, 200, 130) + lembar_prangko(220, 80, 1, 1, 36)
A['B36-T8'] = perpus(meja(150, 150, 90) + buku(150, 150, 50, 20, 'a') + orang(110, tinggi=130, jenis='pria', baju='h'))

# B37 — kehilangan
A['B37-1'] = lantai() + orang(120, tinggi=165, jenis='pria', baju='a', wajah='kaget') + dompet(170, 170, .45) + garis_jatuh(170, 150)
A['B37-2'] = (lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='kaget', tangan={'ki': [(10, 30), (4, 56)], 'ka': [(10, 30), (4, 56)]})
              + gelembung_pikiran(235, 44, 80, 56, dompet(235, 44, .38) + teks(270, 30, '?', 24, angka=True), 205, 74))
A['B37-3'] = lantai() + meja(110, 130, 160) + ponsel(215, 188, 1.1) + garis_jatuh(215, 166) + jalur('M200 196 l-10 -8 M230 196 l10 -8', 'g')
A['B37-4'] = (lantai() + meja(90, 130, 150) + orang(210, tinggi=165, jenis='wanita', baju='a', wajah='kaget', tangan={'ki': [(20, -4), (40, -10)]})
              + teks(250, 34, '?', 30, angka=True) + teks(60, 110, '?', 24, angka=True))
A['B37-5'] = lantai() + orang(110, tinggi=165, jenis='pria', baju='h', wajah='kaget', tangan={'ka': [(20, 10), (40, 20)]}) + buku(175, 186, 34, 24, 'a') + garis_jatuh(175, 150)

# --- B37 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def air_bawah():
    return jalur('M16 160 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 28 0 L284 205 L16 205 Z', 'a')


def apa(x, y, s=1.0):
    return jalur(f'M{f(x)} {f(y)} q{f(-6 * s)} {f(-14 * s)} {f(4 * s)} {f(-22 * s)} q{f(-2 * s)} {f(10 * s)} {f(8 * s)} {f(14 * s)} q{f(6 * s)} {f(-10 * s)} {f(2 * s)} {f(-20 * s)} q{f(14 * s)} {f(10 * s)} {f(8 * s)} {f(28 * s)} Z', 'a')


def gelas_pecah(x, y):
    return jalur(f'M{x - 30} {y} L{x - 20} {y - 30} L{x - 6} {y - 4} Z', 'p') + jalur(f'M{x + 4} {y} L{x + 16} {y - 22} L{x + 30} {y} Z', 'p') + garis((x - 40, y - 20), (x - 50, y - 30), k='t') + garis((x + 40, y - 20), (x + 50, y - 30), k='t')


A['B37-L4a'] = lantai() + meja(150, 150, 200) + layar_ponsel(150, 128, '', .5)
A['B37-L4b'] = lantai() + tas_buka(150, 196, 0, 1.6) + layar_ponsel(150, 112, '', .5)
A['B37-L4c'] = lantai() + orang(110, tinggi=130, jenis='gadis', baju='a', tangan={'ka': [(16, -10), (24, -30)]}) + layar_ponsel(138, 62, '', .4) + orang(220, tinggi=165, jenis='pria', baju='h', wajah='sedih')
A['B37-L5a'] = air_bawah() + buku(150, 175, 60, 40, 'a') + panah(150, 60, 150, 130, 4)
A['B37-L5b'] = lantai() + buku(150, 196, 80, 30, 'a') + panah(150, 80, 150, 150, 4)
A['B37-L5c'] = lantai() + buku(150, 190, 80, 30, 'a') + apa(120, 160, 1.2) + apa(150, 160, 1.4) + apa(180, 160, 1.2)
A['B37-L6a'] = lantai() + kucing(150, 196, 1.4)
A['B37-L6b'] = lantai() + orang(150, tinggi=110, jenis='laki', baju='h', wajah='puas') + es_krim(190, 140, .6)
A['B37-L6c'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h')
A['B37-L8a'] = lantai() + kucing(160, 196, 1.2) + layar_ponsel(210, 150, '', .35) + panah(100, 120, 60, 120, 4)
A['B37-L8b'] = lantai() + anjing(170, 196, 1.2) + layar_ponsel(232, 136, '', .35) + panah(100, 120, 60, 120, 4)
A['B37-L8c'] = lantai() + anjing(170, 196, 1.2) + sepatu(235, 146, .7, 'a') + panah(100, 120, 60, 120, 4)
A['B37-L9'] = lantai() + meja(110, 130, 140) + gelas_pecah(220, 196) + panah(170, 110, 210, 160, 4)
A['B37-L10'] = lantai() + orang(60, tinggi=110, jenis='laki', baju='h', wajah='sedih') + pengendara_sepeda(200, 'pria', 'a', 140) + panah(250, 60, 290, 60, 4)
A['B37-T3a'] = lantai() + orang_ponsel(150, 'wanita', 160, baju='a')
A['B37-T3b'] = lantai() + orang(110, tinggi=155, jenis='wanita', baju='a', tangan={'ka': [(16, 30), (20, 50)]}) + orang(210, tinggi=160, jenis='pria', baju='h', wajah='sedih') + teks(150, 40, '?', 26, angka=True)
A['B37-T3c'] = lantai() + jalan_kaki(150, 'wanita', 160, 'a') + panah(200, 120, 260, 120, 5)
A['B37-T4a'] = lantai() + kucing(150, 196, 1.4)
A['B37-T4b'] = lantai() + orang(150, tinggi=120, jenis='laki', baju='h')
A['B37-T4c'] = lantai() + anjing(150, 196, 1.4)
A['B37-T6a'] = lantai() + pulpen(150, 180, 120, 0) + panah(150, 80, 150, 160, 4)
A['B37-T6b'] = lantai() + orang(80, tinggi=150, jenis='laki', baju='h', wajah='sedih') + orang(210, tinggi=150, jenis='laki', baju='a', tangan={'ka': [(16, -10), (30, -20)]}) + pulpen(250, 60, 60, -30) + panah(150, 40, 190, 40, 4)
A['B37-T6c'] = lantai() + tas_buka(150, 196, 0, 1.6) + pulpen(150, 110, 90, -80)
A['B37-T7'] = lantai() + orang(100, tinggi=160, jenis='wanita', baju='a', wajah='kaget') + tas_tangan(160, 120, 1.0) + buku(200, 196, 40, 20, 'a') + layar_ponsel(240, 186, '', .3) + dompet(170, 190, .5)
A['B37-T8'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h', wajah='sedih', tangan={'ki': [(14, 30), (10, 50)], 'ka': [(14, 30), (10, 50)]}) + teks(210, 50, '?', 30, angka=True)

# B38 — larangan & hati-hati
_kolam = bentuk((20, 150), (280, 150), (284, 204), (16, 204), k='a') + jalur('M30 170 q10 -8 20 0 t20 0 t20 0 t20 0 M150 186 q10 -8 20 0 t20 0 t20 0', 'w')
A['B38-1'] = _kolam + garis((210, 150), (210, 60), lebar=5) + bulat(210, 50, 34, 'p') + bulat(206, 42, 7) + garis((190, 58), (228, 50), lebar=4) + larangan(210, 50, 34)
A['B38-2'] = (lantai() + kotak(100, 196, 40, 6, 'h') + orang(120, tinggi=160, jenis='wanita', baju='a', wajah='kaget', tangan={'ki': [(20, -20), (40, -40)], 'ka': [(20, -20), (40, -40)]},
                                                               kaki_pose={'ki': (-24, -6), 'ka': (18, 0)}) + orang(235, tinggi=160, jenis='pria', baju='h', wajah='kaget', tangan={'ki': [(16, -8), (36, -16)]}) + teks(185, 40, '!', 30, angka=True))
A['B38-3'] = kotak(90, 30, 120, 160, 'p', 8) + kotak(118, 86, 64, 44, 'h', 6) + bulat(150, 108, 14, 'p') + kotak(130, 78, 18, 8, 'h') + larangan(150, 108, 50)
A['B38-4'] = kotak(90, 30, 120, 160, 'p', 8) + hamburger(150, 136, .5) + larangan(150, 110, 50)
A['B38-5'] = (lantai() + mobil(235, 200, 110) + panah(170, 170, 120, 170, 5) + orang(60, tinggi=160, jenis='wanita', baju='a', rambut='uban', wajah='kaget', tangan={'ka': [(20, -10), (44, -20)]})
              + orang(110, tinggi=90, jenis='laki', baju='h'))

# --- B38 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def papan(isi, dilarang=True, x=150, y=105):
    o = kotak(x - 60, y - 75, 120, 150, 'p', 8) + isi
    return o + (larangan(x, y, 50) if dilarang else centang(x + 34, y + 44, 1.0))


def ik_renang(x, y):
    return bulat(x - 4, y - 8, 7) + garis((x - 24, y), (x + 22, y - 8), lebar=4) + jalur(f'M{x - 40} {y + 14} q10 -6 20 0 q10 6 20 0 q10 -6 20 0 q10 6 20 0', 'g', 3)


def ik_gelas(x, y):
    return gelas(x, y + 30, 'air', .9)


def ik_sepeda(x, y):
    return sepeda(x, y + 30, .45)


def ik_jalan(x, y):
    return jalan_kaki(x, 'pria', 70, 'h').replace('', '') if False else orang(x, kaki=y + 36, tinggi=70, jenis='pria', baju='h')


def ik_ponsel(x, y):
    return layar_ponsel(x, y, '', .5)


def ik_bicara(x, y):
    return bulat(x - 14, y, 18, 'p') + muka(x - 14, y, 18, 'nyanyi') + jalur(f'M{x + 8} {y - 10} l12 -6 M{x + 8} {y} l14 0 M{x + 8} {y + 10} l12 6', 'g', 3)


A['B38-L4a'] = papan(ik_renang(150, 105))
A['B38-L4b'] = papan(ik_gelas(150, 105))
A['B38-L4c'] = papan(hamburger(110, 120, .35), True, 110) + papan(ik_gelas(205, 100), False, 205) if False else kotak(30, 30, 110, 150, 'p', 8) + hamburger(85, 130, .35) + larangan(85, 105, 40) + kotak(160, 30, 110, 150, 'p', 8) + gelas(215, 140, 'air', .8) + centang(245, 160, .8)
A['B38-L5a'] = papan(ik_sepeda(150, 105))
A['B38-L5b'] = papan(ik_jalan(150, 105))
A['B38-L5c'] = papan(ik_sepeda(150, 105), False)
A['B38-L6a'] = lantai() + meja_kelas(150) + orang(150, tinggi=110, jenis='wanita', baju='a', duduk=156) + kamus_kecil(190, 136, 30, 36)
A['B38-L6b'] = lantai() + meja_kelas(150) + orang(150, tinggi=110, jenis='wanita', baju='a', duduk=156) + gelas(190, 138, 'air', .5)
A['B38-L6c'] = lantai() + meja_kelas(150) + orang(150, tinggi=110, jenis='wanita', baju='a', duduk=156) + layar_ponsel(190, 124, '', .3)
A['B38-L8a'] = papan(hamburger(150, 130, .45))
A['B38-L8b'] = papan(ik_bicara(150, 105))
A['B38-L8c'] = papan(ik_ponsel(150, 105))
A['B38-L9'] = lantai() + kotak(0, 150, 300, 50, 'a') + ''.join(kotak(110 + i * 14, 152, 8, 46, 'p') for i in range(5)) + mobil(250, 196, 90) + orang(140, kaki=170, tinggi=110, jenis='wanita', baju='a', wajah='kaget') + teks(70, 60, '!', 30, angka=True)
A['B38-L10'] = _kolam + kotak(180, 30, 90, 110, 'p', 6) + jalan_kaki(225, 'laki', 70, 'h').replace('', '') + larangan(225, 85, 36) if False else _kolam + kotak(180, 30, 90, 110, 'p', 6) + orang(225, kaki=120, tinggi=70, jenis='laki', baju='h', tangan={'ki': [(10, 10), (20, 20)], 'ka': [(10, -10), (20, -20)]}) + larangan(225, 85, 36)
A['B38-T3a'] = papan(hamburger(150, 130, .45))
A['B38-T3b'] = papan(kotak(118, 86, 64, 44, 'h', 6) + bulat(150, 108, 14, 'p'), False)
A['B38-T3c'] = A['B38-3']
A['B38-T4a'] = jam_dinding(150, 105, 80, 10, 10)
A['B38-T4b'] = kertas(150, 105, 170, 180, -1) + teks(150, 50, '考試', 24) + ''.join(garis((90, 80 + i * 22), (210, 80 + i * 22), k='t') for i in range(5))
A['B38-T4c'] = lantai() + buku(150, 196, 80, 110, 'a')
A['B38-T6a'] = A['B38-L8b']
A['B38-T6b'] = A['B38-L8c']
A['B38-T6c'] = A['B38-L8a']
A['B38-T7'] = kertas(150, 105, 170, 180, -1) + teks(150, 50, '重要', 26) + bintang(220, 40, 12) + ''.join(garis((90, 90 + i * 22), (210, 90 + i * 22), k='t') for i in range(4))
A['B38-T8'] = lantai() + awan(150, 30, 1.3, 'a') + hujan(150, 60, 220, 60) + kotak(0, 160, 300, 40, 'a') + orang(150, kaki=170, tinggi=120, jenis='pria', baju='h', wajah='kaget')

# B39 — sakit & rumah sakit
_cyn, _rn = sendi(150, LANTAI, 165, 'wanita')['cy'], sendi(150, LANTAI, 165, 'wanita')['r']
A['B39-1'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='p', rambut='pendek') + topi_perawat(150, _cyn, _rn) + palang(150, 100, .35)
A['B39-2'] = lantai() + pegang_perut(150, 'pria', 165, 'a', 'sakit') + jalur('M118 112 l-12 -4 M116 124 l-14 2 M182 112 l12 -4 M184 124 l14 2', 'g')
A['B39-3'] = lantai() + rambut_panjang(150, _cyn, _rn, 110) + orang(150, tinggi=165, jenis='wanita', baju='a')
A['B39-4'] = lantai() + rumah_sakit(200) + jalan_kaki(70, 'wanita', 150, 'a', 'sakit')
_cym, _rm = sendi(150, LANTAI, 165, 'pria')['cy'], sendi(150, LANTAI, 165, 'pria')['r']
A['B39-5'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='kaget') + pipi_merah(150, _cym, _rm) + jalur('M126 30 l-8 -6 M174 30 l8 -6', 'g')

# --- B39 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def perawat(x, tinggi=160):
    cy, r = _kepala(x, tinggi, 'wanita')
    return orang(x, tinggi=tinggi, jenis='wanita', baju='p', rambut='pendek') + topi_perawat(x, cy, r)


def pasien_ranjang(x=150):
    return lantai_kamar() + ranjang(x, 200, 190) + kotak(x - 40, 134, 104, 16, 'a', 7) + bulat(x - 52, 132, 12) + muka(x - 52, 132, 12, 'sakit')


A['B39-L4a'] = lantai() + pegang_perut(150, 'pria', 165, 'a', 'sakit')
A['B39-L4b'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='lelah') + teks(200, 40, 'z z', 20, angka=True)
A['B39-L4c'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', wajah='sakit', tangan={'ki': [(14, -16), (-2, -30)], 'ka': [(14, -16), (-2, -30)]}) + jalur('M110 30 l-10 -6 M190 30 l10 -6', 'g')
A['B39-L5a'] = lantai() + orang(150, tinggi=120, jenis='gadis', baju='a', rambut='pendek')
A['B39-L5b'] = lantai() + rambut_panjang(150, *_kepala(150, 120, 'gadis'), 95) + orang(150, tinggi=120, jenis='gadis', baju='a')
A['B39-L5c'] = lantai() + orang(150, tinggi=120, jenis='laki', baju='h')
A['B39-L6a'] = pasien_ranjang().replace('', '')
A['B39-L6b'] = pasien_ranjang(110).replace('', '') + orang(250, tinggi=160, jenis='pria', baju='h') + kotak_teh(0, 0, 0)[:0] if False else lantai_kamar() + ranjang(110, 200, 170) + orang(65, kaki=150, tinggi=0.01)[:0] + bulat(58, 132, 12) + muka(58, 132, 12, 'sakit') + kotak(70, 134, 90, 16, 'a', 7) + orang(250, tinggi=160, jenis='pria', baju='h') + buah_apel(205, 180, .7)
A['B39-L6c'] = lantai() + rumah_sakit(200) + orang(70, tinggi=165, jenis='pria', baju='p', kacamata=True) + palang(70, 75, .3)
A['B39-L8a'] = pasien_ranjang(110) + orang(250, tinggi=165, jenis='pria', baju='p', kacamata=True, tangan={'ki': [(14, 20), (34, 30)]}) + palang(250, 75, .3)
A['B39-L8b'] = pasien_ranjang(110) + perawat(250) + pil(200, 120, .8)
A['B39-L8c'] = _nightm + orang(150, tinggi=112, jenis='pria', baju='h', wajah='sakit')
A['B39-L9'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='a', rambut='pendek')
A['B39-L10'] = lantai() + meja(150, 150, 220) + kotak(170, 128, 50, 20, 'p', 8) + orang(90, tinggi=150, jenis='pria', baju='h', duduk=156, wajah='sedih') + orang(250, tinggi=160, jenis='wanita', baju='a') + teks(200, 30, '?', 26, angka=True)
A['B39-T3a'] = lantai() + pegang_perut(150, 'wanita', 160, 'a', 'sakit')
A['B39-T3b'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='sakit', tangan={'ka': [(16, -20), (6, -46)]}) + jalur('M170 44 l10 -4 M172 54 l12 0', 'g')
A['B39-T3c'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='sakit', tangan={'ki': [(14, -16), (-2, -30)], 'ka': [(14, -16), (-2, -30)]})
A['B39-T4a'] = jam_penuh(90, 90, 50, 60) + jam_penuh(210, 90, 50, 60) + teks(150, 180, '2h', 28, angka=True)
A['B39-T4b'] = jam_sektor(150, 95, 70, 10) + teks(150, 190, '10min', 22, angka=True)
A['B39-T4c'] = jam_sektor(150, 95, 70, 20) + teks(150, 190, '20min', 22, angka=True)
A['B39-T6a'] = lantai() + orang(150, tinggi=140, jenis='gadis', baju='a', rambut='pendek')
A['B39-T6b'] = lantai() + rambut_panjang(150, *_kepala(150, 140, 'gadis'), 110) + orang(150, tinggi=140, jenis='gadis', baju='a')
A['B39-T6c'] = lantai() + rambut_panjang(150, *_kepala(150, 140, 'gadis'), 110).replace('class="h"', 'class="kuning"') + orang(150, tinggi=140, jenis='gadis', baju='a', rambut='bayi')
A['B39-T7'] = pasien_ranjang(110) + perawat(250)
A['B39-T8'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='h', wajah='sakit') + orang(220, tinggi=155, jenis='wanita', baju='a', wajah='kaget') + teks(160, 40, '?', 26, angka=True)

# B40 — sebab & waktu
A['B40-1'] = (lantai_kamar() + ranjang(150, 200, 200) + bulat(80, 136, 13) + muka(80, 136, 13, 'sakit') + jalur('M66 131 q2 -18 16 -18 q12 0 13 14', 'h')
              + garis((92, 142), (110, 146), lebar=3) + kotak(230, 150, 34, 24, 'p', 3) + kertas(247, 144, 18, 14, 10))
A['B40-2'] = lantai() + matahari(250, 44, 16) + pelari(130, 'pria', 'a', 165)
A['B40-3'] = (lantai_kamar() + jam_dinding(230, 60, 32, 11, 0) + ranjang(100, 200, 160)
              + orang(100, kaki=176, tinggi=110, jenis='pria', baju='p', wajah='lelah', tangan={'ki': [(14, -14), (4, -30)], 'ka': [(14, -14), (4, -30)]}))
A['B40-4'] = lantai() + orang(130, tinggi=165, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(16, -10), (20, -40)]}) + piala(162, 62, .7) + keringat(104, 36) + keringat(160, 80, .8)
A['B40-5'] = (lantai() + jam_dinding(60, 50, 32, 10, 0) + pintu(250, 200, 140, 60) + jalan_kaki(200, 'pria', 150, 'a', 'kaget')
              + orang(60, tinggi=130, jenis='wanita', baju='h', duduk=156, wajah='marah') + orang(120, tinggi=135, jenis='pria', baju='p', duduk=156, wajah='marah'))

# --- B40 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def jam_langit(h, malam):
    return jam_dinding(130, 105, 75, h, 0) + (bulan_bintang(250, 40, .8) if malam else matahari(250, 40, 20))


A['B40-L4a'] = lantai() + matahari(240, 44, 22) + pohon(80) + orang(170, tinggi=150, jenis='pria', baju='h', wajah='puas')
A['B40-L4b'] = sakit_ranjang('pria') if False else lantai_kamar() + ranjang(150, 200, 200) + bulat(80, 136, 13) + muka(80, 136, 13, 'sakit') + kotak(94, 138, 116, 16, 'a', 7)
A['B40-L4c'] = lantai() + awan(150, 30, 1.3, 'a') + hujan(150, 60, 220, 60) + jendela(150, 90, 120, 90)
A['B40-L5a'] = jam_langit(12, True)
A['B40-L5b'] = jam_langit(10, True)
A['B40-L5c'] = jam_langit(12, False)
A['B40-L6a'] = lantai() + pengendara_sepeda(150, 'pria', 'h', 130)
A['B40-L6b'] = lantai() + bus(150, w=240)
A['B40-L6c'] = lantai() + jalan_kaki(150, 'pria', 160, 'h')
A['B40-L8a'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='sedih') + keringat(124, 36) + keringat(176, 46, .8)
A['B40-L8b'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='puas') + keringat(124, 36) + keringat(176, 46, .8)
A['B40-L8c'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='puas', tangan=LAMBAI) + bintang(210, 40, 8)
A['B40-L9'] = lantai() + jam_dinding(60, 50, 32, 9, 30) + papan_tulis(170, 24, 120, 50) + teks(170, 56, '8:00', 18, warna='#fff', angka=True) + pintu(260, 200, 140, 50) + jalan_kaki(215, 'laki', 120, 'h')
A['B40-L10'] = lantai() + matahari(250, 44, 16) + pelari(130, 'pria', 'a', 165) + centang(230, 150, 1.0)
A['B40-T3a'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h', wajah='lelah') + keringat(124, 36)
A['B40-T3b'] = A['B40-2']
A['B40-T3c'] = lantai_kamar() + ranjang(150, 200, 200) + bulat(80, 136, 13) + muka(80, 136, 13, 'sakit') + kotak(94, 138, 116, 16, 'a', 7)
A['B40-T4a'] = lantai_kamar() + ranjang(150, 200, 200) + bulat(80, 136, 13) + muka(80, 136, 13, 'sakit') + kotak(94, 138, 116, 16, 'a', 7) + panah(250, 60, 250, 110, 5)
A['B40-T4b'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='puas', tangan=LAMBAI) + bintang(210, 40, 8)
A['B40-T4c'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='lelah') + keringat(124, 36)
A['B40-T6a'] = lantai_kamar() + ranjang(150, 200, 200) + bulat(80, 136, 13) + muka(80, 136, 13, 'sakit') + kotak(94, 138, 116, 16, 'a', 7)
A['B40-T6b'] = lantai() + pelari(120, 'laki', 'h', 120) + bulat(185, 184, 14, 'p')
A['B40-T6c'] = lantai() + bld(200, '學校', 130, 100) + jalan_kaki(70, 'laki', 120, 'h')
A['B40-T7'] = lantai() + pelari(110, 'wanita', 'a', 160) + buah_apel(220, 160, 1.0) + pisang(250, 150, .5)
A['B40-T8'] = A['B40-5']

# B41 — emosi
A['B41-1'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='nangis')
A['B41-2'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='marah', tangan={'ki': [(20, 20), (4, 36)], 'ka': [(20, 20), (4, 36)]}) + awan(150, 16, .3, 'a') + jalur('M118 36 l-10 -10 M182 36 l10 -10', 'g')
A['B41-3'] = lantai() + orang(150, tinggi=110, jenis='laki', baju='a', wajah='tawa', tangan={'ki': [(14, -30), (6, -54)], 'ka': [(14, -30), (6, -54)]}) + teks(205, 80, 'ha ha', 20, angka=True)
A['B41-4'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='h', wajah='sedih', tangan={'ki': [(2, 30), (6, 58)], 'ka': [(2, 30), (6, 58)]}) + awan(210, 20, .3, 'a') + hujan(210, 34, 40, 20, 3)
A['B41-5'] = lantai() + orang(150, tinggi=110, jenis='gadis', baju='a', wajah='nangis', tangan={'ki': [(14, -10), (4, -26)], 'ka': [(14, -10), (4, -26)]})

# --- B41 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def potret(x, cy, r, jenis='wanita', wajah='senyum', baju='a', **kw):
    anak = jenis in ('laki', 'gadis', 'bayi')
    t = r / (0.12 if anak else 0.085)
    return orang(x, kaki=cy - r + t, tinggi=t, jenis=jenis, wajah=wajah, baju=baju, **kw)


A['B41-L4a'] = potret(150, 90, 44, 'pria', 'marah', 'h') + awan(150, 22, .32, 'a')
A['B41-L4b'] = potret(150, 90, 44, 'pria', 'tawa', 'h') + teks(238, 60, 'ha ha', 22, angka=True)
A['B41-L4c'] = potret(150, 90, 44, 'pria', 'sedih', 'h') + awan(236, 30, .3, 'a') + hujan(236, 44, 40, 20, 3)
A['B41-L5a'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='nyanyi') + orang(210, tinggi=160, jenis='wanita', rambut='uban', baju='p')
A['B41-L5b'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='nyanyi') + papan_tulis(230, 30, 100, 50) + orang(220, tinggi=165, jenis='pria', baju='a', kacamata=True)
A['B41-L5c'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='nyanyi') + orang(210, tinggi=155, jenis='wanita', baju='h')
A['B41-L6a'] = potret(150, 90, 50, 'laki', 'nangis', 'a')
A['B41-L6b'] = potret(150, 90, 50, 'laki', 'tawa', 'a') + teks(238, 60, 'ha ha', 22, angka=True)
A['B41-L6c'] = potret(150, 90, 50, 'laki', 'marah', 'a') + awan(150, 22, .32, 'a')
A['B41-L8a'] = kotak(60, 8, 180, 50, 'h', 4) + potret(55, 130, 30, 'pria', 'tawa', 'h') + potret(150, 130, 30, 'wanita', 'tawa', 'a') + potret(245, 130, 30, 'pria', 'tawa', 'h')
A['B41-L8b'] = kotak(60, 8, 180, 50, 'h', 4) + potret(55, 130, 30, 'pria', 'nangis', 'h') + potret(150, 130, 30, 'wanita', 'nangis', 'a') + potret(245, 130, 30, 'pria', 'nangis', 'h')
A['B41-L8c'] = kotak(60, 8, 180, 50, 'h', 4) + potret(55, 130, 30, 'pria', 'senyum', 'h') + potret(150, 130, 30, 'wanita', 'nangis', 'a') + potret(245, 130, 30, 'pria', 'senyum', 'h')
A['B41-L9'] = A['B41-3']
A['B41-L10'] = lantai() + awan(150, 26, 1.2, 'a') + hujan(150, 50, 220, 40) + payung(150, 100, 70) + orang(120, tinggi=150, jenis='pria', baju='h') + orang(180, tinggi=110, jenis='gadis', baju='a') + pohon(270, s=.8)
A['B41-T3a'] = potret(150, 90, 44, 'wanita', 'sedih', 'a') + awan(236, 30, .3, 'a') + hujan(236, 44, 40, 20, 3)
A['B41-T3b'] = potret(150, 90, 44, 'wanita', 'marah', 'a') + awan(150, 22, .32, 'a') + kue_ultah(250, 196, '', .5)
A['B41-T3c'] = potret(150, 90, 44, 'wanita', 'tawa', 'a')
A['B41-T4a'] = lantai() + pantai_ringkas(150) if False else lantai() + matahari(250, 40, 18) + orang(120, tinggi=160, jenis='pria', baju='p', wajah='puas') + koper(180, 196, .8)
A['B41-T4b'] = lantai() + gedung(220, tingkat=6, lebar=90) + orang(90, tinggi=160, jenis='pria', baju='h') + tas_kerja(118, 140, .5)
A['B41-T4c'] = lantai() + meja_kelas(150) + orang(150, tinggi=140, jenis='pria', baju='h', duduk=156) + buku(150, 136, 40, 20, 'a')
A['B41-T6a'] = A['B41-L6c']
A['B41-T6b'] = A['B41-L8a']
A['B41-T6c'] = A['B41-L6a']
A['B41-T7'] = lantai() + buah_apel(100, 160, 1.2) + pisang(200, 140, .9) + semangka(150, 110, .5)
A['B41-T8'] = lantai() + papan_tulis(220, 30, 110, 50) + orang(220, tinggi=165, jenis='pria', baju='a', kacamata=True) + orang(90, tinggi=120, jenis='gadis', baju='a', wajah='nyanyi') + gelembung(140, 50, 50, 30, teks(140, 56, '…', 16, angka=True), (-1, 1))

# B42 — mengeluarkan & sifat
A['B42-1'] = lantai() + tas_buka(185, 196, 0, .9) + orang(90, tinggi=160, jenis='laki', baju='a', tangan={'ka': [(20, 10), (50, 0)]}) + buku(160, 104, 30, 36, 'h') + panah(190, 130, 170, 104, 4)
A['B42-2'] = lantai() + kucing(150, 196, 1.9) + ''.join(bintang(80 + i * 70, 60 + (i % 2) * 20, 7) for i in range(3))
A['B42-3'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='wanita', duduk=150, baju='a', wajah='tawa', tangan={'ki': [(20, 0), (30, -16)], 'ka': [(20, 0), (30, -16)]}) + kotak(118, 90, 64, 42, 'h', 3) + garis((150, 90), (150, 132), k='w')
A['B42-4'] = lantai() + anjing(140, 198, 1.2) + ''.join(bintang(70 + i * 80, 60 + (i % 2) * 18, 7) for i in range(3))
A['B42-5'] = lantai() + orang(110, tinggi=165, jenis='wanita', baju='a', tangan={'ka': [(20, 20), (46, 16)]}) + tas_tangan(200, 170, 1.0, 'a') + dompet(170, 110, .35) + panah(195, 128, 178, 116, 3)

# --- B42 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kulkas_buka(isi):
    return lantai() + kotak(150, 30, 100, 170, 'p', 6) + garis((160, 110), (240, 110), k='t') + isi + orang(80, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 10), (50, 0)]})


A['B42-L4a'] = kulkas_buka(botol(200, 105, .6))
A['B42-L4b'] = kulkas_buka(kotak_susu(180, 105, .7) + kotak_susu(220, 105, .7))
A['B42-L4c'] = kulkas_buka(botol(180, 105, .6) + botol(220, 105, .6))
A['B42-L5a'] = lantai() + anjing(150, 198, .8) + ''.join(bintang(90 + i * 60, 90 + (i % 2) * 20, 6) for i in range(3))
A['B42-L5b'] = lantai() + anjing(140, 198, 1.8)
A['B42-L5c'] = lantai() + kucing(150, 196, .9)
A['B42-L6a'] = lantai() + meja(200, 150, 140) + kue_ultah(200, 150, '', .6) + orang(70, tinggi=165, jenis='pria', baju='h', tangan={'ka': [(20, 10), (50, 0)]})
A['B42-L6b'] = lantai() + meja(200, 150, 140) + kue_ultah(200, 150, '', .6) + orang(70, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (50, 0)]})
A['B42-L6c'] = lantai() + meja(200, 150, 140) + kue_ultah(200, 150, '', .6) + orang(70, tinggi=160, jenis='wanita', rambut='uban', baju='p', tangan={'ka': [(20, 10), (50, 0)]})
A['B42-L8a'] = lantai() + tas_buka(185, 196, 0, .9) + orang(90, tinggi=160, jenis='laki', baju='a', tangan={'ka': [(20, 10), (50, 0)]}) + pulpen(165, 104, 50, -40) + panah(240, 150, 240, 100, 4)
A['B42-L8b'] = lantai() + tas_buka(185, 196, 0, .9) + orang(90, tinggi=160, jenis='laki', baju='a', tangan={'ka': [(20, 10), (50, 0)]}) + pulpen(165, 104, 50, -40) + panah(240, 100, 240, 150, 4)
A['B42-L8c'] = A['B42-1']
A['B42-L9'] = lantai() + orang(110, tinggi=120, jenis='laki', baju='h', wajah='puas', tangan={'ka': [(16, -10), (30, -30)]}) + kertas(175, 60, 60, 70, 0) + teks(175, 72, '100', 20, angka=True)
A['B42-L10'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(16, -10), (36, -14)]}) + buku(160, 76, 40, 50, 'a') + kal_teks('昨天', False).replace('', '')[:0] + teks(240, 50, '昨天', 18) + tas_belanja(240, 150, 1.0)
A['B42-T3a'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='wanita', duduk=150, baju='a', wajah='tawa') + buku(150, 150, 60, 26, 'a')
A['B42-T3b'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='wanita', duduk=150, baju='a', wajah='lelah') + buku(150, 150, 60, 26, 'a') + teks(210, 50, 'z z', 20, angka=True)
A['B42-T3c'] = lantai() + buku(110, 196, 70, 90, 'a') + label_harga(220, 70, '999', 110, 46)
A['B42-T4a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='kaget') + teks(200, 40, '?!', 24, angka=True)
A['B42-T4b'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='marah') + awan(150, 18, .3, 'a')
A['B42-T4c'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h', wajah='puas') + kertas(220, 60, 50, 60, 0) + teks(220, 70, '100', 16, angka=True)
A['B42-T6a'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='puas') + meja(210, 150, 120) + kue_ultah(210, 150, '', .5)
A['B42-T6b'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='sakit') + meja(210, 150, 120) + kue_ultah(210, 150, '', .5)
A['B42-T6c'] = lantai() + es_krim(150, 196, 1.5)
A['B42-T7'] = lantai() + anjing(150, 198, 1.4) + bentuk((180, 112), (200, 70), (220, 112), k='a')
A['B42-T8'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(20, 10), (50, 10)]}) + orang(210, tinggi=150, jenis='nenek', rambut='uban', baju='p') + tongkat(210, 150) + teks(150, 40, '♥', 30, angka=True)

# B43 — perasaan
A['B43-1'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='gugup', tangan={'ki': [(10, 24), (-8, 40)], 'ka': [(10, 24), (-8, 40)]}) + keringat(120, 40) + keringat(182, 46) + jalur('M126 150 l-6 4 l6 4 M174 150 l6 4 l-6 4', 'g')
A['B43-2'] = lantai() + kotak(16, 30, 268, 20, 'h') + orang(150, tinggi=165, jenis='pria', baju='h', wajah='gugup') + keringat(122, 50) + keringat(180, 56) + mikrofon(210, 150, .9) + garis((210, 190), (210, 200), lebar=4)
A['B43-3'] = lantai() + orang(130, tinggi=165, jenis='pria', baju='a', wajah='sakit', tangan={'ka': [(14, 26), (-4, -6)]}) + pil(152, 64, .5) + gelas(230, 196, 'air', 1.1) + jalur('M110 30 l-8 -8 M150 24 l8 -8', 'g')
A['B43-4'] = lantai() + orang(150, tinggi=165, jenis='wanita', baju='a', wajah='lelah', badan=.95) + jalur('M126 40 q-8 -12 -16 -4', 'g') + teks(200, 40, 'z z', 18, angka=True)
A['B43-5'] = (kotak(16, 16, 268, 188, 'h') + bulan_bintang(240, 50, .5) + garis((16, 200), (284, 200), k='w')
              + orang(110, tinggi=110, jenis='laki', baju='p', wajah='takut') + garis((200, 200), (200, 110), k='w') + bulat(200, 104, 10, 'p'))

# --- B43 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def potret(x, cy, r, jenis='wanita', wajah='senyum', baju='a', **kw):
    anak = jenis in ('laki', 'gadis', 'bayi')
    t = r / (0.12 if anak else 0.085)
    return orang(x, kaki=cy - r + t, tinggi=t, jenis=jenis, wajah=wajah, baju=baju, **kw)


def masakan(gosong=False):
    o = lantai() + meja(150, 170, 220) + piring(150, 162, 80, '')
    if gosong:
        return o + jalur('M110 158 q20 -30 40 -10 q20 -20 40 10 Z', 'h') + jalur('M120 110 q-6 -12 0 -24 M150 104 q-6 -12 0 -24 M180 110 q-6 -12 0 -24', 'g', 4)
    return o + jalur('M106 158 q20 -40 44 -14 q24 -26 44 14 Z', 'a') + ''.join(bulat(130 + i * 20, 146 - (i % 2) * 8, 4, 'h') for i in range(3)) + jalur('M130 110 q-6 -12 0 -24 M170 110 q-6 -12 0 -24', 'g', 2.5) + bintang(240, 60, 8)


A['B43-L4a'] = potret(150, 90, 44, 'pria', 'lelah', 'h') + teks(230, 48, 'z z', 22, angka=True)
A['B43-L4b'] = potret(150, 90, 44, 'pria', 'tawa', 'h')
A['B43-L4c'] = potret(150, 90, 44, 'pria', 'marah', 'h') + awan(150, 22, .32, 'a')
A['B43-L5a'] = masakan(True)
A['B43-L5b'] = lantai() + meja(150, 170, 220) + piring(150, 162, 80, '')
A['B43-L5c'] = masakan(False)
A['B43-L6a'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='h', wajah='sedih', tangan={'ka': [(20, -10), (40, -14)]}) + silang(140, 60, 16, 4) + piring(220, 170, 40, kotak(206, 154, 26, 14, 'a', 3))
A['B43-L6b'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='h', wajah='puas', tangan={'ka': [(14, 26), (-4, -6)]}) + kotak(102, 60, 16, 12, 'a', 3) + piring(220, 170, 40, kotak(206, 154, 26, 14, 'a', 3))
A['B43-L6c'] = lantai() + jalan_kaki(110, 'pria', 160, 'h') + panah(160, 120, 220, 120, 5) + piring(260, 190, 30, '')
A['B43-L8a'] = lantai() + kue(150, 190, 1.6)
A['B43-L8b'] = lemon(150, 105, 2.4)
A['B43-L8c'] = lantai() + orang(110, tinggi=165, jenis='pria', baju='a', wajah='sakit', tangan={'ka': [(14, 26), (-4, -6)]}) + cangkir_kopi(150, 76, .6)
A['B43-L9'] = lantai() + orang(110, tinggi=160, jenis='pria', baju='h', wajah='lelah', tangan={'ki': [(16, -20), (24, -48)], 'ka': [(16, -20), (24, -48)]}) + kardus(110, 30, 80, 30) + keringat(80, 70) + keringat(140, 80, .8) + kardus(230, 196, 60, 50) + kardus(230, 146, 60, 50)
A['B43-L10'] = lantai() + pelari(120, 'laki', 'h', 120) + rumah(240, 200, 100, 80) + garis((40, 120), (70, 120), k='t') + garis((30, 140), (66, 140), k='t')
A['B43-T3a'] = potret(150, 86, 44, 'wanita', 'gugup', 'a') + keringat(96, 60) + keringat(204, 66) + kertas(240, 150, 50, 60, 0)
A['B43-T3b'] = lantai() + sofa(150) + orang(150, tinggi=140, jenis='wanita', baju='a', duduk=150, wajah='puas')
A['B43-T3c'] = potret(150, 90, 44, 'wanita', 'lelah', 'a') + teks(230, 48, 'z z', 22, angka=True)
A['B43-T4a'] = ''.join(jam_penuh(40 + (i % 6) * 44, 60 + (i // 6) * 60, 18, 60) for i in range(12)) + teks(150, 190, '12h', 26, angka=True)
A['B43-T4b'] = ''.join(jam_penuh(40 + (i % 4) * 72, 60 + (i // 4) * 60, 22, 60) for i in range(8)) + teks(150, 190, '8h', 26, angka=True)
A['B43-T4c'] = jam_penuh(90, 90, 50, 60) + jam_penuh(210, 90, 50, 60) + teks(150, 180, '2h', 28, angka=True)
A['B43-T6a'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h', wajah='senyum') + teks(200, 40, '…', 26, angka=True)
A['B43-T6b'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='h', wajah='nyanyi') + orang(220, tinggi=160, jenis='wanita', baju='a', wajah='tawa') + teks(260, 40, 'ha ha', 18, angka=True)
A['B43-T6c'] = lantai() + orang(90, tinggi=165, jenis='pria', baju='h', wajah='nyanyi') + orang(220, tinggi=160, jenis='wanita', baju='a', wajah='kaget') + teks(260, 40, '?', 26, angka=True)
A['B43-T7'] = A['B43-L9']
A['B43-T8'] = lantai() + orang(150, tinggi=165, jenis='pria', baju='h', wajah='kaget', tangan={'ki': [(10, 30), (4, 56)], 'ka': [(10, 30), (4, 56)]}) + gelembung_pikiran(240, 50, 70, 50, layar_ponsel(240, 50, '', .3) + silang(240, 50, 14, 3), 200, 80)

# B44 — perayaan
A['B44-1'] = (lantai() + orang(70, tinggi=150, jenis='wanita', baju='a', wajah='nyanyi', tangan={'ka': [(12, 30), (-8, -8)]}) + mikrofon(102, 62, .9) + not_musik(40, 50)
              + orang(170, tinggi=155, jenis='pria', baju='h', wajah='tawa', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(24, -20), (36, -56)]}, kaki_pose={'ki': (-8, 0), 'ka': (26, -22)})
              + orang(245, tinggi=145, jenis='wanita', baju='p', wajah='tawa', tangan={'ki': [(24, -20), (36, -56)], 'ka': [(24, -20), (36, -56)]}, kaki_pose={'ki': (-26, -22), 'ka': (8, 0)}))
A['B44-2'] = (kotak(16, 16, 268, 188, 'p') + lampion(60, 44, .9) + lampion(240, 44, .9) + meja_bundar(150, 130, 220)
              + piring(150, 128, 50, pangsit(130, 124, .6) + pangsit(160, 122, .6) + pangsit(146, 112, .55)) + orang(60, tinggi=120, jenis='wanita', duduk=160, baju='a') + orang(240, tinggi=120, jenis='pria', duduk=160, baju='h'))
A['B44-3'] = kotak(16, 16, 268, 120, 'h') + kembang_api(90, 70, 36).replace('class="g"', 'class="w"').replace('class="h"', 'class="n"') + kembang_api(210, 60, 30).replace('class="g"', 'class="w"').replace('class="h"', 'class="n"') + lantai() + orang(110, tinggi=60, jenis='wanita', baju='a', tangan=LAMBAI) + orang(170, tinggi=62, jenis='pria', baju='h', tangan={'ki': [(14, -30), (6, -58)]})
A['B44-4'] = (kotak(16, 16, 268, 188, 'p') + lampion(150, 40, .9) + meja_bundar(150, 130, 230) + mangkuk_mi(150, 112, .3, sumpit=False) + piring(90, 126, 26) + piring(210, 126, 26)
              + orang(40, tinggi=130, jenis='wanita', duduk=160, baju='a', rambut='uban') + orang(260, tinggi=135, jenis='pria', duduk=160, baju='h') + orang(150, kaki=200, tinggi=80, jenis='laki', baju='a'))
A['B44-5'] = dua_panel(teks(75, 30, '昨天', 20) + pintu(120, 200, 130, 50) + orang(60, tinggi=140, jenis='pria', baju='a'),
                       teks(225, 30, '今天', 20) + pintu(270, 200, 130, 50) + orang(210, tinggi=140, jenis='pria', baju='a')) + lantai()

# --- B44 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def kotak_sepatu(x, bawah, s=1.0):
    return kotak(x - 34 * s, bawah - 26 * s, 68 * s, 26 * s, 'a', 3) + kotak(x - 36 * s, bawah - 32 * s, 72 * s, 8 * s, 'h', 2)


def baca(x, jenis, baju):
    return orang(x, tinggi=150, jenis=jenis, baju=baju, tangan={'ki': [(12, 26), (24, 30)], 'ka': [(12, 26), (24, 30)]}) + buku(x, 112, 46, 30, 'a')


def tidur_kursi(x, jenis, baju):
    return orang(x, tinggi=150, jenis=jenis, baju=baju, wajah='tidur') + teks(x + 26, 40, 'z z', 16, angka=True)


def angpao(x, y, s=1.0):
    return kotak(x - 30 * s, y - 45 * s, 60 * s, 90 * s, 'm', 4) + bulat(x, y - 10 * s, 14 * s, 'kuning') + teks(x, y - 4 * s, '福', 16 * s)


A['B44-L4a'] = lantai() + rumah(200, 200, 140, 100) + jalan_kaki(70, 'pria', 150, 'h') + koper(110, 196, .6) + panah(120, 120, 150, 120, 4)
A['B44-L4b'] = lantai() + sofa(150) + orang(150, tinggi=140, jenis='pria', baju='h', duduk=150) + tv(260, 150, 60) + meja(260, 150, 60)
A['B44-L4c'] = lantai() + pesawat(200, 50, .6) + orang(80, tinggi=160, jenis='pria', baju='h') + koper(130, 196, .8)
A['B44-L5a'] = lantai() + orang(70, tinggi=160, jenis='wanita', baju='a', wajah='puas') + kotak_sepatu(200, 196) + kotak_sepatu(200, 166) + kotak_sepatu(200, 136)
A['B44-L5b'] = lantai() + orang(70, tinggi=160, jenis='wanita', baju='a', wajah='puas') + kotak_sepatu(200, 196)
A['B44-L5c'] = lantai() + orang(70, tinggi=160, jenis='wanita', baju='a', wajah='puas') + kotak_sepatu(200, 196) + kotak_sepatu(200, 166)
A['B44-L6a'] = lantai() + kue_ultah(150, 196, '', 1.3)
A['B44-L6b'] = lantai() + meja(150, 170, 230) + piring(100, 162, 50, pangsit(85, 154, .8) + pangsit(110, 156, .8)) + piring(205, 162, 60, ikan(205, 150, .6))
A['B44-L6c'] = lantai(196, 60, 240) + hamburger(150, 180, 1.3)
A['B44-L8a'] = lantai() + baca(60, 'wanita', 'a') + tidur_kursi(150, 'pria', 'h') + baca(240, 'pria', 'a')
A['B44-L8b'] = lantai() + baca(60, 'wanita', 'a') + baca(150, 'pria', 'h') + baca(240, 'pria', 'a')
A['B44-L8c'] = lantai() + tidur_kursi(60, 'wanita', 'a') + tidur_kursi(150, 'pria', 'h') + tidur_kursi(240, 'pria', 'a')
A['B44-L9'] = A['B44-5']
A['B44-L10'] = A['B44-2']
A['B44-T3a'] = lantai() + bld(200, '學校', 130, 100) + jalan_kaki(70, 'pria', 150, 'h')
A['B44-T3b'] = A['B44-L4a']
A['B44-T3c'] = A['B44-L4c']
A['B44-T4a'] = A['B44-L6b']
A['B44-T4b'] = lantai() + bentuk((150, 30), (210, 130), (90, 130), k='a') + bentuk((150, 80), (230, 190), (70, 190), k='a') + kotak(140, 190, 20, 10, 'h') + bintang(150, 30, 12)
A['B44-T4c'] = lampion(100, 80, 1.6) + lampion(210, 90, 1.4)
A['B44-T6a'] = lantai() + meja(150, 160, 230) + orang(80, tinggi=140, jenis='wanita', baju='a', duduk=166) + cangkir(120, 156, .6) + teks(120, 190, '茶', 16) + orang(220, tinggi=145, jenis='pria', baju='h', duduk=166) + cangkir_kopi(180, 156, .6) + teks(180, 190, '咖啡', 14)
A['B44-T6b'] = lantai() + meja(150, 160, 230) + orang(80, tinggi=140, jenis='wanita', baju='a', duduk=166) + cangkir(120, 156, .6) + teks(120, 190, '茶', 16) + orang(220, tinggi=145, jenis='pria', baju='h', duduk=166) + cangkir(180, 156, .6) + teks(180, 190, '茶', 16)
A['B44-T6c'] = lantai() + meja(150, 160, 230) + orang(80, tinggi=140, jenis='wanita', baju='a', duduk=166) + cangkir_kopi(120, 156, .6) + teks(120, 190, '咖啡', 14) + orang(220, tinggi=145, jenis='pria', baju='h', duduk=166) + cangkir_kopi(180, 156, .6) + teks(180, 190, '咖啡', 14)
A['B44-T7'] = angpao(150, 105, 1.6)
A['B44-T8'] = A['B44-5']

# B45 — harapan & kesediaan
A['B45-2'] = lantai() + jendela(60, 40, 60, 50) + awan(60, 60, .3, 'a') + orang(130, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ki': [(4, 18), (-14, 12)], 'ka': [(4, 18), (-14, 12)]}) + gelembung_pikiran(230, 60, 100, 76, matahari(230, 60, 16), 190, 96)
A['B45-3'] = (lantai() + kardus(110, 124, 60, 40) + orang(110, tinggi=160, jenis='wanita', baju='a', tangan={'ki': [(10, 20), (4, 58)], 'ka': [(10, 20), (4, 58)]}) + kardus(110, 124, 60, 40)
              + kardus(210, 124, 60, 40) + orang(210, tinggi=165, jenis='pria', baju='h', wajah='puas', tangan={'ki': [(10, 20), (4, 58)], 'ka': [(10, 20), (4, 58)]}) + kardus(210, 124, 60, 40))
A['B45-4'] = lantai() + orang(90, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(20, 6), (46, -4)]}) + undangan(150, 86, .9) + orang(225, tinggi=165, jenis='pria', baju='h')
A['B45-5'] = lantai() + orang(90, tinggi=160, jenis='pria', baju='a', wajah='puas') + gelembung_pikiran(200, 70, 150, 110, potong_kue(170, 96, .5) + orang(230, kaki=118, tinggi=80, jenis='pria', baju='a', wajah='puas'), 130, 110)

# --- B45 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def lampu_ide(x, y, s=1.0):
    return (bulat(x, y, 16 * s, 'kuning') + kotak(x - 7 * s, y + 14 * s, 14 * s, 10 * s, 'a', 2)
            + ''.join(garis((x + 22 * s * c, y + 22 * s * d), (x + 32 * s * c, y + 32 * s * d), lebar=3) for c, d in ((-1, 0), (1, 0), (0, -1), (-.7, -.7), (.7, -.7))))


def baju_gantung(x, y, k='a'):
    return garis((x, y - 20), (x, y - 8), lebar=3) + kaos(x, y + 50, .9, k)


A['B45-1'] = lantai() + papan_tulis(230, 24, 110, 60) + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(16, -20), (24, -50)]}) + lampu_ide(165, 30, .9)
A['B45-L4a'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (40, 0)]}) + jalan_kaki(200, 'pria', 160, 'h') + centang(240, 30, 1.0)
A['B45-L4b'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(20, 10), (40, 0)]}) + orang(210, tinggi=160, jenis='pria', baju='h', wajah='sedih') + silang(250, 30, 16, 4)
A['B45-L4c'] = lantai_kamar() + ranjang(150, 200, 190) + bulat(98, 132, 12) + muka(98, 132, 12, 'tidur') + kotak(110, 134, 104, 16, 'a', 7)
A['B45-L5a'] = lantai() + gunung(150, 200, 260, 160)
A['B45-L5b'] = lantai() + rumah(150, 200, 160, 110)
A['B45-L5c'] = jalur('M16 130 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 40 0 q20 8 40 0 q20 -8 28 0 L284 160 L16 160 Z', 'a') + kotak(16, 160, 268, 40, 'p') + ''.join(bulat(30 + i * 23, 180 + (i % 3) * 5, 2, 'h') for i in range(12)) + matahari(240, 50, 18) + payung(80, 120, 50)
A['B45-L6a'] = lantai() + orang(60, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 10), (40, 0)]}) + baju_gantung(120, 80, 'a') + baju_gantung(240, 60, 'p').replace('', '') + panah(100, 40, 120, 64, 4)
A['B45-L6b'] = lantai() + orang(60, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, -10), (50, -20)]}) + baju_gantung(120, 80, 'a') + baju_gantung(240, 60, 'p') + panah(210, 20, 236, 44, 4)
A['B45-L6c'] = lantai() + orang(60, tinggi=160, jenis='pria', baju='h', wajah='puas') + baju_gantung(120, 80, 'a') + baju_gantung(240, 60, 'p') + panah(100, 40, 120, 64, 4) + panah(210, 20, 236, 44, 4)
A['B45-L8a'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='pria', duduk=150, baju='a') + buku(150, 150, 70, 26, 'p') + teks(220, 50, 'NEW', 18, angka=True)
A['B45-L8b'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='pria', duduk=150, baju='a', wajah='puas') + buku(200, 196, 40, 50, 'a') + centang(240, 120, 1.0)
A['B45-L8c'] = lantai() + toko_buku(orang(140, tinggi=150, jenis='pria', baju='a', tangan={'ka': [(16, 20), (30, 26)]}) + buku(175, 140, 24, 30, 'a'))
A['B45-L9'] = lantai() + orang(80, tinggi=160, jenis='pria', baju='h', wajah='puas') + gelembung_pikiran(200, 70, 150, 100, pesawat(185, 60, .45) + teks(200, 108, '臺灣', 22), 140, 120)
A['B45-L10'] = lantai() + orang(80, tinggi=165, jenis='wanita', rambut='uban', baju='a', tangan={'ka': [(20, -10), (50, -20)]}) + orang(200, tinggi=150, jenis='pria', baju='h') + kotak(232, 150, 50, 40, 'a', 4) + kaos(257, 150, .4, 'p')
A['B45-T3a'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='gugup') + teks(200, 40, '?', 26, angka=True)
A['B45-T3b'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='marah', tangan={'ka': [(20, -10), (40, -14)]}) + silang(220, 50, 18, 4)
A['B45-T3c'] = lantai() + orang(150, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(16, -10), (24, -30)]}) + centang(210, 40, 1.0)
A['B45-T4a'] = lantai() + orang(150, tinggi=160, jenis='pria', baju='h') + jalur('M118 52 l-12 -4 M120 64 l-14 0', 'g') + jalur('M182 52 l12 -4 M180 64 l14 0', 'g') + teks(240, 40, '♪', 26, angka=True)
A['B45-T4b'] = lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='pria', duduk=150, baju='a') + buku(150, 150, 70, 26, 'a')
A['B45-T4c'] = lantai() + meja(150, 150, 200) + kertas(170, 136, 60, 24) + orang(100, tinggi=150, jenis='pria', duduk=156, baju='h', tangan={'ka': [(20, 16), (50, 20)]}) + pulpen(180, 130, 40, -40)
A['B45-T6a'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', tangan={'ka': [(16, 0), (6, -16)]}) + meja(210, 150, 100) + cangkir_kopi(210, 146, .7) + silang(210, 90, 18, 4)
A['B45-T6b'] = lantai() + meja(150, 150, 140) + cangkir(150, 146, 1.0) + teks(150, 190, '茶', 18)
A['B45-T6c'] = lantai() + orang(110, tinggi=160, jenis='wanita', baju='a', wajah='puas', tangan={'ka': [(14, 26), (-4, -6)]}) + cangkir_kopi(140, 74, .6)
A['B45-T7'] = A['B45-1']
A['B45-T8'] = A['B45-L9']

# B46 — tidak / memutuskan
A['B46-1'] = lantai() + meja(90, 140, 150) + piring(90, 134, 50, telur_ceplok(90, 130, .7)) + jam_kecil(60, 50, 7, 30) + jalan_kaki(220, 'pria', 150, 'a') + tas_kerja(196, 162, .45)
A['B46-2'] = lantai() + orang(80, tinggi=150, jenis='wanita', baju='a', wajah='puas') + gelembung_pikiran(200, 76, 160, 120, pesawat(200, 60, .35) + teks(200, 110, '臺灣', 26) + buku(245, 96, 18, 22, 'h'), 118, 120)
A['B46-3'] = ruang_kelas(guru=False, murid=0) + meja_kelas(60) + murid_belakang(60, 200, 100) + meja_kelas(150) + meja_kelas(240) + murid_belakang(240, 200, 100, 'gadis') + panah(150, 74, 150, 104, 5)
A['B46-4'] = teks(150, 30, '昨天', 22) + lantai() + rumah(80, 200, 110, 80) + orang(80, kaki=196, tinggi=60, jenis='laki', baju='p') + sekolah(220, 200, 100, 70) + silang(220, 110, 34, 8)
A['B46-5'] = kalender_tahun(95, 50, '2026') + teks(95, 146, '今年', 20) + kalender_tahun(205, 50, '2027', True) + pesawat(205, 88, .22)


# ---------------- perbaikan B37–B46: potret dekat untuk soal ekspresi ----------------
def potret(x, cy, r, jenis='wanita', wajah='senyum', baju='a', **kw):
    """Kepala + bahu besar (orang yang sama digambar sangat besar; badan terpotong tepi gambar)."""
    anak = jenis in ('laki', 'gadis', 'bayi')
    t = r / (0.12 if anak else 0.085)
    return orang(x, kaki=cy - r + t, tinggi=t, jenis=jenis, wajah=wajah, baju=baju, **kw)


def rambut_terurai(x, cy, r, pj=3.2):
    """Dua helai rambut panjang di depan bahu sampai dada."""
    return (jalur(f'M{f(x - r * .98)} {f(cy)} Q{f(x - r * 1.35)} {f(cy + r * pj * .5)} {f(x - r * 1.2)} {f(cy + r * pj)} L{f(x - r * .72)} {f(cy + r * pj)} Q{f(x - r * .9)} {f(cy + r * pj * .5)} {f(x - r * .7)} {f(cy + r * .4)} Z', 'h')
            + jalur(f'M{f(x + r * .98)} {f(cy)} Q{f(x + r * 1.35)} {f(cy + r * pj * .5)} {f(x + r * 1.2)} {f(cy + r * pj)} L{f(x + r * .72)} {f(cy + r * pj)} Q{f(x + r * .9)} {f(cy + r * pj * .5)} {f(x + r * .7)} {f(cy + r * .4)} Z', 'h'))


A['B39-3'] = potret(150, 72, 40, 'wanita', 'senyum', 'a') + rambut_terurai(150, 72, 40, 3.4)
A['B39-5'] = potret(150, 84, 44, 'pria', 'kaget', 'a') + elips(150 - 44 * .56, 84 + 44 * .3, 44 * .24, 44 * .15, 'm') + elips(150 + 44 * .56, 84 + 44 * .3, 44 * .24, 44 * .15, 'm') + jalur('M96 40 l-12 -8 M204 40 l12 -8', 'g')
A['B41-1'] = potret(150, 84, 44, 'wanita', 'nangis', 'a')
A['B41-2'] = potret(150, 90, 44, 'wanita', 'marah', 'a') + awan(150, 22, .32, 'a') + jalur('M98 44 l-12 -10 M202 44 l12 -10', 'g')
A['B41-3'] = potret(150, 90, 50, 'laki', 'tawa', 'a') + teks(238, 60, 'ha ha', 22, angka=True)
A['B41-4'] = potret(150, 90, 44, 'wanita', 'sedih', 'h') + awan(236, 30, .3, 'a') + hujan(236, 44, 40, 20, 3)
A['B41-5'] = potret(150, 90, 50, 'gadis', 'nangis', 'a')
A['B42-3'] = (lantai() + kursi_depan(150, 150) + orang(150, tinggi=150, jenis='wanita', duduk=150, baju='a', wajah='tawa', tangan={'ki': [(20, 16), (26, 22)], 'ka': [(20, 16), (26, 22)]})
              + kotak(116, 120, 68, 34, 'h', 3) + garis((150, 120), (150, 154), k='w') + teks(214, 60, 'ha ha', 18, angka=True))
A['B43-1'] = potret(150, 86, 44, 'wanita', 'gugup', 'a') + keringat(96, 60) + keringat(204, 66) + keringat(212, 100, .8)
A['B43-2'] = potret(150, 86, 44, 'pria', 'gugup', 'h') + keringat(96, 62) + keringat(204, 60) + mikrofon(240, 170, 1.1)
A['B43-4'] = potret(150, 90, 44, 'wanita', 'lelah', 'a') + teks(230, 48, 'z z', 22, angka=True)
A['B46-2'] = lantai() + orang(80, tinggi=150, jenis='wanita', baju='a', wajah='puas') + gelembung_pikiran(200, 76, 160, 120, pesawat(200, 62, .35) + buku_tumpuk(200, 122, 2, 50, 14) + tas_punggung(240, 92, .6), 118, 120)

# --- B46 tulis ulang 2026-11-16: opsi/gambar latihan (L*) & Tes Bab (T*) ---
def koki(x):
    t = sendi(x, LANTAI, 160, 'pria')
    cy, r = t['cy'], t['r']
    return orang(x, tinggi=160, jenis='pria', baju='p') + kotak(x - r * .9, cy - r * 2.3, r * 1.8, r * 1.3, 'p', 4) + bulat(x - r * .5, cy - r * 2.3, r * .6, 'p') + bulat(x + r * .5, cy - r * 2.3, r * .6, 'p')


def pengajar(x):
    return papan_tulis(x + 70, 30, 120, 70) + orang(x, tinggi=160, jenis='pria', baju='a', tangan={'ka': [(20, -10), (44, -30)]})


def ransel_w(k):
    return (jalur('M117 50 Q117 26 150 26 Q183 26 183 50', 'g', 6) + kotak(94, 46, 112, 140, k, 26)
            + kotak(112, 126, 76, 46, 'p', 10) + garis((112, 140), (188, 140), k='t'))


A['B46-L4a'] = lantai() + pengajar(70)
A['B46-L4b'] = lantai() + koki(110) + kompor(220, 130) + wajan(220, 112, .9)
A['B46-L4c'] = lantai() + dokter2(110, kaki=200, tinggi=160) + rumah_sakit(225, 200, 120, 90)
A['B46-L5a'] = lantai() + rumah(220, 200, 120, 90) + sofa(80, w=130) + orang(80, tinggi=130, jenis='wanita', baju='a', duduk=150) + buku(80, 140, 40, 24, 'a')
A['B46-L5b'] = lantai() + pohon(60) + pohon(250, s=.9) + bangku(160) + orang(160, tinggi=150, jenis='wanita', baju='a')
A['B46-L5c'] = lantai() + bld(200, '學校', 130, 100) + orang(70, tinggi=150, jenis='wanita', baju='a')
A['B46-L6a'] = ransel_w('p')
A['B46-L6b'] = ransel_w('h')
A['B46-L6c'] = (jalur('M57 70 Q57 50 85 50 Q113 50 113 70', 'g', 5) + kotak(40, 66, 90, 110, 'p', 20)
                + jalur('M187 70 Q187 50 215 50 Q243 50 243 70', 'g', 5) + kotak(170, 66, 90, 110, 'h', 20))
A['B46-L8a'] = lantai() + bld(200, '學校', 130, 100) + jalan_kaki(90, 'laki', 110, 'h') + panah(120, 130, 150, 130, 4)
A['B46-L8b'] = lantai() + rumah(80, 200, 110, 80) + orang(170, tinggi=100, jenis='laki', baju='h') + bld(250, '學校', 70, 60) + silang(250, 160, 30, 5)
A['B46-L8c'] = lantai() + meja_kelas(150) + orang(150, tinggi=110, jenis='laki', baju='h', duduk=156, wajah='tidur') + teks(190, 70, 'z z', 18, angka=True) + papan_tulis(150, 10, 120, 40)
A['B46-L9'] = lantai() + meja(170, 150, 180) + kertas(190, 110, 90, 70, -2) + teks(190, 92, '明年', 14) + teks(190, 116, '臺灣', 18) + orang(80, tinggi=150, jenis='wanita', baju='a', duduk=156, tangan={'ka': [(20, 16), (50, 10)]})
A['B46-L10'] = lantai() + orang(80, tinggi=160, jenis='wanita', rambut='uban', baju='a', tangan={'ka': [(20, 0), (46, -6)]}) + kue(150, 100, .8) + orang(220, tinggi=110, jenis='laki', baju='h', wajah='puas')
A['B46-T3a'] = A['B46-L4a']
A['B46-T3b'] = A['B46-L4b']
A['B46-T3c'] = A['B46-L4c']
A['B46-T4a'] = lantai() + piring(150, 180, 90, kotak(105, 140, 90, 36, 'p', 12))
A['B46-T4b'] = lantai() + piring(150, 180, 90, '') + silang(150, 120, 40, 5)
A['B46-T4c'] = lantai() + piring(150, 180, 90, bakpau(150, 174, 1.4))
A['B46-T6a'] = lantai() + kasir(200) + orang(90, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(20, 0), (46, -10)]}) + uang_kertas(150, 64, .7)
A['B46-T6b'] = lantai() + kios_buah(200, 200, 140) + jalan_kaki(70, 'pria', 160, 'h') + silang(70, 30, 16, 4)
A['B46-T6c'] = lantai() + kios_buah(210, 200, 130) + orang(80, tinggi=160, jenis='pria', baju='h', tangan={'ka': [(16, 30), (24, 40)]}) + tas_belanja(106, 150, 1.0)
A['B46-T7'] = A['B46-L9']
A['B46-T8'] = lantai() + buku(80, 196, 40, 70, 'p') + buku(150, 196, 40, 70, 'a') + buku(220, 196, 40, 70, 'p') + panah(150, 40, 150, 110, 5) + orang(270, tinggi=150, jenis='pria', baju='h')

