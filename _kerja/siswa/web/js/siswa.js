/* TAMPILAN SISWA (versi terkunci) — keputusan Carli 2026-11-26.
   Alur: data diri (kuesioner) → penempatan (level TOCFL yang sudah dimiliki, atau tes penempatan bertahap)
   → bab terbuka berurutan: bab berikutnya terbuka setelah Tes Bab ≥ 80% → tes akhir per volume → evaluasi modul.
   Isi bab, soal & audio = app utama apa adanya. Dimuat SETELAH app.js/modul.js/latihan.js/ujian.js dan hanya
   membungkus beberapa fungsinya (beranda, rute, daftar bab, akhir Tes Bab). Data dikirim otomatis ke Google Sheet.
   Sumber: _kerja/siswa/web/ di repo utama; disalin ke repo siswa oleh _kerja/buat_siswa.py. */

const SISWA_KEY = 'tocflsiswa_siswa';
const KIRIM_URL = '';   // ← diisi lewat _kerja/siswa/config.json (kirim_url) saat buat_siswa.py dijalankan
const LULUS = 80;       // nilai minimal Tes Bab untuk membuka bab berikutnya (dan untuk lulus tahap tes penempatan)
const LEVELS = ['A0', 'A1', 'A2'];
const VOL_LEVEL = { 1: 'A0', 2: 'A1', 3: 'A2' };

