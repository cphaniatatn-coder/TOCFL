"""Pustaka komponen ilustrasi soal bergaya buku soal TOCFL (garis hitam, isian hitam/putih/abu datar).

Semua fungsi mengembalikan potongan SVG (string). Kanvas standar 300×220, lantai di y=200.
Kelas gaya (didefinisikan di bungkus()):
  g = garis saja · p = isi putih bergaris · h = isi hitam · a = isi abu · t = garis tipis · m = isi merah (khusus soal warna)
Dipakai oleh gambar_soal.py.
"""
import math

W, H, LANTAI = 300, 220, 200
FONT = "'DFKai-SB','BiauKai','Kaiti TC','Noto Serif TC',serif"
FONT_ANGKA = "'Segoe UI',Roboto,Arial,sans-serif"


def bungkus(isi, w=W, h=H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">'
            '<style>.g{fill:none;stroke:#111;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}'
            '.p{fill:#fff;stroke:#111;stroke-width:3;stroke-linejoin:round;stroke-linecap:round}'
            '.h{fill:#111;stroke:#111;stroke-width:3;stroke-linejoin:round;stroke-linecap:round}'
            '.a{fill:#9a9a9a;stroke:#111;stroke-width:3;stroke-linejoin:round;stroke-linecap:round}'
            '.t{fill:none;stroke:#111;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}'
            '.w{fill:none;stroke:#fff;stroke-width:2.2;stroke-linecap:round}'
            '.m{fill:#d8342c;stroke:#111;stroke-width:3;stroke-linejoin:round}'
            '.hijau{fill:#3a9d4a;stroke:#111;stroke-width:3;stroke-linejoin:round}'
            '.biru{fill:#2f6fd6;stroke:#111;stroke-width:3;stroke-linejoin:round}'
            '.kuning{fill:#f2c230;stroke:#111;stroke-width:3;stroke-linejoin:round}'
            '.n{fill:#fff;stroke:none}'
            f'text{{font-family:{FONT};fill:#111}}.d{{font-family:{FONT_ANGKA};font-weight:700}}</style>'
            f'<rect width="{w}" height="{h}" fill="#fff"/>{isi}</svg>')


def f(x):
    return f'{x:.1f}'.rstrip('0').rstrip('.')


def pts(*p):
    return ' '.join(f'{f(a)},{f(b)}' for a, b in p)


def garis(*p, k='g', lebar=None):
    st = f' style="stroke-width:{lebar}"' if lebar else ''
    return f'<polyline class="{k}" points="{pts(*p)}"{st}/>'


def bentuk(*p, k='p'):
    return f'<polygon class="{k}" points="{pts(*p)}"/>'


def jalur(d, k='g', lebar=None):
    st = f' style="stroke-width:{lebar}"' if lebar else ''
    return f'<path class="{k}" d="{d}"{st}/>'


def kotak(x, y, w, h, k='p', r=0):
    return f'<rect class="{k}" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(r)}"/>'


def bulat(x, y, r, k='p'):
    return f'<circle class="{k}" cx="{f(x)}" cy="{f(y)}" r="{f(r)}"/>'


def elips(x, y, rx, ry, k='p'):
    return f'<ellipse class="{k}" cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(ry)}"/>'


def teks(x, y, s, uk=16, angka=False, k='', anchor='middle', warna=None):
    cls = ' class="d"' if angka else ''
    fill = f' style="fill:{warna}"' if warna else ''   # style, bukan atribut: aturan CSS text{fill} menimpa atribut
    return f'<text x="{f(x)}" y="{f(y)}" font-size="{uk}" text-anchor="{anchor}"{cls}{fill}>{s}</text>'


def lantai(y=LANTAI, x1=16, x2=284):
    return garis((x1, y), (x2, y))


# ================= ORANG =================
# Orang dilihat dari depan. jenis: pria, wanita, laki (anak laki-laki), gadis (anak perempuan), nenek, bayi
# tangan: dict {'ki': [(dx,dy),...], 'ka': [...]} titik relatif terhadap bahu (siku, tangan). Default: tergantung.
# wajah: None | 'senyum' | 'sedih' | 'sakit' | 'tidur' | 'nyanyi' | 'kaget' | 'lelah' | 'lapar' | 'puas'
def orang(x, kaki=LANTAI, tinggi=150, jenis='pria', tangan=None, wajah='senyum', baju='p', duduk=False,
          kacamata=False, rok=None, kaki_pose=None, rambut=None, badan=1.0):
    anak = jenis in ('laki', 'gadis', 'bayi')
    r = tinggi * (0.12 if anak else 0.085)
    atas = kaki - tinggi
    cy = atas + r
    bahu = cy + r * 1.35
    lb = r * (1.9 if jenis in ('wanita', 'gadis', 'nenek') else 2.2) * badan      # lebar bahu (badan <1 kurus, >1 gemuk)
    pinggang = bahu + tinggi * (0.3 if not anak else 0.26)
    if duduk:   # duduk dilihat dari depan: badan turun sampai pinggul = tinggi dudukan (duduk = y dudukan)
        dy = duduk - pinggang
        atas, cy, bahu, pinggang = atas + dy, cy + dy, bahu + dy, duduk
    out = []
    wanita = jenis in ('wanita', 'gadis', 'nenek') if rok is None else rok
    # --- kaki ---
    if duduk:
        out += [garis((x - r * .5, pinggang), (x - r * 1.05, pinggang + 8), (x - r * 1.05, kaki), lebar=r * .4),
                garis((x + r * .5, pinggang), (x + r * 1.05, pinggang + 8), (x + r * 1.05, kaki), lebar=r * .4)]
    else:
        kp = kaki_pose or {}
        ki = kp.get('ki', (-r * .6, 0)); ka = kp.get('ka', (r * .6, 0))
        out += [garis((x - r * .5, pinggang), (x + ki[0], kaki + ki[1]), lebar=r * .38),
                garis((x + r * .5, pinggang), (x + ka[0], kaki + ka[1]), lebar=r * .38)]
    # --- badan ---
    if wanita and not duduk:
        hem = pinggang + tinggi * 0.12
        out.append(bentuk((x - lb / 2, bahu), (x + lb / 2, bahu), (x + lb * .78, hem), (x - lb * .78, hem), k=baju))
    else:
        out.append(bentuk((x - lb / 2, bahu), (x + lb / 2, bahu), (x + lb * .42, pinggang + 2), (x - lb * .42, pinggang + 2), k=baju))
    # --- tangan ---
    t = tangan or {}
    pj = tinggi * (0.3 if not anak else 0.27)
    for sisi, s in (('ki', -1), ('ka', 1)):
        bx, by = x + s * lb / 2, bahu + 3
        titik = [(bx, by)] + [(bx + s * dx if isinstance(dx, (int, float)) else bx, by + dy) for dx, dy in
                              t.get(sisi, [(r * .5, pj)])]
        out.append(garis(*titik, lebar=r * .34))
    # --- kepala ---
    rb = rambut or ('pendek' if jenis in ('pria', 'laki') else 'uban' if jenis == 'nenek' else 'bayi' if jenis == 'bayi' else 'panjang')
    if rb == 'panjang':
        out.append(jalur(f'M{f(x - r * 1.08)} {f(cy)} Q{f(x - r * 1.2)} {f(cy - r * 1.25)} {f(x)} {f(cy - r * 1.18)} '
                         f'Q{f(x + r * 1.2)} {f(cy - r * 1.25)} {f(x + r * 1.08)} {f(cy)} L{f(x + r * 1.15)} {f(cy + r * 1.35)} '
                         f'L{f(x - r * 1.15)} {f(cy + r * 1.35)} Z', k='h'))
    out.append(bulat(x, cy, r))
    if rb == 'pendek':
        out.append(jalur(f'M{f(x - r * 1.02)} {f(cy + r * .1)} Q{f(x - r * 1.1)} {f(cy - r * 1.2)} {f(x)} {f(cy - r * 1.12)} '
                         f'Q{f(x + r * 1.1)} {f(cy - r * 1.2)} {f(x + r * 1.02)} {f(cy + r * .1)} '
                         f'Q{f(x + r * .7)} {f(cy - r * .5)} {f(x - r * .2)} {f(cy - r * .45)} Q{f(x - r * .8)} {f(cy - r * .35)} {f(x - r * 1.02)} {f(cy + r * .1)} Z', k='h'))
    elif rb == 'panjang':
        out.append(jalur(f'M{f(x - r)} {f(cy - r * .05)} Q{f(x - r * .9)} {f(cy - r * 1.1)} {f(x)} {f(cy - r * 1.05)} '
                         f'Q{f(x + r * .9)} {f(cy - r * 1.1)} {f(x + r)} {f(cy - r * .05)} Q{f(x + r * .3)} {f(cy - r * .55)} {f(x - r)} {f(cy - r * .05)} Z', k='h'))
    elif rb == 'uban':
        out.append(jalur(f'M{f(x - r * 1.02)} {f(cy)} Q{f(x - r)} {f(cy - r * 1.15)} {f(x)} {f(cy - r * 1.1)} '
                         f'Q{f(x + r)} {f(cy - r * 1.15)} {f(x + r * 1.02)} {f(cy)} Q{f(x + r * .3)} {f(cy - r * .5)} {f(x - r * 1.02)} {f(cy)} Z', k='a'))
        out.append(bulat(x, cy - r * 1.25, r * .42, k='a'))
    elif rb == 'bayi':
        out.append(jalur(f'M{f(x - r * .3)} {f(cy - r * .95)} q{f(r * .3)} {f(-r * .45)} {f(r * .5)} 0', k='g'))
    out.append(muka(x, cy, r, wajah))
    if kacamata:
        out += [bulat(x - r * .38, cy - r * .05, r * .28, k='t'), bulat(x + r * .38, cy - r * .05, r * .28, k='t'),
                garis((x - r * .1, cy - r * .05), (x + r * .1, cy - r * .05), k='t')]
    return ''.join(out)


