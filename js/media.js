/* Media: audio (mp3 → TTS), gambar SVG (Twemoji, CC-BY 4.0), avatar pembicara, ilustrasi adegan.
   Prinsip Mayer: gambar hanya dipakai bila menunjang makna (coherence), bukan hiasan. */

const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

/* ===== Audio ===== */
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
  stop() { if (window.speechSynthesis) speechSynthesis.cancel(); },
  word(text) {
    const url = `audio/${encodeURIComponent(text.replace(/\//g, '／'))}.mp3`;
    if (!_audioCache[url]) _audioCache[url] = new Audio(url);
    const a = _audioCache[url];
    a.currentTime = 0;
    a.play().catch(() => this.say(text));
  },
  say(text, onend) {
    if (!window.speechSynthesis) { App.toast('Browser ini tidak mendukung suara.'); return; }
    speechSynthesis.cancel();
    const u = this.utter(text);
    if (onend) u.onend = onend;
    speechSynthesis.speak(u);
  },
  // Dialog: baris berurutan; suara 男/女 dibedakan lewat pitch
  lines(lines, onend) {
    if (!window.speechSynthesis) { App.toast('Browser ini tidak mendukung suara.'); return; }
    speechSynthesis.cancel();
    lines.forEach((l, i) => {
      const u = this.utter(l.zh, Pic.pitch(l.sp));
      if (onend && i === lines.length - 1) u.onend = onend;
      speechSynthesis.speak(u);
    });
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
      ? `<img class="tw ${cls}" src="img/twemoji/${this.code(c)}.svg" alt="" draggable="false" onerror="this.replaceWith(document.createTextNode('${c}'))">`
      : `<span class="tw-txt">${esc(c)}</span>`).join('');
  },

  /* Avatar pembicara — memberi 'wajah' pada suara (dual-coding), konsisten di seluruh modul */
  AVATAR: {
    '王大文': '🧑', '李美美': '👩', '安妮': '👧', '志明': '👨', '陳老師': '👩‍🏫', '陳先生': '👨‍💼', '王先生': '👨‍💼',
    '先生': '👨‍💼', '小姐': '👩‍💼', '店員': '👩‍💼', '老闆': '🧔', '老闆娘': '👩‍🦱', '醫生': '🧑‍⚕️', '護士': '👩‍⚕️',
    '媽媽': '👩‍🦳', '美美的媽媽': '👩‍🦳', '房東': '🧓', '陳安安': '🧑‍🎓', '小明': '👦', '安妮的弟弟': '👦',
    '司機': '🧑‍✈️', '男': '👨', '女': '👩',
  },
  avatar(sp) { return this.html(this.AVATAR[sp] || '🧑', 'avatar'); },
  pitch(sp) {
    const f = ['李美美', '安妮', '陳老師', '小姐', '店員', '老闆娘', '護士', '媽媽', '美美的媽媽', '女'];
    const kid = ['小明', '安妮的弟弟'];
    return kid.includes(sp) ? 1.4 : f.includes(sp) ? 1.2 : 0.85;
  },

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