const Siswa = {
  data: null,
  get() { return Store.get(SISWA_KEY, {}); },
  set(patch) { const s = Object.assign(this.get(), patch); Store.set(SISWA_KEY, s); return s; },
  async load() {
    if (!this.data) this.data = await (await fetch('data/siswa.json')).json();
    return this.data;
  },
  uid() {
    const s = this.get();
    if (s.uid) return s.uid;
    const uid = (crypto.randomUUID ? crypto.randomUUID() : Date.now().toString(36) + Math.random().toString(36).slice(2)).replace(/-/g, '').slice(0, 10);
    this.set({ uid });
    return uid;
  },
  admin() { const s = this.get(); return !!s.admin; },

  /* ===== Urutan bab & kunci ===== */
  urut() { return [1, 2, 3].flatMap(v => App.plan[v].map(m => m.code)); },
  mulai() { return this.get().tempat?.mulai || null; },          // 'A01' | 'B01' | 'C01' | '*' (semua terbuka)
  lulus(code) { return (App.getP(code).tes?.best ?? -1) >= LULUS; },
  terbuka(code) {
    if (this.admin()) return true;
    const m = this.mulai();
    if (!m) return false;
    if (m === '*') return true;
    const U = this.urut(), i = U.indexOf(code), i0 = U.indexOf(m);
    if (i < 0) return false;
    return i <= i0 || this.lulus(U[i - 1]);
  },
  // bab yang sedang dikerjakan = bab terbuka pertama (mulai dari titik mulai) yang belum lulus
  kini() {
    const U = this.urut(), m = this.mulai();
    if (!m) return null;
    const i0 = m === '*' ? 0 : U.indexOf(m);
    return U.slice(i0).find(c => this.terbuka(c) && !this.lulus(c)) || null;
  },
  berikut(code) { const U = this.urut(), i = U.indexOf(code); return i >= 0 && i + 1 < U.length ? U[i + 1] : null; },
  volBab(v) { return App.plan[v].map(m => m.code); },
  // bab volume v yang wajib lulus agar tes akhir volume itu terbuka (bab di bawah titik mulai = tidak wajib)
  babWajib(v) {
    const U = this.urut(), m = this.mulai(), i0 = !m || m === '*' ? 0 : U.indexOf(m);
    return this.volBab(v).filter(c => U.indexOf(c) >= i0);
  },
  volSelesai(v) { const w = this.babWajib(v); return w.length > 0 && w.every(c => this.lulus(c)); },
  nLulus() { return this.urut().filter(c => this.lulus(c)).length; },

  /* ===== Langkah besar: 0 data diri · 1 penempatan · 2 belajar ===== */
  langkah() {
    const s = this.get();
    if (!s.profil) return 0;
    if (!this.mulai()) return 1;
    return 2;
  },

  /* ===== Beranda ===== */
  async renderHome() {
    await this.load();
    const s = this.get(), L = this.langkah(), adm = this.admin();
    App.bar('TOCFL Band A', null);
    const kartu = (st, ic, judul, sub, href) => `<button class="card mode-card step-card st-${st}" ${st === 'lock' ? 'disabled' : `onclick="App.go('${href}')"`}>
        ${Pic.html(st === 'done' ? '✅' : st === 'lock' ? '🔒' : ic, 'mode-ic')}
        <div><b>${judul}</b><span>${sub}</span></div>${st === 'lock' ? '' : '<span class="chev">›</span>'}</button>`;
    const nL = this.nLulus(), total = this.urut().length;
    let isi = '';
    if (L === 0) {
      isi = `<button class="card mode-card" onclick="Siswa.bukaPetunjuk()">${Pic.html('❓', 'mode-ic')}
          <div><b>Baca petunjuk dulu</b><span>1 menit · cara kerja modul dan aturan tes</span></div><span class="chev">›</span></button>
        <div class="mode-list">${kartu('cur', '🪪', '1 · Data diri', '± 3 menit', '#/siswa/profil')}</div>`;
    } else if (L === 1) {
      isi = `<div class="mode-list">${kartu('done', '🪪', '1 · Data diri', esc(s.profil.nama), '#/')}</div>
        <h2 class="section-title">2 · Tes penempatan</h2>${this.penempatanHTML()}`;
    } else {
      const k = this.kini(), f = k && App.plan[App.volOf(k)].find(m => m.code === k);
      isi = `${f ? `<button class="card continue" onclick="App.go('#/m/${k}/${App.getP(k).stage || 0}')">
          ${Pic.scene(f.categories[0], 'sm')}
          <div class="continue-txt"><small>Lanjutkan belajar</small><b lang="zh-TW">${esc(f.title)}</b>
            <span>${k} · ${App.getP(k).tes ? `Tes Bab terbaik ${App.getP(k).tes.best}% — perlu ${LULUS}%` : `tahap ${(App.getP(k).stage || 0) + 1} dari 6`}</span></div>
          <span class="chev">›</span></button>` : `<div class="lulus-banner ok">${Pic.html('🎉', 'ic-sm')}<div>Semua bab sudah lulus! 太棒了！</div></div>`}
        <h2 class="section-title">Pilih volume</h2>
        <div class="vol-list">${VOLUMES.map(v => this.volKartu(v)).join('')}</div>
        ${this.postHTML()}`;
    }
    App.main(`
      <section class="hero">
        <div><h1>華語文能力測驗</h1>
          <p>${L < 2 ? 'Modul persiapan TOCFL Band A · Vol.1–3' : `Mulai dari ${this.mulai() === '*' ? 'semua bab' : this.mulai()} · bab terbuka setelah Tes Bab ≥ ${LULUS}%`}</p></div>
        ${App.ring(Math.round(nL / total * 100), `${nL}<small>/${total}</small>`, 'ring-lg')}
      </section>
      ${adm ? this.adminPanel() : ''}
      ${isi}
      ${L >= 1 ? `<button class="card continue" onclick="App.go('#/kirim')">${Pic.html('📤', 'mode-ic')}
        <div class="continue-txt"><small>Hasil</small><b>Status pengiriman</b>
        <span>${s.terkirim ? `Terakhir terkirim: ${new Date(s.terkirim).toLocaleString('id-ID')}` : 'Belum terkirim'}</span></div><span class="chev">›</span></button>` : ''}
      <p class="credit">Ilustrasi: Twemoji © Twitter/X &amp; kontributor, lisensi CC-BY 4.0. Gambar soal hitam-putih: OpenMoji (openmoji.org), lisensi CC BY-SA 4.0. Huruf kai: 全字庫正楷體 (TW-Kai), 國家發展委員會, 政府資料開放授權條款 第1版.</p>`);
  },
  volKartu(v) {
    const bab = this.volBab(v.num), lulus = bab.filter(c => this.lulus(c)).length, buka = this.terbuka(bab[0]);
    return `<button class="card vol-card ${v.color} ${buka ? '' : 'vol-kunci'}" ${buka ? `onclick="App.go('#/v/${v.num}')"` : 'disabled'}>
      <div class="vol-badge">${buka ? v.level : '🔒'}</div>
      <div class="vol-info"><b>Volume ${v.num}</b>
        <span>${v.tbcl} · ${bab.length} bab · ${v.vocab} kata</span>
        <div class="bar"><i style="width:${Math.round(lulus / bab.length * 100)}%"></i></div>
        <small>${buka ? `${lulus}/${bab.length} bab lulus` : 'Terkunci — selesaikan volume sebelumnya dulu'}</small></div>
      ${buka ? '<span class="chev">›</span>' : ''}</button>`;
  },

  /* ===== Daftar bab per volume (dengan kunci) ===== */
  moduleList(vol) {
    const groups = [], k = this.kini();
    for (const m of App.plan[vol]) {
      const cat = m.categories[0];
      if (!groups.length || groups[groups.length - 1].cat !== cat) groups.push({ cat, mods: [] });
      groups[groups.length - 1].mods.push(m);
    }
    return `<p class="kunci-info">${Pic.html('🔒', 'ic-sm')} <span>Bab berikutnya terbuka setelah kamu lulus Tes Bab bab sebelumnya dengan nilai minimal <b>${LULUS}%</b>. Tes Bab ada di tahap terakhir setiap bab dan boleh diulang.</span></p>` +
      groups.map(g => `
      <div class="cat-group">
        <div class="cat-head">${Pic.html(Pic.SCENE[Pic.catNum(g.cat)][0], 'cat-ic')}<span lang="zh-TW">${esc(g.cat)}</span></div>
        ${g.mods.map(m => {
          const buka = this.terbuka(m.code), lul = this.lulus(m.code), p = App.getP(m.code), best = p.tes?.best;
          const st = !buka ? 'lock' : lul ? 'lulus' : m.code === k ? 'kini' : App.status(m.code);
          return `<button class="mod-row st-${st}" ${buka ? `onclick="App.go('#/m/${m.code}/${p.stage || 0}')"` : `onclick="Siswa.kunciPesan('${m.code}')"`}>
            <span class="mod-code">${m.code}</span>
            <span class="mod-main"><b lang="zh-TW">${esc(m.title)}</b><small>${esc(m.scene)}</small></span>
            <span class="mod-state">${!buka ? '🔒' : lul ? `✓ ${best}%` : best != null ? best + '%' : ''}</span>
          </button>`;
        }).join('')}
      </div>`).join('');
  },
  kunciPesan(code) {
    const U = this.urut(), prev = U[U.indexOf(code) - 1];
    App.toast(this.mulai() ? `${code} masih terkunci. Lulus dulu Tes Bab ${prev} (minimal ${LULUS}%).` : 'Selesaikan data diri & tes penempatan dulu.');
  },

  /* ===== 1. Data diri ===== */
  PILIHAN: {
    usia: ['15–18', '19–25', '26–35', '> 35'],
    mandarin: ['A0', 'A1', 'A2'],
    pernah: ['Ya', 'Tidak'],
    lulus: ['準備一級', '準備二級', '入門級 (A1)', '基礎級 (A2) atau lebih tinggi', 'Belum lulus'],
    lama: ['< 6 bulan', '6–12 bulan', '1–2 tahun', '> 2 tahun'],
    rencana: ['≤ 3 bulan lagi', '3–6 bulan lagi', '> 6 bulan lagi', 'Belum tahu'],
    tujuan: ['Kuliah di Taiwan', 'Beasiswa', 'Pekerjaan', 'Minat pribadi', 'Lainnya'],
    cara: ['Belajar sendiri', 'Kursus / les', 'Di sekolah / kampus'],
    wawancara: ['Ya, bersedia', 'Tidak'],
  },
  DESKRIPSI_LEVEL: {
    A0: 'Baru mulai belajar. Bisa memperkenalkan diri, menyebut angka, jam, harga, dan anggota keluarga. (TBCL Level 1, ± 400 kata)',
    A1: 'Bisa bercakap sederhana sehari-hari: berbelanja, bertanya arah, naik kendaraan, ke dokter. (sampai TBCL Level 2, ± 800 kata)',
    A2: 'Bisa bercerita tentang pengalaman, alasan, dan rencana; memahami bacaan pendek. (sampai TBCL Level 3, ± 1.250 kata)',
  },
  // Penempatan dari level TOCFL yang sudah lulus (表2-1 thesis, sumber 華測會 2021):
  // 準備一級 ≈ TBCL 1 (membaca) → A01 · 準備二級 ≈ TBCL 2 → B01 · 入門級 ≈ TBCL 2+ → C01 · 基礎級 ≈ TBCL 3+ → semua bab terbuka
  MULAI_TOCFL: ['A01', 'B01', 'C01', '*'],
  renderProfil() {
    const s = this.get(), p = s.profilDraf || s.profil || {}, P = this.PILIHAN;
    if (s.profil && !this.admin()) return App.go('#/');   // data diri dikunci setelah disimpan
    App.bar('Data diri', '#/');
    const radio = (k, judul) => `<div class="field-k">${judul}</div>
      <div class="seg wrap" role="radiogroup">${P[k].map((o, i) => `<button class="${p[k] === i ? 'on' : ''}" onclick="Siswa.pf('${k}', ${i})">${esc(o)}</button>`).join('')}</div>`;
    const input = (k, judul, attr = '') => `<label class="field-k" for="p-${k}">${judul}</label>
      <input id="p-${k}" class="field" maxlength="100" ${attr} value="${esc(p[k] || '')}" oninput="Siswa.pf('${k}', this.value, true)">`;
    App.main(`
      <div class="panel"><div class="panel-k">${Pic.html('🔒', 'ic-sm')} Tentang data ini</div>
        <p>Modul ini bagian dari penelitian thesis tentang modul persiapan TOCFL Band A. Jawaban, nilai, dan progresmu dikirim ke peneliti dan hanya dipakai untuk penelitian; namamu tidak dipublikasikan.</p></div>
      ${input('nama', 'Nama atau inisial')}
      ${input('email', 'Email aktif', 'type="email" inputmode="email" autocomplete="email"')}
      <p class="hint">Hanya dipakai peneliti untuk menghubungimu. Tidak dipublikasikan.</p>
      ${radio('usia', 'Usia')}
      ${input('asal', 'Asal sekolah / kampus / kota (boleh dikosongkan)')}
      ${radio('mandarin', 'Kemampuan Mandarin saat ini (penilaian diri)')}
      ${p.mandarin != null ? `<p class="hint">${esc(this.DESKRIPSI_LEVEL[P.mandarin[p.mandarin]])}</p>` : ''}
      ${radio('lama', 'Sudah berapa lama belajar Mandarin?')}
      ${radio('pernah', 'Pernah mengikuti ujian TOCFL?')}
      ${p.pernah === 0 ? radio('lulus', 'Level TOCFL tertinggi yang sudah kamu lulus') : ''}
      ${radio('rencana', 'Kapan rencana mengikuti TOCFL?')}
      ${radio('tujuan', 'Tujuan utama belajar Mandarin')}
      ${radio('cara', 'Selama ini kamu belajar Mandarin dengan cara apa?')}
      ${radio('wawancara', 'Bersedia dihubungi untuk wawancara singkat tentang pengalamanmu memakai modul ini?')}
      ${input('wa', 'Nomor WhatsApp (boleh dikosongkan — untuk grup pengingat)', 'type="tel" inputmode="tel"')}
      <div class="field-k">Titik mulaimu</div>
      <p class="hint">${this.penjelasanMulai(p)}</p>
      <div class="checks"><label><input type="checkbox" id="p-setuju" ${p.setuju ? 'checked' : ''} onchange="Siswa.pf('setuju', this.checked, true)">
        Saya bersedia ikut, dan setuju jawaban, nilai, progres, serta email saya di app ini dikirim ke peneliti.</label></div>
      <button class="btn primary block" onclick="Siswa.simpanProfil()">Simpan dan lanjut ›</button>`);
  },
  penjelasanMulai(p) {
    if (p.pernah === 0 && p.lulus != null && p.lulus < 4) {
      const m = this.MULAI_TOCFL[p.lulus];
      return m === '*' ? 'Kamu sudah lulus 基礎級: semua bab langsung terbuka untuk latihan.' : `Berdasarkan level TOCFL-mu, kamu langsung mulai dari bab <b>${m}</b>.`;
    }
    if (p.pernah == null) return 'Jawab pertanyaan di atas dulu.';
    return 'Kamu akan mengerjakan <b>tes penempatan</b> singkat untuk menentukan bab pertamamu.';
  },
  pf(k, v, diam) {
    const s = this.get();
    this.set({ profilDraf: Object.assign({}, s.profilDraf || s.profil || {}, { [k]: v }) });
    if (!diam) { const y = window.scrollY; this.renderProfil(); window.scrollTo(0, y); }
  },
  simpanProfil() {
    const p = Object.assign({}, this.get().profilDraf || this.get().profil || {});
    for (const k of ['nama', 'email', 'asal', 'wa']) p[k] = ((document.getElementById('p-' + k) || {}).value || '').trim();
    if (p.pernah !== 0) delete p.lulus;
    if (!p.nama) return App.toast('Isi nama atau inisialmu.');
    if (p.nama.toLowerCase() === 'admin') return this.masukAdmin();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(p.email)) return App.toast('Isi alamat email yang benar.');
    const wajib = ['usia', 'mandarin', 'lama', 'pernah', 'rencana', 'tujuan', 'cara', 'wawancara', ...(p.pernah === 0 ? ['lulus'] : [])];
    if (wajib.some(k => p[k] == null)) return App.toast('Jawab semua pertanyaan dulu.');
    if (!p.setuju) return App.toast('Centang persetujuan dulu.');
    const tocfl = p.pernah === 0 && p.lulus < 4;
    this.set({ profil: p, profilDraf: null, mulaiWaktu: this.get().mulaiWaktu || Date.now(),
               tempat: tocfl ? { cara: 'tocfl', mulai: this.MULAI_TOCFL[p.lulus], selesai: Date.now() } : { cara: 'tes', tahap: {} } });
    this.uid();
    this.kirimDiam();
    App.go('#/');
  },

  /* ===== 2. Tes penempatan bertahap (paket A tes per level) ===== */
  tahapBerikut() {
    const t = this.get().tempat || {};
    if (t.cara !== 'tes' || t.mulai) return null;
    for (const lv of LEVELS) { if (!t.tahap?.[lv]) return lv; if (t.tahap[lv].skor < LULUS) return null; }
    return null;
  },
  penempatanHTML() {
    const t = this.get().tempat || {}, next = this.tahapBerikut();
    const baris = LEVELS.map(lv => {
      const h = t.tahap?.[lv];
      return `<li><span>Tahap ${lv} · ${this.data.tes[lv].A.length} soal</span>${h ? `<b class="${h.skor >= LULUS ? 'ok' : ''}">${h.skor}%</b>` : lv === next ? '<span>berikutnya</span>' : '<span>–</span>'}</li>`;
    }).join('');
    return `<div class="panel"><div class="panel-k">${Pic.html('🧭', 'ic-sm')} Cara kerja</div>
        <p>Tes dimulai dari level A0. Jika nilaimu ≥ ${LULUS}%, kamu lanjut ke tahap berikutnya (A1, lalu A2). Begitu nilai sebuah tahap di bawah ${LULUS}%, kamu mulai belajar dari volume level itu. Setiap tahap hanya bisa dikerjakan <b>satu kali</b>.</p>
        <ul class="tahap-list">${baris}</ul></div>
      ${next ? `<button class="btn primary block" onclick="App.go('#/siswa/tes/${next}')">Mulai tahap ${next} ›</button>` : ''}`;
  },
  acakUrut(n) { const a = [...Array(n).keys()]; for (let i = n - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; },
  // Urutan pilihan diacak tiap tes (kunci di data tes kebanyakan A), kecuali listen_pic (audio membacakan "A，…").
  // t._p = urutan asli → jawaban dicatat dengan huruf ASLI sehingga kolom di Sheet tetap sebanding antarsiswa.
  acak(t) {
    if (t.type === 'listen_pic' || !Array.isArray(t.options) || t.options.length < 2) return t;
    const p = this.acakUrut(t.options.length), o = { ...t, options: p.map(j => t.options[j]), _p: p };
    if (t.type === 'cloze') o.answers = t.answers.map(a => p.indexOf(a)); else o.answer = p.indexOf(t.answer);
    return o;
  },
  startTes(kind, lv, vol) {
    const s = this.get();
    if (kind === 'pre' && !this.admin() && this.tahapBerikut() !== lv) return App.go('#/');
    if (kind === 'post' && !this.admin() && (!this.volSelesai(vol) || s.post?.[vol]?.tes)) return App.go('#/');
    const paket = kind === 'pre' ? 'A' : 'B';
    const items = this.data.tes[lv][paket].map(t => ({ t: this.acak(t), code: '' }));
    clearInterval(Ujian.timer);
    Soal.plays = {}; Soal.limit = Ujian.PLAY_LIMIT;
    Ujian.session = { kind, lv, vol: vol || 0, items, i: 0, answers: {}, intro: {}, phase: 'q', dur: 30 * 60, end: null, grid: false,
                      title: kind === 'pre' ? `Tes penempatan · ${lv}` : `Tes akhir · Volume ${vol}`, back: '#/', paket };
    App.go('#/ujian');
  },
  hasilTes(s) {
    Soal.limit = null;
    App.bar(s.title, '#/');
    let pesan;
    if (s.kind === 'pre') {
      const m = this.mulai();
      pesan = !m ? `Nilaimu ≥ ${LULUS}% — hebat! Lanjut ke tahap berikutnya.`
        : m === '*' ? 'Kamu lulus semua tahap. Semua bab terbuka untuk latihan.'
        : `Kamu mulai belajar dari bab <b>${m}</b>. Selamat belajar! 加油！`;
    } else {
      const pre = this.get().tempat?.tahap?.[s.lv];
      pesan = `${pre ? `Tes penempatan ${s.lv}: ${pre.skor}% → ` : ''}tes akhir: ${s.pct}%. ${this.get().eval ? '' : 'Satu langkah lagi: beri pendapatmu tentang modul.'}`;
    }
    App.main(`
      <div class="result ${s.pct >= 80 ? 'hi' : s.pct >= 60 ? 'mid' : 'lo'}">
        ${App.ring(s.pct, s.pct + '%', 'ring-lg')}
        <div class="stats3 two">
          <div>${App.ring(s.l, s.l + '%')}<small lang="zh-TW">聽力</small></div>
          <div>${App.ring(s.r, s.r + '%')}<small lang="zh-TW">閱讀</small></div>
        </div>
        <p>${pesan}</p>
      </div>
      <button class="btn primary block" onclick="App.go('${s.kind === 'post' && !this.get().eval ? '#/siswa/eval' : '#/'}')">Lanjut ›</button>`);
  },

  /* ===== Tes akhir per volume + evaluasi ===== */
  postHTML() {
    const s = this.get(), kartu = [];
    for (const v of [1, 2, 3]) {
      const h = s.post?.[v]?.tes, ok = this.volSelesai(v);
      if (!h && !ok) continue;
      kartu.push(`<button class="card mode-card step-card st-${h ? 'done' : 'cur'}" ${h ? 'disabled' : `onclick="App.go('#/siswa/post/${v}')"`}>
        ${Pic.html(h ? '✅' : '🎓', 'mode-ic')}<div><b>Tes akhir · Volume ${v} (${VOL_LEVEL[v]})</b>
        <span>${h ? `Nilai ${h.skor}%` : `${this.data.tes[VOL_LEVEL[v]].B.length} soal gaya TOCFL · 30 menit · satu kali`}</span></div>${h ? '' : '<span class="chev">›</span>'}</button>`);
    }
    if (Object.values(s.post || {}).some(x => x?.tes)) {
      kartu.push(`<button class="card mode-card step-card st-${s.eval ? 'done' : 'cur'}" onclick="App.go('#/siswa/eval')">
        ${Pic.html(s.eval ? '✅' : '💬', 'mode-ic')}<div><b>Pendapatmu tentang modul</b><span>${s.eval ? 'Terima kasih! Boleh diubah.' : '9 pernyataan + 3 pertanyaan singkat'}</span></div><span class="chev">›</span></button>`);
    }
    return kartu.length ? `<h2 class="section-title">Tes akhir & evaluasi</h2><div class="mode-list">${kartu.join('')}</div>` : '';
  },
  EVAL: [
    'Modul ini mudah digunakan.',
    'Petunjuk di setiap tahap jelas.',
    'Dialog dan audio membantu saya memahami situasi nyata.',
    'Soal latihan mirip dengan format ujian TOCFL.',
    'Setelah memakai modul, saya lebih paham format ujian TOCFL.',
    'Modul membantu saya mengingat kosakata baru.',
    'Belajar grammar lewat dialog dan konteks membuat saya lebih mudah paham.',
    'Modul membantu saya menemukan kata kunci dalam soal.',
    'Kosakata dan grammar di modul sesuai dengan level saya.',
  ],
  TERBUKA: ['Bagian modul mana yang paling membantu Anda? Mengapa?', 'Kesulitan apa yang Anda alami saat memakai modul?', 'Apa saran Anda untuk memperbaiki modul?'],
  LIKERT: ['1 = Sangat tidak setuju', '2 = Tidak setuju', '3 = Netral', '4 = Setuju', '5 = Sangat setuju'],
  renderEval() {
    const s = this.get();
    if (!this.admin() && !Object.values(s.post || {}).some(x => x?.tes)) return App.go('#/');
    const jw = s.evalDraf || s.eval?.jw || [], tb = s.terbukaDraf || s.eval?.terbuka || [];
    App.bar('Pendapatmu', '#/');
    App.main(`
      <div class="panel"><p>Seberapa setuju kamu dengan pernyataan tentang modul ini?</p><ul class="likert-legend">${this.LIKERT.map(x => `<li>${x}</li>`).join('')}</ul></div>
      ${this.EVAL.map((it, i) => `<div class="likert ${jw[i] != null ? 'ok' : ''}">
        <p><b>${i + 1}.</b> ${esc(it)}</p>
        <div class="seg likert-seg">${[1, 2, 3, 4, 5].map(v => `<button class="${jw[i] === v ? 'on' : ''}" onclick="Siswa.likert(${i}, ${v})">${v}</button>`).join('')}</div>
        <div class="likert-ends"><small>Sangat tidak setuju</small><small>Sangat setuju</small></div></div>`).join('')}
      <h3 class="sub-title">Pertanyaan singkat (boleh dikosongkan)</h3>
      ${this.TERBUKA.map((q, i) => `<label class="field-k" for="tb-${i}">${i + 1}. ${esc(q)}</label>
        <textarea id="tb-${i}" rows="2" oninput="Siswa.isiTerbuka(${i}, this.value)">${esc(tb[i] || '')}</textarea>`).join('')}
      <button class="btn primary block" onclick="Siswa.simpanEval()">Simpan ✓</button>`);
  },
  likert(i, v) {
    const s = this.get(), arr = (s.evalDraf || s.eval?.jw || []).slice(); arr[i] = v;
    this.set({ evalDraf: arr });
    const y = window.scrollY; this.renderEval(); window.scrollTo(0, y);
  },
  isiTerbuka(i, v) { const s = this.get(), tb = (s.terbukaDraf || s.eval?.terbuka || []).slice(); tb[i] = v; this.set({ terbukaDraf: tb }); },
  simpanEval() {
    const s = this.get(), jw = s.evalDraf || s.eval?.jw || [];
    const kosong = this.EVAL.findIndex((_, i) => jw[i] == null);
    if (kosong >= 0) return App.toast(`Pernyataan ${kosong + 1} belum dijawab.`);
    const tb = s.terbukaDraf || s.eval?.terbuka || [];
    this.set({ eval: { jw: jw.slice(0, this.EVAL.length), terbuka: this.TERBUKA.map((_, i) => tb[i] || ''), waktu: Date.now() }, evalDraf: null, terbukaDraf: null });
    this.kirimDiam();
    App.toast('Terima kasih! 謝謝！');
    App.go('#/');
  },

  /* ===== Mode admin (ketik nama "admin" di Data diri): semua bab terbuka, data tidak dikirim ===== */
  masukAdmin() {
    Store.set(SISWA_KEY, { admin: true, profil: { nama: 'admin' }, tempat: { cara: 'admin', mulai: 'A01' }, mulaiWaktu: Date.now() });
    App.go('#/'); this.renderHome();
  },
  adminMulai(m) { this.set({ tempat: Object.assign({}, this.get().tempat, { mulai: m }) }); this.renderHome(); },
  keluarAdmin() {
    if (!confirm('Keluar dari mode admin? Semua jawaban admin dan progres bab di perangkat ini akan dihapus.')) return;
    Store.set(SISWA_KEY, {}); Store.set(STORAGE_KEY, {});
    this.renderHome();
  },
  adminPanel() {
    const m = this.mulai();
    return `<div class="panel admin-panel"><div class="panel-k">${Pic.html('🔧', 'ic-sm')} Mode admin</div>
      <p class="hint">Semua bab terbuka. Tidak ada data yang dikirim ke peneliti. Titik mulai (untuk mencoba tampilan kunci siswa):</p>
      <div class="seg wrap">${['A01', 'B01', 'C01'].map(x => `<button class="${m === x ? 'on' : ''}" onclick="Siswa.adminMulai('${x}')">${x}</button>`).join('')}</div>
      <div class="admin-act"><button class="btn" onclick="App.go('#/siswa/tes/A0')">Coba tes penempatan</button>
        <button class="btn" onclick="App.go('#/siswa/post/1')">Coba tes akhir</button>
        <button class="btn" onclick="Siswa.keluarAdmin()">Keluar admin</button></div></div>`;
  },

  /* ===== Kirim hasil ===== */
  payload() {
    const s = this.get(), prog = Store.get(STORAGE_KEY, {}), p = s.profil || {}, P = this.PILIHAN;
    const label = k => (p[k] != null && P[k] ? P[k][p[k]] ?? '' : '');
    const bab = this.urut().filter(c => prog[c]).map(c => {
      const x = prog[c];
      return { kode: c, tahap: (x.stage || 0) + 1, selesai: !!x.done, tes_best: x.tes?.best ?? '', tes_last: x.tes?.last ?? '', tes_kali: x.tes?.tries ?? '',
               lulus: this.lulus(c), lulus_waktu: (s.lulusWaktu || {})[c] || null, tugas_best: x.tasks?.best ?? '', tugas_kali: x.tasks?.tries ?? '',
               kata_tes: x.kata?.best ?? '', detik: x.detik || 0 };
    });
    return {
      v: 'siswa1', uid: this.uid(), nama: p.nama || '', email: p.email || '', wa: p.wa || '', asal: p.asal || '',
      profil: Object.fromEntries(Object.keys(P).map(k => [k, label(k)])),
      cara: s.tempat?.cara || '', mulai_bab: this.mulai() || '', tempat_selesai: s.tempat?.selesai || null,
      tahap: s.tempat?.tahap || {}, post: s.post || {}, eval: s.eval || null,
      kini: this.kini() || '', bab_lulus: this.nLulus(), posisi: s.posisi ? `${s.posisi.kode} · ${s.posisi.tahap}/6` : '', aktif: s.posisi?.waktu || null,
      mulai: s.mulaiWaktu || null, waktu: new Date().toISOString(), perangkat: /Mobi|Android|iPhone/i.test(navigator.userAgent) ? 'HP' : 'Komputer',
      bab, log: (s.log || []).slice(-300),
    };
  },
  async kirim() {
    if (this.admin()) throw new Error('mode admin tidak mengirim data');
    if (!KIRIM_URL) throw new Error('KIRIM_URL kosong');
    const res = await fetch(KIRIM_URL, { method: 'POST', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(this.payload()) });
    const j = await res.json();
    if (!j.ok) throw new Error(j.error || 'ditolak');
    this.set({ terkirim: Date.now(), gagalKirim: false });
  },
  kirimDiam() { if (this.get().profil?.setuju && !this.admin()) this.kirim().catch(() => this.set({ gagalKirim: true })); },
  renderKirim() {
    const s = this.get();
    App.bar('Hasil', '#/');
    App.main(`
      <div class="stats3 two">
        <div>${App.ring(Math.round(this.nLulus() / this.urut().length * 100), `${this.nLulus()}`)}<small>bab lulus</small></div>
        <div>${App.ring(0, this.kini() || '–')}<small>bab sekarang</small></div>
      </div>
      ${this.admin() ? '<p class="hint"><b>Mode admin: data tidak dikirim.</b></p>' : ''}
      <div class="panel"><div class="panel-k">${Pic.html('📤', 'ic-sm')} Pengiriman ke peneliti</div>
        <p>${s.terkirim ? `Terakhir terkirim: ${new Date(s.terkirim).toLocaleString('id-ID')}` : 'Belum terkirim.'}
        ${s.gagalKirim ? '<br><b>Pengiriman terakhir gagal — periksa koneksi internet lalu tekan tombol di bawah.</b>' : ''}</p>
        <p class="hint">Hasilmu terkirim otomatis setiap kali kamu menyelesaikan tes atau mencapai tahap baru. Kamu juga bisa mengirim ulang di sini — data lama diperbarui, tidak dobel.</p>
        <p class="hint">Kode siswa: <b>${this.uid()}</b></p></div>
      <button class="btn primary block" id="k-btn" onclick="Siswa.kirimTombol()">${Pic.html('📤', 'ic-sm')} Kirim hasil sekarang</button>
      <p class="hint" id="k-status"></p>`);
  },
  async kirimTombol() {
    const btn = document.getElementById('k-btn'), st = document.getElementById('k-status');
    btn.disabled = true; st.textContent = 'Mengirim…';
    try { await this.kirim(); App.toast('Hasil terkirim. 謝謝！'); this.renderKirim(); }
    catch { this.set({ gagalKirim: true }); st.textContent = 'Gagal mengirim. Periksa koneksi internet, lalu coba lagi.'; btn.disabled = false; }
  },

  /* ===== Petunjuk ===== */
  bukaPetunjuk() { if (!location.hash.startsWith('#/petunjuk')) this._dari = location.hash || '#/'; App.go('#/petunjuk'); },
  renderPetunjuk() {
    App.bar('Petunjuk', this._dari || '#/');
    const li = xs => xs.map(x => `<li>${x}</li>`).join('');
    App.main(`
      <div class="panel"><div class="panel-k">${Pic.html('📱', 'ic-sm')} Sebelum mulai</div>
        <ul class="ptj">${li([
          'Pakai <b>satu HP dan satu browser yang sama</b> dari awal sampai akhir. Progresmu tersimpan di HP itu.',
          '<b>Jangan hapus riwayat browser</b>, dan jangan pakai mode Incognito/Private.',
          'Tulis <b>nama atau inisial asli</b> dan <b>email aktif</b> yang benar.',
          'Siapkan <b>earphone</b>, karena ada soal mendengarkan.',
          '<b>Pengguna iPhone:</b> buka modul paling tidak setiap beberapa hari. Jika tidak dibuka di Safari selama 7 hari, progresmu bisa terhapus.'])}</ul></div>
      <div class="panel"><div class="panel-k">${Pic.html('🧭', 'ic-sm')} Cara kerja</div>
        <ul class="ptj">${li([
          '<b>Data diri</b> → <b>titik mulai</b>: jika sudah punya level TOCFL kamu langsung diarahkan; jika belum, kamu mengerjakan tes penempatan singkat.',
          `Bab terbuka <b>satu per satu</b>. Bab berikutnya terbuka setelah kamu lulus <b>Tes Bab</b> (tahap terakhir setiap bab) dengan nilai minimal <b>${LULUS}%</b>.`,
          'Tes Bab <b>boleh diulang</b> sampai lulus. Bab yang sudah terbuka bisa dibuka lagi kapan saja.',
          'Setelah semua bab satu volume lulus, kerjakan <b>tes akhir</b> volume itu, lalu beri pendapatmu tentang modul.'])}</ul></div>
      <div class="panel"><div class="panel-k">${Pic.html('⚠️', 'ic-sm')} Saat tes penempatan dan tes akhir</div>
        <ul class="ptj">${li([
          'Kerjakan di tempat yang tenang, tanpa gangguan selama 30 menit.',
          'Tes penempatan dan tes akhir <b>tidak bisa diulang</b>. Jawablah dengan jujur dan dengan kemampuanmu sendiri.'])}</ul></div>
      <p class="hint">Hasilmu terkirim otomatis ke peneliti (butuh internet).</p>
      <button class="btn primary block" onclick="App.go('${this._dari || '#/'}')">Mengerti ✓</button>`);
  },
};

