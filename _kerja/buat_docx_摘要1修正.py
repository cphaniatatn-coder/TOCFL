"""摘要1.docx -> 摘要1-修正版.docx sesuai 論文專書撰寫體例 (1120808)."""
import re, sys
import docx
from docx.shared import Pt, Cm, Twips
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_COLOR_INDEX
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

sys.stdout.reconfigure(encoding="utf-8")
SRC = r"C:\Users\user\OneDrive\文件\tocfl-mini\摘要1.docx"
OUT = r"C:\Users\user\OneDrive\文件\tocfl-mini\摘要1-修正版.docx"
ZH, EN = "新細明體", "Times New Roman"
C, L, J = WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.JUSTIFY

# ---------- baca isi asli (paragraf & tabel berurutan) ----------
src = docx.Document(SRC)
items = []
for el in src.element.body:
    if el.tag == qn("w:p"):
        t = "".join(x.text or "" for x in el.iter(qn("w:t"))).strip()
        if t:
            items.append(("p", t))
    elif el.tag == qn("w:tbl"):
        tb = docx.table.Table(el, src)
        items.append(("t", [[c.text.strip() for c in r.cells] for r in tb.rows]))

# ---------- dokumen baru ----------
d = docx.Document()
st = d.styles["Normal"]
st.font.name = EN; st.font.size = Pt(12)
st.element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), ZH)
s = d.sections[0]
s.page_width, s.page_height = Cm(21), Cm(29.7)
s.top_margin = s.bottom_margin = Cm(2.54)
s.left_margin = s.right_margin = Cm(3.18)

# nomor halaman di tengah bawah
fp = s.footer.paragraphs[0]; fp.alignment = C
r = fp.add_run()
for tag, txt in (("begin", None), (None, "PAGE"), ("end", None)):
    if tag:
        e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), tag)
    else:
        e = OxmlElement("w:instrText"); e.set(qn("xml:space"), "preserve"); e.text = txt
    r._r.append(e)

def setfont(run, size=12, bold=False, italic=False):
    run.font.name = EN
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), ZH)
    run.font.size = Pt(size); run.bold = bold; run.italic = italic

def hyperlink(p, url):
    rid = p.part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid)
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    f = OxmlElement("w:rFonts"); f.set(qn("w:ascii"), EN); f.set(qn("w:hAnsi"), EN); f.set(qn("w:eastAsia"), ZH); rpr.append(f)
    c = OxmlElement("w:color"); c.set(qn("w:val"), "0563C1"); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    r.append(rpr); t = OxmlElement("w:t"); t.text = url; t.set(qn("xml:space"), "preserve"); r.append(t)
    h.append(r); p._p.append(h)

