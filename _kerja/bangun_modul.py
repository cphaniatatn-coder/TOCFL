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
    cocok = lambda o: o['w'] == w or w in o['w'].split('/')
    o = next((o for o in tb if o['lv'] == lv and cocok(o)), None) or next(o for o in tb if cocok(o))
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
        e['note'] = f"義項 ini = {sense.replace('-', ' ')}."
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


BENTUK = {  # tipe soal → kolom wajib selain PART
    'listen_pick': {'audio', 'options', 'answer'}, 'listen_reply': {'audio', 'options', 'answer'},
    'listen_dialog': {'lines', 'question', 'options', 'answer'},
    'read_sent': {'text', 'options', 'answer'}, 'read_pick': {'picture', 'options', 'answer'},
    'read_gap': {'picture', 'text', 'options', 'answer'}, 'read_mc': {'text', 'question', 'options', 'answer'},
    'cloze': {'text', 'options', 'answers'},
}


def urut_part(t):
    m = re.match(r'(聽力|閱讀) Part (\d)', t['part'])
    return (0 if m.group(1) == '聽力' else 1, int(m.group(2)))


def cek_soal(code, t):
    """Kembalikan daftar masalah format pada satu soal."""
    salah = []
    if t.get('type') not in BENTUK:
        return [f"tipe tidak dikenal: {t.get('type')}"]
    kurang = (BENTUK[t['type']] | {'part', 'instr', 'why'}) - set(t)
    if kurang:
        salah.append(f"kolom kurang: {sorted(kurang)}")
    if not re.match(r'(聽力|閱讀) Part \d · ', t.get('part', '')):
        salah.append(f"part tidak baku: {t.get('part')}")
    opts = t.get('options', [])
    if t['type'] == 'cloze':
        n = len(re.findall(r'（\d）', t.get('text', '')))
        if n != len(t.get('answers', [])) or len(opts) != n + 1 or len(set(t.get('answers', []))) != n:
            salah.append('cloze: jumlah titik/jawaban/opsi tidak cocok (opsi = titik + 1)')
    elif not (0 <= t.get('answer', -1) < len(opts)):
        salah.append('indeks jawaban di luar opsi')
    if t['type'] in ('listen_pick', 'read_sent') and not all(isinstance(o, dict) and o.get('icon') for o in opts):
        salah.append('opsi harus gambar {icon, label}')
    if t['type'] == 'read_gap' and len(re.findall(r'（\s*）', t.get('text', ''))) != 1:
        salah.append('read_gap: harus tepat satu （　）')
    if len({json.dumps(o, ensure_ascii=False) for o in opts}) != len(opts):
        salah.append('ada opsi kembar')
    return [f'{code}: {s}' for s in salah]


def load_soal():
    """Soal tambahan di _kerja/soal/*.json: {"A01": [soal, ...], ...}"""
    out = {}
    d = f'{K}/soal'
    for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if fn.endswith('.json'):
            for code, ts in json.load(open(f'{d}/{fn}', encoding='utf-8')).items():
                out.setdefault(code, []).extend(ts)
    return out


def main():
    isi = load_isi()
    soal = load_soal()
    masalah = []
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
            # soal inti + soal tambahan, diurutkan seperti ujian: 聽力 P1→P4, lalu 閱讀 P1→P5
            m['tasks'] = sorted(m.get('tasks', []) + soal.pop(code, []), key=urut_part)
            for t in m['tasks']:
                masalah += cek_soal(code, t)
            m['vocab'] = {'core': [entry(lv, t, ov) for t in f[5].split()],
                          'supplement': [entry(lv, t, ov) for t in (f[6].split() if len(f) > 6 else [])]}
            mods.append(m)
        t, s, a = HEAD[lv]
        json.dump({'volume': lv, 'title': t, 'subtitle': s, 'approach': a, 'modules': mods},
                  open(f'{ROOT}/data/modul_vol{lv}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        total[lv] = len(mods)
    print('Modul terakit:', total)
    masalah += [f'{c}: soal tambahan untuk modul yang tidak ada' for c in soal]
    for s in masalah:
        print('   ✗ format soal —', s)
    if masalah:
        sys.exit(1)
    r = subprocess.run([sys.executable, f'{K}/cek_dialog.py'] + [f'{ROOT}/data/modul_vol{lv}.json' for lv in (1, 2, 3)])
    sys.exit(r.returncode)


if __name__ == '__main__':
    main()
