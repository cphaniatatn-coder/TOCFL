/* Tampilan satu modul, tahap demi tahap.
   A0 (vocabulary-first): 情境導入 → 詞彙 → 情境對話 → 練習 → 語法小提示 → 反思
   A1/A2 (TBLL Willis):   情境導入 → 情境對話 → 詞彙 → 溝通任務 → 語法聚焦 → 反思
   Grammar selalu SESUDAH tugas (bukan PPP). */

/* ===== Audio: mp3 di audio/ bila ada, selain itu TTS zh-TW ===== */
let _zhVoice = null;
const _audioCache = {};
if (window.speechSynthesis) {
  const pick = () => {
    const vs = speechSynthesis.getVoices();
    _zhVoice = vs.find(v => v.lang === 'zh-TW' && /hsiaoc|hsiaoyu|xiaoc|xiaoyu/i.test(v.name))
      || vs.find(v => v.lang === 'zh-TW' && /online|natural|neural/i.test(v.name))
      || vs.find(v => v.lang === 'zh-TW') || vs.find(v => v.lang.startsWith('zh')) || null;
  };
  pick();
  speechSynthesis.addEventListener('voiceschanged', pick);
}

const Speech = {
  utter(text, pitch = 1) {
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'zh-TW'; u.rate = 0.85; u.pitch = pitch;
    if (_zhVoice) u.voice = _zhVoice;
    return u;
  },
  // Kata tunggal: coba rekaman mp3 dulu (audio/<kata>.mp3)
  word(text) {
    const url = `audio/${encodeURIComponent(text.replace(/\//g, '／'))}.mp3`;
    if (!_audioCache[url]) _audioCache[url] = new Audio(url);
    const a = _audioCache[url];
    a.currentTime = 0;
    a.play().catch(() => this.say(text));
  },
  say(text) {
    if (!window.speechSynthesis) return App.showToast('Browser ini tidak mendukung suara.');
    speechSynthesis.cancel();
    speechSynthesis.speak(this.utter(text));
  },
  // Dialog: baris berurutan; suara 男/女 dibedakan lewat pitch
  lines(lines) {
    if (!window.speechSynthesis) return App.showToast('Browser ini tidak mendukung suara.');
    speechSynthesis.cancel();
    lines.forEach(l => speechSynthesis.speak(this.utter(l.zh, l.sp === '女' ? 1.25 : l.sp === '男' ? 0.8 : 1)));
  },
};

const STAGES = {
  A0: [
    { key: 'intro', zh: '情境導入', id: 'Tujuan' },
    { key: 'vocab', zh: '詞彙', id: 'Kosakata' },
    { key: 'dialog', zh: '情境對話', id: 'Dialog' },
    { key: 'tasks', zh: '練習', id: 'Latihan TOCFL' },
    { key: 'grammar', zh: '語法小提示', id: 'Tata bahasa' },
    { key: 'reflect', zh: '反思與進度', id: 'Refleksi' },
  ],
  TBLL: [
    { key: 'intro', zh: '情境導入', id: 'Tujuan' },
    { key: 'dialog', zh: '情境對話', id: 'Dialog' },
    { key: 'vocab', zh: '詞彙', id: 'Kosakata' },
    { key: 'tasks', zh: '溝通任務', id: 'Tugas TOCFL' },
    { key: 'grammar', zh: '語法聚焦', id: 'Balok grammar' },
    { key: 'reflect', zh: '反思與進度', id: 'Refleksi' },
  ],
};

