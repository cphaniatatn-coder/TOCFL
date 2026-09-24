"""Pemeriksa kosakata modul: semua teks Mandarin di sebuah modul hanya boleh
memakai kata yang SUDAH diajarkan sampai modul itu (urut A01..A25, B01..B46,
C01..C67), plus nama diri di NAMA. Partikel grammar tanpa entri kosakata
(了, 著) baru boleh dipakai setelah modul yang mengajarkan poin grammar-nya.

Pemakaian:  py _kerja/cek_dialog.py data/modul_vol1.json [data/modul_vol2.json ...]
"""
import json, os, re, sys

K = os.path.dirname(os.path.abspath(__file__))
NAMA = set('王大文 李美美 陳 林 張 王 李 小明 台北 臺北 雅加達 印尼 泗水 台中 高雄 大文 美美 安妮 志明 日本 美國 韓國 越南 泰國 臺南 台南 花蓮 陽明山 淡水 士林 信義 中山 忠孝 安安 小文 小林 故宮 綠島 北投'.split())
# partikel grammar-only → modul pertama yang mengajarkan poinnya
PARTIKEL = {'了': 'B09', '著': 'B08', '第': 'B03', '正在': 'B04', '看起來': 'B43', '聽起來': 'B43', '死了': 'C08', '為了': 'C15', '得不得了': 'C18', '極了': 'C18', '起': 'C33', '以外': 'C36', '分之': 'C38', '百分之': 'C38', '折': 'C40', '慣': 'C44', '睡著': 'C52', '睡不著': 'C52', '以內': 'C67'}


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


VARIAN = {}
for _o in json.load(open(f'{K}/tbcl.json', encoding='utf-8')):
    _parts = [re.sub(r'\d+$', '', p) for p in _o['w'].split('/')]
    for _p in _parts:
        VARIAN.setdefault(_p, set()).update(_parts)


def kosakata_sampai(mid, mods):
    ok = set(NAMA)
    for m, words in mods:
        for w in words:
            ok.add(w)
            ok.update(VARIAN.get(re.sub(r'\d+$', '', w), ()))
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
            # reduplikasi AABB dari kata dua suku yang dikenal (乾乾淨淨 ← 乾淨)
            if i + 4 <= len(seg) and seg[i] == seg[i + 1] and seg[i + 2] == seg[i + 3] and seg[i] + seg[i + 2] in ok:
                i += 4
                continue
            for L in range(min(6, len(seg) - i), 0, -1):
                if seg[i:i + L] in ok:
                    i += L
                    break
            else:
                bad.append(seg[i])
                i += 1
    return bad


def semua_kata():
    tb = json.load(open(f'{K}/tbcl.json', encoding='utf-8'))
    out = set()
    for o in tb:
        for p in o['w'].split('/'):
            p = re.sub(r'\d+$', '', p)
            if len(p) >= 2:
                out.add(p)
    return out


def main():
    mods = urutan()
    resmi = semua_kata()
    diterima = {tuple(l.split('|')[:2]) for l in open(f'{K}/cek_diterima.txt', encoding='utf-8')
                if l.strip() and not l.startswith('#')}
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
            warn = {}
            for s in teks(m):
                for w in resmi - ok:
                    i = s.find(w)
                    while i != -1:
                        # abaikan bila w berada di dalam kata lebih panjang yang sudah dikenal (沒關係 ⊃ 關係)
                        tertutup = any(len(k) > len(w) and s.find(k, max(0, i - len(k) + 1)) != -1 and
                                       s.find(k, max(0, i - len(k) + 1)) <= i and
                                       s.find(k, max(0, i - len(k) + 1)) + len(k) >= i + len(w)
                                       for k in ok if w in k)
                        if not tertutup and (m['code'], w) not in diterima:
                            warn.setdefault(w, s[:30])
                            break
                        i = s.find(w, i + 1)
            print(f"{m['code']}: {'OK' if not probs else str(len(probs)) + ' masalah'}{'' if not warn else f'  (peringatan: {len(warn)})'}")
            for ch, ctx in probs.items():
                print(f'   「{ch}」 belum diajarkan — di: {" | ".join(sorted(ctx))[:120]}')
            for w, ctx in warn.items():
                print(f'   ⚠ kata resmi 「{w}」 belum diajarkan (tersusun dari huruf yang dikenal) — di: {ctx}')
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
