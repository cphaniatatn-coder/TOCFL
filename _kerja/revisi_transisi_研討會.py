"""研討會修正版(1).docx (komentar dosen) -> 研討會修正版(3).docx
Hanya mengganti frasa bertanda kuning yang dinilai dosen terlalu langsung; teks pengganti ditandai hijau.
Selain itu hanya koreksi tanggal 選項隨機化 (10月15日 -> 10月8日). Abstrak tidak disentuh."""
import sys
import docx
from docx.enum.text import WD_COLOR_INDEX

sys.stdout.reconfigure(encoding="utf-8")
SRC = r"C:\Users\user\OneDrive\文件\tocfl-mini\研討會修正版(1).docx"
OUT = r"C:\Users\user\OneDrive\文件\tocfl-mini\研討會修正版(3).docx"
d = docx.Document(SRC)

# frasa kuning -> pengganti (runs yang ditandai kuning, berurutan dalam paragraf)
GANTI = {
    "此外，": "除了學習者本身的困難之外，",
    "關於": "在情緒因素方面，",
    "綜上原因，": "基於上述學習者的備考困難與現行教材的不足，",
    "據分析結果顯示，": "進一步分析各部分的題目內容可以發現，",
    "華語文能力測驗": "Band A",
}
done = []
for p in d.paragraphs:
    for r in p.runs:
        if r.font.highlight_color == WD_COLOR_INDEX.YELLOW and r.text in GANTI:
            done.append(r.text)
            r.text = GANTI[r.text]
            r.font.highlight_color = WD_COLOR_INDEX.BRIGHT_GREEN
assert sorted(done) == sorted(GANTI), done

# tanggal 選項隨機化
for p in d.paragraphs:
    if "10月15日選項隨機化" in p.text:
        for r in p.runs:
            if r.text.startswith("10") or "月15日選項" in r.text or r.text == "15":
                pass
        txt = p.text
        # cari run berisi '15' tepat sebelum '日選項隨機化'
        pos = 0
        target = txt.index("10月15日選項隨機化") + len("10月")
        for r in p.runs:
            if pos <= target < pos + len(r.text):
                k = target - pos
                assert r.text[k:k + 2] == "15", r.text
                r.text = r.text[:k] + "8" + r.text[k + 2:]
                break
            pos += len(r.text)

d.save(OUT)
print("saved", OUT, done)
