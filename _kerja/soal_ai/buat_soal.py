"""Pembuat soal bergaya TOCFL Band A dengan AI + validasi aturan + tinjauan manusia.

Alur:  brief per 單元 (kosakata & grammar yang sudah diajarkan, spesifikasi tiap Part dari analisis mock test)
       → AI membuat soal (JSON) → validator (format, kosakata level, pola grammar, ciri TOCFL)
       → soal yang gagal dikirim balik ke AI beserta kesalahannya (maks. --putaran kali)
       → hasil + lembar tinjauan untuk Carli. TIDAK otomatis masuk bank soal.

Pemakaian (dari root repo):
  py _kerja/soal_ai/buat_soal.py B20                         # 10 butir (komposisi Tes Bab), lewat Claude API
  py _kerja/soal_ai/buat_soal.py B20 --part "聽力 Part 3" --part "閱讀 Part 5" --n 2
  py _kerja/soal_ai/buat_soal.py B20 --tanpa-api             # tulis prompt saja (dipakai di sesi Claude Code / chat)
  py _kerja/soal_ai/buat_soal.py B20 --periksa soal.json     # validasi soal yang dibuat di luar skrip

Mode API butuh:  pip install anthropic   dan kredensial (ANTHROPIC_API_KEY atau `ant auth login`).
Keluaran: _kerja/soal_ai/hasil/<kode>.json + <kode>-tinjau.md ; log lengkap (prompt, jawaban, pemakaian token)
di _kerja/soal_ai/log/ — bukti pembagian peran AI/peneliti untuk thesis.
"""
import argparse, collections, datetime, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE)
ROOT = os.path.dirname(K)
sys.path.insert(0, K)
sys.path.insert(0, HERE)
import cek_dialog as cd                                   # noqa: E402
from bangun_modul import cek_soal                         # noqa: E402
from bangun_bank import POLA_GRAMMAR                      # noqa: E402
from spesifikasi import PART, POLA, KOMPOSISI, KOMPOSISI_LATIHAN, PANJANG, ATURAN_UMUM   # noqa: E402
from cek_ciri import INFER                                                    # noqa: E402

MODEL = 'claude-opus-5-5'
CJK = re.compile(r'[一-鿿]')
LV = {'A': 'A0', 'B': 'A1', 'C': 'A2'}
HURUF = 'ABCDEF'


# ---------------------------------------------------------------- konteks 單元
BACA = {r'先[^生]{1,12}再': '先…再…', r'越來越|越.{1,4}越': '越來越… / 越…越…', r'(看|試|聽|找|想|查)\1看?': 'VV(看) (看看, 試試…)',
        r'把[^手]': '把 + objek', r'比(?![賽方較])': '比 (perbandingan)', r'(?<!覺)得(很|不|太|非常)': 'V得 + derajat (跑得很快)',
        r'(看|去|吃|聽|做|學|來|見)過': 'V過 (pengalaman)', r'太.{1,3}了': '太…了', r'跟.{1,6}一樣': '跟…一樣',
        r'又.{1,3}又': '又…又…'}


def ramah(p):
    return BACA.get(p, p)


def muat():
    mods = []
    for v in (1, 2, 3):
        mods += json.load(open(f'{ROOT}/data/modul_vol{v}.json', encoding='utf-8'))['modules']
    return {m['code']: m for m in mods}


def konteks(code, modul):
    plan = cd.urutan()
    urut = [c for c, _ in plan]
    if code not in urut:
        sys.exit(f'Kode 單元 tidak dikenal: {code}')
    i = urut.index(code)
    diterima = {tuple(l.split('|')[:2]) for l in open(f'{K}/cek_diterima.txt', encoding='utf-8')
                if l.strip() and not l.startswith('#')}
    ok = cd.kosakata_sampai(code, plan) | {w for c, w in diterima if c == code}
    m = modul[code]
    target = [w['w'] for lay in ('core', 'supplement') for w in m['vocab'][lay]]
    grammar_lama = []
    for c in urut[:i + 1]:
        for g in modul[c].get('grammar', []):
            grammar_lama.append(f"{c}: {g.get('pattern') or g.get('point')}")
    target_g = [f"{g.get('pattern')} — {g.get('point')}" for g in m.get('grammar', [])]
    terlarang = [f'「{ramah(p)}」 (baru di {mulai})' for p, mulai in POLA_GRAMMAR.items() if urut.index(mulai) > i]
    terlarang += [f'「{p}」 (baru di {mulai})' for p, mulai in cd.PARTIKEL.items() if urut.index(mulai) > i]
    return dict(code=code, i=i, urut=urut, ok=ok, level=LV[code[0]], judul=m['title'], scene=m.get('scene', ''),
                can_do=m.get('can_do', ''), target=target, target_g=target_g, grammar_lama=grammar_lama,
                terlarang=terlarang, resmi=cd.semua_kata())


