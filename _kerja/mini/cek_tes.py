"""Cek kosakata & pola grammar tes pre/post modul mini.
Batas kosakata: A0 = sampai A25, A1 = sampai B46, A2 = sampai C67.
Pemakaian: py _kerja/mini/cek_tes.py
"""
import json, os, re, sys
K = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, K)
import cek_dialog as cd
from bangun_bank import POLA_GRAMMAR

BATAS = {'A0': 'A25', 'A1': 'B46', 'A2': 'C67'}
mods = cd.urutan()
urut = [m for m, _ in mods]
n = 0
for lv, akhir in BATAS.items():
    ok = cd.kosakata_sampai(akhir, mods)
    T = json.load(open(f'{K}/mini/tes_{lv}.json', encoding='utf-8'))
    for f, items in T.items():
        for t in items:
            for s in cd.teks({k: v for k, v in t.items() if k not in ('tema', 'picture')}):
                bad = cd.cek(s, ok)
                if bad:
                    n += 1
                    print(f'{lv}{f}-{t["no"]}: kata belum diajarkan {bad}: {s}')
                for pola, mulai in POLA_GRAMMAR.items():
                    m = re.search(pola, s)
                    if m and urut.index(mulai) > urut.index(akhir):
                        print(f'{lv}{f}-{t["no"]}: ⚑ pola 「{m.group(0)}」 ({mulai}): {s}')
            if t['type'] == 'cloze':
                if sorted(t['answers']) != sorted(set(t['answers'])) or len(t['options']) != len(t['answers']) + 1:
                    n += 1; print(f'{lv}{f}-{t["no"]}: cloze harus n jawaban unik + 1 opsi lebih')
            elif not 0 <= t['answer'] < len(t['options']):
                n += 1; print(f'{lv}{f}-{t["no"]}: indeks jawaban salah')
print(f'{n} masalah')
