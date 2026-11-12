"""Hitung kemunculan ulang (複現率) kosakata per 單元 — metode mengikuti ide 王珊 (2013):
untuk tiap 單元: berapa kata BARU, berapa kata LAMA (diajarkan di 單元 sebelumnya) yang dipakai lagi;
untuk tiap kata: di berapa 單元 sesudahnya ia muncul lagi.

Teks yang dihitung per 單元: dialog, soal latihan (tasks), contoh grammar, dan Tes Bab (bank_soal).
Segmentasi: forward maximum matching memakai kamus semua kata yang diajarkan (+ variannya).
Pemakaian: py _kerja/hitung_kemunculan.py [--csv keluaran.csv]
"""
import json, re, sys, collections, statistics as st
sys.stdout.reconfigure(encoding='utf-8')
CJK = re.compile(r'[一-鿿]')
SKIP_KEYS = {'why', 'instr', 'part', 'label', 'id', 'py', 'title_id', 'meaning', 'explain', 'img', 'icon',
             'zy', 'pos', 'sp', 'type', 'catatan', 'note'}


def teks(obj, out):
    """Kumpulkan string Mandarin (mayoritas hanzi) dari struktur JSON."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in SKIP_KEYS:
                continue
            teks(v, out)
    elif isinstance(obj, list):
        for v in obj:
            teks(v, out)
    elif isinstance(obj, str):
        n = len(CJK.findall(obj))
        if n and n / max(1, len(re.sub(r'\s', '', obj))) > 0.5:
            out.append(obj)


mods = []
for v in (1, 2, 3):
    mods += json.load(open(f'data/modul_vol{v}.json', encoding='utf-8'))['modules']
bank = json.load(open('data/bank_soal.json', encoding='utf-8'))
idx = {m['code']: i for i, m in enumerate(mods)}

# kamus: bentuk -> 單元 pertama yang mengajarkannya
intro = {}
for i, m in enumerate(mods):
    for lay in ('core', 'supplement'):
        for w in m['vocab'][lay]:
            for f in re.split(r'/', re.sub(r'\d+$', '', w['w'])):
                f = re.sub(r'\d+', '', f).strip()
                if f and f not in intro:
                    intro[f] = i
MAXL = max(map(len, intro))


def segment(s):
    s = ''.join(CJK.findall(s)) if False else s
    toks, i = [], 0
    while i < len(s):
        for L in range(min(MAXL, len(s) - i), 0, -1):
            if s[i:i + L] in intro:
                toks.append(s[i:i + L]); i += L; break
        else:
            i += 1
    return toks


rows = []
muncul = collections.defaultdict(set)  # kata -> set 單元 tempat ia muncul
for i, m in enumerate(mods):
    out = []
    teks(m['dialogs'], out); teks(m['tasks'], out)
    for g in m['grammar']:
        teks(g.get('examples', []), out)
    teks(bank.get(m['code'], []), out)
    toks = [t for s in out for t in segment(s)]
    baru = sum(len(m['vocab'][l]) for l in ('core', 'supplement'))
    lama = {t for t in toks if intro[t] < i}
    lama_tok = sum(1 for t in toks if intro[t] < i)
    for t in set(toks):
        muncul[t].add(i)
    rows.append(dict(code=m['code'], lvl=m['code'][0], baru=baru, lama=len(lama), lama_tok=lama_tok,
                     tok=len(toks), rasio=(lama_tok / len(toks) if toks else 0)))

# per kata: jumlah 單元 SESUDAH diperkenalkan tempat ia muncul lagi
ulang = {w: len([u for u in muncul.get(w, ()) if u > intro[w]]) for w in intro}

LV = {'A': 'A0', 'B': 'A1', 'C': 'A2'}
print('== Per 單元 (rata-rata per level)')
for L in 'ABC':
    r = [x for x in rows if x['lvl'] == L]
    print(f"{LV[L]}: kata baru {st.mean(x['baru'] for x in r):.1f} | kata lama dipakai ulang {st.mean(x['lama'] for x in r):.1f}"
          f" (min {min(x['lama'] for x in r)}, maks {max(x['lama'] for x in r)}) | porsi token kata lama {100*st.mean(x['rasio'] for x in r):.0f}%")
print('\n== 單元 dengan kata baru <= 5: berapa kata lama dipakai ulang')
for x in rows:
    if x['baru'] <= 5:
        print(f"{x['code']}: baru {x['baru']}, lama {x['lama']}, token lama {x['lama_tok']}/{x['tok']}")
print('\n== Korelasi kata baru vs kata lama per 單元 (A1+A2)')
r = [x for x in rows if x['lvl'] != 'A']
print(f"r = {st.correlation([x['baru'] for x in r], [x['lama'] for x in r]):.2f}")
print('\n== Per kata: muncul lagi di berapa 單元 sesudahnya')
for L, rng in (('A0', range(0, 25)), ('A1', range(25, 71)), ('A2', range(71, 138))):
    ws = [w for w in intro if intro[w] in rng]
    vals = [ulang[w] for w in ws]
    nol = [w for w in ws if ulang[w] == 0]
    print(f"{L}: {len(ws)} bentuk | median {st.median(vals)} | rata {st.mean(vals):.1f} | tidak pernah muncul lagi: {len(nol)} ({100*len(nol)/len(ws):.0f}%)"
          f" | muncul lagi >=3 單元: {100*sum(v>=3 for v in vals)/len(ws):.0f}%")
nol_c = [w for w in intro if intro[w] >= 71 and ulang[w] == 0]
print('\nContoh kata A2 yang tidak muncul lagi (catatan: A2 = level terakhir, ruang muncul lagi lebih sempit):', nol_c[:40])
if '--csv' in sys.argv:
    import csv
    with open(sys.argv[sys.argv.index('--csv') + 1], 'w', newline='', encoding='utf-8-sig') as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
