# Pengkodean 500 butir mock test TOCFL Band A set 01-05 (satu pengkode: Claude, 2026-11-12)
# Format baris: set sek part no tema pola
#   sek: L=聽力 R=閱讀 ; tema = 17 情境類別 TBCL ; pola = pola pengecoh UTAMA
# Pola: A 說反/角色對調/否定  B 次要細節當重點  C 相關但文中未提  D 同類替換
#       E 最小差異(同元素,一屬性不同: 數量/位置/時間/組合/狀態)  F 言外之意照字面
#       H 文中出現詞陷阱  I 語法/搭配  J 字形/字音相近  G 段落填空(多餘選項另記)
import collections, sys
sys.stdout.reconfigure(encoding='utf-8')
DATA = """
1 L 1 1 教育 D|1 L 1 2 日常 E|1 L 1 3 日常 E|1 L 1 4 餐飲 D|1 L 1 5 休閒 D|1 L 1 6 情緒 D|1 L 1 7 日常 D|1 L 1 8 餐飲 D|1 L 1 9 日常 D|1 L 1 10 自然 D
1 L 1 11 休閒 D|1 L 1 12 交通 D|1 L 1 13 購物 D|1 L 1 14 教育 D|1 L 1 15 教育 D|1 L 1 16 職業 D|1 L 1 17 餐飲 D|1 L 1 18 教育 D|1 L 1 19 個人 E|1 L 1 20 個人 E
1 L 1 21 餐飲 E|1 L 1 22 日常 E|1 L 1 23 自然 E|1 L 1 24 購物 E|1 L 1 25 醫療 D
1 L 2 26 交通 D|1 L 2 27 醫療 D|1 L 2 28 日常 E|1 L 2 29 休閒 D|1 L 2 30 購物 E|1 L 2 31 個人 E|1 L 2 32 交通 E|1 L 2 33 餐飲 E|1 L 2 34 休閒 D|1 L 2 35 購物 E
1 L 2 36 醫療 D|1 L 2 37 交通 E|1 L 2 38 交通 E|1 L 2 39 交通 D|1 L 2 40 購物 H
1 L 3 41 購物 D|1 L 3 42 教育 H|1 L 3 43 休閒 E|1 L 3 44 教育 E|1 L 3 45 交通 H
1 L 4 46 日常 H|1 L 4 47 日常 A|1 L 4 48 購物 H|1 L 4 49 職業 H|1 L 4 50 購物 H
1 R 1 1 餐飲 E|1 R 1 2 休閒 A|1 R 1 3 日常 E|1 R 1 4 教育 H|1 R 1 5 休閒 D|1 R 1 6 日常 E|1 R 1 7 交通 E|1 R 1 8 日常 H|1 R 1 9 交通 E|1 R 1 10 自然 D
1 R 1 11 情緒 D|1 R 1 12 日常 D|1 R 1 13 休閒 A|1 R 1 14 教育 E|1 R 1 15 購物 H
1 R 2 16 自然 C|1 R 2 17 日常 C|1 R 2 18 日常 D|1 R 2 19 個人 E|1 R 2 20 餐飲 E|1 R 2 21 醫療 E|1 R 2 22 休閒 E|1 R 2 23 教育 E|1 R 2 24 教育 E|1 R 2 25 餐飲 E
1 R 2 26 交通 E|1 R 2 27 交通 E|1 R 2 28 購物 E|1 R 2 29 教育 A|1 R 2 30 交通 E
1 R 3 31 日常 I|1 R 3 32 日常 I|1 R 3 33 日常 D|1 R 3 34 日常 I|1 R 3 35 日常 I|1 R 3 36 社交 J|1 R 3 37 社交 I|1 R 3 38 社交 D|1 R 3 39 社交 D|1 R 3 40 社交 I
1 R 4 41 醫療 G|1 R 4 42 醫療 G|1 R 4 43 醫療 G|1 R 4 44 醫療 G|1 R 4 45 醫療 G
1 R 5 46 職業 C|1 R 5 47 醫療 A|1 R 5 48 文化 C|1 R 5 49 社會 C|1 R 5 50 休閒 A
2 L 1 1 日常 D|2 L 1 2 日常 D|2 L 1 3 交通 D|2 L 1 4 個人 E|2 L 1 5 餐飲 D|2 L 1 6 購物 D|2 L 1 7 交通 D|2 L 1 8 日常 D|2 L 1 9 公共 D|2 L 1 10 教育 D
2 L 1 11 休閒 D|2 L 1 12 個人 E|2 L 1 13 餐飲 D|2 L 1 14 醫療 D|2 L 1 15 日常 E|2 L 1 16 休閒 D|2 L 1 17 日常 D|2 L 1 18 職業 D|2 L 1 19 教育 D|2 L 1 20 自然 D
2 L 1 21 休閒 D|2 L 1 22 休閒 D|2 L 1 23 購物 E|2 L 1 24 日常 D|2 L 1 25 職業 D
2 L 2 26 個人 E|2 L 2 27 購物 E|2 L 2 28 職業 F|2 L 2 29 休閒 E|2 L 2 30 休閒 D|2 L 2 31 購物 D|2 L 2 32 日常 E|2 L 2 33 購物 E|2 L 2 34 安全 D|2 L 2 35 社交 D
2 L 2 36 購物 E|2 L 2 37 社交 D|2 L 2 38 休閒 E|2 L 2 39 購物 E|2 L 2 40 日常 D
2 L 3 41 職業 E|2 L 3 42 餐飲 H|2 L 3 43 職業 H|2 L 3 44 日常 H|2 L 3 45 職業 H
2 L 4 46 醫療 H|2 L 4 47 日常 H|2 L 4 48 教育 H|2 L 4 49 購物 A|2 L 4 50 社交 F
2 R 1 1 餐飲 E|2 R 1 2 個人 E|2 R 1 3 文化 E|2 R 1 4 日常 E|2 R 1 5 個人 E|2 R 1 6 交通 E|2 R 1 7 教育 E|2 R 1 8 休閒 D|2 R 1 9 日常 E|2 R 1 10 醫療 D
2 R 1 11 日常 E|2 R 1 12 休閒 E|2 R 1 13 餐飲 E|2 R 1 14 教育 E|2 R 1 15 醫療 E
2 R 2 16 交通 D|2 R 2 17 日常 C|2 R 2 18 教育 E|2 R 2 19 公共 E|2 R 2 20 餐飲 E|2 R 2 21 休閒 D|2 R 2 22 餐飲 E|2 R 2 23 購物 E|2 R 2 24 日常 E|2 R 2 25 教育 E
2 R 2 26 醫療 A|2 R 2 27 教育 E|2 R 2 28 交通 E|2 R 2 29 日常 E|2 R 2 30 社交 E
2 R 3 31 交通 I|2 R 3 32 交通 I|2 R 3 33 交通 I|2 R 3 34 交通 I|2 R 3 35 交通 D|2 R 3 36 購物 D|2 R 3 37 購物 I|2 R 3 38 購物 I|2 R 3 39 購物 I|2 R 3 40 購物 D
2 R 4 41 日常 G|2 R 4 42 日常 G|2 R 4 43 日常 G|2 R 4 44 日常 G|2 R 4 45 日常 G
2 R 5 46 情緒 C|2 R 5 47 社會 H|2 R 5 48 休閒 B|2 R 5 49 職業 H|2 R 5 50 教育 C
3 L 1 1 醫療 D|3 L 1 2 交通 E|3 L 1 3 自然 E|3 L 1 4 個人 E|3 L 1 5 餐飲 D|3 L 1 6 自然 E|3 L 1 7 日常 D|3 L 1 8 購物 E|3 L 1 9 醫療 D|3 L 1 10 日常 J
3 L 2 11 教育 D|3 L 2 12 日常 E|3 L 2 13 日常 D|3 L 2 14 休閒 D|3 L 2 15 社交 D|3 L 2 16 購物 D|3 L 2 17 日常 E|3 L 2 18 教育 D|3 L 2 19 醫療 E|3 L 2 20 交通 E
3 L 2 21 個人 E|3 L 2 22 職業 H|3 L 2 23 自然 D|3 L 2 24 日常 D|3 L 2 25 日常 H
3 L 3 26 購物 E|3 L 3 27 交通 E|3 L 3 28 教育 H|3 L 3 29 休閒 D|3 L 3 30 醫療 H|3 L 3 31 職業 H|3 L 3 32 教育 H|3 L 3 33 職業 H|3 L 3 34 交通 H|3 L 3 35 日常 D
3 L 3 36 日常 E|3 L 3 37 購物 D|3 L 3 38 餐飲 H|3 L 3 39 日常 H|3 L 3 40 教育 E
3 L 4 41 交通 H|3 L 4 42 餐飲 C|3 L 4 43 醫療 H|3 L 4 44 日常 A|3 L 4 45 購物 B|3 L 4 46 交通 A|3 L 4 47 社交 F|3 L 4 48 教育 F|3 L 4 49 休閒 F|3 L 4 50 個人 H
3 R 1 1 日常 D|3 R 1 2 休閒 D|3 R 1 3 餐飲 E|3 R 1 4 日常 E|3 R 1 5 日常 E|3 R 1 6 日常 E|3 R 1 7 休閒 E|3 R 1 8 交通 E|3 R 1 9 教育 E|3 R 1 10 日常 E
3 R 1 11 日常 E|3 R 1 12 日常 H|3 R 1 13 交通 D|3 R 1 14 教育 E|3 R 1 15 醫療 D
3 R 2 16 日常 E|3 R 2 17 日常 E|3 R 2 18 休閒 C|3 R 2 19 教育 E|3 R 2 20 社交 A|3 R 2 21 休閒 E|3 R 2 22 自然 E|3 R 2 23 餐飲 E|3 R 2 24 社交 E|3 R 2 25 個人 E
3 R 2 26 交通 E|3 R 2 27 交通 E|3 R 2 28 教育 A|3 R 2 29 交通 E|3 R 2 30 餐飲 E
3 R 3 31 日常 I|3 R 3 32 日常 I|3 R 3 33 日常 D|3 R 3 34 日常 D|3 R 3 35 日常 I
3 R 4 36 購物 G|3 R 4 37 購物 G|3 R 4 38 購物 G|3 R 4 39 購物 G|3 R 4 40 購物 G|3 R 4 41 職業 G|3 R 4 42 職業 G|3 R 4 43 職業 G|3 R 4 44 職業 G|3 R 4 45 職業 G
3 R 5 46 公共 A|3 R 5 47 購物 A|3 R 5 48 餐飲 A|3 R 5 49 職業 A|3 R 5 50 餐飲 H
4 L 1 1 教育 D|4 L 1 2 自然 D|4 L 1 3 休閒 D|4 L 1 4 醫療 D|4 L 1 5 休閒 D|4 L 1 6 職業 D|4 L 1 7 自然 D|4 L 1 8 日常 E|4 L 1 9 交通 D|4 L 1 10 職業 D
4 L 2 11 餐飲 D|4 L 2 12 休閒 D|4 L 2 13 社交 E|4 L 2 14 購物 D|4 L 2 15 餐飲 H|4 L 2 16 交通 E|4 L 2 17 購物 D|4 L 2 18 醫療 E|4 L 2 19 日常 E|4 L 2 20 日常 H
4 L 2 21 科技 D|4 L 2 22 情緒 D|4 L 2 23 購物 D|4 L 2 24 自然 D|4 L 2 25 日常 E
4 L 3 26 社交 H|4 L 3 27 餐飲 E|4 L 3 28 購物 E|4 L 3 29 教育 E|4 L 3 30 個人 E|4 L 3 31 教育 D|4 L 3 32 安全 D|4 L 3 33 教育 H|4 L 3 34 交通 D|4 L 3 35 餐飲 D
4 L 3 36 交通 H|4 L 3 37 醫療 H|4 L 3 38 交通 H|4 L 3 39 自然 H|4 L 3 40 日常 E
4 L 4 41 安全 A|4 L 4 42 教育 C|4 L 4 43 職業 D|4 L 4 44 職業 A|4 L 4 45 社交 H|4 L 4 46 社交 F|4 L 4 47 職業 A|4 L 4 48 醫療 H|4 L 4 49 安全 H|4 L 4 50 社交 B
4 R 1 1 休閒 D|4 R 1 2 休閒 D|4 R 1 3 自然 D|4 R 1 4 自然 D|4 R 1 5 醫療 D|4 R 1 6 日常 D|4 R 1 7 教育 E|4 R 1 8 餐飲 E|4 R 1 9 休閒 E|4 R 1 10 安全 E
4 R 1 11 購物 E|4 R 1 12 個人 E|4 R 1 13 醫療 E|4 R 1 14 教育 E|4 R 1 15 交通 E
4 R 2 16 個人 E|4 R 2 17 職業 E|4 R 2 18 餐飲 E|4 R 2 19 教育 E|4 R 2 20 文化 E|4 R 2 21 自然 E|4 R 2 22 自然 E|4 R 2 23 交通 E|4 R 2 24 教育 E|4 R 2 25 餐飲 E
4 R 2 26 休閒 E|4 R 2 27 公共 E|4 R 2 28 交通 E|4 R 2 29 交通 E|4 R 2 30 日常 E
4 R 3 31 自然 I|4 R 3 32 自然 I|4 R 3 33 自然 I|4 R 3 34 自然 I|4 R 3 35 自然 I
4 R 4 36 職業 G|4 R 4 37 職業 G|4 R 4 38 職業 G|4 R 4 39 職業 G|4 R 4 40 職業 G|4 R 4 41 休閒 G|4 R 4 42 休閒 G|4 R 4 43 休閒 G|4 R 4 44 休閒 G|4 R 4 45 休閒 G
4 R 5 46 交通 D|4 R 5 47 教育 C|4 R 5 48 交通 C|4 R 5 49 日常 H|4 R 5 50 社會 C
5 L 1 1 教育 E|5 L 1 2 休閒 D|5 L 1 3 日常 D|5 L 1 4 醫療 D|5 L 1 5 餐飲 D|5 L 1 6 職業 E|5 L 1 7 公共 D|5 L 1 8 教育 E|5 L 1 9 休閒 E|5 L 1 10 自然 E
5 L 2 11 餐飲 E|5 L 2 12 休閒 D|5 L 2 13 餐飲 E|5 L 2 14 科技 D|5 L 2 15 個人 E|5 L 2 16 購物 D|5 L 2 17 餐飲 H|5 L 2 18 日常 H|5 L 2 19 日常 E|5 L 2 20 休閒 H
5 L 2 21 職業 E|5 L 2 22 情緒 D|5 L 2 23 職業 D|5 L 2 24 日常 E|5 L 2 25 日常 D|5 L 2 26 自然 D|5 L 2 27 交通 H|5 L 2 28 日常 E
5 L 3 29 社交 E|5 L 3 30 教育 E|5 L 3 31 餐飲 E|5 L 3 32 個人 E|5 L 3 33 餐飲 H|5 L 3 34 日常 H|5 L 3 35 自然 H|5 L 3 36 職業 D|5 L 3 37 社交 E|5 L 3 38 科技 H
5 L 3 39 餐飲 D|5 L 3 40 職業 H
5 L 4 41 職業 H|5 L 4 42 交通 A|5 L 4 43 教育 C|5 L 4 44 日常 C|5 L 4 45 醫療 A|5 L 4 46 休閒 H|5 L 4 47 社交 F|5 L 4 48 購物 A|5 L 4 49 購物 A|5 L 4 50 購物 B
5 R 1 1 休閒 E|5 R 1 2 休閒 E|5 R 1 3 餐飲 E|5 R 1 4 交通 E|5 R 1 5 休閒 E|5 R 1 6 醫療 E|5 R 1 7 自然 E|5 R 1 8 購物 E|5 R 1 9 個人 E|5 R 1 10 交通 E
5 R 1 11 購物 H|5 R 1 12 購物 E|5 R 1 13 日常 D|5 R 1 14 教育 E|5 R 1 15 休閒 D
5 R 2 16 教育 E|5 R 2 17 餐飲 E|5 R 2 18 休閒 E|5 R 2 19 日常 A|5 R 2 20 日常 E|5 R 2 21 餐飲 E|5 R 2 22 教育 E|5 R 2 23 日常 E|5 R 2 24 職業 A|5 R 2 25 購物 E
5 R 2 26 職業 E|5 R 2 27 安全 E|5 R 2 28 交通 E|5 R 2 29 交通 E|5 R 2 30 職業 E
5 R 3 31 購物 I|5 R 3 32 購物 I|5 R 3 33 購物 I|5 R 3 34 購物 I|5 R 3 35 購物 D|5 R 3 36 購物 I|5 R 3 37 購物 I|5 R 3 38 購物 I|5 R 3 39 購物 I|5 R 3 40 購物 A
5 R 4 41 個人 G|5 R 4 42 個人 G|5 R 4 43 個人 G|5 R 4 44 個人 G|5 R 4 45 個人 G
5 R 5 46 休閒 H|5 R 5 47 教育 H|5 R 5 48 社交 H|5 R 5 49 購物 H|5 R 5 50 職業 A
"""
# Pengecoh "opsi berlebih" 閱讀 P4 per paragraf: hubungannya dengan salah satu jawaban benar
EXTRA = {'1a': 'A', '2a': 'A', '3a': 'E', '3b': 'A', '4a': 'E', '4b': 'C', '5a': 'A'}