def muka(x, y, r, w):
    if not w:
        return ''
    ey, ex = y - r * .08, r * .38
    mata = f'{bulat(x - ex, ey, r * .09, k="h")}{bulat(x + ex, ey, r * .09, k="h")}'
    mulut_y = y + r * .45
    if w == 'senyum':
        return mata + jalur(f'M{f(x - r * .3)} {f(mulut_y - r * .05)} Q{f(x)} {f(mulut_y + r * .25)} {f(x + r * .3)} {f(mulut_y - r * .05)}', 't')
    if w == 'puas':
        return (jalur(f'M{f(x - ex - r * .15)} {f(ey)} q{f(r * .15)} {f(-r * .15)} {f(r * .3)} 0 M{f(x + ex - r * .15)} {f(ey)} q{f(r * .15)} {f(-r * .15)} {f(r * .3)} 0', 't')
                + jalur(f'M{f(x - r * .35)} {f(mulut_y - r * .05)} Q{f(x)} {f(mulut_y + r * .3)} {f(x + r * .35)} {f(mulut_y - r * .05)}', 't'))
    if w in ('sedih', 'lapar'):
        return mata + jalur(f'M{f(x - r * .3)} {f(mulut_y + r * .12)} Q{f(x)} {f(mulut_y - r * .15)} {f(x + r * .3)} {f(mulut_y + r * .12)}', 't')
    if w == 'sakit':
        return (jalur(f'M{f(x - ex - r * .18)} {f(ey - r * .1)} L{f(x - ex + r * .18)} {f(ey + r * .05)} M{f(x + ex + r * .18)} {f(ey - r * .1)} L{f(x + ex - r * .18)} {f(ey + r * .05)}', 't')
                + jalur(f'M{f(x - r * .3)} {f(mulut_y + r * .08)} l{f(r * .15)} {f(-r * .1)} l{f(r * .15)} {f(r * .1)} l{f(r * .15)} {f(-r * .1)} l{f(r * .15)} {f(r * .1)}', 't'))
    if w in ('tidur', 'lelah'):
        m = jalur(f'M{f(x - ex - r * .15)} {f(ey)} q{f(r * .15)} {f(r * .12)} {f(r * .3)} 0 M{f(x + ex - r * .15)} {f(ey)} q{f(r * .15)} {f(r * .12)} {f(r * .3)} 0', 't')
        mulut = (jalur(f'M{f(x - r * .2)} {f(mulut_y)} L{f(x + r * .2)} {f(mulut_y)}', 't') if w == 'tidur'
                 else elips(x, mulut_y + r * .05, r * .14, r * .1, k='t'))
        return m + mulut
    if w == 'nyanyi':
        return (jalur(f'M{f(x - ex - r * .15)} {f(ey)} q{f(r * .15)} {f(-r * .15)} {f(r * .3)} 0 M{f(x + ex - r * .15)} {f(ey)} q{f(r * .15)} {f(-r * .15)} {f(r * .3)} 0', 't')
                + elips(x, mulut_y + r * .05, r * .18, r * .2, k='h'))
    if w == 'kaget':
        return mata + elips(x, mulut_y + r * .05, r * .13, r * .16, k='t')
    return mata


def keringat(x, y, s=1.0):
    return jalur(f'M{f(x)} {f(y)} q{f(-4 * s)} {f(7 * s)} 0 {f(9 * s)} q{f(4 * s)} {f(-2 * s)} 0 {f(-9 * s)} Z', 'p')


# ================= PERABOT & RUANG =================
def meja(x, atas, lebar=150, tinggi=None, k='h'):
    tinggi = tinggi or LANTAI - atas
    return (kotak(x - lebar / 2, atas, lebar, 12, k) + kotak(x - lebar / 2 + 10, atas + 12, 10, tinggi - 12, k)
            + kotak(x + lebar / 2 - 20, atas + 12, 10, tinggi - 12, k))


def kursi(x, lantai_y=LANTAI, arah=1, s=1.0):
    # arah 1 = sandaran di kanan
    sx = x + arah * 22 * s
    return (kotak(min(sx, sx - arah * 0) - 5 * s, lantai_y - 130 * s, 10 * s, 72 * s, 'p')
            + kotak(x - 30 * s, lantai_y - 60 * s, 58 * s, 10 * s, 'a')
            + garis((x - 26 * s, lantai_y - 50 * s), (x - 26 * s, lantai_y)) + garis((x + 24 * s, lantai_y - 50 * s), (x + 24 * s, lantai_y))
            + garis((x - 24 * s, lantai_y - 24 * s), (x + 22 * s, lantai_y - 24 * s))
            + garis((sx - 5 * s, lantai_y - 110 * s), (sx + 5 * s, lantai_y - 110 * s)) + garis((sx - 5 * s, lantai_y - 88 * s), (sx + 5 * s, lantai_y - 88 * s)))


def kursi_depan(x, dudukan, lantai_y=LANTAI, w=70):
    """Kursi dilihat dari depan (gambar SEBELUM orang yang duduk): sandaran, dudukan abu, kaki."""
    return (kotak(x - w / 2 + 6, dudukan - 80, w - 12, 80, 'p') + garis((x - w / 2 + 16, dudukan - 64), (x + w / 2 - 16, dudukan - 64), k='t')
            + kotak(x - w / 2, dudukan, w, 10, 'a') + garis((x - w / 2 + 5, dudukan + 10), (x - w / 2 + 5, lantai_y), lebar=5)
            + garis((x + w / 2 - 5, dudukan + 10), (x + w / 2 - 5, lantai_y), lebar=5))


def tv(x, bawah, lebar=110):
    t = lebar * .64
    return (kotak(x - lebar / 2, bawah - t - 10, lebar, t, 'p', 4) + kotak(x - lebar / 2 + 8, bawah - t - 2, lebar - 16, t - 16, 'h', 2)
            + garis((x - lebar / 2 + 16, bawah - t + 6), (x - lebar / 2 + 32, bawah - t + 6), k='w')
            + kotak(x - 10, bawah - 10, 20, 10, 'p'))


def ranjang(x, lantai_y=LANTAI, lebar=170):
    return (kotak(x - lebar / 2, lantai_y - 95, 12, 95, 'h') + kotak(x + lebar / 2 - 12, lantai_y - 60, 12, 60, 'h')
            + kotak(x - lebar / 2 + 12, lantai_y - 52, lebar - 24, 22, 'p') + kotak(x - lebar / 2 + 12, lantai_y - 30, lebar - 24, 10, 'h')
            + elips(x - lebar / 2 + 36, lantai_y - 60, 20, 9, 'p'))


def pintu(x, lantai_y=LANTAI, t=140, lebar=62, buka=False):
    o = kotak(x - lebar / 2, lantai_y - t, lebar, t, 'p') + kotak(x - lebar / 2 + 8, lantai_y - t + 10, lebar - 16, t / 2 - 16, 't')
    o += kotak(x - lebar / 2 + 8, lantai_y - t / 2 + 4, lebar - 16, t / 2 - 14, 't') + bulat(x + lebar / 2 - 10, lantai_y - t / 2, 3.5, 'h')
    return o


def jendela(x, y, w=70, h=56):
    return kotak(x - w / 2, y, w, h, 'p') + garis((x, y), (x, y + h)) + garis((x - w / 2, y + h / 2), (x + w / 2, y + h / 2))


def rumah(x, lantai_y=LANTAI, lebar=120, t=90):
    return (bentuk((x - lebar / 2 - 10, lantai_y - t), (x, lantai_y - t - 50), (x + lebar / 2 + 10, lantai_y - t), k='h')
            + kotak(x - lebar / 2, lantai_y - t, lebar, t, 'p') + pintu(x + lebar / 4, lantai_y, 56, 28)
            + jendela(x - lebar / 4, lantai_y - t + 18, 34, 28))


