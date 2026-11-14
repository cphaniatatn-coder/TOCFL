#!/bin/sh
# selesai_bab.sh KODE… → pasang draf, tulis SVG, rakit ulang, lembar tinjau, terjemah
py _kerja/soal_ai/pasang.py "$@" || exit 1
py _kerja/gambar_soal.py 2>&1 | grep Vol.1
py _kerja/bangun_modul.py 2>&1 | grep -E -v ": OK$" | grep -v -E "C15|C20|當中|月台" | tail -5
py _kerja/bangun_bank.py 2>&1 | tail -1
py _kerja/soal_ai/lembar_tinjau.py "$@"
py _kerja/terjemah.py 2>&1 | tail -1
