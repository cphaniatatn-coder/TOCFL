/* Dokumen Word instrumen pre/post test modul mini dari _kerja/mini/{tes_A0,tes_A1,tes_A2,kuesioner}.json.
   Pakai: npm install docx (di folder mana saja yang bisa di-require), lalu node _kerja/mini/buat_instrumen.js "Instrumen Pre-Post Test (draf N).docx" */
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, LevelFormat, PageBreak, Footer, PageNumber, BorderStyle,
} = require('docx');

const ROOT = require('path').resolve(__dirname, '../..');   // repo utama (file ini: _kerja/mini/buat_instrumen.js)
const RD = f => JSON.parse(fs.readFileSync(ROOT + '/_kerja/mini/' + f, 'utf8'));
const TES = { A0: RD('tes_A0.json'), A1: RD('tes_A1.json'), A2: RD('tes_A2.json') };
const Q = RD('kuesioner.json');
const OUT = process.argv[2];

const FONT = { ascii: 'Calibri', hAnsi: 'Calibri', eastAsia: 'DFKai-SB', cs: 'Calibri' };
const ZH = { ascii: 'DFKai-SB', hAnsi: 'DFKai-SB', eastAsia: 'DFKai-SB', cs: 'DFKai-SB' };
const W = 9026; // lebar isi A4 dengan margin 1 inci
const ABC = 'ABCDEF';

// pecah teks per aksara supaya hanzi memakai 標楷體 dan Latin tetap Calibri
const run = (text, o = {}) => (text.match(/[一-鿿　-〿＀-￯、，。：；？！（）「」]+|[^一-鿿　-〿＀-￯、，。：；？！（）「」]+/g) || [''])
  .map(seg => new TextRun({ text: seg, font: /[一-鿿　-〿＀-￯]/.test(seg) ? ZH : FONT, ...o }));
const p = (parts, o = {}) => new Paragraph({
  children: (Array.isArray(parts) ? parts : [parts]).flatMap(x => typeof x === 'string' ? run(x) : x),
  spacing: { after: 80 }, ...o,
});
const h1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: run(t), spacing: { before: 240, after: 120 } });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: run(t), spacing: { before: 200, after: 100 } });
const h3 = t => new Paragraph({ heading: HeadingLevel.HEADING_3, children: run(t), spacing: { before: 160, after: 80 } });
const bullet = (parts) => p(parts, { numbering: { reference: 'bul', level: 0 }, spacing: { after: 40 } });
const note = t => p([run(t, { italics: true, color: '555555', size: 20 })]);
const pb = () => new Paragraph({ children: [new PageBreak()] });

const border = { style: BorderStyle.SINGLE, size: 4, color: 'BBBBBB' };
const borders = { top: border, bottom: border, left: border, right: border };
function table(widths, rows, header = true) {
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({
      tableHeader: header && i === 0,
      children: r.map((c, j) => new TableCell({
        width: { size: widths[j], type: WidthType.DXA },
        borders,
        shading: header && i === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: 'E8EEF4' } : undefined,
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        children: (Array.isArray(c) ? c : [c]).map(x => x instanceof Paragraph ? x
          : p(run(String(x), { bold: header && i === 0, size: 20 }), { spacing: { after: 0 } })),
      })),
    })),
  });
}


// ---------- isi ----------
const tri = (o, size = 20) => [
  p([run(o.id, { size })], { spacing: { after: 0 } }),
  p([run(o.en, { size: size - 2, italics: true, color: '555555' })], { spacing: { after: 0 } }),
  p([run(o.vi, { size: size - 2, italics: true, color: '2E6DA4' })], { spacing: { after: 0 } }),
];

function likertTable(items, startNo, withR) {
  const w = withR ? [500, 5226, 600, 540, 540, 540, 540, 540] : [500, 5826, 540, 540, 540, 540, 540];
  const head = ['No', 'Pernyataan / Statement / Phát biểu'].concat(withR ? ['Kode'] : []).concat(['1', '2', '3', '4', '5']);
  const rows = [head];
  // butir dengan versi 'baru': teks biasa untuk yang pernah ikut TOCFL, teks kedua untuk yang belum pernah
  const isi = it => !it.baru ? tri(it) : [
    p([run('Pernah ikut TOCFL:', { size: 16, bold: true, color: '888888' })], { spacing: { after: 0 } }), ...tri(it),
    p([run('Belum pernah ikut TOCFL:', { size: 16, bold: true, color: 'B45309' })], { spacing: { before: 80, after: 0 } }), ...tri(it.baru),
  ];
  items.forEach((it, i) => rows.push([String(startNo + i), isi(it)].concat(withR ? [it.r ? '(R)' : ''] : []).concat(['☐', '☐', '☐', '☐', '☐'])));
  return table(w, rows);
}

