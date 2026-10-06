/**
 * Penerima hasil MODUL MINI (uji coba thesis) → Google Sheet.
 * Tempel di Google Sheet BARU: Ekstensi → Apps Script, lalu Deploy sebagai Web app
 * (Jalankan sebagai: Saya, Akses: Siapa saja). Panduan: _kerja/mini/PANDUAN-kirim-mini.md
 *
 * Lima sheet dibuat otomatis (kirim ulang = baris lama diperbarui, tidak dobel):
 *   Peserta    — 1 baris per peserta: data diri (+ email), level, ringkasan pre/post, posisi terakhir di bab
 *                (posisi_terakhir/aktif_terakhir diperbarui setiap peserta mencapai tahap baru → pantau yang berhenti)
 *   Kecemasan  — 1 baris per peserta × fase (pre/post): skor total, dimensi A–D, jawaban butir 1–20 (mentah)
 *   Tes        — 1 baris per peserta × fase: skor, waktu, benar/salah per butir (q1–q20) & huruf jawaban (j1–j20)
 *   Modul      — 1 baris per peserta × bab
 *   Evaluasi   — 1 baris per peserta: e1–e10 (Likert) + 3 jawaban terbuka
 * Putaran lanjutan: peserta yang sudah selesai boleh lanjut ke level di atasnya. Putaran 2, 3 dikirim dengan
 *   uid "<kode>-P2", "<kode>-P3" → baris terpisah (putaran 1 tidak tertimpa). Kolom kode_asal = kode tanpa -P,
 *   putaran = 1/2/3, level_awal = level putaran 1. Analisis utama: putaran = 1.
 * Skor kecemasan: butir (R) sudah dibalik di app; total 20–100, makin tinggi = makin cemas.
 */

var N_CEMAS = 20, N_TES = 20, N_EVAL = 10;
function nomor(p, n) { var a = []; for (var i = 1; i <= n; i++) a.push(p + i); return a; }

var KOLOM = {
  Peserta: ['uid', 'kode_asal', 'putaran', 'nama', 'email', 'bahasa', 'level', 'level_awal', 'usia', 'negara', 'penilaian_diri', 'pernah_tocfl', 'lulus_tocfl',
            'lama_belajar', 'rencana_tocfl',
            'mulai', 'selesai', 'cemas_pre', 'cemas_post', 'tes_pre', 'tes_post', 'bab_selesai', 'posisi_terakhir', 'aktif_terakhir', 'perangkat', 'terakhir_kirim', 'jumlah_kirim'],
  Kecemasan: ['uid', 'nama', 'level', 'fase', 'waktu', 'total', 'A_umum', 'B_dengar', 'C_baca', 'D_kesiapan'].concat(nomor('b', N_CEMAS)).concat(['putaran']),
  Tes: ['uid', 'nama', 'level', 'fase', 'paket', 'skor', 'benar', 'dari', 'dengar', 'baca', 'detik', 'percobaan', 'selesai']
       .concat(nomor('q', N_TES)).concat(nomor('j', N_TES)).concat(['putaran']),
  Modul: ['uid', 'nama', 'level', 'kode', 'tahap', 'selesai', 'selesai_waktu', 'tugas_best', 'tugas_kali', 'tes_best', 'tes_kali',
          'kata_hafal', 'yakin', 'target', 'sulit', 'diperbarui', 'putaran'],
  Evaluasi: ['uid', 'nama', 'level', 'waktu'].concat(nomor('e', N_EVAL)).concat(['terbuka1', 'terbuka2', 'terbuka3', 'putaran']),
};

function doGet() {
  return jawab({ ok: true, pesan: 'Penerima hasil modul mini TOCFL aktif.' });
}

