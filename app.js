// ═══════════════════════════════════════════════════════
// STATE
// ═══════════════════════════════════════════════════════
let state = {
  level: 'N1',
  tema: 1,
  mode: 'home',
  fc: { idx: 0, flipped: false, known: new Set() },
  score: { correct: 0, total: 0 },
  answered: {}
};

// ═══════════════════════════════════════════════════════
// RENDER HELPERS
// ═══════════════════════════════════════════════════════
const LEVEL_LABELS = { N1:'Novice 1 · A0', N2:'Novice 2 · A0', A1:'Level 1 · A1', A2:'Level 2 · A2' };

function setLevel(lv) {
  state.level = lv;
  state.tema = 1;
  state.fc = { idx:0, flipped:false, known:new Set() };
  state.score = { correct:0, total:0 };
  state.answered = {};
  document.querySelectorAll('.level-btn').forEach(b => b.className = 'level-btn');
  document.querySelector(`.level-btn[onclick="setLevel('${lv}')"]`).className = `level-btn active-${lv}`;
  document.getElementById('level-badge').className = `level-badge badge-${lv}`;
  document.getElementById('level-badge').textContent = LEVEL_LABELS[lv];
  buildTemaNav();
  render();
}

function setTema(id) {
  state.tema = id;
  state.fc = { idx:0, flipped:false, known:new Set() };
  state.answered = {};
  document.querySelectorAll('.tema-item').forEach(el => el.classList.remove('active'));
  document.getElementById(`tema-${id}`)?.classList.add('active');
  render();
}

function setMode(m) {
  state.mode = m;
  state.fc = { idx:0, flipped:false, known:new Set() };
  document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
  document.querySelector(`.mode-btn[onclick="setMode('${m}')"]`).classList.add('active');
  render();
}

function buildTemaNav() {
  const nav = document.getElementById('tema-nav');
  nav.innerHTML = TEMAS.map(t => `
    <div class="tema-item ${state.tema===t.id?'active':''}" id="tema-${t.id}" onclick="setTema(${t.id})">
      <span class="tema-num">${t.id}</span>
      <span class="tema-name">${t.name}<span class="tema-cn">${t.cn}</span></span>
    </div>`).join('');
}

function getMayerTags() {
  return `<div class="mayer-strip">
    <span class="mayer-tag" style="color:#7C3AED">Multimedia</span>
    <span class="mayer-tag" style="color:#0369A1">Modality</span>
    <span class="mayer-tag" style="color:#059669">Segmenting</span>
    <span class="mayer-tag" style="color:#B45309">Signaling</span>
    <span class="mayer-tag" style="color:#6B7280">Coherence</span>
    <span class="mayer-tag" style="color:#7C3AED">Spatial Contiguity</span>
    <span class="mayer-tag" style="color:#DC2626">Redundancy ↓</span>
  </div>`;
}

// ═══════════════════════════════════════════════════════
// RENDER MAIN
// ═══════════════════════════════════════════════════════
function render() {
  const tema = TEMAS.find(t => t.id === state.tema);
  document.getElementById('topbar-title').textContent = state.mode==='home' ? '華語TOCFL學習模組' : tema.name + ' · ' + tema.cn;
  document.getElementById('topbar-cn').textContent = {
    home: 'Mandarin Learning Module · Multimedia Learning (Mayer)',
    flashcard: 'Flashcard — Modality + Signaling',
    reading: 'Reading Text — Spatial Contiguity + Signaling',
    grammar: 'Grammar — Segmenting + Signaling',
    practice: 'TOCFL Practice — Coherence + Segmenting',
  }[state.mode];

  const area = document.getElementById('content-area');
  if (state.mode === 'home') { area.innerHTML = renderHome(); return; }
  if (state.mode === 'flashcard') { area.innerHTML = renderFlashcard(); bindFC(); return; }
  if (state.mode === 'reading') { area.innerHTML = renderReading(); bindReading(); return; }
  if (state.mode === 'grammar') { area.innerHTML = renderGrammar(); bindGrammar(); return; }
  if (state.mode === 'practice') { area.innerHTML = renderPractice(); return; }
}