function soal(t) {
  const out = [];
  const nomor = t.type === 'cloze' ? `${t.no}–${t.no + t.answers.length - 1}` : String(t.no);
  out.push(p([run(`${nomor}. `, { bold: true }), run(t.part, { bold: true }), run(`  ·  ${t.tema}`, { color: '666666', size: 20 })], { spacing: { before: 160, after: 60 }, keepNext: true }));
  if (t.picture) out.push(p([run('[Gambar] ', { bold: true, color: '2E6DA4', size: 20 }), run(t.picture.label, { italics: true, size: 20 })], { keepNext: true }));
  if (t.type.startsWith('listen')) {
    // urutan bunyi sama dengan TocflAudio (web/js/studi.js); 🔔 = bunyi bel (t.bel, bawaan: sebelum 問 di Part 2–4)
    const pic = t.type === 'listen_pic';
    const klip = pic ? ['問：' + t.question, '（A）（B）（C）'] : [...t.lines.map(l => `${l.sp}：${l.zh}`), '問：' + t.question];
    const pos = b => pic ? { 0: 0, 1: 1, 4: 2 }[b] : b, bel = t.bel || (pic ? [] : [t.lines.length]);
    out.push(p([run(`Naskah audio (🔔 = bunyi bel${pic ? '; pilihan tidak tercetak untuk peserta' : '; 問 hanya dibacakan, tidak tercetak'}):`, { size: 20, color: '666666' })], { keepNext: true }));
    [...klip, null].forEach((k, i) => {
      if (bel.some(b => pos(b) === i)) out.push(p([run('🔔', { color: 'B45309' })], { indent: { left: 360 }, spacing: { after: 20 }, keepNext: true }));
      if (k) out.push(p([run(k)], { indent: { left: 360 }, spacing: { after: 20 }, keepNext: true }));
    });
  }
  if (t.text) out.push(p([run(t.text)], { indent: { left: 360 }, keepNext: true }));
  if (t.question && !t.type.startsWith('listen')) out.push(p([run('問：' + t.question)], { indent: { left: 360 }, keepNext: true }));
  return out.concat(t.options.map((o, i) => typeof o === 'string'
    ? p([run(`(${ABC[i]}) `), run(o)], { indent: { left: 720 }, spacing: { after: 20 } })
    : p([run(`(${ABC[i]}) `), run('[gambar] ', { color: '2E6DA4', size: 20 }), run(o.label, { italics: true, size: 20 })], { indent: { left: 720 }, spacing: { after: 20 } })));
}

function kunci(items) {
  const rows = [['No', 'Kunci', 'Alasan & pengecoh']];
  for (const t of items) {
    if (t.type === 'cloze') t.answers.forEach((a, i) => rows.push([String(t.no + i), ABC[a], i === 0 ? t.why : '']));
    else rows.push([String(t.no), ABC[t.answer], t.why]);
  }
  return table([600, 800, 7626], rows);
}

