const Flashcard = {
  cards: [],
  filtered: [],
  index: 0,
  flipped: false,
  filter: 'all',
  showPinyin: true,

  init(chapterId) {
    this.chapterId = chapterId;
    this.currentPart = 'A';
    this.render();
  },

  getCards(part) {
    const chapter = App.data.chapters.find(c => c.id === this.chapterId);
    if (!chapter) return [];
    const partData = chapter.parts[part];
    if (!partData) return [];
    return partData.vocabulary || [];
  },

  loadPart(part) {
    this.currentPart = part;
    this.filter = 'all';
    const all = this.getCards(part);
    this.cards = [...all];
    this.filtered = [...all];
    this.index = 0;
    this.flipped = false;
    this.renderCards();
  },

  applyFilter(f) {
    this.filter = f;
    const all = this.getCards(this.currentPart);
    const progress = App.getProgress(this.chapterId);
    const memorized = progress.flashcard?.[this.currentPart] || [];

    if (f === 'all') {
      this.filtered = [...all];
    } else if (f === 'memorized') {
      this.filtered = all.filter(v => memorized.includes(v.vocab));
    } else if (f === 'unmemorized') {
      this.filtered = all.filter(v => !memorized.includes(v.vocab));
    }
    this.index = 0;
    this.flipped = false;
    this.renderCards();
  },

  flip() {
    this.flipped = !this.flipped;
    const inner = document.querySelector('.flashcard-inner');
    if (inner) inner.classList.toggle('flipped', this.flipped);
  },

  next() {
    if (this.index < this.filtered.length - 1) {
      this.index++;
      this.flipped = false;
      this.renderCard();
    }
  },

  prev() {
    if (this.index > 0) {
      this.index--;
      this.flipped = false;
      this.renderCard();
    }
  },

  markMemorized(vocab) {
    const progress = App.getProgress(this.chapterId);
    if (!progress.flashcard) progress.flashcard = {};
    if (!progress.flashcard[this.currentPart]) progress.flashcard[this.currentPart] = [];
    const list = progress.flashcard[this.currentPart];
    if (!list.includes(vocab)) list.push(vocab);
    App.saveProgress(this.chapterId, progress);
    App.showToast('Ditandai sudah hafal ✓', 'success');
    if (this.index < this.filtered.length - 1) this.next();
    else this.renderCards();
  },

  shuffle() {
    for (let i = this.filtered.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.filtered[i], this.filtered[j]] = [this.filtered[j], this.filtered[i]];
    }
    this.index = 0;
    this.flipped = false;
    this.renderCard();
    App.showToast('Kartu diacak!');
  },

  togglePinyin() {
    this.showPinyin = !this.showPinyin;
    const el = document.getElementById('fc-pinyin-el');
    if (el) el.classList.toggle('pinyin-hidden', !this.showPinyin);
    const btn = document.getElementById('btn-toggle-pinyin');
    if (btn) {
      btn.classList.toggle('active', !this.showPinyin);
      btn.textContent = this.showPinyin ? '👁 Sembunyikan Pinyin' : '👁 Tampilkan Pinyin';
    }
    App.showToast(this.showPinyin ? 'Pinyin ditampilkan' : 'Pinyin disembunyikan');
  },

  posLabel(pos) {
    const map = {
      'N': 'Kata Benda', 'V': 'Kata Kerja', 'Vi': 'Kata Kerja Intransitif',
      'Vs': 'Kata Sifat', 'Vst': 'Kata Kerja Statis', 'Vp': 'Kata Kerja Prestasi',
      'Vaux': 'Kata Kerja Bantu', 'Vpt': 'Kata Kerja Modal', 'Adv': 'Kata Keterangan',
      'Conj': 'Kata Sambung', 'Ptc': 'Partikel', 'Det': 'Penentu',
      'M': 'Kata Bantu Bilangan', 'Prep': 'Kata Depan', 'V-sep': 'Kata Kerja Terpisah',
      'Vp-sep': 'Kata Kerja Terpisah', 'N/Vi': 'Kata Benda/Kerja',
      'N/V-sep': 'Kata Benda/Kerja', 'V/Vaux': 'Kata Kerja/Bantu', 'N/M': 'Kata Benda/Satuan',
      'Vs-pred': 'Kata Sifat Predikat', 'Vst/V': 'Kata Kerja Statis'
    };
    return map[pos] || pos;
  },

  renderCard() {
    const area = document.getElementById('fc-card-area');
    if (!area) return;
    if (this.filtered.length === 0) {
      area.innerHTML = `<div class="empty-state"><div class="empty-icon">🃏</div><p>Tidak ada kartu untuk ditampilkan.</p></div>`;
      return;
    }
    if (this.index >= this.filtered.length) {
      this.renderCompletion(area);
      return;
    }

    const card = this.filtered[this.index];
    const progress = App.getProgress(this.chapterId);
    const memorized = progress.flashcard?.[this.currentPart] || [];
    const isMemorized = memorized.includes(card.vocab);
    const levelBadge = card.level === 'novice1'
      ? `<span class="badge badge-novice1">Novice 1</span>`
      : `<span class="badge badge-novice2">Novice 2</span>`;

    area.innerHTML = `
      <div class="flashcard-scene" id="fc-scene">
        <div class="flashcard-inner${this.flipped ? ' flipped' : ''}" id="fc-inner">
          <div class="flashcard-front">
            <div class="fc-hanzi">${card.vocab}</div>
            <div class="fc-pinyin${this.showPinyin ? '' : ' pinyin-hidden'}" id="fc-pinyin-el">${card.pinyin}</div>
            <div class="fc-hint">Klik kartu untuk melihat arti</div>
          </div>
          <div class="flashcard-back">
            <div class="fc-meaning">${card.meaning}</div>
            <div class="fc-pos-badge">${this.posLabel(card.pos)}</div>
            <div class="fc-level-badge">${levelBadge}</div>
          </div>
        </div>
      </div>
      <div class="fc-controls">
        <button class="btn-memorized no" onclick="Flashcard.next()">Lewati</button>
        <button class="btn-memorized yes${isMemorized ? ' done' : ''}" onclick="Flashcard.markMemorized('${card.vocab.replace(/'/g, "\\'")}')">
          ${isMemorized ? '✓ Sudah Hafal' : 'Sudah Hafal'}
        </button>
      </div>
      <div class="fc-nav">
        <button class="fc-nav-btn" onclick="Flashcard.prev()" ${this.index === 0 ? 'disabled' : ''}>← Sebelumnya</button>
        <div class="fc-progress-bar">
          <div class="bar-track">
            <div class="bar-fill" style="width:${((this.index + 1) / this.filtered.length) * 100}%"></div>
          </div>
        </div>
        <button class="fc-nav-btn" onclick="Flashcard.next()" ${this.index === this.filtered.length - 1 ? 'disabled' : ''}>Berikutnya →</button>
      </div>
    `;

    document.getElementById('fc-scene').addEventListener('click', () => this.flip());
  },

  renderCompletion(area) {
    const progress = App.getProgress(this.chapterId);
    const memorized = (progress.flashcard?.[this.currentPart] || []).length;
    const total = this.filtered.length;
    area.innerHTML = `
      <div class="fc-completion">
        <div class="completion-icon">🎉</div>
        <h3>Sesi selesai!</h3>
        <p>Kamu telah menyelesaikan semua kartu di bagian ini.<br>
           <strong>${memorized} / ${this.getCards(this.currentPart).length}</strong> kata sudah dihafal.</p>
        <button class="btn btn-primary" onclick="Flashcard.loadPart('${this.currentPart}')">Ulangi dari awal</button>
      </div>
    `;
  },

  renderCards() {
    const statsEl = document.getElementById('fc-stats');
    const progress = App.getProgress(this.chapterId);
    const memorized = (progress.flashcard?.[this.currentPart] || []).length;
    const total = this.getCards(this.currentPart).length;

    if (statsEl) {
      statsEl.innerHTML = `
        <span>Bagian <strong>${this.currentPart}</strong> &mdash; ${this.filtered.length} kartu</span>
        <span class="fc-count">${memorized}/${total} dihafal</span>
      `;
    }

    const filtersEl = document.getElementById('fc-filters');
    if (filtersEl) {
      filtersEl.innerHTML = `
        <button class="fc-filter-btn${this.filter === 'all' ? ' active' : ''}" onclick="Flashcard.applyFilter('all')">Semua (${total})</button>
        <button class="fc-filter-btn${this.filter === 'unmemorized' ? ' active' : ''}" onclick="Flashcard.applyFilter('unmemorized')">Belum Hafal (${total - memorized})</button>
        <button class="fc-filter-btn${this.filter === 'memorized' ? ' active' : ''}" onclick="Flashcard.applyFilter('memorized')">Sudah Hafal (${memorized})</button>
        <button class="btn-shuffle" onclick="Flashcard.shuffle()">🔀 Acak</button>
        <button class="btn-toggle-pinyin${this.showPinyin ? '' : ' active'}" id="btn-toggle-pinyin" onclick="Flashcard.togglePinyin()">
          ${this.showPinyin ? '👁 Sembunyikan Pinyin' : '👁 Tampilkan Pinyin'}
        </button>
      `;
    }

    this.renderCard();
  },

  render() {
    const chapter = App.data.chapters.find(c => c.id === this.chapterId);
    const parts = Object.keys(chapter.parts);
    const container = document.getElementById('tab-flashcard');
    container.innerHTML = `
      <div class="part-selector">
        ${parts.map(p => `
          <button class="part-btn${p === this.currentPart ? ' active' : ''}" onclick="Flashcard.switchPart('${p}')">
            Bagian ${p}: ${chapter.parts[p].title}
          </button>
        `).join('')}
      </div>
      <div class="flashcard-area">
        <div class="fc-stats" id="fc-stats"></div>
        <div class="fc-filters" id="fc-filters"></div>
        <div id="fc-card-area"></div>
      </div>
    `;
    this.loadPart(this.currentPart);
  },

  switchPart(part) {
    this.currentPart = part;
    document.querySelectorAll('.part-btn').forEach(b => {
      b.classList.toggle('active', b.textContent.trim().startsWith('Bagian ' + part));
    });
    this.loadPart(part);
  }
};
