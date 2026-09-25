"""Rakit bank soal Tes Bab: _kerja/bank/*.json → data/bank_soal.json

Tiap bab = 10 butir bergaya TOCFL Band A (lihat analisis-ujian-tocfl.md):
  聽力 P1 ×2  gambar (3 opsi)            listen_pick
  聽力 P2 ×1  tanya-jawab 2 baris → gambar  listen_dialog (opsi gambar)
  聽力 P3 ×1  dialog 4 baris + 問 → gambar   listen_dialog (opsi gambar)
  聽力 P4 ×1  dialog 4 baris + 問 → A–D teks listen_dialog (4 opsi teks)
  閱讀 P1 ×1  kalimat → 3 gambar            read_sent
  閱讀 P2 ×1  gambar → 3 kalimat            read_pick
  閱讀 P3 ×1  gambar + kalimat rumpang      read_gap
  閱讀 P4 ×1  paragraf, 5 titik + 6 frasa   cloze  (A0: 3–5 titik, tetap n+1 opsi)
  閱讀 P5 ×1  wacana pendek + 1 soal, A–D   read_mc (4 opsi)
Semua teks Mandarin dicek dengan pemeriksa kosakata modul (hanya kata yang sudah
diajarkan sampai bab itu).

Pemakaian:  py _kerja/bangun_bank.py
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bangun_modul import cek_soal, urut_part
import cek_dialog as cd

K = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(K)
POLA = ['聽力 Part 1', '聽力 Part 1', '聽力 Part 2', '聽力 Part 3', '聽力 Part 4',
        '閱讀 Part 1', '閱讀 Part 2', '閱讀 Part 3', '閱讀 Part 4', '閱讀 Part 5']


def cek_bentuk(code, ts):
    salah = []
    parts = sorted(t['part'][:9] for t in ts)
    if parts != sorted(POLA):
        salah.append(f'komposisi bagian tidak sesuai pola 10 butir: {parts}')
    for t in ts:
        p, pic = t['part'][:9], all(isinstance(o, dict) for o in t.get('options', []))
        if p in ('聽力 Part 2', '聽力 Part 3') and (t['type'] != 'listen_dialog' or not pic or len(t['options']) != 3):
            salah.append(f'{p}: harus listen_dialog dengan 3 opsi gambar')
        if p == '聽力 Part 2' and len(t.get('lines', [])) != 2:
            salah.append('聽力 Part 2: dialog harus 2 baris (tanya-jawab)')
        if p in ('聽力 Part 3', '聽力 Part 4') and len(t.get('lines', [])) != 4:
            salah.append(f'{p}: dialog harus 4 baris')
        if p in ('聽力 Part 4', '閱讀 Part 5') and (pic or len(t['options']) != 4):
            salah.append(f'{p}: harus 4 opsi teks (A–D)')
        if p == '閱讀 Part 4':
            n = len(t['answers'])
            if not (code.startswith('A') and 3 <= n <= 5) and n != 5:
                salah.append(f'閱讀 Part 4: harus 5 titik kosong (A0 boleh 3–5), dapat {n}')
    return [f'{code}: {s}' for s in salah]


def main():
    src = {}
    d = f'{K}/bank'
    for fn in sorted(os.listdir(d)):
        if fn.endswith('.json'):
            for code, ts in json.load(open(f'{d}/{fn}', encoding='utf-8')).items():
                if code in src:
                    sys.exit(f'Bab {code} ganda di bank/{fn}')
                src[code] = ts
    mods = cd.urutan()
    urut = [m for m, _ in mods]
    resmi = cd.semua_kata()
    diterima = {tuple(l.split('|')[:2]) for l in open(f'{K}/cek_diterima.txt', encoding='utf-8')
                if l.strip() and not l.startswith('#')}
    masalah, out = [], {}
    for code in sorted(src, key=urut.index):
        ts = sorted(src[code], key=urut_part)
        for t in ts:
            masalah += cek_soal(code, t)
        masalah += cek_bentuk(code, ts)
        ok = cd.kosakata_sampai(code, mods)
        for s in cd.teks(ts):
            for ch in cd.cek(s, ok):
                masalah.append(f'{code}: 「{ch}」 belum diajarkan — di: {s[:40]}')
            for w in resmi - ok:
                if w in s and (code, w) not in diterima and not any(len(k) > len(w) and w in k and k in s for k in ok):
                    masalah.append(f'{code}: ⚠ kata resmi 「{w}」 belum diajarkan — di: {s[:40]}')
        for i, t in enumerate(ts):
            t['id'] = f'{code}-{i + 1:02d}'
        out[code] = ts
    for m in masalah:
        print('  ✗', m)
    json.dump(out, open(f'{ROOT}/data/bank_soal.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n = sum(len(v) for v in out.values())
    print(f'Bank soal: {len(out)} bab, {n} butir. {"0 masalah" if not masalah else str(len(masalah)) + " masalah"}')
    sys.exit(1 if masalah else 0)


if __name__ == '__main__':
    main()
