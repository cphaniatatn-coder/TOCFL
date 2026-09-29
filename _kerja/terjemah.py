"""Versi English data app: data/*.json (Indonesia, hasil rakit) → data/en/*.json.

Terjemahan disimpan sebagai kamus teks-Indonesia → teks-English di _kerja/terjemahan_en.json.
Teks yang diterjemahkan = kolom penjelasan/arti (bukan hanzi, pinyin, atau kode):
  id, title_id, scene, can_do, exam_link, instr, why, part, label, explain, meaning, point,
  pattern, q, options (hanya yang berhuruf Latin), note, extra, subtitle, peran di blocks.

  py _kerja/terjemah.py           → tulis data/en/*.json; teks yang belum punya terjemahan tetap
                                    Indonesia dan didaftar di _kerja/terjemahan_kurang.txt
  py _kerja/terjemah.py bersih    → buang terjemahan yang teks Indonesianya sudah tidak dipakai

Jalankan ulang SETIAP KALI data/*.json dirakit ulang (bangun_modul, bangun_bank, buat_rencana_json).
Teks yang kurang: terjemahkan lalu tambahkan ke terjemahan_en.json (format {"Indonesia": "English"}).
"""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

R = Path(__file__).resolve().parent.parent
K = R / '_kerja'
KAMUS = K / 'terjemahan_en.json'
KURANG = K / 'terjemahan_kurang.txt'
FILES = ['rencana', 'modul_vol1', 'modul_vol2', 'modul_vol3', 'bank_soal']
KEYS = {'id', 'title_id', 'scene', 'can_do', 'exam_link', 'instr', 'why', 'part', 'label', 'explain',
        'meaning', 'point', 'pattern', 'q', 'options', 'note', 'extra', 'subtitle'}
LATIN = re.compile(r'[A-Za-z]{2,}')


def jalan(o, key, fn):
    """Salin struktur o; teks yang perlu diterjemahkan dilewatkan ke fn."""
    if isinstance(o, dict):
        return {k: jalan(v, k, fn) for k, v in o.items()}
    if isinstance(o, list):
        if key == 'blocks':   # [hanzi, peran]
            return [[b[0], fn(b[1])] + b[2:] if isinstance(b, list) and len(b) > 1 and isinstance(b[1], str) and LATIN.search(b[1]) else b for b in o]
        return [jalan(v, key, fn) for v in o]
    if isinstance(o, str) and key in KEYS and LATIN.search(o):
        return fn(o)
    return o


def main():
    kamus = json.loads(KAMUS.read_text(encoding='utf-8')) if KAMUS.exists() else {}
    dipakai, kurang = set(), {}

    def tr(s):
        dipakai.add(s)
        if s in kamus:
            return kamus[s]
        kurang.setdefault(s, None)
        return s

    (R / 'data' / 'en').mkdir(exist_ok=True)
    for f in FILES:
        src = json.loads((R / 'data' / f'{f}.json').read_text(encoding='utf-8'))
        out = jalan(src, None, tr)
        tulis = json.dumps(out, ensure_ascii=False, indent=1)
        dst = R / 'data' / 'en' / f'{f}.json'
        if not dst.exists() or dst.read_text(encoding='utf-8') != tulis:
            dst.write_text(tulis, encoding='utf-8')
            print('ditulis', dst.relative_to(R))

    if 'bersih' in sys.argv[1:]:
        buang = [s for s in kamus if s not in dipakai]
        for s in buang:
            del kamus[s]
        KAMUS.write_text(json.dumps(kamus, ensure_ascii=False, indent=1), encoding='utf-8')
        print(f'{len(buang)} terjemahan tak terpakai dibuang')

    if kurang:
        KURANG.write_text('\n'.join(json.dumps(s, ensure_ascii=False) for s in kurang) + '\n', encoding='utf-8')
        print(f'⚠ {len(kurang)} teks belum punya terjemahan English (masih Indonesia di app) → {KURANG.relative_to(R)}')
    else:
        KURANG.unlink(missing_ok=True)
        print(f'OK: {len(dipakai)} teks, semua sudah punya terjemahan English')


if __name__ == '__main__':
    main()
