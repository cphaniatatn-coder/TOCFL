"""Lembar tinjauan bergambar (HTML) untuk soal hasil tulis ulang: py _kerja/soal_ai/lembar_tinjau.py A01 [A02 …]

Membaca _kerja/soal_ai/hasil/<kode>-latihan.json dan <kode>-tes.json (kolom pola_pengecoh ikut ditampilkan),
menulis _kerja/soal_ai/hasil/<kode>-tinjau.html: tiap soal dengan gambar SVG, transkrip, opsi, kunci ✔,
kode pola tiap pengecoh, penjelasan, dan kotak centang/catatan untuk Carli.
"""
import html, json, os, sys
from spesifikasi import POLA

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = '../../../img/soal'
e = html.escape


def gambar(p, besar=False):
    if not isinstance(p, dict):
        return e(p)
    w = 260 if besar else 170
    img = f'<img src="{IMG}/{e(p["img"])}.svg" width="{w}">' if p.get('img') else f'<div class="emo">{e(p.get("icon", ""))}</div>'
    return f'{img}<div class="lab">{e(p.get("label", ""))}</div>'


def kartu(n, t):
    pola = t.get('pola_pengecoh', {})
    h = [f'<section><h3>{n}. {e(t["part"])}</h3>']
    if t.get('picture'):
        h.append(f'<div class="pic">{gambar(t["picture"], True)}</div>')
    for l in t.get('lines', []):
        h.append(f'<div class="ln"><b>{e(l["sp"])}：</b>{e(l["zh"])}</div>')
    if t.get('text'):
        h.append(f'<div class="tx">{e(t["text"])}</div>')
    if t.get('question'):
        h.append(f'<div class="q">問：{e(t["question"])}</div>')
    opts = t.get('options', [])
    kunci = t.get('answers') if t['type'] == 'cloze' else [t.get('answer')]
    h.append('<div class="opts">')
    for i, o in enumerate(opts):
        hur = 'ABCDEF'[i]
        if t['type'] == 'cloze':
            tanda = ' ✔ (' + ','.join(str(k + 1) for k, a in enumerate(kunci) if a == i) + ')' if i in kunci else f' ✗ lebih [{pola.get("lebih", "?")}]'
        else:
            tanda = ' ✔' if i == t.get('answer') else f' ✗ [{pola.get(hur, "?")}]'
        cls = 'ok' if '✔' in tanda else ''
        h.append(f'<div class="opt {cls}"><b>{hur}.</b> {gambar(o)}<span class="t">{e(tanda)}</span></div>')
    h.append('</div>')
    h.append(f'<p class="why">{e(t.get("why", ""))}</p>')
    h.append('<label><input type="checkbox"> diterima</label> <input class="cat" placeholder="catatan Carli"></section>')
    return ''.join(h)


def main(kode):
    bag = []
    for jenis, judul in (('latihan', 'Soal latihan modul (12)'), ('tes', 'Tes Bab (10)')):
        p = f'{HERE}/hasil/{kode}-{jenis}.json'
        if os.path.exists(p):
            items = json.load(open(p, encoding='utf-8'))
            bag.append(f'<h2>{judul}</h2>' + ''.join(kartu(i + 1, t) for i, t in enumerate(items)))
    leg = ' · '.join(f'<b>{k}</b> {e(v)}' for k, v in POLA.items())
    out = (f'<!doctype html><meta charset="utf-8"><title>Tinjau {kode}</title><style>'
           'body{font-family:"DFKai-SB","BiauKai",serif,sans-serif;max-width:980px;margin:16px auto;padding:0 16px;font-size:17px}'
           'section{border:1px solid #bbb;border-radius:8px;padding:10px 14px;margin:12px 0}h3{margin:0 0 6px;font:600 15px sans-serif}'
           '.opts{display:flex;flex-wrap:wrap;gap:10px;margin:8px 0}.opt{border:1px solid #ddd;border-radius:6px;padding:6px;min-width:120px}'
           '.opt.ok{border:2px solid #2a8a3a;background:#f0fbf2}.lab{font:12px sans-serif;color:#555;max-width:260px}'
           '.t{font:13px sans-serif;margin-left:4px}.why{font:14px sans-serif;color:#333}.q{font-weight:700;margin-top:6px}'
           '.tx{background:#f6f6f6;padding:6px 8px;border-radius:4px}.emo{font-size:40px}.cat{width:60%;font:13px sans-serif}'
           '.leg{font:13px sans-serif;color:#444}</style>'
           f'<h1>Tinjauan soal {kode}</h1><p class="leg">Kode pola pengecoh: {leg}</p>' + ''.join(bag))
    f = f'{HERE}/hasil/{kode}-tinjau.html'
    open(f, 'w', encoding='utf-8').write(out)
    print('ditulis', os.path.relpath(f))


if __name__ == '__main__':
    for k in sys.argv[1:]:
        main(k)
