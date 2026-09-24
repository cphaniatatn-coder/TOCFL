/* Satu modul, tahap demi tahap — desain mengikuti prinsip Mayer:
   - Segmenting   : dialog muncul baris per baris (dikendalikan pelajar), kosakata & soal satu per layar
   - Signaling    : kata baru modul disorot di dialog; balok grammar berwarna per fungsi
   - Contiguity   : arti kata muncul tepat di kata yang disentuh (bukan di daftar terpisah)
   - Dual-coding  : avatar pembicara + suara; gambar SVG pada soal
   - Modality/Redundancy: soal 聽力 = audio + gambar, transkrip baru muncul SETELAH menjawab
   - Coherence    : tidak ada hiasan yang tidak menunjang makna
   Urutan tahap: A0 (vocabulary-first) vs TBLL (Willis) — grammar selalu SESUDAH tugas. */

const STAGES = {
  A0: [['intro', '情境導入', 'Tujuan', '🎯'], ['vocab', '詞彙', 'Kosakata', '🗂️'], ['dialog', '情境對話', 'Dialog', '💬'],
       ['tasks', '練習', 'Latihan', '📝'], ['grammar', '語法小提示', 'Grammar', '🧩'], ['reflect', '反思與進度', 'Refleksi', '🪞']],
  TBLL: [['intro', '情境導入', 'Tujuan', '🎯'], ['dialog', '情境對話', 'Dialog', '💬'], ['vocab', '詞彙', 'Kosakata', '🗂️'],
         ['tasks', '溝通任務', 'Tugas', '📝'], ['grammar', '語法聚焦', 'Grammar', '🧩'], ['reflect', '反思與進度', 'Refleksi', '🪞']],
};

