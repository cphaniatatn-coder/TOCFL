"""Ilustrasi soal 聽力 Part 1 bergaya buku soal TOCFL, digambar dengan kode (SVG).

    py _kerja/gambar_soal.py            → tulis img/soal/<ID>.svg untuk semua adegan
                                           + lembar periksa _kerja/gambar/periksa_vol<N>.html (WAJIB dicek visual)
    py _kerja/gambar_soal.py pasang     → isi picture.img pada soal listen_pic yang gambarnya ada

ID = <modul>-<n>: soal listen_pic ke-n di modul itu, urut isi/ → soal/ → bank/.
Adegan per volume: adegan_vol1.py, adegan_vol2.py, adegan_vol3.py (dict A). Komponen: svg_lib.py, svg_adegan.py.
"""
import importlib, json, os, sys

K = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(K)
sys.path.insert(0, K)
from svg_lib import bungkus

OUT = f'{R}/img/soal'
HURUF = {1: 'A', 2: 'B', 3: 'C'}


def adegan():
    A = {}
    for v in (1, 2, 3):
        if os.path.exists(f'{K}/adegan_vol{v}.py'):
            A.update(importlib.import_module(f'adegan_vol{v}').A)
    return A


def sumber(v):
    """File sumber volume v (isi, soal tambahan, bank) → {path: data}."""
    h = HURUF[v]
    files = [f'{K}/isi/{fn}' for fn in sorted(os.listdir(f'{K}/isi')) if fn.startswith((h, f'vol{v}_'))]
    files += [p for p in (f'{K}/soal/vol{v}.json', f'{K}/bank/vol{v}.json') if os.path.exists(p)]
    return {p: json.load(open(p, encoding='utf-8')) for p in files}


def urutan_soal(v, data=None):
    """[(ID, soal)] untuk semua listen_pic volume v, urut isi → soal → bank per modul."""
    data = data or sumber(v)
    isi, tamb, bank = {}, {}, {}
    for p, d in data.items():
        if '/isi/' in p:
            if 'modules' in d:
                for m in d['modules']:
                    isi[m['code']] = m['tasks']
            else:
                isi[os.path.basename(p)[:-5]] = d['tasks']
        elif '/soal/' in p:
            tamb = d
        else:
            bank = d
    out = []
    for c in sorted(isi):
        n = 0
        for ts in (isi[c], tamb.get(c, []), bank.get(c, [])):
            for t in ts:
                if t['type'] == 'listen_pic':
                    n += 1
                    out.append((f'{c}-{n}', t))
    return out


def tulis():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(f'{K}/gambar', exist_ok=True)
    A = adegan()
    for i, isi in A.items():
        open(f'{OUT}/{i}.svg', 'w', encoding='utf-8').write(bungkus(isi))
    for v in (1, 2, 3):
        daftar = urutan_soal(v)
        if not daftar:
            continue
        kurang = [i for i, _ in daftar if i not in A]
        kartu = ''.join(
            f'<figure><img src="../../img/soal/{i}.svg"><figcaption><b>{i}</b> {t["question"]}<br>✔ {t["options"][t["answer"]]}'
            f'<br><small>✗ {" / ".join(o for k, o in enumerate(t["options"]) if k != t["answer"])}</small></figcaption></figure>'
            for i, t in daftar if i in A)
        open(f'{K}/gambar/periksa_vol{v}.html', 'w', encoding='utf-8').write(
            '<!doctype html><meta charset="utf-8"><style>body{font-family:sans-serif;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:10px}'
            'figure{margin:0;border:1px solid #ccc;padding:4px}img{width:100%}figcaption{font-size:12px}</style>' + kartu)
        print(f'Vol.{v}: {len(daftar)} soal listen_pic, {len(daftar) - len(kurang)} bergambar; belum: {" ".join(kurang[:20]) or "tidak ada"}'
              + (' …' if len(kurang) > 20 else ''))


def pasang():
    A = adegan()
    for v in (1, 2, 3):
        data = sumber(v)
        n = 0
        for i, t in urutan_soal(v, data):
            if i in A and os.path.exists(f'{OUT}/{i}.svg') and t['picture'].get('img') != i:
                t['picture']['img'] = i; n += 1
        if n:
            for p, d in data.items():
                json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); open(p, 'a', encoding='utf-8').write('\n')
        print(f'Vol.{v}: picture.img baru dipasang pada {n} soal')


if __name__ == '__main__':
    pasang() if sys.argv[1:] == ['pasang'] else tulis()
