"""Spesifikasi soal bergaya TOCFL Band A per Part — diturunkan dari analisis 5 set mock test resmi
(analisis-ujian-tocfl.md Bagian 4, 6, 7, 8; hitungan 500 butir di _kerja/kode_mocktest.py).

Kode pola pengecoh (sama dengan kode_mocktest.py):
  A 說反/角色對調  B 次要細節當重點  C 相關但文中未提  D 同類替換
  E 最小差異 (unsur sama, beda satu atribut: posisi/jumlah/waktu/kombinasi/status)
  F 言外之意照字面  H 文中出現詞陷阱 (kata/angka/tempat yang benar-benar disebut, tapi bukan jawabannya)
  I 語法/搭配  J 字形/字音相近
"""

POLA = {
    'A': 'kebalikan makna / peran tertukar / negasi',
    'B': 'detail sekunder dijadikan poin utama',
    'C': 'terkait topik tetapi tidak disebut di teks',
    'D': 'ganti dengan benda/aktivitas/tempat dari kategori yang sama',
    'E': 'pasangan minimal: unsur sama, beda SATU atribut (posisi, jumlah, waktu, harga, kombinasi, status)',
    'F': 'ucapan tidak langsung / basa-basi dipahami secara harfiah',
    'H': 'jebakan kata yang terdengar/tertulis: memakai kata, angka, atau tempat yang benar-benar muncul di teks tetapi bukan jawabannya',
    'I': 'kata fungsi / kolokasi yang salah secara tata bahasa',
    'J': 'hanzi atau bunyi mirip',
}

# Komposisi 1 paket = 10 butir, sama dengan Tes Bab (bangun_bank.POLA)
KOMPOSISI = ['聽力 Part 1', '聽力 Part 1', '聽力 Part 2', '聽力 Part 3', '聽力 Part 4',
             '閱讀 Part 1', '閱讀 Part 2', '閱讀 Part 3', '閱讀 Part 4', '閱讀 Part 5']
# Komposisi soal latihan modul (12 butir, sama dengan susunan tasks di 126 dari 138 單元) — tetapi dalam FORMAT RESMI
# (聽力 P2 = tanya-jawab → gambar, bukan listen_reply; 聽力 P3 = 4 baris → gambar).
KOMPOSISI_LATIHAN = ['聽力 Part 1', '聽力 Part 1', '聽力 Part 1', '聽力 Part 2', '聽力 Part 2', '聽力 Part 3', '聽力 Part 4',
                     '閱讀 Part 1', '閱讀 Part 2', '閱讀 Part 3', '閱讀 Part 4', '閱讀 Part 5']

# Panjang teks per level (hanzi). A2 = panjang resmi; A0/A1 lebih pendek (keputusan desain yang sudah dipakai di bank).
PANJANG = {
    '閱讀 Part 1': {'A0': (6, 12), 'A1': (8, 14), 'A2': (8, 16)},
    '閱讀 Part 2': {'A0': (5, 10), 'A1': (6, 12), 'A2': (8, 12)},        # per opsi kalimat
    '閱讀 Part 4': {'A0': (30, 60), 'A1': (50, 90), 'A2': (80, 110)},    # paragraf setelah diisi
    '閱讀 Part 5': {'A0': (30, 60), 'A1': (50, 90), 'A2': (80, 130)},
}

