"""Audit: seberapa sesuai soal latihan modul (data/modul_vol*.json → tasks) dan Tes Bab (_kerja/bank)
dengan ciri soal TOCFL Band A hasil analisis 5 mock test (analisis-ujian-tocfl.md Bagian 6–8; spesifikasi.py).

Yang diukur per Part & per level (semua otomatis; pola pengecoh tidak bisa diukur otomatis):
  1. format resmi: tipe, jumlah baris dialog, opsi gambar/teks, jumlah opsi
  2. panjang teks vs rentang di spesifikasi.PANJANG
  3. 男的/女的 (seharusnya 0)
  4. sebaran posisi jawaban (per 單元 & total)
  5. 聽P4 / 閱P5: pertanyaan inferensial (意思/覺得/為什麼/可能/說了什麼/會…) vs faktual
  6. 聽P4 / 閱P5: jawaban benar = kutipan persis dari teks (soal resmi memakai parafrase)
  7. opsi tidak gramatikal (perkiraan dari kata kunci di "why") — soal resmi: pengecoh gramatikal, salahnya di makna
Pemakaian: py _kerja/soal_ai/cek_ciri.py
"""
import collections, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE); ROOT = os.path.dirname(K)
sys.path.insert(0, HERE)
from spesifikasi import PANJANG   # noqa: E402
sys.stdout.reconfigure(encoding='utf-8')
CJK = re.compile(r'[一-鿿]')
LV = {'A': 'A0', 'B': 'A1', 'C': 'A2'}
INFER = re.compile(r'意思|覺得|為什麼|可能|說了什麼|在談|會發生|哪一個是對|告訴我們|主要|看法|怎麼想|談什麼|說什麼')
TAKGRAM = re.compile(r'urutan(nya)? salah|tidak gramatikal|salah tata|perlu kata|kurang kata|bukan bentuk|tidak lengkap|tidak bisa dipakai bersama|struktur salah')
hz = lambda s: len(CJK.findall(s or ''))


def muat():
    sumber = {'latihan': {}, 'tes_bab': {}}
    for v in (1, 2, 3):
        for m in json.load(open(f'{ROOT}/data/modul_vol{v}.json', encoding='utf-8'))['modules']:
            sumber['latihan'][m['code']] = m['tasks']
    for f in glob.glob(f'{K}/bank/*.json'):
        sumber['tes_bab'].update(json.load(open(f, encoding='utf-8')))
    return sumber


def part_of(t):
    m = re.match(r'(聽力|閱讀) Part (\d)', t.get('part', ''))
    return f'{m.group(1)} Part {m.group(2)}' if m else '?'


def format_resmi(t, p):
    """Kembalikan alasan tidak sesuai format resmi (None = sesuai)."""
    o = t.get('options', [])
    pic = bool(o) and all(isinstance(x, dict) for x in o)
    n = len(t.get('lines', []))
    if p == '聽力 Part 1':
        return None if t['type'] == 'listen_pic' and len(o) == 3 and not pic else 'bukan 1 gambar + 3 jawaban lisan'
    if p == '聽力 Part 2':
        if t['type'] == 'listen_reply':
            return 'listen_reply (dengar tanya → pilih jawaban teks); resmi: tanya-jawab → gambar'
        return None if n == 2 and pic and len(o) == 3 else f'{n} baris / opsi {"gambar" if pic else "teks"}'
    if p == '聽力 Part 3':
        return None if n == 4 and pic and len(o) == 3 else f'{n} baris / opsi {"gambar" if pic else "teks"} ({len(o)})'
    if p == '聽力 Part 4':
        return None if n == 4 and not pic and len(o) == 4 else f'{n} baris / {len(o)} opsi'
    if p == '閱讀 Part 1':
        return None if pic and len(o) == 3 else 'opsi bukan 3 gambar'
    if p == '閱讀 Part 2':
        return None if not pic and len(o) == 3 and t.get('picture') else 'bukan gambar → 3 kalimat'
    if p == '閱讀 Part 3':
        return None if len(re.findall(r'（\s*）', t.get('text', ''))) == 1 and len(o) == 3 else 'bukan 1 titik + 3 kata'
    if p == '閱讀 Part 4':
        k = len(t.get('answers', []))
        rata = sum(hz(x) for x in o) / max(1, len(o))
        alasan = []
        if k != 5:
            alasan.append(f'{k} titik')
        if rata < 3:
            alasan.append(f'opsi kata/huruf (rata {rata:.1f} hanzi; resmi frasa 3–7)')
        return '; '.join(alasan) or None
    if p == '閱讀 Part 5':
        return None if not pic and len(o) == 4 else f'{len(o)} opsi'
    return 'part tidak dikenal'