const BP_DENGAR = [
  ['聽力 Part 1', 'Gambar + pertanyaan + 3 jawaban lisan', '4', '1–4'],
  ['聽力 Part 2', 'Tanya-jawab 2 baris → 3 gambar', '3', '5–7'],
  ['聽力 Part 3', 'Dialog 4 baris + 問 → 3 gambar', '2', '8–9'],
  ['聽力 Part 4', 'Dialog 4 baris → 4 opsi teks (inferensial)', '1', '10'],
];
const BP = {
  A0: BP_DENGAR.concat([
    ['閱讀 Part 1', 'Kalimat → 3 gambar', '2', '11–12'],
    ['閱讀 Part 2', 'Gambar → 3 kalimat', '2', '13–14'],
    ['閱讀 Part 3', 'Gambar + kalimat rumpang → 3 kata', '2', '15–16'],
    ['閱讀 Part 4', 'Paragraf, 3 titik kosong + 4 pilihan', '3', '17–19'],
    ['閱讀 Part 5', 'Wacana pendek + 4 opsi', '1', '20'],
  ]),
  A1: BP_DENGAR.concat([
    ['閱讀 Part 1', 'Kalimat → 3 gambar', '1', '11'],
    ['閱讀 Part 2', 'Gambar → 3 kalimat', '1', '12'],
    ['閱讀 Part 3', 'Gambar + kalimat rumpang → 3 kata', '1', '13'],
    ['閱讀 Part 4', 'Paragraf, 5 titik kosong + 6 pilihan', '5', '14–18'],
    ['閱讀 Part 5', 'Wacana pendek + 4 opsi', '2', '19–20'],
  ]),
};
BP.A2 = BP.A1.map(r => r[0] === '閱讀 Part 4' ? [r[0], 'Paragraf ±100 hanzi, 5 titik kosong + 6 pilihan FRASA', r[2], r[3]] : r);
const BATAS = { A0: 'TBCL Level 1 (sampai A25)', A1: 'TBCL Level 1–2 (sampai B46)', A2: 'TBCL Level 1–3 (sampai C67)' };

