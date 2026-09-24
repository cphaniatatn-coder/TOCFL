import openpyxl, sys, collections, json
wb=openpyxl.load_workbook(r'C:\Users\user\OneDrive\文件\TOCFL\pemetaan-kategori.xlsx',read_only=True)
allw={}
for lv in (1,2,3):
    d=collections.defaultdict(list)
    for r in list(wb[f'Level {lv}'].iter_rows(values_only=True))[1:]:
        d[str(r[5])].append((r[0],r[1],r[2]))
    allw[lv]=d
json.dump(allw,open(sys.argv[1]+'/bycat.json','w',encoding='utf-8'),ensure_ascii=False)
lv=int(sys.argv[2])
for k in sorted(allw[lv],key=lambda x:(x.startswith('T'),int(x) if x.isdigit() else 0,x)):
    print(k, len(allw[lv][k]), ' '.join(w for _,w,_ in allw[lv][k]))