def gedung(x, lantai_y=LANTAI, tingkat=6, sorot=None, lebar=90, tt=24):
    o = kotak(x - lebar / 2, lantai_y - tingkat * tt - 6, lebar, tingkat * tt + 6, 'p')
    for i in range(tingkat):
        y = lantai_y - (i + 1) * tt
        k = 'h' if sorot == i + 1 else 'p'
        o += kotak(x - lebar / 2 + 10, y + 5, 22, 13, k) + kotak(x - 11, y + 5, 22, 13, k) + kotak(x + lebar / 2 - 32, y + 5, 22, 13, k)
    return o


def pohon(x, lantai_y=LANTAI, s=1.0):
    return (kotak(x - 5 * s, lantai_y - 50 * s, 10 * s, 50 * s, 'h')
            + jalur(f'M{f(x)} {f(lantai_y - 120 * s)} c{f(-30 * s)} 0 {f(-42 * s)} {f(30 * s)} {f(-30 * s)} {f(45 * s)} '
                    f'c{f(-14 * s)} {f(20 * s)} {f(8 * s)} {f(32 * s)} {f(30 * s)} {f(25 * s)} c{f(22 * s)} {f(7 * s)} {f(44 * s)} {f(-5 * s)} {f(30 * s)} {f(-25 * s)} '
                    f'c{f(12 * s)} {f(-15 * s)} 0 {f(-45 * s)} {f(-30 * s)} {f(-45 * s)} Z', 'p')
            + jalur(f'M{f(x - 14 * s)} {f(lantai_y - 92 * s)} q8 -8 16 0 M{f(x + 4 * s)} {f(lantai_y - 76 * s)} q8 -8 16 0', 't'))


def bangku(x, lantai_y=LANTAI, lebar=80):
    return (kotak(x - lebar / 2, lantai_y - 40, lebar, 8, 'h') + kotak(x - lebar / 2, lantai_y - 66, lebar, 8, 'p')
            + garis((x - lebar / 2 + 8, lantai_y - 32), (x - lebar / 2 + 8, lantai_y)) + garis((x + lebar / 2 - 8, lantai_y - 32), (x + lebar / 2 - 8, lantai_y)))


def papan_tulis(x, y, w=150, h=80):
    return kotak(x - w / 2, y, w, h, 'h', 3) + kotak(x - w / 2 - 4, y + h, w + 8, 6, 'p')


# ================= BENDA =================
def bola(x, y, r=12, jenis='sepak'):
    if jenis == 'sepak':
        return bulat(x, y, r) + bentuk(*[(x + r * .45 * math.cos(math.radians(a)), y + r * .45 * math.sin(math.radians(a))) for a in range(-90, 270, 72)], k='h')
    return bulat(x, y, r, 'a') + jalur(f'M{f(x - r)} {f(y)} L{f(x + r)} {f(y)} M{f(x)} {f(y - r)} L{f(x)} {f(y + r)}', 't')


def buku(x, y, w=36, h=48, k='h'):
    return kotak(x - w / 2, y - h, w, h, k, 2) + garis((x - w / 2 + 5, y - h), (x - w / 2 + 5, y), k='w' if k == 'h' else 't')


def buku_tumpuk(x, y, n=3, w=64, t=26):
    o = ''
    for i in range(n):
        yy = y - i * (t + 4)
        dx = (-6, 8, -2, 6)[i % 4]
        k = ('h', 'p', 'a', 'p')[i % 4]
        o += kotak(x - w / 2 + dx, yy - t, w, t, k, 3) + garis((x - w / 2 + dx + 10, yy - t), (x - w / 2 + dx + 10, yy), k='w' if k == 'h' else 't')
    return o


def salju(x, y, r=9):
    return ''.join(garis((x - math.cos(math.radians(a)) * r, y - math.sin(math.radians(a)) * r),
                         (x + math.cos(math.radians(a)) * r, y + math.sin(math.radians(a)) * r), lebar=2.4) for a in (90, 30, 150))


def pulpen(x, y, pj=90, sudut=0):
    return (f'<g transform="rotate({sudut} {f(x)} {f(y)})">' + kotak(x - pj / 2, y - 5, pj - 14, 10, 'h', 2)
            + bentuk((x + pj / 2 - 14, y - 5), (x + pj / 2, y), (x + pj / 2 - 14, y + 5), k='p') + kotak(x - pj / 2 + 8, y - 8, 22, 3, 'h') + '</g>')


def kertas(x, y, w=46, h=60, miring=0):
    return (f'<g transform="rotate({miring} {f(x)} {f(y)})">' + kotak(x - w / 2, y - h / 2, w, h, 'p')
            + ''.join(garis((x - w / 2 + 7, y - h / 2 + 12 + i * 10), (x + w / 2 - 7, y - h / 2 + 12 + i * 10), k='t') for i in range(4)) + '</g>')


def komputer(x, bawah, w=110):
    h = w * .62
    return (kotak(x - w / 2, bawah - h - 16, w, h, 'p', 4) + kotak(x - w / 2 + 7, bawah - h - 9, w - 14, h - 14, 'h', 2)
            + bentuk((x - w / 2 - 12, bawah), (x + w / 2 + 12, bawah), (x + w / 2, bawah - 16), (x - w / 2, bawah - 16), k='a'))


def ponsel(x, y, s=1.0, layar='h'):
    return kotak(x - 11 * s, y - 20 * s, 22 * s, 40 * s, 'p', 4 * s) + kotak(x - 8 * s, y - 15 * s, 16 * s, 28 * s, layar, 1)


def gelas(x, bawah, isi='air', s=1.0, es=False):
    top = bawah - 60 * s
    o = bentuk((x - 22 * s, top), (x + 22 * s, top), (x + 17 * s, bawah), (x - 17 * s, bawah), k='p')
    if isi == 'susu':
        o += bentuk((x - 20.5 * s, top + 12 * s), (x + 20.5 * s, top + 12 * s), (x + 17 * s, bawah), (x - 17 * s, bawah), k='a')
    elif isi == 'air':
        o += garis((x - 20 * s, top + 14 * s), (x + 20 * s, top + 14 * s), k='t')
    if es:
        o += kotak(x - 14 * s, top + 16 * s, 13 * s, 13 * s, 'p', 2) + kotak(x + 1 * s, top + 22 * s, 13 * s, 13 * s, 'p', 2) + kotak(x - 8 * s, top + 34 * s, 13 * s, 13 * s, 'p', 2)
    return o


def cangkir(x, bawah, s=1.0, uap=True, k='p'):
    o = jalur(f'M{f(x - 24 * s)} {f(bawah - 40 * s)} L{f(x + 24 * s)} {f(bawah - 40 * s)} L{f(x + 20 * s)} {f(bawah)} L{f(x - 20 * s)} {f(bawah)} Z', k)
    o += jalur(f'M{f(x + 23 * s)} {f(bawah - 32 * s)} q{f(16 * s)} {f(2 * s)} {f(12 * s)} {f(16 * s)} q{f(-3 * s)} {f(6 * s)} {f(-14 * s)} {f(6 * s)}', 'g')
    o += elips(x, bawah + 2, 34 * s, 5 * s, 'p')
    if uap:
        o += uap_(x, bawah - 50 * s, s)
    return o


def uap_(x, y, s=1.0):
    return jalur(''.join(f'M{f(x + dx * s)} {f(y)} q{f(-7 * s)} {f(-8 * s)} 0 {f(-16 * s)} q{f(7 * s)} {f(-8 * s)} 0 {f(-16 * s)} ' for dx in (-12, 0, 12)), 't')


def mangkuk_mi(x, y, s=1.0, sumpit=True, uap=True):
    o = ''
    if uap:
        o += uap_(x, y - 18 * s, s * 1.2)
    if sumpit:
        o += garis((x - 80 * s, y - 14 * s), (x + 88 * s, y - 42 * s), lebar=5 * s) + garis((x - 78 * s, y - 2 * s), (x + 90 * s, y - 28 * s), lebar=5 * s)
    o += jalur(f'M{f(x - 90 * s)} {f(y)} L{f(x + 90 * s)} {f(y)} Q{f(x + 86 * s)} {f(y + 56 * s)} {f(x + 26 * s)} {f(y + 64 * s)} L{f(x - 26 * s)} {f(y + 64 * s)} Q{f(x - 86 * s)} {f(y + 56 * s)} {f(x - 90 * s)} {f(y)} Z', 'h')
    o += kotak(x - 22 * s, y + 64 * s, 44 * s, 12 * s, 'h', 3)
    o += elips(x, y, 90 * s, 14 * s, 'p')
    o += jalur(f'M{f(x - 64 * s)} {f(y)} q{f(10 * s)} {f(-8 * s)} {f(20 * s)} 0 t{f(20 * s)} 0 t{f(20 * s)} 0 t{f(20 * s)} 0 t{f(20 * s)} 0 t{f(20 * s)} 0 t{f(10 * s)} 0', 't')
    return o


