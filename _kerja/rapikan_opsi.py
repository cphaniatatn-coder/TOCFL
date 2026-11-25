"""Rapikan urutan pilihan bank soal sesuai kaidah 華測會〈命題設計概述〉2022 (slide 40):
  1. pilihan angka/hari/tanggal/jam diurutkan secara logis (依邏輯次序或時序);
  2. posisi kunci soal 4 pilihan teks diratakan per volume (以隨機方式平均分配正確選項的位置) dengan
     menukar kunci ke posisi yang kurang terwakili (hanya soal yang pilihannya bukan angka/waktu);
  3. huruf A–D di `why` (Indonesia) ikut disesuaikan. terjemahan_en.json TIDAK disentuh (English tidak
     dipakai lagi sejak 2026-11-25).

Pemakaian:  py _kerja/rapikan_opsi.py <huruf volume: A|B|C> [tulis]
  tanpa 'tulis' = pratinjau saja (tampilkan setiap why sebelum/sesudah — WAJIB diperiksa).
Sesudahnya: bangun_bank.py → terjemah.py → buat_audio.py (urutan pilihan 聽力 Part 1 ikut terekam).
"""
import hashlib, json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
K = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, K)
from bangun_bank import nilai_urut

HURUF = re.compile(r'(?<![A-Za-z0-9])([A-D])(?![A-Za-z0-9–-])'
                   r'(?=\s*[:,)=]|\.(?:\s|$)|$|\s+&\s|\s+(?:dan|and|atau|or|salah|keliru|kebalikan|kebalikannya|tidak|has|is|'
                   r'are|does|wrong|juga|also|hanya|only|menyebut|menjawab|mentions|says|berkata)\b)')


def ganti_huruf(s, peta):
    s = HURUF.sub(lambda m: 'ABCD'[peta['ABCD'.index(m.group(1))]] if 'ABCD'.index(m.group(1)) in peta else m.group(1), s)
    # daftar huruf yang jadi tak berurutan ("D, B, C:" / "D dan C:" / "D & C:") diurutkan kembali
    s = re.sub(r'(?<![A-Za-z])([A-D](?:, [A-D])+)(?=:)', lambda m: ', '.join(sorted(m.group(1).split(', '))), s)
    return re.sub(r'(?<![A-Za-z])([A-D]) (dan|and|&) ([A-D])(?=:)', lambda m: f'{min(m[1], m[3])} {m[2]} {max(m[1], m[3])}', s)


def berlaku(t):
    o = t.get('options') or []
    return (t['type'] not in ('cloze', 'read_gap') and len(o) >= 3 and all(isinstance(x, str) for x in o)
            and isinstance(t.get('answer'), int))


def terapkan(t, urutan, log, alasan):
    """urutan = indeks lama dalam urutan baru."""
    peta = {lama: baru for baru, lama in enumerate(urutan)}
    if all(k == v for k, v in peta.items()):
        return
    why0 = t['why']
    t['options'] = [t['options'][i] for i in urutan]
    t['answer'] = peta[t['answer']]
    t['why'] = ganti_huruf(why0, peta)
    log.append((alasan, t, why0))


def main():
    vol, tulis = sys.argv[1], 'tulis' in sys.argv[2:]
    d = f'{K}/bank'
    asli = {fn: open(f'{d}/{fn}', encoding='utf-8').read() for fn in sorted(os.listdir(d)) if fn.endswith('.json')}
    files = {fn: json.loads(s) for fn, s in asli.items()}
    items = [(code, t) for data in files.values() for code, ts in data.items() if code.startswith(vol)
             for t in ts if berlaku(t)]
    log = []
    # 1. urutkan pilihan angka/waktu
    angka = set()
    for code, t in items:
        nil = nilai_urut(t['options'])
        if not nil:
            continue
        angka.add(id(t))
        if nil != sorted(nil) and nil != sorted(nil, reverse=True):
            terapkan(t, sorted(range(len(nil)), key=nil.__getitem__), log, f'{code} {t["part"][:9]} urut angka')
    # 2. ratakan posisi kunci soal 4 pilihan
    empat = [(c, t) for c, t in items if len(t['options']) == 4]
    hit = [0] * 4
    for _, t in empat:
        hit[t['answer']] += 1
    print('Posisi kunci 4 pilihan sebelum:', hit)
    bebas = [(c, t) for c, t in empat if id(t) not in angka]
    # urutan acak tetap (hash kode+bagian) supaya pertukaran tersebar di semua bab, bukan menumpuk di bab awal
    bebas.sort(key=lambda ct: hashlib.md5((ct[0] + ct[1]['part']).encode()).hexdigest())
    for c, t in bebas:          # sebar per bab: ambil kandidat berurutan, tukar bila posisinya kelebihan
        hi, lo = max(range(4), key=hit.__getitem__), min(range(4), key=hit.__getitem__)
        if hit[hi] - hit[lo] <= 1:
            break
        if t['answer'] == hi:
            urutan = list(range(4))
            urutan[hi], urutan[lo] = lo, hi
            terapkan(t, urutan, log, f'{c} {t["part"][:9]} kunci {"ABCD"[hi]}→{"ABCD"[lo]}')
            hit[hi] -= 1
            hit[lo] += 1
    print('Posisi kunci 4 pilihan sesudah:', hit)
    for alasan, t, why0 in log:
        print(f'\n## {alasan}\n  pilihan: {t["options"]}  kunci={"ABCD"[t["answer"]]}\n  why lama: {why0}\n  why baru: {t["why"]}')
    print(f'\n{len(log)} butir diubah.' + ('' if tulis else ' (pratinjau — tambahkan "tulis" untuk menyimpan)'))
    if tulis:
        for fn, data in files.items():   # hanya file yang berubah; format sama dengan aslinya (indent 1 + baris akhir)
            baru = json.dumps(data, ensure_ascii=False, indent=1) + '\n'
            if baru != asli[fn]:
                open(f'{d}/{fn}', 'w', encoding='utf-8').write(baru)


if __name__ == '__main__':
    main()
