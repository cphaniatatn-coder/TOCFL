/* Dokumen Word modul (dialog → kosakata → grammar), satu file per volume, dari data/modul_vol{1,2,3}.json.
   Pakai: npm install docx (di folder mana saja; set NODE_PATH bila perlu), lalu
     node _kerja/buat_word.js [folder_keluaran] [id|en]
   Default: folder "Modul Word" di root repo, bahasa id (data/), en = data/en/. */
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType,
  ShadingType, AlignmentType, LevelFormat, PageBreak, Footer, PageNumber, BorderStyle,
  TableOfContents,
} = require('docx');

const ROOT = path.resolve(__dirname, '..');
const OUT = path.resolve(process.argv[2] || path.join(ROOT, 'Modul Word'));
const LANG = process.argv[3] || 'id';
const DATA = path.join(ROOT, 'data', LANG === 'en' ? 'en' : '');
const T = (id, en) => (LANG === 'en' ? en : id);

const FONT = { ascii: 'Calibri', hAnsi: 'Calibri', eastAsia: 'DFKai-SB', cs: 'Calibri' };
const ZH = { ascii: 'DFKai-SB', hAnsi: 'DFKai-SB', eastAsia: 'DFKai-SB', cs: 'DFKai-SB' };
const W = 9026; // lebar isi A4, margin 1 inci

// hanzi, tanda baca CJK, zhuyin & tanda nadanya → 標楷體; sisanya Calibri
const CJK = '⺀-鿿豈-﫿︰-﹏＀-￯ˇˊˋ˙';
const RE_SEG = new RegExp(`[${CJK}]+|[^${CJK}]+`, 'g');
const RE_CJK = new RegExp(`[${CJK}]`);
const run = (text, o = {}) => (String(text ?? '').match(RE_SEG) || [''])
  .map(seg => {
    const zh = RE_CJK.test(seg);
    const size = o.size && zh && o.zhSize ? o.zhSize : o.size;
    const { zhSize, ...rest } = o;
    return new TextRun({ text: seg, font: zh ? ZH : FONT, ...rest, ...(size ? { size } : {}) });
  });
const p = (parts, o = {}) => new Paragraph({
  children: (Array.isArray(parts) ? parts : [parts]).flatMap(x => typeof x === 'string' ? run(x) : x),
  spacing: { after: 80 }, ...o,
});
const h1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: run(t) });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: run(t) });
const h3 = t => new Paragraph({ heading: HeadingLevel.HEADING_3, children: run(t) });
const bullet = parts => p(parts, { numbering: { reference: 'bul', level: 0 }, spacing: { after: 40 } });
const pb = () => new Paragraph({ children: [new PageBreak()] });

const border = { style: BorderStyle.SINGLE, size: 4, color: 'BBBBBB' };
const borders = { top: border, bottom: border, left: border, right: border };
const cellP = (parts, o = {}) => p(parts, { spacing: { after: 0 }, ...o });
function table(widths, rows, header = true) {
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({
      tableHeader: header && i === 0,
      cantSplit: true,
      children: r.map((c, j) => new TableCell({
        width: { size: widths[j], type: WidthType.DXA },
        borders,
        shading: header && i === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: 'E8EEF4' } : undefined,
        margins: { top: 50, bottom: 50, left: 90, right: 90 },
        children: (Array.isArray(c) ? c : [c]).map(x => x instanceof Paragraph ? x
          : cellP(run(String(x ?? ''), { bold: header && i === 0, size: 20, zhSize: 24 }))),
      })),
    })),
  });
}
const box = (parts, fill = 'F3F6FA') => new Paragraph({
  children: parts.flatMap(x => typeof x === 'string' ? run(x) : x),
  shading: { type: ShadingType.CLEAR, color: 'auto', fill },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: '4A7FB5', space: 6 } },
  spacing: { before: 60, after: 100 }, indent: { left: 120 },
});

