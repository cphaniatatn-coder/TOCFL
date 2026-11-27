/**
 * Penerima hasil TAMPILAN SISWA (versi terkunci) → Google Sheet.
 * Tempel di Google Sheet BARU: Ekstensi → Apps Script, lalu Deploy sebagai Web app
 * (Jalankan sebagai: Saya, Akses: Siapa saja). Panduan: _kerja/siswa/PANDUAN-kirim-siswa.md
 *
 * Enam sheet dibuat otomatis (kirim ulang = baris lama diperbarui, tidak dobel):
 *   Siswa       — 1 baris per siswa: data diri (+ email, WhatsApp, bersedia wawancara), titik mulai, bab sekarang,
 *                 jumlah bab lulus, posisi & waktu aktif terakhir (→ pantau siswa yang berhenti / pilih siswa wawancara)
 *   Penempatan  — 1 baris per siswa × tahap (A0/A1/A2): skor, benar/salah per butir (q1–q20) & huruf jawaban (j1–j20)
 *   TesAkhir    — 1 baris per siswa × volume: sama dengan Penempatan (paket B)
 *   Bab         — 1 baris per siswa × bab yang pernah dibuka: tahap, Tes Bab (terbaik/terakhir/jumlah), lulus, menit belajar
 *   TesBab      — 1 baris per percobaan Tes Bab (siswa × bab × percobaan ke-)
 *   Evaluasi    — 1 baris per siswa: e1–e9 (Likert 1–5) + 3 jawaban terbuka
 */

var N_TES = 20, N_EVAL = 9;
function nomor(p, n) { var a = []; for (var i = 1; i <= n; i++) a.push(p + i); return a; }

var KOLOM = {
  Siswa: ['uid', 'nama', 'email', 'whatsapp', 'asal', 'usia', 'penilaian_diri', 'lama_belajar', 'pernah_tocfl', 'lulus_tocfl', 'rencana_tocfl',
          'tujuan', 'cara_belajar', 'bersedia_wawancara', 'cara_penempatan', 'mulai_bab', 'penempatan_selesai', 'bab_sekarang', 'bab_lulus',
          'posisi_terakhir', 'aktif_terakhir', 'mulai', 'perangkat', 'terakhir_kirim', 'jumlah_kirim'],
  Penempatan: ['uid', 'nama', 'tahap', 'paket', 'skor', 'lulus_tahap', 'benar', 'dari', 'dengar', 'baca', 'detik', 'selesai']
              .concat(nomor('q', N_TES)).concat(nomor('j', N_TES)),
  TesAkhir: ['uid', 'nama', 'volume', 'paket', 'skor', 'benar', 'dari', 'dengar', 'baca', 'detik', 'selesai']
            .concat(nomor('q', N_TES)).concat(nomor('j', N_TES)),
  Bab: ['uid', 'nama', 'kode', 'tahap', 'selesai_refleksi', 'tes_best', 'tes_last', 'tes_kali', 'lulus', 'lulus_waktu',
        'tugas_best', 'tugas_kali', 'tes_kata_best', 'menit_belajar', 'diperbarui'],
  TesBab: ['uid', 'nama', 'kode', 'percobaan', 'skor', 'dengar', 'baca', 'detik', 'waktu'],
  Evaluasi: ['uid', 'nama', 'waktu'].concat(nomor('e', N_EVAL)).concat(['terbuka1', 'terbuka2', 'terbuka3']),
};

function doGet() {
  return jawab({ ok: true, pesan: 'Penerima hasil tampilan siswa TOCFL aktif.' });
}