def contoh(part, ktx):
    """Satu contoh soal yang sudah disetujui, dari 單元 sebelumnya di level yang sama (atau terdekat)."""
    bank = {}
    for fn in sorted(os.listdir(f'{K}/bank')):
        if fn.endswith('.json'):
            bank.update(json.load(open(f'{K}/bank/{fn}', encoding='utf-8')))
    for c in reversed(ktx['urut'][:ktx['i']]):
        for t in bank.get(c, []):
            if t['part'].startswith(part):
                t = {k: v for k, v in t.items() if k not in ('id',)}
                return c, t
    return None, None


# ---------------------------------------------------------------- prompt
def prompt_sistem():
    bag = ['Kamu penulis soal latihan bergaya TOCFL Band A (華語文能力測驗) untuk aplikasi belajar mandiri. '
           'Soal mengikuti format resmi berdasarkan analisis 5 set mock test resmi. Kosakata DIKUNCI pada '
           'daftar kata yang sudah diajarkan (fidelitas level TBCL) — memakai kata di luar daftar adalah kesalahan.',
           '\n## Kode pola pengecoh', *[f'{k} = {v}' for k, v in POLA.items()],
           '\n## Aturan umum', ATURAN_UMUM, '\n## Spesifikasi per Part']
    for nama, s in PART.items():
        pola = ', '.join(f'{k} ±{v}%' for k, v in s['pola'].items())
        bag.append(f"### {nama}  (type: {s['type']})\n- part: \"{s['part']}\"\n- instr: \"{s['instr']}\"\n"
                   f"- Bentuk: {s['bentuk']}\n- Sebaran pola pengecoh di ujian asli: {pola}\n- Catatan: {s['catatan']}")
    bag.append('\n## Format keluaran\nKembalikan HANYA satu blok ```json berisi array soal. Tiap soal memakai kolom '
               'persis seperti contoh (type, part, instr, picture/lines/text/question, options, answer atau answers, why), '
               'ditambah "pola_pengecoh": {"<huruf pengecoh>": "<kode pola>"} (untuk cloze: {"lebih": "<kode>"}).')
    return '\n'.join(bag)


def prompt_user(ktx, parts):
    lv = ktx['level']
    bag = [f"# 單元 {ktx['code']} 「{ktx['judul']}」 · level {lv}",
           f"Situasi 單元: {ktx['scene']}", f"Can-do: {ktx['can_do']}",
           f"Kata baru 單元 ini (utamakan dipakai): {' '.join(ktx['target'])}",
           f"Grammar 單元 ini (utamakan dipakai): {'; '.join(ktx['target_g']) or '-'}",
           '\n## Kosakata yang BOLEH dipakai (semua kata yang sudah diajarkan sampai 單元 ini + nama diri)',
           ' '.join(sorted(ktx['ok'])),
           '\n## Grammar yang sudah diajarkan', '; '.join(ktx['grammar_lama']),
           '\n## Pola yang BELUM boleh dipakai di 單元 ini', ', '.join(ktx['terlarang']) or '-',
           '\n## Panjang teks untuk level ini (hanzi)']
    for p, rng in PANJANG.items():
        bag.append(f'- {p}: {rng[lv][0]}–{rng[lv][1]}')
    bag.append('\n## Contoh soal yang sudah disetujui (gaya & format — JANGAN disalin isinya)')
    for p in dict.fromkeys(parts):
        c, t = contoh(p, ktx)
        if t:
            bag.append(f'### {p} (dari {c})\n```json\n{json.dumps(t, ensure_ascii=False)}\n```')
    hitung = collections.Counter(parts)
    bag.append('\n## Tugas\nBuat soal BARU untuk 單元 ini, urut sesuai daftar: '
               + ', '.join(f'{p} ×{n}' for p, n in hitung.items())
               + f'. Total {len(parts)} soal. Topik dekat dengan situasi 單元, tetapi jangan menyalin dialog modul.')
    return '\n'.join(bag)


# ---------------------------------------------------------------- validasi
def hz(s):
    return len(CJK.findall(s or ''))