def piring(x, y, rx=70, isi=''):
    return elips(x, y, rx, rx * .22, 'p') + elips(x, y - 1, rx * .72, rx * .15, 't') + isi


def telur_ceplok(x, y, s=1.0):
    return jalur(f'M{f(x - 30 * s)} {f(y)} q{f(-6 * s)} {f(-14 * s)} {f(12 * s)} {f(-14 * s)} q{f(10 * s)} {f(-8 * s)} {f(24 * s)} {f(-2 * s)} '
                 f'q{f(18 * s)} {f(2 * s)} {f(14 * s)} {f(12 * s)} q{f(-2 * s)} {f(10 * s)} {f(-22 * s)} {f(8 * s)} q{f(-24 * s)} {f(4 * s)} {f(-28 * s)} {f(-4 * s)} Z', 'p') + elips(x, y - 6 * s, 10 * s, 7 * s, 'h')


def ikan(x, y, s=1.0, k='p'):
    return (jalur(f'M{f(x - 40 * s)} {f(y)} Q{f(x - 5 * s)} {f(y - 26 * s)} {f(x + 32 * s)} {f(y)} Q{f(x - 5 * s)} {f(y + 26 * s)} {f(x - 40 * s)} {f(y)} Z', k)
            + bentuk((x + 28 * s, y), (x + 50 * s, y - 16 * s), (x + 50 * s, y + 16 * s), k='h')
            + bulat(x - 26 * s, y - 4 * s, 3 * s, 'h') + jalur(f'M{f(x - 14 * s)} {f(y - 12 * s)} q{f(6 * s)} {f(12 * s)} 0 {f(24 * s)}', 't'))


def daging(x, y, s=1.0):
    return jalur(f'M{f(x - 34 * s)} {f(y)} q{f(-4 * s)} {f(-22 * s)} {f(24 * s)} {f(-24 * s)} q{f(40 * s)} {f(-4 * s)} {f(44 * s)} {f(14 * s)} q{f(4 * s)} {f(18 * s)} {f(-30 * s)} {f(18 * s)} q{f(-34 * s)} 0 {f(-38 * s)} {f(-8 * s)} Z', 'a') + jalur(f'M{f(x - 18 * s)} {f(y - 8 * s)} q{f(18 * s)} {f(-10 * s)} {f(36 * s)} {f(-2 * s)}', 'w')


def roti(x, y, s=1.0):
    return (jalur(f'M{f(x - 56 * s)} {f(y)} L{f(x - 56 * s)} {f(y - 30 * s)} Q{f(x - 56 * s)} {f(y - 56 * s)} {f(x)} {f(y - 56 * s)} Q{f(x + 56 * s)} {f(y - 56 * s)} {f(x + 56 * s)} {f(y - 30 * s)} L{f(x + 56 * s)} {f(y)} Z', 'a')
            + jalur(f'M{f(x - 28 * s)} {f(y - 44 * s)} l{f(10 * s)} {f(-8 * s)} M{f(x - 4 * s)} {f(y - 46 * s)} l{f(10 * s)} {f(-8 * s)} M{f(x + 20 * s)} {f(y - 44 * s)} l{f(10 * s)} {f(-8 * s)}', 'w'))


def bakpao(x, y, s=1.0):
    return (jalur(f'M{f(x - 30 * s)} {f(y)} Q{f(x - 34 * s)} {f(y - 38 * s)} {f(x)} {f(y - 40 * s)} Q{f(x + 34 * s)} {f(y - 38 * s)} {f(x + 30 * s)} {f(y)} Z', 'p')
            + jalur(f'M{f(x - 10 * s)} {f(y - 36 * s)} Q{f(x)} {f(y - 30 * s)} {f(x)} {f(y - 40 * s)} Q{f(x)} {f(y - 30 * s)} {f(x + 10 * s)} {f(y - 36 * s)} M{f(x - 14 * s)} {f(y - 26 * s)} Q{f(x)} {f(y - 20 * s)} {f(x + 14 * s)} {f(y - 26 * s)}', 't'))


def buah_apel(x, y, s=1.0):
    return (jalur(f'M{f(x)} {f(y - 26 * s)} C{f(x - 30 * s)} {f(y - 40 * s)} {f(x - 34 * s)} {f(y + 6 * s)} {f(x - 8 * s)} {f(y + 8 * s)} Q{f(x)} {f(y + 4 * s)} {f(x + 8 * s)} {f(y + 8 * s)} '
                  f'C{f(x + 34 * s)} {f(y + 6 * s)} {f(x + 30 * s)} {f(y - 40 * s)} {f(x)} {f(y - 26 * s)} Z', 'p')
            + garis((x, y - 26 * s), (x + 4 * s, y - 38 * s)) + jalur(f'M{f(x + 4 * s)} {f(y - 34 * s)} q{f(10 * s)} {f(-10 * s)} {f(18 * s)} {f(-4 * s)} q{f(-8 * s)} {f(8 * s)} {f(-18 * s)} {f(4 * s)} Z', 'h'))


def mikrofon(x, y, s=1.0):
    return elips(x, y, 9 * s, 11 * s, 'a') + kotak(x - 4 * s, y + 9 * s, 8 * s, 30 * s, 'h', 2)


def not_musik(x, y, s=1.0):
    return (elips(x, y, 6 * s, 4.5 * s, 'h') + garis((x + 5 * s, y), (x + 5 * s, y - 24 * s)) + jalur(f'M{f(x + 5 * s)} {f(y - 24 * s)} q{f(10 * s)} {f(4 * s)} {f(10 * s)} {f(14 * s)}', 'g'))


def jam_dinding(x, y, r, jam, menit, lingkar=True):
    o = bulat(x, y, r, 'p') + (bulat(x, y, r * .88, 't') if lingkar else '')
    for i in range(12):
        a = math.radians(i * 30)
        p1 = (x + math.sin(a) * r * .72, y - math.cos(a) * r * .72)
        p2 = (x + math.sin(a) * r * .84, y - math.cos(a) * r * .84)
        o += garis(p1, p2, lebar=4 if i % 3 == 0 else 2.2)
    am = math.radians(menit * 6)
    aj = math.radians((jam % 12) * 30 + menit * .5)
    o += garis((x, y), (x + math.sin(aj) * r * .45, y - math.cos(aj) * r * .45), lebar=r * .09)
    o += garis((x, y), (x + math.sin(am) * r * .7, y - math.cos(am) * r * .7), lebar=r * .055)
    return o + bulat(x, y, r * .06, 'h')


def weker(x, y, r, jam, menit):
    return (bulat(x - r * .7, y - r * .85, r * .32, 'h') + bulat(x + r * .7, y - r * .85, r * .32, 'h')
            + garis((x - r * .6, y + r * .85), (x - r * .85, y + r * 1.15), lebar=4) + garis((x + r * .6, y + r * .85), (x + r * .85, y + r * 1.15), lebar=4)
            + jam_dinding(x, y, r, jam, menit))


def bulan_bintang(x, y, s=1.0):
    return (jalur(f'M{f(x)} {f(y - 22 * s)} A{f(22 * s)} {f(22 * s)} 0 1 0 {f(x + 18 * s)} {f(y + 14 * s)} A{f(17 * s)} {f(17 * s)} 0 1 1 {f(x)} {f(y - 22 * s)} Z', 'h')
            + bintang(x + 42 * s, y - 14 * s, 6 * s) + bintang(x - 36 * s, y + 6 * s, 4.5 * s) + bintang(x + 30 * s, y + 26 * s, 4 * s))


def bintang(x, y, r):
    p = []
    for i in range(10):
        a = math.radians(-90 + i * 36)
        rr = r if i % 2 == 0 else r * .45
        p.append((x + math.cos(a) * rr, y + math.sin(a) * rr))
    return bentuk(*p, k='h')


def matahari(x, y, r=18, k='p'):
    o = bulat(x, y, r, k)
    for i in range(8):
        a = math.radians(i * 45)
        o += garis((x + math.cos(a) * (r + 6), y + math.sin(a) * (r + 6)), (x + math.cos(a) * (r + 16), y + math.sin(a) * (r + 16)))
    return o


