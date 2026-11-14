"""Ringkasan satu 單元 untuk menulis ulang soal: py _kerja/soal_ai/lihat_bab.py A03
Kata & grammar baru, lalu semua soal latihan (isi + soal) dan Tes Bab dalam satu baris per soal."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); K = os.path.dirname(HERE); R = os.path.dirname(K)
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding='utf-8')
from buat_soal import muat, konteks   # noqa: E402
from pasang import berkas_isi         # noqa: E402


def baris(t):
    o = t.get('options', [])
    op = ' / '.join((x.get('label', '') + (f"<{x['img']}>" if x.get('img') else '')) if isinstance(x, dict) else x for x in o)
    isi = ''
    if t.get('picture'):
        isi += f"[{t['picture'].get('label', '')}{'<' + t['picture']['img'] + '>' if t['picture'].get('img') else ''}] "
    isi += ' '.join(f"{l['sp']}:{l['zh']}" for l in t.get('lines', []))
    isi += t.get('audio', '') + t.get('text', '')
    q = t.get('question', '')
    k = t.get('answers', t.get('answer'))
    return f"{t['type']}|{t['part'][:9]}| {isi} ‖ 問:{q} ‖ {op} ‖ ✔{k}"


def main(kode):
    mod = muat()
    ktx = konteks(kode, mod)
    m = mod[kode]
    print(f"# {kode} {ktx['judul']} — {ktx['scene']}")
    print('Kata baru:', ' '.join(ktx['target']))
    print('Grammar:', '; '.join(ktx['target_g']))
    print('Tokoh/nama di dialog:', ' '.join(sorted({l.get('sp', '') for d in m.get('dialogs', m.get('dialog', [])) if isinstance(d, dict) for l in d.get('lines', [])}))[:200])
    v = {'A': 1, 'B': 2, 'C': 3}[kode[0]]
    _, _, mi = berkas_isi(kode)
    print('## LATIHAN (isi)')
    for t in mi.get('tasks', []):
        print(' ', baris(t))
    import glob
    for sub in ('soal', 'bank'):
        for p in sorted(glob.glob(f'{K}/{sub}/vol{v}*.json')):
            d = json.load(open(p, encoding='utf-8'))
            if kode in d:
                print(f'## {sub.upper()}')
                for i, t in enumerate(d[kode]):
                    print(f'  {i}', baris(t))


if __name__ == '__main__':
    main(sys.argv[1])
