#!/bin/sh
# cek_draf.sh KODE → validasi draf latihan & tes, tampilkan hanya masalah (abaikan gambar yang belum dibuat & pola kosong)
for f in latihan tes; do
  py soal_ai/buat_soal.py $1 --periksa soal_ai/hasil/$1-$f.json | head -1 | sed "s/^/$f: /"
  grep -E "^## |✗|⚑" soal_ai/hasil/$1-tinjau.md | grep -v -E "jalankan py _kerja/gambar_soal|pola_pengecoh kosong" | grep -B1 -E "✗|⚑" | grep -v "^--"
done