/* ===== Renderer soal bersama (dipakai Modul & Ujian) ===== */
const Soal = {
  reg: {}, plays: {},
  limit: null,
  play(key) {
    const t = this.reg[key];
    if (this.limit && (this.plays[key] || 0) >= this.limit) return App.toast(`Di ujian, audio hanya bisa diputar ${this.limit}×.`);
    this.plays[key] = (this.plays[key] || 0) + 1;
    const btn = document.getElementById('play-' + key);
    if (btn) { btn.classList.add('playing'); btn.querySelector('small').textContent = `diputar ${this.plays[key]}×`; }
    const done = () => btn && btn.classList.remove('playing');
    t.lines ? Speech.lines(t.lines, done) : Speech.say(t.audio, done);
  },
  answered(t, a) { return t.type === 'cloze' ? !!(a && a.checked) : a != null; },
  score(t, a) {
    if (t.type === 'cloze') return [t.answers.filter((x, k) => a && a.vals && a.vals[k] === x).length, t.answers.length];
    return [a === t.answer ? 1 : 0, 1];
  },
  isListen(t) { return t.type.startsWith('listen'); },
  // Cloze: ketuk titik kosong → pilih kata; pilihan yang sama berpindah, titik aktif maju otomatis
  clozeSel(a, k) { a = a || { vals: [] }; a.sel = k; return a; },
  clozeFill(t, a, oi) {
    a = a || { vals: [] };
    const n = t.answers.length, empty = () => [...Array(n).keys()].find(i => a.vals[i] == null);
    let k = a.sel != null ? a.sel : empty();
    if (k == null) k = 0;
    const prev = a.vals.indexOf(oi); if (prev >= 0) a.vals[prev] = undefined;
    a.vals[k] = oi;
    a.sel = empty() ?? null;
    return a;
  },
  // mode: 'practice' (umpan balik langsung) | 'exam' (tanpa umpan balik sampai selesai) | 'review'
  body(t, key, a, ns, mode) {
    this.reg[key] = t;
    const show = mode === 'review' || (mode === 'practice' && this.answered(t, a));
    const L = 'ABCDEF';
    let h = `<div class="q-instr">${esc(t.instr)}</div>`;
    if (this.isListen(t)) {
      h += `<button class="play-big" id="play-${key}" onclick="Soal.play('${key}')" aria-label="Putar audio">
              ${Pic.html('🔊', 'play-ic')}<span>Dengarkan</span><small>${this.plays[key] ? `diputar ${this.plays[key]}×` : 'ketuk untuk memutar'}</small></button>`;
      if (show) {
        const tr = t.lines ? t.lines.map(l => `<div class="tr-line">${Pic.avatar(l.sp)}<span lang="zh-TW">${esc(l.zh)}</span></div>`).join('')
                           : `<div class="tr-line"><span lang="zh-TW">${esc(t.audio)}</span></div>`;
        h += `<details class="transcript" open><summary>Transkrip</summary>${tr}</details>`;
      }
      if (t.question) h += `<div class="q-ask" lang="zh-TW">問：${esc(t.question)}</div>`;
    }
    if (t.type === 'read_pick') h += `<figure class="q-picture">${Pic.html(t.picture.icon, 'pic-xl')}<figcaption>${esc(t.picture.label)}</figcaption></figure>`;
    if (t.type === 'read_mc') h += `<div class="q-text" lang="zh-TW">${esc(t.text)}</div><div class="q-ask" lang="zh-TW">問：${esc(t.question)}</div>`;

    if (t.type === 'cloze') {
      const vals = (a && a.vals) || [], sel = a && a.sel != null ? a.sel : vals.findIndex(v => v == null);
      let k = -1;
      const text = esc(t.text).replace(/（(\d)）/g, () => {
        k++;
        const v = vals[k], st = show ? (v === t.answers[k] ? 'right' : 'wrong') : (k === sel && !show ? 'sel' : '');
        return `<button class="blank ${st}" ${show ? 'disabled' : `onclick="${ns}.clozeSel('${key}', ${k})"`}>
          <small>${k + 1}</small>${v != null ? esc(t.options[v]) : '＿＿'}</button>${show && v !== t.answers[k] ? `<span class="fix">→ ${esc(t.options[t.answers[k]])}</span>` : ''}`;
      });
      h += `<div class="q-text cloze" lang="zh-TW">${text}</div>`;
      if (!show) {
        h += `<div class="chips" lang="zh-TW">${t.options.map((o, oi) => {
          const used = vals.includes(oi);
          return `<button class="chip ${used ? 'used' : ''}" onclick="${ns}.clozeFill('${key}', ${oi})"><b>${L[oi]}</b>${esc(o)}</button>`;
        }).join('')}</div>`;
        if (mode === 'practice') h += `<button class="btn primary block" onclick="${ns}.clozeCheck('${key}')">Periksa jawaban</button>`;
      }
    } else {
      const pic = t.type === 'listen_pick';
      h += `<div class="opts ${pic ? 'opts-pic' : ''}">${t.options.map((o, oi) => {
        const cls = show ? (oi === t.answer ? 'right' : oi === a ? 'wrong' : 'dim') : (oi === a ? 'sel' : '');
        const lab = typeof o === 'string' ? `<span lang="zh-TW">${esc(o)}</span>` : `${Pic.html(o.icon, 'pic-opt')}<small>${esc(o.label)}</small>`;
        return `<button class="opt ${cls}" ${show ? 'disabled' : `onclick="${ns}.pick('${key}', ${oi})"`}><b class="opt-l">${L[oi]}</b>${lab}</button>`;
      }).join('')}</div>`;
    }
    if (show) {
      const [g, n] = this.score(t, a);
      h += `<div class="feedback ${g === n ? 'ok' : 'no'}">${Pic.html(g === n ? '✅' : '🔁', 'fb-ic')}<div><b>${g === n ? 'Tepat!' : 'Belum tepat — lihat alasannya:'}</b><p>${esc(t.why)}</p></div></div>`;
    }
    return h;
  },
};