function doPost(e) {
  var kunci = LockService.getScriptLock();
  kunci.waitLock(20000);
  try {
    var d = JSON.parse(e.postData.contents);
    if (d.v !== 'mini1' || !d.uid) return jawab({ ok: false, error: 'format data tidak dikenal' });
    var uid = "'" + String(d.uid).slice(0, 20), nama = teks(d.nama, 60), lv = teks(d.level, 4), p = d.profil || {};
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var pre = d.pre || {}, post = d.post || {};
    var modul = d.modul || [];
    var put = Number(d.putaran) || 1, asal = "'" + String(d.uid_asal || d.uid).slice(0, 20);

    var sp = sheet(ss, 'Peserta'), lama = cari(sp, function (x) { return "'" + x[0] === uid; });
    var kali = lama.length ? (Number(sp.getRange(lama[0], KOLOM.Peserta.length).getValue()) || 0) + 1 : 1;
    tulis(sp, lama, [[uid, asal, put, nama, teks(d.email, 100), teks(d.lang, 4), lv, teks(d.level_awal || d.level, 4), teks(p.usia, 20), teks(p.negara, 30),
                      teks(p.mandarin, 4), teks(p.pernah, 10), teks(p.lulus, 40), teks(p.lama, 20), teks(p.rencana, 30), tgl(d.mulai), tgl(d.selesai),
                      pre.cemas_skor ? pre.cemas_skor.total : '', post.cemas_skor ? post.cemas_skor.total : '',
                      pre.tes ? pre.tes.skor : '', post.tes ? post.tes.skor : '',
                      modul.filter(function (m) { return m.selesai; }).length, teks(d.posisi, 30), tgl(d.aktif), teks(d.perangkat, 20), new Date(), kali]]);

    var cemas = [], tes = [];
    ['pre', 'post'].forEach(function (f) {
      var x = d[f] || {};
      if (x.cemas && x.cemas_skor) {
        var s = x.cemas_skor;
        cemas.push([uid, nama, lv, f, tgl(x.cemas_waktu), s.total, s.A, s.B, s.C, s.D].concat(isi(x.cemas, N_CEMAS)).concat([put]));
      }
      if (x.tes) {
        var t = x.tes, butir = t.butir || [];
        tes.push([uid, nama, lv, f, teks(t.paket, 2), t.skor, t.benar, t.dari, t.dengar, t.baca, t.detik, x.tes_coba, tgl(t.selesai)]
          .concat(isi(butir.map(function (b) { return b.benar; }), N_TES))
          .concat(isi(butir.map(function (b) { return teks(b.jawab, 2); }), N_TES)).concat([put]));
      }
    });
    simpanBanyak(sheet(ss, 'Kecemasan'), function (x) { return x[0] + '|' + x[3]; }, cemas);
    simpanBanyak(sheet(ss, 'Tes'), function (x) { return x[0] + '|' + x[3]; }, tes);

    var sekarang = new Date();
    simpanBanyak(sheet(ss, 'Modul'), function (x) { return x[0] + '|' + x[3]; },
      modul.slice(0, 20).map(function (m) {
        return [uid, nama, lv, teks(m.kode, 6), m.tahap, m.selesai ? 'ya' : '', tgl(m.selesai_waktu), m.tugas_best, m.tugas_kali,
                m.tes_best, m.tes_kali, m.kata_hafal, m.yakin, teks(m.target, 500), teks(m.sulit, 500), sekarang, put];
      }));

    if (d.eval) {
      simpanBanyak(sheet(ss, 'Evaluasi'), function (x) { return x[0]; },
        [[uid, nama, lv, sekarang].concat(isi(d.eval, N_EVAL)).concat(isi((d.terbuka || []).map(function (t) { return teks(t, 1000); }), 3)).concat([put])]);
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

// teks dari peserta: dipotong & diawali ' bila bisa dibaca sebagai rumus (=, +, -, @)
function teks(x, maks) {
  var t = String(x == null ? '' : x).slice(0, maks);
  return /^[=+\-@<>]/.test(t) ? "'" + t : t;
}

function jawab(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