def panjang(t, p, lv):
    if p not in PANJANG:
        return None
    lo, hi = PANJANG[p][lv]
    o = t.get('options', [])
    if p == '閱讀 Part 2':
        n = sum(hz(x) for x in o if isinstance(x, str)) / max(1, len(o))
    elif p == '閱讀 Part 4':
        s = t.get('text', '')
        for k, a in enumerate(t.get('answers', [])):
            if 0 <= a < len(o):
                s = s.replace(f'（{k + 1}）', str(o[a]))
        n = hz(s)
    else:
        n = hz(t.get('text', ''))
    return n, lo, hi


def audit(nama, data):
    print(f'\n################ {nama.upper()} — {sum(len(v) for v in data.values())} soal')
    per = collections.defaultdict(lambda: collections.defaultdict(list))
    tumpuk, nanren, total_jaw = [], 0, collections.Counter()
    for code, ts in data.items():
        lv = LV[code[0]]
        jaw = collections.Counter()
        for t in ts:
            p = part_of(t)
            d = per[(p, lv)]
            d['n'].append(1)
            f = format_resmi(t, p)
            d['format'].append(f)
            pj = panjang(t, p, lv)
            if pj:
                d['panjang'].append(pj)
            semua = ' '.join([t.get('question', ''), t.get('text', ''), t.get('audio', '')]
                             + [l['zh'] for l in t.get('lines', [])] + [x for x in t.get('options', []) if isinstance(x, str)])
            if re.search(r'[男女]的', semua):
                nanren += 1
            if p in ('聽力 Part 4', '閱讀 Part 5'):
                d['infer'].append(bool(INFER.search(t.get('question', ''))))
                src = t.get('text', '') + ''.join(l['zh'] for l in t.get('lines', []))
                o = t.get('options', [])
                a = t.get('answer', -1)
                if 0 <= a < len(o) and isinstance(o[a], str):
                    kunci = re.sub(r'[。！？，、\s]', '', o[a])
                    d['kutip'].append(len(kunci) >= 3 and kunci in re.sub(r'[。！？，、\s]', '', src))
            d['takgram'].append(bool(TAKGRAM.search(t.get('why', ''))))
            if 'answer' in t:
                jaw[t['answer']] += 1
                total_jaw[t['answer']] += 1
        if jaw and max(jaw.values()) >= max(4, 0.45 * sum(jaw.values())):
            tumpuk.append(f'{code}:{dict(jaw)}')

    print('Part        | lv | n   | sesuai format resmi | panjang dalam rentang (rata vs target) | inferensial | kunci=kutipan | opsi tak gramatikal*')
    for p in ['聽力 Part 1', '聽力 Part 2', '聽力 Part 3', '聽力 Part 4', '閱讀 Part 1', '閱讀 Part 2', '閱讀 Part 3', '閱讀 Part 4', '閱讀 Part 5']:
        for lv in ('A0', 'A1', 'A2'):
            d = per.get((p, lv))
            if not d:
                continue
            n = len(d['n'])
            fmt = sum(x is None for x in d['format'])
            pj = d['panjang']
            pjs = f"{100 * sum(lo <= x <= hi for x, lo, hi in pj) / len(pj):3.0f}% ({sum(x for x, _, _ in pj) / len(pj):.0f} vs {pj[0][1]}–{pj[0][2]})" if pj else '-'
            inf = f"{100 * sum(d['infer']) / len(d['infer']):.0f}%" if d['infer'] else '-'
            kut = f"{100 * sum(d['kutip']) / len(d['kutip']):.0f}%" if d['kutip'] else '-'
            tg = f"{100 * sum(d['takgram']) / n:.0f}%"
            print(f'{p} | {lv} | {n:3d} | {100 * fmt / n:3.0f}% | {pjs} | {inf} | {kut} | {tg}')
            alasan = collections.Counter(x for x in d['format'] if x)
            for a, c in alasan.most_common(2):
                print(f'      ↳ {c}× {a}')
    print(f'男的/女的: {nanren}')
    tot = sum(total_jaw.values())
    print('Posisi jawaban total:', {('ABCD'[k] if k < 4 else k): f'{100 * v / tot:.0f}%' for k, v in sorted(total_jaw.items())})
    print(f'單元 dengan posisi jawaban menumpuk (≥45% di satu huruf): {len(tumpuk)} dari {len(data)}')
    print('   contoh:', ', '.join(tumpuk[:8]))


if __name__ == '__main__':
    s = muat()
    audit('soal latihan modul', s['latihan'])
    audit('tes bab', s['tes_bab'])
    print('\n* perkiraan dari kata kunci di "why" (mis. "urutannya salah", "perlu kata"); cek manual.')