// ---------- isi modul ----------
function modul(m) {
  const out = [];
  out.push(h1(`${m.code} · ${m.title}`));
  out.push(p([run(m.title_py, { color: '666666', size: 22 })], { spacing: { after: 20 } }));
  out.push(p([run(m.title_id, { italics: true, size: 22 })], { spacing: { after: 60 } }));
  out.push(p([run(T('Kategori: ', 'Category: '), { bold: true, size: 20 }), run(m.categories.join(' · '), { size: 20, zhSize: 22 })]));
  out.push(p([run(T('Situasi: ', 'Situation: '), { bold: true }), ...run(m.scene)]));
  out.push(p([run(T('Setelah bab ini, kamu bisa:', 'After this unit you can:'), { bold: true })], { spacing: { after: 40 } }));
  m.can_do.forEach(c => out.push(bullet(c)));
  if (m.exam_link) out.push(p([run(T('Kaitan dengan ujian: ', 'Exam link: '), { bold: true, size: 20 }), ...run(m.exam_link, { size: 20, color: '444444' })], { spacing: { before: 60, after: 80 } }));

  // 1. Dialog
  out.push(h2(`情境對話 · ${T('Dialog', 'Dialogue')}`));
  m.dialogs.forEach((d, i) => {
    out.push(h3(`${T('Adegan', 'Scene')} ${i + 1}: ${d.place} — ${d.title_id}`));
    out.push(table([1500, W - 1500], d.lines.map(l => [
      cellP(run(l.sp, { bold: true, size: 24 })),
      [
        cellP(run(l.zh, { size: 26 })),
        cellP(run(l.py, { size: 18, color: '777777' })),
        cellP(run(l.id, { size: 20, italics: true, color: '2E5C8A' })),
      ],
    ]), false));
    out.push(p(''));
  });

  // 2. Kosakata
  out.push(h2(`詞彙 · ${T('Kosakata', 'Vocabulary')}`));
  const head = ['No.', T('Kata', 'Word'), 'Pinyin', '注音', T('Kelas', 'POS'), T('Arti', 'Meaning')];
  const wd = [520, 1350, 1500, 1650, 800, W - 520 - 1350 - 1500 - 1650 - 800];
  const baris = (list) => [head, ...list.map((v, i) => {
    const arti = [cellP(run(v.meaning, { size: 20 }))];
    const tanda = [];
    if (v.variants) tanda.push(T('Varian: ', 'Variants: ') + v.variants.split('/').join('、'));
    if (v.maju) tanda.push(T(`dimajukan dari Level ${v.maju}`, `brought forward from Level ${v.maju}`));
    if (v.extra) tanda.push(T('di luar daftar resmi TBCL', 'outside the official TBCL list'));
    if (tanda.length) arti.push(cellP(run(tanda.join(' · '), { size: 17, color: '888888', zhSize: 19 })));
    if (v.note) arti.push(cellP(run(v.note, { size: 18, italics: true, color: '555555', zhSize: 20 })));
    return [String(i + 1), cellP(run(v.w, { size: 28, bold: true })), cellP(run(v.py, { size: 20 })),
      cellP(run(v.zy || '', { size: 20 })), cellP(run(v.pos, { size: 18 })), arti];
  })];
  out.push(h3(`${T('Kosakata inti', 'Core vocabulary')} (核心) — ${m.vocab.core.length} ${T('kata', 'words')}`));
  out.push(table(wd, baris(m.vocab.core)));
  if (m.vocab.supplement?.length) {
    out.push(h3(`${T('Kosakata tambahan', 'Supplementary vocabulary')} (補充) — ${m.vocab.supplement.length} ${T('kata', 'words')}`));
    out.push(table(wd, baris(m.vocab.supplement)));
  }

  // 3. Grammar
  out.push(h2(`語法聚焦 · ${T('Tata bahasa', 'Grammar')}`));
  (m.grammar || []).forEach((g, i) => {
    out.push(h3(`${i + 1}. ${g.point}`));
    out.push(box([run(T('Pola: ', 'Pattern: '), { bold: true, size: 20 }), ...run(g.pattern, { size: 22, zhSize: 26 })]));
    out.push(p(g.explain));
    out.push(p([run(T('Contoh:', 'Examples:'), { bold: true })], { spacing: { after: 40 } }));
    g.examples.forEach(e => out.push(bullet([...run(e.zh, { size: 26 }), run('  — ' + e.id, { italics: true, color: '2E5C8A', size: 20 })])));
    (g.catatan || []).forEach(c => {
      out.push(p([run('📘 ' + T('Catatan dari ', 'Note from ') + c.rujukan, { bold: true, size: 20, zhSize: 22 })], { spacing: { before: 100, after: 40 } }));
      c.note.forEach(n => out.push(bullet(run(n, { size: 20, zhSize: 23 }))));
    });
  });
  if (!(m.grammar || []).length) out.push(p([run(T('Tidak ada poin grammar resmi baru di bab ini; fokus pada kosakata.', 'No new official grammar point in this unit; the focus is vocabulary.'), { italics: true, color: '555555' })]));
  if (m.recycle?.length) {
    out.push(h3(T('Pola dari bab sebelumnya', 'Patterns from earlier units')));
    m.recycle.forEach(r => out.push(bullet([...run(r.zh, { size: 24 }), run('  — ' + r.id, { size: 20, color: '555555' })])));
  }
  // catatan tingkat bab: 📘 dari buku rujukan, 💡 kata fungsi (tanpa rujukan; pola lengkapnya di bab berikutnya)
  (m.catatan || []).forEach(c => {
    out.push(h3(`${c.rujukan ? '📘' : '💡'} ${c.point || T('Catatan', 'Note')}`));
    if (c.rujukan) out.push(p([run(c.rujukan, { size: 18, color: '777777', zhSize: 20 })], { spacing: { after: 40 } }));
    c.note.forEach(n => out.push(bullet(run(n, { size: 20, zhSize: 23 }))));
  });
  return out;
}