PART = {
    '聽力 Part 1': dict(
        type='listen_pic', part='聽力 Part 1 · Deskripsi gambar',
        instr='Lihat gambar. Dengarkan pertanyaan dan jawaban A–C, lalu pilih jawaban yang cocok dengan gambar.',
        bentuk='SATU gambar (picture: {icon: emoji, label: deskripsi Indonesia yang memuat detail kunci}); '
               'question = pertanyaan lisan pendek (5W1H: …在哪裡？…在做什麼？…怎麼了？有幾個…？); '
               'options = 3 jawaban lisan (teks), satu kerangka kalimat yang sama, hanya unsur kuncinya berganti.',
        pola={'D': 70, 'E': 30},
        catatan='Ketiga jawaban harus berkerangka sama (mis. 他在睡覺。/他在念書。/他在玩。). '
                'Pertanyaan tentang orang di gambar memakai 這位先生/這位小姐/他/她, BUKAN 男的/女的.'),
    '聽力 Part 2': dict(
        type='listen_dialog', part='聽力 Part 2 · Tanya-jawab satu putaran',
        instr='Dengarkan tanya-jawab singkat, lalu pilih gambar yang cocok.',
        bentuk='lines = TEPAT 2 baris (tanya lalu jawab), sp "男"/"女"; question = ulang/ringkas pertanyaannya; '
               'options = 3 GAMBAR {icon, label}.',
        pola={'D': 45, 'E': 42, 'H': 13},
        catatan='Pengecoh gambar paling sering pasangan minimal: unsur sama, beda satu atribut.'),
    '聽力 Part 3': dict(
        type='listen_dialog', part='聽力 Part 3 · Dialog beberapa putaran',
        instr='Dengarkan dialognya, lalu pilih gambar yang menjawab pertanyaan.',
        bentuk='lines = TEPAT 4 baris bergantian 男/女; question = pertanyaan 問 tentang dialog '
               '(pakai 這位先生/這位小姐 bila menyebut pembicara); options = 3 GAMBAR {icon, label}.',
        pola={'H': 48, 'E': 33, 'D': 19},
        catatan='Ciri khas: dialog menyebut DUA atau lebih pilihan (tempat/waktu/benda), hanya satu yang benar '
                'pada akhirnya (mis. 本來…後來…, 不是…是…). Pengecoh memakai pilihan yang disebut tapi ditolak (pola H).'),
    '聽力 Part 4': dict(
        type='listen_dialog', part='聽力 Part 4 · Dialog + makna tersirat',
        instr='Dengarkan dialognya, lalu pilih jawaban yang paling tepat.',
        bentuk='lines = TEPAT 4 baris bergantian 男/女; question inferensial (…的意思是什麼？…為什麼…？…可能是做什麼工作的？); '
               'options = 4 TEKS (A–D), 4–12 hanzi, parafrase (bukan kutipan persis).',
        pola={'H': 38, 'A': 28, 'F': 15, 'C': 10, 'B': 9},
        catatan='Di ujian asli Part 4 hanya diputar SEKALI. Ragam santai: basa-basi, alasan, penolakan halus. '
                'Pakai 這位先生/這位小姐 di pertanyaan & opsi.'),
    '閱讀 Part 1': dict(
        type='read_sent', part='閱讀 Part 1 · Kalimat → gambar',
        instr='Baca kalimatnya, lalu pilih gambar yang cocok.',
        bentuk='text = SATU kalimat; options = 3 GAMBAR {icon, label}.',
        pola={'E': 67, 'D': 24, 'H': 9},
        catatan='Gambar pengecoh hampir selalu pasangan minimal (jam, jumlah, posisi, urutan, siapa melakukan apa).'),
    '閱讀 Part 2': dict(
        type='read_pick', part='閱讀 Part 2 · Gambar → kalimat',
        instr='Lihat gambarnya, lalu pilih kalimat yang cocok.',
        bentuk='picture = {icon, label} yang memuat detail kunci; options = 3 KALIMAT tentang gambar.',
        pola={'E': 83, 'A': 9, 'C': 8},
        catatan='Gambar bisa adegan, papan pengumuman, jadwal, menu, harga. Pengecoh = kalimat yang salah SATU detail.'),
    '閱讀 Part 3': dict(
        type='read_gap', part='閱讀 Part 3 · Isian bergambar',
        instr='Lihat gambarnya, lalu pilih kata yang tepat untuk titik kosong.',
        bentuk='picture = {icon, label}; text = satu kalimat dengan TEPAT satu （　）; options = 3 kata.',
        pola={'I': 73, 'D': 23, 'J': 4},
        catatan='Opsi sering kata fungsi/kolokasi (幫/讓/對, 收/寄/借, 就/才/再, 戴/穿/帶).'),
    '閱讀 Part 4': dict(
        type='cloze', part='閱讀 Part 4 · Melengkapi paragraf',
        instr='Isi setiap titik kosong. Satu pilihan hanya boleh dipakai sekali, dan ada SATU pilihan yang tidak terpakai.',
        bentuk='text = paragraf naratif orang pertama dengan titik （1）（2）… ; options = titik+1 FRASA (3–7 hanzi); '
               'answers = indeks opsi untuk tiap titik berurutan.',
        pola={'G': 100},
        catatan='Titik = frasa yang menjaga alur logis (sebab–akibat, urutan waktu, kontras). Opsi berlebih = '
                'antonim atau pasangan minimal dari salah satu jawaban benar (以後/以前, 好/壞, 也/才) dan tidak cocok '
                'di titik mana pun. A0 boleh 3–5 titik; A1/A2 tepat 5 titik.'),
    '閱讀 Part 5': dict(
        type='read_mc', part='閱讀 Part 5 · Pemahaman bacaan',
        instr='Baca teksnya, lalu pilih jawaban yang paling tepat.',
        bentuk='text = satu wacana pendek utuh (anekdot, cerita pribadi, pengumuman, opini ringan); '
               'question inferensial / gagasan utama; options = 4 TEKS (A–D), parafrase.',
        pola={'C': 32, 'H': 32, 'A': 28, 'B': 8},
        catatan='Pertanyaan khas: 這篇短文說了什麼？寫這段話的人覺得…怎麼樣？…可能是做什麼工作的？…以後會發生什麼事？'),
}

