# Analisis tesis rujukan (folder `我要用的論文/`, 18 PDF + 4 PDF resmi TOCFL) — 2026-11-16, ditambah 2026-11-25

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
   - ⚠ Menyebut TOCFL menjadi **CAT (adaptif berbasis komputer) sejak 2023-01-01** — **KOREKSI 2026-11-25:** menurut
     華測會, CAT sudah dipakai di Taiwan sejak 2016/2017; 2023 = CAT pertama di luar negeri (India, 30-04-2023) &
     masuknya 準備級 (lihat bagian E). Jangan kutip angka 2023 dari tesis ini → mode "Ujian penuh format resmi" kita meniru format tetap lama; perlu disebut di metodologi. Ambang lulus di tabelnya (41/42, 57/60) tidak konsisten dengan teksnya (45/42, 60) → cocokkan dengan dokumen resmi di `TOCFL Band A/`.
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

## E. Kaidah resmi penyusunan soal TOCFL, CAT, HSK & ujian internasional (penelusuran 2026-11-25)

PDF yang disimpan ke `我要用的論文/` (folder di-.gitignore, salinan lokal saja):
- `華測會 2022 命題設計概述（官方簡報）.pdf` — https://tocfl.edu.tw/assets/files/2022presentation.pdf (47 slide, dibaca penuh)
- `曾文璇等 2023 使用語料庫與能力基準設計TOCFL試題（華文世界132）.pdf` — https://tocfl.edu.tw/assets/files/TOCFL_design.pdf (dibaca penuh)
- `華測會 TOCFL 電腦化適性測驗 CAT 簡介（舊版手冊）.pdf` — https://etudes-chinoises.unistra.fr/websites/lge/departements/chinois/CAT_En_DM.pdf (dibaca penuh; versi lama, skala 100)
- `藍珮君、陳柏熹 2014 華語文閱讀測驗信效度分析與垂直等化研究.pdf` — https://tocfl.edu.tw/assets/files/Reading_RV.pdf (hanya bagian kriteria; encoding teks hasil ekstraksi rusak, angka terbaca)

### E1. Kaidah resmi 華測會 menyusun soal (〈命題設計概述〉 2022) — dasar kaidah utama
- **8 langkah penyusunan tes** (mengutip 陳柏熹 2011《心理與教育測驗：測驗編製理論與實務》, 精策, hlm. 30):
  決定測驗目標 → 建立測驗藍圖 → 選擇適當題型 → 編製試題 → 修改(審查)試題 → 預試 → 試題分析 → 建立題庫.
  ⚠ Kutip 陳柏熹 (2011) sebagai sumber primer (cari bukunya).
- TOCFL **「不以任何特定教材為命題依據」**; bahan = beragam situasi sehari-hari yang nyata.
- **11 主題領域** resmi: 個人資料, 飲食, 旅行, 閒暇時間娛樂, 健康及身體照顧, 購物, 日常生活, 工作, 房屋與家庭環境,
  與他人的關係, 教育 (rinciannya di slide 18–28; mirip 《華語八千詞表》 & TBCL 主題情境).
- Band A (入門基礎級) = 「測知日常生活的一般簡易溝通能力」; 聽 4 tipe (看圖回答/問答理解/對話理解/對話), 閱 5 tipe.
- **Kaidah stem (題幹):** tidak memakai 超等詞彙, 專有名詞, 俚俗語; logis & sesuai situasi nyata; kalimat pertama
  「建立情境、帶入主題」; **giliran bicara seimbang** (contoh buruk: jawaban 「有。」「好啊！」 membuat informasi terlalu
  sedikit); paragraf utuh & kohesif; sesuai batas jumlah karakter.
- **Kaidah pertanyaan (提問):** hanya satu pertanyaan; jelas & sesuai level; **hindari bentuk negatif** (不喜歡…);
  **tidak bisa dijawab dengan pengetahuan umum** atau budaya yang pasti diajarkan; kalimat lengkap (bukan 「小美應該___?」).
