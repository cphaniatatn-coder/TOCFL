import openpyxl, glob, json, sys
f=[x for x in glob.glob(r'C:\Users\user\OneDrive\文件\TOCFL\TBCL 資料分享\*') if 'A2' in x and '詞彙' in x][0]
rows=list(openpyxl.load_workbook(f,read_only=True)['總表'].iter_rows(values_only=True))[1:]
out=[dict(id=int(r[0]),w=r[1],lv=int(r[3].replace('*','')[1]),star='*' in r[3],cat=r[4],py=r[6]) for r in rows]
json.dump(out,open(sys.argv[1]+'/tbcl.json','w',encoding='utf-8'),ensure_ascii=False)
lv=int(sys.argv[2])
print(' '.join(f"{o['id']}{o['w']}" for o in out if o['lv']==lv and o['cat']=='核心詞'))