ATURAN_UMUM = """\
- Hanya satu jawaban benar per soal; pengecoh harus masuk akal tetapi jelas salah bila teks dipahami.
- Tiap pengecoh mengikuti pola yang ditentukan (lihat kode pola); tulis kode pola tiap pengecoh di "pola_pengecoh".
- Tokoh soal NETRAL dan tidak berulang: 王先生, 李小姐, 小明, 小美, 陳太太, 張老師… (bukan tokoh cerita modul).
- Rujukan ke pembicara/orang: 這位先生 / 這位小姐 (posesif: 這位先生的姊姊). JANGAN pakai 男的/女的.
- Latar Taiwan; harga pakai 元 atau 塊. Tanpa stereotip negara/budaya mana pun; jangan mengasumsikan asal pembaca.
- "why" ditulis dalam bahasa Indonesia, 1–2 kalimat: alasan jawaban benar + kenapa tiap pengecoh salah
  (sebut huruf: "A: … B: …").
- Untuk gambar: icon = 1–3 emoji yang mewakili, label = deskripsi Indonesia yang memuat DETAIL PEMBEDA
  (mis. "jam 10:25", "dua sepatu di bawah label $500"). Ilustrasi SVG akan dibuat terpisah.
- Posisi jawaban benar harus tersebar merata (tidak lebih dari 40% di huruf yang sama); untuk soal 4 opsi,
  jawaban D juga harus muncul.
- SEMUA opsi harus kalimat/kata yang gramatikal dan wajar; salahnya ada di MAKNA, bukan di tata bahasa
  (pengecualian: 閱讀 Part 3, di mana pilihan kata fungsi yang tidak cocok memang dinilai).
- 聽力 Part 4 & 閱讀 Part 5: pertanyaan inferensial / gagasan utama (bukan sekadar fakta yang tertulis), dan
  jawaban benar berupa PARAFRASE — jangan kutipan persis dari dialog/teks.
- 聽力 Part 3: opsi berupa GAMBAR dan dialog TEPAT 4 baris; jawabannya baru jelas setelah seluruh dialog.
- 閱讀 Part 4: opsi berupa FRASA (3–7 hanzi), bukan huruf/kata tunggal.
"""
