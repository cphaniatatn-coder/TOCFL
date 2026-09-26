"""Edit konten app lewat Excel.

    py _kerja/konten_excel.py ekspor   → buat _kerja/edit-konten.xlsx dari data sumber
    py _kerja/konten_excel.py impor    → tulis perubahan Excel kembali ke data sumber,
                                          lalu periksa, rakit app, perbarui ledger & audio

Sumber data yang sebenarnya tetap file teks di _kerja/ (isi/, soal/, bank/, arti.json,
kata_tambahan.json, plan_L*.txt). Excel hanya "jendela edit": file sumber yang tidak
berubah tidak ditulis ulang sama sekali.
"""
import json, os, re, subprocess, sys
import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

K = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(K)
XLSX = f'{K}/edit-konten.xlsx'
HURUF = 'ABCDEFGH'

# ---------- baca sumber ----------
def muat_json(p): return json.load(open(p, encoding='utf-8'))

def tulis_json(p, obj, lama):
    """Tulis hanya bila isinya berubah; kembalikan True bila ditulis."""
    if obj == lama:
        return False
    json.dump(obj, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(p, 'a', encoding='utf-8').write('\n')
    return True

def urutan_kode():
    out = []
    for lv in (1, 2, 3):
        for l in open(f'{K}/plan_L{lv}.txt', encoding='utf-8'):
            if l.strip() and not l.startswith('#'):
                out.append(l.split('|')[0])
    return out

def isi_files():
    """{file: (obj, [modul...], tunggal?)} — file tunggal (A01.json) tidak menyimpan 'code'."""
    out = {}
    for fn in sorted(os.listdir(f'{K}/isi')):
        if fn.endswith('.json'):
            d = muat_json(f'{K}/isi/{fn}')
            if 'modules' in d:
                out[fn] = (d, d['modules'], False)
            else:
                out[fn] = (d, [dict(d, code=fn[:-5])], True)
    return out

def soal_files(folder):
    return {fn: muat_json(f'{K}/{folder}/{fn}') for fn in sorted(os.listdir(f'{K}/{folder}')) if fn.endswith('.json')}

def plan_lines():
    out = {}
    for lv in (1, 2, 3):
        for l in open(f'{K}/plan_L{lv}.txt', encoding='utf-8'):
            if l.strip() and not l.startswith('#'):
                f = l.rstrip('\n').split('|')
                while len(f) < 7: f.append('')
                out[f[0]] = (lv, f)
    return out

# ---------- format sel ----------
def opsi_ke_teks(o): return f"{o['icon']} | {o['label']}" if isinstance(o, dict) else o
def teks_ke_opsi(s, gambar):
    if gambar:
        ic, _, lab = s.partition('|')
        return {'icon': ic.strip(), 'label': lab.strip()}
    return s
def baris_ke_teks(lines): return '\n'.join(f"{l['sp']}：{l['zh']}" for l in lines)
def teks_ke_baris(s):
    out = []
    for l in s.split('\n'):
        if l.strip():
            sp, _, zh = l.partition('：')
            if not zh: raise ValueError(f'baris dialog harus "pembicara：kalimat" — dapat: {l}')
            out.append({'sp': sp.strip(), 'zh': zh.strip()})
    return out
def sel(v): return '' if v is None else str(v).strip()
def daftar(s): return [x.strip() for x in sel(s).split('\n') if x.strip()]

KOL_SOAL = ['tipe', 'bagian', 'petunjuk', 'audio', 'teks', 'pertanyaan', 'dialog (pembicara：kalimat)',
            'gambar (ikon | keterangan)', 'pilihan (satu per baris)', 'jawaban (A/B/…; cloze: B, A, C)', 'alasan']

def soal_ke_baris(t):
    pic = t.get('options') and isinstance(t['options'][0], dict)
    jaw = ', '.join(HURUF[i] for i in t['answers']) if t['type'] == 'cloze' else HURUF[t['answer']]
    return [t['type'], t['part'], t['instr'], t.get('audio', ''), t.get('text', ''), t.get('question', ''),
            baris_ke_teks(t.get('lines', [])), opsi_ke_teks(t['picture']) if t.get('picture') else '',
            '\n'.join(opsi_ke_teks(o) for o in t['options']), jaw, t['why']]

def baris_ke_soal(v, lama=None):
    tipe, part, instr, audio, teks, tanya, dlg, gbr, pil, jaw, why = [sel(x) for x in v]
    t = {'type': tipe, 'part': part, 'instr': instr}
    if audio: t['audio'] = audio
    if dlg: t['lines'] = teks_ke_baris(dlg)
    if tanya: t['question'] = tanya
    if gbr: t['picture'] = teks_ke_opsi(gbr, True)
    if teks: t['text'] = teks
    gambar = tipe in ('listen_pick', 'read_sent') or (tipe == 'listen_dialog' and '|' in pil.split('\n')[0])
    t['options'] = [teks_ke_opsi(o, gambar) for o in daftar(pil)]
    huruf = [x.strip().upper() for x in jaw.replace('，', ',').split(',') if x.strip()]
    if any(h not in HURUF for h in huruf): raise ValueError(f'jawaban harus huruf A–H, dapat "{jaw}"')
    if tipe == 'cloze':
        t['answers'] = [HURUF.index(h) for h in huruf]
    else:
        if len(huruf) != 1: raise ValueError(f'jawaban harus satu huruf, dapat "{jaw}"')
        t['answer'] = HURUF.index(huruf[0])
    for i in t.get('answers', [t.get('answer')]):
        if not (0 <= i < len(t['options'])):
            raise ValueError(f'jawaban "{HURUF[i]}" tidak ada di pilihan (hanya {len(t["options"])} pilihan)')
    t['why'] = why
    # pertahankan kolom lain yang tidak ada di Excel (bila ada) & urutan kolom asli (supaya riwayat perubahan rapi)
    if lama:
        for k, x in lama.items():
            if k not in t and k not in ('audio', 'lines', 'question', 'picture', 'text', 'answer', 'answers'):
                t[k] = x
        t = {**{k: t[k] for k in lama if k in t}, **{k: v for k, v in t.items() if k not in lama}}
    return t

# ---------- EKSPOR ----------
def ekspor():
    kode_urut = urutan_kode()
    isi = isi_files(); plan = plan_lines()
    mod = {m['code']: (fn, m) for fn, (_, ms, _) in isi.items() for m in ms}
    tb = {o['w']: o['lv'] for o in muat_json(f'{K}/tbcl.json')}
    wb = openpyxl.Workbook()
    sheets = {}
    def sheet(nama, kolom, lebar):
        ws = wb.create_sheet(nama); ws.append(kolom)
        for i, w in enumerate(lebar, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = 'B2' if nama != 'Petunjuk' else None
        sheets[nama] = ws
        return ws

    wb.remove(wb.active)
    ws = sheet('Petunjuk', ['Cara memakai file ini'], [120])
    for l in PETUNJUK.strip('\n').split('\n'):
        ws.append([l])

    ws = sheet('Modul', ['kode', 'judul (中文)', 'pinyin judul', 'arti judul', 'ringkasan (daftar modul)', 'adegan', 'tujuan (satu per baris)', 'kaitan ujian'],
               [7, 26, 30, 30, 40, 50, 55, 55])
    for c in kode_urut:
        fn, m = mod[c]; f = plan[c][1]
        ws.append([c, m.get('title', f[1]), m['title_py'], m['title_id'], f[2], m['scene'], '\n'.join(m['can_do']), m['exam_link']])

    ws = sheet('Dialog', ['kode', 'dialog ke-', 'tempat', 'judul dialog', 'baris ke-', 'pembicara', '中文', 'pinyin', 'terjemahan'],
               [7, 9, 18, 26, 9, 12, 45, 50, 50])
    for c in kode_urut:
        for di, d in enumerate(mod[c][1]['dialogs'], 1):
            for li, l in enumerate(d['lines'], 1):
                ws.append([c, di, d['place'], d['title_id'], li, l['sp'], l['zh'], l['py'], l['id']])

    ws = sheet('Grammar', ['kode', 'no', 'TBCL #', 'poin', 'pola', 'balok (kata=peran | …)', 'penjelasan', 'cek: pertanyaan', 'cek: pilihan (satu per baris)', 'cek: jawaban'],
               [7, 5, 8, 28, 26, 36, 60, 28, 30, 10])
    for c in kode_urut:
        for gi, g in enumerate(mod[c][1]['grammar'], 1):
            ws.append([c, gi, g['tbcl_id'], g['point'], g['pattern'], ' | '.join(f'{w}={r}' for w, r in g['blocks']), g['explain'],
                       g['check']['q'], '\n'.join(g['check']['options']), HURUF[g['check']['answer']]])

    ws = sheet('Contoh grammar', ['kode', 'grammar no', 'contoh ke-', '中文', 'terjemahan'], [7, 11, 10, 45, 55])
    for c in kode_urut:
        for gi, g in enumerate(mod[c][1]['grammar'], 1):
            for ei, e in enumerate(g['examples'], 1):
                ws.append([c, gi, ei, e['zh'], e['id']])

    soal = soal_files('soal')
    kode_soal = {c: fn for fn, d in soal.items() for c in d}
    ws = sheet('Soal latihan', ['kode', 'sumber', 'no'] + KOL_SOAL, [7, 10, 5, 13, 30, 30, 30, 36, 20, 36, 30, 36, 14, 50])
    for c in kode_urut:
        for i, t in enumerate(mod[c][1]['tasks'], 1):
            ws.append([c, 'inti', i] + soal_ke_baris(t))
        for i, t in enumerate(soal.get(kode_soal.get(c), {}).get(c, []), 1):
            ws.append([c, 'tambahan', i] + soal_ke_baris(t))

    bank = soal_files('bank')
    kode_bank = {c: fn for fn, d in bank.items() for c in d}
    ws = sheet('Bank soal', ['kode', 'no'] + KOL_SOAL, [7, 5, 13, 30, 30, 30, 36, 20, 36, 30, 36, 14, 50])
    for c in kode_urut:
        for i, t in enumerate(bank.get(kode_bank.get(c), {}).get(c, []), 1):
            ws.append([c, i] + soal_ke_baris(t))

    arti = muat_json(f'{K}/arti.json'); tamb = muat_json(f'{K}/kata_tambahan.json')
    ws = sheet('Arti kosakata', ['kata (entri)', 'level', 'sumber', 'jenis kata', 'arti (bahasa Indonesia)'], [26, 7, 12, 11, 60])
    for w, a in arti.items():
        ws.append([w, tb.get(w, ''), 'TBCL', a.get('pos', ''), a.get('meaning', '')])
    for w, a in tamb.items():
        if not w.startswith('_'):
            ws.append([w, a['lv'], 'tambahan', a['pos'], a['meaning']])

    ws = sheet('Arti khusus modul', ['kode', 'kata', 'arti', 'jenis kata', 'catatan'], [7, 12, 45, 11, 50])
    for c in kode_urut:
        for w, o in mod[c][1].get('vocab_override', {}).items():
            ws.append([c, w, o.get('meaning', ''), o.get('pos', ''), o.get('note', '')])

    ws = sheet('Kosakata per modul', ['kode', 'kategori (1–17)', 'grammar (TBCL #)', '核心 (pisah spasi)', '補充 (pisah spasi)'], [7, 12, 14, 60, 60])
    for c in kode_urut:
        f = plan[c][1]
        ws.append([c, f[3], f[4], f[5], f[6]])

    ws = sheet('Daur ulang', ['kode', 'no', '中文', 'terjemahan'], [7, 5, 45, 55])
    for c in kode_urut:
        for i, r in enumerate(mod[c][1].get('recycle', []), 1):
            ws.append([c, i, r['zh'], r['id']])

    kepala = PatternFill('solid', fgColor='DCE6F1')
    for ws in wb.worksheets:
        for cell in ws[1]:
            cell.font = Font(bold=True); cell.fill = kepala
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical='top')
        if ws.title != 'Petunjuk':
            ws.auto_filter.ref = ws.dimensions
    try:
        wb.save(XLSX)
    except PermissionError:
        sys.exit(f'Tidak bisa menyimpan {XLSX} — tutup dulu file itu di Excel, lalu jalankan ulang.')
    print(f'Selesai: {XLSX}')
    for ws in wb.worksheets[1:]:
        print(f'  {ws.title}: {ws.max_row - 1} baris')

# ---------- IMPOR ----------
def baris_sheet(wb, nama):
    ws = wb[nama]
    rows = list(ws.iter_rows(min_row=2, values_only=True))
    return [r for r in rows if r and any(x not in (None, '') for x in r)]

def impor():
    if not os.path.exists(XLSX):
        sys.exit('Belum ada edit-konten.xlsx — jalankan dulu: py _kerja/konten_excel.py ekspor')
    wb = openpyxl.load_workbook(XLSX, read_only=True)
    kode_urut = urutan_kode(); kset = set(kode_urut)
    salah = []
    def cek_kode(c, sh, n):
        if c not in kset: salah.append(f'{sh} baris {n}: kode "{c}" tidak dikenal')
        return c in kset
    def num(x, sh, n, nama):
        try:
            v = float(sel(x)); return int(v) if v.is_integer() else v
        except ValueError:
            salah.append(f'{sh} baris {n}: kolom "{nama}" harus angka'); return 0

    # --- kumpulkan per modul dari setiap sheet ---
    M, DL, GR, EX, TI, TT, BK, OV, RC, PL = ({} for _ in range(10))
    for n, r in enumerate(baris_sheet(wb, 'Modul'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Modul', n): M[c] = r
    for n, r in enumerate(baris_sheet(wb, 'Dialog'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Dialog', n):
            DL.setdefault(c, []).append((num(r[1], 'Dialog', n, 'dialog ke-'), num(r[4], 'Dialog', n, 'baris ke-'), r))
    for n, r in enumerate(baris_sheet(wb, 'Grammar'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Grammar', n): GR.setdefault(c, []).append((num(r[1], 'Grammar', n, 'no'), n, r))
    for n, r in enumerate(baris_sheet(wb, 'Contoh grammar'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Contoh grammar', n):
            EX.setdefault((c, num(r[1], 'Contoh grammar', n, 'grammar no')), []).append((num(r[2], 'Contoh grammar', n, 'contoh ke-'), r))
    for n, r in enumerate(baris_sheet(wb, 'Soal latihan'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Soal latihan', n):
            tujuan = TI if sel(r[1]) == 'inti' else TT if sel(r[1]) == 'tambahan' else None
            if tujuan is None: salah.append(f'Soal latihan baris {n}: sumber harus "inti" atau "tambahan"'); continue
            tujuan.setdefault(c, []).append((num(r[2], 'Soal latihan', n, 'no'), n, r[3:]))
    for n, r in enumerate(baris_sheet(wb, 'Bank soal'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Bank soal', n): BK.setdefault(c, []).append((num(r[1], 'Bank soal', n, 'no'), n, r[2:]))
    for n, r in enumerate(baris_sheet(wb, 'Arti khusus modul'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Arti khusus modul', n): OV.setdefault(c, []).append(r)
    for n, r in enumerate(baris_sheet(wb, 'Daur ulang'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Daur ulang', n): RC.setdefault(c, []).append((num(r[1], 'Daur ulang', n, 'no'), r))
    for n, r in enumerate(baris_sheet(wb, 'Kosakata per modul'), 2):
        c = sel(r[0])
        if cek_kode(c, 'Kosakata per modul', n): PL[c] = r

    def soal_list(rows, sh, lama_list):
        out = []
        for i, (no, n, v) in enumerate(sorted(rows, key=lambda x: x[0])):
            try:
                out.append(baris_ke_soal(v, lama_list[i] if i < len(lama_list) else None))
            except (ValueError, IndexError) as e:
                salah.append(f'{sh} baris {n}: {e}')
        return out

    # --- modul (isi/*.json) ---
    isi = isi_files(); plan = plan_lines(); ditulis = []
    for fn, (obj, mods, tunggal) in isi.items():
        baru_mods = []
        for m in mods:
            c = m['code']; b = json.loads(json.dumps(m))
            if c in M:
                r = M[c]
                if 'title' in m: b['title'] = sel(r[1])
                b['title_py'], b['title_id'], b['scene'] = sel(r[2]), sel(r[3]), sel(r[5])
                b['can_do'], b['exam_link'] = daftar(r[6]), sel(r[7])
            if c in DL:
                dmap = {}
                for di, li, r in sorted(DL[c], key=lambda x: (x[0], x[1])):
                    d = dmap.setdefault(di, {'place': sel(r[2]), 'title_id': sel(r[3]), 'lines': []})
                    d['lines'].append({'sp': sel(r[5]), 'zh': sel(r[6]), 'py': sel(r[7]), 'id': sel(r[8])})
                b['dialogs'] = [dmap[k] for k in sorted(dmap)]
            else:
                b['dialogs'] = []
            b['tasks'] = soal_list(TI.get(c, []), 'Soal latihan', m.get('tasks', []))
            gl = []
            for no, n, r in sorted(GR.get(c, []), key=lambda x: x[0]):
                try:
                    blok = [[w.strip(), rr.strip()] for w, _, rr in (x.partition('=') for x in sel(r[5]).split('|')) if w.strip()]
                    gl.append({'tbcl_id': num(r[2], 'Grammar', n, 'TBCL #'), 'point': sel(r[3]), 'pattern': sel(r[4]), 'blocks': blok,
                               'explain': sel(r[6]),
                               'examples': [{'zh': sel(e[3]), 'id': sel(e[4])} for _, e in sorted(EX.get((c, no), []), key=lambda x: x[0])],
                               'check': {'q': sel(r[7]), 'options': daftar(r[8]), 'answer': HURUF.index(sel(r[9]).upper())}})
                except (ValueError, IndexError) as e:
                    salah.append(f'Grammar baris {n}: {e}')
            b['grammar'] = gl
            ov = {}
            for r in OV.get(c, []):
                o = {k: sel(v) for k, v in (('meaning', r[2]), ('pos', r[3]), ('note', r[4])) if sel(v)}
                if o: ov[sel(r[1])] = o
            if ov or 'vocab_override' in m: b['vocab_override'] = ov
            if RC.get(c) or 'recycle' in m:
                b['recycle'] = [{'zh': sel(r[2]), 'id': sel(r[3])} for _, r in sorted(RC.get(c, []), key=lambda x: x[0])]
            baru_mods.append(b)
        if tunggal:
            baru = {k: v for k, v in baru_mods[0].items() if k != 'code'}
        else:
            baru = dict(obj, modules=baru_mods)
        if not salah and tulis_json(f'{K}/isi/{fn}', baru, obj): ditulis.append(f'isi/{fn}')

    # --- soal tambahan & bank soal ---
    for folder, SRC, sh in (('soal', TT, 'Soal latihan'), ('bank', BK, 'Bank soal')):
        files = soal_files(folder)
        milik = {c: fn for fn, d in files.items() for c in d}
        for c in SRC:
            if c not in milik: salah.append(f'{sh}: modul {c} belum punya file di _kerja/{folder}/ (tambahkan dulu lewat Claude)')
        for fn, d in files.items():
            baru = {c: soal_list(SRC.get(c, []), sh, d[c]) for c in d}
            if not salah and tulis_json(f'{K}/{folder}/{fn}', baru, d): ditulis.append(f'{folder}/{fn}')

    # --- arti kosakata ---
    arti = muat_json(f'{K}/arti.json'); tamb = muat_json(f'{K}/kata_tambahan.json')
    a2, t2 = json.loads(json.dumps(arti)), json.loads(json.dumps(tamb))
    for n, r in enumerate(baris_sheet(wb, 'Arti kosakata'), 2):
        w, src = sel(r[0]), sel(r[2])
        tgt = t2 if src == 'tambahan' else a2
        if w not in tgt:
            salah.append(f'Arti kosakata baris {n}: kata "{w}" tidak ada (menambah kata baru dilakukan lewat daftar resmi)'); continue
        tgt[w]['pos'], tgt[w]['meaning'] = sel(r[3]), sel(r[4])
    if not salah:
        if tulis_json(f'{K}/arti.json', a2, arti): ditulis.append('arti.json')
        if tulis_json(f'{K}/kata_tambahan.json', t2, tamb): ditulis.append('kata_tambahan.json')

    # --- rencana (judul, ringkasan, kategori, grammar, kosakata per modul) ---
    judul_di_isi = {m['code'] for _, (_, ms, _) in isi.items() for m in ms if 'title' in m}
    for lv in (1, 2, 3):
        p = f'{K}/plan_L{lv}.txt'; lama = open(p, encoding='utf-8').read(); out = []
        for l in lama.splitlines():
            if l.strip() and not l.startswith('#'):
                f = l.split('|'); c = f[0]; n_asli = len(f)
                while len(f) < 7: f.append('')
                if c in M and c not in judul_di_isi: f[1] = sel(M[c][1])
                if c in M: f[2] = sel(M[c][4])
                if c in PL: f[3], f[4], f[5], f[6] = (sel(x) for x in PL[c][1:5])
                l = '|'.join(f[:max(n_asli, 7 if f[6] else 6)])
            out.append(l)
        baru = '\n'.join(out) + ('\n' if lama.endswith('\n') else '')
        if not salah and baru != lama:
            open(p, 'w', encoding='utf-8').write(baru); ditulis.append(f'plan_L{lv}.txt')

    if salah:
        print('✗ Ada kesalahan di Excel — TIDAK ada file yang diubah. Perbaiki dulu:')
        for s in salah[:40]: print('  -', s)
        sys.exit(1)
    if not ditulis:
        print('Tidak ada perubahan di Excel.'); return
    print('File sumber yang diperbarui:', ', '.join(ditulis))

    # --- periksa & rakit ---
    py = sys.executable
    def jalan(cmd, judul):
        r = subprocess.run([py] + cmd, cwd=R, capture_output=True, text=True, encoding='utf-8', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        teks = (r.stdout + r.stderr).strip().splitlines()
        penting = [l for l in teks if not l.endswith(': OK')]
        print(f'\n== {judul} ==')
        print('\n'.join(penting[-40:]) if penting else 'OK')
        return r.returncode == 0
    ok = True
    if any(x.startswith('plan_') for x in ditulis):
        for lv in (1, 2, 3):
            ok &= jalan([f'{K}/val.py', K, str(lv)], f'Validasi kosakata Level {lv}')
    ok &= jalan([f'{K}/bangun_modul.py'], 'Rakit modul + periksa kosakata')
    ok &= jalan([f'{K}/bangun_bank.py'], 'Rakit bank soal + periksa format')
    jalan([f'{K}/buat_rencana_json.py'], 'Peta modul')
    jalan([f'{K}/buat_ledger.py'], 'Ledger')
    if ok:
        jalan([f'{K}/buat_audio.py'], 'Audio (kalimat baru direkam; butuh internet)')
        print('\n✓ Selesai. Buka app untuk melihat hasilnya, lalu commit & push.')
    else:
        print('\n✗ Ada masalah di atas. Perbaiki di Excel lalu jalankan impor lagi (audio belum dibuat).')


PETUNJUK = """
EDIT KONTEN APP TOCFL LEWAT EXCEL

1. Buat file ini (selalu dari data terbaru):   py _kerja/konten_excel.py ekspor
2. Edit di Excel, SIMPAN, lalu TUTUP file-nya.
3. Masukkan perubahan ke app:                  py _kerja/konten_excel.py impor
   Perintah ini memeriksa isi, merakit app, memperbarui ledger, dan merekam audio untuk kalimat baru.
   Kalau ada kesalahan, tidak ada file yang diubah — pesan akan menunjukkan sheet & baris yang salah.

ATURAN PENTING
- Jangan ubah kolom "kode". Urutan baris boleh diubah; urutan dipakai dari kolom nomor (dialog ke-, baris ke-, no).
- Menambah baris dialog: sisipkan baris dengan kode & "dialog ke-" yang sama, isi "baris ke-" (mis. 2.5 untuk di antara 2 dan 3 juga boleh).
- Menghapus kalimat/soal: hapus barisnya.
- Kalau mengubah 中文, ubah juga pinyin & terjemahannya (pinyin tidak dibuat otomatis).
- Dialog & soal hanya boleh memakai kata yang SUDAH diajarkan sampai modul itu. Pemeriksa akan menyebut kata yang belum diajarkan.
- Tokoh baru di dialog: tambahkan namanya ke SPEAKERS di js/media.js supaya suaranya benar (perempuan F1/F2, laki-laki M1/M2, anak K).
- Sel berisi beberapa baris (tujuan, pilihan, dialog soal): tekan Alt+Enter untuk baris baru di dalam sel.

FORMAT KHUSUS
- Soal, kolom "dialog": satu baris per kalimat, format  男：你好！  (titik dua lebar ：).
- Soal, kolom "pilihan": satu pilihan per baris. Pilihan bergambar ditulis  🌅 | pagi hari  (ikon | keterangan).
- Soal, kolom "jawaban": huruf pilihan yang benar (A, B, C, D). Untuk cloze: huruf per titik kosong, urut, mis.  B, A, C.
- Grammar, kolom "balok": kata=peran dipisah " | ", mis.  我=S | 是=是 | 李美美=N
- Kosakata per modul: kata dipisah spasi; kata@義項 = makna kedua (lihat CLAUDE.md). Mengubah ini ikut memeriksa cakupan 100%.
- Arti kosakata: kolom "kata (entri)" jangan diubah; ubah jenis kata & arti saja.
"""

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'ekspor': ekspor()
    elif cmd == 'impor': impor()
    else: print(__doc__)
