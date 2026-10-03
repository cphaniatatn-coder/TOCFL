"""Kelola _kerja/mini/kamus_mini.json ({"teks Indonesia": {"en": …, "vi": …}}).

    py _kerja/mini/kamus.py tambah <file.json>   → gabungkan [[id, en, vi], …] atau [[id, vi], …] (vi saja)
    py _kerja/mini/kamus.py tugas vi [n]         → tulis _kerja/mini/tugas_vi.json: teks yang belum punya vi,
                                                   berpasangan dengan English-nya (sebagai acuan terjemahan)
Teks yang belum punya terjemahan didaftar oleh py _kerja/buat_mini.py cek (kurang_*.txt).
"""
import json, sys
from pathlib import Path
M = Path(__file__).resolve().parent; K = M.parent
KAMUS = M / 'kamus_mini.json'


def muat():
    return json.loads(KAMUS.read_text(encoding='utf-8')) if KAMUS.exists() else {}


def simpan(d):
    KAMUS.write_text(json.dumps(dict(sorted(d.items())), ensure_ascii=False, indent=0) + '\n', encoding='utf-8')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    cmd = sys.argv[1]
    d = muat()
    if cmd == 'tambah':
        n = 0
        for x in json.loads(Path(sys.argv[2]).read_text(encoding='utf-8')):
            e = d.setdefault(x[0], {})
            if len(x) == 3: e['en'], e['vi'] = x[1], x[2]
            else: e['vi'] = x[1]
            n += 1
        simpan(d); print(f'{n} entri digabung; kamus: {len(d)} teks')
    elif cmd == 'tugas':
        en = json.loads((K / 'terjemahan_en.json').read_text(encoding='utf-8'))
        kurang = [json.loads(l) for l in (M / 'kurang_vi.txt').read_text(encoding='utf-8').splitlines() if l.strip()]
        out = [[s, (d.get(s) or {}).get('en') or en.get(s, '')] for s in kurang]
        (M / 'tugas_vi.json').write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding='utf-8')
        print(f'{len(out)} teks → _kerja/mini/tugas_vi.json')
