"""Isi field "zy" (zhuyin per karakter, dipisah spasi) untuk semua kosakata di data/modul_vol*.json dari kolom bopomofo kosakata.xlsx."""
import json, glob, re, openpyxl
bp = {}
for ws in openpyxl.load_workbook('kosakata.xlsx', read_only=True).worksheets:
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[1] and r[8]:
            for w, z in zip(str(r[1]).split('/'), str(r[8]).split('/')):
                bp.setdefault(re.sub(r'\d+$', '', w.strip()), z.strip())
for f in glob.glob('data/modul_vol*.json'):
    d = json.load(open(f, encoding='utf-8')); miss = []
    for m in d['modules']:
        for v in m['vocab']['core'] + m['vocab']['supplement']:
            z = bp.get(v['w'])
            if z and len(z.split()) == len(v['w']): v['zy'] = z
            else: miss.append(v['w'])
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f, 'tanpa zhuyin:', miss)
