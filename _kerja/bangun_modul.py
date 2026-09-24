"""Rakit data/modul_vol{1,2,3}.json dari:
  - _kerja/plan_L*.txt   → urutan modul, kategori, daftar 核心/補充 (kata@義項)
  - _kerja/isi/<KODE>.json → konten tulisan tangan (adegan, dialog, tugas, grammar)
  - _kerja/tbcl.json (pinyin resmi), kosakata.xlsx (zhuyin), _kerja/arti.json (arti)
Konten boleh memuat "vocab_override": {kata: {meaning, pos, note}}.
Setelah merakit, langsung menjalankan cek_dialog.py.

Pemakaian:  py _kerja/bangun_modul.py
"""
import json, os, re, subprocess, sys
import openpyxl

K = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(K)
CAT = {1:'個人資料',2:'日常起居',3:'職業',4:'休閒、娛樂',5:'交通、旅遊',6:'社交、人際',7:'身體、醫療',8:'教育、學習',9:'購物、商店',10:'餐飲、烹飪',11:'公共服務',12:'安全',13:'自然環境',14:'社會',15:'文化',16:'情緒、態度',17:'科技'}
HEAD = {
    1: ('Volume 1 · A0', 'TBCL 第1級 — 25 adegan, vocabulary-first', 'A0'),
    2: ('Volume 2 · A1', 'TBCL 第2級 — 46 adegan, TBLL 6 tahap', 'TBLL'),
    3: ('Volume 3 · A2', 'TBCL 第3級 — 67 adegan, TBLL 6 tahap', 'TBLL'),
}

tb = json.load(open(f'{K}/tbcl.json', encoding='utf-8'))
arti = json.load(open(f'{K}/arti.json', encoding='utf-8'))
bp = {}
for ws in openpyxl.load_workbook(f'{ROOT}/kosakata.xlsx', read_only=True).worksheets:
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[1] and r[8]:
            for w, z in zip(str(r[1]).split('/'), str(r[8]).split('/')):
                bp.setdefault(re.sub(r'\d+$', '', w.strip()), z.strip())


def entry(lv, token, override):
    w, _, sense = token.partition('@')
    o = next(o for o in tb if o['lv'] == lv and (o['w'] == w or w in o['w'].split('/')))
    parts = o['w'].split('/')
    idx = parts.index(w) if w in parts else 0
    show = re.sub(r'\d+$', '', parts[0] if w == o['w'] else w)
    pys = (o['py'] or '').split('/')
    py = re.sub(r'\s+', '', (pys[idx] if idx < len(pys) else pys[0]).strip())
    a = arti.get(o['w'], {})
    e = {'w': show, 'py': py, 'pos': a.get('pos', ''), 'meaning': a.get('meaning', '')}
    if '/' in o['w'] and w == o['w']:
        e['variants'] = '/'.join(re.sub(r'\d+$', '', p) for p in parts)
    if sense:
        e['note'] = f'義項 ini = {sense}.'
    e.update(override.get(show, {}))
    z = bp.get(show)
    if z and len(z.split()) == len(show):
        e['zy'] = z
    return e


def load_isi():
    isi = {}
    for fn in sorted(os.listdir(f'{K}/isi')):
        if fn.endswith('.json'):
            d = json.load(open(f'{K}/isi/{fn}', encoding='utf-8'))
            for c in (d['modules'] if 'modules' in d else [dict(d, code=fn[:-5])]):
                if c['code'] in isi:
                    sys.exit(f"Modul {c['code']} ganda di isi/{fn}")
                isi[c['code']] = c
    return isi


def main():
    isi = load_isi()
    total = {}
    for lv in (1, 2, 3):
        mods = []
        for line in open(f'{K}/plan_L{lv}.txt', encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            f = line.rstrip('\n').split('|')
            code = f[0]
            if code not in isi:
                continue
            c = {k: v for k, v in isi[code].items() if k != 'code'}
            ov = c.pop('vocab_override', {})
            m = {'code': code, 'title': c.pop('title', f[1]),
                 'categories': [f'{x}. {CAT[int(x)]}' for x in f[3].split(',')]}
            m.update(c)
            m['vocab'] = {'core': [entry(lv, t, ov) for t in f[5].split()],
                          'supplement': [entry(lv, t, ov) for t in (f[6].split() if len(f) > 6 else [])]}
            mods.append(m)
        t, s, a = HEAD[lv]
        json.dump({'volume': lv, 'title': t, 'subtitle': s, 'approach': a, 'modules': mods},
                  open(f'{ROOT}/data/modul_vol{lv}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        total[lv] = len(mods)
    print('Modul terakit:', total)
    r = subprocess.run([sys.executable, f'{K}/cek_dialog.py'] + [f'{ROOT}/data/modul_vol{lv}.json' for lv in (1, 2, 3)])
    sys.exit(r.returncode)


if __name__ == '__main__':
    main()
