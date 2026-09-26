"""Pisahkan pinyin per suku kata (wǎnān → wǎn ān) dengan mencocokkan tiap suku kata ke hanzinya.

Tanpa hanzi, pinyin sering ambigu (wǎnān = wǎn ān 晚安, bukan wǎ nān). Karena itu setiap kata pinyin
dipecah ke semua kemungkinan suku kata yang sah, lalu dipilih potongan yang cocok dengan bacaan
hanzi pada posisi itu (bacaan dari pypinyin, semua bacaan alternatif ikut dipertimbangkan).

    from pinyin import pisah
    teks, masalah = pisah('Wǎnān! Nǐ hǎo.', '晚安！你好。')   # → 'Wǎn ān! Nǐ hǎo.', None

Dipakai oleh bangun_modul.py (kosakata, dialog, judul). Butuh: pip install pypinyin
"""
import re, unicodedata
from functools import lru_cache
from pypinyin import pinyin as _py, Style

NADA = {'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a', 'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e', 'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
        'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o', 'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u', 'ǖ': 'ü', 'ǘ': 'ü', 'ǚ': 'ü', 'ǜ': 'ü',
        'ń': 'n', 'ň': 'n', 'ǹ': 'n', 'ḿ': 'm'}
HURUF = r"A-Za-züÜ" + ''.join(NADA) + ''.join(k.upper() for k in NADA)
KATA = re.compile(rf"[{HURUF}]+(?:['’][{HURUF}]+)*")
HANZI = re.compile(r'[㐀-鿿豈-﫿]')

_INISIAL = 'b p m f d t n l g k h j q x zh ch sh r z c s y w'.split()
_FINAL = ('a o e ai ei ao ou an en ang eng ong er i ia ie iao iu ian in iang ing iong u ua uo uai ui uan un uang ueng '
          'ü üe üan ün ue uan un ê m n ng hm hng').split()


def _suku_sah():
    s = set()
    for i in [''] + _INISIAL:
        for f in _FINAL:
            s.add(i + f)
    s |= {'yi', 'ya', 'ye', 'yao', 'you', 'yan', 'yin', 'yang', 'ying', 'yong', 'wu', 'wa', 'wo', 'wai', 'wei', 'wan', 'wen',
          'wang', 'weng', 'yu', 'yue', 'yuan', 'yun', 'r'}
    return s


SAH = _suku_sah()


def polos(s):
    """Hilangkan tanda nada, huruf kecil (ü tetap ü)."""
    return ''.join(NADA.get(c, c) for c in unicodedata.normalize('NFC', s).lower())


def _nada(s):
    return sum(c in NADA for c in s.lower())


# Bacaan baku Taiwan (教育部) yang tidak dikenal pypinyin (bacaan daratan)
TAIWAN = {'姊': {'jie'}, '和': {'han'}, '垃': {'le'}, '圾': {'se'}}


@lru_cache(maxsize=None)
def bacaan(ch):
    """Semua bacaan (tanpa nada) sebuah hanzi."""
    out = set(TAIWAN.get(ch, ()))
    for r in _py(ch, style=Style.NORMAL, heteronym=True, v_to_u=True)[0]:
        out.add(r)
    return out


def _erhua(p):
    """Untuk suku 兒化 (zhèr, yìdiǎr ← diǎn, wár ← wán): kembalikan bentuk dasar yang mungkin, atau None."""
    if not p.endswith('r') or p in ('r', 'er'):
        return None
    dasar = [p[:-1] + x for x in ('', 'n', 'i', 'ng')]
    dasar = [d for d in dasar if d in SAH]
    return dasar or None


def _potong(kata):
    """Semua cara memecah satu kata pinyin menjadi suku kata sah (maks. 1 tanda nada per suku)."""
    kata = kata.replace("'", '').replace('’', '')
    hasil = []

    def jalan(i, acc):
        if i == len(kata):
            hasil.append(acc); return
        for L in range(min(6, len(kata) - i), 0, -1):
            s = kata[i:i + L]
            p = polos(s)
            if (p in SAH or _erhua(p) is not None) and _nada(s) <= 1:
                jalan(i + L, acc + [s])
    jalan(0, [])
    return hasil


def _cocok(suku, ch, berikut):
    """Apakah suku kata cocok dengan hanzi ch? Kembalikan jumlah hanzi yang dipakai (0 = tidak cocok)."""
    p = polos(suku)
    b = bacaan(ch)
    if p in b:
        return 1
    # 兒化: 這兒 → zhèr (dua hanzi, satu suku)
    if berikut == '兒' and any(d in b for d in (_erhua(p) or [])):
        return 2
    return 0


def pisah(py, zh):
    """Kembalikan (pinyin bersuku terpisah, pesan masalah atau None)."""
    py = unicodedata.normalize('NFC', py).replace('ɑ', 'a')  # alfa Latin (ɑ) kadang terselip di data
    kata = list(KATA.finditer(py))
    hz = HANZI.findall(zh)
    pilihan = [_potong(k.group()) for k in kata]
    # DP: (indeks kata, posisi hanzi) → daftar potongan terpilih
    memo = {}

    def dp(ki, hi):
        if ki == len(kata):
            return [] if hi == len(hz) else None
        if (ki, hi) in memo:
            return memo[(ki, hi)]
        best = None
        for cara in pilihan[ki]:
            j = hi; ok = True
            for s in cara:
                if j >= len(hz):
                    ok = False; break
                n = _cocok(s, hz[j], hz[j + 1] if j + 1 < len(hz) else '')
                if not n:
                    ok = False; break
                j += n
            if ok:
                sisa = dp(ki + 1, j)
                if sisa is not None:
                    best = [cara] + sisa; break
        memo[(ki, hi)] = best
        return best

    susun = dp(0, 0)
    masalah = None
    if susun is None:
        # tidak bisa dicocokkan dengan hanzi: pecah seadanya (potongan pertama) dan laporkan
        susun = [c[0] if c else [k.group()] for c, k in zip(pilihan, kata)]
        n_py = sum(len(c) for c in susun)
        masalah = f'pinyin tidak cocok dengan hanzi ({n_py} suku kata pinyin vs {len(hz)} hanzi)'
    out, akhir = [], 0
    for k, cara in zip(kata, susun):
        out.append(py[akhir:k.start()])
        out.append(' '.join(cara))
        akhir = k.end()
    out.append(py[akhir:])
    return ''.join(out), masalah


if __name__ == '__main__':
    for py, zh in [('wǎnān', '晚安'), ('Zǎo\'ān!', '早安！'), ('nǚér', '女兒'), ('zhèr', '這兒'), ('míngzi', '名字'),
                   ('Nǐ hǎo! Wǒ jiào Wáng Dàwén.', '你好！我叫王大文。'), ('xiǎngyào', '想要'), ('fāngàn', '方案'),
                   ('Hǎo o, wǒmen yìqǐ qù!', '好喔，我們一起去！'), ('yìdiǎr', '一點兒')]:
        print(zh, '→', pisah(py, zh))