TOK = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*|(〔[^〕]*〕)|<(https?://[^>]+)>")
def inline(p, text, size=12, bold=False):
    pos = 0
    for m in TOK.finditer(text):
        if m.start() > pos:
            setfont(p.add_run(text[pos:m.start()]), size, bold)
        if m.group(1):
            setfont(p.add_run(m.group(1)), size, True)
        elif m.group(2):
            setfont(p.add_run(m.group(2)), size, bold, True)
        elif m.group(3):
            rr = p.add_run(m.group(3)); setfont(rr, size, bold)
            rr.font.highlight_color = WD_COLOR_INDEX.YELLOW
        else:
            hyperlink(p, m.group(4))
        pos = m.end()
    if pos < len(text):
        setfont(p.add_run(text[pos:]), size, bold)

def para(text, size=12, bold=False, align=J, first=24, left=0, before=0, after=0, keep=False):
    p = d.add_paragraph(); pf = p.paragraph_format
    p.alignment = align; pf.line_spacing = 1.0
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    pf.left_indent = Pt(left); pf.first_line_indent = Pt(first)
    pf.keep_with_next = keep
    inline(p, text, size, bold)
    return p

def pagebreak():
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

CJK = r"[\u3400-\u9fff\u3000-\u303f\uff00-\uffef「」『』（）]"
def zh_punct(t):
    """Tanda baca dalam kalimat Mandarin -> lebar penuh; teks Inggris dibiarkan."""
    t = t.replace("(", "（").replace(")", "）")
    for h, f in ((",", "，"), (":", "："), (";", "；")):
        t = re.sub(rf"(?<={CJK}){re.escape(h)}\s*|\s*{re.escape(h)}(?={CJK})", f, t)
    return t.replace("\t", "")

# ---------- halaman judul Mandarin: teks ASLI (sudah dikirim ke penguji), hanya format yang diubah ----------
orig = [x for k_, x in items if k_ == "p"]
TITLE_ZH = orig[1]
i_abs = orig.index("摘要")
i_kw = next(i for i, x in enumerate(orig) if x.startswith("關鍵詞"))
ABS_ZH = orig[i_abs + 1:i_kw]
KW_ZH = orig[i_kw]

para(TITLE_ZH, 18, True, C, 0, after=24)
para("摘要", 16, True, C, 0, before=12, after=12)
for t in ABS_ZH:
    para(t)
lab, _, rest = KW_ZH.partition("：")
para(f"**{lab}：**{rest}", align=L, first=0, before=24)
pagebreak()

# ---------- halaman judul Inggris: terjemahan langsung abstrak asli ----------
TITLE_EN = ("Editing and Design of Test-Preparation Materials for the Test of Chinese as a Foreign Language: "
            "Applying the ADDIE Model")
ABS_EN = [
    "The Test of Chinese as a Foreign Language (TOCFL) is a standardized test administered by the Steering Committee for the Test of "
    "Proficiency–Huayu (SC-TOP), and it serves as proof of language proficiency for international and overseas Chinese students who wish "
    "to study or work in Taiwan. As the number of students coming to Taiwan for higher education increases, most test takers must pass this "
    "test to meet admission requirements, yet they commonly face high test anxiety, insufficient answering time, limited vocabulary, and a "
    "lack of understanding of grammar in context, while targeted digital interactive materials are still lacking on the market. This study "
    "therefore aims to develop an HTML5 interactive learning module for TOCFL beginner-level (Band A) test takers, corresponding to Levels 1 "
    "to 3 of the Taiwan Benchmarks for the Chinese Language (TBCL) (i.e., A0, A1, and A2), to help learners become familiar with the item "
    "types in a short time, reduce cognitive load, and improve the effectiveness of self-directed learning.",
    "Based on a needs survey, this study applies all five phases of the ADDIE model for research and development. With "
    "“situation first” as its core, the design phase thoroughly integrates five major theories: Mayer’s multimedia learning "
    "principles are used to optimize audiovisual presentation, Sweller’s cognitive load theory (through “building-block grammar”) "
    "to control intrinsic load, and Bachman and Palmer’s language testing framework to ensure authenticity, while Zimmerman’s "
    "self-regulated learning (SRL) theory is introduced to provide process tracking and reflective feedback. Through a field trial and outcome "
    "evaluation, the study not only produces interactive materials for self-study but also verifies the module’s actual effectiveness in "
    "reducing anxiety and improving test performance, offering a reference for the future design and practice of digital Chinese teaching materials.",
]
KW_EN = "Test of Chinese as a Foreign Language (TOCFL), ADDIE model, digital learning, cognitive load theory, self-regulated learning"

para(TITLE_EN, 18, True, C, 0, after=24)
para("Abstract", 16, True, C, 0, before=12, after=12)
for t in ABS_EN:
    para(t)
para("**Keywords:** " + KW_EN, align=L, first=0, before=24)
pagebreak()

# ---------- isi ----------
H1 = {"緒論": "壹、緒論", "文獻探討": "貳、文獻探討", "研究方法": "參、研究方法",
      "研究結果": "肆、研究結果", "結論": "伍、結論"}
H2 = {
    "第一節 研究動機與研究背景": "一、研究動機與研究背景",
    "第二節 研究目的與研究問題": "二、研究目的與研究問題",
    "華語文能力測驗與臺灣華語文能力基準": "一、華語文能力測驗與臺灣華語文能力基準",
    "考試焦慮": "二、考試焦慮",
    "任務型語言教學": "三、任務型語言教學",
    "認知負荷與多媒體學習": "四、認知負荷與多媒體學習",
    "自主學習與行動學習": "五、自主學習與行動學習",
    "研究缺口": "六、研究缺口",
    "研究設計": "一、研究設計",
    "教材設計與發展": "二、教材設計與發展",
    "試用版與研究對象": "三、試用版與研究對象",
    "研究工具": "四、研究工具",
    "研究流程與資料分析": "五、研究流程與資料分析",
}
NUM = "一二三四五六七八九"
PLACE = {
    "肆、研究結果": "〔待補：試用結果。依目前字數，本章與結論合計約可再寫1,700字（全文上限10,000字，含摘要、圖表與參考文獻）〕",
    "伍、結論": "〔待補：結論與建議〕",
}

def table(rows):
    ncol = max(len(r) for r in rows)
    t = d.add_table(rows=len(rows), cols=ncol); t.style = d.styles["Table Grid"]
    t.alignment = 1
    total = 8300  # lebar teks A4 dengan margin 3.18 cm, dxa
    longest = [max(len(r[j]) if j < len(r) else 0 for r in rows) for j in range(ncol)]
    # kolom pendek diberi lebar pas (240 dxa per karakter 12pt), sisanya dibagi ke kolom panjang
    need = [max(x, 2) * 240 + 240 for x in longest]
    short = [j for j in range(ncol) if need[j] <= total * 0.3]
    if len(short) == ncol:
        widths = [int(total * n / sum(need)) for n in need]
    else:
        rest = total - sum(need[j] for j in short)
        longw = sum(longest[j] for j in range(ncol) if j not in short)
        widths = [need[j] if j in short else int(rest * longest[j] / longw) for j in range(ncol)]
    t.autofit = False
    for j, gc in enumerate(t._tbl.tblGrid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(widths[j]))
    for i, r in enumerate(rows):
        for j in range(ncol):
            cell = t.cell(i, j); cell.width = Twips(widths[j])
            p = cell.paragraphs[0]; p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.keep_with_next = i < len(rows) - 1  # tabel tidak terpotong halaman
            p.alignment = C if (i == 0 or len(r[j] if j < len(r) else "") <= 12) else L
            inline(p, zh_punct(r[j] if j < len(r) else ""), 12)
    trPr = t.rows[0]._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trPr.append(th)

started = False
prev = None
k = 0
while k < len(items):
    kind, x = items[k]; k += 1
    if kind == "p" and x == "緒論":
        started = True
    if not started:
        continue
    if kind == "t":
        table(x)
        if not (k < len(items) and items[k][0] == "p" and re.match(r"^[（(](本研究|研究者)整理|^資料來源", items[k][1])):
            para("", first=0)  # spasi satu baris sesudah tabel tanpa sumber
        continue
    t = zh_punct(x)
    if x in H1:
        h = H1[x]
        para(h, 16, True, C, 0, before=0 if prev is None else 12, after=12, keep=True)
        prev = "h1"
        if h in PLACE:
            para(PLACE[h])
        continue
    if x.strip() in H2:
        para(H2[x.strip()], 14, True, L, 0, before=0 if prev == "h1" else 12, after=12, keep=True)
        prev = "h2"; continue
    prev = "p"
    m = re.match(r"^([一二三四五六七八九])、(.*)$", t)
    if m:  # butir daftar (pertanyaan penelitian, instrumen) -> （一）
        para(f"（{m.group(1)}）{m.group(2)}", first=-36, left=36)
        continue
    if re.match(r"^表\d+", t):
        t = re.sub(r"^(表\d+)\s*", r"\1　", t)
        para(t, align=C, first=0, before=12, keep=True)
        continue
    if t in ("（本研究整理）", "（研究者整理）"):
        t = "資料來源：研究者整理。"
    if t.startswith("資料來源"):
        para(t, align=L, first=0, after=12)
        continue
    if t.startswith("N ＝"):
        para(t, align=C, first=0, before=6, after=6)
        continue
    # koreksi isi kecil
    t = t.replace("曾文璇等，2023", "曾文璇等人，2023")
    t = t.replace("2026年10月15日選項隨機化", "2026年10月8日選項隨機化")
    para(t)

# ---------- 參考文獻 ----------
para("參考文獻", 12, True, L, 0, before=24, after=12, keep=True)
REFS_ZH = [
    "白芬茹（2017）。**行動載具運用於漢字教學的學習成效之探討——以智慧型手機結合即時通訊軟體LINE為例**（未出版碩士論文）。國立臺灣師範大學。",
    "施俐綺（2025）。**生成式AI在華語文分級測驗試題編寫之應用研究——與TOCFL試題之比較分析**（未出版碩士論文）。國立臺灣師範大學。",
    "國家華語測驗推動工作委員會（2021）。**TOCFL成績單新增TBCL對應欄位答客問**。國家華語測驗推動工作委員會。取自 <https://tocfl.edu.tw/assets/files/announcement/TOCFLandTBCL01.pdf>",
    "國家華語測驗推動工作委員會（n.d.）。**華語文能力測驗聽讀測驗模擬試題（Band A第1–5套）**。國家華語測驗推動工作委員會。取自 <https://tocfl.edu.tw/>",
    "國家教育研究院（2023）。**華語文能力基準應用參考指引**。新北市：國家教育研究院。",
    "張莉萍（2011）。**華語文能力指標研究**。華語文能力測驗成果發表會。臺北：臺灣。",
    "陳靖佳（2013）。**情境感知行動華語文學習之成效研究**（未出版碩士論文）。國立臺灣師範大學。",
    "曾文璇、蔡怡珊、林玲英、陳柏熹（2023）。使用華語文語料庫與能力基準整合應用系統設計TOCFL測驗試題。**華文世界，132**，115-123。",
    "藍珮君（2007）。**基礎華語文能力測驗與歐洲語言共同參考架構的對應關係**。第三屆華文教學國際論壇。臺北：臺灣。〔待核對：作者姓名〕",
]
REFS_EN = [
    "Alderson, J. C., & Wall, D. (1993). Does washback exist? *Applied Linguistics, 14*(2), 115-129.",
    "Bachman, L. F., & Palmer, A. S. (1996). *Language testing in practice*. Oxford, England: Oxford University Press.",
    "Bandura, A. (1986). *Social foundations of thought and action: A social cognitive theory*. Englewood Cliffs, NJ: Prentice-Hall.",
    "Branch, R. M. (2009). *Instructional design: The ADDIE approach*. New York, NY: Springer.",
    "Bruner, J. S. (1960). *The process of education*. Cambridge, MA: Harvard University Press.",
    "Cassady, J. C., & Johnson, R. E. (2002). Cognitive test anxiety and academic performance. *Contemporary Educational Psychology, 27*(2), 270-295.",
    "Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Hillsdale, NJ: Lawrence Erlbaum.",
    "Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika, 16*(3), 297-334.",
    "Dweck, C. S., & Leggett, E. L. (1988). A social-cognitive approach to motivation and personality. *Psychological Review, 95*(2), 256-273.",
    "Elkhafaifi, H. (2005). Listening comprehension and anxiety in the Arabic language classroom. *The Modern Language Journal, 89*(2), 206-220.",
    "Elliot, A. J., & Harackiewicz, J. M. (1996). Approach and avoidance achievement goals and intrinsic motivation: A mediational analysis. *Journal of Personality and Social Psychology, 70*(3), 461-475.",
    "Ellis, R. (2003). *Task-based language learning and teaching*. Oxford, England: Oxford University Press.",
    "Eysenck, M. W., Derakshan, N., Santos, R., & Calvo, M. G. (2007). Anxiety and cognitive performance: Attentional control theory. *Emotion, 7*(2), 336-353.",
    "Garrison, D. R. (1997). Self-directed learning: Toward a comprehensive model. *Adult Education Quarterly, 48*(1), 18-33.",
    "Horwitz, E. K., Horwitz, M. B., & Cope, J. (1986). Foreign language classroom anxiety. *The Modern Language Journal, 70*(2), 125-132.",
    "Long, M. H. (1985). A role for instruction in second language acquisition: Task-based language teaching. In K. Hyltenstam & M. Pienemann (Eds.), *Modelling and assessing second language acquisition* (pp. 77-99). Clevedon, England: Multilingual Matters.",
    "MacIntyre, P. D., & Gardner, R. C. (1994). The subtle effects of language anxiety on cognitive processing in the second language. *Language Learning, 44*(2), 283-305.",
    "Mayer, R. E. (2009). *Multimedia learning* (2nd ed.). New York, NY: Cambridge University Press.",
    "Messick, S. (1996). Validity and washback in language testing. *Language Testing, 13*(3), 241-256.",
    "Nunan, D. (2004). *Task-based language teaching*. Cambridge, England: Cambridge University Press.",
    "Richey, R. C., & Klein, J. D. (2007). *Design and development research: Methods, strategies, and issues*. Mahwah, NJ: Lawrence Erlbaum.",
    "Saito, Y., Garza, T. J., & Horwitz, E. K. (1999). Foreign language reading anxiety. *The Modern Language Journal, 83*(2), 202-218.",
    "Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257-285.",
    "Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296.",
    "Willis, J. (1996). *A framework for task-based learning*. Harlow, England: Longman.",
    "Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice, 41*(2), 64-70.",
]
for ref in REFS_ZH + REFS_EN:
    para(ref, align=L, first=-24, left=24)

d.core_properties.title = TITLE_ZH
d.core_properties.author = ""
d.save(OUT)

# ---------- hitung 字 (gaya Word: 1 per karakter CJK, 1 per kata Latin) ----------
def count(text):
    cjk = len(re.findall(r"[\u3400-\u9fff\uff01-\uff60\u3000-\u303f「」『』—…]", text))
    lat = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.\-–/&]*", re.sub(r"[\u3400-\u9fff]", " ", text)))
    return cjk + lat
full = docx.Document(OUT)
txt = "\n".join(p.text for p in full.paragraphs)
tbl = "\n".join(c.text for t in full.tables for r in t.rows for c in r.cells)
print("abstrak ZH 字:", sum(len(t) for t in ABS_ZH))
print("total 字 (dengan tabel):", count(txt) + count(tbl))
print("saved", OUT)