// ═══ HOME ═══
function renderHome() {
  return `
  <div style="max-width:600px">
    ${getMayerTags()}
    <p style="color:var(--text2);font-size:14px;margin-bottom:24px;line-height:1.7">
      Welcome! Select a <b>Topic</b> from the left sidebar, then choose a learning module.<br>
      This app is designed based on Richard Mayer's <b>Multimedia Learning</b> principles.
    </p>
    <div class="welcome-grid">
      <div class="welcome-card" onclick="setMode('flashcard')">
        <div class="wc-icon">◈</div>
        <div class="wc-title">Flashcard</div>
        <div class="wc-desc">Learn vocabulary with flip cards. Audio + pinyin + meaning. Mark words you've mastered.</div>
      </div>
      <div class="welcome-card" onclick="setMode('reading')">
        <div class="wc-icon">▤</div>
        <div class="wc-title">Reading</div>
        <div class="wc-desc">Reading texts by topic. Click highlighted words to see pinyin & meaning.</div>
      </div>
      <div class="welcome-card" onclick="setMode('grammar')">
        <div class="wc-icon">◎</div>
        <div class="wc-title">Grammar</div>
        <div class="wc-desc">Sentence patterns + examples + fill-in-the-blank exercises. Key words highlighted.</div>
      </div>
      <div class="welcome-card" onclick="setMode('practice')">
        <div class="wc-icon">✎</div>
        <div class="wc-title">Practice</div>
        <div class="wc-desc">TOCFL-style multiple choice questions. Instant score + answer explanations.</div>
      </div>
    </div>
    <div style="margin-top:24px;padding:16px;background:var(--surface);border-radius:var(--radius);border:1px solid var(--border)">
      <div style="font-size:12px;font-weight:600;color:var(--text3);margin-bottom:8px;text-transform:uppercase;letter-spacing:.06em">Current Level</div>
      <div style="font-size:22px;font-weight:600;color:var(--accent)">${LEVEL_LABELS[state.level]}</div>
      <div style="font-size:13px;color:var(--text3);margin-top:4px">Active topic: ${TEMAS.find(t=>t.id===state.tema).name} · ${TEMAS.find(t=>t.id===state.tema).cn}</div>
    </div>
  </div>`;
}

// ═══ FLASHCARD ═══
function renderFlashcard() {
  const words = (VOCAB[state.level]||{})[state.tema] || [];
  if (!words.length) return `<div class="fc-container"><p style="color:var(--text3)">No vocabulary yet for this topic. Try another topic!</p></div>`;

  const { idx, flipped, known } = state.fc;
  const w = words[idx % words.length];
  const total = words.length;
  const pct = Math.round((idx/total)*100);

  return `
  <div class="fc-container">
    ${getMayerTags()}
    <div class="fc-counter">${idx+1} / ${total} words · ${known.size} mastered ✓</div>
    <div class="fc-progress-bar"><div class="fc-progress-fill" style="width:${pct}%"></div></div>

    <div class="card-scene" onclick="flipCard()">
      <div class="card-wrap ${flipped?'flipped':''}" id="card-wrap">
        <div class="card-face card-front">
          <button class="audio-btn" data-text="${w.w.split('/')[0]}" onclick="event.stopPropagation();speakWord('${w.w.split('/')[0]}')" title="Listen to pronunciation">🔊</button>
          <div class="card-char">${w.w.split('/')[0]}</div>
          <div class="card-hint">Click to reveal pinyin & meaning · 點擊翻轉</div>
        </div>
        <div class="card-face card-back">
          <button class="audio-btn" data-text="${w.w.split('/')[0]}" onclick="event.stopPropagation();speakWord('${w.w.split('/')[0]}')" title="Listen to pronunciation">🔊</button>
          <div class="card-pinyin">${w.p}</div>
          <div class="card-char" style="font-size:48px">${w.w.split('/')[0]}</div>
          <div class="card-meaning">${w.m || '—'}</div>
          <div class="card-pos">${w.pos}</div>
        </div>
      </div>
    </div>

    <div class="fc-controls">
      <button class="fc-btn" onclick="prevCard()">← Previous</button>
      <button class="fc-btn skip" onclick="nextCard(false)">Skip ✕</button>
      <button class="fc-btn know" onclick="nextCard(true)">Know ✓</button>
    </div>

    <div class="vocab-list">
      <div class="vocab-list-title">All vocabulary for this topic (${total} words)</div>
      <div class="vocab-grid">
        ${words.map((wd,i) => `
          <div class="vocab-chip ${state.fc.known.has(i)?'known':''}" onclick="jumpCard(${i})">
            <span class="vc-char">${wd.w.split('/')[0]}</span>
            <span class="vc-pinyin">${wd.p}</span>
            <span class="vc-meaning">${wd.m||'—'}</span>
          </div>`).join('')}
      </div>
    </div>
  </div>`;
}