const children = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: run('Instrumen Pre-test & Post-test', { bold: true, size: 36 }) }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: run('Uji Coba Modul Mini TOCFL Band A (A0 · A1 · A2)', { size: 26 }) }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, children: run('Draf 7 · 5 Oktober 2026 · untuk ditinjau bersama pembimbing', { italics: true, color: '666666', size: 20 }) }),

  h1('1. Desain uji coba'),
  p('Tujuan: mengetahui (1) apakah modul menurunkan kecemasan peserta terhadap ujian TOCFL dan (2) apakah kemampuan peserta pada tema & grammar yang sering diujikan meningkat setelah memakai modul.'),
  p('Desain: satu kelompok, pre-test – perlakuan – post-test (one-group pretest–posttest). Peserta memilih level sendiri (A0/A1/A2) dan hanya mengerjakan 6 bab di level itu. Bahasa instrumen: Indonesia, English, Tiếng Việt (dipilih peserta).'),
  table([2000, 4226, 2800], [
    ['Tahap', 'Isi', 'Perkiraan waktu'],
    ['1. Pre-test', 'Bagian I Data peserta + Bagian II Skala kecemasan + Bagian III Tes kemampuan (Paket A)', '± 5 + 5 + 30 menit'],
    ['2. Modul', '6 bab level yang dipilih: 6 tahap + soal latihan + Tes Bab', '± 30–40 menit per bab'],
    ['3. Post-test', 'Bagian II Skala kecemasan (sama persis) + Bagian III Tes kemampuan (Paket B) + Bagian IV Evaluasi modul', '± 5 + 30 + 5 menit'],
  ]),
  p(''),
  p('Di aplikasi: pre-test wajib selesai sebelum bab terbuka; post-test baru terbuka setelah keenam bab selesai. Semua jawaban & waktu pengerjaan dikirim ke Google Sheet.'),
  h3('Bab yang dipakai (tema & grammar yang paling sering muncul di mock test)'),
  table([1000, 8026], [
    ['Level', 'Bab'],
    ['A0', 'A02 asal negara (嗎, 這/那/哪) · A04 keluarga (數+量) · A09 posisi benda (地點表達) · A10 rutinitas & jam · A18 harga · A24 cuaca'],
    ['A1', 'B04 sedang melakukan apa (在/正在, 呢) · B19 perbandingan cuaca (比, 跟…一樣) · B20 pakaian (太…了, 有一點) · B30 arah (從…往, V到) · B33 perjalanan (是…的, V了) · B40 izin sakit (因為…所以, 但是)'],
    ['A2', 'C04 menata rumah (把) · C16 kantor (必須, 不用) · C24 rencana & cuaca (要是…就, …的話) · C28 sakit (被, V掉) · C40 diskon (一M比一M) · C58 kejutan (不但…而且)'],
  ]),

  h1('2. Dasar dari kuesioner awal'),
  p('Kuesioner awal 「華語文能力測驗調查」 (25 responden: 24 Indonesia, 1 Vietnam; 22 pernah ikut ujian) dipakai untuk menyusun butir. Kendala yang paling banyak disebut dipetakan ke butir Bagian II, dan harapan terhadap bahan ajar dipetakan ke Bagian IV:'),
  table([5226, 1800, 2000], [['Kendala / harapan (jumlah responden)', 'Bagian II', 'Bagian IV']].concat((() => {
    const m = {};
    let n = 1;
    Q.cemas.forEach(d => d.items.forEach(it => { if (it.kendala) (m[it.kendala] = m[it.kendala] || { a: [], b: [] }).a.push(n); n++; }));
    Q.eval.forEach((it, i) => { if (it.harapan) (m['Harapan: ' + it.harapan] = m['Harapan: ' + it.harapan] || { a: [], b: [] }).b.push(i + 1); });
    return Object.entries(m).map(([k, v]) => [k, v.a.join(', ') || '—', v.b.join(', ') || '—']);
  })())),

  h1('3. Dasar penyusunan & rujukan instrumen'),
  p('Tidak ada bagian yang mengambil (mengadopsi) instrumen baku apa adanya. Semua butir disusun baru dengan mengacu pada rujukan di bawah dan pada hasil kuesioner awal. Konsekuensinya, validitas dan reliabilitas harus dibuktikan sendiri di penelitian ini (lihat Catatan untuk pembimbing).'),
  table([1900, 3626, 3500], [
    ['Komponen', 'Rujukan', 'Cara dipakai'],
    ['Desain penelitian', 'Campbell & Stanley (1963): one-group pretest–posttest design', 'Satu kelompok diukur sebelum & sesudah memakai modul. Keterbatasan: tanpa kelompok kontrol, sehingga perubahan skor tidak bisa sepenuhnya dipastikan berasal dari modul.'],
    ['Bagian I Data peserta', 'Kuesioner awal 「華語文能力測驗調查」 (25 responden)', 'Kategori jawaban disamakan agar hasil uji coba bisa dibandingkan dengan kuesioner awal.'],
    ['Bagian II Skala kecemasan', 'FLCAS (Horwitz, Horwitz & Cope, 1986); FLRAS (Saito, Horwitz & Garza, 1999); kecemasan menyimak (Kim, 2000); skala Likert (Likert, 1932)', 'Dimensi diambil dari konsep ketiga skala: kecemasan umum/takut dinilai (A), kecemasan menyimak (B), kecemasan membaca (C), kepercayaan diri (D). Isi butir diturunkan dari kendala yang paling sering disebut di kuesioner awal. Kalimat butir BUKAN terjemahan atau kutipan skala asli.'],
    ['Bagian III Tes kemampuan', 'Format TOCFL Band A (國家華語測驗推動工作委員會, SC-TOP); 臺灣華語文能力基準 TBCL (國家教育研究院)', 'Bagian 聽力 Part 1–4 dan 閱讀 Part 1–5 meniru bentuk soal TOCFL Band A. Kosakata & grammar dibatasi pada level TBCL peserta (dicek otomatis). Semua soal baru, bukan soal asli TOCFL.'],
    ['Bagian IV Evaluasi modul', 'Harapan terhadap bahan ajar di kuesioner awal', 'Disusun sendiri; tiap butir dipetakan ke satu harapan responden (tabel di bagian 2).'],
  ]),
  note('Draf butir dan terjemahannya disusun dengan bantuan Claude (AI). Setiap rujukan di atas wajib dicocokkan dengan sumber aslinya sebelum dikutip di thesis.'),

  h1('Bagian I — Data peserta (pre-test saja)'),
  note('Kategori disamakan dengan kuesioner awal agar hasilnya bisa dibandingkan.'),
  bullet('Kode peserta (dibuat otomatis oleh aplikasi) dan nama/inisial'),
  bullet('Usia: 15–18 / 19–25 / 26–35 / > 35 tahun'),
  bullet('Kewarganegaraan: Indonesia / Vietnam / lainnya: ____'),
  bullet('Kemampuan Mandarin saat ini (penilaian diri): A0 / A1 / A2'),
  bullet('Pernah mengikuti ujian kemampuan bahasa Mandarin (TOCFL)? Ya / Tidak — bila ya, level & tahun: ____'),
  bullet('Lama belajar bahasa Mandarin: < 6 bulan / 6–12 bulan / 1–2 tahun / > 2 tahun'),
  bullet('Rencana mengikuti TOCFL: ≤ 3 bulan lagi / 3–6 bulan / > 6 bulan / belum tahu'),
  bullet('Level yang dipilih untuk uji coba:'),
  table([1000, 8026], [['Level', 'Deskripsi untuk membantu peserta memilih']].concat(['A0', 'A1', 'A2'].map(l => [l, tri(Q.level[l])]))),

  h1('Bagian II — Skala Kecemasan Ujian TOCFL (pre-test & post-test, identik)'),
  note('Butir disusun sendiri dengan mengacu pada dimensi kecemasan bahasa asing FLCAS (Horwitz, Horwitz & Cope, 1986), kecemasan membaca (FLRAS; Saito, Horwitz & Garza, 1999), dan kecemasan menyimak (Kim, 2000), lalu disesuaikan dengan kendala dari kuesioner awal. Kalimatnya bukan kutipan skala aslinya. Rujukan WAJIB diverifikasi sebelum dipakai di thesis.'),
  p([run('Dua versi kalimat: ', { bold: true }), run('butir 3, 5, 6, dan 10 punya kalimat kedua untuk peserta yang menjawab "Tidak" pada pertanyaan "Pernah mengikuti TOCFL?" di Bagian I, karena kalimat aslinya mengandaikan pengalaman ujian. Aplikasi memilih versinya otomatis, dan versi yang sama dipakai di pre-test dan post-test. Isi yang diukur tetap sama, jadi nomor butir dan penskoran tidak berubah. Peserta yang belum pernah ikut juga melihat petunjuk tambahan berikut:')]),
  ...tri(Q.petunjuk_baru, 20),
  p(''),
  ...tri(Q.likert, 20),
];
let no = 1;
for (const d of Q.cemas) {
  children.push(h3(`${d.dim.id} / ${d.dim.en} / ${d.dim.vi}`));
  children.push(likertTable(d.items, no, true));
  no += d.items.length;
}
children.push(
  p(''),
  p([run('Penskoran: ', { bold: true }), run('butir bertanda (R) dibalik (1↔5, 2↔4). Skor total 20–100; makin tinggi = makin cemas. Skor per dimensi (A–D) dilaporkan terpisah. Kode (R) TIDAK ditampilkan kepada peserta, dan urutan butir di aplikasi bisa diacak.')]),
  p([run('Analisis yang disarankan: ', { bold: true }), run('reliabilitas Cronbach α (pre-test); perbandingan pre vs post dengan uji-t berpasangan, atau Wilcoxon bila sampel kecil/tidak normal; dilaporkan per level dan keseluruhan.')]),

  pb(),
  h1('Bagian III — Tes Kemampuan bergaya TOCFL'),
  p('Tiap level punya dua paket setara: Paket A untuk pre-test, Paket B untuk post-test. Butir bernomor sama di kedua paket setara (bagian ujian, tema, dan tingkat kesulitan sama; kalimat & jawaban berbeda). Semua butir baru — tidak sama dengan soal latihan atau Tes Bab di modul. 20 butir per paket, ± 30 menit.'),
  p([run('Audio 聽力 (meniru TOCFL): ', { bold: true }), run('tombol putar hanya bisa ditekan sekali, lalu seluruh naskah diputar otomatis 2 kali (jeda ±2,5 detik), kecepatan normal (1×) tanpa pilihan kecepatan, dengan jeda antarkalimat. Part 1: 問 lalu pilihan A, B, C dibacakan. Part 2–4: dialog, lalu bunyi bel 🔔, lalu 問 dibacakan; teks 問 tidak tercetak di layar. Posisi bel per soal ditandai 🔔 di naskah audio.')]),
  note('Semua teks Mandarin sudah dicek otomatis (py _kerja/mini/cek_tes.py): hanya memakai kosakata TBCL sampai level peserta, tanpa pola grammar di atas levelnya. Gambar di draf ini masih berupa deskripsi; versi akhir memakai ilustrasi hitam-putih bergaya TOCFL seperti di aplikasi.'),
);
for (const lv of ['A0', 'A1', 'A2']) {
  children.push(h2(`Kisi-kisi ${lv} — kosakata: ${BATAS[lv]}`));
  children.push(table([1500, 4526, 1000, 2000], [['Bagian', 'Format', 'Butir', 'Nomor']].concat(BP[lv])));
  for (const [f, nama] of [['A', `Paket A — Pre-test ${lv}`], ['B', `Paket B — Post-test ${lv}`]]) {
    const T = TES[lv][f];
    children.push(pb(), h2(nama));
    children.push(p([run('聽力 (menyimak)', { bold: true })]));
    T.filter(t => t.part.startsWith('聽')).forEach(t => children.push(...soal(t)));
    children.push(p([run('閱讀 (membaca)', { bold: true })], { spacing: { before: 240, after: 80 } }));
    T.filter(t => t.part.startsWith('閱')).forEach(t => children.push(...soal(t)));
    children.push(h3('Kunci jawaban ' + nama.split(' — ')[0] + ' ' + lv), kunci(T));
  }
  children.push(pb());
}

