/* Bahasa antarmuka. Tampilan default = English–Mandarin untuk semua pengunjung.
   Versi Indonesia dibuka dengan kode rahasia (di sini hanya tersimpan hash-nya, jadi kode tidak
   terbaca dari sumber halaman):
     - komputer: ketik kodenya di mana saja (bukan di kotak isian)
     - HP: buka alamat app + #/<kode>, mis. …/index.html#/kodeku
   Kode yang sama mengembalikan ke English. Pilihan tersimpan per perangkat (localStorage tocfl_lang),
   tidak ada tombol bahasa yang terlihat. Ganti kode: py _kerja/kode_bahasa.py <kode baru>
   Data isi: English di data/en/ (dibuat _kerja/terjemah.py), Indonesia di data/. */

const LANG_KEY = 'tocfl_lang';
const LANG = (() => { try { return localStorage.getItem(LANG_KEY) === 'id' ? 'id' : 'en'; } catch { return 'en'; } })();
const T = (en, id) => (LANG === 'id' ? id : en);
document.documentElement.lang = LANG;

const Lang = {
  /* KODE */ HASH: 'gdkehcbmcc',
  DATA: LANG === 'id' ? 'data/' : 'data/en/',
  LOCALE: LANG === 'id' ? 'id-ID' : 'en-GB',
  is(s) { return cyrb53(`lang|${String(s).trim().toLowerCase()}`).toString(36) === this.HASH; },
  toggle() {
    try { localStorage.setItem(LANG_KEY, LANG === 'id' ? 'en' : 'id'); } catch { return; }
    history.replaceState(null, '', location.pathname + location.search + '#/');
    location.reload();
  },
  buf: '',
};

document.addEventListener('keydown', e => {
  if (e.ctrlKey || e.metaKey || e.altKey || e.key.length !== 1 || /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
  Lang.buf = (Lang.buf + e.key.toLowerCase()).slice(-40);
  for (let i = 0; i < Lang.buf.length - 3; i++) if (Lang.is(Lang.buf.slice(i))) { Lang.buf = ''; return Lang.toggle(); }
});
