// Pre-load zh-TW voice once at startup to avoid delay on first speak
let _zhVoice = null;
const _audioCache = {};

if (window.speechSynthesis) {
  const _pickVoice = () => {
    const voices = window.speechSynthesis.getVoices();
    if (!voices.length) return;
    _zhVoice =
      voices.find(v => v.lang === 'zh-TW' && /hsiaoc|hsiaoyu|xiaoc|xiaoyu/i.test(v.name)) ||
      voices.find(v => v.lang === 'zh-TW' && /online|natural|neural/i.test(v.name) && !/zhiwei/i.test(v.name)) ||
      voices.find(v => v.lang === 'zh-TW' && !/zhiwei/i.test(v.name)) ||
      voices.find(v => v.lang === 'zh-TW') ||
      voices.find(v => v.lang.startsWith('zh')) ||
      null;
  };
  _pickVoice();
  window.speechSynthesis.addEventListener('voiceschanged', _pickVoice);
}

const Flashcard = {
  cards: [],
  filtered: [],
  index: 0,
  flipped: false,
  filter: 'all',
  showPinyin: true,
  showZhuyin: true,

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

  _pinyinTone(syl) {
    const map = {
      'ā':1,'á':2,'ǎ':3,'à':4,
      'ē':1,'é':2,'ě':3,'è':4,
      'ī':1,'í':2,'ǐ':3,'ì':4,
      'ō':1,'ó':2,'ǒ':3,'ò':4,
      'ū':1,'ú':2,'ǔ':3,'ù':4,
      'ǖ':1,'ǘ':2,'ǚ':3,'ǜ':4
    };
    for (const ch of syl) if (map[ch]) return map[ch];
    return 0;
  },

  _pinyinSetTone(syl, tone) {
    const rows = [
      ['ā','á','ǎ','à'], ['ē','é','ě','è'],
      ['ī','í','ǐ','ì'], ['ō','ó','ǒ','ò'],
      ['ū','ú','ǔ','ù'], ['ǖ','ǘ','ǚ','ǜ']
    ];
    for (const row of rows) {
      for (const ch of row) {
        if (syl.includes(ch)) return syl.replace(ch, row[tone - 1]);
      }
    }
    return syl;
  },

  normalizePinyin(s) {
    return s
      .replace(/ă/g, 'ǎ').replace(/ĭ/g, 'ǐ').replace(/ŏ/g, 'ǒ').replace(/ŭ/g, 'ǔ')
      .replace(/ɑ/g, 'a')
      .replace(/​/g, '');
  },

  applySandhi(pinyin, hanzi = '') {
    const s = pinyin.trim().split(/\s+/);
    const chars = [...hanzi];

    // T3 + T3 → T2 + T3
    for (let i = 0; i < s.length - 1; i++) {
      if (this._pinyinTone(s[i]) === 3 && this._pinyinTone(s[i + 1]) === 3)
        s[i] = this._pinyinSetTone(s[i], 2);
    }

    // 一 (yī): only for the actual character 一
    for (let i = 0; i < s.length - 1; i++) {
      if (s[i] === 'yī' && (chars.length === 0 || chars[i] === '一')) {
        const t = this._pinyinTone(s[i + 1]);
        s[i] = t === 4 ? 'yí' : t > 0 ? 'yì' : 'yī';
      }
    }

    // 不 (bù): only for the actual character 不, before T4 → bú (T2)
    for (let i = 0; i < s.length - 1; i++) {
      if (s[i] === 'bù' && (chars.length === 0 || chars[i] === '不') && this._pinyinTone(s[i + 1]) === 4)
        s[i] = 'bú';
    }

    return s.join(' ');
  },

  toggleZhuyin() {
    this.showZhuyin = !this.showZhuyin;
    const el = document.getElementById('fc-hanzi-el');
    if (el) el.classList.toggle('zhuyin-hidden', !this.showZhuyin);
    const btn = document.getElementById('btn-toggle-zhuyin');
    if (btn) {
      btn.classList.toggle('active', !this.showZhuyin);
      btn.textContent = this.showZhuyin ? 'ㄅ 隱藏注音' : 'ㄅ 顯示注音';
    }
    App.showToast(this.showZhuyin ? '注音符號顯示' : '注音符號隱藏');
  },

  _syllableToZhuyin(syl) {
    const toneMap = {
      'ā':['a',1],'á':['a',2],'ǎ':['a',3],'à':['a',4],
      'ē':['e',1],'é':['e',2],'ě':['e',3],'è':['e',4],
      'ī':['i',1],'í':['i',2],'ǐ':['i',3],'ì':['i',4],
      'ō':['o',1],'ó':['o',2],'ǒ':['o',3],'ò':['o',4],
      'ū':['u',1],'ú':['u',2],'ǔ':['u',3],'ù':['u',4],
      'ǖ':['ü',1],'ǘ':['ü',2],'ǚ':['ü',3],'ǜ':['ü',4]
    };
    let tone = 0;
    const bare = syl.toLowerCase().replace(/[āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]/g, c => {
      if (toneMap[c]) { const [b, t] = toneMap[c]; tone = t; return b; }
      return c;
    });
    const table = {
      // Zero initial
      'a':'ㄚ','ai':'ㄞ','an':'ㄢ','ang':'ㄤ','ao':'ㄠ',
      'e':'ㄜ','ei':'ㄟ','en':'ㄣ','eng':'ㄥ','er':'ㄦ',
      'o':'ㄛ','ou':'ㄡ',
      // Medial i (written with y-)
      'yi':'ㄧ','ya':'ㄧㄚ','ye':'ㄧㄝ','yao':'ㄧㄠ','you':'ㄧㄡ',
      'yan':'ㄧㄢ','yin':'ㄧㄣ','yang':'ㄧㄤ','ying':'ㄧㄥ','yong':'ㄩㄥ',
      // Medial u (written with w-)
      'wu':'ㄨ','wa':'ㄨㄚ','wo':'ㄨㄛ','wai':'ㄨㄞ','wei':'ㄨㄟ',
      'wan':'ㄨㄢ','wen':'ㄨㄣ','wang':'ㄨㄤ','weng':'ㄨㄥ',
      // Medial ü (written with yu-)
      'yu':'ㄩ','yue':'ㄩㄝ','yuan':'ㄩㄢ','yun':'ㄩㄣ',
      // b ㄅ
      'ba':'ㄅㄚ','bai':'ㄅㄞ','ban':'ㄅㄢ','bang':'ㄅㄤ','bao':'ㄅㄠ',
      'bei':'ㄅㄟ','ben':'ㄅㄣ','beng':'ㄅㄥ',
      'bi':'ㄅㄧ','bian':'ㄅㄧㄢ','biao':'ㄅㄧㄠ','bie':'ㄅㄧㄝ','bin':'ㄅㄧㄣ','bing':'ㄅㄧㄥ',
      'bo':'ㄅㄛ','bu':'ㄅㄨ',
      // p ㄆ
      'pa':'ㄆㄚ','pai':'ㄆㄞ','pan':'ㄆㄢ','pang':'ㄆㄤ','pao':'ㄆㄠ',
      'pei':'ㄆㄟ','pen':'ㄆㄣ','peng':'ㄆㄥ',
      'pi':'ㄆㄧ','pian':'ㄆㄧㄢ','piao':'ㄆㄧㄠ','pie':'ㄆㄧㄝ','pin':'ㄆㄧㄣ','ping':'ㄆㄧㄥ',
      'po':'ㄆㄛ','pou':'ㄆㄡ','pu':'ㄆㄨ',
      // m ㄇ
      'ma':'ㄇㄚ','mai':'ㄇㄞ','man':'ㄇㄢ','mang':'ㄇㄤ','mao':'ㄇㄠ',
      'me':'ㄇㄜ','mei':'ㄇㄟ','men':'ㄇㄣ','meng':'ㄇㄥ',
      'mi':'ㄇㄧ','mian':'ㄇㄧㄢ','miao':'ㄇㄧㄠ','mie':'ㄇㄧㄝ','min':'ㄇㄧㄣ','ming':'ㄇㄧㄥ','miu':'ㄇㄧㄡ',
      'mo':'ㄇㄛ','mou':'ㄇㄡ','mu':'ㄇㄨ',
      // f ㄈ
      'fa':'ㄈㄚ','fan':'ㄈㄢ','fang':'ㄈㄤ',
      'fei':'ㄈㄟ','fen':'ㄈㄣ','feng':'ㄈㄥ',
      'fo':'ㄈㄛ','fou':'ㄈㄡ','fu':'ㄈㄨ',
      // d ㄉ
      'da':'ㄉㄚ','dai':'ㄉㄞ','dan':'ㄉㄢ','dang':'ㄉㄤ','dao':'ㄉㄠ',
      'de':'ㄉㄜ','dei':'ㄉㄟ','den':'ㄉㄣ','deng':'ㄉㄥ',
      'di':'ㄉㄧ','dian':'ㄉㄧㄢ','diao':'ㄉㄧㄠ','die':'ㄉㄧㄝ','ding':'ㄉㄧㄥ','diu':'ㄉㄧㄡ',
      'dong':'ㄉㄨㄥ','dou':'ㄉㄡ',
      'du':'ㄉㄨ','duan':'ㄉㄨㄢ','dui':'ㄉㄨㄟ','dun':'ㄉㄨㄣ','duo':'ㄉㄨㄛ',
      // t ㄊ
      'ta':'ㄊㄚ','tai':'ㄊㄞ','tan':'ㄊㄢ','tang':'ㄊㄤ','tao':'ㄊㄠ',
      'te':'ㄊㄜ','teng':'ㄊㄥ',
      'ti':'ㄊㄧ','tian':'ㄊㄧㄢ','tiao':'ㄊㄧㄠ','tie':'ㄊㄧㄝ','ting':'ㄊㄧㄥ',
      'tong':'ㄊㄨㄥ','tou':'ㄊㄡ',
      'tu':'ㄊㄨ','tuan':'ㄊㄨㄢ','tui':'ㄊㄨㄟ','tun':'ㄊㄨㄣ','tuo':'ㄊㄨㄛ',
      // n ㄋ
      'na':'ㄋㄚ','nai':'ㄋㄞ','nan':'ㄋㄢ','nang':'ㄋㄤ','nao':'ㄋㄠ',
      'ne':'ㄋㄜ','nei':'ㄋㄟ','nen':'ㄋㄣ','neng':'ㄋㄥ',
      'ni':'ㄋㄧ','nian':'ㄋㄧㄢ','niang':'ㄋㄧㄤ','niao':'ㄋㄧㄠ','nie':'ㄋㄧㄝ','nin':'ㄋㄧㄣ','ning':'ㄋㄧㄥ','niu':'ㄋㄧㄡ',
      'nong':'ㄋㄨㄥ','nou':'ㄋㄡ',
      'nu':'ㄋㄨ','nuan':'ㄋㄨㄢ','nun':'ㄋㄨㄣ','nuo':'ㄋㄨㄛ',
      'nü':'ㄋㄩ','nüe':'ㄋㄩㄝ','nv':'ㄋㄩ','nve':'ㄋㄩㄝ',
      // l ㄌ
      'la':'ㄌㄚ','lai':'ㄌㄞ','lan':'ㄌㄢ','lang':'ㄌㄤ','lao':'ㄌㄠ',
      'le':'ㄌㄜ','lei':'ㄌㄟ','leng':'ㄌㄥ',
      'li':'ㄌㄧ','lia':'ㄌㄧㄚ','lian':'ㄌㄧㄢ','liang':'ㄌㄧㄤ','liao':'ㄌㄧㄠ','lie':'ㄌㄧㄝ','lin':'ㄌㄧㄣ','ling':'ㄌㄧㄥ','liu':'ㄌㄧㄡ',
      'long':'ㄌㄨㄥ','lou':'ㄌㄡ',
      'lu':'ㄌㄨ','luan':'ㄌㄨㄢ','lun':'ㄌㄨㄣ','luo':'ㄌㄨㄛ',
      'lü':'ㄌㄩ','lüe':'ㄌㄩㄝ','lv':'ㄌㄩ','lve':'ㄌㄩㄝ',
      // g ㄍ
      'ga':'ㄍㄚ','gai':'ㄍㄞ','gan':'ㄍㄢ','gang':'ㄍㄤ','gao':'ㄍㄠ',
      'ge':'ㄍㄜ','gei':'ㄍㄟ','gen':'ㄍㄣ','geng':'ㄍㄥ',
      'gong':'ㄍㄨㄥ','gou':'ㄍㄡ',
      'gu':'ㄍㄨ','gua':'ㄍㄨㄚ','guai':'ㄍㄨㄞ','guan':'ㄍㄨㄢ','guang':'ㄍㄨㄤ','gui':'ㄍㄨㄟ','gun':'ㄍㄨㄣ','guo':'ㄍㄨㄛ',
      // k ㄎ
      'ka':'ㄎㄚ','kai':'ㄎㄞ','kan':'ㄎㄢ','kang':'ㄎㄤ','kao':'ㄎㄠ',
      'ke':'ㄎㄜ','kei':'ㄎㄟ','ken':'ㄎㄣ','keng':'ㄎㄥ',
      'kong':'ㄎㄨㄥ','kou':'ㄎㄡ',
      'ku':'ㄎㄨ','kua':'ㄎㄨㄚ','kuai':'ㄎㄨㄞ','kuan':'ㄎㄨㄢ','kuang':'ㄎㄨㄤ','kui':'ㄎㄨㄟ','kun':'ㄎㄨㄣ','kuo':'ㄎㄨㄛ',
      // h ㄏ
      'ha':'ㄏㄚ','hai':'ㄏㄞ','han':'ㄏㄢ','hang':'ㄏㄤ','hao':'ㄏㄠ',
      'he':'ㄏㄜ','hei':'ㄏㄟ','hen':'ㄏㄣ','heng':'ㄏㄥ',
      'hong':'ㄏㄨㄥ','hou':'ㄏㄡ',
      'hu':'ㄏㄨ','hua':'ㄏㄨㄚ','huai':'ㄏㄨㄞ','huan':'ㄏㄨㄢ','huang':'ㄏㄨㄤ','hui':'ㄏㄨㄟ','hun':'ㄏㄨㄣ','huo':'ㄏㄨㄛ',
      // j ㄐ
      'ji':'ㄐㄧ','jia':'ㄐㄧㄚ','jian':'ㄐㄧㄢ','jiang':'ㄐㄧㄤ','jiao':'ㄐㄧㄠ','jie':'ㄐㄧㄝ',
      'jin':'ㄐㄧㄣ','jing':'ㄐㄧㄥ','jiong':'ㄐㄩㄥ','jiu':'ㄐㄧㄡ',
      'ju':'ㄐㄩ','juan':'ㄐㄩㄢ','jun':'ㄐㄩㄣ','jue':'ㄐㄩㄝ',
      // q ㄑ
      'qi':'ㄑㄧ','qia':'ㄑㄧㄚ','qian':'ㄑㄧㄢ','qiang':'ㄑㄧㄤ','qiao':'ㄑㄧㄠ','qie':'ㄑㄧㄝ',
      'qin':'ㄑㄧㄣ','qing':'ㄑㄧㄥ','qiong':'ㄑㄩㄥ','qiu':'ㄑㄧㄡ',
      'qu':'ㄑㄩ','quan':'ㄑㄩㄢ','qun':'ㄑㄩㄣ','que':'ㄑㄩㄝ',
      // x ㄒ
      'xi':'ㄒㄧ','xia':'ㄒㄧㄚ','xian':'ㄒㄧㄢ','xiang':'ㄒㄧㄤ','xiao':'ㄒㄧㄠ','xie':'ㄒㄧㄝ',
      'xin':'ㄒㄧㄣ','xing':'ㄒㄧㄥ','xiong':'ㄒㄩㄥ','xiu':'ㄒㄧㄡ',
      'xu':'ㄒㄩ','xuan':'ㄒㄩㄢ','xun':'ㄒㄩㄣ','xue':'ㄒㄩㄝ',
      // zh ㄓ
      'zha':'ㄓㄚ','zhai':'ㄓㄞ','zhan':'ㄓㄢ','zhang':'ㄓㄤ','zhao':'ㄓㄠ',
      'zhe':'ㄓㄜ','zhei':'ㄓㄟ','zhen':'ㄓㄣ','zheng':'ㄓㄥ','zhi':'ㄓ',
      'zhong':'ㄓㄨㄥ','zhou':'ㄓㄡ',
      'zhu':'ㄓㄨ','zhua':'ㄓㄨㄚ','zhuai':'ㄓㄨㄞ','zhuan':'ㄓㄨㄢ','zhuang':'ㄓㄨㄤ','zhui':'ㄓㄨㄟ','zhun':'ㄓㄨㄣ','zhuo':'ㄓㄨㄛ',
      // ch ㄔ
      'cha':'ㄔㄚ','chai':'ㄔㄞ','chan':'ㄔㄢ','chang':'ㄔㄤ','chao':'ㄔㄠ',
      'che':'ㄔㄜ','chen':'ㄔㄣ','cheng':'ㄔㄥ','chi':'ㄔ',
      'chong':'ㄔㄨㄥ','chou':'ㄔㄡ',
      'chu':'ㄔㄨ','chua':'ㄔㄨㄚ','chuai':'ㄔㄨㄞ','chuan':'ㄔㄨㄢ','chuang':'ㄔㄨㄤ','chui':'ㄔㄨㄟ','chun':'ㄔㄨㄣ','chuo':'ㄔㄨㄛ',
      // sh ㄕ
      'sha':'ㄕㄚ','shai':'ㄕㄞ','shan':'ㄕㄢ','shang':'ㄕㄤ','shao':'ㄕㄠ',
      'she':'ㄕㄜ','shei':'ㄕㄟ','shen':'ㄕㄣ','sheng':'ㄕㄥ','shi':'ㄕ',
      'shou':'ㄕㄡ',
      'shu':'ㄕㄨ','shua':'ㄕㄨㄚ','shuai':'ㄕㄨㄞ','shuan':'ㄕㄨㄢ','shuang':'ㄕㄨㄤ','shui':'ㄕㄨㄟ','shun':'ㄕㄨㄣ','shuo':'ㄕㄨㄛ',
      // r ㄖ
      'ran':'ㄖㄢ','rang':'ㄖㄤ','rao':'ㄖㄠ',
      're':'ㄖㄜ','ren':'ㄖㄣ','reng':'ㄖㄥ','ri':'ㄖ',
      'rong':'ㄖㄨㄥ','rou':'ㄖㄡ',
      'ru':'ㄖㄨ','ruan':'ㄖㄨㄢ','rui':'ㄖㄨㄟ','run':'ㄖㄨㄣ','ruo':'ㄖㄨㄛ',
      // z ㄗ
      'za':'ㄗㄚ','zai':'ㄗㄞ','zan':'ㄗㄢ','zang':'ㄗㄤ','zao':'ㄗㄠ',
      'ze':'ㄗㄜ','zei':'ㄗㄟ','zen':'ㄗㄣ','zeng':'ㄗㄥ','zi':'ㄗ',
      'zong':'ㄗㄨㄥ','zou':'ㄗㄡ',
      'zu':'ㄗㄨ','zuan':'ㄗㄨㄢ','zui':'ㄗㄨㄟ','zun':'ㄗㄨㄣ','zuo':'ㄗㄨㄛ',
      // c ㄘ
      'ca':'ㄘㄚ','cai':'ㄘㄞ','can':'ㄘㄢ','cang':'ㄘㄤ','cao':'ㄘㄠ',
      'ce':'ㄘㄜ','cen':'ㄘㄣ','ceng':'ㄘㄥ','ci':'ㄘ',
      'cong':'ㄘㄨㄥ','cou':'ㄘㄡ',
      'cu':'ㄘㄨ','cuan':'ㄘㄨㄢ','cui':'ㄘㄨㄟ','cun':'ㄘㄨㄣ','cuo':'ㄘㄨㄛ',
      // s ㄙ
      'sa':'ㄙㄚ','sai':'ㄙㄞ','san':'ㄙㄢ','sang':'ㄙㄤ','sao':'ㄙㄠ',
      'se':'ㄙㄜ','sen':'ㄙㄣ','seng':'ㄙㄥ','si':'ㄙ',
      'song':'ㄙㄨㄥ','sou':'ㄙㄡ',
      'su':'ㄙㄨ','suan':'ㄙㄨㄢ','sui':'ㄙㄨㄟ','sun':'ㄙㄨㄣ','suo':'ㄙㄨㄛ',
    };
    const zhuyin = table[bare];
    if (!zhuyin) return syl;
    const marks = ['˙', '', 'ˊ', 'ˇ', 'ˋ'];
    if (tone === 0) return '˙' + zhuyin;
    return zhuyin + (marks[tone] || '');
  },

  renderZhuyinRuby(vocab, pinyin) {
    // Strip parenthetical phonetic annotations like (˙ㄗ) before rendering
    const cleanVocab = vocab.replace(/\([^)]*\)/g, '').trim();
    // For variant entries like 你/妳, render each variant group separated by /
    const variants = cleanVocab.split('/');
    const syllableGroups = pinyin.trim().split('/').map(p => p.trim().split(/\s+/));
    return variants.map((variant, vi) => {
      const chars = [...variant.trim()];
      const syllables = syllableGroups[vi] || syllableGroups[0];
      const rubyStr = chars.map((char, i) => {
        const syl = syllables[i];
        if (!syl) return `<ruby>${char}<rt class="zhuyin-rt"></rt></ruby>`;
        return `<ruby>${char}<rt class="zhuyin-rt">${this._syllableToZhuyin(syl)}</rt></ruby>`;
      }).join('');
      return rubyStr;
    }).join('<span class="variant-sep">/</span>');
  },

  speak(text) {
    const cleanText = text.replace(/\([^)]*\)/g, '').trim();
    const safeText = cleanText.replace(/\//g, '／').replace(/\\/g, '＼').replace(/:/g, '：');
    const url = `audio/${encodeURIComponent(safeText)}.mp3`;

    // Reuse cached Audio object to avoid re-fetching on each click
    if (!_audioCache[url]) _audioCache[url] = new Audio(url);
    const audio = _audioCache[url];
    audio.currentTime = 0;

    audio.play().catch(() => {
      if (!window.speechSynthesis) return;
      // Chrome bug: synthesis can freeze after ~15s idle; resume first
      if (window.speechSynthesis.paused) window.speechSynthesis.resume();
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = 'zh-TW';
      utter.rate = 0.9;
      if (_zhVoice) utter.voice = _zhVoice;
      window.speechSynthesis.speak(utter);
    });
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
    const levelBadgeMap = {
      'novice1': '<span class="badge badge-novice1">Novice 1</span>',
      'novice2': '<span class="badge badge-novice2">Novice 2</span>',
      'level1':  '<span class="badge badge-level1">Elementary</span>',
      'level2':  '<span class="badge badge-level2">Pre-Inter.</span>',
    };
    const levelBadge = levelBadgeMap[card.level] || `<span class="badge badge-count">${card.level || ''}</span>`;
    const spokenPinyin = this.applySandhi(this.normalizePinyin(card.pinyin), card.vocab);
    const safeVocab = card.vocab.replace(/'/g, "\\'");
    const safePinyin = spokenPinyin.replace(/'/g, "\\'");

    area.innerHTML = `
      <div class="flashcard-scene" id="fc-scene">
        <div class="flashcard-inner${this.flipped ? ' flipped' : ''}" id="fc-inner">
          <div class="flashcard-front">
            <div class="fc-hanzi${this.showZhuyin ? '' : ' zhuyin-hidden'}" id="fc-hanzi-el">${this.renderZhuyinRuby(card.vocab, spokenPinyin)}</div>
            <div class="fc-pinyin${this.showPinyin ? '' : ' pinyin-hidden'}" id="fc-pinyin-el">${spokenPinyin}</div>
            <button class="fc-audio-btn" onclick="event.stopPropagation(); Flashcard.speak('${safeVocab}')">🔊</button>
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
        <button class="btn-toggle-zhuyin${this.showZhuyin ? '' : ' active'}" id="btn-toggle-zhuyin" onclick="Flashcard.toggleZhuyin()">
          ${this.showZhuyin ? 'ㄅ 隱藏注音' : 'ㄅ 顯示注音'}
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