def periksa_satu(t, ktx, part):
    gagal, peringatan = [], []
    s = PART[part]
    if t.get('type') != s['type']:
        gagal.append(f"type harus {s['type']}")
    gagal += [x.split(': ', 1)[1] for x in cek_soal(ktx['code'], t)]
    opts = t.get('options', [])
    pic = all(isinstance(o, dict) for o in opts) and opts
    n_lines = len(t.get('lines', []))
    if part == '聽力 Part 2' and (n_lines != 2 or not pic or len(opts) != 3):
        gagal.append('聽力 Part 2: 2 baris dialog + 3 opsi gambar')
    if part == '聽力 Part 3' and (n_lines != 4 or not pic or len(opts) != 3):
        gagal.append('聽力 Part 3: 4 baris dialog + 3 opsi gambar')
    if part in ('聽力 Part 4', '閱讀 Part 5') and (pic or len(opts) != 4):
        gagal.append(f'{part}: 4 opsi teks')
    if part in ('聽力 Part 4', '聽力 Part 3') and n_lines == 4:
        sp = [l.get('sp') for l in t['lines']]
        if any(a == b for a, b in zip(sp, sp[1:])):
            peringatan.append('pembicara tidak bergantian')
    if part in ('閱讀 Part 1', '聽力 Part 2', '聽力 Part 3') and not pic:
        gagal.append('opsi harus gambar {icon, label}')
    if part == '閱讀 Part 4':
        n = len(t.get('answers', []))
        if ktx['level'] != 'A0' and n != 5:
            gagal.append(f'閱讀 Part 4: harus 5 titik, dapat {n}')
        if ktx['level'] == 'A0' and not 3 <= n <= 5:
            gagal.append(f'閱讀 Part 4 (A0): 3–5 titik, dapat {n}')
    # panjang
    lv = ktx['level']
    if part in PANJANG:
        lo, hi = PANJANG[part][lv]
        if part == '閱讀 Part 2':
            for j, o in enumerate(opts):
                if isinstance(o, str) and not lo <= hz(o) <= hi:
                    peringatan.append(f'opsi {HURUF[j]} {hz(o)} hanzi (target {lo}–{hi})')
        else:
            teks = t.get('text', '')
            if part == '閱讀 Part 4':
                for k, a in enumerate(t.get('answers', [])):
                    if 0 <= a < len(opts):
                        teks = teks.replace(f'（{k + 1}）', str(opts[a]))
            n = hz(teks)
            if not lo <= n <= hi:
                (gagal if n < lo * 0.7 or n > hi * 1.3 else peringatan).append(f'panjang teks {n} hanzi (target {lo}–{hi})')
    # kosakata level
    ok = ktx['ok']
    for st in cd.teks(t):
        bad = cd.cek(st, ok)
        if bad:
            gagal.append(f'huruf/kata belum diajarkan 「{"".join(dict.fromkeys(bad))}」 di: {st[:30]}')
        for w in ktx['resmi'] - ok:
            if w in st and not any(len(k) > len(w) and w in k and k in st for k in ok):
                gagal.append(f'kata TBCL 「{w}」 belum diajarkan di: {st[:30]}')
                break
    semua = ' '.join(cd.teks(t))
    if re.search(r'[男女]的', semua):
        gagal.append('memakai 男的/女的 — ganti 這位先生/這位小姐')
    for pola, mulai in POLA_GRAMMAR.items():
        mm = re.search(pola, semua)
        if mm and ktx['urut'].index(mulai) > ktx['i']:
            peringatan.append(f'pola 「{mm.group(0)}」 baru diajarkan di {mulai} (cek manual)')
    if part in ('聽力 Part 4', '閱讀 Part 5'):
        if not INFER.search(t.get('question', '')):
            peringatan.append('pertanyaan tampaknya faktual, bukan inferensial')
        a = t.get('answer', -1)
        src = re.sub(r'[。！？，、\s]', '', t.get('text', '') + ''.join(l.get('zh', '') for l in t.get('lines', [])))
        if 0 <= a < len(opts) and isinstance(opts[a], str):
            kunci = re.sub(r'[。！？，、\s]', '', opts[a])
            if len(kunci) >= 3 and kunci in src:
                peringatan.append('jawaban benar = kutipan persis dari teks (resmi: parafrase)')
    if part == '閱讀 Part 4':
        rata = sum(hz(o) for o in opts) / max(1, len(opts))
        if rata < 3:
            gagal.append(f'opsi 閱讀 Part 4 harus frasa 3–7 hanzi (rata {rata:.1f})')
    if not t.get('pola_pengecoh'):
        peringatan.append('pola_pengecoh kosong')
    return gagal, peringatan


