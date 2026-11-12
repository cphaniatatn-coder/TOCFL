"""Profil gaya 情境對話 di 138 單元 — untuk melihat apakah gayanya seragam & di mana tanda "kaku".
Indikator (heuristik, bukan penilaian akhir):
- panjang: adegan, baris, hanzi per baris
- partikel akhir kalimat lisan (啊 吧 呢 喔 啦 嘛 耶 欸 哦 呀)
- penanda wacana (對了 那 好啊 是嗎 真的嗎 沒問題 好吧 不過 其實 欸)
- "jawaban gema": jawaban mengulang kata kerja/objek pertanyaan secara utuh (mis. 你喜歡X嗎？我喜歡X。)
- kepadatan 很 + adj, kata ganti 我/你 di awal baris, sapaan nama di awal baris
- baris yang sama persis muncul di banyak 單元 (formula)
Pemakaian: py _kerja/profil_dialog.py
"""
import json, re, sys, collections, statistics as st
sys.stdout.reconfigure(encoding='utf-8')
CJK = re.compile(r'[一-鿿]')
PART = '啊吧呢喔啦嘛耶欸哦呀'
WACANA = ['對了', '好啊', '是嗎', '真的嗎', '沒問題', '好吧', '不過', '其實', '那就', '那我們', '欸', '哇', '咦', '嗯', '唉']

mods = []
for v in (1, 2, 3):
    mods += json.load(open(f'data/modul_vol{v}.json', encoding='utf-8'))['modules']

rows, semua_baris = [], collections.Counter()
for m in mods:
    lines = [l for d in m['dialogs'] for l in d['lines']]
    zh = [l['zh'] for l in lines]
    n = len(zh)
    hz = [len(CJK.findall(s)) for s in zh]
    # partikel di akhir klausa (sebelum tanda baca atau akhir)
    part = sum(len(re.findall(f'[{PART}][。！？，～…!?,]*$|[{PART}][，。！？]', s)) for s in zh)
    wac = sum(any(s.startswith(w) or ('，' + w) in s for w in WACANA) for s in zh)
    # jawaban gema: baris berikut (pembicara beda) memuat >=4 hanzi berturut-turut dari pertanyaan
    gema = 0
    for a, b in zip(lines, lines[1:]):
        if a['sp'] != b['sp'] and re.search(r'[嗎？?]', a['zh']):
            q = ''.join(CJK.findall(re.sub(r'嗎.*', '', a['zh'])))
            if any(q[i:i + 4] in b['zh'] for i in range(max(0, len(q) - 3))):
                gema += 1
    hen = sum(s.count('很') for s in zh)
    pron = sum(bool(re.match(r'^(我|你|妳|您)', s)) for s in zh)
    for s in zh:
        semua_baris[s] += 1
    rows.append(dict(code=m['code'], lvl=m['code'][0], adegan=len(m['dialogs']), baris=n,
                     hz=st.mean(hz) if hz else 0, part=part / n if n else 0, wac=wac / n if n else 0,
                     gema=gema, hen=hen / n if n else 0, pron=pron / n if n else 0,
                     tokoh=len({l['sp'] for l in lines})))

LV = {'A': 'A0', 'B': 'A1', 'C': 'A2'}
print('== Rata-rata per level')
print('level | adegan | baris | hanzi/baris | partikel/baris | penanda wacana/baris | jawaban gema/單元 | 很/baris | baris diawali 我/你')
for L in 'ABC':
    r = [x for x in rows if x['lvl'] == L]
    f = lambda k: st.mean(x[k] for x in r)
    print(f"{LV[L]} | {f('adegan'):.1f} | {f('baris'):.1f} | {f('hz'):.1f} | {f('part'):.2f} | {f('wac'):.2f} | {f('gema'):.1f} | {f('hen'):.2f} | {100*f('pron'):.0f}%")

print('\n== Sebaran (min / median / maks) seluruh 138')
for k in ('baris', 'hz', 'part', 'wac', 'gema'):
    v = sorted(x[k] for x in rows)
    print(f'{k}: {v[0]:.2f} / {st.median(v):.2f} / {v[-1]:.2f}')

print('\n== 單元 paling "berisiko kaku" (skor = gema tinggi + partikel & penanda wacana rendah)')
for x in rows:
    x['skor'] = x['gema'] / max(1, x['baris']) * 2 - x['part'] - x['wac']
for x in sorted(rows, key=lambda x: -x['skor'])[:12]:
    print(f"{x['code']}: baris {x['baris']}, gema {x['gema']}, partikel/baris {x['part']:.2f}, wacana/baris {x['wac']:.2f}")
print('\n== 單元 paling "lisan"')
for x in sorted(rows, key=lambda x: x['skor'])[:6]:
    print(f"{x['code']}: baris {x['baris']}, gema {x['gema']}, partikel/baris {x['part']:.2f}, wacana/baris {x['wac']:.2f}")

print('\n== Baris yang sama persis di >=3 單元')
for s, c in semua_baris.most_common(15):
    if c >= 3: print(c, s)

pk = collections.Counter()
for m in mods:
    for d in m['dialogs']:
        for l in d['lines']:
            for ch in re.findall(f'([{PART}])[。！？，～…]', l['zh']):
                pk[ch] += 1
print('\n== Partikel yang dipakai:', pk.most_common())
