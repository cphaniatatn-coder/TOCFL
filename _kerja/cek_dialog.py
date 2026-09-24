"""Pemeriksa kosakata modul: semua teks Mandarin di sebuah modul hanya boleh
memakai kata yang SUDAH diajarkan sampai modul itu (urut A01..A25, B01..B46,
C01..C67), plus nama diri di NAMA. Partikel grammar tanpa entri kosakata
(了, 著) baru boleh dipakai setelah modul yang mengajarkan poin grammar-nya.

Pemakaian:  py _kerja/cek_dialog.py data/modul_vol1.json [data/modul_vol2.json ...]
"""
import json, os, re, sys

K = os.path.dirname(os.path.abspath(__file__))
NAMA = set('王大文 李美美 陳 林 張 王 李 小明 台北 臺北 雅加達 印尼 泗水 台中 高雄 大文 美美 安妮 志明 日本 美國 韓國 越南 泰國 臺南 台南 花蓮 陽明山 淡水 士林 信義 中山 忠孝 安安 小文 小林'.split())
# partikel grammar-only → modul pertama yang mengajarkan poinnya
PARTIKEL = {'了': 'B09', '著': 'B08'}


def urutan():
    mods = []
    for lv in (1, 2, 3):
        for line in open(f'{K}/plan_L{lv}.txt', encoding='utf-8'):
            if line.startswith('#') or not line.strip():
                continue
            f = line.rstrip('\n').split('|')
            words = f[5].split() + (f[6].split() if len(f) > 6 else [])
            mods.append((f[0], [w.split('@')[0] for w in words]))
    return mods


def kosakata_sampai(mid, mods):
    ok = set(NAMA)
    for m, words in mods:
        for w in words:
            ok.add(w)
            ok.update(re.sub(r'\d+$', '', p) for p in w.split('/'))
        for p, start in PARTIKEL.items():
            if m == start:
                ok.add(p)
        if m == mid:
            return ok
    raise KeyError(mid)


def teks(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k in ('id', 'meaning', 'arti', 'explain', 'note', 'py', 'pinyin', 'why', 'goal', 'scene', 'pos', 'label', 'instr', 'sp', 'part', 'point', 'pattern', 'categories', 'place', 'title_id', 'title_py', 'can_do', 'exam_link', 'subtitle', 'approach', 'code'):
                continue  # teks Indonesia / pinyin
            yield from teks(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from teks(v)


def cek(s, ok):
    bad = []
    for seg in re.findall(r'[一-鿿]+', s):
        i = 0
        while i < len(seg):
            for L in range(min(6, len(seg) - i), 0, -1):
                if seg[i:i + L] in ok:
                    i += L
                    break
            else:
                bad.append(seg[i])
                i += 1
    return bad


def main():
    mods = urutan()
    total = 0
    for path in sys.argv[1:]:
        vol = json.load(open(path, encoding='utf-8'))
        for m in vol['modules']:
            ok = kosakata_sampai(m['code'], mods)
            probs = {}
            for s in teks(m):
                for ch in cek(s, ok):
                    probs.setdefault(ch, set()).add(s[:30])
            total += len(probs)
            print(f"{m['code']}: {'OK' if not probs else str(len(probs)) + ' masalah'}")
            for ch, ctx in probs.items():
                print(f'   「{ch}」 belum diajarkan — di: {" | ".join(sorted(ctx))[:120]}')
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
