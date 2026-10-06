# Analisis buku rujukan grammar untuk modul mini

**Buku:** 張黛琪（編著）《看圖學中文語法・基礎篇》 *The Ultimate Illustrated Chinese Grammar Guide (Basic Level)*,
國立臺灣師範大學國語教學中心 (MTC NTNU) 策劃. File: `TOCFL/看圖學中文語法基礎篇.pdf` (hasil scan, 102 halaman PDF;
1 halaman PDF = 2 halaman buku, halaman buku *b* ada di halaman PDF ⌊(b−2)/2⌋).

**Isi:** 35 unit grammar dasar (setiap unit: gambar + kalimat contoh, kotak *Tips*, latihan), 3 set latihan TOCFL
入門基礎級 (Band A), dan daftar 1000 kata Band A. Pendekatannya visual dan kontrastif: pola disandingkan dengan pola
yang mirip (在 vs 有, 才 vs 就, 把 vs 被 vs kalimat biasa, 有一點 vs 一點) dan kesalahan umum ditandai ✗.

## Pemetaan ke 18 bab modul mini

| Bab | Grammar modul | Unit buku | Dipakai sebagai catatan |
|---|---|---|---|
| A02 | 嗎, 哪 | 4–5 | A-不-A (是不是), 嗎 tidak bersama kata tanya, 誰 vs 哪, 從哪裡來 |
| A04 | 數+量, angka | 1–2, 5, 7–8 | kelompok kata bantu bilangan, 這/那 + angka + M, 這些/那些, 沒有 (bukan 不有), 兩 vs 二, 幾 vs 多少, 零 |
| A09 | letak benda | 11–13 | X 在 tempat vs tempat 有 X vs tempat 是 X, 上/下/裡, 中間/對面 |
| A10 | (tanpa poin grammar) | 15–16 | 兩點, 半/一刻/差, waktu sebelum V, titik waktu vs durasi |
| A18 | (tanpa poin grammar) | 7–8 | 幾 vs 多少, 塊 = 元, topik + 一杯多少錢, 多 untuk harga kira-kira |
| A24 | (tanpa poin grammar) | 19, 23, 34 | A-不-A, 越來越, 最 |
| B04 | 在/正在, 呢 | 5, 13, 17 | dua fungsi 在, 正在 = tepat saat itu, 一邊…一邊, N + 呢 |
| B19 | 比, 跟…一樣 | 23–25 | selisih sesudah Vs (✗ 很/一點 sebelum), 沒有/不像…那麼, 比較/更/最, 不一樣, ✗ 一樣很 |
| B20 | 太…了, 有一點 | 19, 23 | 有沒有 Vs一點的, 有一點 Vs vs Vs 一點, 不太 |
| B30 | 從…往, V到/V在 | 13–14, 19, 29 | urutan petunjuk arah, 從 A 到 B, 來/去 dari posisi pembicara, 離, V在 vs V到 |
| B33 | 是…的, V了 | 17–18, 21 | 是…的 untuk kejadian lampau + negasi, 還是 vs 或是, V了 + durasi, 了…了, 了 perubahan |
| B40 | 因為…所以, 但是 | 26 | (tingkat bab) 才 vs 就 — dipakai di Tes Bab B40 |
| C04 | 把 | 27–29 | V tidak berdiri sendiri, objek tertentu, negasi sebelum 把, V + 進/出/上/下 + 來/去, keterangan hasil |
| C28 | 被, V掉 | 31, 33 | 被 dengan/tanpa pelaku, kalimat biasa ↔ 被 ↔ 把, keterangan hasil, V得/不 + hasil |
| C40 | 一M比一M, Vs了一點 | 23–24, 34 | 越來越 / 越…越…, Vs了一點 ≈ 有一點 Vs |
| C16, C24, C58 | 必須/不用, 要是…就, 不但…而且 | — | tidak dibahas di buku → tidak ditambah catatan |

## Cara dipasang
- Isi catatan (Indonesia/English/Vietnam) di `_kerja/mini/catatan_grammar.json` — **disarikan dengan kata sendiri**,
  contoh kalimat memakai kosakata modul; bukan salinan teks/gambar buku.
- `buat_mini.py` memasangnya sebagai `grammar[i].catatan` (per poin) dan `modul.catatan` (tingkat bab);
  `js/modul.js` menampilkannya di tahap 語法聚焦 sebagai kotak "📘 Catatan dari buku grammar" + sumber & unit.
- Hanya modul mini; app utama tidak punya data `catatan` sehingga tampilannya tidak berubah.
- Untuk thesis: buku ini bisa dikutip sebagai rujukan penyusunan penjelasan grammar (lihat `_sumber` di file JSON).
