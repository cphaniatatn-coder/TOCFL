/* Media: audio (mp3 → TTS), gambar SVG (Twemoji, CC-BY 4.0), avatar pembicara, ilustrasi adegan.
   Prinsip Mayer: gambar hanya dipakai bila menunjang makna (coherence), bukan hiasan. */

const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

/* ===== Audio =====
   Utama: rekaman Mandarin Taiwan (zh-TW, Microsoft Neural) yang sudah dibuat oleh _kerja/buat_audio.py —
   suara mengikuti pembicara (perempuan → suara perempuan, laki-laki → suara laki-laki).
   Cadangan (teks belum punya rekaman / offline): suara browser zh-TW, dipilih perempuan/laki-laki bila tersedia. */
const Audio_ = { map: null, speakers: {}, cur: null, token: 0 };
fetch('data/audio.json').then(r => r.json()).then(d => { Audio_.map = d.clips; Audio_.speakers = d.speakers; }).catch(() => { Audio_.map = {}; });

let _voiceF = null, _voiceM = null;
if (window.speechSynthesis) {
  const pick = () => {
    const tw = speechSynthesis.getVoices().filter(v => /zh[-_]TW/i.test(v.lang));
    _voiceF = tw.find(v => /hsiaochen|hsiaoyu|hanhan|yating|mei-?jia|female/i.test(v.name)) || tw[0] || null;
    _voiceM = tw.find(v => /yunjhe|zhiwei|male/i.test(v.name) && !/female/i.test(v.name)) || null;
  };
  pick();
  speechSynthesis.addEventListener('voiceschanged', pick);
}

const Speech = {
  // profil suara per pembicara (sama dengan _kerja/buat_audio.py)
  profil(sp) { return Audio_.speakers[sp] || 'F1'; },
  stop() {
    Audio_.token++;
    if (Audio_.cur) { Audio_.cur.pause(); Audio_.cur = null; }
    if (window.speechSynthesis) speechSynthesis.cancel();
  },
  // Putar satu teks dengan profil tertentu; kembalikan Promise yang selesai saat audio berakhir
  play(text, prof, token) {
    return new Promise(done => {
      if (token !== Audio_.token) return done();
      const id = Audio_.map && Audio_.map[`${prof}|${text}`];
      if (id) {
        const a = new Audio(`audio/tts/${id}.mp3`);
        Audio_.cur = a;
        a.onended = () => done();
        a.onerror = () => this.tts(text, prof).then(done);
        a.play().catch(() => this.tts(text, prof).then(done));
      } else this.tts(text, prof).then(done);
    });
  },
  tts(text, prof) {
    return new Promise(done => {
      if (!window.speechSynthesis) { App.toast('Audio belum tersedia untuk kalimat ini.'); return done(); }
      const male = /^M|^K/.test(prof);
      const u = new SpeechSynthesisUtterance(text);
      u.lang = 'zh-TW'; u.rate = 0.9;
      const v = male ? (_voiceM || _voiceF) : _voiceF;
      if (v) u.voice = v;
      // bila tidak ada suara laki-laki zh-TW di perangkat ini, rendahkan nada sebagai pengganti
      u.pitch = male && !_voiceM ? 0.7 : prof === 'K' ? 1.3 : 1;
      u.onend = u.onerror = () => done();
      speechSynthesis.speak(u);
    });
  },
  word(text) { this.stop(); this.play(text, 'W', Audio_.token); },
  say(text, onend) { this.stop(); this.play(text, 'N', Audio_.token).then(() => onend && onend()); },
  // Dialog: baris berurutan, masing-masing dengan suara pembicaranya
  async lines(lines, onend) {
    this.stop();
    const t = Audio_.token;
    for (const l of lines) {
      if (t !== Audio_.token) return;
      await this.play(l.zh, this.profil(l.sp), t);
      await new Promise(r => setTimeout(r, 250));   // jeda singkat antarbaris
    }
    if (t === Audio_.token && onend) onend();
  },
};

