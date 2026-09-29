"""Ganti kode rahasia pembuka versi Indonesia di js/lang.js (yang disimpan hanya hash-nya).
Pakai: py _kerja/kode_bahasa.py <kode baru>     (huruf besar/kecil dianggap sama, minimal 4 karakter)"""
import re, sys
from pathlib import Path


def cyrb53(s, seed=0):
    # sama dengan cyrb53 di js/media.js (per unit UTF-16)
    M = 0xFFFFFFFF
    imul = lambda a, b: (a * b) & M
    h1, h2 = 0xdeadbeef ^ seed, 0x41c6ce57 ^ seed
    b = s.encode('utf-16-le')
    for i in range(0, len(b), 2):
        unit = b[i] | b[i + 1] << 8
        h1 = imul(h1 ^ unit, 2654435761)
        h2 = imul(h2 ^ unit, 1597334677)
    h1 = imul(h1 ^ (h1 >> 16), 2246822507)
    h1 ^= imul(h2 ^ (h2 >> 13), 3266489909)
    h2 = imul(h2 ^ (h2 >> 16), 2246822507)
    h2 ^= imul(h1 ^ (h1 >> 13), 3266489909)
    return 4294967296 * (2097151 & h2) + (h1 & M)


def base36(n):
    d = '0123456789abcdefghijklmnopqrstuvwxyz'
    out = ''
    while True:
        n, r = divmod(n, 36)
        out = d[r] + out
        if not n:
            return out


def main():
    if len(sys.argv) != 2 or len(sys.argv[1].strip()) < 4 or '/' in sys.argv[1]:
        sys.exit(__doc__)
    kode = sys.argv[1].strip().lower()
    f = Path(__file__).resolve().parent.parent / 'js' / 'lang.js'
    src = f.read_text(encoding='utf-8')
    new = re.sub(r"(/\* KODE \*/ HASH: ')[0-9a-z]+(')", lambda m: m.group(1) + base36(cyrb53('lang|' + kode)) + m.group(2), src)
    f.write_text(new, encoding='utf-8')
    print(f'Kode diganti. Komputer: ketik "{kode}". HP: buka alamat app + #/{kode}')


if __name__ == '__main__':
    main()