- **Kaidah pilihan (選項):** panjang setara, **≤15 hanzi**; diurutkan menurut panjang/logika (angka, arah)/waktu;
  **posisi kunci disebar acak merata**; tanpa pilihan gabungan (甲乙) & tanpa 以上皆是/皆非; **sudut orang ketiga**;
  tanpa nama diri/slang; deskripsi positif–negatif seimbang; **kunci = parafrase, bukan salinan stem**; pengecoh
  menarik tapi tidak "mungkin benar"; pilihan tidak saling mencakup (contoh: 身體不舒服 ⊃ 肚子很痛); logika pilihan
  = logika pertanyaan; soal-soal dalam satu kelompok **tidak saling membocorkan jawaban** & tidak menguji 考點 sama.
- **公平性:** tanpa diskriminasi/pujian bagi gender, ras, daerah, agama, politik; **tidak memakai materi yang lebih
  akrab bagi kelompok tertentu** (contoh buruk resmi: soal telur Paskah); peluang benar hanya dipengaruhi kemampuan
  yang diukur; sumber teks tidak tunggal. **原創性:** soal asli, belum pernah muncul di buku/ujian; sumber dicantumkan.
- **考點:** 話語的主旨和大意, 重要細節, 說話者的想法與表達方式. Alur: pilih ranah/tugas → level → bahan → stem → 考點
  → pertanyaan → kunci → pengecoh.
- Sumber penulisan soal yang disarankan: CEFR, TBCL, ACTFL; 華語八千詞; 語料庫與能力基準整合應用系統;
  halaman 「試題編寫範例」 https://tocfl.edu.tw/index.php/teach/examples (belum dibaca).

### E2. Prosedur kendali level kosakata (曾文璇、蔡怡珊、林玲英、陳柏熹 2023, 《華文世界》132)
- Cocokkan bahan dengan deskriptor TOCFL + TBCL → ambil teks nyata (koran, siaran, web) → potong & tulis ulang →
  segmentasi + cek level setiap kata dengan **國教院教材編輯輔助系統** (contoh: kata >level 6 ±4% = masih bisa
  dikendalikan) → ganti kata 超等/未收錄 dengan 關聯替換詞語選擇器 / 語義場關聯詞替換系統 (輕生 → 自殺 L4) → cek
  makna tetap & kalimat lancar → nama diri tidak dijadikan 考點 → analisis 大意/重要訊息/想法 tiap paragraf → pengecoh
  「必須扣緊文本材料內容或話題」 → cek level lagi & cek antarsoal tidak saling memberi jawaban.
- **Pakai untuk:** pembenaran langsung validator TBCL di pipeline (`cek_dialog.py`, `bangun_bank.py`): TOCFL sendiri
  mengendalikan level kosakata dengan cara yang sama.

### E3. CAT TOCFL (華語文聽力閱讀電腦化適性測驗)
Sumber: https://tocfl.edu.tw/tocfl/index.php/test/cat (sub-halaman list/1–5, diakses 2026-11-25), brosur lama
(unistra), https://english.moe.gov.tw/cp-117-36280-b4fea-1.html.
- IRT **model Rasch** (soal skor 0/1). Kemampuan diestimasi setelah tiap jawaban → sistem memilih soal yang paling
  cocok berikutnya; jawaban benar → soal lebih sulit, salah → lebih mudah.
- Peserta **tidak memilih level**; soal diambil dari semua band (peserta 入門/基礎級 bisa mendapat soal 進階/高階).
- 聽力 ±35 soal (±50 menit, **10 detik** per soal setelah audio selesai, lalu otomatis lanjut); 閱讀 ±35 soal (60 menit);
  total per peserta bervariasi **25–40 soal**. Berhenti bila waktu habis atau kemampuan sudah terukur; 閱讀 <25 soal
  dijawab → skor disesuaikan proporsional.
- **Tidak bisa kembali/mengubah jawaban**; soal yang tidak dijawab = salah. Tipe soal = sama dengan format tetap.
- Perbandingan resmi (slide 2022 hlm. 5): **CBT** = pilih level, 50 soal tetap per tes, boleh lompat & cek ulang;
  **CAT** = tanpa pilih level, ±35 soal, tidak bisa kembali.
- **Skor (situs sekarang):** skala 0–700. Ambang 聽/閱: 準備一級 190/195, 準備二級 295/305, **入門級 355/355,
  基礎級 435/450**, 進階級 480/490, 高階級 555/570, 流利級 600/610, 精通級 655/690. Ambang ditetapkan dengan
  standard setting metode Angoff.
  ⚠ Brosur lama = skala 100 (Level 1 21/21, Level 2 40/40, Level 3 46/48…) → kutip versi situs + tanggal akses.