def awan(x, y, s=1.0, k='p'):
    return jalur(f'M{f(x - 44 * s)} {f(y + 14 * s)} q{f(-16 * s)} {f(-2 * s)} {f(-12 * s)} {f(-18 * s)} q{f(4 * s)} {f(-14 * s)} {f(22 * s)} {f(-10 * s)} '
                 f'q{f(6 * s)} {f(-22 * s)} {f(30 * s)} {f(-18 * s)} q{f(18 * s)} {f(-16 * s)} {f(38 * s)} {f(-2 * s)} q{f(24 * s)} {f(-4 * s)} {f(24 * s)} {f(18 * s)} '
                 f'q{f(16 * s)} {f(4 * s)} {f(8 * s)} {f(20 * s)} Z', k)


def hujan(x, y, w=110, h=60, n=9):
    o = ''
    for i in range(n):
        xx = x - w / 2 + (i + .5) * w / n
        yy = y + (i % 3) * 12
        o += garis((xx, yy), (xx - 6, yy + 16), lebar=2.4) + garis((xx - 10, yy + 26 + (i % 2) * 8), (xx - 16, yy + 42 + (i % 2) * 8), lebar=2.4)
    return o


def angin(x, y, s=1.0):
    return jalur(f'M{f(x)} {f(y)} L{f(x + 70 * s)} {f(y)} q{f(18 * s)} 0 {f(14 * s)} {f(-14 * s)} q{f(-4 * s)} {f(-10 * s)} {f(-14 * s)} {f(-4 * s)} '
                 f'M{f(x + 10 * s)} {f(y + 16 * s)} L{f(x + 90 * s)} {f(y + 16 * s)} q{f(16 * s)} 0 {f(12 * s)} {f(12 * s)} q{f(-4 * s)} {f(8 * s)} {f(-12 * s)} {f(4 * s)} '
                 f'M{f(x - 6 * s)} {f(y + 32 * s)} L{f(x + 54 * s)} {f(y + 32 * s)}', 'g')


def gunung(x, lantai_y=LANTAI, w=220, h=130, salju=True):
    o = bentuk((x - w / 2, lantai_y), (x - w * .1, lantai_y - h), (x + w * .12, lantai_y - h * .62), (x + w * .25, lantai_y - h * .78), (x + w / 2, lantai_y), k='a')
    if salju:
        o += bentuk((x - w * .1, lantai_y - h), (x - w * .19, lantai_y - h * .78), (x - w * .1, lantai_y - h * .82), (x - w * .02, lantai_y - h * .74), k='p')
    return o


def bunga(x, y, s=1.0):
    o = garis((x, y), (x, y + 30 * s), lebar=2.4) + jalur(f'M{f(x)} {f(y + 18 * s)} q{f(10 * s)} {f(-8 * s)} {f(14 * s)} {f(-2 * s)} q{f(-6 * s)} {f(8 * s)} {f(-14 * s)} {f(2 * s)} Z', 'h')
    for i in range(5):
        a = math.radians(i * 72 - 90)
        o += elips(x + math.cos(a) * 7 * s, y + math.sin(a) * 7 * s, 5.5 * s, 5.5 * s, 'p')
    return o + bulat(x, y, 4 * s, 'h')


# ================= KENDARAAN =================
def kereta(x, lantai_y=LANTAI, w=250):
    o = jalur(f'M{f(x - w / 2)} {f(lantai_y - 22)} L{f(x - w / 2)} {f(lantai_y - 92)} L{f(x + w / 2 - 36)} {f(lantai_y - 92)} Q{f(x + w / 2)} {f(lantai_y - 90)} {f(x + w / 2)} {f(lantai_y - 44)} L{f(x + w / 2)} {f(lantai_y - 22)} Z', 'p')
    o += kotak(x - w / 2, lantai_y - 58, w, 10, 'h')
    for i in range(4):
        o += kotak(x - w / 2 + 12 + i * 44, lantai_y - 84, 32, 22, 'h', 2)
    o += jalur(f'M{f(x + w / 2 - 34)} {f(lantai_y - 84)} L{f(x + w / 2 - 12)} {f(lantai_y - 84)} Q{f(x + w / 2 - 4)} {f(lantai_y - 76)} {f(x + w / 2 - 4)} {f(lantai_y - 62)} L{f(x + w / 2 - 34)} {f(lantai_y - 62)} Z', 'h')
    for dx in (-w / 2 + 30, -w / 2 + 70, w / 2 - 70, w / 2 - 30):
        o += bulat(x + dx, lantai_y - 16, 10, 'h') + bulat(x + dx, lantai_y - 16, 3, 'n')
    o += garis((x - w / 2 - 20, lantai_y - 4), (x + w / 2 + 20, lantai_y - 4)) + garis((x - w / 2 - 20, lantai_y + 2), (x + w / 2 + 20, lantai_y + 2), k='t')
    return o


def bus(x, lantai_y=LANTAI, w=210):
    o = kotak(x - w / 2, lantai_y - 104, w, 86, 'p', 10)
    for i in range(4):
        o += kotak(x - w / 2 + 12 + i * 40, lantai_y - 94, 30, 30, 'h', 3)
    o += kotak(x + w / 2 - 34, lantai_y - 94, 24, 62, 'a', 2) + kotak(x - w / 2, lantai_y - 52, w - 38, 8, 'h')
    for dx in (-w / 2 + 40, w / 2 - 56):
        o += bulat(x + dx, lantai_y - 16, 15, 'h') + bulat(x + dx, lantai_y - 16, 5, 'n')
    return o


def mobil(x, lantai_y=LANTAI, w=150, taksi=False, k='p'):
    o = jalur(f'M{f(x - w / 2)} {f(lantai_y - 20)} L{f(x - w / 2)} {f(lantai_y - 46)} Q{f(x - w / 2 + 4)} {f(lantai_y - 54)} {f(x - w / 2 + 18)} {f(lantai_y - 56)} '
              f'L{f(x - w * .26)} {f(lantai_y - 58)} L{f(x - w * .14)} {f(lantai_y - 86)} L{f(x + w * .2)} {f(lantai_y - 86)} L{f(x + w * .32)} {f(lantai_y - 58)} '
              f'L{f(x + w / 2 - 8)} {f(lantai_y - 54)} Q{f(x + w / 2)} {f(lantai_y - 50)} {f(x + w / 2)} {f(lantai_y - 40)} L{f(x + w / 2)} {f(lantai_y - 20)} Z', k)
    o += bentuk((x - w * .2, lantai_y - 60), (x - w * .1, lantai_y - 80), (x + .02 * w, lantai_y - 80), (x + .02 * w, lantai_y - 60), k='h')
    o += bentuk((x + .06 * w, lantai_y - 60), (x + .06 * w, lantai_y - 80), (x + w * .17, lantai_y - 80), (x + w * .26, lantai_y - 60), k='h')
    for dx in (-w * .3, w * .3):
        o += bulat(x + dx, lantai_y - 18, 15, 'h') + bulat(x + dx, lantai_y - 18, 5, 'n')
    if taksi:
        o += kotak(x - 18, lantai_y - 100, 36, 14, 'h', 3) + teks(x, lantai_y - 89, 'TAXI', 10, angka=True, warna='#fff')
    return o


def pesawat(x, y, s=1.0):
    return (jalur(f'M{f(x - 110 * s)} {f(y)} Q{f(x - 110 * s)} {f(y - 14 * s)} {f(x - 90 * s)} {f(y - 14 * s)} L{f(x + 80 * s)} {f(y - 14 * s)} Q{f(x + 112 * s)} {f(y - 12 * s)} {f(x + 112 * s)} {f(y)} '
                  f'Q{f(x + 112 * s)} {f(y + 12 * s)} {f(x + 80 * s)} {f(y + 14 * s)} L{f(x - 90 * s)} {f(y + 14 * s)} Q{f(x - 110 * s)} {f(y + 14 * s)} {f(x - 110 * s)} {f(y)} Z', 'p')
            + bentuk((x - 10 * s, y + 2 * s), (x + 30 * s, y + 2 * s), (x - 20 * s, y + 60 * s), (x - 40 * s, y + 60 * s), k='h')
            + bentuk((x - 10 * s, y - 6 * s), (x + 26 * s, y - 6 * s), (x - 16 * s, y - 44 * s), (x - 32 * s, y - 44 * s), k='a')
            + bentuk((x - 96 * s, y - 12 * s), (x - 74 * s, y - 12 * s), (x - 94 * s, y - 46 * s), (x - 106 * s, y - 46 * s), k='h')
            + ''.join(bulat(x + dx * s, y - 4 * s, 3.2 * s, 'h') for dx in range(-60, 80, 14)))


# ================= PAKAIAN =================
def sepatu(x, y, s=1.0, k='h'):
    return jalur(f'M{f(x - 34 * s)} {f(y)} L{f(x - 34 * s)} {f(y - 26 * s)} Q{f(x - 18 * s)} {f(y - 30 * s)} {f(x - 10 * s)} {f(y - 22 * s)} '
                 f'Q{f(x + 6 * s)} {f(y - 14 * s)} {f(x + 28 * s)} {f(y - 12 * s)} Q{f(x + 38 * s)} {f(y - 10 * s)} {f(x + 38 * s)} {f(y)} Z', k) + garis((x - 34 * s, y - 5 * s), (x + 38 * s, y - 5 * s), k='w' if k == 'h' else 't')


