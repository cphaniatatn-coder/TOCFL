# Panduan: hasil tampilan siswa → Google Sheet

Tampilan siswa mengirim data **otomatis** setelah: data diri disimpan, setiap tahap tes penempatan, setiap percobaan
Tes Bab, setiap kali siswa mencapai tahap baru di sebuah bab, tes akhir, dan evaluasi. Siswa juga bisa mengirim ulang
dari halaman **Hasil**. Selama URL penerima belum diisi, data hanya tersimpan di perangkat siswa ("Belum terkirim").

## Pasang sekali (±5 menit)

1. Buka <https://sheets.new> → beri nama, mis. **Hasil Siswa Modul TOCFL**. Pakai Sheet BARU (terpisah dari Sheet modul mini).
2. Menu **Ekstensi → Apps Script**.
3. Hapus isi `Code.gs`, tempel seluruh isi `_kerja/siswa/kirim_siswa.gs`, lalu klik **Simpan**.
4. **Deploy → Deployment baru** → roda gigi → **Aplikasi web**:
   - *Jalankan sebagai*: **Saya**
   - *Yang memiliki akses*: **Siapa saja** (siswa tidak perlu akun Google)
   - **Deploy** → **Izinkan akses** → pilih akun → (bila muncul peringatan verifikasi) **Lanjutan → Buka … (tidak aman)** → **Izinkan**.
5. Salin **URL aplikasi web** (berakhiran `/exec`). Uji dengan membukanya di browser → harus tampil
   `{"ok":true,"pesan":"Penerima hasil tampilan siswa TOCFL aktif."}`.
6. Isi URL itu di `_kerja/siswa/config.json` → `"kirim_url": "…/exec"` (atau berikan ke Claude), lalu jalankan
   `py _kerja/buat_siswa.py` dan push repo siswa.

## Isi Sheet

| Sheet | Satu baris = | Isi |
|---|---|---|
| **Siswa** | satu siswa | nama, email, WhatsApp, asal, data diri (usia, penilaian diri, lama belajar, TOCFL, rencana, tujuan, cara belajar), **bersedia wawancara**, cara penempatan & bab mulai, bab sekarang, jumlah bab lulus, posisi & waktu aktif terakhir |
| **Penempatan** | siswa × tahap (A0/A1/A2) | paket A, skor %, lulus tahap (≥ 80%), benar/dari, 聽力 %, 閱讀 %, detik, q1–q20 (1 = benar), j1–j20 (huruf jawaban asli) |
| **TesAkhir** | siswa × volume | paket B, skor %, benar/dari, 聽力 %, 閱讀 %, detik, q1–q20, j1–j20 |
| **Bab** | siswa × bab yang pernah dibuka | tahap, refleksi selesai, Tes Bab (terbaik/terakhir/jumlah), lulus & waktunya, nilai tugas, Tes Kosakata, menit belajar |
| **TesBab** | satu percobaan Tes Bab | bab, percobaan ke-, skor %, 聽力 %, 閱讀 %, detik, waktu |
| **Evaluasi** | satu siswa | e1–e9 (Likert 1–5) + 3 jawaban terbuka |

- Kolom **bersedia_wawancara**, **bab_lulus**, dan **aktif_terakhir** di sheet Siswa membantu memilih siswa untuk 深度訪談.
- Kirim ulang tidak membuat baris ganda — baris lama diperbarui (kunci: uid / uid + tahap / uid + bab / uid + bab + percobaan).

## Catatan

- Siswa dikenali dari kode acak di perangkatnya (`uid`, tampil sebagai "Kode siswa" di halaman Hasil). Ganti HP/browser
  = siswa baru, jadi minta siswa memakai satu perangkat dari awal sampai akhir.
- Mode admin: ketik nama **admin** di Data diri → semua bab terbuka, tidak ada data yang dikirim (untuk mencoba tampilan).
- URL `/exec` ada di kode app yang publik; skrip menolak format yang salah & menetralkan rumus, tapi periksa Sheet sebelum analisis.
- Bila `kirim_siswa.gs` diubah: **Deploy → Kelola deployment → edit (pensil) → Versi baru → Deploy** (URL tetap sama).
