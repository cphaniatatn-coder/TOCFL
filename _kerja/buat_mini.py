"""Bangun repo MODUL MINI (uji coba thesis: kecemasan ujian, pre/post test) dari app utama.

Keputusan Carli 2026-10-03: 6 bab per level (tema & grammar yang paling sering muncul di mock test), bab diambil
APA ADANYA dari app utama (tidak disusun ulang), repo terpisah untuk dibagikan ke peserta, 3 bahasa (id/en/vi).

    py _kerja/buat_mini.py          → tulis seluruh repo mini ke folder `out` di _kerja/mini/config.json
    py _kerja/buat_mini.py cek      → hanya laporkan teks yang belum diterjemahkan (tanpa menulis)

Sumber (semuanya di repo utama — repo mini TIDAK diedit tangan):
  data/*.json + data/en/*.json        isi 18 bab, Tes Bab, rencana (id + en)
  _kerja/mini/tes_A{0,1,2}.json       tes awal (paket A) & tes akhir (paket B) — cek: py _kerja/mini/cek_tes.py
  _kerja/mini/kuesioner.json          skala kecemasan, evaluasi modul, deskripsi level (id/en/vi)
  _kerja/mini/kamus_mini.json         {"teks Indonesia": {"en": …, "vi": …}} — terjemahan isi yang belum ada di
                                      _kerja/terjemahan_en.json (en) dan SEMUA terjemahan Vietnam (vi)
  _kerja/mini/ui_vi.json              teks antarmuka English → Vietnam (pola {0} {1} untuk teks bernilai)
  _kerja/mini/web/                    index.html, js/lang.js, js/studi.js, css/studi.css khusus mini
  _kerja/mini/config.json             {"out": folder repo mini, "kirim_url": URL Apps Script penerima}
Teks yang belum diterjemahkan tetap tampil Indonesia/English dan didaftar di _kerja/mini/kurang_{en,vi,ui}.txt.

Kata pendukung: kata di dialog/soal/contoh bab yang diajarkan di bab LAIN pada level yang sama yang tidak ikut uji
coba → vocab.pendukung (bisa diketuk di dialog + daftar di tahap 詞彙). Kata level di bawahnya dianggap sudah
dikuasai peserta yang memilih level itu.
"""
import json, os, re, shutil, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
K = Path(__file__).resolve().parent; R = K.parent; M = K / 'mini'
sys.path.insert(0, str(K))
import cek_dialog as cd
import terjemah as tj

MINI = {1: ['A02', 'A04', 'A09', 'A10', 'A18', 'A24'],
        2: ['B04', 'B19', 'B20', 'B30', 'B33', 'B40'],
        3: ['C04', 'C16', 'C24', 'C28', 'C40', 'C58']}
SEMUA = [c for v in MINI.values() for c in v]
LEVEL = {'A0': 1, 'A1': 2, 'A2': 3}
CFG = json.loads((M / 'config.json').read_text(encoding='utf-8'))
OUT = (K / CFG['out']).resolve() if not os.path.isabs(CFG['out']) else Path(CFG['out'])
JS = ['media.js', 'app.js', 'modul.js', 'latihan.js', 'ujian.js']
# Label bagian & petunjuk soal tes = sama persis dengan bank soal Tes Bab (terjemahannya sudah ada)
BAGIAN = {
    ('listen_pic', '聽力 Part 1'): ('聽力 Part 1 · Deskripsi gambar', 'Lihat gambar. Dengarkan pertanyaan dan jawaban A–C, lalu pilih jawaban yang cocok dengan gambar.'),
    ('listen_dialog', '聽力 Part 2'): ('聽力 Part 2 · Tanya-jawab satu putaran', 'Dengarkan tanya-jawab singkat, lalu pilih gambar yang cocok.'),
    ('listen_dialog', '聽力 Part 3'): ('聽力 Part 3 · Dialog beberapa putaran', 'Dengarkan dialognya, lalu pilih gambar yang menjawab pertanyaan.'),
    ('listen_dialog', '聽力 Part 4'): ('聽力 Part 4 · Dialog + makna tersirat', 'Dengarkan dialognya, lalu pilih jawaban yang paling tepat.'),
    ('read_sent', '閱讀 Part 1'): ('閱讀 Part 1 · Kalimat → gambar', 'Baca kalimatnya, lalu pilih gambar yang cocok.'),
    ('read_pick', '閱讀 Part 2'): ('閱讀 Part 2 · Gambar → kalimat', 'Lihat gambarnya, lalu pilih kalimat yang cocok.'),
    ('read_gap', '閱讀 Part 3'): ('閱讀 Part 3 · Isian bergambar', 'Lihat gambarnya, lalu pilih kata yang tepat untuk titik kosong.'),
    ('cloze', '閱讀 Part 4'): ('閱讀 Part 4 · Melengkapi paragraf', 'Isi setiap titik kosong. Satu pilihan hanya boleh dipakai sekali, dan ada SATU pilihan yang tidak terpakai.'),
    ('read_mc', '閱讀 Part 5'): ('閱讀 Part 5 · Pemahaman bacaan', 'Baca teksnya, lalu pilih jawaban yang paling tepat.'),
}


