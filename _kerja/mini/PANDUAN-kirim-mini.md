# Panduan: hasil uji coba modul mini → Google Sheet

App mini mengirim data peserta **otomatis** setelah tiap langkah: kuesioner awal, tes awal, setiap bab selesai, kuesioner
akhir, tes akhir, dan evaluasi. Peserta juga bisa mengirim ulang dari halaman **Hasil**. Selama URL penerima belum diisi,
data hanya tersimpan di perangkat peserta (halaman Hasil menampilkan "Belum terkirim").

## Pasang sekali (±5 menit)

1. Buka <https://sheets.new> → beri nama, mis. **Hasil Uji Coba Modul Mini**. Pakai Sheet BARU, terpisah dari app utama.
2. Menu **Ekstensi → Apps Script**.
3. Hapus isi `Code.gs`, tempel seluruh isi `_kerja/mini/kirim_mini.gs`, lalu klik **Simpan**.
4. **Deploy → Deployment baru** → roda gigi → **Aplikasi web**:
   - *Jalankan sebagai*: **Saya**
   - *Yang memiliki akses*: **Siapa saja** (peserta tidak perlu akun Google)
   - **Deploy** → **Izinkan akses** → pilih akun → (bila muncul peringatan verifikasi) **Lanjutan → Buka … (tidak aman)** → **Izinkan**.
5. Salin **URL aplikasi web** (berakhiran `/exec`). Uji dengan membukanya di browser → harus tampil
   `{"ok":true,"pesan":"Penerima hasil modul mini TOCFL aktif."}`.
6. Isi URL itu di `_kerja/mini/config.json` → `"kirim_url": "…/exec"` (atau berikan ke Claude), lalu jalankan
   `py _kerja/buat_mini.py` dan push repo mini.

## Isi Sheet

| Sheet | Satu baris = | Isi |
|---|---|---|
| **Peserta** | satu peserta | nama, bahasa, level, data diri (usia, negara, kemampuan, pernah TOCFL, lama belajar, rencana), waktu mulai/selesai, skor kecemasan pre/post, nilai tes pre/post, jumlah bab selesai |
| **Kecemasan** | peserta × fase (pre/post) | skor total 20–100 + dimensi A (umum), B (聽力), C (閱讀), D (kesiapan) + jawaban mentah b1–b20 |
| **Tes** | peserta × fase | paket (A/B), skor %, benar/dari, 聽力 %, 閱讀 %, detik, percobaan ke-, q1–q20 (1 = benar), j1–j20 (huruf jawaban) |
| **Modul** | peserta × bab | tahap, selesai & waktunya, nilai tugas & Tes Bab, kata dihafal, target, bagian sulit |
| **Evaluasi** | satu peserta | e1–e10 (Likert 1–5) + 3 jawaban terbuka |

- Skor kecemasan sudah memperhitungkan butir terbalik (R): makin tinggi = makin cemas. Jawaban mentah (b1–b20) tetap
  disimpan apa adanya (1–5 seperti yang dipilih peserta) untuk uji reliabilitas.
- q1–q20 per butir (Part 4 dihitung per titik kosong) → bisa langsung dipakai untuk Cronbach α / analisis butir.
- Kirim ulang tidak membuat baris ganda — baris lama diperbarui (kunci: uid + fase / uid + bab).

## Catatan

- Peserta dikenali dari kode acak di perangkatnya (`uid`, tampil sebagai "Kode peserta" di halaman Hasil). Ganti HP/browser
  = peserta baru, jadi minta peserta memakai satu perangkat dari awal sampai akhir.
- Bila tes awal/akhir diulang (mis. halaman dimuat ulang di tengah tes), kolom **percobaan** > 1 — perhatikan saat analisis.
- URL `/exec` ada di kode app yang publik; skrip menolak format yang salah & menetralkan rumus, tapi periksa Sheet sebelum analisis.
- Bila `kirim_mini.gs` diubah: **Deploy → Kelola deployment → edit (pensil) → Versi baru → Deploy** (URL tetap sama).
