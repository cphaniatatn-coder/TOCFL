"""Sisipkan blok adegan ke adegan_vol<N>.py tepat sebelum blok 單元 berikutnya, lalu render SVG 單元 itu.
py _kerja/soal_ai/sisip_adegan.py A03 blok.py   (blok diberi penanda '# --- <KODE> tulis ulang'; blok lama dengan penanda sama diganti)"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.dirname(HERE)
sys.path.insert(0, K)
kode, blok = sys.argv[1], open(sys.argv[2], encoding='utf-8').read().rstrip() + '\n\n'
v = {'A': 1, 'B': 2, 'C': 3}[kode[0]]
p = f'{K}/adegan_vol{v}.py'
s = open(p, encoding='utf-8').read()
tanda = f'# --- {kode} tulis ulang'
if tanda in s:   # ganti blok lama
    a = s.index(tanda)
    m = re.search(r'\n# (?:---|[A-C]\d\d) ', s[a + 5:])
    s = s[:a] + s[a + 5 + m.start() + 1:] if m else s[:a]
nxt = f'{kode[0]}{int(kode[1:]) + 1:02d}'
m = re.search(rf'^# {nxt}\b', s, re.M)
s = s[:m.start()] + blok + s[m.start():] if m else s.rstrip() + '\n\n' + blok
open(p, 'w', encoding='utf-8', newline='').write(s)
import importlib
mod = importlib.import_module(f'adegan_vol{v}')
from svg_lib import bungkus
n = 0
for i, isi in mod.A.items():
    if i.startswith(kode + '-'):
        open(f'{os.path.dirname(K)}/img/soal/{i}.svg', 'w', encoding='utf-8').write(bungkus(isi)); n += 1
print(f'{kode}: {n} SVG ditulis')