const Modul = {
  vol: null, m: null, stage: 0,
  showPy: false, showZy: true, hl: true,
  revealed: {}, vi: 0, vflip: false, ti: 0, answers: {}, vlist: false,

  stages() { return STAGES[App.volData[this.vol].approach === 'A0' ? 'A0' : 'TBLL']; },

  open(code, stage) {
    const f = App.findModule(code);
    if (!this.m || this.m.code !== code) {
      this.revealed = {}; this.vi = 0; this.vflip = false; this.ti = 0; this.answers = {}; this.vlist = false; this._saved = false; Soal.plays = {};
    }
    Soal.limit = null;
    this.vol = f.vol; this.m = f.m;
    this.stage = Math.max(0, Math.min(5, stage || 0));
    const p = App.getP(code);
    App.setP(code, { stage: Math.max(p.stage || 0, this.stage) });
    Store.set('tocfl_last', { code, stage: this.stage });
    this.render();
  },
  go(i) { App.go(`#/m/${this.m.code}/${Math.max(0, Math.min(5, i))}`); },
  key() { return this.stages()[this.stage][0]; },

  render() {
    const m = this.m, st = this.stages(), cur = st[this.stage];
    const reached = App.getP(m.code).stage || 0;
    App.bar(`${m.code}`, `#/v/${this.vol}`, `<span class="bar-pill">${this.stage + 1}/6</span>`);
    App.main(`
      <header class="mod-head ${this.stage ? 'compact' : ''}">
        ${Pic.scene(m.categories[0], this.stage ? 'sm' : 'md')}
        <div class="mod-title">
          <small>${m.categories.map(esc).join(' · ')}</small>
          <h1 lang="zh-TW">${esc(m.title)}</h1>
          <button class="say-btn" onclick="Speech.say(Modul.m.title)" aria-label="Dengarkan judul">${Pic.html('🔊', 'ic-sm')}</button>
          <p class="mod-sub">${esc(m.title_py)}<br><em>${esc(m.title_id)}</em></p>
        </div>
      </header>
      <nav class="steps" aria-label="Tahap modul">
        ${st.map((s, i) => `<button class="step ${i === this.stage ? 'cur' : ''} ${i <= reached ? 'seen' : ''}" onclick="Modul.go(${i})" title="${s[2]}">
          ${Pic.html(s[3], 'step-ic')}<span lang="zh-TW">${s[1]}</span></button>`).join('')}
      </nav>
      <section class="stage stage-${cur[0]}">
        <h2 class="stage-title"><span lang="zh-TW">${cur[1]}</span> · ${cur[2]}</h2>
        ${this['r_' + cur[0]]()}
      </section>
      <div class="dock">
        ${this.stage > 0 ? `<button class="btn ghost" onclick="Modul.go(${this.stage - 1})">‹ ${st[this.stage - 1][2]}</button>` : '<span></span>'}
        ${this.stage < 5 ? `<button class="btn primary" onclick="Modul.next()">${st[this.stage + 1][2]} ›</button>`
                         : `<button class="btn primary" onclick="Modul.finish()">Selesai ✓</button>`}
      </div>`);
  },
  next() { if (this.key() === 'intro') this.saveGoal(); this.go(this.stage + 1); },
  keepScroll(fn) { const y = window.scrollY; fn(); this.render(); window.scrollTo(0, y); },

  /* ---------- 1. 情境導入 ---------- */
  r_intro() {
    const m = this.m, p = App.getP(m.code);
    return `
      <div class="panel situ"><div class="panel-k">Situasi</div><p>${esc(m.scene)}</p></div>
      <div class="panel"><div class="panel-k">${Pic.html('🎯', 'ic-sm')} Setelah modul ini, kamu bisa…</div>
        <ul class="cando">${m.can_do.map(c => `<li>${esc(c)}</li>`).join('')}</ul></div>
      <div class="panel exam"><div class="panel-k">${Pic.html('🏆', 'ic-sm')} Kenapa penting untuk ujian?</div><p>${esc(m.exam_link)}</p></div>
      <label class="field-k" for="goal-input">Target pribadimu</label>
      <textarea id="goal-input" rows="2" placeholder="Contoh: aku ingin bisa menjawab pertanyaan ini tanpa ragu…">${esc(p.goal || '')}</textarea>
      <p class="hint">Kamu bebas melompat ke tahap mana pun lewat penanda di atas.</p>`;
  },
  saveGoal() { const el = document.getElementById('goal-input'); if (el) App.setP(this.m.code, { goal: el.value.trim() }); },

  /* ---------- 詞彙: kartu satu per satu (segmenting) ---------- */
  allVocab() {
    const { core, supplement } = this.m.vocab;
    return [...core.map(v => ({ ...v, layer: 'core' })), ...supplement.map(v => ({ ...v, layer: 'sup' }))];
  },
  hanzi(w, zy) {
    if (!this.showZy || !zy) return esc(w);
    const marks = zy.split(/\s+/);
    return [...w].map((c, i) => `<span class="zy-unit"><span class="zy-hanzi">${c}</span><span class="zy-mark">${marks[i] || ''}</span></span>`).join('');
  },
  r_vocab() {
    const all = this.allVocab(), known = App.getP(this.m.code).known || {};
    const toolbar = `<div class="toolbar">
        <button class="toggle ${this.showZy ? 'on' : ''}" onclick="Modul.keepScroll(()=>Modul.showZy=!Modul.showZy)">注音</button>
        <button class="toggle ${this.vlist ? 'on' : ''}" onclick="Modul.keepScroll(()=>Modul.vlist=!Modul.vlist)">Daftar</button>
        <span class="spacer"></span>
        <button class="btn small" onclick="Latihan.start({vol:${this.vol}, codes:['${this.m.code}'], mode:'dengar', from:location.hash})">${Pic.html('🎧', 'ic-sm')} Latihan kata</button>
      </div>`;
    if (this.vlist) {
      return toolbar + `<div class="vgrid">${all.map((v, i) => `
        <button class="vcell ${v.layer}" onclick="Modul.keepScroll(()=>{Modul.vlist=false;Modul.vi=${i};Modul.vflip=true})">
          <b lang="zh-TW">${esc(v.w)}</b><small>${esc(v.py)}</small>${known[v.w] ? '<i class="known">✓</i>' : ''}</button>`).join('')}</div>`;
    }
    const i = Math.min(this.vi, all.length - 1), v = all[i];
    return toolbar + `
      <div class="vcard ${v.layer}">
        <div class="vcard-top"><span class="layer-chip">${v.layer === 'core' ? '核心 · dipakai aktif' : '補充 · cukup dikenali'}</span>
          <span class="vcount">${i + 1}/${all.length}</span></div>
        <button class="vword" lang="zh-TW" onclick="Speech.word('${esc(v.w)}')" aria-label="Dengarkan">${this.hanzi(v.w, v.zy)}</button>
        <div class="vpy">${esc(v.py)} <button class="say-btn" onclick="Speech.word('${esc(v.w)}')" aria-label="Dengarkan">${Pic.html('🔊', 'ic-sm')}</button></div>
        ${this.vflip ? `<div class="vmean"><span class="pos">${esc(v.pos)}</span> ${esc(v.meaning)}${v.note ? `<small>${esc(v.note)}</small>` : ''}</div>`
                     : `<button class="btn ghost block" onclick="Modul.keepScroll(()=>Modul.vflip=true)">Coba ingat artinya, lalu ketuk untuk melihat</button>`}
        <button class="know ${known[v.w] ? 'on' : ''}" onclick="Modul.toggleKnown('${esc(v.w)}')">${known[v.w] ? '✓ Sudah hafal' : 'Tandai sudah hafal'}</button>
      </div>
      <div class="vnav">
        <button class="btn ghost" ${i === 0 ? 'disabled' : ''} onclick="Modul.keepScroll(()=>{Modul.vi=${i - 1};Modul.vflip=false})">‹</button>
        <div class="dots">${all.map((x, k) => `<i class="${k === i ? 'cur' : ''} ${known[x.w] ? 'k' : ''}"></i>`).join('')}</div>
        <button class="btn ghost" ${i === all.length - 1 ? 'disabled' : ''} onclick="Modul.keepScroll(()=>{Modul.vi=${i + 1};Modul.vflip=false})">›</button>
      </div>`;
  },
  toggleKnown(w) {
    const k = App.getP(this.m.code).known || {};
    k[w] = !k[w];
    this.keepScroll(() => App.setP(this.m.code, { known: k }));
  },

  /* ---------- 情境對話: baris demi baris + sorotan kata baru ---------- */
  highlight(zh) {
    if (!this.hl) return esc(zh);
    const all = this.allVocab().map((v, i) => [v.w, i]).filter(([w]) => w).sort((a, b) => b[0].length - a[0].length);
    let out = '', i = 0;
    while (i < zh.length) {
      const hit = all.find(([w]) => zh.startsWith(w, i));
      if (hit) { out += `<button class="kw ${this.allVocab()[hit[1]].layer}" onclick="event.stopPropagation();Modul.kw(${hit[1]}, this)">${esc(hit[0])}</button>`; i += hit[0].length; }
      else { out += esc(zh[i]); i++; }
    }
    return out;
  },
  kw(idx, el) {
    const v = this.allVocab()[idx];
    document.querySelectorAll('.kw-pop').forEach(x => x.remove());
    const pop = document.createElement('div');
    pop.className = 'kw-pop';
    pop.innerHTML = `<b lang="zh-TW">${esc(v.w)}</b> <span>${esc(v.py)}</span><p>${esc(v.meaning)}</p>`;
    // Melayang tepat di bawah kata (contiguity) tanpa mendorong baris teks
    const box = el.closest('.bubble'), r = el.getBoundingClientRect(), br = box.getBoundingClientRect();
    box.appendChild(pop);
    const left = Math.max(0, Math.min(r.left - br.left, br.width - pop.offsetWidth));
    pop.style.left = left + 'px'; pop.style.top = (r.bottom - br.top + 4) + 'px';
    Speech.word(v.w);
    setTimeout(() => document.addEventListener('click', () => pop.remove(), { once: true }), 0);
  },
  r_dialog() {
    return `
      <div class="toolbar">
        <button class="toggle ${this.showPy ? 'on' : ''}" onclick="Modul.keepScroll(()=>Modul.showPy=!Modul.showPy)">拼音</button>
        <button class="toggle ${this.hl ? 'on' : ''}" onclick="Modul.keepScroll(()=>Modul.hl=!Modul.hl)">Sorot kata baru</button>
      </div>
      <p class="hint">Ketuk kata yang disorot untuk melihat artinya. Ketuk balon untuk melihat terjemahan.</p>
      ${this.m.dialogs.map((d, di) => {
        const n = this.revealed[di] ?? 1, lines = d.lines;
        const speakers = [...new Set(lines.map(l => l.sp))];
        return `<div class="chat">
          <div class="chat-head"><span lang="zh-TW">${esc(d.place)}</span><small>${esc(d.title_id)}</small>
            <button class="btn small" onclick="Modul.playAll(${di})">${Pic.html('▶️', 'ic-sm')} Putar</button></div>
          ${lines.slice(0, n).map((l, li) => {
            const right = speakers.indexOf(l.sp) % 2 === 1;
            return `<div class="msg ${right ? 'me' : ''} ${li === n - 1 ? 'new' : ''}">
              ${Pic.avatar(l.sp)}
              <div class="bubble" onclick="this.classList.toggle('show-id')">
                <small class="who" lang="zh-TW">${esc(l.sp)}</small>
                <div class="zh" lang="zh-TW">${this.highlight(l.zh)}
                  <button class="say-btn" onclick="event.stopPropagation();Speech.say(Modul.m.dialogs[${di}].lines[${li}].zh)" aria-label="Dengarkan">${Pic.html('🔊', 'ic-xs')}</button></div>
                ${this.showPy ? `<div class="py">${esc(l.py)}</div>` : ''}
                <div class="idn">${esc(l.id)}</div>
              </div></div>`;
          }).join('')}
          ${n < lines.length ? `<div class="chat-more">
              <button class="btn primary small" onclick="Modul.reveal(${di})">Baris berikutnya ▸</button>
              <button class="btn ghost small" onclick="Modul.keepScroll(()=>Modul.revealed[${di}]=${lines.length})">Tampilkan semua</button></div>` : ''}
        </div>`;
      }).join('')}`;
  },
  reveal(di) {
    const n = (this.revealed[di] ?? 1) + 1;
    this.keepScroll(() => (this.revealed[di] = n));
    const l = this.m.dialogs[di].lines[n - 1];
    if (l) Speech.lines([l]);
  },
  playAll(di) { this.keepScroll(() => (this.revealed[di] = this.m.dialogs[di].lines.length)); Speech.lines(this.m.dialogs[di].lines); },

  /* ---------- 溝通任務: satu soal per layar ---------- */
  ans(key) { return this.answers[key]; },
  pick(key, oi) { this.answers[key] = oi; this.afterAnswer(); },
  clozeSel(key, k) { this.answers[key] = Soal.clozeSel(this.answers[key], k); this.keepScroll(() => {}); },
  clozeFill(key, oi) { this.answers[key] = Soal.clozeFill(Soal.reg[key], this.answers[key], oi); this.keepScroll(() => {}); },
  clozeCheck(key) {
    const t = Soal.reg[key], a = this.answers[key] || { vals: [] };
    if (t.answers.some((_, k) => a.vals[k] == null)) return App.toast('Isi semua titik kosong dulu.');
    a.checked = true; this.answers[key] = a; this.afterAnswer();
  },
  score() {
    let g = 0, n = 0;
    this.m.tasks.forEach((t, i) => { const [x, y] = Soal.score(t, this.answers['t' + i]); g += x; n += y; });
    return Math.round(g / n * 100);
  },
  allDone() { return this.m.tasks.every((t, i) => Soal.answered(t, this.answers['t' + i])); },
  afterAnswer() {
    if (this.allDone()) {
      const s = this.score(), p = App.getP(this.m.code);
      if (!this._saved) {
        App.setP(this.m.code, { tasks: { last: s, best: Math.max(s, p.tasks?.best ?? 0), tries: (p.tasks?.tries || 0) + 1 } });
        this._saved = true;
      }
    }
    this.keepScroll(() => {});
  },
  r_tasks() {
    const tasks = this.m.tasks, n = tasks.length;
    if (this.ti >= n) return this.taskSummary();
    const i = this.ti, t = tasks[i], key = 't' + i, a = this.answers[key];
    return `
      <div class="q-progress">${tasks.map((x, k) => {
        const aa = this.answers['t' + k], st = Soal.answered(x, aa) ? (Soal.score(x, aa)[0] === Soal.score(x, aa)[1] ? 'ok' : 'no') : '';
        return `<button class="${k === i ? 'cur' : ''} ${st}" onclick="Modul.keepScroll(()=>Modul.ti=${k})">${k + 1}</button>`;
      }).join('')}</div>
      <div class="q-card">
        <div class="q-part" lang="zh-TW">${esc(t.part)}</div>
        ${Soal.body(t, key, a, 'Modul', 'practice')}
      </div>
      ${Soal.answered(t, a) ? `<button class="btn primary block" onclick="Modul.keepScroll(()=>Modul.ti=${i + 1})">${i + 1 < n ? 'Soal berikutnya ›' : 'Lihat hasil ›'}</button>` : ''}`;
  },
  taskSummary() {
    if (!this.allDone()) { this.ti = this.m.tasks.findIndex((t, i) => !Soal.answered(t, this.answers['t' + i])); return this.r_tasks(); }
    const s = this.score(), p = App.getP(this.m.code);
    const msg = s >= 80 ? 'Kamu sudah menguasai tugas di adegan ini. Lanjutkan ke grammar untuk merapikan polanya.'
      : s >= 60 ? 'Hampir! Baca lagi penjelasan di soal yang belum tepat — pola kesalahannya biasanya sama.'
      : 'Belum — dan itu wajar di percobaan awal. Ulangi dialog, lalu coba lagi. Skor terbaikmu tetap tersimpan.';
    return `<div class="result ${s >= 80 ? 'hi' : s >= 60 ? 'mid' : 'lo'}">
        ${App.ring(s, s + '%', 'ring-lg')}
        <p>${msg}</p>
        <small>Percobaan ke-${p.tasks?.tries || 1} · skor terbaik ${p.tasks?.best ?? s}%</small>
        <div class="row">
          <button class="btn ghost" onclick="Modul.retry()">${Pic.html('🔁', 'ic-sm')} Coba lagi</button>
          <button class="btn ghost" onclick="Modul.keepScroll(()=>Modul.ti=0)">Tinjau jawaban</button>
        </div></div>`;
  },
  retry() { this.answers = {}; this.ti = 0; this._saved = false; Soal.plays = {}; this.keepScroll(() => {}); },

  /* ---------- 語法: balok Lego ---------- */
  r_grammar() {
    const gc = App.getP(this.m.code).gchecks || {};
    if (!this.m.grammar.length) return `
      <div class="panel"><div class="panel-k">Tidak ada pola baru di adegan ini</div>
        <p>Adegan ini sengaja hanya menambah kosakata. Pola yang kamu pakai ulang:</p>
        <ul class="examples">${(this.m.recycle || []).map((r, i) => `<li><span lang="zh-TW">${esc(r.zh)}</span>
          <button class="say-btn" onclick="Speech.say(Modul.m.recycle[${i}].zh)">${Pic.html('🔊', 'ic-xs')}</button><small>${esc(r.id)}</small></li>`).join('')}</ul></div>`;
    return `<p class="hint">Pola ini sudah kamu pakai di dialog & tugas. Sekarang kita bongkar susunan baloknya.</p>
      ${this.m.grammar.map((g, gi) => `
      <article class="gcard">
        <div class="gcard-head"><span class="gid">TBCL #${g.tbcl_id}</span><h3 lang="zh-TW">${esc(g.point)}</h3></div>
        <div class="blocks" lang="zh-TW">${g.blocks.map(([w, role], bi) => `<span class="block r${bi % 5}"><b>${esc(w)}</b><small>${esc(role)}</small></span>`).join('')}</div>
        <div class="pattern">Pola: <code lang="zh-TW">${esc(g.pattern)}</code></div>
        <p>${esc(g.explain)}</p>
        <ul class="examples">${g.examples.map((e, ei) => `<li><span lang="zh-TW">${esc(e.zh)}</span>
          <button class="say-btn" onclick="Speech.say(Modul.m.grammar[${gi}].examples[${ei}].zh)" aria-label="Dengarkan">${Pic.html('🔊', 'ic-xs')}</button>
          <small>${esc(e.id)}</small></li>`).join('')}</ul>
        <div class="gcheck"><div class="panel-k">Cek cepat</div><div lang="zh-TW">${esc(g.check.q)}</div>
          <div class="opts">${g.check.options.map((o, oi) => {
            const a = gc[gi], cls = a != null ? (oi === g.check.answer ? 'right' : oi === a ? 'wrong' : 'dim') : '';
            return `<button class="opt ${cls}" ${a != null ? 'disabled' : `onclick="Modul.gcheck(${gi}, ${oi})"`}><span lang="zh-TW">${esc(o)}</span></button>`;
          }).join('')}</div></div>
      </article>`).join('')}`;
  },
  gcheck(gi, oi) { const gc = App.getP(this.m.code).gchecks || {}; gc[gi] = oi; this.keepScroll(() => App.setP(this.m.code, { gchecks: gc })); },

  /* ---------- 反思與進度 ---------- */
  r_reflect() {
    const m = this.m, p = App.getP(m.code), cando = p.cando || [], known = p.known || {};
    const nKnown = this.allVocab().filter(v => known[v.w]).length, nAll = this.allVocab().length;
    const lv = [['😟', 'Belum'], ['🙂', 'Cukup'], ['😎', 'Yakin']];
    const strats = ['Ulangi dialog sambil mendengar', 'Latih kata 核心 dengan audio', 'Kerjakan ulang tugas', 'Lanjut ke modul berikutnya'];
    return `
      <div class="stats3">
        <div>${App.ring(p.tasks ? p.tasks.best : 0, p.tasks ? p.tasks.best + '%' : '–')}<small>Tugas terbaik</small></div>
        <div>${App.ring(Math.round(nKnown / nAll * 100), `${nKnown}/${nAll}`)}<small>Kata dihafal</small></div>
        <div>${App.ring(Math.round(cando.filter(x => x === 2).length / m.can_do.length * 100), `${cando.filter(x => x === 2).length}/${m.can_do.length}`)}<small>Target yakin</small></div>
      </div>
      ${p.goal ? `<div class="panel"><div class="panel-k">Target yang kamu tulis di awal</div><p>“${esc(p.goal)}”</p></div>` : ''}
      <h3 class="sub-title">Seberapa yakin kamu sekarang?</h3>
      ${m.can_do.map((c, ci) => `<div class="cr-row"><p>${esc(c)}</p>
        <div class="seg">${lv.map(([ic, lb], li) => `<button class="${cando[ci] === li ? 'on' : ''}" onclick="Modul.rate(${ci}, ${li})">${Pic.html(ic, 'ic-sm')}${lb}</button>`).join('')}</div></div>`).join('')}
      <label class="field-k" for="diff-input">Bagian mana yang masih sulit?</label>
      <textarea id="diff-input" rows="2" onblur="App.setP(Modul.m.code, {diff: this.value.trim()})" placeholder="Mis. aku masih tertukar 會 dan 能 waktu mendengar…">${esc(p.diff || '')}</textarea>
      <div class="field-k">Langkahku berikutnya</div>
      <div class="checks">${strats.map((s, si) => `<label><input type="checkbox" ${(p.strat || []).includes(si) ? 'checked' : ''} onchange="Modul.strat(${si}, this.checked)"> ${s}</label>`).join('')}</div>`;
  },
  rate(ci, li) { const c = App.getP(this.m.code).cando || []; c[ci] = li; this.keepScroll(() => App.setP(this.m.code, { cando: c })); },
  strat(si, on) { const s = new Set(App.getP(this.m.code).strat || []); on ? s.add(si) : s.delete(si); App.setP(this.m.code, { strat: [...s] }); },
  finish() {
    const d = document.getElementById('diff-input');
    App.setP(this.m.code, { diff: d ? d.value.trim() : '', done: true });
    App.toast(`${this.m.code} selesai. 加油！`);
    App.go(`#/v/${this.vol}`);
  },
};