def kaos(x, y, s=1.0, k='p'):
    return jalur(f'M{f(x - 22 * s)} {f(y - 50 * s)} L{f(x - 50 * s)} {f(y - 36 * s)} L{f(x - 42 * s)} {f(y - 18 * s)} L{f(x - 30 * s)} {f(y - 24 * s)} L{f(x - 30 * s)} {f(y + 30 * s)} '
                 f'L{f(x + 30 * s)} {f(y + 30 * s)} L{f(x + 30 * s)} {f(y - 24 * s)} L{f(x + 42 * s)} {f(y - 18 * s)} L{f(x + 50 * s)} {f(y - 36 * s)} L{f(x + 22 * s)} {f(y - 50 * s)} '
                 f'Q{f(x)} {f(y - 36 * s)} {f(x - 22 * s)} {f(y - 50 * s)} Z', k)


# ================= TANDA & ANGKA =================
def kalender_bulan(x, y, bulan, tgl_sorot, w=120, h=120, ikon=''):
    o = kotak(x - w / 2, y, w, h, 'p', 4) + kotak(x - w / 2, y, w, 30, 'h', 4)
    o += teks(x, y + 22, f'{bulan}月', 18, warna='#fff')
    o += teks(x, y + 92, str(tgl_sorot), 56, angka=True)
    o += bulat(x - w / 2 + 18, y - 4, 5, 'h') + bulat(x + w / 2 - 18, y - 4, 5, 'h')
    return o + ikon


def kalender_minggu(x, y, hari_ini, sorot, w=270):
    """Deret 7 hari (日一二三四五六). hari_ini & sorot = indeks 0..6 (0 = 日). hari_ini diberi label 今天."""
    nama = '日一二三四五六'
    lw = w / 7
    o = kotak(x - w / 2, y, w, 70, 'p', 4) + kotak(x - w / 2, y, w, 24, 'h', 4)
    for i, n in enumerate(nama):
        cx = x - w / 2 + lw * (i + .5)
        o += teks(cx, y + 18, f'星期{n}' if False else n, 15, warna='#fff')
        if i:
            o += garis((x - w / 2 + lw * i, y + 24), (x - w / 2 + lw * i, y + 70), k='t')
        if i == hari_ini:
            o += teks(cx, y + 54, '今天', 15)
        if i == sorot:
            o += bulat(cx, y + 48, 17, 't') + bulat(cx, y + 48, 21, 'g')
    return o


def label_harga(x, y, harga, w=130, h=64):
    return (bentuk((x - w / 2, y), (x + w / 2 - 20, y), (x + w / 2, y + h / 2), (x + w / 2 - 20, y + h), (x - w / 2, y + h), k='p')
            + bulat(x + w / 2 - 22, y + h / 2, 5, 'g') + teks(x - 10, y + h / 2 + 12, f'${harga}', 32, angka=True))


def struk(x, y, total, w=110, h=150):
    o = jalur(f'M{f(x - w / 2)} {f(y)} L{f(x + w / 2)} {f(y)} L{f(x + w / 2)} {f(y + h)} ' + ''.join(
        f'L{f(x + w / 2 - (i + .5) * w / 8)} {f(y + h - 8)} L{f(x + w / 2 - (i + 1) * w / 8)} {f(y + h)} ' for i in range(8)) + 'Z', 'p')
    for i in range(4):
        o += garis((x - w / 2 + 12, y + 20 + i * 16), (x + w / 2 - 12 - (i % 2) * 20, y + 20 + i * 16), k='t')
    o += garis((x - w / 2 + 10, y + 92), (x + w / 2 - 10, y + 92), lebar=2)
    o += teks(x - w / 2 + 12, y + 122, '共', 20, anchor='start') + teks(x + w / 2 - 10, y + 122, f'${total}', 22, angka=True, anchor='end')
    return o


def larangan(x, y, r=34):
    return bulat(x, y, r, 'g') + f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="none" stroke="#111" stroke-width="7"/>' + garis((x - r * .7, y - r * .7), (x + r * .7, y + r * .7), lebar=7)


def silang(x, y, r=26, lebar=8):
    return garis((x - r, y - r), (x + r, y + r), lebar=lebar) + garis((x + r, y - r), (x - r, y + r), lebar=lebar)


def centang(x, y, s=1.0, lebar=6):
    return garis((x - 14 * s, y), (x - 4 * s, y + 10 * s), (x + 16 * s, y - 14 * s), lebar=lebar)


def panah(x1, y1, x2, y2, lebar=6):
    a = math.atan2(y2 - y1, x2 - x1)
    kp = 16
    return (garis((x1, y1), (x2, y2), lebar=lebar)
            + bentuk((x2 + math.cos(a) * 6, y2 + math.sin(a) * 6), (x2 - math.cos(a - .5) * kp, y2 - math.sin(a - .5) * kp),
                     (x2 - math.cos(a + .5) * kp, y2 - math.sin(a + .5) * kp), k='h'))


def gelembung(x, y, w, h, isi, ekor=(-1, 1)):
    ex, ey = ekor
    return (jalur(f'M{f(x - w / 2 + 12)} {f(y - h / 2)} L{f(x + w / 2 - 12)} {f(y - h / 2)} Q{f(x + w / 2)} {f(y - h / 2)} {f(x + w / 2)} {f(y - h / 2 + 12)} '
                  f'L{f(x + w / 2)} {f(y + h / 2 - 12)} Q{f(x + w / 2)} {f(y + h / 2)} {f(x + w / 2 - 12)} {f(y + h / 2)} '
                  f'L{f(x + ex * 8)} {f(y + h / 2)} L{f(x + ex * 26)} {f(y + h / 2 + 18)} L{f(x - ex * 6)} {f(y + h / 2)} '
                  f'L{f(x - w / 2 + 12)} {f(y + h / 2)} Q{f(x - w / 2)} {f(y + h / 2)} {f(x - w / 2)} {f(y + h / 2 - 12)} '
                  f'L{f(x - w / 2)} {f(y - h / 2 + 12)} Q{f(x - w / 2)} {f(y - h / 2)} {f(x - w / 2 + 12)} {f(y - h / 2)} Z', 'p') + isi)


def kartu_nama(x, y, nama, w=170, h=96):
    return (kotak(x - w / 2, y, w, h, 'p', 6) + kotak(x - w / 2 + 12, y + 16, 30, 36, 'a', 3)
            + teks(x + 22, y + 52, nama, 34) + garis((x - w / 2 + 12, y + 70), (x + w / 2 - 12, y + 70), k='t')
            + garis((x - w / 2 + 12, y + 80), (x + w / 2 - 40, y + 80), k='t'))


def bendera_taiwan(x, y, w=120, h=80):
    """中華民國國旗 (hitam-putih): latar merah → abu, kanton biru → hitam, 白日 = matahari putih 12 sinar,
    dikelilingi lingkar biru (hitam) dan cakram putih. BUKAN bintang."""
    o = kotak(x, y, w, h, 'a') + kotak(x, y, w / 2, h / 2, 'h')
    cx, cy = x + w / 4, y + h / 4
    ch = h / 2                               # tinggi kanton
    ujung, dasar = ch * .40, ch * .235        # jari-jari ujung sinar & pangkal sinar
    for i in range(12):
        a = math.radians(i * 30 - 90)
        o += bentuk((cx + math.cos(a) * ujung, cy + math.sin(a) * ujung),
                    (cx + math.cos(a - math.radians(15)) * dasar, cy + math.sin(a - math.radians(15)) * dasar),
                    (cx + math.cos(a + math.radians(15)) * dasar, cy + math.sin(a + math.radians(15)) * dasar), k='n')
    o += f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(dasar * 1.02)}" fill="#fff"/>'
    o += f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(dasar * .92)}" fill="#111"/>'
    o += f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(dasar * .78)}" fill="#fff"/>'
    return o + garis((x, y), (x, LANTAI), lebar=4)   # tiang sampai lantai


def pil(x, y, s=1.0):
    return (f'<g transform="rotate(-30 {f(x)} {f(y)})">' + kotak(x - 16 * s, y - 7 * s, 32 * s, 14 * s, 'p', 7 * s)
            + jalur(f'M{f(x)} {f(y - 7 * s)} L{f(x + 9 * s)} {f(y - 7 * s)} A{f(7 * s)} {f(7 * s)} 0 0 1 {f(x + 9 * s)} {f(y + 7 * s)} L{f(x)} {f(y + 7 * s)} Z', 'h') + '</g>')