function bindFC() {}
function flipCard() {
  state.fc.flipped = !state.fc.flipped;
  const cw = document.getElementById('card-wrap');
  if (cw) cw.classList.toggle('flipped', state.fc.flipped);
}
function nextCard(know) {
  const words = (VOCAB[state.level]||{})[state.tema] || [];
  if (know) state.fc.known.add(state.fc.idx);
  state.fc.idx = (state.fc.idx + 1) % words.length;
  state.fc.flipped = false;
  render();
}
function prevCard() {
  const words = (VOCAB[state.level]||{})[state.tema] || [];
  state.fc.idx = (state.fc.idx - 1 + words.length) % words.length;
  state.fc.flipped = false;
  render();
}
function jumpCard(i) {
  state.fc.idx = i;
  state.fc.flipped = false;
  render();
}

// ═══════════════════════════════════════════════════════
// AUDIO ENGINE — low-latency TTS
// ═══════════════════════════════════════════════════════
let _ttsVoice  = null;
let _ttsReady  = false;
let _ttsToken  = 0;   // supersede old utterances without cancel()

function _initTTS() {
  if (!('speechSynthesis' in window)) return;

  function pickVoice() {
    const all = speechSynthesis.getVoices();
    if (!all.length) return false;
    const priority = ['zh-TW','zh_TW','zh-TW-Wavenet','zh','zh-CN','zh_CN'];
    for (const lang of priority) {
      const v = all.find(v => v.lang.toLowerCase().startsWith(lang.toLowerCase()));
      if (v) { _ttsVoice = v; _ttsReady = true; _setAudioStatus(true); return true; }
    }
    const fallback = all.find(v => v.lang.toLowerCase().includes('zh'));
    if (fallback) { _ttsVoice = fallback; _ttsReady = true; _setAudioStatus(true); return true; }
    _setAudioStatus(false);
    return false;
  }

  if (!pickVoice()) {
    speechSynthesis.addEventListener('voiceschanged', () => {
      if (pickVoice()) { _warmUp(); _startKeepAlive(); }
    }, { once: true });
  } else {
    _warmUp();
    _startKeepAlive();
  }
}

// Speak a zero-width-space silently to keep engine warm
function _silentPing() {
  if (!('speechSynthesis' in window) || !_ttsReady) return;
  const u = new SpeechSynthesisUtterance('​');
  u.volume = 0;
  u.lang = 'zh-TW';
  if (_ttsVoice) u.voice = _ttsVoice;
  speechSynthesis.speak(u);
}

function _warmUp() {
  if (!('speechSynthesis' in window)) return;
  _silentPing();
}

// Chrome pauses SpeechSynthesis after ~14 s of silence — keep it alive
function _startKeepAlive() {
  setInterval(() => {
    if (!speechSynthesis.speaking && !speechSynthesis.pending) _silentPing();
    // Also kick Chrome if it got stuck in a paused state
    if (speechSynthesis.paused) speechSynthesis.resume();
  }, 10000);
}

// Pre-warm on hover so the engine is never cold when user clicks
document.addEventListener('mouseover', (e) => {
  const btn = e.target.closest('.audio-btn');
  if (btn && !speechSynthesis.speaking && !speechSynthesis.pending) _silentPing();
}, { passive: true });

function _speak(text, rate = 0.85) {
  if (!('speechSynthesis' in window)) return;

  const myToken = ++_ttsToken;

  function _go() {
    if (myToken !== _ttsToken) return; // a newer call superseded this one
    const u = new SpeechSynthesisUtterance(text);
    u.lang   = 'zh-TW';
    u.rate   = rate;
    u.pitch  = 1;
    u.volume = 1;
    if (_ttsVoice) u.voice = _ttsVoice;
    u.onstart = () => { if (myToken === _ttsToken) _setAudioBtnState(text, 'playing'); };
    u.onend   = () => { if (myToken === _ttsToken) _setAudioBtnState(text, 'idle'); };
    u.onerror = (e) => { if (e.error !== 'interrupted' && myToken === _ttsToken) _setAudioBtnState(text, 'idle'); };
    speechSynthesis.speak(u);
  }

  if (speechSynthesis.speaking) {
    // Cancel current and give the engine a single minimal tick to settle
    speechSynthesis.cancel();
    setTimeout(_go, 30);
  } else {
    if (!_ttsReady) {
      // Voice not ready yet — try once more then speak anyway
      const all = speechSynthesis.getVoices();
      const v = all.find(v => v.lang.toLowerCase().includes('zh'));
      if (v) { _ttsVoice = v; _ttsReady = true; }
    }
    _go();
  }
}

