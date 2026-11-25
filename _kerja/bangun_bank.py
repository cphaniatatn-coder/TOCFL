"""Rakit bank soal Tes Bab: _kerja/bank/*.json → data/bank_soal.json

Tiap bab = 10 butir bergaya TOCFL Band A (lihat analisis-ujian-tocfl.md):
  聽力 P1 ×2  1 gambar + tanya + 3 jawaban lisan  listen_pic (format resmi; listen_pick = format lama)
  聽力 P2 ×1  tanya-jawab 2 baris → gambar  listen_dialog (opsi gambar)
  聽力 P3 ×1  dialog 4 baris + 問 → gambar   listen_dialog (opsi gambar)
  聽力 P4 ×1  dialog 4 baris + 問 → A–D teks listen_dialog (4 opsi teks)
  閱讀 P1 ×1  kalimat → 3 gambar            read_sent
  閱讀 P2 ×1  gambar → 3 kalimat            read_pick
  閱讀 P3 ×1  gambar + kalimat rumpang      read_gap
  閱讀 P4 ×1  paragraf, 5 titik + 6 frasa   cloze  (A0: 3–5 titik, tetap n+1 opsi)
  閱讀 P5 ×1  wacana pendek + 1 soal, A–D   read_mc (4 opsi)
Semua teks Mandarin dicek dengan pemeriksa kosakata modul (hanya kata yang sudah
diajarkan sampai bab itu).

Pemakaian:  py _kerja/bangun_bank.py
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bangun_modul import cek_soal, urut_part
import cek_dialog as cd

K = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(K)
POLA = ['聽力 Part 1', '聽力 Part 1', '聽力 Part 2', '聽力 Part 3', '聽力 Part 4',
        '閱讀 Part 1', '閱讀 Part 2', '閱讀 Part 3', '閱讀 Part 4', '閱讀 Part 5']


def cek_bentuk(code, ts):
    salah = []
    parts = sorted(t['part'][:9] for t in ts)
    if parts != sorted(POLA):
        salah.append(f'komposisi bagian tidak sesuai pola 10 butir: {parts}')
    for t in ts:
        p, pic = t['part'][:9], all(isinstance(o, dict) for o in t.get('options', []))
        if p in ('聽力 Part 2', '聽力 Part 3') and (t['type'] != 'listen_dialog' or not pic or len(t['options']) != 3):
            salah.append(f'{p}: harus listen_dialog dengan 3 opsi gambar')
        if p == '聽力 Part 2' and len(t.get('lines', [])) != 2:
            salah.append('聽力 Part 2: dialog harus 2 baris (tanya-jawab)')
        if p in ('聽力 Part 3', '聽力 Part 4') and len(t.get('lines', [])) != 4:
            salah.append(f'{p}: dialog harus 4 baris')
        if p in ('聽力 Part 4', '閱讀 Part 5') and (pic or len(t['options']) != 4):
            salah.append(f'{p}: harus 4 opsi teks (A–D)')
        if p == '閱讀 Part 4':
            n = len(t['answers'])
            if not (code.startswith('A') and 3 <= n <= 5) and n != 5:
                salah.append(f'閱讀 Part 4: harus 5 titik kosong (A0 boleh 3–5), dapat {n}')
    return [f'{code}: {s}' for s in salah]


# Pola grammar yang baru boleh dipakai mulai bab tertentu (pemeriksa kosakata tidak bisa menangkapnya).
# Hasilnya PERINGATAN untuk ditinjau manual, bukan kegagalan: pola bisa kebetulan cocok (mis. 比 dalam 比賽).
POLA_GRAMMAR = {
    r'的時候': 'C12', r'先[^生]{1,12}再': 'C19', r'還沒': 'C07', r'把[^手]': 'C03', r'越來越|越.{1,4}越': 'C10',
    r'一邊': 'C19', r'(看|試|聽|找|想|查)\1看?': 'C34', r'被': 'B37', r'比(?![賽方較])': 'B19',
    r'(?<!覺)得(很|不|太|非常)': 'B15', r'(看|去|吃|聽|做|學|來|見)過': 'B12', r'了': 'B09', r'著': 'B08',
    r'太.{1,3}了': 'B20', r'跟.{1,6}一樣': 'B19', r'又.{1,3}又': 'B24', r'已經': 'B33',
}


def cek_grammar(code, ts, urut):
    i = urut.index(code)
    out = []
    for t in ts:
        s = ' '.join([t.get('audio', ''), t.get('text', ''), t.get('question', '')] + [l['zh'] for l in t.get('lines', [])]
                     + [o for o in t.get('options', []) if isinstance(o, str)])
        for pola, mulai in POLA_GRAMMAR.items():
            m = re.search(pola, s)
            if m and i < urut.index(mulai):
                out.append(f'{code}: ⚑ pola 「{m.group(0)}」 baru diajarkan di {mulai} — tinjau manual: {s[:40]}')
    return out


# Kaidah penulisan soal resmi 華測會〈命題設計概述〉2022 (slide 34–45; ringkasan di analisis-tesis-rujukan.md E1).
# Hasilnya PERINGATAN ◇ untuk ditinjau; yang sudah ditinjau & diterima dicatat di bank_kaidah_diterima.txt
# (satu baris = teks peringatan sampai sebelum " — ").
HZ = re.compile(r'[一-鿿]')
ANGKA = {'零': 0, '一': 1, '二': 2, '兩': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}


def _hz(s):
    return ''.join(HZ.findall(s or ''))


def _angka(s):
    n, cur = 0, 0
    for ch in s:
        if ch in ANGKA:
            cur = ANGKA[ch]
        else:
            n += (cur or 1) * {'十': 10, '百': 100, '千': 1000, '萬': 10000}[ch]
            cur = 0
    return n + cur


def _nilai(o):
    """Nilai urut sebuah pilihan bila berupa angka/hari/tanggal/jam (untuk kaidah 'urut logis'); None bila bukan."""
    N = '[零一二兩三四五六七八九十百千萬]+'
    m = re.search(r'星期([一二三四五六天日])', o)
    if m:
        return {'天': 7, '日': 7}.get(m.group(1), ANGKA.get(m.group(1)))
    m = re.search(f'({N})月({N})[號日]', o)
    if m:
        return _angka(m.group(1)) * 100 + _angka(m.group(2))
    m = re.search(f'({N})點(半|({N})分)?', o)
    if m and '小時' not in o and _angka(m.group(1)) <= 24:   # jam dinding: 十二點 sebelum 一點 (點 >24 = desimal)
        return (_angka(m.group(1)) % 12) * 60 + (30 if m.group(2) == '半' else _angka(m.group(3)) if m.group(3) else 0)
    m = re.search(N, o)
    if not m or m.start() > 2 or len(_hz(o)) - len(m.group(0)) > 4:
        return None
    return _angka(m.group(0))


def nilai_urut(opts):
    """Nilai urut tiap pilihan bila SEMUA pilihan angka/waktu dengan satuan yang sama (sisa teks tanpa angka
    identik, mis. 三個/十二個); None bila bukan (mis. 兩層/二樓/三個臥室 = besaran berbeda, jangan diurutkan)."""
    nil = [_nilai(o) for o in opts]
    sisa = {re.sub('[零一二兩三四五六七八九十百千萬半]', '', _hz(o)) for o in opts}
    return nil if None not in nil and len(sisa) == 1 else None


def cek_kaidah(code, ts):
    out = []
    for t in ts:
        p = t['part'][:9]
        opts = [o for o in t.get('options', []) if isinstance(o, str)]
        stem = _hz(t.get('text', '') + ''.join(l['zh'] for l in t.get('lines', [])))
        q = t.get('question', '')
        tag = f'{code} {p}'
        if q and t['type'] != 'listen_pic':
            q2 = re.sub(r'(.)[不沒]\1', '', q)
            for w in ('不舒服', '差不多', '不好意思', '對不起', '不客氣', '不只', '不見', '不一樣'):
                q2 = q2.replace(w, '')
            if re.search(r'[不沒]', q2):
                out.append(f'{tag}: ◇ pertanyaan negatif 「{q}」 (hindari 否定問法)')
        for l in t.get('lines', []):
            if 0 < len(_hz(l['zh'])) <= 2:
                out.append(f'{tag}: ◇ giliran sangat pendek 「{l["zh"]}」 (話輪分配平均)')
                break
        if isinstance(t.get('answer'), int) and len(t.get('options', [])) >= 3:
            # huruf di `why` harus cocok dengan kunci (kesalahan lama yang ditemukan: A05, B03, B13, B19, B36)
            L, w = 'ABCD'[t['answer']], t.get('why', '')
            if (re.search(rf'(?<![A-Za-z0-9]){L}(?:(?:,| dan| &) [A-D])*\s*(?::|salah|keliru)', w)
                    or re.search(rf'(?<![A-Za-z0-9])[A-D](?:,| dan| &) {L}\s*:', w)):
                out.append(f'{tag}: ◇ penjelasan menyebut kunci {L} sebagai pilihan salah')
            if any(x != L for x in re.findall(r'→ ([A-D])(?![A-Za-z0-9])', w)):
                out.append(f'{tag}: ◇ penjelasan menunjuk huruf selain kunci {L}')
        if len(opts) < 3 or t['type'] in ('cloze', 'read_gap'):
            continue
        ls = [len(_hz(o)) for o in opts]
        if max(ls) > 15:
            out.append(f'{tag}: ◇ pilihan {max(ls)} hanzi (maks. 15)')
        if min(ls) and max(ls) - min(ls) >= 5 and max(ls) >= 2 * min(ls):
            out.append(f'{tag}: ◇ panjang pilihan timpang {ls} (長度差異不要太大)')
        nil = nilai_urut(opts)
        if nil and nil != sorted(nil) and nil != sorted(nil, reverse=True):
            out.append(f'{tag}: ◇ pilihan angka/waktu tidak urut {opts} (依邏輯次序/時序)')
        if t['type'] != 'listen_pic' and len(opts) == 4 and sum('我' in o.replace('「我」', '') for o in opts) >= 2:
            out.append(f'{tag}: ◇ pilihan memakai 我 (敘述方式為第三人稱視角)')
        if isinstance(t.get('answer'), int) and stem:
            k = _hz(opts[t['answer']])
            if len(k) >= 4 and k in stem:
                out.append(f'{tag}: ◇ kunci 「{opts[t["answer"]]}」 disalin persis dari teks (必須換句話說)')
    return out


def cek_posisi(out):
    """Kaidah 以隨機方式平均分配正確選項的位置: sebaran kunci per volume & jumlah pilihan."""
    hasil, hit = [], {}
    for code, ts in out.items():
        for t in ts:
            if isinstance(t.get('answer'), int) and len(t.get('options', [])) in (3, 4):
                key = (code[0], len(t['options']))
                hit.setdefault(key, [0] * key[1])[t['answer']] += 1
    for (v, n), c in sorted(hit.items()):
        tot = sum(c)
        teks = ' '.join(f'{"ABCD"[i]}={x}' for i, x in enumerate(c))
        if tot >= 2 * n and max(c) - min(c) > max(2, round(0.12 * tot)):
            hasil.append(f'◇ posisi kunci {v}-bab {n} pilihan tidak merata: {teks} (以隨機方式平均分配)')
    return hasil


def main():
    src = {}
    d = f'{K}/bank'
    for fn in sorted(os.listdir(d)):
        if fn.endswith('.json'):
            for code, ts in json.load(open(f'{d}/{fn}', encoding='utf-8')).items():
                if code in src:
                    sys.exit(f'Bab {code} ganda di bank/{fn}')
                src[code] = ts
    mods = cd.urutan()
    urut = [m for m, _ in mods]
    resmi = cd.semua_kata()
    diterima = {tuple(l.split('|')[:2]) for l in open(f'{K}/cek_diterima.txt', encoding='utf-8')
                if l.strip() and not l.startswith('#')}
    masalah, tinjau, out = [], [], {}
    for code in sorted(src, key=urut.index):
        ts = sorted(src[code], key=urut_part)
        for t in ts:
            masalah += cek_soal(code, t)
        masalah += cek_bentuk(code, ts)
        # bentuk yang sudah ditinjau & diterima (cek_diterima.txt, mis. A08 開了) dikenali sebagai satu satuan
        ok = cd.kosakata_sampai(code, mods) | {w for c, w in diterima if c == code}
        for s in cd.teks(ts):
            for ch in cd.cek(s, ok):
                masalah.append(f'{code}: 「{ch}」 belum diajarkan — di: {s[:40]}')
            for w in resmi - ok:
                if w in s and (code, w) not in diterima and not any(len(k) > len(w) and w in k and k in s for k in ok):
                    masalah.append(f'{code}: ⚠ kata resmi 「{w}」 belum diajarkan — di: {s[:40]}')
        tinjau += cek_grammar(code, ts, urut)
        tinjau += cek_kaidah(code, ts)
        for i, t in enumerate(ts):
            t['id'] = f'{code}-{i + 1:02d}'
        out[code] = ts
    diterima_g = set()
    for fn in ('bank_grammar_diterima.txt', 'bank_kaidah_diterima.txt'):
        if os.path.exists(f'{K}/{fn}'):
            diterima_g |= {l.strip() for l in open(f'{K}/{fn}', encoding='utf-8') if l.strip() and not l.startswith('#')}
    tinjau += cek_posisi(out)
    for m in tinjau:
        if m.split(' — ')[0] not in diterima_g:
            print('  ', m)
    for m in masalah:
        print('  ✗', m)
    json.dump(out, open(f'{ROOT}/data/bank_soal.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    n = sum(len(v) for v in out.values())
    print(f'Bank soal: {len(out)} bab, {n} butir. {"0 masalah" if not masalah else str(len(masalah)) + " masalah"}')
    sys.exit(1 if masalah else 0)


if __name__ == '__main__':
    main()
