# Panduan: Kirim hasil ke Google Sheet

Tombol **Kirim hasil belajar** di beranda app mengirim progres peserta ke Google Sheet milik guru.
Selama `KIRIM_URL` di `js/kirim.js` masih kosong, tombol itu **tidak muncul**.

## Pasang sekali (±5 menit)

1. Buka <https://sheets.new> (masuk dengan akun Google Anda) → beri nama, mis. **Hasil Uji Coba TOCFL**.
2. Menu **Ekstensi → Apps Script**.
3. Hapus isi `Code.gs`, lalu tempel seluruh isi file `_kerja/kirim_hasil.gs`. Klik **Simpan** (ikon disket).
4. Klik **Deploy → Deployment baru**.
   - Ikon roda gigi → pilih **Aplikasi web**.
   - *Jalankan sebagai*: **Saya**.
   - *Yang memiliki akses*: **Siapa saja** (peserta tidak perlu akun Google).
   - Klik **Deploy** → **Izinkan akses** → pilih akun Anda → (bila muncul "Google belum memverifikasi aplikasi ini")
     **Lanjutan → Buka … (tidak aman)** → **Izinkan**. Ini normal untuk skrip buatan sendiri.
5. Salin **URL aplikasi web** (berakhiran `/exec`).
6. Tempel URL itu di `js/kirim.js` → `const KIRIM_URL = '…';`, lalu commit & push (atau berikan URL ke Claude).
7. Uji: buka URL `/exec` di browser → harus tampil `{"ok":true,"pesan":"Penerima hasil TOCFL aktif."}`.

## Isi Sheet

| Sheet | Satu baris = | Isi |
|---|---|---|
| **Peserta** | satu peserta (per perangkat) | nama, kelas, waktu kirim terakhir, jumlah modul selesai, Tes Bab & rata-ratanya, ujian simulasi, latihan kosakata, berapa kali mengirim |
| **Modul** | peserta × modul | tahap terakhir, selesai, nilai tugas & Tes Bab (terbaik/terakhir/berapa kali), kata dihafal, target "yakin", tulisan target pribadi & bagian sulit |
| **Ujian** | satu ujian simulasi | volume, waktu, jumlah soal, nilai total/聽力/閱讀 |

Kirim ulang tidak membuat baris ganda — baris lama diperbarui.

## Catatan

- Peserta dikenali dari kode acak di perangkatnya (`uid`), bukan dari nama. Ganti HP/browser = peserta baru.
- Peserta harus mencentang persetujuan sebelum mengirim (penting untuk etika penelitian thesis).
- URL `/exec` ada di kode app yang publik, jadi siapa pun secara teknis bisa mengirim data ke Sheet. Skrip menolak data
  yang formatnya salah & menetralkan rumus (`=…`), tapi tetap periksa Sheet sebelum dianalisis.
- Bila kode `kirim_hasil.gs` diubah: **Deploy → Kelola deployment → edit (pensil) → Versi: Versi baru → Deploy**
  (URL tetap sama).