- Sejarah: CAT resmi sejak 2016/2017 di Taiwan (situs 華測會 & 師大 huayubest); 2023 = pertama di luar negeri (India)
  + masuknya 準備級.
- **Kriteria masuk bank soal** (藍珮君 & 陳柏熹 2014, 華語文教學研究 11(1):99–126; angka diverifikasi dari PDF): uji
  coba harus fit Rasch (**infit MNSQ 0,7–1,3; infit ZSTD −3 s/d 3**) & **daya beda D ≥ 0,2**; reliabilitas KR20 tiap
  level ≥0,90. Makalah ini juga menyebut CAT butuh bank soal besar yang **digabung secara vertikal** (vertical
  equating) ke satu skala.
- **TIDAK dipublikasikan:** cara memilih soal pertama, aturan berhenti berbasis SE, exposure control, ukuran bank soal,
  content balancing. TR-001–TR-032 (https://tocfl.edu.tw/tocfl/index.php/study/resreport) = laporan reliabilitas &
  validitas tahunan, tidak ada yang khusus CAT.
- Makalah 華測會 lain yang relevan (https://tocfl.edu.tw/tocfl/index.php/study/publication): 洪小雯 (2013)
  影響對外漢語閱讀測驗難度的因素; 詹益智 (2008) faktor kesulitan soal dialog pendek 聽力 (ACTFL); 林玲英、藍珮君
  (2011) kesulitan soal di komputer vs kertas; 藍珮君等 (2014) 以TOCFL連結CEFR與ACTFL：標準設定; Yes/No Angoff
  (2013); Wu, Huang, Chen & Chen (2025) multistage testing, *J. Educational Measurement*.
- **Implikasi untuk thesis:** mode "Ujian penuh · format resmi" di app meniru **CBT format tetap** (50 soal, bisa
  kembali di dalam satu bagian), bukan CAT → sebut eksplisit di metodologi. Pertimbangkan: latihan tanpa kembali,
  batas 10 detik untuk menjawab 聽力, sesekali soal di atas level (CAT memang memunculkannya).

### E4. HSK (Tiongkok)
- 《HSK标准教程》 (ed. 姜丽萍, BLCUP): prinsip **「考教结合、以考促教、以考促学」**; penyusun menganalisis 33 set
  soal asli (±1,2 juta karakter) + 大纲 & 出题指南; ditegaskan bukan 应试教材, tujuan akhir = kemampuan berbahasa
  menyeluruh. Sumber: https://www.slideshare.net/PhoenixtreePublishing/introduction-of-hsk-standard-course-serieshsk ,
  https://www.blcup.com/PInfo/index/8212 → paling dekat dengan posisi thesis kita.
- Analisis buku itu (Lanzhou Univ.): HSK2 https://chinese.lzu.edu.cn/chinese/upload/files/20201117/709dad8347d44ddca76dc1ca3cfdc979.pdf ;
  HSK1 dari sudut 考教结合 https://chinese.lzu.edu.cn/chinese/upload/files/20201117/dc404f71120a4a87b438ec82f194e5a3.pdf
- Tesis S2: 《新HSK五级阅读部分命题研究》 (CNKI CMFD 1015563714.nh); 《HSK标准教程》离合词编写和教学研究;
  《基于新HSK考试的对外汉语教材分析——以《HSK标准教程5》为例》 (2021).
- Buku: 张旺熹、王佶旻《中国汉语水平考试HSK(改进版)研究》 — prinsip desain, teknik penulisan soal, sistem
  manajemen penulisan soal.
- Penyelenggara: 张晋军《新汉语水平考试(HSK)题库建设之我见》 (bank soal, penyusunan paket soal otomatis, CAT);
  张晋军等《对新汉语水平考试(HSK)的新思考》 https://www.chinesetest.cn/userfiles/file/yanjiu/12.doc ;
  汉考国际《汉语考试命题平台管理办法》 (hanya aturan manajemen penulis soal, bukan cara menulis soal).
- Kritik: buku persiapan HSK setelah 2010 terlalu berfokus pada trik ujian, soal asli & simulasi
  (https://m.fx361.com/news/2015/0522/23504664.html) → celah yang diisi thesis.
- Belum ada publikasi tentang CAT HSK resmi; yang terdekat: tes kosakata Mandarin bertipe MST (IJCLE No.17, 2025) &
  AIG + CAT untuk kosakata L2 Mandarin (ACL W19-4403).

### E5. IELTS, TOEFL & teori umum
- **Washback buku persiapan ujian:** Wang (1997) tesis S2 Lancaster, buku persiapan IELTS; Hilke & Wadden (1997),
  10 buku TOEFL di Jepang; Alderson & Hamp-Lyons (1996) *Language Testing* 13(3), kursus TOEFL; Green (2007)
  *IELTS Washback in Context*, SiLT 25 (PDF gratis: https://www.cambridgeenglish.org/Images/734967-studies-in-language-testing-volume-25.pdf).
- **Kaidah penyusunan tes bahasa:** Council of Europe/ALTE (2011) *Manual for Language Test Development and
  Examining* (gratis: https://rm.coe.int/1680667a2b; edisi revisi 2026:
  https://rm.coe.int/new-revised-manual-for-language-test-development-and-examining-joint-p/48802cc30d);
  Khalifa & Weir (2009) *Examining Reading* (SiLT 29, kerangka validitas sosio-kognitif Cambridge).
- **Kaidah soal pilihan ganda:** Haladyna, Downing & Rodriguez (2002), *Applied Measurement in Education*
  15(3):309–333, 31 pedoman (stem positif, hindari tipe K/gabungan, dll.). ⚠ Cek nomor pedoman di artikel asli.

### E6. Yang belum ditemukan & cara mencarinya
- Tesis yang khusus membahas **penyusunan buku persiapan TOCFL** secara utuh hampir tidak ada (yang terdekat:
  tesis NTNU materi tes untuk siswa Vietnam, A.5) → menguatkan klaim kebaruan thesis.
- Cari lanjut: NDLTD (ndltd.ncl.edu.tw) 「華語文能力測驗 教材」「TOCFL 教材」; CNKI 「HSK 教材 编写」「考教结合」
  「HSK 命题」 (tidak bisa diakses Claude).

### E7. Cocokkan dengan app — pemeriksa otomatis di `bangun_bank.py` (2026-11-25); Vol.1–3 SELESAI
Audit awal bank soal (1.380 butir): kunci 4 pilihan menumpuk di D (A0 28/50, A1 42/92, A2 51/134); pilihan angka/waktu
sering tidak urut; 41 butir panjang pilihan timpang; 34 kunci disalin persis; ±7 pertanyaan negatif; 31 giliran ≤2 hanzi.
Pilot Vol.1: 12 butir diurutkan, 14 kunci dipindah (4 pilihan jadi A12 B13 C12 D13), 15 butir ditulis ulang, 1 `why`
yang salah sejak awal diperbaiki (A05 閱讀 P5), 3 giliran penutup diterima.
Vol.2: 25 butir diurutkan/kunci dipindah (4 pilihan jadi A23 B24 C24 D21), ±40 butir ditulis ulang, 6 `why` salah huruf
diperbaiki (B03, B12, B13, B19, B36 + B07), 19 peringatan diterima (giliran wajar, kalimat syarat, waktu setelah penolakan).
Vol.3: 33 butir diurutkan/kunci dipindah (4 pilihan jadi A33 B34 C33 D34), 41 butir ditulis ulang, 5 `why` salah huruf
diperbaiki (C06, C07, C08, C38, C41), 11 peringatan diterima. Hasil akhir: 1.380 butir, 0 peringatan terbuka.
Bandingkan soal latihan, bank soal & ujian dengan kaidah E1: pilihan ≤15 hanzi & panjang setara; posisi kunci
merata; tanpa pertanyaan negatif; tanpa soal yang bisa dijawab dengan pengetahuan umum; kunci = parafrase; pilihan
tidak saling mencakup; giliran dialog seimbang; antarsoal tidak saling membocorkan. Yang sudah sesuai: sudut orang
ketiga (這位先生/這位小姐), kendali level TBCL, posisi jawaban seimbang (Vol.2–3), netral budaya (siswa global).