function _setAudioStatus(ready) {
  const dot = document.getElementById('audio-dot');
  const lbl = document.getElementById('audio-label');
  if (!dot || !lbl) return;
  if (ready) {
    dot.style.background = '#22C55E';
    lbl.textContent = 'Audio ready · ' + (_ttsVoice ? _ttsVoice.lang : 'zh-TW');
  } else {
    dot.style.background = '#F59E0B';
    lbl.textContent = 'Audio unavailable';
  }
}

function _setAudioBtnState(text, st) {
  document.querySelectorAll('.audio-btn').forEach(btn => {
    if (btn.dataset.text === text) {
      btn.textContent = st === 'playing' ? '⏹' : '🔊';
      btn.style.background = st === 'playing' ? 'var(--accent)' : '';
      btn.style.color = st === 'playing' ? '#fff' : '';
    }
  });
}

// Public API
function speakWord(text) { _speak(text, 0.82); }
function speakText() {
  const body = document.getElementById('reading-body');
  if (body) _speak(body.textContent, 0.78);
}
function speakQ(qi) {
  const qs = PRACTICE_QS[state.level] || PRACTICE_QS['N1'];
  _speak(qs[qi]?.q || '', 0.78);
}

_initTTS();

// ═══ READING ═══
function renderReading() {
  const reading = (READINGS[state.level]||{})[state.tema];
  if (!reading) return `
    <div class="reading-container">
      ${getMayerTags()}
      <div class="reading-card">
        <div class="reading-label">課文 Reading Text</div>
        <div class="reading-title">No reading for this topic yet</div>
        <div class="reading-sub">Content coming soon — try another topic or level</div>
        <div style="color:var(--text3);font-size:14px">Each topic will have a full reading text in a future update.</div>
      </div>
    </div>`;

  const bodyHtml = reading.body.replace(/<kw w="([^"]+)" p="([^"]+)" m="([^"]+)">([^<]+)<\/kw>/g,
    (_, w, p, m, char) => `<span class="kw" data-w="${w}" data-p="${p}" data-m="${m}" onmouseenter="showTip(event,'${w}','${p}','${m}')" onmouseleave="hideTip()">${char}</span>`
  );

  const qsHtml = reading.qs.map((q,qi) => `
    <div class="rq-item">
      <div class="rq-q">${qi+1}. ${q.q}</div>
      <div class="rq-options">
        ${q.opts.map((opt,oi) => `<button class="rq-opt" id="rq-${qi}-${oi}" onclick="answerRQ(${qi},${oi},${q.ans})">${opt}</button>`).join('')}
      </div>
    </div>`).join('');

  return `
  <div class="reading-container">
    ${getMayerTags()}
    <div class="reading-card" style="position:relative">
      <div class="reading-label">📖 課文 · Reading Text
        <button onclick="speakText()" style="padding:4px 10px;border-radius:99px;border:1px solid var(--border);background:var(--surface2);font-size:11px;cursor:pointer;color:var(--text2)">🔊 Listen</button>
      </div>
      <div class="reading-title">${reading.title}</div>
      <div class="reading-sub">${reading.titleEn}</div>
      <div class="reading-body" id="reading-body">${bodyHtml}</div>
      <div style="margin-top:16px;padding:10px 12px;background:var(--surface2);border-radius:var(--radius-sm);font-size:12px;color:var(--text3)">
        💡 Mayer principles applied: ${reading.notes}
      </div>
    </div>
    <div class="reading-qs">
      <div class="rq-title">Comprehension Questions · 閱讀理解</div>
      ${qsHtml}
    </div>
  </div>`;
}

function bindReading() {}
function showTip(e, w, p, m) {
  const tt = document.getElementById('tooltip');
  document.getElementById('tt-char').textContent = w;
  document.getElementById('tt-pinyin').textContent = p;
  document.getElementById('tt-meaning').textContent = m;
  tt.style.left = (e.pageX+10)+'px';
  tt.style.top = (e.pageY-40)+'px';
  tt.classList.add('show');
}
function hideTip() { document.getElementById('tooltip').classList.remove('show'); }
function answerRQ(qi, oi, ans) {
  document.querySelectorAll(`[id^="rq-${qi}-"]`).forEach(b => b.disabled = true);
  document.getElementById(`rq-${qi}-${oi}`).classList.add(oi===ans?'correct':'wrong');
  if (oi===ans) document.getElementById(`rq-${qi}-${ans}`).classList.add('correct');
  else document.getElementById(`rq-${qi}-${ans}`).classList.add('correct');
}