rows = []
for chunk in DATA.replace('\n', '|').split('|'):
    t = chunk.split()
    if t:
        s, sek, part, no, tema, pola = t
        rows.append(dict(s=int(s), sek=sek, part=int(part), no=int(no), tema=tema, pola=pola))
print('jumlah butir:', len(rows), collections.Counter((r['sek']) for r in rows))
assert len(rows) == 500, len(rows)
import json
json.dump(rows, open(sys.argv[1] + '/kode.json', 'w', encoding='utf-8'), ensure_ascii=False)

NAMA = {'A': 'A 說反/角色對調', 'B': 'B 次要細節', 'C': 'C 相關未提', 'D': 'D 同類替換', 'E': 'E 最小差異',
        'F': 'F 言外之意', 'H': 'H 文中詞陷阱', 'I': 'I 語法搭配', 'J': 'J 形音相近', 'G': 'G 段落填空'}
print('\n== TEMA (semua 500 butir)')
tc = collections.Counter(r['tema'] for r in rows)
for k, v in tc.most_common(): print(f'{k}\t{v}\t{v/5:.1f}%')
print('\n== TEMA per sek')
for sek in 'LR':
    c = collections.Counter(r['tema'] for r in rows if r['sek'] == sek)
    print(sek, c.most_common())
