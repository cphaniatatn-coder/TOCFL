/* Kirim hasil belajar ke Google Sheet guru (untuk uji coba / data thesis).
   Penerima = Google Apps Script web app (kode: _kerja/kirim_hasil.gs, panduan: _kerja/PANDUAN-kirim-hasil.md).
   Hanya dikirim bila peserta menekan tombol & menyetujui; tanpa KIRIM_URL fitur ini tersembunyi.
   Kirim ulang = baris lama diperbarui (kunci: id acak perangkat + kode modul). */

const KIRIM_URL = '';   // ← isi dengan URL web app Apps Script (https://script.google.com/macros/s/…/exec)
const PESERTA_KEY = 'tocfl_peserta';

const Kirim = {
  aktif() { return !!KIRIM_URL; },

  peserta() {
    const p = Store.get(PESERTA_KEY, {});
    if (!p.uid) {
      p.uid = (crypto.randomUUID ? crypto.randomUUID() : Date.now().toString(36) + Math.random().toString(36).slice(2)).slice(0, 13);
      Store.set(PESERTA_KEY, p);
    }
    return p;
  },

  /* Kumpulkan data dari localStorage — hanya progres app, tanpa data pribadi selain nama/kelas yang diketik peserta. */
  data(nama, kelas) {
    const prog = Store.get(STORAGE_KEY, {});
    const modul = Object.entries(prog).map(([kode, p]) => ({
      kode,
      tahap: (p.stage || 0) + 1,
      selesai: !!p.done,
      tugas_best: p.tasks?.best ?? '', tugas_last: p.tasks?.last ?? '', tugas_kali: p.tasks?.tries ?? '',
      tes_best: p.tes?.best ?? '', tes_last: p.tes?.last ?? '', tes_kali: p.tes?.tries ?? '',
      kata_hafal: Object.values(p.known || {}).filter(Boolean).length,
      yakin: (p.cando || []).filter(x => x === 2).length,
      target: p.goal || '', sulit: p.diff || '',
    })).sort((a, b) => a.kode.localeCompare(b.kode));
    const uj = Store.get(UJIAN_KEY, {});
    const ujian = Object.entries(uj).flatMap(([vol, xs]) => xs.map(x => ({ vol: +vol, waktu: new Date(x.d).toISOString(), soal: x.n, nilai: x.pct, dengar: x.l, baca: x.r })));
    const vs = Object.values(Store.get(VSTATS_KEY, {}));
    const tes = modul.filter(m => m.tes_best !== '');
    return {
      v: 1, uid: this.peserta().uid, nama, kelas,
      waktu: new Date().toISOString(),
      perangkat: /Mobi|Android|iPhone/i.test(navigator.userAgent) ? 'HP' : 'Komputer',
      ringkasan: {
        modul_dibuka: modul.length,
        modul_selesai: modul.filter(m => m.selesai).length,
        tes_bab: tes.length,
        rata_tes: tes.length ? Math.round(tes.reduce((a, m) => a + m.tes_best, 0) / tes.length) : '',
        ujian: ujian.length,
        kata_dilatih: vs.length,
        jawaban_benar: vs.reduce((a, x) => a + (x.r || 0), 0),
        jawaban_salah: vs.reduce((a, x) => a + (x.w || 0), 0),
      },
      modul, ujian,
    };
  },

  render() {
    App.bar(T('Send results', 'Kirim hasil'), '#/');
    if (!this.aktif()) { App.main(`<div class="empty"><p>${T('Your teacher has not turned on result sending yet.', 'Fitur kirim hasil belum diaktifkan oleh guru.')}</p></div>`); return; }
    const p = this.peserta(), r = this.data(p.nama || '', p.kelas || '').ringkasan;
    App.main(`
      <div class="panel"><div class="panel-k">${Pic.html('📊', 'ic-sm')} ${T('What will be sent', 'Yang akan dikirim')}</div>
        <ul class="kirim-list">
          ${(LANG === 'id' ? ['Nama & kelas yang kamu ketik di bawah', 'Progres modul: tahap, nilai tugas & Tes Bab, jumlah kata dihafal', 'Tulisan refleksi: target pribadi & bagian yang masih sulit', 'Nilai ujian simulasi & jumlah latihan kosakata']
            : ['The name & class you type below', 'Module progress: stage, task & unit-test scores, words memorised', 'Your reflections: personal goals & parts that are still difficult', 'Mock exam scores & amount of vocabulary practice']).map(x => `<li>${x}</li>`).join('')}
        </ul>
        <p class="hint">${LANG === 'id' ? `Saat ini: ${r.modul_selesai} modul selesai · ${r.tes_bab} Tes Bab${r.rata_tes !== '' ? ` (rata-rata ${r.rata_tes}%)` : ''} · ${r.ujian} ujian simulasi · ${r.kata_dilatih} kata dilatih.`
          : `So far: ${r.modul_selesai} modules done · ${r.tes_bab} unit tests${r.rata_tes !== '' ? ` (average ${r.rata_tes}%)` : ''} · ${r.ujian} mock exams · ${r.kata_dilatih} words practised.`}</p>
        <p class="hint">${Pic.html('🔒', 'ic-xs')} ${T('The data is only used by your teacher for learning research. You can send again at any time — the old data will be updated.', 'Data hanya dipakai gurumu untuk penelitian pembelajaran. Kamu boleh mengirim ulang kapan saja — data lama diperbarui.')}</p>
      </div>
      <label class="field-k" for="k-nama">${T('Name', 'Nama')}</label>
      <input id="k-nama" class="field" autocomplete="name" maxlength="60" value="${esc(p.nama || '')}" placeholder="${T('Full name', 'Nama lengkap')}">
      <label class="field-k" for="k-kelas">${T('Class / group code (optional)', 'Kelas / kode kelompok (boleh kosong)')}</label>
      <input id="k-kelas" class="field" maxlength="40" value="${esc(p.kelas || '')}" placeholder="${T('E.g. Evening Mandarin', 'Mis. Mandarin Sore')}">
      <div class="checks" style="margin-top:14px"><label><input type="checkbox" id="k-setuju"> ${T('I agree to send the data above to my teacher.', 'Saya setuju data di atas dikirim ke guru.')}</label></div>
      <button class="btn primary block" id="k-btn" onclick="Kirim.kirim()">${Pic.html('📤', 'ic-sm')} ${T('Send results', 'Kirim hasil')}</button>
      <p class="hint" id="k-status">${p.terakhir ? `${T('Last sent', 'Terakhir dikirim')}: ${new Date(p.terakhir).toLocaleString(Lang.LOCALE)}` : ''}</p>`);
  },

  async kirim() {
    const nama = document.getElementById('k-nama').value.trim(), kelas = document.getElementById('k-kelas').value.trim();
    const btn = document.getElementById('k-btn'), st = document.getElementById('k-status');
    if (!nama) { App.toast(T('Enter your name first.', 'Isi namamu dulu.')); document.getElementById('k-nama').focus(); return; }
    if (!document.getElementById('k-setuju').checked) { App.toast(T('Tick the consent box first.', 'Centang persetujuan dulu.')); return; }
    Store.set(PESERTA_KEY, Object.assign(this.peserta(), { nama, kelas }));
    btn.disabled = true; st.textContent = T('Sending…', 'Mengirim…');
    try {
      // text/plain = "simple request": tidak memicu preflight CORS yang tidak didukung Apps Script
      const res = await fetch(KIRIM_URL, { method: 'POST', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(this.data(nama, kelas)) });
      const j = await res.json();
      if (!j.ok) throw new Error(j.error || 'ditolak');
      Store.set(PESERTA_KEY, Object.assign(this.peserta(), { terakhir: Date.now() }));
      st.textContent = T(`Sent ${new Date().toLocaleString(Lang.LOCALE)}. Thank you!`, `Terkirim ${new Date().toLocaleString(Lang.LOCALE)}. Terima kasih!`);
      App.toast(T('Results sent. 謝謝！', 'Hasil terkirim. 謝謝！'));
    } catch (e) {
      st.textContent = T('Sending failed. Check your internet connection, then try again.', 'Gagal mengirim. Periksa koneksi internet, lalu coba lagi.');
    } finally { btn.disabled = false; }
  },
};