def botol_obat(x, bawah, s=1.0):
    return (kotak(x - 20 * s, bawah - 56 * s, 40 * s, 56 * s, 'p', 5 * s) + kotak(x - 14 * s, bawah - 68 * s, 28 * s, 12 * s, 'h', 2)
            + kotak(x - 20 * s, bawah - 40 * s, 40 * s, 22 * s, 'a') + garis((x, bawah - 36 * s), (x, bawah - 22 * s), k='w') + garis((x - 7 * s, bawah - 29 * s), (x + 7 * s, bawah - 29 * s), k='w'))


def jam_pasir(x, y, s=1.0):
    return (kotak(x - 24 * s, y - 40 * s, 48 * s, 7 * s, 'h') + kotak(x - 24 * s, y + 33 * s, 48 * s, 7 * s, 'h')
            + jalur(f'M{f(x - 18 * s)} {f(y - 33 * s)} L{f(x + 18 * s)} {f(y - 33 * s)} L{f(x + 3 * s)} {f(y)} L{f(x + 18 * s)} {f(y + 33 * s)} L{f(x - 18 * s)} {f(y + 33 * s)} L{f(x - 3 * s)} {f(y)} Z', 'p')
            + bentuk((x - 10 * s, y + 33 * s), (x + 10 * s, y + 33 * s), (x, y + 18 * s), k='h') + bentuk((x - 10 * s, y - 24 * s), (x + 10 * s, y - 24 * s), (x, y - 6 * s), k='h'))


def palang(x, y, s=1.0):
    return kotak(x - 8 * s, y - 24 * s, 16 * s, 48 * s, 'h') + kotak(x - 24 * s, y - 8 * s, 48 * s, 16 * s, 'h')


def kue_ultah(x, bawah, lilin='', s=1.0):
    o = kotak(x - 60 * s, bawah - 50 * s, 120 * s, 50 * s, 'p', 4) + jalur(f'M{f(x - 60 * s)} {f(bawah - 36 * s)} ' + ''.join(
        f'q{f(7.5 * s)} {f(12 * s)} {f(15 * s)} 0 ' for _ in range(8)), 'g') + kotak(x - 70 * s, bawah, 140 * s, 6 * s, 'h')
    if lilin:
        o += teks(x, bawah - 58 * s, lilin, 44 * s, angka=True)
        o += jalur(f'M{f(x - 4 * s)} {f(bawah - 104 * s)} q{f(-6 * s)} {f(-10 * s)} {f(4 * s)} {f(-20 * s)} q{f(6 * s)} {f(12 * s)} {f(-4 * s)} {f(20 * s)} Z', 'h')
    return o


def hewan_sapi(x, y, s=1.0):
    o = kotak(x - 60 * s, y - 40 * s, 110 * s, 56 * s, 'p', 20 * s)
    o += jalur(f'M{f(x - 20 * s)} {f(y - 40 * s)} q{f(10 * s)} {f(20 * s)} {f(30 * s)} {f(8 * s)} q{f(14 * s)} {f(-8 * s)} {f(8 * s)} {f(-8 * s)} Z', 'h')
    o += bulat(x - 36 * s, y + 2 * s, 12 * s, 'h')
    for dx in (-48, -22, 20, 38):
        o += garis((x + dx * s, y + 14 * s), (x + dx * s, y + 50 * s), lebar=7 * s)
    o += elips(x + 66 * s, y - 32 * s, 24 * s, 20 * s, 'p') + elips(x + 78 * s, y - 24 * s, 12 * s, 9 * s, 'a')
    o += jalur(f'M{f(x + 52 * s)} {f(y - 48 * s)} q{f(-8 * s)} {f(-16 * s)} {f(4 * s)} {f(-20 * s)} M{f(x + 78 * s)} {f(y - 50 * s)} q{f(8 * s)} {f(-14 * s)} {f(-2 * s)} {f(-20 * s)}', 'g')
    o += bulat(x + 64 * s, y - 38 * s, 3 * s, 'h') + garis((x - 60 * s, y - 30 * s), (x - 74 * s, y + 6 * s), lebar=3)
    return o


def hewan_babi(x, y, s=1.0):
    o = elips(x, y - 14 * s, 62 * s, 40 * s, 'p')
    for dx in (-40, -16, 16, 40):
        o += garis((x + dx * s, y + 18 * s), (x + dx * s, y + 44 * s), lebar=8 * s)
    o += bulat(x + 58 * s, y - 24 * s, 30 * s, 'p') + elips(x + 84 * s, y - 18 * s, 13 * s, 10 * s, 'p')
    o += bulat(x + 80 * s, y - 18 * s, 2.4 * s, 'h') + bulat(x + 88 * s, y - 18 * s, 2.4 * s, 'h') + bulat(x + 62 * s, y - 34 * s, 3 * s, 'h')
    o += bentuk((x + 42 * s, y - 50 * s), (x + 50 * s, y - 68 * s), (x + 60 * s, y - 52 * s), k='h')
    o += jalur(f'M{f(x - 62 * s)} {f(y - 18 * s)} q{f(-14 * s)} {f(-6 * s)} {f(-8 * s)} {f(-16 * s)} q{f(6 * s)} {f(-4 * s)} {f(2 * s)} {f(6 * s)}', 'g')
    return o


def hewan_ayam(x, y, s=1.0):
    o = jalur(f'M{f(x - 50 * s)} {f(y - 40 * s)} Q{f(x - 60 * s)} {f(y + 20 * s)} {f(x)} {f(y + 20 * s)} Q{f(x + 46 * s)} {f(y + 20 * s)} {f(x + 44 * s)} {f(y - 20 * s)} '
              f'L{f(x + 40 * s)} {f(y - 60 * s)} Q{f(x + 28 * s)} {f(y - 78 * s)} {f(x + 14 * s)} {f(y - 60 * s)} L{f(x + 10 * s)} {f(y - 26 * s)} Q{f(x - 20 * s)} {f(y - 24 * s)} {f(x - 50 * s)} {f(y - 40 * s)} Z', 'p')
    o += jalur(f'M{f(x - 50 * s)} {f(y - 40 * s)} l{f(-10 * s)} {f(-26 * s)} l{f(14 * s)} {f(10 * s)} l{f(4 * s)} {f(-22 * s)} l{f(8 * s)} {f(24 * s)} Z', 'h')
    o += jalur(f'M{f(x + 20 * s)} {f(y - 72 * s)} q{f(4 * s)} {f(-14 * s)} {f(12 * s)} {f(-6 * s)} q{f(6 * s)} {f(-8 * s)} {f(10 * s)} {f(4 * s)} Z', 'h')
    o += bentuk((x + 44 * s, y - 62 * s), (x + 58 * s, y - 56 * s), (x + 44 * s, y - 52 * s), k='h') + bulat(x + 30 * s, y - 62 * s, 3 * s, 'h')
    o += garis((x - 6 * s, y + 20 * s), (x - 10 * s, y + 46 * s), (x - 20 * s, y + 50 * s)) + garis((x + 12 * s, y + 20 * s), (x + 12 * s, y + 46 * s), (x + 2 * s, y + 50 * s))
    return o


def toko(x, lantai_y=LANTAI, w=170, h=120):
    o = kotak(x - w / 2, lantai_y - h, w, h, 'p') + kotak(x - w / 2 - 8, lantai_y - h - 10, w + 16, 12, 'h')
    o += ''.join(jalur(f'M{f(x - w / 2 - 8 + i * (w + 16) / 6)} {f(lantai_y - h + 2)} q{f((w + 16) / 12)} {f(20)} {f((w + 16) / 6)} 0', 'h' if i % 2 == 0 else 'p') for i in range(6))
    o += kotak(x - w / 2 + 14, lantai_y - h + 40, 56, 44, 'p') + kotak(x + 14, lantai_y - 80, 44, 80, 'p') + bulat(x + 50, lantai_y - 40, 3, 'h')
    return o


def tas_belanja(x, bawah, s=1.0):
    return (kotak(x - 22 * s, bawah - 50 * s, 44 * s, 50 * s, 'a', 3) + jalur(f'M{f(x - 10 * s)} {f(bawah - 50 * s)} q0 {f(-18 * s)} {f(10 * s)} {f(-18 * s)} q{f(10 * s)} 0 {f(10 * s)} {f(18 * s)}', 'g'))


def dompet(x, y, s=1.0):
    return (kotak(x - 50 * s, y - 34 * s, 100 * s, 68 * s, 'h', 8 * s) + kotak(x + 14 * s, y - 14 * s, 44 * s, 28 * s, 'p', 6 * s)
            + bulat(x + 30 * s, y, 4 * s, 'h') + jalur(f'M{f(x - 50 * s)} {f(y - 20 * s)} L{f(x + 14 * s)} {f(y - 20 * s)}', 'w'))


