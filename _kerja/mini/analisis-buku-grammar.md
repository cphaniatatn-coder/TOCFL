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

---

# Buku kedua: 進階篇

**Buku:** 劉崇仁、張莉萍（編著）《看圖學中文語法・進階篇》 *The Ultimate Illustrated Chinese Grammar Guide (Advanced Level)*,
MTC NTNU 策劃. File: `TOCFL/看圖學中文語法進階篇.pdf` (scan, 116 halaman PDF; halaman buku *b* ≈ halaman PDF b/2 + 2).
Sasaran TOCFL **Band B** (Level 3–4): 32 unit pola kalimat majemuk + 3 set latihan membaca Band B. Pola yang mirip
fungsinya disandingkan dalam satu unit (mis. 只要…就 vs 只有…才, 要是 vs 既然, 一直 vs 一向 vs 往往).

| Bab | Grammar modul | Unit 進階篇 | Dipakai sebagai catatan |
|---|---|---|---|
| B19 | 比 | 7 | A 比不上 / 不如 B |
| B33 | (tingkat bab, kata 以為) | 15 | 以為 = mengira (keliru), 以為…，沒想到… |
| B40 | 因為…所以, 但是, 才/就 | 3, 5, 28 | …，是因為…, 之所以…是因為, 由於…因此 (formal); 雖然 → wajib 可是/但是/不過; 再 vs 才 |
| C04 | 把 | 32 | 把 O V了 + jumlah kali / + bagian dari O |
| C24 | 要是…就, …的話 | 4, 12 | 要是 (lisan) vs 如果 (formal), 既然…就 (fakta), 只要…就 / 只有…才 |
| C28 | (tingkat bab, 一直咳嗽) | 27 | 一直 vs 一向 |
| C58 | 不但…而且, 沒想到 | 9, 15 | letak 不但 menurut subjek, topik + dua subjek, 既…又…; 以為…，沒想到… |
| C16 | 必須 / 不用 | — | tidak dibahas di kedua buku |

## Soal latihan grammar tambahan
`_kerja/mini/latihan_grammar.py` → `latihan_grammar.json`: 4 soal per poin grammar (29 poin) + 3 soal per topik tingkat bab
(A10, A18, A24, B40) = 128 soal, id/en/vi, setiap soal dengan penjelasan. Kalimat Mandarin diperiksa otomatis hanya memakai
kata yang sudah diajarkan sampai bab itu (`cek_dialog.kosakata_sampai`). Ditampilkan di 語法聚焦 sebagai "✏️ Latihan
tambahan" di bawah "Cek cepat"; jawaban disimpan di progres bab (`glat`).