/* ===== Sambungan ke app utama ===== */
const Kirim = { aktif: () => false, render: () => Siswa.renderKirim() };
App.renderHome = () => Siswa.renderHome();
App.moduleList = vol => Siswa.moduleList(vol);

// Latihan kosakata & ujian simulasi hanya memakai bab yang sudah terbuka
const _words = Latihan.words;
Latihan.words = function (vol, codes) { return _words.call(this, vol, codes).filter(v => Siswa.terbuka(v.code)); };
const _ubank = Ujian.bank;
Ujian.bank = function (vol) { return _ubank.call(this, vol).filter(x => Siswa.terbuka(x.code)); };

// Tes Bab: catat setiap percobaan; bila nilai ≥ 80% untuk pertama kali, bab berikutnya terbuka
Ujian.w = function (t) { const k = this.session.kind; return (this.session.full || k === 'pre' || k === 'post') && t.type === 'cloze' ? t.answers.length : 1; };
const _finish = Ujian.finish, _result = Ujian.result;
Ujian.finish = function () {
  const s = this.session;
  if (s.kind === 'tes') {
    const sudah = Siswa.lulus(s.code);
    _finish.call(this);
    const st = Siswa.get(), log = (st.log || []).concat([{ kode: s.code, skor: s.pct, dengar: s.l, baca: s.r, detik: s.used, waktu: Date.now(),
      ke: App.getP(s.code).tes?.tries || 1 }]);
    const patch = { log };
    if (!sudah && Siswa.lulus(s.code)) { patch.lulusWaktu = Object.assign({}, st.lulusWaktu, { [s.code]: Date.now() }); s.baruLulus = true; }
    Siswa.set(patch);
    Siswa.kirimDiam();
    return;
  }
  if (s.kind !== 'pre' && s.kind !== 'post') return _finish.call(this);
  clearInterval(this.timer); Speech.stop();
  const per = this.PARTS.map(() => [0, 0]), butir = [];
  s.items.forEach((x, i) => {
    const a = s.answers['u' + i], [g, n] = Soal.score(x.t, a), p = per[this.partOf(x.t)];
    p[0] += g; p[1] += n;
    const huruf = v => 'ABCDEF'[x.t._p ? x.t._p[v] : v];   // kembali ke huruf urutan asli
    if (x.t.type === 'cloze') x.t.answers.forEach((k, j) => butir.push({ no: x.t.no + j, jawab: a?.vals?.[j] != null ? huruf(a.vals[j]) : '', benar: a?.vals?.[j] === k ? 1 : 0 }));
    else butir.push({ no: x.t.no, jawab: a != null ? huruf(a) : '', benar: a === x.t.answer ? 1 : 0 });
  });
  const sum = arr => arr.reduce((a, [g, n]) => [a[0] + g, a[1] + n], [0, 0]), pc = ([g, n]) => n ? Math.round(g / n * 100) : 0;
  s.per = per; s.pct = pc(sum(per)); s.l = pc(sum(per.slice(0, 4))); s.r = pc(sum(per.slice(4)));
  s.used = this.elapsed(); s.phase = 'result';
  const [benar, dari] = sum(per);
  const hasil = { paket: s.paket, skor: s.pct, benar, dari, dengar: s.l, baca: s.r, detik: s.used, selesai: Date.now(), butir };
  const st = Siswa.get();
  if (s.kind === 'pre') {
    const tempat = Object.assign({}, st.tempat, { tahap: Object.assign({}, st.tempat?.tahap, { [s.lv]: hasil }) });
    if (s.pct < LULUS) { tempat.mulai = Siswa.volBab(LEVELS.indexOf(s.lv) + 1)[0]; tempat.selesai = Date.now(); }
    else if (s.lv === 'A2') { tempat.mulai = '*'; tempat.selesai = Date.now(); }
    if (!Siswa.admin() || !st.tempat?.mulai) Siswa.set({ tempat });
  } else {
    Siswa.set({ post: Object.assign({}, st.post, { [s.vol]: { tes: hasil } }) });
  }
  Siswa.kirimDiam();
  App.go('#/ujian');
};
Ujian.result = function () {
  const s = this.session;
  if (s.kind === 'pre' || s.kind === 'post') return Siswa.hasilTes(s);
  const r = _result.call(this);
  if (s.kind === 'tes') {
    const next = Siswa.berikut(s.code), ok = Siswa.lulus(s.code);
    const html = ok
      ? `<div class="lulus-banner ok">${Pic.html('🔓', 'ic-sm')}<div>${s.baruLulus ? `Lulus! ${next ? `Bab <b>${next}</b> sekarang terbuka.` : 'Ini bab terakhir.'}` : `Kamu sudah lulus bab ini (terbaik ${App.getP(s.code).tes.best}%).`}
          ${next ? `<small><button class="btn primary" style="margin-top:8px" onclick="App.go('#/m/${next}/0')">Buka ${next} ›</button></small>` : ''}</div></div>`
      : `<div class="lulus-banner belum">${Pic.html('🔒', 'ic-sm')}<div>Belum lulus — perlu minimal ${LULUS}% untuk membuka ${next || 'bab berikutnya'}.
          <small>Pelajari lagi bagian yang salah (lihat pembahasan di bawah), lalu ulangi Tes Bab. Nilai terbaikmu tetap tersimpan.</small></div></div>`;
    document.getElementById('app-main')?.insertAdjacentHTML('afterbegin', html);
  }
  return r;
};

