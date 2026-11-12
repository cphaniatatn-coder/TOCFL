"""Bandingkan kosakata.xlsx dengan daftar kata 技術報告《說情話境》(國教院 2020).
Siapkan dulu teks PDF: pdftotext -enc UTF-8 -raw "技術報告：《說情話境-華語文詞語情境分類》.pdf" <folder>/raw.txt
Pemakaian (dari root repo): py _kerja/banding_jishu.py <folder berisi raw.txt>"""
import re, sys, collections, json, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
S = sys.argv[1]
lines = [re.sub(r'[-]', '', l) for l in open(S + '/raw.txt', encoding='utf-8').read().splitlines()]
LV = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5}

# cari awal daftar (kemunculan terakhir "核心詞（2,519）")
start = max(i for i, l in enumerate(lines) if l.strip().startswith('核心詞（2,519）'))
end = next(i for i in range(start, len(lines)) if lines[i].strip().startswith('第三節') and '小結' in lines[i])
cat = '核心詞'; lv = None
pdf = []  # (word, cat, level)
for l in lines[start + 1:end]:
    t = l.strip()
    if not t or re.fullmatch(r'\d+', t):
        continue
    if t.startswith('註') or t.startswith('「') or t in ('、',) or '範疇' in t or '諮詢' in t or '新增' in t:
        continue
    m = re.match(r'^(\d+)\.\s*(\S+?)\s*[（(]\s*[\d,]+\s*[）)]$', t)
    if m:
        cat = m.group(2); lv = None; continue
    m = re.match(r'^第(.)級（[\d,]+）$', t)
    if m:
        lv = LV[m.group(1)]; continue
    if lv is None:
        continue
    for w in re.split(r'\s{2,}', t):
        w = re.sub(r'\s+(?=\d)', '', w).strip()
        if w: pdf.append((w, cat, lv))

# hitung per kategori-level untuk cek parsing
cnt = collections.Counter((c, l) for _, c, l in pdf)
print('PDF total', len(pdf))

def norm(w):
    return re.sub(r'[0-9０-９]+$', '', w.strip())

def variants(w):
    return {norm(x) for x in re.split(r'[/／]', w) if x.strip()}

pidx = collections.defaultdict(list)
for w, c, l in pdf:
    for v in variants(w):
        pidx[v].append((w, c, l))

# Excel
wb = openpyxl.load_workbook('kosakata.xlsx', read_only=True)
rows = []
for ws in wb.worksheets:
    for r in list(ws.iter_rows(values_only=True))[1:]:
        if r and r[1]:
            rows.append(r)
CATN = lambda c: (c or '').replace('、', '').replace('，', '')
res = collections.Counter(); diff_cat = []; diff_lv = []; missing = []; ok = 0
for r in rows:
    w, ji, sit = r[1], r[3], r[4]
    xlv = int(re.search(r'\d', ji).group())
    hits = []
    for v in variants(w):
        hits += pidx.get(v, [])
    hits = list(dict.fromkeys(hits))
    if not hits:
        missing.append((w, ji, sit)); continue
    # pilih yg levelnya sama dulu
    same_lv = [h for h in hits if h[2] == xlv]
    h = (same_lv or hits)[0]
    if not same_lv:
        diff_lv.append((w, ji, sit, h))
    if CATN(h[1]) != CATN(sit):
        diff_cat.append((w, ji, sit, h[1], h[2]))
    else:
        ok += 1
print('Excel rows', len(rows), '| cocok kategori', ok, '| beda kategori', len(diff_cat),
      '| beda level', len(diff_lv), '| tidak ketemu di PDF', len(missing))
print('\n== BEDA KATEGORI (Excel -> PDF)')
for d in diff_cat: print(d)
print('\n== BEDA LEVEL')
for d in diff_lv: print(d)
print('\n== TIDAK KETEMU DI PDF')
for d in missing: print(d)
# PDF level1-3 yang tidak ada di Excel
xw = set()
for r in rows:
    xw |= variants(r[1])
print('\n== PDF level 1-3 tidak ada di Excel')
for w, c, l in pdf:
    if l <= 3 and not (variants(w) & xw):
        print((w, c, l))
print('\nPDF per level:', collections.Counter(l for _, _, l in pdf))
