# Analisis tesis rujukan (folder `我要用的論文/`, 18 PDF) — 2026-11-16

Dibaca: abstrak, kesimpulan, dan bagian kunci (bukan seluruh isi).

## A. Paling relevan

1. **生成式 AI 在華語文分級測驗試題編寫之應用研究－與 TOCFL 試題之比較分析** (NTNU, 114; file "TOCFL 設計題式.pdf")
   - GPT-4 membuat soal Band A, dibandingkan dengan soal resmi; 40 pemelajar Vietnam; kerangka PIRLS 4 tingkat + Bloom.
   - 聽力 AI ≈ resmi; 閱讀 AI terlalu mudah, daya beda rendah; kosakata di atas level; pengecoh lemah; jarang inferensial.
   - Data resmi 聽力: 52–82% 直接提取, ≤18% 詮釋整合. Part 1 hampir semua 直接提取, Part 3 ±setengah 直接推論, Part 4 didominasi 詮釋整合.
   - Pakai untuk: membenarkan validator TBCL, 6 pola pengecoh, audit inferensial (`cek_ciri.py`); bisa melaporkan tingkat kognitif soal dengan PIRLS.
2. **基於 Model Context Protocol 之 TOCFL 自動出題架構** (Chung Yuan, 114)
   - Basis data wordlist/grammar/morpheme/character + CKIP; alat query_words, query_grammars, replace_word, penghitung karakter.
   - Mirip pipeline kita; pembeda: tanpa uji ke pemelajar, tanpa kurikulum.
3. **以電腦輔助初級越南華語學習者 TOCFL 閱讀測驗的歷時研究：Google 表單和 ChatGPT** (PCCU, 114)
   - 18 minggu, latihan simulasi 閱讀 via Google Form + ChatGPT + Wordwall, buku 《時代華語2》; studi kasus longitudinal.
4. **以初級華語文能力測驗為導向之課程設計** (Wenzao, 109)
   - TBLT + penelitian tindakan; kesalahan terbanyak = hanzi; saran: evaluasi pengenalan (bukan tulis) huruf, prioritaskan ketepatan tata bahasa & pemahaman menyeluruh.
5. **基於越南學生需求的華語文測驗教材設計與編寫研究** (NTNU, 114)
   - Topik penting: 日常生活 78.6%, 地點方向 71%, 學習工作 69.5%, 社交 64.9%, 時間天氣 64.1%, 購物 61.8%, 娛樂 58%, 個人資料 55.7%, 食物 49.6%, 健康 48.9%.
   - Pemelajar minta penjelasan tata bahasa, banyak contoh kalimat, ilustrasi, pembedaan sinonim → dukung catatan 📘 & gambar.
6. **越南籍移工華語課程設計—擬通過 TOCFL A2** (Wenzao, 112)
   - 《時代華語》 disesuaikan, 集中識字 + 語法翻譯; peserta hadir penuh lulus A2.
   - Acuan: A1 240–480 jam / 800 kata; A2 480–720 jam / 1.200 kata.
   - ⚠ Menyebut TOCFL menjadi **CAT (adaptif berbasis komputer) sejak 2023-01-01** → mode "Ujian penuh format resmi" kita meniru format tetap lama; perlu disebut di metodologi. Ambang lulus di tabelnya (41/42, 57/60) tidak konsisten dengan teksnya (45/42, 60) → cocokkan dengan dokumen resmi di `TOCFL Band A/`.
7. **線上主題式華語教學設計—TOCFL A1 越南** (Wenzao, 114) — tematik + tugas nyata, ASSURE.
8. **以故事教學法融入線上華語課程—TOCFL A2 越南** (Wenzao, 114) — bercerita menaikkan ingatan & keterlibatan; dukung 情境對話 berbasis cerita.

## B. Berguna untuk metode/konteks
- **印尼亞齊大學短期華語課** (Taitung): konten lokal menaikkan minat; full-Mandarin menurunkan minat, bantuan EN/ID menekan kecemasan → dukung UI dwibahasa & tujuan menurunkan kecemasan.
- **以西方國家學習者為對象之身心健康華語教材** (NTNU, 114): satu-satunya yang menyentuh aspek psikologis; relevan untuk kecemasan & "siswa global".
- **印尼基礎中文教材編寫與遠距教學** (NCNU, 114) dan **印尼學生來臺讀大學必備知識** (NTNU, 113): alur analisis kebutuhan → materi → evaluasi ahli + siswa (bisa ditiru untuk instrumen).
- **ASSURE 同步視訊遠距** (Wenzao) dan **Nearpod 混成** (Wenzao, 111): ASSURE dipakai di 4 tesis → jelaskan kenapa kita memakai TBLL 6 tahap + Mayer, atau petakan ke ASSURE.
- **短期華語文化課** (Chung Yuan, 112): 文化三層次 + 5C, untuk catatan budaya.

## C. Relevansi rendah
- Laporan OCAC 僑生專班; 高職建教僑生 (Pingtung); 學術中文 Rusia — hanya latar belakang statistik.

## Celah yang bisa diklaim sebagai kontribusi
1. Cakupan 100% kosakata & tata bahasa TBCL Band A dengan kontrol beban kognitif.
2. Aplikasi belajar mandiri (semua tesis = kursus dipimpin guru).
3. Pemelajar global (semua tesis fokus satu negara, terutama Vietnam).
4. Mengukur kecemasan ujian pra-pasca intervensi.
5. Pembuatan soal berbantuan AI + validator level + pola pengecoh, diuji ke pemelajar.
