"""Bangun repo TAMPILAN SISWA (versi terkunci) dari app utama.

Keputusan Carli 2026-11-26: isi = seluruh Vol.1–3 (A01–C67) apa adanya; bedanya hanya:
  - bab terkunci: bab berikutnya terbuka setelah Tes Bab bab sebelumnya ≥ 80%;
  - pendaftaran (kuesioner data diri) → penempatan: sudah punya level TOCFL → langsung diarahkan,
    belum → tes penempatan bertahap (paket A tes TOCFL Mini per level, lulus tahap ≥ 80%);
  - tes akhir (paket B) setelah satu volume selesai, lalu evaluasi modul;
  - data siswa tersimpan di perangkat (awalan tocflsiswa_) dan terkirim otomatis ke Google Sheet;
  - Bahasa Indonesia saja.

    py _kerja/buat_siswa.py         → sinkronkan seluruh repo siswa ke folder `out` di _kerja/siswa/config.json

Sumber (repo siswa TIDAK diedit tangan):
  data/rencana.json, data/modul_vol{1,2,3}.json, data/bank_soal.json   isi semua bab + Tes Bab (Indonesia)
  _kerja/mini/tes_A{0,1,2}.json                                     tes penempatan (paket A) & tes akhir (paket B)
  _kerja/siswa/web/                                                 index.html, js/siswa.js, css/siswa.css
  _kerja/siswa/config.json                                          {"out": folder repo siswa, "kirim_url": URL Apps Script}
  js/*.js, css/*.css, img/, audio/tts/                              app utama
Sesudah mengubah data di repo utama: jalankan ulang skrip ini, lalu commit & push di folder repo siswa.
"""
import fnmatch, hashlib, json, os, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
K = Path(__file__).resolve().parent; R = K.parent; S = K / 'siswa'
sys.path.insert(0, str(K))
from buat_mini import BAGIAN   # label bagian & petunjuk soal tes = sama dengan bank soal Tes Bab

CFG = json.loads((S / 'config.json').read_text(encoding='utf-8'))
OUT = (K / CFG['out']).resolve() if not os.path.isabs(CFG['out']) else Path(CFG['out'])
JS = ['media.js', 'lang.js', 'app.js', 'modul.js', 'latihan.js', 'ujian.js']
LEVEL = ['A0', 'A1', 'A2']


