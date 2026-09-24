"""Tulis ulang ledger.md dari data/modul_vol*.json (per 義項) + _kerja/ledger_catatan.md."""
import json, os
K = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(K)
rows, quick, gq = [], [], []
for v in (1, 2, 3):
    for m in json.load(open(f'{R}/data/modul_vol{v}.json', encoding='utf-8'))['modules']:
        scene = m['categories'][0].split('. ')[1]
        def ent(w):
            mean = w['meaning'].split(';')[0].split('；')[0].split('(')[0].strip().rstrip(',')
            if w.get('note') and '義項' in w['note']:
                mean = w['meaning']
            return f"{w['w']}（{mean}｜{scene}/{m['code']}）"
        c = [ent(w) for w in m['vocab']['core']]; s = [ent(w) for w in m['vocab']['supplement']]
        g = [f"#{x['tbcl_id']} {x['point'].split(' —')[0]}" for x in m['grammar']]
        rows.append(f"| {m['code']} | {v} | {m['title']} | {scene} | {' · '.join(c)} | {' · '.join(s) or '—'} | {' · '.join(g) or '— (daur ulang)'} |")
        quick += c + s; gq += [f"{x} ({m['code']})" for x in g]
head = """# ledger.md — Pencatat Anti-Pengulangan per 義項 (REBUILD 2026-09-24)

> FILE INI DIBUAT OTOMATIS oleh `py _kerja/buat_ledger.py` dari `data/modul_vol*.json`.
> Catatan manual ditulis di `_kerja/ledger_catatan.md` (ikut disalin ke bawah).
> Ledger lama (34 modul, per 詞形) disimpan utuh di `ledger-lama-34modul.md` — jangan dihapus.
>
> ATURAN (prinsip-thesis.md, bagian 多義詞):
> - Unit pelacakan = 義項 (bentuk + makna), format `詞形（makna｜情境/modul）`.
> - Bentuk sama + makna BARU = entri baru yang sah (di rencana ditulis `kata@義項`).
>   Bentuk sama + makna SAMA = daur ulang (複習), tidak dicatat ulang.
> - Rencana alokasi lengkap 138 modul: `_kerja/plan_L*.txt` & `rencana-modul.xlsx`.
> - Cek kosakata: `py _kerja/bangun_modul.py` (merakit + menjalankan cek_dialog.py).

## Tabel Riwayat Modul (isi sudah dibangun)

| Modul | Vol | Judul | 情境 | 核心 (義項) | 補充 (義項) | Grammar (TBCL #) |
|---|---|---|---|---|---|---|
"""
out = head + '\n'.join(rows) + f"\n\n## Daftar Cepat — 義項 yang SUDAH terpakai ({len(quick)})\n" + ' · '.join(quick)
out += f"\n\n## Daftar Cepat — Grammar yang SUDAH terpakai ({len(gq)})\n" + ' · '.join(gq)
out += '\n\n## Catatan Status\n' + open(f'{K}/ledger_catatan.md', encoding='utf-8').read() + '\n'
open(f'{R}/ledger.md', 'w', encoding='utf-8').write(out)
print('ledger.md:', len(rows), 'modul,', len(quick), '義項,', len(gq), 'grammar')