print('\n== TEMA muncul di berapa set (dari 5)')
for k in tc:
    print(k, len({r['s'] for r in rows if r['tema'] == k}), end=' | ')
print('\n\n== POLA per part')
for sek in 'LR':
    for p in range(1, 6):
        sub = [r for r in rows if r['sek'] == sek and r['part'] == p]
        if not sub: continue
        c = collections.Counter(r['pola'] for r in sub)
        print(f'{sek}P{p} (n={len(sub)}):', ', '.join(f'{k}={v}' for k, v in sorted(c.items())))
print('\n== POLA total (tanpa G)')
c = collections.Counter(r['pola'] for r in rows if r['pola'] != 'G')
n = sum(c.values())
for k, v in c.most_common(): print(f'{NAMA[k]}\t{v}\t{100*v/n:.1f}%')
print('\n== POLA per generasi (tanpa G)')
for nama, ss in (('set 01-02', (1, 2)), ('set 03-05', (3, 4, 5))):
    c = collections.Counter(r['pola'] for r in rows if r['pola'] != 'G' and r['s'] in ss)
    n = sum(c.values()); print(nama, n, ', '.join(f'{k}={100*v/n:.0f}%' for k, v in c.most_common()))
print('\n== Opsi berlebih 閱讀 P4 (7 paragraf):', collections.Counter(EXTRA.values()))