def periksa(items, ktx, parts):
    hasil = []
    for j, t in enumerate(items):
        part = parts[j] if j < len(parts) else next((p for p in PART if t.get('part', '').startswith(p)), None)
        if part is None:
            hasil.append((['part tidak dikenal'], []))
            continue
        hasil.append(periksa_satu(t, ktx, part))
    if len(items) != len(parts):
        hasil.append(([f'jumlah soal {len(items)}, diminta {len(parts)}'], []))
    jaw = collections.Counter(t.get('answer') for t in items if 'answer' in t)
    if jaw and max(jaw.values()) > max(3, len(items) * 0.4):
        hasil.append(([], [f'posisi jawaban menumpuk: {dict(jaw)}']))
    empat = [t for t in items if len(t.get('options', [])) == 4 and 'answer' in t]
    if len(empat) >= 4 and not any(t['answer'] == 3 for t in empat):
        hasil.append(([], ['tidak ada jawaban D di soal 4 opsi']))
    return hasil


# ---------------------------------------------------------------- API
def ambil_json(teks):
    m = re.search(r'```json\s*(.*?)```', teks, re.S)
    raw = m.group(1) if m else teks[teks.find('['): teks.rfind(']') + 1]
    data = json.loads(raw)
    return data['items'] if isinstance(data, dict) and 'items' in data else data


def panggil(client, system, messages, log):
    import anthropic
    try:
        with client.beta.messages.stream(
            model=MODEL, max_tokens=32000,
            betas=['server-side-fallback-2026-07-01'], fallbacks='default',   # tolakan → model cadangan otomatis
            output_config={'effort': 'high'},
            system=[{'type': 'text', 'text': system, 'cache_control': {'type': 'ephemeral'}}],
            messages=messages,
        ) as stream:
            resp = stream.get_final_message()
    except anthropic.RateLimitError as e:
        sys.exit(f'Batas laju API tercapai, coba lagi nanti ({e.message}).')
    except anthropic.APIStatusError as e:
        sys.exit(f'Galat API {e.status_code}: {e.message}')
    except anthropic.APIConnectionError:
        sys.exit('Tidak bisa terhubung ke API (cek internet).')
    log['panggilan'].append(dict(request_id=resp._request_id, model=resp.model, stop=resp.stop_reason,
                                 usage=resp.usage.to_dict()))
    if resp.stop_reason == 'refusal':
        sys.exit('Permintaan ditolak oleh model (refusal) — lihat log.')
    if resp.stop_reason == 'max_tokens':
        sys.exit('Jawaban terpotong (max_tokens) — kurangi jumlah soal per panggilan.')
    teks = ''.join(b.text for b in resp.content if b.type == 'text')
    log['jawaban'].append(teks)
    return resp, teks


def buat(code, parts, putaran):
    try:
        import anthropic
    except ImportError:
        sys.exit('SDK belum terpasang: pip install anthropic   (atau pakai --tanpa-api)')
    modul = muat()
    ktx = konteks(code, modul)
    system, user = prompt_sistem(), prompt_user(ktx, parts)
    client = anthropic.Anthropic()
    log = dict(waktu=datetime.datetime.now().isoformat(timespec='seconds'), kode=code, model=MODEL,
               parts=parts, system=system, user=user, panggilan=[], jawaban=[], umpan_balik=[])
    messages = [{'role': 'user', 'content': user}]
    resp, teks = panggil(client, system, messages, log)
    items = ambil_json(teks)
    for r in range(putaran):
        hasil = periksa(items, ktx, parts)
        salah = [(j, g) for j, (g, _) in enumerate(hasil[:len(items)]) if g]
        if not salah and len(items) == len(parts):
            break
        umpan = 'Beberapa soal gagal validasi. Perbaiki HANYA soal ini dan kembalikan array JSON lengkap ' \
                f'({len(parts)} soal, urutan sama):\n' + '\n'.join(
                    f'- soal {j + 1} ({parts[j] if j < len(parts) else "?"}): ' + '; '.join(g) for j, g in salah)
        log['umpan_balik'].append(umpan)
        messages += [{'role': 'assistant', 'content': resp.content}, {'role': 'user', 'content': umpan}]
        resp, teks = panggil(client, system, messages, log)
        items = ambil_json(teks)
    simpan(code, items, ktx, parts, log)


