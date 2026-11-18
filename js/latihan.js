/* Latihan kosakata interaktif — retrieval practice + pengulangan kata yang sering salah.
   Mayer: satu kata per layar (segmenting); audio + hanzi + arti ditampilkan berdekatan
   saat umpan balik (contiguity); tanpa hiasan selain penanda benar/salah (coherence). */

const VSTATS_KEY = 'tocfl_vocab_stats';

const Latihan = {
  session: null,
  MODES: {
    kartu:  { ic: '🗂️', name: T('Flashcards', 'Kartu kilat'), desc: T('See the word, recall its meaning, then flip the card. Be honest with yourself.', 'Lihat kata, ingat artinya, lalu balik kartunya. Jujur pada dirimu sendiri.') },
    dengar: { ic: '🎧', name: T('Listen → Meaning', 'Dengar → Arti'), desc: T('Sound only, no text — trains your ear like 聽力.', 'Hanya suara, tanpa tulisan — melatih telinga seperti 聽力.') },
    hanzi:  { ic: '📖', name: T('Hanzi → Meaning', 'Hanzi → Arti'), desc: T('Recognise the written word without pinyin — like 閱讀.', 'Kenali kata tertulis tanpa pinyin — seperti 閱讀.') },
    arti:   { ic: '🔁', name: T('Meaning → Hanzi', 'Arti → Hanzi'), desc: T('From English, choose the right hanzi.', 'Dari bahasa Indonesia, pilih hanzi yang tepat.') },
    tes:    { ic: '📝', name: T('Vocabulary check', 'Tes Kosakata'), desc: '' },
  },
  // Tes Kosakata per bab: 3 dengar→arti, 3 hanzi→arti, 2 arti→hanzi (kata 核心), lalu kalimat rumpang dari data
  TES_KINDS: ['dengar', 'dengar', 'dengar', 'hanzi', 'hanzi', 'hanzi', 'arti', 'arti'],

  stats() { return Store.get(VSTATS_KEY, {}); },
  id(code, w) { return `${code}:${w}`; },
  weak(s) { return s && s.w > s.r; },

  words(vol, codes) {
    const out = [];
    for (const m of App.volData[vol].modules) {
      if (codes && !codes.includes(m.code)) continue;
      for (const [layer, list] of [['core', m.vocab.core], ['sup', m.vocab.supplement]])
        for (const v of list) out.push({ ...v, code: m.code, layer, id: this.id(m.code, v.w) });
    }
    return out;
  },
  opened(vol) { return App.plan[vol].filter(m => App.status(m.code) !== 'new').map(m => m.code); },

  menu(vol) {
    const st = this.stats(), all = this.words(vol), opened = this.opened(vol);
    const seen = all.filter(v => st[v.id]).length, weak = all.filter(v => this.weak(st[v.id])).length;
    const scope = this._scope || (opened.length ? 'buka' : 'semua');
    const scopes = [['buka', `${T('Opened', 'Sudah dibuka')} · ${opened.length}`, opened.length], ['semua', `${T('All', 'Semua')} · ${App.plan[vol].length}`, 1],
                    ['sulit', `${T('Hard words', 'Kata sulit')} · ${weak}`, weak]];
    return `
      <div class="stats3">
        <div>${App.ring(Math.round(seen / all.length * 100), `${seen}`)}<small>${T('words practised', 'kata pernah dilatih')}</small></div>
        <div>${App.ring(all.length ? Math.round((seen - weak) / all.length * 100) : 0, `${seen - weak}`, 'ring-ok')}<small>${T('mostly right', 'lebih sering benar')}</small></div>
        <div>${App.ring(all.length ? Math.round(weak / all.length * 100) : 0, `${weak}`, 'ring-warn')}<small>${T('hard words', 'kata sulit')}</small></div>
      </div>
      <div class="field-k">${T('Take words from modules…', 'Ambil kata dari modul…')}</div>
      <div class="seg wrap">${scopes.map(([k, l, ok]) => `<button class="${k === scope ? 'on' : ''}" ${ok ? '' : 'disabled'} onclick="Latihan._scope='${k}';App.route()">${l}</button>`).join('')}</div>
      <div class="field-k">${T('Choose a practice mode · 10 words per session', 'Pilih cara latihan · 10 kata per sesi')}</div>
      <div class="mode-list">${Object.entries(this.MODES).filter(([k]) => k !== 'tes').map(([k, m]) => `
        <button class="card mode-card" onclick="Latihan.startScope(${vol}, '${k}')">
          ${Pic.html(m.ic, 'mode-ic')}<div><b>${m.name}</b><span>${m.desc}</span></div><span class="chev">›</span></button>`).join('')}
      </div>
      <p class="hint">${T('Words you miss will come back more often until you get them right more often than wrong.', 'Kata yang salah akan lebih sering muncul lagi sampai kamu lebih sering benar daripada salah.')}</p>`;
  },
  startScope(vol, mode) {
    const scope = this._scope || (this.opened(vol).length ? 'buka' : 'semua');
    if (scope === 'sulit') return this.start({ vol, mode, weakOnly: true });
    this.start({ vol, mode, codes: scope === 'buka' ? this.opened(vol) : null });
  },

  /* Pilih 10 kata: kata sulit & belum pernah dilatih didahulukan, sisanya acak */
  start({ vol, codes = null, mode = 'dengar', weakOnly = false, from = null, list = null }) {
    const st = this.stats();
    let pool = list || this.words(vol, codes);
    if (weakOnly) pool = pool.filter(v => this.weak(st[v.id]));
    if (!pool.length) return App.toast(T('No words to practise yet.', 'Belum ada kata untuk dilatih.'));
    const prio = v => { const s = st[v.id]; return !s ? 1 : this.weak(s) ? 0 : 2 + (s.r - s.w) * 0.1; };
    pool = shuffle(pool).sort((a, b) => prio(a) - prio(b)).slice(0, 10);
    const distract = this.words(vol);
    this.session = {
      vol, mode, from: from || `#/v/${vol}/kata`, i: 0, res: [], flip: false,
      items: shuffle(pool).map(v => ({ v, opts: mode === 'kartu' ? null : this.options(v, distract, codes) })),
    };
    Soal.plays = {};
    App.go('#/latihan');
  },
  // jumlah butir otomatis: 8, atau 2× jumlah kata bila bab hanya punya sedikit kata
  tesAuto(nWords) { return Math.min(this.TES_KINDS.length, nWords * 2); },
  tesCount(m) { return this.tesAuto(m.vocab.core.length + m.vocab.supplement.length) + (m.tes_kata || []).length; },
  /* Tes Kosakata satu bab: 8 butir otomatis dari kata 核心 + kalimat rumpang (m.tes_kata). Skor → progres .kata */
  startTes(vol, code, from) {
    const m = App.volData[vol].modules.find(x => x.code === code);
    const all = this.words(vol), core = all.filter(v => v.code === code && v.layer === 'core');
    if (!core.length) return App.toast(T('No words to test yet.', 'Belum ada kata untuk dites.'));
    // kata 核心 + 補充 (keputusan Carli 2026-11-18): ±5 核心 + ±3 補充 per tes, kekurangan diisi dari lapis lain.
    // Tiap kata paling banyak 2× (jenis soal berbeda), jadi bab dengan sedikit kata punya tes lebih pendek.
    const sup = shuffle(all.filter(v => v.code === code && v.layer === 'sup')), c = shuffle(core);
    const nSup = Math.min(sup.length, Math.max(3, this.TES_KINDS.length - c.length));
    const words = shuffle(c.slice(0, this.TES_KINDS.length - nSup).concat(sup.slice(0, nSup)))
      .concat(c.slice(this.TES_KINDS.length - nSup), sup.slice(nSup));
    const n = this.tesAuto(words.length), first = {}, items = [];
    for (let i = 0; i < n; i++) {
      const v = words[i % words.length];
      let kind = this.TES_KINDS[Math.floor(i / n * this.TES_KINDS.length)];
      if (first[v.w] === kind) kind = ['dengar', 'hanzi', 'arti'].find(k => k !== kind);
      first[v.w] = first[v.w] || kind;
      items.push({ kind, v, opts: this.options(v, all, [code]) });
    }
    const urut = { dengar: 0, hanzi: 1, arti: 2 };
    items.sort((a, b) => urut[a.kind] - urut[b.kind]);
    for (const t of m.tes_kata || []) {
      const v = core.find(x => x.w === t.a) || { w: t.a, py: '', meaning: '', code };
      items.push({ kind: 'kalimat', v, t, opts: shuffle([t.a, ...t.x]) });
    }
    this.session = { vol, mode: 'tes', code, from: from || location.hash, i: 0, res: [], flip: false, items };
    Soal.plays = {};
    App.go('#/latihan');
  },
  // 4 pilihan: pengecoh dari modul yang sama bila cukup, lalu dari volume; arti & hanzi tidak boleh kembar
  options(v, all, codes) {
    const same = shuffle(all.filter(x => x.code === v.code)), rest = shuffle(all.filter(x => x.code !== v.code));
    const out = [v], seenM = new Set([v.meaning]), seenW = new Set([v.w]);
    for (const x of [...same, ...rest]) {
      if (out.length === 4) break;
      if (seenM.has(x.meaning) || seenW.has(x.w)) continue;
      seenM.add(x.meaning); seenW.add(x.w); out.push(x);
    }
    return shuffle(out);
  },

  render() {
    const s = this.session, n = s.items.length;
    App.bar(`${this.MODES[s.mode].name}`, s.from, `<span class="bar-pill">${Math.min(s.i + 1, n)}/${n}</span>`);
    if (s.i >= n) return this.summary();
    const it = s.items[s.i], v = it.v, r = s.res[s.i];
    const prog = `<div class="lprog"><i style="width:${s.i / n * 100}%"></i></div>`;
    let h;
    if (s.mode === 'kartu') {
      h = `<div class="vcard flash ${v.layer}">
          <div class="vcard-top"><span class="layer-chip">${v.code}</span></div>
          <button class="vword" lang="zh-TW" onclick="Speech.word('${esc(v.say || v.w)}')">${esc(v.w)}</button>
          ${s.flip ? `<div class="vpy">${esc(v.py)}</div><div class="vmean"><span class="pos">${esc(v.pos)}</span> ${esc(v.meaning)}</div>`
                   : `<p class="hint">${T('Say this word and recall its meaning first.', 'Ucapkan kata ini dan ingat artinya dulu.')}</p>`}
        </div>
        ${s.flip ? `<div class="row2">
            <button class="btn warn" onclick="Latihan.mark(false)">${Pic.html('🔁', 'ic-sm')} ${T('Not yet', 'Belum ingat')}</button>
            <button class="btn ok" onclick="Latihan.mark(true)">${Pic.html('✅', 'ic-sm')} ${T('Got it', 'Ingat')}</button></div>`
                 : `<button class="btn primary block" onclick="Latihan.flip()">${T('Flip card', 'Balik kartu')}</button>`}`;
    } else {
      const kind = this.kind(it);
      const hint = { dengar: T('Listen, then choose the meaning', 'Dengarkan, lalu pilih artinya'), hanzi: T('Choose the meaning of this word', 'Pilih arti kata ini'),
                     arti: T('Choose the matching word', 'Pilih kata yang sesuai'), kalimat: T('Choose the word that fits the gap', 'Pilih kata yang tepat untuk titik kosong') };
      const prompt = kind === 'dengar'
        ? `<button class="play-big" id="play-lw" onclick="Speech.word('${esc(v.say || v.w)}')">${Pic.html('🔊', 'play-ic')}<span>${T('Listen', 'Dengarkan')}</span><small>${T('tap to play again', 'ketuk untuk memutar lagi')}</small></button>`
        : kind === 'hanzi' ? `<div class="vword static" lang="zh-TW">${esc(v.w)}</div>`
        : kind === 'kalimat' ? `<div class="lsent" lang="zh-TW">${esc(it.t.zh).replace('（　）', `<span class="gap">${r != null ? esc(it.t.a) : '（　）'}</span>`)}</div>`
        : `<div class="lmean">${esc(v.meaning)}<small>${esc(v.pos)}</small></div>`;
      const lab = x => kind === 'kalimat' ? `<span lang="zh-TW" class="big-zh">${esc(x)}</span>`
        : kind === 'arti' ? `<span lang="zh-TW" class="big-zh">${esc(x.w)}</span>` : `<span>${esc(x.meaning)}</span>`;
      const benar = x => kind === 'kalimat' ? x === it.t.a : x === v;
      h = `<div class="q-card">${s.mode === 'tes' ? `<p class="hint">${hint[kind]}</p>` : ''}${prompt}
        <div class="opts">${it.opts.map((x, oi) => {
          const cls = r == null ? '' : benar(x) ? 'right' : oi === r.pick ? 'wrong' : 'dim';
          return `<button class="opt ${cls}" ${r == null ? `onclick="Latihan.pick(${oi})"` : 'disabled'}><b class="opt-l">${'ABCD'[oi]}</b>${lab(x)}</button>`;
        }).join('')}</div>
        ${r != null ? `<div class="feedback ${r.ok ? 'ok' : 'no'}">${Pic.html(r.ok ? '✅' : '🔁', 'fb-ic')}
            <div><b lang="zh-TW">${esc(v.w)}</b> <span>${esc(v.py)}</span>
              <button class="say-btn" onclick="Speech.word('${esc(v.say || v.w)}')">${Pic.html('🔊', 'ic-xs')}</button>
              <p>${esc(v.meaning)} · <small>${v.code}</small></p>${kind === 'kalimat' ? `<p>${esc(it.t.id)}</p>` : ''}</div></div>` : ''}
      </div>
      ${r != null ? `<button class="btn primary block" onclick="Latihan.next()">${s.i + 1 < n ? T('Next ›', 'Berikutnya ›') : T('See results ›', 'Lihat hasil ›')}</button>` : ''}`;
    }
    App.main(prog + h);
    Speech.preload([[v.say || v.w, 'W'], ...(s.items[s.i + 1] ? [[s.items[s.i + 1].v.say || s.items[s.i + 1].v.w, 'W']] : [])]);
    if (this.kind(it) === 'dengar' && r == null && !Soal.plays['lw' + s.i]) { Soal.plays['lw' + s.i] = 1; setTimeout(() => Speech.word(v.say || v.w), 250); }
  },
  kind(it) { return this.session.mode === 'tes' ? it.kind : this.session.mode; },
  record(v, ok) {
    const st = this.stats(), x = st[v.id] || { r: 0, w: 0 };
    ok ? x.r++ : x.w++; x.t = Date.now(); st[v.id] = x;
    Store.set(VSTATS_KEY, st);
  },
  pick(oi) {
    const s = this.session, it = s.items[s.i], ok = it.kind === 'kalimat' ? it.opts[oi] === it.t.a : it.opts[oi] === it.v;
    s.res[s.i] = { pick: oi, ok };
    if (it.v.id) this.record(it.v, ok);
    if (this.kind(it) !== 'dengar') Speech.word(it.v.say || it.v.w);
    this.render();
  },
  flip() { const v = this.session.items[this.session.i].v; this.session.flip = true; Speech.word(v.say || v.w); this.render(); },
  mark(ok) { const s = this.session; s.res[s.i] = { ok }; this.record(s.items[s.i].v, ok); this.next(); },
  next() { const s = this.session; s.i++; s.flip = false; this.render(); window.scrollTo(0, 0); },

  summary() {
    const s = this.session, ok = s.res.filter(r => r && r.ok).length, n = s.items.length;
    let wrong = s.items.filter((_, i) => !s.res[i]?.ok);
    const pct = Math.round(ok / n * 100);
    if (s.mode === 'tes') return this.summaryTes(s, ok, n, pct, wrong);
    App.main(`
      <div class="result ${pct >= 80 ? 'hi' : pct >= 60 ? 'mid' : 'lo'}">
        ${App.ring(pct, `${ok}/${n}`, 'ring-lg')}
        <p>${pct === 100 ? T('Perfect! You recalled every word from memory.', 'Sempurna! Semua kata terpanggil dari ingatan.') : pct >= 60 ? T('Good. The words you missed have been noted and will come back more often.', 'Bagus. Kata yang salah sudah dicatat dan akan muncul lagi lebih sering.') : T('That is fine — the effort of recalling is exactly what strengthens memory. Go over the missed words now.', 'Tidak apa-apa — justru usaha mengingat inilah yang memperkuat ingatan. Ulangi kata yang salah sekarang.')}</p>
      </div>
      ${wrong.length ? `<h3 class="sub-title">${T('To review', 'Perlu diulang')}</h3>
        <div class="wlist">${wrong.map(({ v }) => `<button class="wrow" onclick="Speech.word('${esc(v.say || v.w)}')">
          <b lang="zh-TW">${esc(v.w)}</b><span>${esc(v.py)}</span><small>${esc(v.meaning)}</small>${Pic.html('🔊', 'ic-xs')}</button>`).join('')}</div>` : ''}
      <div class="row2">
        ${wrong.length ? `<button class="btn primary" onclick="Latihan.again(true)">${T('Retry the missed ones', 'Ulangi yang salah')}</button>` : ''}
        <button class="btn ghost" onclick="Latihan.again(false)">${T('New session', 'Sesi baru')}</button>
      </div>
      <button class="btn ghost block" onclick="App.go('${s.from}')">${T('Done', 'Selesai')}</button>`);
  },
  summaryTes(s, ok, n, pct, wrong) {
    if (!s.saved) {   // simpan sekali per sesi: terbaik, terakhir, jumlah percobaan
      const k = App.getP(s.code).kata || { best: 0, tries: 0 };
      App.setP(s.code, { kata: { best: Math.max(k.best || 0, pct), last: pct, tries: (k.tries || 0) + 1 } });
      s.saved = true;
    }
    const best = App.getP(s.code).kata.best;
    const seen = new Set(), words = wrong.map(x => x.v).filter(v => v.id && !seen.has(v.w) && seen.add(v.w));
    App.main(`
      <div class="result ${pct >= 80 ? 'hi' : pct >= 60 ? 'mid' : 'lo'}">
        ${App.ring(pct, `${ok}/${n}`, 'ring-lg')}
        <p>${pct >= 80 ? T('Great — you know this unit\'s key words well. You are ready for the tasks.', 'Hebat — kamu sudah menguasai kata inti bab ini. Siap lanjut ke tugas.')
          : pct >= 60 ? T('Good. Review the words below once more before the tasks.', 'Bagus. Ulangi sekali lagi kata di bawah sebelum mengerjakan tugas.')
          : T('That is fine — this check shows which words need more practice. Review them and try again.', 'Tidak apa-apa — tes ini menunjukkan kata yang perlu dilatih lagi. Ulangi lalu coba lagi.')}</p>
        <small>${T('Best score', 'Skor terbaik')}: ${best}%</small>
      </div>
      ${words.length ? `<h3 class="sub-title">${T('To review', 'Perlu diulang')}</h3>
        <div class="wlist">${words.map(v => `<button class="wrow" onclick="Speech.word('${esc(v.say || v.w)}')">
          <b lang="zh-TW">${esc(v.w)}</b><span>${esc(v.py)}</span><small>${esc(v.meaning)}</small>${Pic.html('🔊', 'ic-xs')}</button>`).join('')}</div>` : ''}
      <div class="row2">
        ${words.length ? `<button class="btn primary" onclick="Latihan.latihSalah()">${T('Practise the missed words', 'Latih kata yang salah')}</button>` : ''}
        <button class="btn ghost" onclick="Latihan.startTes(${s.vol}, '${s.code}', '${s.from}')">${T('Take the check again', 'Ulangi tes')}</button>
      </div>
      <button class="btn ghost block" onclick="App.go('${s.from}')">${T('Back to the module', 'Kembali ke modul')}</button>`);
  },
  latihSalah() {
    const s = this.session, seen = new Set();
    const list = s.items.filter((_, i) => !s.res[i]?.ok).map(x => x.v).filter(v => v.id && !seen.has(v.w) && seen.add(v.w));
    this.start({ vol: s.vol, mode: 'dengar', from: s.from, list });
  },
  again(wrongOnly) {
    const s = this.session;
    const list = wrongOnly ? s.items.filter((_, i) => !s.res[i]?.ok).map(x => x.v) : null;
    const codes = [...new Set(s.items.map(x => x.v.code))];
    this.start({ vol: s.vol, mode: s.mode, from: s.from, list, codes: list ? null : (s.from.startsWith('#/m/') ? codes : null) });
  },
};

function shuffle(a) {
  a = [...a];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}
