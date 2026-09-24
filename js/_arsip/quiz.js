const Quiz = {
  chapterId: null,
  questions: [],
  index: 0,
  score: 0,
  answered: false,

  init(chapterId) {
    this.chapterId = chapterId;
    this.questions = [];
    this.index = 0;
    this.score = 0;
    this.answered = false;
    this.render();
  },

  async loadData() {
    try {
      const res = await fetch(`data/quiz_volume${App.currentVolume}.json`);
      if (!res.ok) return null;
      const all = await res.json();
      const chapter = all.find(q => q.chapter_id === this.chapterId);
      return chapter?.questions || null;
    } catch {
      return null;
    }
  },

  answer(optionIndex) {
    if (this.answered) return;
    this.answered = true;
    const q = this.questions[this.index];
    const correct = q.answer;
    const isCorrect = optionIndex === correct;
    if (isCorrect) this.score++;

    const opts = document.querySelectorAll('.quiz-option-btn');
    opts.forEach((btn, i) => {
      btn.disabled = true;
      if (i === correct) btn.classList.add('correct');
      else if (i === optionIndex && !isCorrect) btn.classList.add('wrong');
    });

    const nextBtn = document.getElementById('quiz-next-btn');
    if (nextBtn) {
      nextBtn.style.display = 'flex';
      nextBtn.textContent = this.index < this.questions.length - 1 ? 'Soal Berikutnya →' : 'Lihat Hasil';
    }

    this.updateScoreBadge();
  },

  next() {
    if (this.index < this.questions.length - 1) {
      this.index++;
      this.answered = false;
      this.renderQuestion();
    } else {
      this.renderResult();
    }
  },

  updateScoreBadge() {
    const el = document.getElementById('quiz-score-badge');
    if (el) el.textContent = `Skor: ${this.score}/${this.index + (this.answered ? 1 : 0)}`;
  },

  renderQuestion() {
    const q = this.questions[this.index];
    const letters = ['A', 'B', 'C', 'D'];
    const typeLabel = { multiple_choice: 'Pilihan Ganda', fill_blank: 'Isi Titik-titik' };
    const area = document.getElementById('quiz-question-area');
    if (!area) return;

    area.innerHTML = `
      <div class="quiz-question-card">
        <div class="quiz-type-label">${typeLabel[q.type] || 'Soal'}</div>
        <div class="quiz-question-text">${q.question}</div>
        <div class="option-list">
          ${q.options.map((opt, i) => `
            <button class="option-btn quiz-option-btn" onclick="Quiz.answer(${i})">
              <span class="option-letter">${letters[i]}</span>
              <span>${opt}</span>
            </button>
          `).join('')}
        </div>
      </div>
      <button class="btn btn-primary" id="quiz-next-btn" style="display:none; margin:0 auto;"
        onclick="Quiz.next()">
        ${this.index < this.questions.length - 1 ? 'Soal Berikutnya →' : 'Lihat Hasil'}
      </button>
    `;

    const progressEl = document.getElementById('quiz-progress-text');
    if (progressEl) progressEl.textContent = `Soal ${this.index + 1} dari ${this.questions.length}`;

    const barEl = document.getElementById('quiz-bar-fill');
    if (barEl) barEl.style.width = `${((this.index + 1) / this.questions.length) * 100}%`;
  },

  renderResult() {
    const total = this.questions.length;
    const pct = Math.round((this.score / total) * 100);
    let msg, color;
    if (pct >= 80) { msg = 'Luar biasa! Pertahankan!'; color = 'var(--success)'; }
    else if (pct >= 60) { msg = 'Bagus! Terus berlatih.'; color = 'var(--primary-light)'; }
    else { msg = 'Jangan menyerah, ulangi lagi!'; color = 'var(--accent)'; }

    const progress = App.getProgress(this.chapterId);
    if (!progress.quiz) progress.quiz = {};
    const prev = progress.quiz.bestScore || 0;
    if (pct > prev) {
      progress.quiz.bestScore = pct;
      App.saveProgress(this.chapterId, progress);
    }

    const container = document.getElementById('tab-quiz');
    container.innerHTML = `
      <div class="quiz-result">
        <div class="result-score" style="color:${color}">${pct}%</div>
        <div class="result-label">${this.score} dari ${total} jawaban benar</div>
        <div class="result-msg">${msg}</div>
        <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
          <button class="btn btn-primary" onclick="Quiz.init(${this.chapterId})">Coba Lagi</button>
          <button class="btn btn-outline" onclick="App.navigateChapter(${this.chapterId})">Kembali ke Bab</button>
        </div>
      </div>
    `;
  },

  async render() {
    const container = document.getElementById('tab-quiz');
    container.innerHTML = `<div class="loading-screen"><div class="spinner"></div><p>Memuat soal...</p></div>`;

    const questions = await this.loadData();

    if (!questions || questions.length === 0) {
      container.innerHTML = `
        <div class="placeholder-box">
          <div class="placeholder-icon">✏️</div>
          <h3>Soal latihan belum tersedia</h3>
          <p>Tambahkan soal untuk bab ini dengan membuat file:<br>
          <strong>data/quiz_volume${App.currentVolume}.json</strong></p>
          <code>[
  {
    "chapter_id": ${this.chapterId},
    "questions": [
      {
        "type": "multiple_choice",
        "question": "＿＿ 是我的朋友。",
        "options": ["他", "她", "我", "你"],
        "answer": 0
      }
    ]
  }
]</code>
        </div>
      `;
      return;
    }

    this.questions = questions;
    this.index = 0;
    this.score = 0;
    this.answered = false;

    container.innerHTML = `
      <div class="quiz-header-bar">
        <span class="quiz-progress-text" id="quiz-progress-text">Soal 1 dari ${questions.length}</span>
        <span class="quiz-score-badge" id="quiz-score-badge">Skor: 0/0</span>
      </div>
      <div class="bar-track" style="margin-bottom:20px;">
        <div class="bar-fill" id="quiz-bar-fill" style="width:0%"></div>
      </div>
      <div id="quiz-question-area"></div>
    `;

    this.renderQuestion();
  }
};
