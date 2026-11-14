"""Pembantu menulis draf: fungsi singkat pembuat objek soal (dipakai skrip draf per 單元 di scratchpad)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
I1 = 'Lihat gambar. Dengarkan pertanyaan dan jawaban A–C, lalu pilih jawaban yang cocok dengan gambar.'


def g(label, img=None, icon='🖼️'):
    d = {'icon': icon, 'label': label}
    if img:
        d['img'] = img
    return d


def ln(*xs):
    """ln('男:…', '女:…') → lines"""
    return [{'sp': x.split(':', 1)[0], 'zh': x.split(':', 1)[1]} for x in xs]


def P1(pic, q, opts, ans, why, pola):
    return dict(type='listen_pic', part='聽力 Part 1 · Deskripsi gambar', instr=I1, picture=pic, question=q, options=opts,
                answer=ans, why=why, pola_pengecoh=pola)


def P2(lines, q, opts, ans, why, pola):
    return dict(type='listen_dialog', part='聽力 Part 2 · Tanya-jawab satu putaran',
                instr='Dengarkan tanya-jawab singkat, lalu pilih gambar yang cocok.', lines=ln(*lines), question=q,
                options=opts, answer=ans, why=why, pola_pengecoh=pola)


def P3(lines, q, opts, ans, why, pola):
    return dict(type='listen_dialog', part='聽力 Part 3 · Dialog beberapa putaran',
                instr='Dengarkan dialognya, lalu pilih gambar yang menjawab pertanyaan.', lines=ln(*lines), question=q,
                options=opts, answer=ans, why=why, pola_pengecoh=pola)


def P4(lines, q, opts, ans, why, pola):
    return dict(type='listen_dialog', part='聽力 Part 4 · Dialog + makna tersirat',
                instr='Dengarkan dialognya, lalu pilih jawaban yang paling tepat.', lines=ln(*lines), question=q,
                options=opts, answer=ans, why=why, pola_pengecoh=pola)


def R1(text, opts, ans, why, pola):
    return dict(type='read_sent', part='閱讀 Part 1 · Kalimat → gambar', instr='Baca kalimatnya, lalu pilih gambar yang cocok.',
                text=text, options=opts, answer=ans, why=why, pola_pengecoh=pola)


def R2(pic, opts, ans, why, pola):
    return dict(type='read_pick', part='閱讀 Part 2 · Gambar → kalimat', instr='Lihat gambarnya, lalu pilih kalimat yang cocok.',
                picture=pic, options=opts, answer=ans, why=why, pola_pengecoh=pola)


def R3(pic, text, opts, ans, why, pola):
    return dict(type='read_gap', part='閱讀 Part 3 · Isian bergambar',
                instr='Lihat gambarnya, lalu pilih kata yang tepat untuk titik kosong.', picture=pic, text=text, options=opts,
                answer=ans, why=why, pola_pengecoh=pola)


def R4(text, opts, answers, why, lebih):
    return dict(type='cloze', part='閱讀 Part 4 · Melengkapi paragraf',
                instr='Isi setiap titik kosong. Satu pilihan hanya boleh dipakai sekali, dan ada SATU pilihan yang tidak terpakai.',
                text=text, options=opts, answers=answers, why=why, pola_pengecoh={'lebih': lebih})


def R5(text, q, opts, ans, why, pola):
    return dict(type='read_mc', part='閱讀 Part 5 · Pemahaman bacaan', instr='Baca teksnya, lalu pilih jawaban yang paling tepat.',
                text=text, question=q, options=opts, answer=ans, why=why, pola_pengecoh=pola)


def susun(t, urut, why=None, pola=None):
    """Susun ulang opsi soal lama: urut = indeks lama untuk posisi baru. Kunci ikut pindah; why/pola boleh diganti."""
    t = dict(t)
    o = t['options']
    t['options'] = [o[i] for i in urut]
    t['answer'] = urut.index(t['answer'])
    if why:
        t['why'] = why
    if pola:
        t['pola_pengecoh'] = pola
    return t


def tulis(kode, latihan, tes):
    for nama, xs in (('latihan', latihan), ('tes', tes)):
        json.dump(xs, open(f'{HERE}/hasil/{kode}-{nama}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    huruf = lambda xs: ''.join('ABCD'[t['answer']] if 'answer' in t else '-' for t in xs)
    print(kode, 'latihan', huruf(latihan), '| tes', huruf(tes))


def lama(kode):
    """Soal lama: (latihan_isi, latihan_soal, bank)."""
    import sys
    sys.path.insert(0, HERE)
    from pasang import berkas_isi
    K = os.path.dirname(HERE)
    v = {'A': 1, 'B': 2, 'C': 3}[kode[0]]
    _, _, m = berkas_isi(kode)
    import glob
    out = [m.get('tasks', [])]
    for sub in ('soal', 'bank'):
        for p in sorted(glob.glob(f'{K}/{sub}/vol{v}*.json')):
            d = json.load(open(p, encoding='utf-8'))
            if kode in d:
                out.append(d[kode])
    return out
