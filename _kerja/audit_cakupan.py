"""Audit cakupan web vs kosakata.xlsx & grammar.xlsx.
Pemakaian: py _kerja/audit_cakupan.py"""
import json, re, openpyxl, collections, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
norm = lambda w: re.sub(r'[\d\s]+$', '', str(w).strip())

# --- data web ---
web_v, web_g = {}, {}
for v in (1, 2, 3):
    d = json.load(open(f'{R}/data/modul_vol{v}.json', encoding='utf-8'))
    for m in d['modules']:
        for layer in ('core', 'supplement'):
            for e in m['vocab'][layer]:
                forms = {norm(e['w'])} | {norm(x) for x in re.split(r'[/／]', e.get('variants', '')) if x}
                for f in forms:
                    web_v.setdefault(f, set()).add((v, m['code']))
        for g in m['grammar']:
            web_g.setdefault(int(g['tbcl_id']), []).append((v, m['code'], g['point']))

# --- kosakata.xlsx ---
print('=== KOSAKATA ===')
wb = openpyxl.load_workbook(f'{R}/kosakata.xlsx', read_only=True)
tot_x = tot_ok = 0
for lv, ws in enumerate(wb.worksheets, 1):
    rows = [r for r in list(ws.iter_rows(values_only=True))[1:] if r[1]]
    miss, lain = [], []
    for r in rows:
        forms = [norm(x) for x in re.split(r'[/／]', str(r[1])) if x.strip()]
        hit = [web_v[f] for f in forms if f in web_v]
        if not hit:
            miss.append(str(r[1]))
        elif not any(v == lv for h in hit for v, _ in h):
            lain.append(f"{r[1]}→Vol{sorted({v for h in hit for v, _ in h})}")
    ok = len(rows) - len(miss)
    tot_x += len(rows); tot_ok += ok
    print(f'Level {lv} ({ws.title}): {len(rows)} baris di xlsx | ada di web: {ok} | TIDAK ada: {len(miss)} | ada tapi di volume lain: {len(lain)}')
    if miss: print('   tidak ada:', ' '.join(miss))
    if lain: print('   volume lain:', ' '.join(lain))
print(f'TOTAL: {tot_ok}/{tot_x} baris kosakata.xlsx tercakup di web')

# --- grammar.xlsx ---
print('\n=== GRAMMAR ===')
wb = openpyxl.load_workbook(f'{R}/grammar.xlsx', read_only=True)
tot_x = tot_ok = 0
semua_id = set()
for lv, ws in enumerate(wb.worksheets, 1):
    rows = [r for r in list(ws.iter_rows(values_only=True))[1:] if r[0]]
    miss, lain, dobel = [], [], []
    for r in rows:
        i = int(r[0]); semua_id.add(i)
        h = web_g.get(i)
        if not h:
            miss.append(f'#{i} {r[1]}')
            continue
        if not any(v == lv for v, _, _ in h):
            lain.append(f'#{i} {r[1]}→{h[0][1]}')
        if len(h) > 1:
            dobel.append(f"#{i}×{len(h)} ({', '.join(c for _, c, _ in h)})")
    ok = len(rows) - len(miss)
    tot_x += len(rows); tot_ok += ok
    print(f'Level {lv} ({ws.title}): {len(rows)} poin di xlsx | ada di web: {ok} | TIDAK ada: {len(miss)} | volume lain: {len(lain)} | diajarkan >1×: {len(dobel)}')
    for lab, xs in (('tidak ada', miss), ('volume lain', lain), ('lebih dari sekali', dobel)):
        if xs: print(f'   {lab}:', '; '.join(xs))
asing = sorted(set(web_g) - semua_id)
print(f'TOTAL: {tot_ok}/{tot_x} poin grammar.xlsx tercakup di web')
if asing: print('Poin di web yang TIDAK ada di grammar.xlsx:', asing)

# --- cek nama poin: tbcl_id web vs 語法點 xlsx ---
nama = {}
for ws in wb.worksheets:
    for r in list(ws.iter_rows(values_only=True))[1:]:
        if r[0]: nama[int(r[0])] = str(r[1])
beda = [(i, nama[i], h[0][2]) for i, h in sorted(web_g.items()) if i in nama and nama[i].split('（')[0][:2] not in h[0][2]]
print(f'\nContoh pencocokan nomor→nama (untuk memastikan penomoran sama), {len(beda)} yang namanya tidak mirip:')
for i, a, b in beda[:25]:
    print(f'   #{i}: xlsx「{a}」  web「{b[:40]}」')
