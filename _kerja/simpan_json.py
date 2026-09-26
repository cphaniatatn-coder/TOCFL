"""Simpan file sumber soal TANPA mengubah format aslinya (supaya riwayat git hanya memuat perubahan nyata).

- File berformat json.dump(indent=1) → ditulis ulang dengan format yang sama.
- File isi/ Vol.2–3 yang ditulis ringkas (tiap soal 2–3 baris) → hanya objek soal yang berubah yang diganti,
  di tempatnya, dengan gaya ringkas yang sama. Syarat: jumlah & urutan soal tidak berubah.
File yang isinya tidak berubah tidak disentuh sama sekali.
"""
import json


def _akhir_objek(t, i):
    """Indeks setelah '}' penutup objek yang dimulai di t[i] == '{' (memperhitungkan string)."""
    d, s, esc = 0, False, False
    for j in range(i, len(t)):
        c = t[j]
        if s:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == '"': s = False
        elif c == '"': s = True
        elif c == '{': d += 1
        elif c == '}':
            d -= 1
            if d == 0:
                return j + 1
    raise ValueError('objek tidak tertutup')


def _ringkas(t):
    """Gaya ringkas file isi/: baris 1 = type/part/instr, baris 2 = isi soal, baris 3 = why."""
    j = lambda k: f'"{k}": {json.dumps(t[k], ensure_ascii=False)}'
    satu = [k for k in ('type', 'part', 'instr') if k in t]
    tiga = [k for k in ('why', 'id') if k in t]
    dua = [k for k in t if k not in satu + tiga]
    baris = [', '.join(j(k) for k in satu), ', '.join(j(k) for k in dua), ', '.join(j(k) for k in tiga)]
    return '{' + ',\n   '.join(b for b in baris if b) + '}'


def _soal_urut(d):
    if isinstance(d, dict) and 'modules' in d:
        return [t for m in d['modules'] for t in m.get('tasks', [])]
    if isinstance(d, dict) and 'tasks' in d:
        return list(d['tasks'])
    return [t for ts in d.values() for t in ts]


def simpan(p, baru):
    """Tulis data baru ke p dengan mempertahankan format. Kembalikan True bila file berubah."""
    teks = open(p, encoding='utf-8').read()
    lama = json.loads(teks)
    if lama == baru:
        return False
    if json.dumps(lama, ensure_ascii=False, indent=1) == teks.rstrip('\n'):
        akhir = '\n' if teks.endswith('\n') else ''          # pertahankan ada/tidaknya baris baru di akhir file
        open(p, 'w', encoding='utf-8').write(json.dumps(baru, ensure_ascii=False, indent=1) + akhir)
        return True
    # format ringkas: cari objek soal ({"type": …) berurutan dan ganti yang berubah
    lama_s, baru_s = _soal_urut(lama), _soal_urut(baru)
    if len(lama_s) != len(baru_s):
        raise ValueError(f'{p}: jumlah soal berubah — format ringkas tidak bisa dipertahankan')
    rentang, i = [], 0
    while True:
        i = teks.find('{"type": "', i)
        if i < 0:
            break
        e = _akhir_objek(teks, i)
        rentang.append((i, e)); i = e
    if len(rentang) != len(lama_s) or any(json.loads(teks[a:b]) != o for (a, b), o in zip(rentang, lama_s)):
        raise ValueError(f'{p}: objek soal di teks tidak cocok dengan data — tidak ditulis')
    out, akhir = [], 0
    for (a, b), o, n in zip(rentang, lama_s, baru_s):
        out.append(teks[akhir:a]); out.append(teks[a:b] if o == n else _ringkas(n)); akhir = b
    out.append(teks[akhir:])
    hasil = ''.join(out)
    if json.loads(hasil) != baru:
        raise ValueError(f'{p}: hasil penggantian tidak sama dengan data baru (ada perubahan di luar soal?) — tidak ditulis')
    open(p, 'w', encoding='utf-8', newline='').write(hasil)
    return True
