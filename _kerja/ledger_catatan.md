- **2026-09-24 — 3 modul percontohan dibangun** (A01, B01, C01), semua lolos `cek_dialog.py`.
  - A01 memakai A0 vocabulary-first: 情境導入 → 詞彙 → 情境對話 → 練習 → 語法小提示 → 反思.
  - B01/C01 memakai TBLL 6 tahap: 情境導入 → 情境對話 → 詞彙 → 溝通任務 → 語法聚焦 → 反思.
  - 義項 kedua yang dicatat eksplisit: 貴（貴姓, hormat｜A01）— 貴 'mahal' belum diajarkan;
    光（habis｜C01）— 光 'cahaya/hanya' belum diajarkan.
  - Kontrol grammar di dialog dicek MANUAL (skrip hanya mengecek kosakata & partikel 了/著):
    B01 — 在那裡游 diganti 去那裡游 (在3 baru di B08). Pemakaian 跟 (跟1 resmi di B35) dibiarkan
    sesuai keputusan "leksikal dasar boleh" di CLAUDE.md.
- **2026-09-24 — Volume 1 (A01–A25) selesai dibangun**, semua lolos `cek_dialog.py`.
  - Koreksi urutan rencana (ketahuan saat menulis dialog):
    A06↔A07 tukar grammar (不 harus ada sebelum A-not-A; kata 不 pindah ke A06, 球 turun ke 補充, 美 naik ke 核心 A07);
    家 pindah A08→A04 (dibutuhkan judul "你家有幾個人？", 孩子 turun ke 補充 A04);
    judul A09 → 桌子上有什麼？ (書 baru di A13), A12 → 這是我們的老師。 (hindari 在3),
    A22 → 我頭很痛。 (怎麼了 = grammar L2 #71).
  - 義項 baru: 貴（mahal｜購物/A18）ditambahkan sebagai 補充 A18 (義項 pertama 貴姓 di A01).
  - Pola L2 yang SENGAJA dihindari di A0: 在3 (在+PW+V), 了, 話題優先 (topik di depan), 怎麼了.
  - Pola L2 yang dipakai dalam bentuk leksikal dasar (keputusan CLAUDE.md): 怎麼+V, 幾/多少, 還是 (pertanyaan pilihan),
    從, 就, 因為…所以, 給+orang, 沒+V, 看到/看見, 去+V (連動). A19 memuat 比 hanya di teks bacaan (reseptif, lapis 補充).
- **2026-09-24 — Volume 2 (B01–B46) selesai dibangun**, semua lolos `cek_dialog.py` (+ lapisan peringatan kata majemuk) dan smoke test browser.
  - Judul rencana yang diganti karena mendahului grammar/kosakata: B23 → 可以用信用卡嗎？ (刷卡 = L3),
    B25 → 我們炒了青菜就吃飯！ (先…再… = L3), B40 → …所以今天不能上課 (沒1 baru di B46),
    B42 → 我喜歡的人很聰明。 (Vs的N baru di B43), B44 → 過年，有的人回家… (…的時候 = L3), B46 臺灣 (ejaan).
  - 義項 baru lintas level: 家（kata bantu bilangan toko/restoran｜B28, 義項 pertama 'rumah' di A04）;
    哪（retoris 哪有…｜B29）; 送 dipakai dua 義項 di B05 (memberi & mengantar).
  - Morfem grammar yang didaftarkan di pemeriksa (bukan kosakata): 了 (B09), 著 (B08), 第 (B03), 正在 (B04).
  - Peringatan yang ditinjau & diterima dicatat di `_kerja/cek_diterima.txt` (mis. 火車站 = 火車+站, 看起來 dibawa V起來1 di B43).
  - Pola L3 yang SENGAJA dihindari di Vol.2: …的時候, 先…再…, V好, VV看, 還沒, 把 (kecuali 1× leksikal di B09 sesuai keputusan
    "leksikal dasar"), 不用/不必. Kata majemuk L3 yang ketahuan & diganti: 長大, 一般, 城市, 吵, 聞, 汗, 亂, 位子, 帶來 (di cek), 首.
- **2026-09-24 — Volume 3 (C01–C67) selesai dibangun. SEMUA 138 MODUL LENGKAP**, lolos `cek_dialog.py`
  (kosakata + peringatan kata majemuk) dan smoke test browser (6 tahap, kunci jawaban konsisten, 0 error JS).
  - Judul rencana yang diganti: C03 → 請把碗洗了。 (把O V了 sesuai C03), C07 → 我兩天沒睡覺了！ (睡好 = V好 C47),
    C09 → 鄉下沒有城市那麼方便。 (熱鬧 baru C40), C46 臺灣 (ejaan).
  - Kata dipindah antar-modul (cakupan tetap 100%): 流 C54→C28 (流鼻水 tak terhindarkan di adegan flu);
    減 C40→C37 (operasi hitung butuh 減).
  - Morfem yang "dibawa" poin grammar & didaftarkan di pemeriksa (PARTIKEL): 看起來/聽起來 (B43), 死了 (C08),
    為了 (C15), 得不得了/極了 (C18), 起 (C33), 以外 (C36), 分之/百分之 (C38), 折 (C40), 慣 (C44),
    睡著/睡不著 (C52), 以內 (C67). Reduplikasi AABB (乾乾淨淨) dikenali otomatis dari kata dasarnya.
  - 下 'berikutnya' (下個星期/下學期) SENGAJA dihindari di seluruh modul: 義項 itu tidak ada di rencana
    (下 hanya diajarkan sebagai 'bawah', A09). Kalau mau diajarkan, tambahkan 下@berikutnya ke rencana.
  - Interpretasi poin grammar yang labelnya ambigu (mohon dicek Carli): 沒(有)2 #118 = pertanyaan "…了沒有？";
    就2 #174 = penegasan 就是/就在; 叫1/叫2 #115/116 = memanggil / menyuruh; 可以3 #168 = 還可以 'lumayan';
    從2 #85 = 'lewat (jalur)'; 又2 #91 = 又不是… (bantahan); 呢2 #117 = penegasan di akhir pernyataan.
