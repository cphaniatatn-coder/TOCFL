"""Buat data/rencana.json (peta 138 modul) dari _kerja/plan_L*.txt."""
import json
G = json.load(open('_kerja/grammar.json', encoding='utf-8'))
CAT = {1:'個人資料',2:'日常起居',3:'職業',4:'休閒、娛樂',5:'交通、旅遊',6:'社交、人際',7:'身體、醫療',8:'教育、學習',9:'購物、商店',10:'餐飲、烹飪',11:'公共服務',12:'安全',13:'自然環境',14:'社會',15:'文化',16:'情緒、態度',17:'科技'}
out = {}
for lv in (1, 2, 3):
    gm = {int(x['id']): x['g'] for x in G[f'第{lv}級']}
    mods = []
    for l in open(f'_kerja/plan_L{lv}.txt', encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('|')
        mods.append({'code': f[0], 'title': f[1], 'scene': f[2],
                     'categories': [f'{c}. {CAT[int(c)]}' for c in f[3].split(',')],
                     'grammar': [] if f[4] in ('—', '') else [gm[int(x)] for x in f[4].split(',')],
                     'n_core': len(f[5].split()), 'n_sup': len(f[6].split()) if len(f) > 6 else 0})
    out[lv] = mods
json.dump(out, open('data/rencana.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in out.items()})
