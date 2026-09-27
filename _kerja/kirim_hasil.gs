/**
 * Penerima "Kirim hasil" app TOCFL Band A → Google Sheet.
 * Tempel di Google Sheet: Ekstensi → Apps Script, lalu Deploy sebagai Web app
 * (Jalankan sebagai: Saya, Akses: Siapa saja). Panduan: _kerja/PANDUAN-kirim-hasil.md
 *
 * Tiga sheet dibuat otomatis:
 *   Peserta — 1 baris per peserta (perangkat), ringkasan terbaru
 *   Modul   — 1 baris per peserta × modul (diperbarui saat kirim ulang)
 *   Ujian   — 1 baris per ujian simulasi
 */

var KOLOM = {
  Peserta: ['uid', 'nama', 'kelas', 'terakhir_kirim', 'perangkat', 'modul_dibuka', 'modul_selesai', 'tes_bab', 'rata_tes',
            'ujian', 'kata_dilatih', 'jawaban_benar', 'jawaban_salah', 'jumlah_kirim'],
  Modul: ['uid', 'nama', 'kelas', 'kode', 'tahap', 'selesai', 'tugas_best', 'tugas_last', 'tugas_kali',
          'tes_best', 'tes_last', 'tes_kali', 'kata_hafal', 'yakin', 'target', 'sulit', 'diperbarui'],
  Ujian: ['uid', 'nama', 'kelas', 'vol', 'waktu', 'soal', 'nilai', 'dengar', 'baca'],
};

function doGet() {
  return jawab({ ok: true, pesan: 'Penerima hasil TOCFL aktif.' });
}

function doPost(e) {
  var kunci = LockService.getScriptLock();
  kunci.waitLock(20000);
  try {
    var d = JSON.parse(e.postData.contents);
    if (d.v !== 1 || !d.uid || !d.nama) return jawab({ ok: false, error: 'format data tidak dikenal' });
    var nama = teks(d.nama, 60), kelas = teks(d.kelas, 40), uid = "'" + String(d.uid).slice(0, 20), r = d.ringkasan || {};
    var ss = SpreadsheetApp.getActiveSpreadsheet();

    var sp = sheet(ss, 'Peserta'), lama = cari(sp, function (x) { return "'" + x[0] === uid; });
    var kali = lama.length ? (Number(sp.getRange(lama[0], 14).getValue()) || 0) + 1 : 1;
    tulis(sp, lama, [[uid, nama, kelas, new Date(), teks(d.perangkat, 20), r.modul_dibuka, r.modul_selesai, r.tes_bab,
                      r.rata_tes, r.ujian, r.kata_dilatih, r.jawaban_benar, r.jawaban_salah, kali]]);

    var sekarang = new Date();
    simpanBanyak(sheet(ss, 'Modul'), function (x) { return x[0] + '|' + x[3]; },
      (d.modul || []).slice(0, 200).map(function (m) {
        return [uid, nama, kelas, teks(m.kode, 6), m.tahap, m.selesai ? 'ya' : '', m.tugas_best, m.tugas_last, m.tugas_kali,
                m.tes_best, m.tes_last, m.tes_kali, m.kata_hafal, m.yakin, teks(m.target, 500), teks(m.sulit, 500), sekarang];
      }));
    simpanBanyak(sheet(ss, 'Ujian'), function (x) { return x[0] + '|' + x[4]; },
      (d.ujian || []).slice(0, 500).map(function (u) {
        return [uid, nama, kelas, u.vol, "'" + String(u.waktu).slice(0, 30), u.soal, u.nilai, u.dengar, u.baca];
      }));
    return jawab({ ok: true });
  } catch (err) {
    return jawab({ ok: false, error: String(err) });
  } finally {
    kunci.releaseLock();
  }
}

function sheet(ss, nama) {
  var s = ss.getSheetByName(nama);
  if (!s) {
    s = ss.insertSheet(nama);
    s.getRange(1, 1, 1, KOLOM[nama].length).setValues([KOLOM[nama]]).setFontWeight('bold');
    s.setFrozenRows(1);
  }
  return s;
}

// nomor baris (1-based) yang cocok
function cari(s, cocok) {
  var n = s.getLastRow();
  if (n < 2) return [];
  var v = s.getRange(2, 1, n - 1, s.getLastColumn()).getValues(), hasil = [];
  for (var i = 0; i < v.length; i++) if (cocok(v[i])) hasil.push(i + 2);
  return hasil;
}

// Tulis banyak baris sekaligus: baris dengan kunci sama diperbarui, sisanya ditambah di bawah (satu kali tulis).
function simpanBanyak(s, kunci, baris) {
  if (!baris.length) return;
  var n = s.getLastRow(), ada = {};
  if (n > 1) s.getRange(2, 1, n - 1, baris[0].length).getValues().forEach(function (x, i) { ada[kunci(x)] = i + 2; });
  var baru = [];
  baris.forEach(function (b) {
    var k = kunci(b.map(function (v) { return typeof v === 'string' ? v.replace(/^'/, '') : v; }));
    if (ada[k] > 0) s.getRange(ada[k], 1, 1, b.length).setValues([b]);
    else { ada[k] = -1; baru.push(b); }
  });
  if (baru.length) s.getRange(s.getLastRow() + 1, 1, baru.length, baru[0].length).setValues(baru);
}

function tulis(s, baris, nilai) {
  if (baris.length) s.getRange(baris[0], 1, 1, nilai[0].length).setValues(nilai);
  else s.appendRow(nilai[0]);
}

// teks dari peserta: dipotong & diawali ' bila bisa dibaca sebagai rumus (=, +, -, @)
function teks(x, maks) {
  var t = String(x == null ? '' : x).slice(0, maks);
  return /^[=+\-@]/.test(t) ? "'" + t : t;
}

function jawab(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