def lonceng(x, y, s=1.0):
    return (jalur(f'M{f(x - 36 * s)} {f(y + 30 * s)} Q{f(x - 30 * s)} {f(y + 22 * s)} {f(x - 28 * s)} {f(y)} Q{f(x - 26 * s)} {f(y - 36 * s)} {f(x)} {f(y - 38 * s)} '
                  f'Q{f(x + 26 * s)} {f(y - 36 * s)} {f(x + 28 * s)} {f(y)} Q{f(x + 30 * s)} {f(y + 22 * s)} {f(x + 36 * s)} {f(y + 30 * s)} Z', 'h')
            + bulat(x, y + 38 * s, 7 * s, 'h') + kotak(x - 5 * s, y - 50 * s, 10 * s, 12 * s, 'h')
            + jalur(f'M{f(x - 52 * s)} {f(y - 20 * s)} q{f(-8 * s)} {f(14 * s)} 0 {f(28 * s)} M{f(x + 52 * s)} {f(y - 20 * s)} q{f(8 * s)} {f(14 * s)} 0 {f(28 * s)} '
                    f'M{f(x - 64 * s)} {f(y - 28 * s)} q{f(-12 * s)} {f(22 * s)} 0 {f(44 * s)} M{f(x + 64 * s)} {f(y - 28 * s)} q{f(12 * s)} {f(22 * s)} 0 {f(44 * s)}', 'g'))


def rambu_halte(x, lantai_y=LANTAI):
    return (garis((x, lantai_y), (x, lantai_y - 150), lebar=6) + kotak(x - 34, lantai_y - 176, 68, 56, 'p', 6)
            + kotak(x - 24, lantai_y - 168, 48, 30, 'h', 5) + kotak(x - 18, lantai_y - 162, 16, 12, 'n') + kotak(x + 2, lantai_y - 162, 16, 12, 'n')
            + bulat(x - 14, lantai_y - 134, 5, 'h') + bulat(x + 14, lantai_y - 134, 5, 'h'))


def stasiun(x, lantai_y=LANTAI, w=120, h=90):
    return (bentuk((x - w / 2 - 12, lantai_y - h), (x, lantai_y - h - 34), (x + w / 2 + 12, lantai_y - h), k='h')
            + kotak(x - w / 2, lantai_y - h, w, h, 'p') + kotak(x - 18, lantai_y - 56, 36, 56, 'h')
            + bulat(x, lantai_y - h + 16, 11, 'p') + garis((x, lantai_y - h + 16), (x, lantai_y - h + 9), k='t') + garis((x, lantai_y - h + 16), (x + 5, lantai_y - h + 16), k='t')
            + kotak(x - w / 2 + 10, lantai_y - 60, 22, 26, 'p') + kotak(x + w / 2 - 32, lantai_y - 60, 22, 26, 'p'))


def rumah_sakit(x, lantai_y=LANTAI, w=150, h=110):
    return (kotak(x - w / 2, lantai_y - h, w, h, 'p') + palang(x, lantai_y - h + 28, .8)
            + kotak(x - 22, lantai_y - 52, 44, 52, 'a') + garis((x, lantai_y - 52), (x, lantai_y))
            + kotak(x - w / 2 + 12, lantai_y - 60, 26, 24, 'p') + kotak(x + w / 2 - 38, lantai_y - 60, 26, 24, 'p'))


def sofa(x, lantai_y=LANTAI, w=170):
    return (kotak(x - w / 2, lantai_y - 90, w, 50, 'a', 12) + kotak(x - w / 2 - 12, lantai_y - 64, 26, 50, 'a', 10)
            + kotak(x + w / 2 - 14, lantai_y - 64, 26, 50, 'a', 10) + kotak(x - w / 2 + 12, lantai_y - 48, w - 24, 26, 'p', 6)
            + garis((x - w / 2, lantai_y - 14), (x - w / 2, lantai_y), lebar=5) + garis((x + w / 2, lantai_y - 14), (x + w / 2, lantai_y), lebar=5))


def kuda_gambar(x, lantai_y=LANTAI):
    """Papan lukis (easel) dengan kanvas bergambar bunga."""
    return (garis((x - 30, lantai_y), (x, lantai_y - 150), (x + 30, lantai_y), lebar=5) + garis((x, lantai_y - 150), (x, lantai_y - 10), lebar=4)
            + kotak(x - 40, lantai_y - 140, 80, 70, 'p') + kotak(x - 46, lantai_y - 70, 92, 7, 'h') + bunga(x - 10, lantai_y - 118, .8) + matahari(x + 20, lantai_y - 122, 7))


def sendi(x, kaki=LANTAI, tinggi=150, jenis='pria', duduk=None, badan=1.0):
    """Titik tubuh orang() — untuk meletakkan benda di tangan/kepala. Kembalikan dict r, cy (pusat kepala), bahu, lb, pinggang."""
    anak = jenis in ('laki', 'gadis', 'bayi')
    r = tinggi * (0.12 if anak else 0.085)
    cy = kaki - tinggi + r
    bahu = cy + r * 1.35
    lb = r * (1.9 if jenis in ('wanita', 'gadis', 'nenek') else 2.2) * badan
    pinggang = bahu + tinggi * (0.3 if not anak else 0.26)
    if duduk:
        dy = duduk - pinggang
        cy, bahu, pinggang = cy + dy, bahu + dy, duduk
    return {'r': r, 'cy': cy, 'bahu': bahu, 'lb': lb, 'pinggang': pinggang}


def tangan_di(x, s_, sisi, dx, dy):
    """Posisi akhir tangan: sisi -1 = kiri, 1 = kanan; dx keluar dari bahu, dy dari bahu."""
    return (x + sisi * s_['lb'] / 2 + sisi * dx, s_['bahu'] + 3 + dy)


def payung(x, y, r=60):
    return (jalur(f'M{f(x - r)} {f(y)} Q{f(x - r)} {f(y - r * .9)} {f(x)} {f(y - r * .9)} Q{f(x + r)} {f(y - r * .9)} {f(x + r)} {f(y)} '
                  f'q{f(-r / 6)} {f(-10)} {f(-r / 3)} 0 q{f(-r / 6)} {f(-10)} {f(-r / 3)} 0 q{f(-r / 6)} {f(-10)} {f(-r / 3)} 0 '
                  f'q{f(-r / 6)} {f(-10)} {f(-r / 3)} 0 q{f(-r / 6)} {f(-10)} {f(-r / 3)} 0 q{f(-r / 6)} {f(-10)} {f(-r / 3)} 0 Z', 'h')
            + garis((x, y - r * .9), (x, y + r * .95), lebar=3.5) + jalur(f'M{f(x)} {f(y + r * .95)} q0 {f(10)} {f(-9)} {f(10)}', 'g', 3.5))


def gulungan_film(x, y, r=26):
    o = bulat(x, y, r, 'h')
    for i in range(5):
        a = math.radians(i * 72 - 90)
        o += bulat(x + math.cos(a) * r * .55, y + math.sin(a) * r * .55, r * .2, 'n')
    return o + bulat(x, y, r * .12, 'n')


def mimbar(x, lantai_y=LANTAI):
    return bentuk((x - 34, lantai_y - 100), (x + 34, lantai_y - 100), (x + 26, lantai_y), (x - 26, lantai_y), k='a') + kotak(x - 40, lantai_y - 108, 80, 10, 'h')


def teko(x, bawah, s=1.0):
    return (jalur(f'M{f(x - 36 * s)} {f(bawah)} Q{f(x - 50 * s)} {f(bawah - 50 * s)} {f(x)} {f(bawah - 54 * s)} Q{f(x + 50 * s)} {f(bawah - 50 * s)} {f(x + 36 * s)} {f(bawah)} Z', 'p')
            + jalur(f'M{f(x - 42 * s)} {f(bawah - 36 * s)} L{f(x - 70 * s)} {f(bawah - 56 * s)} L{f(x - 64 * s)} {f(bawah - 30 * s)}', 'g')
            + jalur(f'M{f(x + 40 * s)} {f(bawah - 40 * s)} q{f(24 * s)} {f(0)} {f(10 * s)} {f(28 * s)}', 'g', 5)
            + elips(x, bawah - 54 * s, 18 * s, 5 * s, 'h') + bulat(x, bawah - 62 * s, 5 * s, 'h'))


def kotak_susu(x, bawah, s=1.0):
    return (kotak(x - 20 * s, bawah - 70 * s, 40 * s, 70 * s, 'p') + bentuk((x - 20 * s, bawah - 70 * s), (x, bawah - 88 * s), (x + 20 * s, bawah - 70 * s), k='p')
            + kotak(x - 20 * s, bawah - 50 * s, 40 * s, 26 * s, 'a') + jalur(f'M{f(x - 10 * s)} {f(bawah - 37 * s)} q{f(10 * s)} {f(-10 * s)} {f(20 * s)} 0', 'w'))