// Tahap refleksi: pengingat syarat lulus di dekat kartu Tes Bab
const _rReflect = Modul.r_reflect;
Modul.r_reflect = function () {
  const next = Siswa.berikut(this.m.code), ok = Siswa.lulus(this.m.code);
  return `<p class="kunci-info">${Pic.html(ok ? '🔓' : '🔒', 'ic-sm')} <span>${ok ? `Tes Bab sudah lulus${next ? ` — ${next} terbuka` : ''}.` : `Lulus Tes Bab dengan nilai minimal <b>${LULUS}%</b> untuk membuka ${next || 'bab berikutnya'}.`}</span></p>` + _rReflect.call(this);
};

// Posisi & lama belajar per bab (ikut terkirim; membantu memilih siswa untuk wawancara)
let _aktif = Date.now();
['pointerdown', 'keydown', 'scroll', 'touchstart'].forEach(e => addEventListener(e, () => { _aktif = Date.now(); }, { passive: true }));
setInterval(() => {
  const m = location.hash.match(/^#\/m\/([A-Z]\d+)/);
  if (!m || document.hidden || Siswa.admin() || Date.now() - _aktif > 180000) return;
  App.setP(m[1], { detik: (App.getP(m[1]).detik || 0) + 15 });
}, 15000);
const _modOpen = Modul.open;
Modul.open = function (code, stage) {
  const before = App.getP(code).stage;
  _modOpen.call(this, code, stage);
  const after = App.getP(code).stage;
  if (Siswa.admin() || (before != null && after <= before)) return;
  Siswa.set({ posisi: { kode: code, tahap: after + 1, waktu: Date.now() } });
  clearTimeout(Siswa._tunda); Siswa._tunda = setTimeout(() => Siswa.kirimDiam(), 3000);
};

// Tombol ? (petunjuk) di bar atas — disembunyikan selama tes berjalan
const _bar = App.bar;
App.bar = function (title, back, extra = '') {
  const tes = location.hash.startsWith('#/ujian') && Ujian.session && Ujian.session.phase !== 'result';
  const tombol = tes || location.hash.startsWith('#/petunjuk') ? '' : `<button class="bar-pill bar-help" onclick="Siswa.bukaPetunjuk()" aria-label="Petunjuk" title="Petunjuk">?</button>`;
  return _bar.call(this, title, back, extra + tombol);
};

// Rute tambahan: #/petunjuk · #/siswa/profil · #/siswa/tes/A0|A1|A2 · #/siswa/post/1|2|3 · #/siswa/eval · #/kirim
const _route = App.route;
App.route = async function () {
  const p = (location.hash.replace(/^#\/?/, '') || '').split('/').filter(Boolean);
  try { await Siswa.load(); } catch { return App.main('<div class="empty"><p>Gagal memuat data. Periksa koneksi, lalu muat ulang.</p></div>'); }
  if (p[0] === 'siswa') {
    Speech.stop();
    if (p[1] === 'profil') return Siswa.renderProfil();
    if (p[1] === 'tes' && LEVELS.includes(p[2])) { if (await Pembaruan.cek()) return Pembaruan.muat(); return Siswa.startTes('pre', p[2]); }
    if (p[1] === 'post' && VOL_LEVEL[p[2]]) { if (await Pembaruan.cek()) return Pembaruan.muat(); return Siswa.startTes('post', VOL_LEVEL[p[2]], +p[2]); }
    if (p[1] === 'eval') return Siswa.renderEval();
    return App.go('#/');
  }
  if (p[0] === 'kirim') { Speech.stop(); return Siswa.renderKirim(); }
  if (p[0] === 'petunjuk') { Speech.stop(); return Siswa.renderPetunjuk(); }
  // bab & volume baru bisa dibuka setelah data diri + penempatan; bab terkunci → kembali ke daftar volume
  if ((p[0] === 'm' || p[0] === 'v') && Siswa.langkah() < 2) return App.go('#/');
  if (p[0] === 'm' && App.volOf(p[1]) && !Siswa.terbuka(p[1])) { Siswa.kunciPesan(p[1]); return App.go(`#/v/${App.volOf(p[1])}`); }
  if (p[0] === 'v' && VOLUMES.some(v => v.num === +p[1]) && !Siswa.terbuka(Siswa.volBab(+p[1])[0])) return App.go('#/');
  return _route.call(this);
};

/* ===== Pembaruan otomatis (sama dengan modul mini) =====
   Versi = semua ?v= di index.html + DATA_V (diisi buat_siswa.py). Dicek hanya di saat aman: sebelum tes dimulai,
   dan saat kembali ke aplikasi di beranda — tidak pernah di tengah tes/bab. */
const Pembaruan = {
  baru: null, terakhir: 0,
  versi: html => [...html.matchAll(/(?:src|href)="([^"]+\?v=[^"]+)"/g)].map(m => m[1]).concat(html.match(/DATA_V = '([^']*)'/)?.[1] || '').join('|'),
  sekarang() { return [...document.querySelectorAll('script[src*="?v="],link[href*="?v="]')].map(e => e.getAttribute('src') || e.getAttribute('href')).concat(window.DATA_V || '').join('|'); },
  async cek() {
    if (Date.now() - this.terakhir < 60000) return !!this.baru;
    this.terakhir = Date.now();
    try {
      const ctl = new AbortController(), tm = setTimeout(() => ctl.abort(), 4000);
      const html = await (await fetch(`${location.pathname}?nc=${Date.now()}`, { cache: 'no-store', signal: ctl.signal })).text();
      clearTimeout(tm);
      const v = this.versi(html);
      let dicoba = ''; try { dicoba = sessionStorage.getItem('pembaruan') || ''; } catch { /* */ }
      this.baru = v.includes('siswa.js?v=') && v !== this.sekarang() && v !== dicoba ? v : null;
    } catch { this.baru = null; }   // offline / lambat: lanjut dengan versi sekarang
    return !!this.baru;
  },
  muat() {
    try { sessionStorage.setItem('pembaruan', this.baru); } catch { /* */ }
    let h = 0; for (const c of this.baru) h = (h * 31 + c.charCodeAt(0)) >>> 0;
    location.replace(`${location.pathname}?u=${h.toString(36)}${location.hash}`);
  },
};
document.addEventListener('visibilitychange', async () => {
  if (document.hidden || !/^(#\/?)?$/.test(location.hash)) return;
  if (await Pembaruan.cek() && /^(#\/?)?$/.test(location.hash)) Pembaruan.muat();
});