const Modul = {
  vol: null, m: null, stage: 0,
  showPy: false, showZy: true,
  answers: {},   // jawaban tugas sesi ini: {taskIndex: pilihan | [pilihan per titik]}

  stages() { return STAGES[App.volData[this.vol].approach === 'A0' ? 'A0' : 'TBLL']; },

  open(vol, code) {
    this.vol = vol;
    this.m = App.moduleContent(vol, code);
    const p = App.getP(code);
    this.stage = Math.min(p.stage || 0, 5);
    this.answers = {};
    this.render();
  },

  go(i) {
    this.stage = Math.max(0, Math.min(5, i));
    const p = App.getP(this.m.code);
    App.setP(this.m.code, { stage: Math.max(p.stage || 0, this.stage) });
    if (window.speechSynthesis) speechSynthesis.cancel();
    this.render();
  },

  render() {
    const m = this.m, st = this.stages(), cur = st[this.stage];
    const reached = App.getP(m.code).stage || 0;
    App.crumbs([['Pilih Volume', 'App.renderVolumes()'], [`Volume ${this.vol}`, 'App.renderDashboard()'], [m.code]]);
    App.main(`
      <div class="mod-head">
        <div class="mod-code">${m.code} · ${m.categories.map(esc).join(' · ')}</div>
        <h2 lang="zh-TW">${esc(m.title)} <button class="btn-audio" onclick="Speech.say(Modul.m.title)" aria-label="Dengarkan judul">🔊</button></h2>
        <div class="mod-sub">${esc(m.title_py)} — <em>${esc(m.title_id)}</em></div>
      </div>
      <ol class="stepper">
        ${st.map((s, i) => `
          <li class="${i === this.stage ? 'cur' : ''}${i <= reached ? ' seen' : ''}">
            <button onclick="Modul.go(${i})"><span class="step-n">${i + 1}</span><span class="step-zh" lang="zh-TW">${s.zh}</span><span class="step-id">${s.id}</span></button>
          </li>`).join('')}
      </ol>
      <section class="stage stage-${cur.key}">${this['r_' + cur.key]()}</section>
      <div class="stage-nav">
        ${this.stage > 0 ? `<button class="btn btn-outline" onclick="Modul.go(${this.stage - 1})">← ${st[this.stage - 1].id}</button>` : '<span></span>'}
        ${this.stage < 5 ? `<button class="btn btn-primary" onclick="Modul.next()">${st[this.stage + 1].id} →</button>` : ''}
      </div>`);
  },

  next() {
    if (this.st_key() === 'intro') this.saveGoal();
    this.go(this.stage + 1);
  },
  st_key() { return this.stages()[this.stage].key; },

  /* ---------- 1. 情境導入: situasi + tujuan eksplisit (GDL) + target pribadi (SRL forethought) ---------- */
  r_intro() {
    const m = this.m, p = App.getP(m.code);
    return `
      <div class="panel scene-panel"><div class="panel-label">Situasi</div><p>${esc(m.scene)}</p></div>
      <div class="panel">
        <div class="panel-label">Setelah modul ini, kamu bisa…</div>
        <ul class="cando">${m.can_do.map(c => `<li>${esc(c)}</li>`).join('')}</ul>
      </div>
      <div class="panel exam-panel"><div class="panel-label">Kenapa ini penting untuk ujian?</div><p>${esc(m.exam_link)}</p></div>
      <label class="field-label" for="goal-input">Target pribadimu untuk modul ini</label>
      <textarea id="goal-input" rows="2" placeholder="Contoh: aku mau bisa menjawab 您貴姓 tanpa berpikir lama…">${esc(p.goal || '')}</textarea>
      <p class="hint">Kamu boleh melompat ke tahap mana pun lewat penanda di atas — atur sendiri langkah belajarmu.</p>`;
  },
  saveGoal() {
    const el = document.getElementById('goal-input');
    if (el) App.setP(this.m.code, { goal: el.value.trim() });
  },

  /* ---------- 詞彙: dua lapis 核心 / 補充 ---------- */
  hanzi(w, zy) {
    if (!this.showZy || !zy) return `<span class="hz">${esc(w)}</span>`;
    const marks = zy.split(/\s+/);
    return [...w].map((c, i) => `<span class="zy-unit"><span class="zy-hanzi">${c}</span><span class="zy-mark">${marks[i] || ''}</span></span>`).join('');
  },
  wordCard(v, layer) {
    return `
      <div class="word-card ${layer}">
        <button class="btn-audio" onclick="Speech.word('${esc(v.w)}')" aria-label="Dengarkan ${esc(v.w)}">🔊</button>
        <div class="word-hz" lang="zh-TW">${this.hanzi(v.w, v.zy)}</div>
        <div class="word-py">${esc(v.py)}</div>
        <div class="word-mean"><span class="pos">${esc(v.pos)}</span> ${esc(v.meaning)}</div>
        ${v.note ? `<div class="word-note">義項: ${esc(v.note)}</div>` : ''}
      </div>`;
  },
  r_vocab() {
    const { core, supplement } = this.m.vocab;
    return `
      <div class="toolbar">
        <button class="chip-toggle${this.showZy ? ' on' : ''}" onclick="Modul.showZy=!Modul.showZy; Modul.render()">注音 ${this.showZy ? 'ON' : 'OFF'}</button>
      </div>
      <h3 class="layer-title">核心 · Kata inti <small>— untuk DIPAKAI saat bicara & menulis (${core.length})</small></h3>
      <div class="word-grid">${core.map(v => this.wordCard(v, 'core')).join('')}</div>
      ${supplement.length ? `
      <h3 class="layer-title sup">補充 · Kata pelengkap <small>— cukup DIKENALI saat membaca/mendengar (${supplement.length})</small></h3>
      <div class="word-grid">${supplement.map(v => this.wordCard(v, 'sup')).join('')}</div>` : ''}`;
  },

  /* ---------- 情境對話 ---------- */
  r_dialog() {
    return `
      <div class="toolbar">
        <button class="chip-toggle${this.showPy ? ' on' : ''}" onclick="Modul.showPy=!Modul.showPy; Modul.render()">拼音 ${this.showPy ? 'ON' : 'OFF'}</button>
        <span class="hint">Ketuk ▸ di tiap baris untuk melihat artinya — coba pahami dulu tanpa terjemahan.</span>
      </div>
      ${this.m.dialogs.map((d, di) => `
        <div class="dialog-box">
          <div class="dialog-head">
            <div><span lang="zh-TW">${esc(d.place)}</span> <small>${esc(d.title_id)}</small></div>
            <button class="btn btn-outline btn-sm" onclick="Speech.lines(Modul.m.dialogs[${di}].lines)">▶ Putar dialog</button>
          </div>
          ${d.lines.map((l, li) => `
            <div class="dl-line">
              <div class="dl-sp" lang="zh-TW">${esc(l.sp)}</div>
              <div class="dl-body">
                <div class="dl-zh" lang="zh-TW">${esc(l.zh)} <button class="btn-audio sm" onclick="Speech.say(Modul.m.dialogs[${di}].lines[${li}].zh)" aria-label="Dengarkan">🔊</button></div>
                ${this.showPy ? `<div class="dl-py">${esc(l.py)}</div>` : ''}
                <details class="dl-id"><summary>arti</summary>${esc(l.id)}</details>
              </div>
            </div>`).join('')}
        </div>`).join('')}`;
  },

  /* ---------- 溝通任務 / 練習: format TOCFL Band A, nomor berlanjut ---------- */
  r_tasks() {
    const t = this.m.tasks;
    const done = t.every((_, i) => this.isAnswered(i));
    return `
      <p class="hint">Soal mengikuti format resmi TOCFL Band A. Untuk soal 聽力, dengarkan dulu — teksnya baru muncul setelah kamu menjawab.</p>
      ${t.map((task, i) => this.renderTask(task, i)).join('')}
      ${done ? this.scoreBox() : ''}`;
  },
  isAnswered(i) {
    const a = this.answers[i], t = this.m.tasks[i];
    return t.type === 'cloze' ? Array.isArray(a) && a.checked : a != null;
  },
  renderTask(t, i) {
    const n = i + 1, ans = this.answers[i], answered = this.isAnswered(i);
    let body = '';
    const isListen = t.type.startsWith('listen');
    if (isListen) {
      const play = t.lines ? `Speech.lines(Modul.m.tasks[${i}].lines)` : `Speech.say(Modul.m.tasks[${i}].audio)`;
      body += `<button class="btn btn-outline btn-sm play-btn" onclick="${play}">▶ Dengarkan</button>`;
      if (answered) {
        const tr = t.lines ? t.lines.map(l => `${esc(l.sp)}：${esc(l.zh)}`).join('<br>') : esc(t.audio);
        body += `<div class="transcript" lang="zh-TW">${tr}</div>`;
      }
      if (t.question) body += `<div class="task-q" lang="zh-TW">問：${esc(t.question)}</div>`;
    }
    if (t.type === 'read_pick') body += `<div class="task-picture" title="${esc(t.picture.label)}">${t.picture.icon}<small>${esc(t.picture.label)}</small></div>`;
    if (t.type === 'read_mc') body += `<div class="task-text" lang="zh-TW">${esc(t.text)}</div><div class="task-q" lang="zh-TW">問：${esc(t.question)}</div>`;

    if (t.type === 'cloze') {
      body += this.renderCloze(t, i);
    } else {
      const L = 'ABCD';
      body += `<div class="opts${t.type === 'listen_pick' ? ' opts-pic' : ''}">${t.options.map((o, oi) => {
        const cls = answered ? (oi === t.answer ? ' right' : oi === ans ? ' wrong' : '') : '';
        const label = typeof o === 'string' ? `<span lang="zh-TW">${esc(o)}</span>` : `<span class="pic">${o.icon}</span><small>${esc(o.label)}</small>`;
        return `<button class="opt${cls}" ${answered ? 'disabled' : `onclick="Modul.pick(${i}, ${oi})"`}><b>${L[oi]}</b>${label}</button>`;
      }).join('')}</div>`;
    }
    if (answered) {
      const ok = t.type === 'cloze' ? ans.every((a, k) => a === t.answers[k]) : ans === t.answer;
      body += `<div class="feedback ${ok ? 'ok' : 'no'}"><b>${ok ? 'Tepat!' : 'Belum tepat.'}</b> ${esc(t.why)}</div>`;
    }
    return `<div class="task"><div class="task-head"><span class="task-n">${n}</span><span class="task-part" lang="zh-TW">${esc(t.part)}</span></div>
      <div class="task-instr">${esc(t.instr)}</div>${body}</div>`;
  },
  renderCloze(t, i) {
    const a = this.answers[i] || [];
    const checked = a.checked;
    const L = 'ABCDEF';
    let k = -1;
    const text = esc(t.text).replace(/（(\d)）/g, () => {
      k++;
      const sel = a[k];
      const cls = checked ? (sel === t.answers[k] ? 'right' : 'wrong') : '';
      return `<select class="blank ${cls}" ${checked ? 'disabled' : ''} onchange="Modul.fill(${i}, ${k}, this.value)" aria-label="Titik ${k + 1}">
        <option value="">(${k + 1})</option>${t.options.map((o, oi) => `<option value="${oi}"${sel === oi ? ' selected' : ''}>${L[oi]}. ${esc(o)}</option>`).join('')}
      </select>${checked && sel !== t.answers[k] ? `<span class="fix">${esc(t.options[t.answers[k]])}</span>` : ''}`;
    });
    return `<div class="cloze-opts" lang="zh-TW">${t.options.map((o, oi) => `<span><b>${L[oi]}</b> ${esc(o)}</span>`).join('')}</div>
      <div class="task-text cloze" lang="zh-TW">${text}</div>
      ${checked ? '' : `<button class="btn btn-primary btn-sm" onclick="Modul.checkCloze(${i})">Periksa</button>`}`;
  },
  pick(i, oi) { this.answers[i] = oi; this.afterAnswer(); },
  fill(i, k, v) {
    const a = this.answers[i] || [];
    a[k] = v === '' ? undefined : Number(v);
    this.answers[i] = a;
  },
  checkCloze(i) {
    const a = this.answers[i] || [], t = this.m.tasks[i];
    if (t.answers.some((_, k) => a[k] == null)) return App.showToast('Isi semua titik kosong dulu.');
    a.checked = true;
    this.answers[i] = a;
    this.afterAnswer();
  },
  // Skor dihitung per butir (tiap titik cloze = 1 butir)
  score() {
    let got = 0, tot = 0;
    this.m.tasks.forEach((t, i) => {
      const a = this.answers[i];
      if (t.type === 'cloze') { t.answers.forEach((x, k) => { tot++; if (a && a[k] === x) got++; }); }
      else { tot++; if (a === t.answer) got++; }
    });
    return Math.round(got / tot * 100);
  },
  afterAnswer() {
    const y = window.scrollY;
    if (this.m.tasks.every((_, i) => this.isAnswered(i))) {
      const s = this.score(), p = App.getP(this.m.code);
      App.setP(this.m.code, { tasks: { last: s, best: Math.max(s, p.tasks?.best ?? 0), tries: (p.tasks?.tries || 0) + 1 } });
    }
    this.render();
    window.scrollTo(0, y);
  },
  // Umpan balik berorientasi mastery (GOL): proses & langkah berikutnya, bukan sekadar angka
  scoreBox() {
    const s = this.score(), p = App.getP(this.m.code);
    const msg = s >= 80 ? 'Kamu sudah menguasai tugas di adegan ini. Lanjutkan ke balok grammar untuk merapikan polanya.'
      : s >= 60 ? 'Hampir! Baca lagi penjelasan di soal yang belum tepat — pola kesalahannya biasanya sama.'
      : 'Belum — dan itu wajar di percobaan awal. Ulangi dialog (tahap sebelumnya) lalu coba lagi; skor terbaikmu tetap tersimpan.';
    return `<div class="score-box ${s >= 80 ? 'hi' : s >= 60 ? 'mid' : 'lo'}">
      <div class="score-num">${s}%</div>
      <div><p>${msg}</p><small>Percobaan ke-${p.tasks?.tries || 1} · skor terbaik ${p.tasks?.best ?? s}%</small></div>
      <button class="btn btn-outline btn-sm" onclick="Modul.answers={}; Modul.render()">Coba lagi</button>
    </div>`;
  },

  /* ---------- 語法: balok Lego, sesudah tugas ---------- */
  r_grammar() {
    const gc = App.getP(this.m.code).gchecks || {};
    if (!this.m.grammar.length) return `
      <div class="panel"><div class="panel-label">Tidak ada pola baru di adegan ini</div>
        <p>Adegan ini sengaja hanya menambah kosakata. Pola yang kamu pakai ulang di dialog & tugas:</p>
        <ul class="examples">${(this.m.recycle || []).map(r => `<li><span lang="zh-TW">${esc(r.zh)}</span><small>${esc(r.id)}</small></li>`).join('')}</ul>
      </div>`;
    return `
      <p class="hint">Pola di bawah ini sudah kamu pakai di dialog & tugas. Sekarang kita bongkar susunan baloknya.</p>
      ${this.m.grammar.map((g, gi) => `
        <div class="gram-card">
          <div class="gram-head"><span class="gram-id">TBCL #${g.tbcl_id}</span><h3 lang="zh-TW">${esc(g.point)}</h3></div>
          <div class="blocks" lang="zh-TW">${g.blocks.map(([w, role]) => `<span class="block role-${esc(role)}"><b>${esc(w)}</b><small>${esc(role)}</small></span>`).join('<span class="plus">+</span>')}</div>
          <div class="pattern">Pola: <code lang="zh-TW">${esc(g.pattern)}</code></div>
          <p>${esc(g.explain)}</p>
          <ul class="examples">${g.examples.map((e, ei) => `<li><span lang="zh-TW">${esc(e.zh)}</span> <button class="btn-audio sm" onclick="Speech.say(Modul.m.grammar[${gi}].examples[${ei}].zh)" aria-label="Dengarkan">🔊</button><small>${esc(e.id)}</small></li>`).join('')}</ul>
          <div class="gcheck">
            <div class="gcheck-q">Cek cepat: <span lang="zh-TW">${esc(g.check.q)}</span></div>
            <div class="opts">${g.check.options.map((o, oi) => {
              const a = gc[gi];
              const cls = a != null ? (oi === g.check.answer ? ' right' : oi === a ? ' wrong' : '') : '';
              return `<button class="opt${cls}" ${a != null ? 'disabled' : `onclick="Modul.gcheck(${gi}, ${oi})"`}><span lang="zh-TW">${esc(o)}</span></button>`;
            }).join('')}</div>
          </div>
        </div>`).join('')}`;
  },
  gcheck(gi, oi) {
    const gc = App.getP(this.m.code).gchecks || {};
    gc[gi] = oi;
    App.setP(this.m.code, { gchecks: gc });
    const y = window.scrollY; this.render(); window.scrollTo(0, y);
  },

  /* ---------- 反思與進度: evaluasi diri (SRL) ---------- */
  r_reflect() {
    const m = this.m, p = App.getP(m.code);
    const cando = p.cando || [];
    const lv = [['😟', 'Belum'], ['🙂', 'Cukup'], ['😎', 'Yakin']];
    const strats = ['Ulangi dialog sambil mendengar', 'Latih kata 核心 dengan audio', 'Kerjakan ulang tugas TOCFL', 'Lanjut ke modul berikutnya'];
    return `
      ${p.goal ? `<div class="panel"><div class="panel-label">Target yang kamu tulis di awal</div><p>“${esc(p.goal)}”</p></div>` : ''}
      <div class="panel"><div class="panel-label">Hasil tugas</div>
        <p>${p.tasks ? `Skor terakhir <b>${p.tasks.last}%</b> · terbaik <b>${p.tasks.best}%</b> (${p.tasks.tries}× mencoba)` : 'Kamu belum menyelesaikan tugas TOCFL di modul ini.'}</p></div>
      <h3 class="layer-title">Seberapa yakin kamu sekarang?</h3>
      <div class="cando-rate">${m.can_do.map((c, ci) => `
        <div class="cr-row"><span>${esc(c)}</span>
          <div class="cr-btns">${lv.map(([ic, lb], li) => `<button class="${cando[ci] === li ? 'on' : ''}" onclick="Modul.rate(${ci}, ${li})">${ic} ${lb}</button>`).join('')}</div>
        </div>`).join('')}</div>
      <label class="field-label" for="diff-input">Bagian mana yang masih sulit?</label>
      <textarea id="diff-input" rows="2" onblur="App.setP(Modul.m.code, {diff: this.value.trim()})" placeholder="Mis. aku masih tertukar 會 dan 能 waktu mendengar…">${esc(p.diff || '')}</textarea>
      <div class="field-label">Langkahku berikutnya</div>
      <div class="strats">${strats.map((s, si) => `<label><input type="checkbox" ${(p.strat || []).includes(si) ? 'checked' : ''} onchange="Modul.strat(${si}, this.checked)"> ${s}</label>`).join('')}</div>
      <button class="btn btn-primary" onclick="Modul.finish()">${p.done ? '✓ Modul selesai — kembali ke peta' : 'Tandai modul selesai'}</button>`;
  },
  rate(ci, li) {
    const c = App.getP(this.m.code).cando || [];
    c[ci] = li;
    App.setP(this.m.code, { cando: c });
    const y = window.scrollY; this.render(); window.scrollTo(0, y);
  },
  strat(si, on) {
    const s = new Set(App.getP(this.m.code).strat || []);
    on ? s.add(si) : s.delete(si);
    App.setP(this.m.code, { strat: [...s] });
  },
  finish() {
    const d = document.getElementById('diff-input');
    App.setP(this.m.code, { diff: d ? d.value.trim() : '', done: true });
    App.showToast(`${this.m.code} selesai. 加油！`);
    App.renderDashboard();
  },
};
