/* Ujian simulasi per volume — urutan & proporsi bagian mengikuti format TOCFL Band A
   (聽力 lalu 閱讀), dengan batas waktu. Tidak ada umpan balik sampai ujian dikumpulkan,
   lalu setiap soal bisa ditinjau beserta alasannya dan tautan ke modul asalnya. */

const UJIAN_KEY = 'tocfl_ujian';

const Ujian = {
  session: null, timer: null,
  // Bobot tiap bagian (mengikuti jumlah soal ujian resmi Band A: 聽力 25/15/5/5, 閱讀 15/15/10/5/5)
  PARTS: [
    ['聽力 Part 1', 25, 'Deskripsi gambar', 'Dengarkan kalimat, pilih gambar yang cocok.'],
    ['聽力 Part 2', 15, 'Tanya-jawab', 'Dengarkan pertanyaan/kalimat, pilih tanggapan yang tepat.'],
    ['聽力 Part 3', 5, 'Dialog', 'Dengarkan dialog beberapa putaran, jawab pertanyaannya.'],
    ['聽力 Part 4', 5, 'Makna tersirat', 'Dengarkan dialog, tangkap maksud yang tidak diucapkan langsung.'],
    ['閱讀 Part 1', 15, 'Papan & tanda', 'Baca tanda/pengumuman singkat.'],
    ['閱讀 Part 2', 15, 'Gambar → kalimat', 'Lihat gambar, pilih kalimat yang cocok.'],
    ['閱讀 Part 3', 10, 'Membaca informasi', 'Baca informasi praktis (jadwal, menu, iklan), jawab pertanyaannya.'],
    ['閱讀 Part 4', 5, 'Melengkapi paragraf', 'Isi titik kosong dalam paragraf. Ada pilihan yang tidak terpakai.'],
    ['閱讀 Part 5', 5, 'Pemahaman bacaan', 'Baca teks pendek, jawab pertanyaannya.'],
  ],
  SEC_PER_ITEM: 72,
  PLAY_LIMIT: 2,

  partOf(t) { return this.PARTS.findIndex(p => t.part.startsWith(p[0])); },
  bank(vol) {
    const out = [];
    for (const m of App.volData[vol].modules) m.tasks.forEach(t => out.push({ t, code: m.code }));
    return out;
  },
  history(vol) { return (Store.get(UJIAN_KEY, {})[vol] || []); },

  menu(vol) {
    const bank = this.bank(vol), h = this.history(vol), s = this.session;
    const avail = this.PARTS.map((p, i) => bank.filter(x => this.partOf(x.t) === i).length);
    const running = s && s.vol === vol && s.phase !== 'result';
    return `
      <div class="panel exam">
        <div class="panel-k">${Pic.html('📝', 'ic-sm')} Seperti ujian sungguhan</div>
        <p>Soal diambil acak dari ${bank.length} soal di ${App.volData[vol].modules.length} modul volume ini, disusun menurut urutan bagian TOCFL: <b lang="zh-TW">聽力</b> dulu, lalu <b lang="zh-TW">閱讀</b>.
        Ada batas waktu, audio maksimal diputar ${this.PLAY_LIMIT}×, dan jawaban baru dinilai setelah kamu mengumpulkan.</p>
      </div>
      ${running ? `<button class="card continue" onclick="App.go('#/ujian')">${Pic.html('⏱️', 'mode-ic')}
          <div class="continue-txt"><small>Ujian sedang berjalan</small><b>Lanjutkan · soal ${s.i + 1}/${s.items.length}</b></div><span class="chev">›</span></button>` : ''}
      <div class="mode-list">
        ${[[20, 'Ujian singkat'], [40, 'Ujian lengkap']].map(([n, l]) => `
        <button class="card mode-card" onclick="Ujian.start(${vol}, ${n})">
          ${Pic.html(n === 20 ? '⏱️' : '🏁', 'mode-ic')}
          <div><b>${l} · ${n} soal</b><span>± ${Math.round(n * this.SEC_PER_ITEM / 60)} menit · ${n / 2} 聽力 + ${n / 2} 閱讀</span></div><span class="chev">›</span></button>`).join('')}
      </div>
      <details class="panel"><summary class="panel-k">Bank soal per bagian</summary>
        <ul class="partlist">${this.PARTS.map((p, i) => `<li><span lang="zh-TW">${p[0]}</span> ${p[2]}<b>${avail[i]}</b></li>`).join('')}</ul></details>
      ${h.length ? `<h3 class="sub-title">Riwayat</h3>
        <div class="hist">${h.slice(-8).reverse().map(x => `<div class="hrow">
          <span>${new Date(x.d).toLocaleDateString('id-ID', { day: 'numeric', month: 'short' })}</span>
          <span>${x.n} soal</span><span>聽 ${x.l}%</span><span>閱 ${x.r}%</span><b>${x.pct}%</b></div>`).join('')}</div>` : ''}`;
  },

  /* Susun paket: bagi n/2 聽力 & n/2 閱讀 menurut bobot; kekurangan di satu bagian dialihkan ke bagian lain */
  compose(vol, n) {
    const bank = shuffle(this.bank(vol));
    const byPart = this.PARTS.map((_, i) => bank.filter(x => this.partOf(x.t) === i));
    const pick = this.PARTS.map(() => 0);
    for (const [idx, total] of [[[0, 1, 2, 3], n / 2], [[4, 5, 6, 7, 8], n / 2]]) {
      const w = idx.reduce((a, i) => a + this.PARTS[i][1], 0);
      idx.forEach(i => (pick[i] = Math.min(byPart[i].length, Math.round(total * this.PARTS[i][1] / w))));
      let left = total - idx.reduce((a, i) => a + pick[i], 0);
      while (left > 0) {
        const i = idx.filter(i => pick[i] < byPart[i].length).sort((a, b) => (byPart[b].length - pick[b]) - (byPart[a].length - pick[a]))[0];
        if (i == null) break;
        pick[i]++; left--;
      }
      while (left < 0) { const i = idx.filter(i => pick[i] > 0).sort((a, b) => pick[b] - pick[a])[0]; pick[i]--; left++; }
    }
    return byPart.flatMap((list, i) => list.slice(0, pick[i]));
  },
  start(vol, n) {
    clearInterval(this.timer);
    const items = this.compose(vol, n);
    Soal.plays = {}; Soal.limit = this.PLAY_LIMIT;
    this.session = { vol, items, i: 0, answers: {}, intro: {}, phase: 'q', dur: items.length * this.SEC_PER_ITEM, end: null, grid: false };
    App.go('#/ujian');
  },

  render() {
    const s = this.session;
    if (s.phase === 'result') return this.result();
    Soal.limit = this.PLAY_LIMIT;
    const it = s.items[s.i], pi = this.partOf(it.t);
    if (!s.intro[pi]) return this.partIntro(pi);
    if (!s.end) s.end = Date.now() + s.dur * 1000;
    this.tick();
    const key = 'u' + s.i, n = s.items.length;
    App.bar(`Ujian · Vol.${s.vol}`, `#/v/${s.vol}/ujian`, `<span class="bar-pill timer" id="ujian-timer"></span>`);
    this.tick();
    App.main(`
      <div class="lprog"><i style="width:${this.nAnswered() / n * 100}%"></i></div>
      <div class="exam-top"><span lang="zh-TW">${esc(this.PARTS[pi][0])} · ${this.PARTS[pi][2]}</span>
        <button class="btn small ghost" onclick="Ujian.toggleGrid()">Soal ${s.i + 1}/${n} ▾</button></div>
      ${s.grid ? this.grid() : ''}
      <div class="q-card">${Soal.body(it.t, key, s.answers[key], 'Ujian', 'exam')}</div>
      <div class="dock">
        <button class="btn ghost" ${s.i === 0 ? 'disabled' : ''} onclick="Ujian.goto(${s.i - 1})">‹ Sebelumnya</button>
        ${s.i + 1 < n ? `<button class="btn primary" onclick="Ujian.goto(${s.i + 1})">Berikutnya ›</button>`
                      : `<button class="btn primary" onclick="Ujian.submit()">Kumpulkan</button>`}
      </div>`);
  },
  partIntro(pi) {
    const s = this.session, p = this.PARTS[pi];
    const cnt = s.items.filter(x => this.partOf(x.t) === pi).length;
    const first = s.items.findIndex(x => this.partOf(x.t) === pi) + 1;
    App.bar(`Ujian · Vol.${s.vol}`, `#/v/${s.vol}/ujian`, s.end ? `<span class="bar-pill timer" id="ujian-timer"></span>` : '');
    this.tick();
    App.main(`
      <div class="part-intro">
        ${Pic.html(pi < 4 ? '🎧' : '📖', 'pic-xl')}
        <h2 lang="zh-TW">${p[0].replace(/Part (\d)/, '第$1部分')}</h2>
        <b>${p[2]}</b>
        <p>${p[3]}</p>
        <small>Soal ${first}–${first + cnt - 1} · ${cnt} soal${pi < 4 ? ` · audio maks. ${this.PLAY_LIMIT}×` : ''}</small>
        ${!s.end ? `<p class="hint">Waktu (${Math.round(s.dur / 60)} menit) mulai berjalan saat kamu menekan Mulai.</p>` : ''}
        <button class="btn primary block" onclick="Ujian.session.intro[${pi}]=true;Ujian.render()">${s.end ? 'Lanjut' : 'Mulai'}</button>
      </div>`);
  },
  tick() {
    const s = this.session;
    clearInterval(this.timer);
    if (!s || !s.end || s.phase === 'result') return;
    const upd = () => {
      const left = Math.max(0, Math.round((s.end - Date.now()) / 1000));
      const el = document.getElementById('ujian-timer');
      if (el) { el.textContent = `⏱ ${Math.floor(left / 60)}:${String(left % 60).padStart(2, '0')}`; el.classList.toggle('low', left < 120); }
      if (left === 0) { clearInterval(this.timer); App.toast('Waktu habis — jawaban dikumpulkan.'); this.finish(); }
    };
    upd(); this.timer = setInterval(upd, 1000);
  },
  nAnswered() { const s = this.session; return s.items.filter((x, i) => this.done(x.t, s.answers['u' + i])).length; },
  done(t, a) { return t.type === 'cloze' ? !!(a && t.answers.every((_, k) => a.vals[k] != null)) : a != null; },
  grid() {
    const s = this.session;
    return `<div class="qgrid">${s.items.map((x, i) => `<button class="${i === s.i ? 'cur' : ''} ${this.done(x.t, s.answers['u' + i]) ? 'ok' : ''}" onclick="Ujian.goto(${i})">${i + 1}</button>`).join('')}</div>`;
  },
  toggleGrid() { this.session.grid = !this.session.grid; this.render(); },
  goto(i) { Speech.stop(); this.session.i = i; this.session.grid = false; this.render(); window.scrollTo(0, 0); },
  pick(key, oi) { this.session.answers[key] = oi; this.keep(); },
  clozeSel(key, k) { this.session.answers[key] = Soal.clozeSel(this.session.answers[key], k); this.keep(); },
  clozeFill(key, oi) { this.session.answers[key] = Soal.clozeFill(Soal.reg[key], this.session.answers[key], oi); this.keep(); },
  keep() { const y = window.scrollY; this.render(); window.scrollTo(0, y); },
  submit() {
    const left = this.session.items.length - this.nAnswered();
    if (left && !confirm(`Masih ada ${left} soal belum dijawab. Kumpulkan sekarang?`)) return;
    this.finish();
  },

  finish() {
    const s = this.session;
    clearInterval(this.timer);
    Speech.stop();
    const per = this.PARTS.map(() => [0, 0]);
    s.items.forEach((x, i) => { const [g, n] = Soal.score(x.t, s.answers['u' + i]); const p = per[this.partOf(x.t)]; p[0] += g; p[1] += n; });
    const sum = arr => arr.reduce((a, [g, n]) => [a[0] + g, a[1] + n], [0, 0]);
    const pc = ([g, n]) => n ? Math.round(g / n * 100) : 0;
    s.per = per; s.pct = pc(sum(per)); s.l = pc(sum(per.slice(0, 4))); s.r = pc(sum(per.slice(4)));
    s.used = Math.min(s.dur, Math.round((Date.now() - (s.end - s.dur * 1000)) / 1000));
    s.phase = 'result'; s.filter = 'salah';
    const all = Store.get(UJIAN_KEY, {});
    (all[s.vol] = all[s.vol] || []).push({ d: Date.now(), n: s.items.length, pct: s.pct, l: s.l, r: s.r });
    Store.set(UJIAN_KEY, all);
    App.go('#/ujian');
  },
  result() {
    const s = this.session;
    Soal.limit = null;
    App.bar(`Hasil ujian · Vol.${s.vol}`, `#/v/${s.vol}/ujian`);
    const wrongCodes = [...new Set(s.items.filter((x, i) => { const [g, n] = Soal.score(x.t, s.answers['u' + i]); return g < n; }).map(x => x.code))];
    const list = s.items.map((x, i) => ({ x, i, ok: (([g, n]) => g === n)(Soal.score(x.t, s.answers['u' + i])) }))
      .filter(r => s.filter === 'semua' || !r.ok);
    App.main(`
      <div class="result ${s.pct >= 80 ? 'hi' : s.pct >= 60 ? 'mid' : 'lo'}">
        ${App.ring(s.pct, s.pct + '%', 'ring-lg')}
        <p>Waktu terpakai ${Math.floor(s.used / 60)} menit ${s.used % 60} detik.</p>
        <div class="stats3 two">
          <div>${App.ring(s.l, s.l + '%')}<small lang="zh-TW">聽力</small></div>
          <div>${App.ring(s.r, s.r + '%')}<small lang="zh-TW">閱讀</small></div>
        </div>
      </div>
      <h3 class="sub-title">Per bagian</h3>
      <div class="partbars">${this.PARTS.map((p, i) => s.per[i][1] ? `<div class="pb">
          <span lang="zh-TW">${p[0]}</span><div class="bar"><i style="width:${s.per[i][0] / s.per[i][1] * 100}%"></i></div><b>${s.per[i][0]}/${s.per[i][1]}</b></div>` : '').join('')}</div>
      <p class="hint">Di 閱讀 Part 4, setiap titik kosong dihitung satu poin, sama seperti di ujian resmi.</p>
      ${wrongCodes.length ? `<div class="panel"><div class="panel-k">Modul yang perlu diulang</div>
        <div class="chips">${wrongCodes.map(c => `<button class="chip" onclick="App.go('#/m/${c}/0')">${c} <span lang="zh-TW">${esc(App.findModule(c).m.title)}</span></button>`).join('')}</div></div>` : ''}
      <div class="toolbar"><h3 class="sub-title">Tinjau soal</h3><span class="spacer"></span>
        <div class="seg">${[['salah', 'Yang salah'], ['semua', 'Semua']].map(([k, l]) => `<button class="${s.filter === k ? 'on' : ''}" onclick="Ujian.session.filter='${k}';Ujian.keep()">${l}</button>`).join('')}</div></div>
      ${list.map(({ x, i }) => `<div class="q-card review">
          <div class="q-part"><b>${i + 1}.</b> <span lang="zh-TW">${esc(x.t.part)}</span> · <a href="#/m/${x.code}/0">${x.code}</a></div>
          ${Soal.body(x.t, 'r' + i, s.answers['u' + i], 'Ujian', 'review')}</div>`).join('') || '<p class="hint">Tidak ada soal yang salah. 太棒了！</p>'}
      <div class="row2"><button class="btn primary" onclick="Ujian.start(${s.vol}, ${s.items.length})">Ujian baru</button>
        <button class="btn ghost" onclick="App.go('#/v/${s.vol}/ujian')">Selesai</button></div>`);
  },
};