def baca(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def tulis(p, d):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')


# ---------- data Indonesia: 18 bab + kata pendukung ----------
def zh_bab(m, bank):
    """Semua teks Mandarin yang tampil di bab: dialog, tugas, contoh grammar, daur ulang, Tes Bab."""
    out = [l['zh'] for d in m['dialogs'] for l in d['lines']]
    out += [s for t in m['tasks'] + bank for s in cd.teks(t) if isinstance(s, str)]
    out += [e['zh'] for g in m['grammar'] for e in g['examples']] + [r['zh'] for r in m.get('recycle', [])]
    return out


def pecah(s, ok):
    """Segmentasi rakus (kata terpanjang dulu), sama dengan pemeriksa kosakata; kembalikan kata yang dikenali."""
    hasil = []
    for seg in re.findall(r'[一-鿿]+', s):
        i = 0
        while i < len(seg):
            for L in range(min(6, len(seg) - i), 0, -1):
                if seg[i:i + L] in ok:
                    hasil.append(seg[i:i + L]); i += L; break
            else:
                i += 1
    return hasil


def data_id():
    vols = {v: baca(R / f'data/modul_vol{v}.json') for v in (1, 2, 3)}
    bank = baca(R / 'data/bank_soal.json')
    urut = cd.urutan()
    # kata → (bab yang mengajarkan, entri kosakata)
    entri, asal = {}, {}
    for v, d in vols.items():
        for m in d['modules']:
            for e in m['vocab']['core'] + m['vocab']['supplement']:
                for w in {e['w'], *(e.get('variants') or '').split('/')} - {''}:
                    entri.setdefault(w, e); asal.setdefault(w, m['code'])
    for v, d in vols.items():
        for m in d['modules']:
            if m['code'] not in SEMUA:
                continue
            lv = m['code'][0]
            ok = cd.kosakata_sampai(m['code'], urut)
            sendiri = {e['w'] for e in m['vocab']['core'] + m['vocab']['supplement']}
            pend, lihat = [], set()
            for s in zh_bab(m, bank.get(m['code'], [])):
                for w in pecah(s, ok):
                    a = asal.get(w)
                    if a and a[0] == lv and a not in SEMUA and w not in sendiri and entri[w]['w'] not in lihat:
                        lihat.add(entri[w]['w'])
                        e = entri[w]
                        pend.append({k: e[k] for k in ('w', 'py', 'zy', 'pos', 'meaning', 'say') if e.get(k)} | {'dari': asal[e['w']]})
            m['vocab']['pendukung'] = pend
        d['modules'] = [m for m in d['modules'] if m['code'] in SEMUA]
    rencana = {k: [m for m in ms if m['code'] in SEMUA] for k, ms in baca(R / 'data/rencana.json').items()}
    bank = {c: bank[c] for c in SEMUA if c in bank}
    pasang_gambar_bab(vols, bank)
    pasang_catatan_grammar(vols)
    return vols, bank, rencana


def pasang_catatan_grammar(vols):
    """Tahap 語法聚焦 modul mini:
    - catatan dari buku rujukan (_kerja/mini/catatan_grammar.json, 基礎篇 & 進階篇) → grammar[i].catatan / modul.catatan
    - soal latihan tambahan (_kerja/mini/latihan_grammar.json, dibuat latihan_grammar.py) → grammar[i].latihan / modul.latihan
    Teks Indonesia dipasang di sini; English/Vietnam lewat catatan_kamus() di penerjemah."""
    C = baca(M / 'catatan_grammar.json') if (M / 'catatan_grammar.json').exists() else {}
    L = baca(M / 'latihan_grammar.json')['soal'] if (M / 'latihan_grammar.json').exists() else {}
    blok = lambda b: ({'point': b['point']['id']} if 'point' in b else {}) | {
        'rujukan': f'《看圖學中文語法・{b["buku"]}》 {b["unit"]}', 'note': [n['id'] for n in b['note']]}
    for d in vols.values():
        for m in d['modules']:
            c, l = C.get(m['code'], {}), L.get(m['code'], {})
            for i, g in enumerate(m['grammar'], 1):
                if f'g{i}' in c: g['catatan'] = [blok(b) for b in c[f'g{i}']]
                if f'g{i}' in l: g['latihan'] = l[f'g{i}']
            if 'bab' in c: m['catatan'] = [blok(b) for b in c['bab']]
            if 'bab' in l: m['latihan'] = l['bab']


def catatan_kamus():
    """{teks Indonesia: {en, vi}} dari catatan_grammar.json & latihan_grammar.json, untuk penerjemah()."""
    out = {}
    p = M / 'catatan_grammar.json'
    if p.exists():
        for kode, c in baca(p).items():
            if kode.startswith('_'): continue
            for daftar in c.values():
                for b in daftar:
                    for n in b['note'] + ([b['point']] if 'point' in b else []):
                        out[n['id']] = {'en': n['en'], 'vi': n['vi']}
    p = M / 'latihan_grammar.json'
    if p.exists():
        out.update(baca(p)['kamus'])
    return out


def pasang_gambar_bab(vols, bank):
    """Ilustrasi SVG 溝通任務 & Tes Bab (_kerja/mini/gambar_bab.py) menggantikan ikon emoji.
    Dipasang hanya bila keterangan gambar di data masih sama dengan saat digambar (gambar_bab_label.json);
    bila soal diedit, ikon tetap dipakai dan dilaporkan supaya digambar ulang."""
    p = M / 'gambar_bab_label.json'
    if not p.exists():
        return
    label, basi = baca(p), []
    def cocok(kunci, ket):
        if kunci not in label: return False
        if label[kunci] != ket: basi.append(kunci); return False
        return (R / f'img/soal/{kunci}.svg').exists()
    for d in vols.values():
        for m in d['modules']:
            for k, daftar in (('t', m['tasks']), ('b', bank.get(m['code'], []))):
                for i, t in enumerate(daftar, 1):
                    kunci = f'M{m["code"]}-{k}{i}'
                    if t.get('picture') and not t['picture'].get('img') and cocok(kunci, t['picture']['label']):
                        t['picture'] = dict(t['picture'], img=kunci)
                    if any(isinstance(o, dict) for o in t.get('options', [])):
                        t['options'] = [dict(o, img=kunci + 'abc'[j]) if isinstance(o, dict) and cocok(kunci + 'abc'[j], o['label']) else o
                                        for j, o in enumerate(t['options'])]
    if basi:
        print(f'⚑ {len(basi)} gambar bab tidak dipasang karena keterangannya berubah (gambar ulang: py _kerja/mini/gambar_bab.py):', ', '.join(basi))


def data_studi():
    """studi.json versi Indonesia: tes per level & paket + kuesioner (dibahasakan nanti)."""
    tes = {}
    for lv in LEVEL:
        T = baca(M / f'tes_{lv}.json')
        tes[lv] = {}
        for paket, items in T.items():
            out = []
            for t in items:
                t = {k: v for k, v in t.items() if k != 'tema'}
                t['part'], t['instr'] = BAGIAN[(t['type'], t['part'][:9])]
                if t.get('picture', {}).get('img') is None and os.path.exists(R / f'img/soal/T{lv}{paket}-{t["no"]}.svg'):
                    t.setdefault('picture', {})['img'] = f'T{lv}{paket}-{t["no"]}'
                # pilihan bergambar → ilustrasi T<lv><paket>-<no><a|b|c>.svg (_kerja/mini/gambar_pilihan.py)
                t['options'] = [dict(o, img=f'T{lv}{paket}-{t["no"]}{"abc"[k]}')
                                if isinstance(o, dict) and os.path.exists(R / f'img/soal/T{lv}{paket}-{t["no"]}{"abc"[k]}.svg') else o
                                for k, o in enumerate(t['options'])]
                out.append(t)
            tes[lv][paket] = out
    return {'tes': tes}


def kuesioner(lang):
    Q = baca(M / 'kuesioner.json')
    # 'tb' = teks untuk peserta yang belum pernah ikut TOCFL (hanya butir yang punya versi 'baru')
    return {'likert': Q['likert'][lang], 'petunjukBaru': Q['petunjuk_baru'][lang],
            'cemas': [{'dim': d['dim'][lang], 'items': [{'t': it[lang], 'r': it['r'], **({'tb': it['baru'][lang]} if 'baru' in it else {})}
                                                         for it in d['items']]} for d in Q['cemas']],
            'eval': [x[lang] for x in Q['eval']], 'terbuka': [x[lang] for x in Q['terbuka']],
            'level': {k: v[lang] for k, v in Q['level'].items()}}


# ---------- terjemahan ----------
def penerjemah(lang, kurang):
    utama = baca(K / 'terjemahan_en.json') if lang == 'en' else {}
    mini = baca(M / 'kamus_mini.json') if (M / 'kamus_mini.json').exists() else {}
    mini = {**mini, **catatan_kamus()}
    def tr(s):
        x = (mini.get(s) or {}).get(lang) or utama.get(s)
        if x is None:
            kurang.setdefault(s, None)
            return s
        return x
    return tr


# ---------- teks antarmuka (T('English', 'Indonesia')) ----------
def argumen_T(src):
    """Argumen pertama setiap T(…) — string '…' atau template `…${…}…` (boleh bersarang) → kunci dengan {0} {1}."""
    out = []
    for m in re.finditer(r'(?<![\w.])T\(\s*([\'`])', src):
        q, i, buf, n, depth = m.group(1), m.end(), '', 0, 0
        while i < len(src):
            c = src[i]
            if c == '\\':
                buf += src[i + 1]; i += 2; continue
            if q == '`' and src.startswith('${', i):
                # lewati ekspresi ${…} sampai kurung kurawal penutup yang seimbang
                j, d = i + 2, 1
                while d:
                    d += {'{': 1, '}': -1}.get(src[j], 0); j += 1
                buf += '{%d}' % n; n += 1; i = j; continue
            if c == q:
                break
            buf += c; i += 1
        out.append(buf)
    return out


UI_EXTRA = [  # teks English di luar T(): nama & petunjuk bagian ujian (Ujian.PARTS), strategi refleksi
    'Picture description', 'Question & answer', 'Dialogue', 'Implied meaning', 'Sentence → picture', 'Picture → sentence',
    'Gap fill with picture', 'Paragraph completion', 'Reading comprehension',
    'Look at the picture, listen to the question and three answers (A–C), then choose the one that matches the picture.',
    'Listen to a short exchange and choose the right picture or response.', 'Listen to a dialogue of several turns and the question.',
    'Listen to the dialogue and catch what is meant but not said directly. Choose A–D.', 'Read one sentence and choose the matching picture.',
    'Look at the picture and choose the matching sentence.', 'Look at the picture and choose the right word for the blank.',
    'Fill in the blanks in the paragraph. Each option can be used only once; some options are not used.', 'Read a short text and choose answer A–D.',
    'Replay the dialogue and listen', 'Practise the 核心 words with audio', 'Redo the tasks', 'Move on to the next module',
]


def ui_kunci():
    keys = []
    for f in JS:
        keys += argumen_T((R / 'js' / f).read_text(encoding='utf-8'))
    keys += argumen_T((M / 'web/js/studi.js').read_text(encoding='utf-8'))
    return list(dict.fromkeys(keys + UI_EXTRA))


# ---------- salin & tulis ----------
def salin_js(src):
    s = src.read_text(encoding='utf-8')
    s = s.replace("'tocfl_", "'tocflmini_")          # penyimpanan terpisah dari app utama (satu origin github.io)
    if src.name == 'modul.js':                       # sorotan dialog = kosakata bab + kata pendukung
        for a, b in [("const all = this.allVocab().map((v, i) => [v.w, i])", "const all = this.hlVocab().map((v, i) => [v.w, i])"),
                     ("this.allVocab()[hit[1]].layer", "this.hlVocab()[hit[1]].layer"),
                     ("const v = this.allVocab()[idx];", "const v = this.hlVocab()[idx];")]:
            assert a in s, f'modul.js berubah — sesuaikan tambalan buat_mini.py: {a}'
            s = s.replace(a, b)
    return s


def nama_audio():
    """Nama file mp3 yang dipakai 18 bab + tes (logika sama dengan buat_audio.kumpulkan)."""
    import buat_audio as ba
    job = set()
    def tambah(prof, text):
        if (text or '').strip(): job.add(f'{prof}|{text.strip()}')
    def soal(t):
        for l in t.get('lines', []):
            tambah(ba.PEMBICARA.get(l['sp'], 'F1'), l['zh'])
        if t.get('audio'): tambah('N', t['audio'])
        if t.get('type') == 'listen_pic':
            for x in [t['question']] + [f'{"ABC"[i]}，{o}' for i, o in enumerate(t['options'])]:
                tambah('N', x)
    vols, bank, _ = data_id()
    for d in vols.values():
        for m in d['modules']:
            tambah('N', m['title'])
            for dl in m['dialogs']:
                for l in dl['lines']: tambah(ba.PEMBICARA.get(l['sp'], 'F1'), l['zh'])
            for t in m['tasks']: soal(t)
            for g in m['grammar']:
                for e in g['examples']: tambah('N', e['zh'])
            for r in m.get('recycle', []): tambah('N', r['zh'])
            for e in m['vocab']['core'] + m['vocab']['supplement'] + m['vocab']['pendukung']:
                tambah('W', e.get('say') or e['w'])
    for ts in bank.values():   # bank = Tes Bab 18 bab mini saja
        for t in ts:
            soal(t)
            if t['type'] == 'listen_dialog' and t.get('question'): tambah('N', t['question'])   # 問 dibacakan (gaya TOCFL)
    for lv in LEVEL:
        for items in baca(M / f'tes_{lv}.json').values():
            for t in items:
                soal(t)
                if t['type'] == 'listen_dialog' and t.get('question'): tambah('N', t['question'])   # 問 dibacakan (gaya TOCFL)
    return {ba.nama(k) for k in job}


def main():
    hanya_cek = 'cek' in sys.argv[1:]
    vols, bank, rencana = data_id()
    studi = data_studi()
    kurang = {'en': {}, 'vi': {}}
    paket = {}
    for lang in ('id', 'en', 'vi'):
        tr = (lambda s: s) if lang == 'id' else penerjemah(lang, kurang[lang])
        j = lambda o: tj.jalan(o, None, tr)
        paket[lang] = {**{f'modul_vol{v}.json': j(d) for v, d in vols.items()},
                       'bank_soal.json': j(bank), 'rencana.json': j(rencana),
                       'studi.json': {**j(studi), 'kuesioner': kuesioner(lang)}}
    vi_ui = baca(M / 'ui_vi.json') if (M / 'ui_vi.json').exists() else {}
    ui_kurang = [k for k in ui_kunci() if k not in vi_ui]
    for nama, isi in [('kurang_en.txt', kurang['en']), ('kurang_vi.txt', kurang['vi']), ('kurang_ui.txt', ui_kurang)]:
        p = M / nama
        if isi:
            p.write_text('\n'.join(json.dumps(s, ensure_ascii=False) for s in isi) + '\n', encoding='utf-8')
        else:
            p.unlink(missing_ok=True)
    print(f'belum diterjemahkan: en {len(kurang["en"])} · vi {len(kurang["vi"])} · antarmuka vi {len(ui_kurang)}  (_kerja/mini/kurang_*.txt)')
    for lv, v in LEVEL.items():
        print(f'  {lv}: kata pendukung per bab', {m["code"]: len(m["vocab"]["pendukung"]) for m in vols[v]["modules"]})
    if hanya_cek:
        return

    # Kumpulkan semua file target dulu, lalu SINKRONKAN: hanya file yang berubah yang ditulis, file yang tidak
    # dipakai lagi dihapus (folder di OneDrive sering terkunci bila dihapus sekaligus).
    F = {}   # path relatif → bytes atau Path sumber
    for lang, files in paket.items():
        for fn, d in files.items():
            F[f'data/{lang}/{fn}'] = json.dumps(d, ensure_ascii=False, separators=(',', ':')).encode()
    web = M / 'web'
    for f in web.rglob('*'):
        if f.is_file():
            s = f.read_text(encoding='utf-8')
            if f.name == 'studi.js':
                s = s.replace("const KIRIM_URL = '';", f"const KIRIM_URL = {json.dumps(CFG.get('kirim_url', ''))};")
            F[f.relative_to(web).as_posix()] = s.encode()
    for f in JS:
        F[f'js/{f}'] = salin_js(R / 'js' / f).encode()
    F['js/vi.js'] = ('/* Teks antarmuka Vietnam — dibuat _kerja/buat_mini.py dari _kerja/mini/ui_vi.json */\nwindow.VI_UI = '
                     + json.dumps(vi_ui, ensure_ascii=False, indent=0) + ';\n').encode()
    for f in ('style.css', 'kai.css'):
        F[f'css/{f}'] = R / 'css' / f
    # ?v=<hash isi> di index.html: GitHub Pages meng-cache JS/CSS 10 menit, jadi tanpa ini browser bisa memakai versi lama
    import hashlib
    isi = lambda v: v.read_bytes() if isinstance(v, Path) else v
    data_v = hashlib.md5(b''.join(isi(F[k]) for k in sorted(F) if k.startswith('data/'))).hexdigest()[:8]
    F['index.html'] = F['index.html'].replace(b"window.DATA_V = '';", f"window.DATA_V = '{data_v}';".encode())
    F['index.html'] = re.sub(r'((?:src|href)="((?:js|css)/[^"?]+))"',
                             lambda m: f'{m[1]}?v={hashlib.md5(isi(F[m[2]])).hexdigest()[:8]}"' if m[2] in F else m[0],
                             F['index.html'].decode()).encode()
    for f in (R / 'img').rglob('*'):
        if f.is_file():
            F[f.relative_to(R).as_posix()] = f
    audio = nama_audio()
    ada = [n for n in sorted(audio) if (R / f'audio/tts/{n}.mp3').exists()]
    for n in ada:
        F[f'audio/tts/{n}.mp3'] = R / f'audio/tts/{n}.mp3'
    F['.nojekyll'] = b''
    F['README.md'] = (
        '# TOCFL Band A — modul uji coba\n\nVersi mini (18 bab: 6 per level A0/A1/A2) dari app modul TOCFL Band A, untuk uji coba thesis:\n'
        'kuesioner kecemasan + tes awal → 6 bab → kuesioner + tes akhir + evaluasi modul. Bahasa: Indonesia · English · Tiếng Việt.\n\n'
        '**Jangan edit repo ini langsung.** Semua file dibuat ulang oleh `py _kerja/buat_mini.py` di repo utama (`cphaniatatn-coder/TOCFL`).\n\n'
        'Ilustrasi: Twemoji © Twitter/X & kontributor (CC-BY 4.0); gambar soal hitam-putih: OpenMoji (CC BY-SA 4.0).\n').encode()
    tulis_n = hapus_n = 0
    for rel, src in F.items():
        dst = OUT / rel
        isi = src if isinstance(src, bytes) else None
        if isi is None:
            if dst.exists() and dst.stat().st_size == src.stat().st_size and dst.read_bytes() == src.read_bytes():
                continue
            isi = src.read_bytes()
        elif dst.exists() and dst.read_bytes() == isi:
            continue
        dst.parent.mkdir(parents=True, exist_ok=True); dst.write_bytes(isi); tulis_n += 1
    for f in sorted(OUT.rglob('*'), reverse=True):
        rel = f.relative_to(OUT).as_posix()
        if rel == '.git' or rel.startswith('.git/'):
            continue
        if f.is_file() and rel not in F:
            f.unlink(); hapus_n += 1
        elif f.is_dir() and not any(f.iterdir()):
            f.rmdir()
    print(f'{tulis_n} file ditulis, {hapus_n} dihapus')
    print(f'repo mini: {OUT} · audio {len(ada)}/{len(audio)} file' + ('' if len(ada) == len(audio) else ' — jalankan py _kerja/buat_audio.py untuk yang kurang'))


if __name__ == '__main__':
    main()