def baca(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def padat(d): return json.dumps(d, ensure_ascii=False, separators=(',', ':')).encode()


def data_tes():
    """Tes penempatan & tes akhir dari tes TOCFL Mini: {level: {A: [...], B: [...]}} dengan label bagian & gambar."""
    out = {}
    for lv in LEVEL:
        out[lv] = {}
        for paket, items in baca(K / 'mini' / f'tes_{lv}.json').items():
            hasil = []
            for t in items:
                t = {k: v for k, v in t.items() if k != 'tema'}
                t['part'], t['instr'] = BAGIAN[(t['type'], t['part'][:9])]
                if t.get('picture', {}).get('img') is None and (R / f'img/soal/T{lv}{paket}-{t["no"]}.svg').exists():
                    t.setdefault('picture', {})['img'] = f'T{lv}{paket}-{t["no"]}'
                t['options'] = [dict(o, img=f'T{lv}{paket}-{t["no"]}{"abc"[k]}')
                                if isinstance(o, dict) and (R / f'img/soal/T{lv}{paket}-{t["no"]}{"abc"[k]}.svg').exists() else o
                                for k, o in enumerate(t['options'])]
                hasil.append(t)
            out[lv][paket] = hasil
    return out


def salin_js(f):
    s = (R / 'js' / f).read_text(encoding='utf-8')
    s = s.replace("'tocfl_", "'tocflsiswa_")          # penyimpanan terpisah dari app utama & mini (satu origin github.io)
    if f == 'lang.js':                                # hanya Bahasa Indonesia: kode rahasia English dimatikan
        a = "is(s) { return cyrb53(`lang|${String(s).trim().toLowerCase()}`).toString(36) === this.HASH; },"
        assert a in s, 'lang.js berubah — sesuaikan buat_siswa.py'
        s = s.replace(a, 'is() { return false; },')
    return s


def font_kai(F):
    """全字庫正楷體 (TW-Kai) dipotong ke huruf yang dipakai repo siswa (cara sama dengan buat_mini.font_kai)."""
    pola = re.compile(r'[ˇˉ-ˋ˙⺀-鿿豈-﫿＀-￯\U00020000-\U0002FA1F]')
    huruf = set()
    for k, v in F.items():
        if k.endswith(('.json', '.js', '.html')) and isinstance(v, bytes):
            huruf |= set(pola.findall(v.decode('utf-8')))
    teks = ''.join(sorted(huruf))
    cache, kunci = S / 'font_cache' / 'twkai-siswa.woff2', S / 'font_cache' / 'twkai-siswa.txt'
    src = K / 'mini' / 'font_src'
    sumber = sorted(src.glob('TW-Kai-*.ttf')) if src.is_dir() else []
    tanda = hashlib.md5((teks + '|' + ','.join(f.name for f in sumber)).encode()).hexdigest()
    if sumber and not (cache.exists() and kunci.exists() and kunci.read_text(encoding='utf-8') == tanda):
        from fontTools import subset
        from fontTools.ttLib import TTFont
        cache.parent.mkdir(exist_ok=True)
        utama = [f for f in sumber if 'Ext' not in f.name and 'Plus' not in f.name][0]
        opt = subset.Options(); opt.flavor = 'woff2'; opt.layout_features = ['*']; opt.name_IDs = ['*']; opt.notdef_outline = True
        font = TTFont(utama)
        sub = subset.Subsetter(opt); sub.populate(text=teks); sub.subset(font)
        font.flavor = 'woff2'; font.save(cache); kunci.write_text(tanda, encoding='utf-8')
        print(f'  font TW-Kai: {len(teks)} huruf → {cache.stat().st_size // 1024} KB')
    elif not cache.exists():
        print('  ⚠ font TW-Kai belum ada (sumber di _kerja/mini/font_src/) — HP memakai font cadangan')
        return
    F['fonts/twkai-siswa.woff2'] = cache


def main():
    F = {}   # path relatif → bytes atau Path sumber
    for fn in ['rencana.json', 'modul_vol1.json', 'modul_vol2.json', 'modul_vol3.json', 'bank_soal.json']:
        F[f'data/{fn}'] = padat(baca(R / 'data' / fn))
    F['data/siswa.json'] = padat({'tes': data_tes()})
    web = S / 'web'
    for f in web.rglob('*'):
        if f.is_file():
            s = f.read_text(encoding='utf-8')
            if f.name == 'siswa.js':
                s = s.replace("const KIRIM_URL = '';", f"const KIRIM_URL = {json.dumps(CFG.get('kirim_url', ''))};")
            F[f.relative_to(web).as_posix()] = s.encode()
    for f in JS:
        F[f'js/{f}'] = salin_js(f).encode()
    for f in ('style.css', 'kai.css'):
        F[f'css/{f}'] = R / 'css' / f
    font_kai(F)
    # ?v=<hash isi> di index.html (GitHub Pages meng-cache JS/CSS ±10 menit) + DATA_V untuk pembaruan otomatis
    isi = lambda v: v.read_bytes() if isinstance(v, Path) else v
    data_v = hashlib.md5(b''.join(isi(F[k]) for k in sorted(F) if k.startswith('data/'))).hexdigest()[:8]
    html = F['index.html'].decode().replace("window.DATA_V = '';", f"window.DATA_V = '{data_v}';")
    html = re.sub(r'((?:src|href)="((?:js|css)/[^"?]+))"',
                  lambda m: f'{m[1]}?v={hashlib.md5(isi(F[m[2]])).hexdigest()[:8]}"' if m[2] in F else m[0], html)
    F['index.html'] = html.encode()
    for d in ('img', 'audio/tts'):
        for f in (R / d).rglob('*'):
            if f.is_file() and not f.name.startswith('.'):
                F[f.relative_to(R).as_posix()] = f
    F['.nojekyll'] = b''
    ABAIKAN = ['Rekap-*.xlsx', '~$*', 'desktop.ini']
    F['.gitignore'] = ('# Rekap hasil siswa (berisi email) — jangan di-commit\n' + '\n'.join(ABAIKAN) + '\n').encode()
    F['README.md'] = (
        '# TOCFL Band A — tampilan siswa\n\nVersi terkunci dari app modul TOCFL Band A (Vol.1–3, A01–C67): pendaftaran → penempatan '
        '(level TOCFL atau tes penempatan) → bab terbuka berurutan setelah Tes Bab ≥ 80% → tes akhir per volume → evaluasi. '
        'Data siswa terkirim ke Google Sheet peneliti.\n\n'
        '**Jangan edit repo ini langsung.** Semua file dibuat ulang oleh `py _kerja/buat_siswa.py` di repo utama (`cphaniatatn-coder/TOCFL`).\n\n'
        'Ilustrasi: Twemoji © Twitter/X & kontributor (CC-BY 4.0); gambar soal hitam-putih: OpenMoji (CC BY-SA 4.0); '
        'huruf kai: 全字庫正楷體 (TW-Kai), 國家發展委員會, 政府資料開放授權條款 第1版.\n').encode()

    # SINKRONKAN: hanya file yang berubah yang ditulis; file yang tidak dipakai lagi dihapus
    tulis_n = hapus_n = 0
    for rel, src in F.items():
        dst = OUT / rel
        data = src if isinstance(src, bytes) else None
        if data is None:
            if dst.exists() and dst.stat().st_size == src.stat().st_size and dst.read_bytes() == src.read_bytes():
                continue
            data = src.read_bytes()
        elif dst.exists() and dst.read_bytes() == data:
            continue
        dst.parent.mkdir(parents=True, exist_ok=True); dst.write_bytes(data); tulis_n += 1
    if OUT.exists():
        for f in sorted(OUT.rglob('*'), reverse=True):
            rel = f.relative_to(OUT).as_posix()
            if rel == '.git' or rel.startswith('.git/') or any(fnmatch.fnmatch(f.name, p) for p in ABAIKAN):
                continue
            if f.is_file() and rel not in F:
                f.unlink(); hapus_n += 1
            elif f.is_dir() and not any(f.iterdir()):
                f.rmdir()
    print(f'repo siswa: {OUT} · {tulis_n} file ditulis, {hapus_n} dihapus · data {data_v}'
          + ('' if CFG.get('kirim_url') else ' · ⚠ kirim_url kosong (data belum terkirim ke Google Sheet)'))


if __name__ == '__main__':
    main()
