/* TOCFL Band A — app belajar mandiri (SDL): 3 volume × modul adegan.
   Struktur & jumlah modul: rencana-modul.xlsx / data/rencana.json.
   Isi modul: data/modul_vol{n}.json. Tampilan tahap: js/modul.js. */

const VOLUMES = [
  { num: 1, level: 'A0', tbcl: 'TBCL 第1級', vocab: 396, grammar: 15, approach: 'Vocabulary-first',
    file: 'data/modul_vol1.json' },
  { num: 2, level: 'A1', tbcl: 'TBCL 第2級', vocab: 402, grammar: 92, approach: 'TBLL 6 tahap',
    file: 'data/modul_vol2.json' },
  { num: 3, level: 'A2', tbcl: 'TBCL 第3級', vocab: 456, grammar: 134, approach: 'TBLL 6 tahap',
    file: 'data/modul_vol3.json' },
];

const STORAGE_KEY = 'tocfl_modul_progress';

const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

const App = {
  plan: null,        // data/rencana.json — peta semua modul
  volData: {},       // isi modul per volume (yang sudah dibuat)
  currentVolume: null,

  async init() {
    try {
      this.plan = await (await fetch('data/rencana.json')).json();
    } catch {
      this.main(`<div class="loading-screen"><p>Gagal memuat <strong>data/rencana.json</strong>. Jalankan app lewat server lokal (mis. <code>py -m http.server</code>).</p></div>`);
      return;
    }
    await Promise.all(VOLUMES.map(async v => {
      try { this.volData[v.num] = await (await fetch(v.file)).json(); }
      catch { this.volData[v.num] = { modules: [] }; }
    }));
    this.renderVolumes();
  },

  main(html) { document.getElementById('app-main').innerHTML = html; window.scrollTo(0, 0); },

  crumbs(items) {
    document.getElementById('breadcrumb').innerHTML = items.map(([label, fn], i) =>
      fn ? `<a onclick="${fn}">${esc(label)}</a>` : `<span>${esc(label)}</span>`
    ).join('<span class="sep">›</span>');
  },

  /* ===== penyimpanan progres (per-pelajar, lokal) ===== */
  loadAll() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); } catch { return {}; }
  },
  getP(code) { return this.loadAll()[code] || {}; },
  setP(code, patch) {
    const all = this.loadAll();
    all[code] = Object.assign(all[code] || {}, patch);
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(all)); } catch { /* mode privat: progres tidak tersimpan */ }
    this.updateHeader();
  },

  status(code) {
    const p = this.getP(code);
    if (p.done) return 'done';
    if (p.goal || p.stage || p.tasks) return 'progress';
    return 'new';
  },

  updateHeader() {
    const el = document.getElementById('header-progress');
    if (!el) return;
    const done = Object.values(this.loadAll()).filter(p => p.done).length;
    const total = this.plan ? Object.values(this.plan).reduce((a, m) => a + m.length, 0) : 0;
    el.textContent = total ? `Modul selesai: ${done}/${total}` : '';
  },

  moduleContent(vol, code) {
    return (this.volData[vol]?.modules || []).find(m => m.code === code);
  },

  /* ===== PILIH VOLUME ===== */
  renderVolumes() {
    this.currentVolume = null;
    this.crumbs([]);
    this.updateHeader();
    this.main(`
      <div class="volume-selector-header">
        <h1>華語文能力測驗 · Band A</h1>
        <p>Belajar mandiri per adegan. Satu modul = satu situasi nyata, lengkap dengan latihan soal bergaya TOCFL.</p>
      </div>
      <div class="volume-grid">
        ${VOLUMES.map(v => {
          const mods = this.plan[v.num] || [];
          const built = mods.filter(m => this.moduleContent(v.num, m.code)).length;
          const done = mods.filter(m => this.status(m.code) === 'done').length;
          return `
          <div class="volume-card vol-${v.num}" onclick="App.selectVolume(${v.num})">
            <div class="vol-header"><div class="vol-num">${v.num}</div><div class="vol-level-badge">${v.level}</div></div>
            <h3 class="vol-title">Volume ${v.num} · ${v.level}</h3>
            <div class="vol-subtitle">${v.tbcl} · ${v.approach}</div>
            <div class="vol-stats">
              <div class="vol-stat"><span>${mods.length}</span><small>Modul</small></div>
              <div class="vol-stat"><span>${v.vocab}</span><small>Kosakata</small></div>
              <div class="vol-stat"><span>${v.grammar}</span><small>Grammar</small></div>
            </div>
            <div class="vol-built">${built} modul sudah berisi · ${done} selesai</div>
            <div class="vol-cta">Buka peta modul →</div>
          </div>`;
        }).join('')}
      </div>`);
  },

  selectVolume(num) {
    this.currentVolume = num;
    this.renderDashboard();
  },

  /* ===== PETA MODUL (dashboard volume) ===== */
  renderDashboard() {
    const v = VOLUMES.find(x => x.num === this.currentVolume);
    const mods = this.plan[v.num];
    const all = this.loadAll();
    const done = mods.filter(m => all[m.code]?.done).length;
    const scores = mods.map(m => all[m.code]?.tasks?.best).filter(s => s != null);
    const avg = scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : null;

    this.crumbs([['Pilih Volume', 'App.renderVolumes()'], [`Volume ${v.num} · ${v.level}`]]);
    this.main(`
      <div class="dashboard-header">
        <h1>Volume ${v.num} · ${v.level}</h1>
        <p>${v.tbcl} · ${mods.length} adegan · ${v.approach}</p>
      </div>
      <div class="overall-progress">
        <div class="progress-stat"><div class="stat-num">${done}</div><div class="stat-label">Modul selesai</div></div>
        <div class="progress-divider"></div>
        <div class="progress-stat"><div class="stat-num">${avg ?? '–'}${avg != null ? '%' : ''}</div><div class="stat-label">Rata-rata tugas</div></div>
        <div class="progress-divider"></div>
        <div class="overall-bar">
          <label><span>Kemajuan volume</span><span><strong>${done}</strong>/${mods.length}</span></label>
          <div class="bar-track"><div class="bar-fill" style="width:${Math.round(done / mods.length * 100)}%"></div></div>
        </div>
      </div>
      <div class="chapter-grid">
        ${mods.map(m => this.moduleCard(v.num, m)).join('')}
      </div>`);
    this.updateHeader();
  },

  moduleCard(vol, m) {
    const built = !!this.moduleContent(vol, m.code);
    const st = this.status(m.code);
    const best = this.getP(m.code).tasks?.best;
    const stLabel = !built ? 'Belum tersedia' : st === 'done' ? '✓ Selesai' : st === 'progress' ? 'Sedang dipelajari' : 'Baru';
    return `
      <div class="chapter-card mod-card${built ? '' : ' mod-locked'} st-${built ? st : 'locked'}"
           ${built ? `onclick="Modul.open(${vol}, '${m.code}')"` : ''}>
        <div class="card-num">${m.code} <span class="mod-status">${stLabel}</span></div>
        <h3 class="mod-title-zh" lang="zh-TW">${esc(m.title)}</h3>
        <div class="card-topic">${esc(m.scene)}</div>
        <div class="card-meta">
          ${m.categories.map(c => `<span class="badge badge-count">${esc(c)}</span>`).join('')}
          <span class="badge badge-soft">${m.n_core} 核心${m.n_sup ? ` + ${m.n_sup} 補充` : ''}</span>
        </div>
        ${m.grammar.length ? `<div class="mod-grammar">${m.grammar.map(g => `<span>${esc(g)}</span>`).join('')}</div>` : '<div class="mod-grammar mod-grammar-none">Tanpa grammar baru (daur ulang)</div>'}
        ${best != null ? `<div class="mod-score">Skor tugas terbaik: ${best}%</div>` : ''}
      </div>`;
  },

  showToast(msg) {
    let t = document.getElementById('app-toast');
    if (!t) { t = document.createElement('div'); t.id = 'app-toast'; t.className = 'toast'; document.body.appendChild(t); }
    t.textContent = msg;
    requestAnimationFrame(() => requestAnimationFrame(() => t.classList.add('show')));
    clearTimeout(t._timer);
    t._timer = setTimeout(() => t.classList.remove('show'), 2500);
  },
};

document.addEventListener('DOMContentLoaded', () => App.init());