children.push(
  h1('Bagian IV — Evaluasi modul (post-test saja)'),
  ...tri(Q.likert, 20),
  likertTable(Q.eval, 1, false),
  h3('Pertanyaan terbuka'),
  ...Q.terbuka.flatMap((o, i) => [p([run(`${i + 1}. `, { bold: true }), run(o.id)], { spacing: { after: 0 } }), p([run(o.en, { italics: true, color: '555555', size: 20 })], { indent: { left: 280 }, spacing: { after: 0 } }), p([run(o.vi, { italics: true, color: '2E6DA4', size: 20 })], { indent: { left: 280 }, spacing: { after: 120 } })]),

  h1('Catatan untuk dibahas dengan pembimbing'),
  bullet('Validitas isi: butir skala kecemasan & tes kemampuan sebaiknya ditinjau ahli (expert judgment) sebelum dipakai.'),
  bullet('Terjemahan: teks English & Tiếng Việt disiapkan Claude; perlu dicek penutur asli (idealnya back-translation) agar skor antarbahasa sebanding.'),
  bullet('Paket A/B: bila ingin menghindari perbedaan tingkat kesulitan antarpaket, separuh peserta dapat mengerjakan B → A (counterbalancing).'),
  bullet('Peserta memilih level sendiri. Hasil pre-test bisa dipakai untuk memeriksa apakah pilihan level masuk akal (mis. skor sangat tinggi/rendah).'),
  bullet('Butir 3, 5, 6, 10 punya dua versi kalimat (pernah / belum pernah ikut TOCFL). Saat analisis, laporkan juga hasil per kelompok "pernah" dan "belum pernah" (kolom pernah_tocfl di Google Sheet), dan periksa apakah kedua versi berperilaku sama (mis. Cronbach α per kelompok).'),
  bullet('Karena butir skala disusun sendiri (bukan FLCAS/FLRAS asli), perlu uji coba terbatas (pilot) dan Cronbach α sebelum data utama dikumpulkan.'),

  h1('Daftar pustaka'),
  note('Format APA 7. Tetap cocokkan tahun, volume, dan halaman dengan sumber asli; entri bertanda [cek] belum lengkap.'),
  ...[
    'Campbell, D. T., & Stanley, J. C. (1963). Experimental and quasi-experimental designs for research. Rand McNally.',
    'Horwitz, E. K., Horwitz, M. B., & Cope, J. (1986). Foreign language classroom anxiety. The Modern Language Journal, 70(2), 125–132.',
    'Kim, J.-H. (2000). Foreign language listening anxiety: A study of Korean students learning English [Doctoral dissertation, The University of Texas at Austin].',
    'Likert, R. (1932). A technique for the measurement of attitudes. Archives of Psychology, 22(140), 1–55.',
    'Saito, Y., Horwitz, E. K., & Garza, T. J. (1999). Foreign language reading anxiety. The Modern Language Journal, 83(2), 202–218.',
    '國家華語測驗推動工作委員會 (SC-TOP). (t.t.). 華語文能力測驗 TOCFL 準備級・入門基礎級 (Band A) 測驗說明. [cek: judul halaman, tahun, URL]',
    '國家教育研究院. (t.t.). 臺灣華語文能力基準 (Taiwan Benchmarks for the Chinese Language, TBCL). [cek: tahun terbit & URL]',
  ].map(t => p(t, { indent: { left: 540, hanging: 540 }, spacing: { after: 100 } })),
);

const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 30, bold: true, color: '1F3864', font: FONT }, paragraph: { outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 26, bold: true, color: '2E6DA4', font: FONT }, paragraph: { outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 23, bold: true, color: '333333', font: FONT }, paragraph: { outlineLevel: 2 } },
    ],
  },
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: '888888' })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b); console.log('ditulis', OUT); });