# ---------------------------------------------------------------- keluaran
def simpan(code, items, ktx, parts, log=None):
    os.makedirs(f'{HERE}/hasil', exist_ok=True)
    hasil = periksa(items, ktx, parts)
    out, md = [], [f'# Tinjauan soal AI — {code} 「{ktx["judul"]}」 ({ktx["level"]})', '',
                   'Centang yang diterima, tulis perbaikan di bawahnya. Soal BELUM masuk bank soal.', '']
    for j, t in enumerate(items):
        g, w = hasil[j] if j < len(hasil) else ([], [])
        t = dict(t, sumber='ai', status='gagal' if g else ('tinjau' if w else 'lolos'))
        out.append(t)
        md.append(f"## {j + 1}. {t.get('part', '?')} — {t['status'].upper()}")
        if t.get('picture'):
            md.append(f"Gambar: {t['picture'].get('icon', '')} {t['picture'].get('label', '')}")
        for l in t.get('lines', []):
            md.append(f"- {l.get('sp')}：{l.get('zh')}")
        if t.get('text'):
            md.append(f"> {t['text']}")
        if t.get('question'):
            md.append(f"問：{t['question']}")
        for k, o in enumerate(t.get('options', [])):
            o = f"{o.get('icon', '')} {o.get('label', '')}" if isinstance(o, dict) else o
            benar = (k == t.get('answer')) or (k in t.get('answers', []))
            md.append(f"  {HURUF[k]}. {o}{'  ✔' if benar and 'answer' in t else ''}")
        if 'answers' in t:
            md.append(f"Jawaban: {[HURUF[a] for a in t['answers']]}")
        md.append(f"Pola pengecoh: {t.get('pola_pengecoh')}  ·  why: {t.get('why')}")
        md += [f'  ✗ {x}' for x in g] + [f'  ⚑ {x}' for x in w] + ['- [ ] diterima', '']
    for g, w in hasil[len(items):]:
        md += [f'✗ {x}' for x in g] + [f'⚑ {x}' for x in w]
    json.dump(dict(kode=code, dibuat=datetime.date.today().isoformat(), items=out),
              open(f'{HERE}/hasil/{code}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(f'{HERE}/hasil/{code}-tinjau.md', 'w', encoding='utf-8').write('\n'.join(md))
    if log:
        os.makedirs(f'{HERE}/log', exist_ok=True)
        stamp = log['waktu'].replace(':', '')
        json.dump(log, open(f'{HERE}/log/{stamp}_{code}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    st = collections.Counter(t['status'] for t in out)
    print(f'{code}: {len(out)} soal — lolos {st["lolos"]}, perlu tinjau {st["tinjau"]}, gagal {st["gagal"]}')
    print(f'  → {os.path.relpath(HERE)}/hasil/{code}-tinjau.md')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('kode')
    ap.add_argument('--part', action='append', help='mis. "聽力 Part 3" (boleh berulang); default = 10 butir Tes Bab')
    ap.add_argument('--n', type=int, default=1, help='jumlah soal per --part')
    ap.add_argument('--jenis', choices=['tes', 'latihan'], default='tes',
                    help='komposisi bawaan: tes = 10 butir Tes Bab; latihan = 12 butir soal latihan modul (format resmi)')
    ap.add_argument('--putaran', type=int, default=3, help='maks. putaran perbaikan otomatis')
    ap.add_argument('--tanpa-api', action='store_true', help='tulis prompt ke hasil/<kode>-prompt.md saja')
    ap.add_argument('--periksa', metavar='FILE', help='validasi soal JSON yang dibuat di luar skrip')
    a = ap.parse_args()
    for p in a.part or []:
        if p not in PART:
            sys.exit(f'Part tidak dikenal: {p}. Pilihan: {", ".join(PART)}')
    parts = [p for p in (a.part or []) for _ in range(a.n)] if a.part else \
        list(KOMPOSISI_LATIHAN if a.jenis == 'latihan' else KOMPOSISI)
    if a.periksa:
        modul = muat()
        ktx = konteks(a.kode, modul)
        data = json.load(open(a.periksa, encoding='utf-8'))
        items = data['items'] if isinstance(data, dict) else data
        parts = [next(p for p in PART if t.get('part', '').startswith(p)) for t in items]
        simpan(a.kode, items, ktx, parts)
    elif a.tanpa_api:
        ktx = konteks(a.kode, muat())
        os.makedirs(f'{HERE}/hasil', exist_ok=True)
        f = f'{HERE}/hasil/{a.kode}-prompt.md'
        open(f, 'w', encoding='utf-8').write('# SYSTEM\n\n' + prompt_sistem() + '\n\n# USER\n\n' + prompt_user(ktx, parts))
        print(f'Prompt ditulis: {os.path.relpath(f)}')
    else:
        buat(a.kode, parts, a.putaran)


if __name__ == '__main__':
    main()
