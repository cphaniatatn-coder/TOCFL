const Reading = {
  chapterId: null,
  data: null,
  answers: {},

  init(chapterId) {
    this.chapterId = chapterId;
    this.answers = {};
    this.render();
  },

  loadData() {
    const chapter = App.data?.chapters?.find(c => c.id === this.chapterId);
    if (!chapter) return null;
    const readings = [];
    for (const part of ['A', 'B']) {
      const r = chapter.parts[part]?.reading;
      if (r) readings.push({ part, ...r });
    }
    return readings.length ? readings : null;
  },

  answer(qIndex, optionIndex, correctIndex) {
    if (this.answers[qIndex] !== undefined) return;
    this.answers[qIndex] = optionIndex;

    const opts = document.querySelectorAll(`[data-q="${qIndex}"] .option-btn`);
    opts.forEach((btn, i) => {
      btn.disabled = true;
      if (i === correctIndex) btn.classList.add('correct');
      else if (i === optionIndex) btn.classList.add('wrong');
    });

    const progress = App.getProgress(this.chapterId);
    if (!progress.reading) progress.reading = {};
    progress.reading.answered = (progress.reading.answered || 0) + 1;
    if (optionIndex === correctIndex) {
      progress.reading.correct = (progress.reading.correct || 0) + 1;
    }
    App.saveProgress(this.chapterId, progress);
  },

  render() {
    const container = document.getElementById('tab-reading');
    const readings = this.loadData();

    if (!readings || readings.length === 0) {
      container.innerHTML = `
        <div class="reading-area">
          <div class="placeholder-box">
            <div class="placeholder-icon">📖</div>
            <h3>Teks bacaan belum tersedia</h3>
            <p>Tambahkan data reading pada chapter ini di file volume JSON.</p>
          </div>
        </div>
      `;
      return;
    }

    container.innerHTML = `<div class="reading-area" id="reading-content"></div>`;
    const content = document.getElementById('reading-content');

    readings.forEach((section, si) => {
      const passageEl = document.createElement('div');
      passageEl.className = 'reading-passage';
      const htmlText = section.text.replace(/\n\n/g, '</p><p>').replace(/\n/g, '<br>');
      passageEl.innerHTML = `<div class="reading-title">${section.title || 'Teks Bacaan'}</div><p>${htmlText}</p>`;
      content.appendChild(passageEl);

      if (section.questions?.length) {
        const qContainer = document.createElement('div');
        qContainer.className = 'reading-questions';
        section.questions.forEach((q, qi) => {
          const idx = `${si}_${qi}`;
          const letters = ['A', 'B', 'C', 'D'];
          qContainer.innerHTML += `
            <div class="question-card" data-q="${idx}">
              <div class="question-num">Pertanyaan ${qi + 1}</div>
              <div class="question-text">${q.question}</div>
              <div class="option-list">
                ${q.options.map((opt, oi) => `
                  <button class="option-btn" onclick="Reading.answer('${idx}', ${oi}, ${q.answer})">
                    <span class="option-letter">${letters[oi]}</span>
                    <span>${opt}</span>
                  </button>
                `).join('')}
              </div>
            </div>
          `;
        });
        content.appendChild(qContainer);
      }
    });
  }
};
