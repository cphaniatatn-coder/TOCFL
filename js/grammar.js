const Grammar = {
  chapterId: null,
  currentPart: 'A',

  init(chapterId) {
    this.chapterId = chapterId;
    this.currentPart = 'A';
    this.render();
  },

  getGrammar(part) {
    const chapter = App.data.chapters.find(c => c.id === this.chapterId);
    return chapter?.parts[part]?.grammar || [];
  },

  toggleCard(id) {
    const card = document.getElementById('gcard-' + id);
    if (card) card.classList.toggle('open');
  },

  markUnderstood(id) {
    const progress = App.getProgress(this.chapterId);
    if (!progress.grammar) progress.grammar = {};
    if (!progress.grammar[this.currentPart]) progress.grammar[this.currentPart] = [];
    const list = progress.grammar[this.currentPart];
    if (!list.includes(id)) {
      list.push(id);
      App.saveProgress(this.chapterId, progress);
    }
    const card = document.getElementById('gcard-' + id);
    if (card) card.classList.add('understood');
    const btn = document.getElementById('gbtn-' + id);
    if (btn) { btn.textContent = '✓ Sudah Dipahami'; btn.classList.add('done'); }
    const check = document.getElementById('gcheck-' + id);
    if (check) { check.style.display = 'inline'; }
    App.showToast('Pola ditandai sudah dipahami ✓', 'success');
    this.updateSummary();
  },

  updateSummary() {
    const grammar = this.getGrammar(this.currentPart);
    const progress = App.getProgress(this.chapterId);
    const done = (progress.grammar?.[this.currentPart] || []).length;
    const total = grammar.length;
    const sumEl = document.getElementById('grammar-summary');
    if (sumEl) sumEl.textContent = `${done}/${total} pola dipahami`;
  },

  loadPart(part) {
    this.currentPart = part;
    this.renderList();
  },

  renderList() {
    const grammar = this.getGrammar(this.currentPart);
    const progress = App.getProgress(this.chapterId);
    const understood = progress.grammar?.[this.currentPart] || [];

    const listEl = document.getElementById('grammar-list');
    if (!listEl) return;

    if (grammar.length === 0) {
      listEl.innerHTML = `<div class="empty-state"><div class="empty-icon">📝</div><p>Belum ada pola tata bahasa untuk bagian ini.</p></div>`;
      return;
    }

    listEl.innerHTML = grammar.map(g => {
      const isDone = understood.includes(g.id);
      return `
        <div class="grammar-card${isDone ? ' understood' : ''}" id="gcard-${g.id}">
          <div class="grammar-card-header" onclick="Grammar.toggleCard('${g.id}')">
            <span class="grammar-id">${g.id}</span>
            <span class="grammar-pattern">${g.pattern}</span>
            ${isDone ? `<span class="understood-check" id="gcheck-${g.id}">✓</span>` : `<span id="gcheck-${g.id}" style="display:none" class="understood-check">✓</span>`}
            <span class="grammar-toggle">▼</span>
          </div>
          <div class="grammar-card-body">
            <div class="grammar-label">Penjelasan</div>
            <div class="grammar-explanation">${g.explanation}</div>
            <div class="grammar-label">Contoh Kalimat</div>
            <div class="grammar-example">${g.example}</div>
            <button class="btn-understood${isDone ? ' done' : ''}" id="gbtn-${g.id}"
              onclick="Grammar.markUnderstood('${g.id}')">
              ${isDone ? '✓ Sudah Dipahami' : 'Tandai Sudah Dipahami'}
            </button>
          </div>
        </div>
      `;
    }).join('');

    this.updateSummary();
  },

  render() {
    const chapter = App.data.chapters.find(c => c.id === this.chapterId);
    const parts = Object.keys(chapter.parts);
    const container = document.getElementById('tab-grammar');
    const progress = App.getProgress(this.chapterId);

    container.innerHTML = `
      <div class="part-selector">
        ${parts.map(p => `
          <button class="part-btn${p === this.currentPart ? ' active' : ''}" onclick="Grammar.switchPart('${p}')">
            Bagian ${p}: ${chapter.parts[p].title}
          </button>
        `).join('')}
      </div>
      <div style="display:flex; justify-content:flex-end; margin-bottom:12px;">
        <span style="font-size:.85rem; color:var(--text-sub);" id="grammar-summary"></span>
      </div>
      <div class="grammar-list" id="grammar-list"></div>
    `;
    this.loadPart(this.currentPart);
  },

  switchPart(part) {
    this.currentPart = part;
    document.querySelectorAll('#tab-grammar .part-btn').forEach(b => {
      b.classList.toggle('active', b.textContent.trim().startsWith('Bagian ' + part));
    });
    this.loadPart(part);
  }
};