// ═══ GRAMMAR ═══
function renderGrammar() {
  const gps = GRAMMAR[state.level] || GRAMMAR['N1'];
  return `
  <div class="grammar-container">
    ${getMayerTags()}
    ${gps.map((g,gi) => `
      <div class="grammar-card">
        <div class="grammar-num">Grammar Point ${gi+1} · 語法點</div>
        <div class="grammar-title">${g.title}</div>
        <div class="grammar-title-en">${g.titleEn}</div>
        <div class="grammar-pattern">${g.pattern}</div>
        <ul class="grammar-examples">
          ${g.examples.map(ex => `
            <li>
              <span style="font-size:16px">${ex.zh.replace(/<mark>([^<]+)<\/mark>/g,'<span class="highlight-word">$1</span>')}</span>
              <span class="eg-cn">${ex.en}${ex.note?' · '+ex.note:''}</span>
            </li>`).join('')}
        </ul>
        <div class="fill-blank">
          <div class="fill-blank-title">✎ Fill in the Blank</div>
          ${g.fills.map((f,fi) => `
            <div class="fill-q">
              ${f.q.replace('___',`<input class="fill-input" id="fi-${gi}-${fi}" placeholder="___" oninput="checkFill(${gi},${fi},'${f.ans}')">`)}
            </div>`).join('')}
          <button class="check-btn" onclick="checkAllFills(${gi})">Check Answers</button>
        </div>
      </div>`).join('')}
  </div>`;
}
function bindGrammar() {}
function checkFill(gi, fi, ans) {
  const inp = document.getElementById(`fi-${gi}-${fi}`);
  if (!inp) return;
  const val = inp.value.trim();
  if (val === ans) inp.classList.add('correct');
  else { inp.classList.remove('correct'); inp.classList.add('wrong'); }
}
function checkAllFills(gi) {
  const gps = GRAMMAR[state.level] || GRAMMAR['N1'];
  const g = gps[gi];
  g.fills.forEach((f,fi) => checkFill(gi, fi, f.ans));
}

// ═══ PRACTICE ═══
function renderPractice() {
  const qs = PRACTICE_QS[state.level] || PRACTICE_QS['N1'];
  return `
  <div class="practice-container">
    ${getMayerTags()}
    <div class="practice-header">
      <div>
        <div style="font-size:14px;font-weight:500">TOCFL Practice Questions · 練習題</div>
        <div style="font-size:12px;color:var(--text3);margin-top:2px">${LEVEL_LABELS[state.level]} — ${qs.length} questions</div>
      </div>
      <div class="practice-score">
        <div class="score-num" id="score-display">0/${qs.length}</div>
        <div class="score-label">Correct</div>
      </div>
    </div>
    ${qs.map((q,qi) => `
      <div class="q-card" id="qcard-${qi}">
        <div class="q-type">
          <span>Question ${qi+1}</span>
          <span class="q-type-badge ${q.type==='listening'?'listening-badge':'reading-badge'}">${q.type==='listening'?'Listening 聽力':'Reading 閱讀'}</span>
        </div>
        ${q.type==='listening'?`<button class="q-audio-btn" onclick="speakQ(${qi})">🔊 Listen to Question</button>`:''}
        <div class="q-text" id="qtext-${qi}" style="white-space:pre-wrap">${q.q}</div>
        <div class="q-options">
          ${q.opts.map((opt,oi) => `
            <button class="q-opt" id="qopt-${qi}-${oi}" onclick="answerQ(${qi},${oi},${q.ans},'${q.exp.replace(/'/g,"\\'")}')">
              ${String.fromCharCode(65+oi)}. ${opt}
            </button>`).join('')}
        </div>
        <div class="explanation" id="exp-${qi}"></div>
      </div>`).join('')}
  </div>`;
}

let practiceScore = 0;
function answerQ(qi, oi, ans, exp) {
  const qs = PRACTICE_QS[state.level] || PRACTICE_QS['N1'];
  if (state.answered[qi] !== undefined) return;
  state.answered[qi] = oi;
  document.querySelectorAll(`[id^="qopt-${qi}-"]`).forEach(b => b.disabled = true);
  document.getElementById(`qopt-${qi}-${oi}`).classList.add(oi===ans?'correct':'wrong');
  if (oi !== ans) document.getElementById(`qopt-${qi}-${ans}`).classList.add('correct');
  const expEl = document.getElementById(`exp-${qi}`);
  expEl.textContent = '💡 ' + exp;
  expEl.classList.add('show');
  if (oi === ans) { state.score.correct++; }
  state.score.total++;
  document.getElementById('score-display').textContent = `${state.score.correct}/${qs.length}`;
}

// ═══════════════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════════════
buildTemaNav();
render();
