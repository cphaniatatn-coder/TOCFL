import json, sys, collections
S=sys.argv[1]; lv=int(sys.argv[2])
tb=json.load(open(S+'/tbcl.json',encoding='utf-8'))
lvw={o['w']:o for o in tb if o['lv']==lv}
tambahan={k for k,v in json.load(open(S+'/kata_tambahan.json',encoding='utf-8')).items() if not k.startswith('_') and v['lv']==lv}
alias={}
for w in lvw:
    alias[w]=w
    for p in w.split('/'): alias.setdefault(p,w)
allw={}
for o in tb:
    for p in [o['w']]+o['w'].split('/'): allw.setdefault(p,o)
seen=collections.defaultdict(list); errs=[]
mods=[]
for line in open(f'{S}/plan_L{lv}.txt',encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    f=line.rstrip('\n').split('|'); mid=f[0]
    core=f[5].split(); sup=f[6].split() if len(f)>6 else []
    if len(core)>10: errs.append(f'{mid}: 核心 {len(core)}>10')
    ng=0 if f[4] in ('—','') else len(f[4].split(','))
    if ng>2: errs.append(f'{mid}: grammar {ng}>2')
    core=[w for w in core]; 
    for layer,ws in (('核心',core),('補充',sup)):
        for w in ws:
            yx='@' in w; w=w.split('@')[0]
            if yx and w in allw:
                continue
            if w in tambahan:
                continue
            if w not in alias:
                o=allw.get(w); errs.append(f'{mid}: "{w}" bukan kata Level {lv}'+(f" (ada di Level {o['lv']})" if o else ' (tidak ada di daftar TBCL)'))
            elif not yx: seen[alias[w]].append(f'{mid}/{layer}')
    mods.append((mid,len(core),len(sup),ng))
for w,l in seen.items():
    if len(l)>1: errs.append(f'GANDA {w}: {l}')
miss=[w for w in lvw if w not in seen]
print('\n'.join(errs)); print('BELUM TERTAMPUNG',len(miss),' '.join(miss))
print('modul',len(mods),'核心 avg %.1f'%(sum(m[1] for m in mods)/len(mods)),'補充 max',max(m[2] for m in mods))
G=json.load(open(S+'/grammar.json',encoding='utf-8'))[f'第{lv}級']
used=collections.Counter()
for line in open(f'{S}/plan_L{lv}.txt',encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    g=line.split('|')[4]
    if g not in ('—',''): used.update(int(x) for x in g.split(','))
print('GRAMMAR belum:',[f"{x['id']}:{x['g']}" for x in G if int(x['id']) not in used],' ganda:',[k for k,v in used.items() if v>1], f'tercakup {len(set(used))}/{len(G)}')