function doPost(e) {
  var kunci = LockService.getScriptLock();
  kunci.waitLock(20000);
  try {
    var d = JSON.parse(e.postData.contents);
    if (d.v !== 'siswa1' || !d.uid) return jawab({ ok: false, error: 'format data tidak dikenal' });
    var uid = "'" + String(d.uid).slice(0, 20), nama = teks(d.nama, 60), p = d.profil || {};
    var ss = SpreadsheetApp.getActiveSpreadsheet(), sekarang = new Date();

    var sp = sheet(ss, 'Siswa'), lama = cari(sp, function (x) { return "'" + x[0] === uid; });
    var kali = lama.length ? (Number(sp.getRange(lama[0], KOLOM.Siswa.length).getValue()) || 0) + 1 : 1;
    tulis(sp, lama, [[uid, nama, teks(d.email, 100), teks(d.wa, 30), teks(d.asal, 100), teks(p.usia, 20), teks(p.mandarin, 4), teks(p.lama, 20),
                      teks(p.pernah, 10), teks(p.lulus, 40), teks(p.rencana, 30), teks(p.tujuan, 30), teks(p.cara, 30), teks(p.wawancara, 20),
                      teks(d.cara, 10), teks(d.mulai_bab, 6), tgl(d.tempat_selesai), teks(d.kini, 6), d.bab_lulus || 0,
                      teks(d.posisi, 30), tgl(d.aktif), tgl(d.mulai), teks(d.perangkat, 20), sekarang, kali]]);

    var baris = function (h) {
      var b = h.butir || [];
      return { atas: [teks(h.paket, 2), h.skor, h.benar, h.dari, h.dengar, h.baca, h.detik, tgl(h.selesai)],
               bawah: isi(b.map(function (x) { return x.benar; }), N_TES).concat(isi(b.map(function (x) { return teks(x.jawab, 2); }), N_TES)) };
    };
    var tempat = [];
    Object.keys(d.tahap || {}).forEach(function (lv) {
      var h = d.tahap[lv], r = baris(h);
      tempat.push([uid, nama, teks(lv, 4), r.atas[0], h.skor, h.skor >= 80 ? 'ya' : ''].concat(r.atas.slice(2)).concat(r.bawah));
    });
    simpanBanyak(sheet(ss, 'Penempatan'), function (x) { return x[0] + '|' + x[2]; }, tempat);

    var akhir = [];
    Object.keys(d.post || {}).forEach(function (v) {
      var h = (d.post[v] || {}).tes; if (!h) return;
      var r = baris(h);
      akhir.push([uid, nama, Number(v)].concat(r.atas).concat(r.bawah));
    });
    simpanBanyak(sheet(ss, 'TesAkhir'), function (x) { return x[0] + '|' + x[2]; }, akhir);

    simpanBanyak(sheet(ss, 'Bab'), function (x) { return x[0] + '|' + x[2]; },
      (d.bab || []).slice(0, 150).map(function (m) {
        return [uid, nama, teks(m.kode, 6), m.tahap, m.selesai ? 'ya' : '', m.tes_best, m.tes_last, m.tes_kali, m.lulus ? 'ya' : '', tgl(m.lulus_waktu),
                m.tugas_best, m.tugas_kali, m.kata_tes, Math.round((Number(m.detik) || 0) / 60), sekarang];
      }));

    simpanBanyak(sheet(ss, 'TesBab'), function (x) { return x[0] + '|' + x[2] + '|' + x[3]; },
      (d.log || []).slice(-300).map(function (t) {
        return [uid, nama, teks(t.kode, 6), t.ke, t.skor, t.dengar, t.baca, t.detik, tgl(t.waktu)];
      }));

    if (d.eval) {
      simpanBanyak(sheet(ss, 'Evaluasi'), function (x) { return x[0]; },
        [[uid, nama, tgl(d.eval.waktu)].concat(isi(d.eval.jw, N_EVAL)).concat(isi((d.eval.terbuka || []).map(function (t) { return teks(t, 1000); }), 3))]);
    }
    return jawab({ ok: true });
  } catch (err) {
    return jawab({ ok: false, error: String(err) });
  } finally {
    kunci.releaseLock();
  }
}

function isi(arr, n) { var a = []; for (var i = 0; i < n; i++) a.push(arr && arr[i] != null ? arr[i] : ''); return a; }
function tgl(ms) { return ms ? new Date(ms) : ''; }

function sheet(ss, nama) {
  var s = ss.getSheetByName(nama);
  if (!s) {
    s = ss.insertSheet(nama);
    s.setFrozenRows(1);
  }
  var h = s.getRange(1, 1, 1, KOLOM[nama].length);
  if (h.getValues()[0].join('|') !== KOLOM[nama].join('|')) h.setValues([KOLOM[nama]]).setFontWeight('bold');
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

// teks dari siswa: dipotong & diawali ' bila bisa dibaca sebagai rumus (=, +, -, @)
function teks(x, maks) {
  var t = String(x == null ? '' : x).slice(0, maks);
  return /^[=+\-@<>]/.test(t) ? "'" + t : t;
}

function jawab(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
