"""Konversi 論文-研討會版.md -> .docx, memakai 論文-第一至三章-v2.docx sebagai template gaya."""
import re, copy, sys
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC = r"C:\Users\user\OneDrive\文件\TOCFL\論文\論文-研討會版.md"
TPL = r"C:\Users\user\OneDrive\文件\TOCFL\論文\論文-第一至三章-v2.docx"
OUT = r"C:\Users\user\OneDrive\文件\TOCFL\論文\論文-研討會版.docx"

d = docx.Document(TPL)
body = d.element.body
for el in list(body):
    if el.tag != qn("w:sectPr"):
        body.remove(el)

def font(run, size=12, bold=False, italic=False):
    run.font.name = "Times New Roman"
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "標楷體")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic

def hyperlink(p, text, url, size):
    part = p.part
    rid = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid)
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    f = OxmlElement("w:rFonts")
    for k in ("w:ascii", "w:hAnsi"): f.set(qn(k), "Times New Roman")
    f.set(qn("w:eastAsia"), "標楷體"); rpr.append(f)
    c = OxmlElement("w:color"); c.set(qn("w:val"), "0563C1"); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rpr.append(sz)
    r.append(rpr); t = OxmlElement("w:t"); t.text = text
    t.set(qn("xml:space"), "preserve"); r.append(t); h.append(r)
    p._p.append(h)

TOKEN = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)|<(https?://[^>]+)>|\*\*(.+?)\*\*|\*(.+?)\*|(〔[^〕]*〕)")

def inline(p, text, size=12, bold=False):
    pos = 0
    for m in TOKEN.finditer(text):
        if m.start() > pos:
            font(p.add_run(text[pos:m.start()]), size, bold)
        if m.group(2):
            hyperlink(p, m.group(1), m.group(2), size)
        elif m.group(3):
            hyperlink(p, m.group(3), m.group(3), size)
        elif m.group(4):
            font(p.add_run(m.group(4)), size, True)
        elif m.group(5):
            font(p.add_run(m.group(5)), size, bold, italic=True)
        elif m.group(6):
            r = p.add_run(m.group(6)); font(r, size, bold)
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW
        pos = m.end()
    if pos < len(text):
        font(p.add_run(text[pos:]), size, bold)

def para(text, size=12, bold=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent=True,
         before=0, after=0, spacing=1.5, keep=False, hanging=None):
    p = d.add_paragraph()
    pf = p.paragraph_format
    p.alignment = align
    pf.line_spacing = spacing
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if indent: pf.first_line_indent = Pt(24)
    if hanging is not None:
        pf.left_indent = Pt(hanging); pf.first_line_indent = Pt(-hanging)
    if keep: pf.keep_with_next = True
    inline(p, text, size, bold)
    return p

def table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-{3,}:?", c) for c in r)]
    ncol = max(len(r) for r in cells)
    t = d.add_table(rows=len(cells), cols=ncol)
    t.style = d.styles["Table Grid"]
    for i, r in enumerate(cells):
        for j in range(ncol):
            cell = t.cell(i, j)
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            inline(p, r[j] if j < len(r) else "", 11, bold=(i == 0))
    # column widths proportional to the longest text in each column (min share for short columns)
    total = 8646  # letter width minus template margins, in dxa
    longest = [max(len(re.sub(r"[*〔〕]", "", r[j])) if j < len(r) else 0 for r in cells) for j in range(ncol)]
    weights = [max(L, 4) for L in longest]
    widths = [int(total * w / sum(weights)) for w in weights]
    t.autofit = False
    grid = t._tbl.tblGrid
    for j, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(widths[j]))
    for row in t.rows:
        for j, cell in enumerate(row.cells):
            cell.width = docx.shared.Twips(widths[j])
    # header row repeats across pages
    trPr = t.rows[0]._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trPr.append(th)

lines = open(SRC, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
in_refs = False
i = 0
while i < len(lines):
    l = lines[i].rstrip()
    if not l or l == "---":
        i += 1; continue
    if l.startswith("|"):
        block = []
        while i < len(lines) and lines[i].startswith("|"):
            block.append(lines[i]); i += 1
        table(block); continue
    if l.startswith("# "):
        para(l[2:], 18, True, WD_ALIGN_PARAGRAPH.CENTER, False, after=6)
    elif l.startswith("## "):
        in_refs = "參考文獻" in l
        para(l[3:], 16, True, WD_ALIGN_PARAGRAPH.CENTER, False, before=18, after=6, keep=True)
    elif l.startswith("### "):
        para(l[4:], 14, True, WD_ALIGN_PARAGRAPH.LEFT, False, before=12, after=6, keep=True)
    elif re.match(r"^（研討會版", l):
        para(l, 10, False, WD_ALIGN_PARAGRAPH.CENTER, False, after=12)
    elif re.match(r"^表\d+　", l):
        para(l, 12, False, WD_ALIGN_PARAGRAPH.CENTER, False, before=12, keep=True)
    elif l.startswith("資料來源") or (l.startswith("註") and not in_refs):
        para(l, 10, False, WD_ALIGN_PARAGRAPH.LEFT, False, spacing=1.15, after=6)
    elif l.startswith("> "):
        txt = l[2:]
        if "N ＝" in txt:
            para(txt, 12, False, WD_ALIGN_PARAGRAPH.CENTER, False, before=6, after=6)
        else:
            para(txt, 10, False, WD_ALIGN_PARAGRAPH.LEFT, False, spacing=1.15, after=6)
    elif in_refs and re.match(r"^[壹貳參]、", l):
        para(l, 12, True, WD_ALIGN_PARAGRAPH.LEFT, False, before=12, after=6, keep=True)
    elif in_refs:
        para(l, 12, False, WD_ALIGN_PARAGRAPH.LEFT, False, spacing=1.15, after=6, hanging=24)
    else:
        para(l)
    i += 1

d.core_properties.title = "以情境任務為導向之TOCFL Band A線上備考教材設計與試用研究（研討會版）"
d.save(OUT)
print("saved", OUT)
