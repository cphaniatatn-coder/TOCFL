"""Ganti 男的/女的 di semua soal (latihan & bank) → 這位先生/這位小姐 (keputusan Carli 2026-09-28).
Bentuk posesif mendapat 的: 男的姊姊 → 這位先生的姊姊; 女的的作業 → 這位小姐的作業.
Pemakaian: py _kerja/ganti_nanren.py [tulis]   (tanpa 'tulis' = hanya pratinjau)"""
import glob, json, os, re, sys
K = os.path.dirname(os.path.abspath(__file__))
ORANG = {'男': '這位先生', '女': '這位小姐'}
MILIK = ('意思 家 姊姊 哥哥 弟弟 妹妹 爸爸 媽媽 父親 母親 兒子 女兒 男朋友 女朋友 朋友 同學 手上 手 心情 早餐 '
         '衣服 鞋子 口袋 書包 書 班 辦公室 身體 臥室 零用錢 機車 作業 身高 日文 中文 學校 生日 東西 房間 電話 名字 工作').split()
POLA = re.compile(r'(?<![男女兒美])([男女])的(的|(?=' + '|'.join(sorted(MILIK, key=len, reverse=True)) + '))?')
LEWATI = {'sp', 'py', 'pinyin', 'id', 'picture', 'img', 'icon'}


def ganti(s):
    return POLA.sub(lambda m: ORANG[m.group(1)] + ('的' if m.lastindex and m.group(2) is not None else ''), s)


def jalan(o, catat):
    if isinstance(o, dict):
        return {k: (v if k in LEWATI else jalan(v, catat)) for k, v in o.items()}
    if isinstance(o, list):
        return [jalan(v, catat) for v in o]
    if isinstance(o, str) and POLA.search(o):
        b = ganti(o); catat.append((o, b)); return b
    return o


def main(tulis):
    """Ganti langsung di teks file (format tulisan tangan tetap utuh); hasilnya dicek sama dengan penggantian per-JSON."""
    semua = []
    for f in sorted(glob.glob(f'{K}/isi/*.json') + glob.glob(f'{K}/soal/*.json') + glob.glob(f'{K}/bank/*.json')):
        raw = open(f, encoding='utf-8').read(); d = json.loads(raw); catat = []
        if os.path.basename(os.path.dirname(f)) == 'isi':   # di isi hanya bagian soal (tasks)
            for m in (d['modules'] if 'modules' in d else [d]):
                if 'tasks' in m: m['tasks'] = jalan(m['tasks'], catat)
        else:
            d = jalan(d, catat)
        if not catat:
            continue
        semua += catat
        baru = POLA.sub(lambda m: ORANG[m.group(1)] + ('的' if m.group(2) is not None else ''), raw)
        if json.loads(baru) != d:
            sys.exit(f'{f}: penggantian teks tidak sama dengan penggantian per-JSON (ada 男的/女的 di luar soal?) — tidak ditulis')
        if tulis:
            open(f, 'w', encoding='utf-8', newline='').write(baru)
    return semua


if __name__ == '__main__':
    hasil = main(len(sys.argv) > 1 and sys.argv[1] == 'tulis')
    print(len(hasil), 'teks diganti')
    for a, b in hasil:
        if '位先生的' in b or '位小姐的' in b: print('  ', a[:40], '→', b[:50])
