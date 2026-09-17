const VOLUME_META = [
  {
    num: 1, title: 'Volume 1', subtitle: '時代華語一 L01-L04', level: 'A1',
    file: 'data/shidai_volume1.json', available: true,
    chapters: 34, vocab: 204, grammar: 32
  },
  {
    num: 2, title: 'Volume 2', subtitle: '時代華語一 L05-L08', level: 'A1',
    file: 'data/shidai_volume2.json', available: true,
    chapters: 36, vocab: 229, grammar: 32
  },
  {
    num: 3, title: 'Volume 3', subtitle: '時代華語一 L09-L12', level: 'A1 / A2',
    file: 'data/shidai_volume3.json', available: true,
    chapters: 32, vocab: 174, grammar: 28
  },
  {
    num: 4, title: 'Volume 4', subtitle: '時代華語一 L13-L16', level: 'A2',
    file: 'data/shidai_volume4.json', available: true,
    chapters: 39, vocab: 198, grammar: 35
  },
];

const App = {
  data: null,
  currentView: 'volume-selector',
  currentVolume: null,
  currentChapterId: null,
  currentTab: 'flashcard',

  getStorageKey() {
    return `tocfl_progress_vol${this.currentVolume}`;
  },

  async init() {
    this._patchQuizReflection();
    this.renderVolumeSelector();
  },

  /* ===== 反思與進度 — REFLEKSI PASCA-TUGAS (patch Quiz.renderResult) ===== */

  _patchQuizReflection() {
    if (typeof Quiz === 'undefined' || Quiz._reflectionPatched) return;
    Quiz._reflectionPatched = true;
    const origRenderResult = Quiz.renderResult.bind(Quiz);
    Quiz.renderResult = function () {
      origRenderResult();
      App._appendQuizReflection(this.chapterId);
    };
  },

  _appendQuizReflection(chapterId) {
    const container = document.getElementById('tab-quiz');
    if (!container) return;
    const diff = (this.getReflection(chapterId).difficulty || '').replace(/</g, '&lt;');
    container.insertAdjacentHTML('beforeend', `
      <div class="quiz-reflection" style="max-width:560px; margin:24px auto 0; padding:16px; border:1px solid var(--border,#d4d4d8); border-radius:10px;">
        <div class="intro-stage-label" style="font-size:.8rem; letter-spacing:.08em; color:var(--text-sub); text-transform:uppercase; margin-bottom:8px;">反思與進度 · Refleksi</div>
        <label for="quiz-reflection-input" style="display:block; font-weight:600; margin-bottom:8px;">Bagian mana yang masih sulit?</label>
        <textarea id="quiz-reflection-input" rows="3" style="width:100%; box-sizing:border-box; padding:10px 12px; border:1px solid var(--border,#d4d4d8); border-radius:8px; font:inherit; resize:vertical;"
          placeholder="Tulis bagian, pola kalimat, atau kosakata yang masih membingungkan…"
          onblur="App.saveReflectionField(${chapterId}, 'difficulty', this.value)">${diff}</textarea>
      </div>
    `);
  },

  showLoading() {
    document.getElementById('app-main').innerHTML = `
      <div class="loading-screen">
        <div class="spinner"></div>
        <p>Memuat data TOCFL...</p>
      </div>
    `;
  },

  getProgress(chapterId) {
    const all = JSON.parse(localStorage.getItem(this.getStorageKey()) || '{}');
    return all[chapterId] || {};
  },

  saveProgress(chapterId, data) {
    const all = JSON.parse(localStorage.getItem(this.getStorageKey()) || '{}');
    all[chapterId] = data;
    localStorage.setItem(this.getStorageKey(), JSON.stringify(all));
    this.updateHeaderProgress();
  },

  /* Refleksi/tujuan belajar — field baru "reflection" di dalam tocfl_progress_vol{n},
     tidak mengubah kunci lama & diabaikan oleh calcChapterProgress(). */
  getReflection(chapterId) {
    return this.getProgress(chapterId).reflection || {};
  },

  saveReflectionField(chapterId, field, value) {
    const progress = this.getProgress(chapterId);
    if (!progress.reflection) progress.reflection = {};
    progress.reflection[field] = (value || '').trim();
    this.saveProgress(chapterId, progress);
  },

  calcChapterProgress(chapterId) {
    const chapter = this.data.chapters.find(c => c.id === chapterId);
    const progress = this.getProgress(chapterId);
    const activities = [false, false, false, false];

    let totalVocab = 0, memorized = 0;
    Object.keys(chapter.parts).forEach(p => {
      const vocab = chapter.parts[p].vocabulary || [];
      totalVocab += vocab.length;
      memorized += (progress.flashcard?.[p] || []).length;
    });
    if (totalVocab > 0 && memorized > 0) activities[0] = memorized >= totalVocab ? 'done' : 'partial';

    let totalGrammar = 0, doneGrammar = 0;
    Object.keys(chapter.parts).forEach(p => {
      const g = chapter.parts[p].grammar || [];
      totalGrammar += g.length;
      doneGrammar += (progress.grammar?.[p] || []).length;
    });
    if (totalGrammar > 0 && doneGrammar > 0) activities[1] = doneGrammar >= totalGrammar ? 'done' : 'partial';

    if (progress.reading?.answered > 0) activities[2] = 'partial';
    if (progress.quiz?.bestScore >= 60) activities[3] = progress.quiz.bestScore >= 80 ? 'done' : 'partial';

    const score = activities.filter(a => a === 'done').length * 25
      + activities.filter(a => a === 'partial').length * 10;

    return { activities, score: Math.min(score, 100) };
  },

  calcOverallProgress() {
    if (!this.data) return { done: 0, total: 0, pct: 0 };
    const total = this.data.chapters.length;
    let totalPct = 0;
    this.data.chapters.forEach(c => { totalPct += this.calcChapterProgress(c.id).score; });
    return {
      done: this.data.chapters.filter(c => this.calcChapterProgress(c.id).score >= 80).length,
      total,
      pct: Math.round(totalPct / total)
    };
  },

  updateHeaderProgress() {
    const el = document.getElementById('header-progress');
    if (!el) return;
    if (!this.currentVolume) { el.textContent = ''; return; }
    const { pct } = this.calcOverallProgress();
    el.textContent = `Progress: ${pct}%`;
  },

  /* ===== VOLUME SELECTOR ===== */

  renderVolumeSelector() {
    this.currentView = 'volume-selector';
    document.getElementById('header-progress').textContent = '';
    document.getElementById('breadcrumb').innerHTML = '';

    document.getElementById('app-main').innerHTML = `
      <div class="volume-selector-header">
        <h1>華語文能力測驗</h1>
        <p>TOCFL Preparation — Pilih Volume Pelajaran</p>
      </div>
      <div class="volume-grid">
        ${VOLUME_META.map(v => this._renderVolumeCard(v)).join('')}
      </div>
    `;
  },

  _renderVolumeCard(v) {
    if (v.available) {
      return `
        <div class="volume-card vol-${v.num}" onclick="App.selectVolume(${v.num})">
          <div class="vol-header">
            <div class="vol-num">${v.num}</div>
            <div class="vol-level-badge">${v.level}</div>
          </div>
          <h3 class="vol-title">${v.title}</h3>
          <div class="vol-subtitle">${v.subtitle}</div>
          <div class="vol-stats">
            <div class="vol-stat"><span>${v.chapters}</span><small>Bab</small></div>
            <div class="vol-stat"><span>${v.vocab}</span><small>Kosakata</small></div>
            <div class="vol-stat"><span>${v.grammar}</span><small>Tata Bahasa</small></div>
          </div>
          <div class="vol-cta">Mulai Belajar →</div>
        </div>
      `;
    }
    return `
      <div class="volume-card vol-${v.num} vol-unavailable">
        <div class="vol-header">
          <div class="vol-num">${v.num}</div>
          <div class="vol-level-badge">${v.level}</div>
        </div>
        <h3 class="vol-title">${v.title}</h3>
        <div class="vol-subtitle">${v.subtitle}</div>
        <div class="vol-coming-soon">Segera Hadir</div>
      </div>
    `;
  },

  async selectVolume(num) {
    this.currentVolume = num;
    const meta = VOLUME_META.find(v => v.num === num);
    this.showLoading();
    try {
      const res = await fetch(meta.file);
      if (!res.ok) throw new Error('not found');
      this.data = await res.json();
      this.renderDashboard();
    } catch {
      document.getElementById('app-main').innerHTML = `
        <div class="loading-screen">
          <div style="color:var(--danger); text-align:center;">
            <div style="font-size:2rem; margin-bottom:12px;">⚠️</div>
            <p>Gagal memuat data. Pastikan file <strong>${meta.file}</strong> tersedia.</p>
            <button class="btn btn-outline" style="margin-top:20px;" onclick="App.renderVolumeSelector()">← Kembali</button>
          </div>
        </div>
      `;
    }
  },

  /* ===== DASHBOARD ===== */

  renderDashboard() {
    this.currentView = 'dashboard';
    const meta = VOLUME_META.find(v => v.num === this.currentVolume);
    const { done, total, pct } = this.calcOverallProgress();
    let totalVocab = 0;
    this.data.chapters.forEach(c => {
      Object.keys(c.parts).forEach(p => { totalVocab += (c.parts[p].vocabulary || []).length; });
    });

    document.getElementById('app-main').innerHTML = `
      <div class="dashboard-header">
        <h1>華語文能力測驗</h1>
        <p>TOCFL Preparation — ${meta.title}: ${meta.subtitle}</p>
      </div>
      <div class="overall-progress">
        <div class="progress-stat">
          <div class="stat-num">${total}</div>
          <div class="stat-label">Total Bab</div>
        </div>
        <div class="progress-divider"></div>
        <div class="progress-stat">
          <div class="stat-num">${totalVocab}</div>
          <div class="stat-label">Kosakata</div>
        </div>
        <div class="progress-divider"></div>
        <div class="progress-stat">
          <div class="stat-num">${this.data.total_grammar_points}</div>
          <div class="stat-label">Pola Tata Bahasa</div>
        </div>
        <div class="progress-divider"></div>
        <div class="overall-bar">
          <label><span>Progress Keseluruhan</span><span><strong>${done}</strong>/${total} bab selesai</span></label>
          <div class="bar-track"><div class="bar-fill" style="width:${pct}%"></div></div>
        </div>
      </div>
      <div class="chapter-grid">
        ${this.data.chapters.map(c => this.renderChapterCard(c)).join('')}
      </div>
    `;

    document.getElementById('breadcrumb').innerHTML = `
      <a onclick="App.renderVolumeSelector()">Pilih Volume</a>
      <span class="sep">›</span>
      <span>${meta.title}</span>
    `;
    this.updateHeaderProgress();
  },

  renderChapterCard(chapter) {
    const { activities, score } = this.calcChapterProgress(chapter.id);
    const levelMap = {
      'novice1': '<span class="badge badge-novice1">Novice 1</span>',
      'novice2': '<span class="badge badge-novice2">Novice 2</span>',
      'novice1+novice2': '<span class="badge badge-both">Novice 1 & 2</span>',
      'elementary': '<span class="badge badge-elem">Elementary</span>',
      'A1': '<span class="badge badge-level1">A1 Elementary</span>',
      'A2': '<span class="badge badge-level2">A2</span>',
      '基礎級 A2 (Part 1)': '<span class="badge badge-level2">A2 Part 1</span>',
      '基礎級 A2 (Part 2)': '<span class="badge badge-level2">A2 Part 2</span>',
    };
    const levelBadge = levelMap[chapter.level] || '';
    let totalVocab = 0;
    Object.keys(chapter.parts).forEach(p => { totalVocab += (chapter.parts[p].vocabulary || []).length; });
    const actLabels = ['Kosakata', 'Tata Bahasa', 'Membaca', 'Latihan'];

    return `
      <div class="chapter-card" onclick="App.navigateChapter(${chapter.id})">
        <div class="card-num">Bab ${chapter.id}</div>
        <h3>${chapter.title}</h3>
        <div class="card-topic">${chapter.topic}</div>
        <div class="card-meta">
          ${levelBadge}
          <span class="badge badge-count">${totalVocab} kata</span>
        </div>
        <div class="card-progress">
          <label><span>Progress</span><span>${score}%</span></label>
          <div class="bar-track-sm"><div class="bar-fill-sm" style="width:${score}%"></div></div>
        </div>
        <div class="activity-icons">
          ${activities.map((a, i) => `
            <div class="activity-dot${a === 'done' ? ' done' : a === 'partial' ? ' partial' : ''}" title="${actLabels[i]}"></div>
          `).join('')}
        </div>
      </div>
    `;
  },

  /* ===== CHAPTER VIEW ===== */

  navigateChapter(chapterId) {
    this.currentChapterId = chapterId;
    this.currentTab = 'flashcard';
    this.renderChapterIntro(chapterId);
  },

  /* ===== 情境導入 — SITUASI + PENETAPAN TUJUAN (SRL forethought) ===== */

  renderChapterIntro(chapterId) {
    this.currentChapterId = chapterId;
    const chapter = this.data.chapters.find(c => c.id === chapterId);
    const meta = VOLUME_META.find(v => v.num === this.currentVolume);
    const goal = (this.getReflection(chapterId).goal || '').replace(/</g, '&lt;');

    document.getElementById('breadcrumb').innerHTML = `
      <a onclick="App.renderVolumeSelector()">Pilih Volume</a>
      <span class="sep">›</span>
      <a onclick="App.renderDashboard()">${meta.title}</a>
      <span class="sep">›</span>
      <span>Bab ${chapter.id}: ${chapter.title}</span>
    `;

    document.getElementById('app-main').innerHTML = `
      <div class="chapter-intro" style="max-width:640px; margin:0 auto; padding:8px 4px;">
        <div class="intro-stage-label" style="font-size:.8rem; letter-spacing:.08em; color:var(--text-sub); text-transform:uppercase; margin-bottom:6px;">情境導入 · Persiapan</div>
        <h2 style="margin:0 0 16px;">Bab ${chapter.id}: ${chapter.title}</h2>
        <div class="intro-topic" style="background:var(--surface,#f4f4f5); border-radius:10px; padding:14px 16px; margin-bottom:20px;">
          <span class="intro-topic-label" style="display:block; font-size:.75rem; text-transform:uppercase; letter-spacing:.06em; color:var(--text-sub); margin-bottom:4px;">Situasi / Topik</span>
          <p style="margin:0;">${chapter.topic}</p>
        </div>
        <div class="intro-goal" style="margin-bottom:20px;">
          <label for="intro-goal-input" style="display:block; font-weight:600; margin-bottom:8px;">Apa yang ingin kamu kuasai di bab ini?</label>
          <textarea id="intro-goal-input" rows="3" style="width:100%; box-sizing:border-box; padding:10px 12px; border:1px solid var(--border,#d4d4d8); border-radius:8px; font:inherit; resize:vertical;"
            placeholder="Contoh: bisa memesan makanan dan menanyakan harga…"
            onblur="App.saveReflectionField(${chapterId}, 'goal', this.value)">${goal}</textarea>
        </div>
        <button class="btn btn-primary" onclick="App.startChapter(${chapterId})">Mulai Belajar →</button>
      </div>
    `;
    this.updateHeaderProgress();
  },

  startChapter(chapterId) {
    const input = document.getElementById('intro-goal-input');
    if (input) this.saveReflectionField(chapterId, 'goal', input.value);
    this.currentChapterId = chapterId;
    this.currentTab = 'flashcard';
    this.renderChapterView();
  },

  renderChapterView() {
    const chapter = this.data.chapters.find(c => c.id === this.currentChapterId);
    const meta = VOLUME_META.find(v => v.num === this.currentVolume);
    const { score } = this.calcChapterProgress(this.currentChapterId);
    const levelMap = {
      'novice1': '<span class="badge badge-novice1">Novice 1</span>',
      'novice2': '<span class="badge badge-novice2">Novice 2</span>',
      'novice1+novice2': '<span class="badge badge-both">Novice 1 & 2</span>',
      'elementary': '<span class="badge badge-elem">Elementary</span>',
      'A1': '<span class="badge badge-level1">A1 Elementary</span>',
      'A2': '<span class="badge badge-level2">A2</span>',
      '基礎級 A2 (Part 1)': '<span class="badge badge-level2">A2 Part 1</span>',
      '基礎級 A2 (Part 2)': '<span class="badge badge-level2">A2 Part 2</span>',
    };

    document.getElementById('breadcrumb').innerHTML = `
      <a onclick="App.renderVolumeSelector()">Pilih Volume</a>
      <span class="sep">›</span>
      <a onclick="App.renderDashboard()">${meta.title}</a>
      <span class="sep">›</span>
      <span>Bab ${chapter.id}: ${chapter.title}</span>
    `;

    document.getElementById('app-main').innerHTML = `
      <div class="chapter-header">
        <h2>Bab ${chapter.id}: ${chapter.title}</h2>
        <div class="ch-meta">
          ${levelMap[chapter.level] || ''}
          <span class="badge badge-count">${chapter.topic}</span>
          <span style="font-size:.8rem; color:var(--text-sub); margin-left:auto;">Progress: ${score}%</span>
        </div>
      </div>
      <div class="tab-nav">
        <button class="tab-btn${this.currentTab === 'flashcard' ? ' active' : ''}" onclick="App.switchTab('flashcard')">
          <span class="tab-icon">🃏</span><span class="tab-text">Kosakata</span>
        </button>
        <button class="tab-btn${this.currentTab === 'reading' ? ' active' : ''}" onclick="App.switchTab('reading')">
          <span class="tab-icon">📖</span><span class="tab-text">Membaca</span>
        </button>
        <button class="tab-btn${this.currentTab === 'quiz' ? ' active' : ''}" onclick="App.switchTab('quiz')">
          <span class="tab-icon">✏️</span><span class="tab-text">Latihan Soal</span>
        </button>
        <button class="tab-btn${this.currentTab === 'grammar' ? ' active' : ''}" onclick="App.switchTab('grammar')">
          <span class="tab-icon">📝</span><span class="tab-text">Tata Bahasa</span>
        </button>
      </div>
      <div id="tab-flashcard" class="tab-content${this.currentTab === 'flashcard' ? ' active' : ''}"></div>
      <div id="tab-reading" class="tab-content${this.currentTab === 'reading' ? ' active' : ''}"></div>
      <div id="tab-quiz" class="tab-content${this.currentTab === 'quiz' ? ' active' : ''}"></div>
      <div id="tab-grammar" class="tab-content${this.currentTab === 'grammar' ? ' active' : ''}"></div>
    `;

    this.loadTab(this.currentTab);
  },

  switchTab(tab) {
    this.currentTab = tab;
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    event.currentTarget.classList.add('active');
    document.getElementById('tab-' + tab).classList.add('active');
    this.loadTab(tab);
  },

  loadTab(tab) {
    const el = document.getElementById('tab-' + tab);
    if (!el || el.dataset.loaded === tab + this.currentChapterId) return;
    el.dataset.loaded = tab + this.currentChapterId;

    if (tab === 'flashcard') Flashcard.init(this.currentChapterId);
    else if (tab === 'grammar') Grammar.init(this.currentChapterId);
    else if (tab === 'reading') Reading.init(this.currentChapterId);
    else if (tab === 'quiz') Quiz.init(this.currentChapterId);
  },

  showToast(msg, type = '') {
    let toast = document.getElementById('app-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'app-toast';
      toast.className = 'toast';
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.className = 'toast' + (type ? ' ' + type : '');
    requestAnimationFrame(() => {
      requestAnimationFrame(() => toast.classList.add('show'));
    });
    clearTimeout(toast._timer);
    toast._timer = setTimeout(() => toast.classList.remove('show'), 2500);
  }
};

document.addEventListener('DOMContentLoaded', () => App.init());