function hd(size, before, after) {
  return { run: { font: FONT, size, bold: true, color: '1F3A5F' }, paragraph: { spacing: { before, after }, keepNext: true, keepLines: true } };
}

async function volume(n) {
  const d = JSON.parse(fs.readFileSync(path.join(DATA, `modul_vol${n}.json`), 'utf8'));
  const isi = [
    p([run(d.title, { bold: true, size: 44, color: '1F3A5F' })], { alignment: AlignmentType.CENTER, spacing: { before: 2400, after: 200 } }),
    p([run(d.subtitle, { size: 26, color: '555555' })], { alignment: AlignmentType.CENTER, spacing: { after: 200 } }),
    p([run(T('Modul TOCFL Band A — dialog, kosakata, tata bahasa', 'TOCFL Band A modules — dialogue, vocabulary, grammar'), { size: 22, italics: true })], { alignment: AlignmentType.CENTER }),
    pb(),
    p([run(T('Daftar isi', 'Contents'), { bold: true, size: 32, color: '1F3A5F' })]),
    new TableOfContents(T('Daftar isi', 'Contents'), { hyperlink: true, headingStyleRange: '1-1' }),
    p([run(T('(Bila daftar isi kosong: klik kanan → Update Field di Word.)', '(If the contents list is empty: right-click → Update Field in Word.)'), { size: 18, italics: true, color: '888888' })]),
  ];
  d.modules.forEach(m => { isi.push(pb()); isi.push(...modul(m)); });

  const doc = new Document({
    creator: 'Carli', title: d.title,
    features: { updateFields: true },
    styles: {
      default: { document: { run: { font: FONT, size: 22 } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, ...hd(34, 0, 80), paragraph: { spacing: { before: 0, after: 80 }, keepNext: true, outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, ...hd(28, 280, 120), paragraph: { spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 1, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '4A7FB5', space: 2 } } } },
        { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, ...hd(23, 180, 80), paragraph: { spacing: { before: 180, after: 80 }, keepNext: true, outlineLevel: 2 } },
      ],
    },
    numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 260 } } } }] }] },
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [d.title + ' · ', PageNumber.CURRENT], size: 18, color: '888888', font: FONT })] })] }) },
      children: isi,
    }],
  });
  fs.mkdirSync(OUT, { recursive: true });
  const nama = path.join(OUT, `Modul ${d.title.replace(/[·]/g, '-').replace(/\s+/g, ' ')}${LANG === 'en' ? ' (EN)' : ''}.docx`);
  fs.writeFileSync(nama, await Packer.toBuffer(doc));
  console.log(nama, d.modules.length, 'modul');
}

(async () => { for (const n of [1, 2, 3]) await volume(n); })();