/* ===== Gambar (Twemoji SVG lokal) ===== */
const Pic = {
  MOD: new Set([0x200d, 0xfe0f, 0x20e3]),
  clusters(s) {
    const out = []; let cur = '', join = false;
    for (const ch of s) {
      const cp = ch.codePointAt(0);
      const isMod = this.MOD.has(cp) || (cp >= 0x1f3fb && cp <= 0x1f3ff);
      if (cur && (isMod || join)) cur += ch; else { if (cur) out.push(cur); cur = ch; }
      join = cp === 0x200d;
    }
    if (cur) out.push(cur);
    return out;
  },
  isEmoji(c) {
    const cp = c.codePointAt(0);
    return cp >= 0x2190 && !(cp >= 0x3000 && cp <= 0x9fff) && !(cp >= 0xff00 && cp <= 0xffef);
  },
  code(c) {
    if (!c.includes('‍')) c = c.replace(/️/g, '');
    return [...c].map(x => x.codePointAt(0).toString(16)).join('-');
  },
  // Ubah string emoji (bisa gabungan, mis. "📚⬆") menjadi deretan <img> SVG
  html(s, cls = '') {
    return this.clusters(s || '').map(c => this.isEmoji(c)
      ? `<img class="tw ${cls}${this.isSwatch(c) ? ' tw-sw' : ''}" src="img/twemoji/${this.code(c)}.svg" alt="" draggable="false" onerror="this.replaceWith(document.createTextNode('${c}'))">`
      : `<span class="tw-txt">${esc(c)}</span>`).join('');
  },
  // Kotak warna (🟥⬜⬛…) dipakai sebagai penanda warna benda di sebelahnya → digambar kecil
  isSwatch(c) { const cp = c.codePointAt(0); return (cp >= 0x1f7e5 && cp <= 0x1f7eb) || cp === 0x2b1b || cp === 0x2b1c; },
  // Gambar soal: beberapa ikon disusun sebaris, makin banyak makin kecil
  group(s, cls) {
    const n = this.clusters(s || '').filter(c => this.isEmoji(c) && !this.isSwatch(c)).length;
    return `<span class="pic-row n${Math.min(n, 4)}">${this.html(s, cls)}</span>`;
  },

  /* Avatar pembicara — memberi 'wajah' pada suara (dual-coding), konsisten di seluruh modul */
  AVATAR: {
    '王大文': '🧑', '李美美': '👩', '安妮': '👧', '志明': '👨', '陳老師': '👩‍🏫', '陳先生': '👨‍💼', '王先生': '👨‍💼',
    '先生': '👨‍💼', '小姐': '👩‍💼', '店員': '👩‍💼', '老闆': '🧔', '老闆娘': '👩‍🦱', '醫生': '🧑‍⚕️', '護士': '👩‍⚕️',
    '媽媽': '👩‍🦳', '美美的媽媽': '👩‍🦳', '房東': '🧓', '陳安安': '🧑‍🎓', '小明': '👦', '安妮的弟弟': '👦',
    '司機': '🧑‍✈️', '男': '👨', '女': '👩',
  },
  avatar(sp) { return this.html(this.AVATAR[sp] || '🧑', 'avatar'); },

  /* Ilustrasi adegan per 情境類別: latar sederhana (SVG buatan sendiri) + 2 ikon penanda situasi */
  SCENE: {
    1: ['🪪', '👋', '#FDE8D7', '#F6B98E'], 2: ['🏠', '🛋️', '#E6F0E6', '#9CC59C'], 3: ['💼', '🏢', '#E7ECF4', '#9DB0CF'],
    4: ['⚽', '🎬', '#FFF1CC', '#F2C94C'], 5: ['🚆', '🗺️', '#E3F2F7', '#86C3D7'], 6: ['🤝', '💬', '#F4E6F2', '#D39BCB'],
    7: ['🩺', '💊', '#FBE3E3', '#EE9A9A'], 8: ['🏫', '📚', '#E9E6F7', '#A99BDB'], 9: ['🛍️', '💳', '#FDEBDD', '#F4A96A'],
    10: ['🍜', '🥢', '#FFF0DD', '#F0B36B'], 11: ['🏦', '📮', '#E2EEF0', '#8FB9BF'], 12: ['🚨', '⚠️', '#FCE5DC', '#E98E6B'],
    13: ['⛰️', '🌳', '#E1F2E6', '#7CC49A'], 14: ['🌏', '♻️', '#E4EFE9', '#8EBFA5'], 15: ['🧧', '🏮', '#FBE2DF', '#E0827A'],
    16: ['😊', '💭', '#FFF4D6', '#F1CF6B'], 17: ['📱', '💻', '#E4EAF5', '#93A6CC'],
  },
  catNum(cat) { return parseInt(String(cat), 10) || 1; },
  scene(cat, size = 'lg') {
    const [a, b, bg, fg] = this.SCENE[this.catNum(cat)] || this.SCENE[1];
    return `<div class="scene scene-${size}" style="--scene-bg:${bg};--scene-fg:${fg}">
      <svg class="scene-bgsvg" viewBox="0 0 200 90" preserveAspectRatio="none" aria-hidden="true">
        <path d="M0 62 Q50 44 100 58 T200 52 V90 H0 Z" fill="var(--scene-fg)" opacity=".55"/>
        <path d="M0 74 Q60 60 120 72 T200 68 V90 H0 Z" fill="var(--scene-fg)" opacity=".85"/>
        <circle cx="168" cy="20" r="9" fill="#fff" opacity=".7"/>
      </svg>
      <div class="scene-icons">${this.html(a, 'scene-ic')}${this.html(b, 'scene-ic scene-ic2')}</div>
    </div>`;
  },
};
