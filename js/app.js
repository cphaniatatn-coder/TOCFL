const VOLUME_META = [
  {
    num: 1, title: 'Volume 1', subtitle: 'Novice 1 & 2', level: 'Pre-A1 ~ A1',
    file: 'data/tocfl_volume1.json', available: true,
    chapters: 10, vocab: 331, grammar: 40
  },
  {
    num: 2, title: 'Volume 2', subtitle: 'Elementary', level: 'A1',
    file: 'data/tocfl_volume2.json', available: true,
    chapters: 10, vocab: 334, grammar: 40
  },
  {
    num: 3, title: 'Volume 3', subtitle: 'Pre-Intermediate 1', level: 'A2',
    file: 'data/tocfl_volume3.json', available: true,
    chapters: 7, vocab: 234, grammar: 28
  },
  {
    num: 4, title: 'Volume 4', subtitle: 'Pre-Intermediate 2', level: 'A2',
    file: 'data/tocfl_volume4.json', available: true,
    chapters: 7, vocab: 237, grammar: 28
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
    this.renderVolumeSelector();
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
        <p>TOCFL Preparation — ${meta.title}: ${meta.subtitle} &nbsp;·&nbsp; ${this.data.level}</p>
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
    };
    const levelBadge = levelMap[chapter.level] || `<span class="badge badge-count">${chapter.level || ''}</span>`;
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
        <button class="tab-btn${this.currentTab === 'grammar' ? ' active' : ''}" onclick="App.switchTab('grammar')">
          <span class="tab-icon">📝</span><span class="tab-text">Tata Bahasa</span>
        </button>
        <button class="tab-btn${this.currentTab === 'reading' ? ' active' : ''}" onclick="App.switchTab('reading')">
          <span class="tab-icon">📖</span><span class="tab-text">Membaca</span>
        </button>
        <button class="tab-btn${this.currentTab === 'quiz' ? ' active' : ''}" onclick="App.switchTab('quiz')">
          <span class="tab-icon">✏️</span><span class="tab-text">Latihan Soal</span>
        </button>
      </div>
      <div id="tab-flashcard" class="tab-content${this.currentTab === 'flashcard' ? ' active' : ''}"></div>
      <div id="tab-grammar" class="tab-content${this.currentTab === 'grammar' ? ' active' : ''}"></div>
      <div id="tab-reading" class="tab-content${this.currentTab === 'reading' ? ' active' : ''}"></div>
      <div id="tab-quiz" class="tab-content${this.currentTab === 'quiz' ? ' active' : ''}"></div>
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
