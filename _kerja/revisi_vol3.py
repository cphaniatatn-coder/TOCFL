"""Revisi dialog Vol.3/A2 berdasarkan laporan review Carli (《TOCFL 模組 Vol.1–3 對話審查報告》, 2026-11-04)
+ koreksi level TBCL. Sekali jalan: mengambil semua bab C dari BARU gabungan (pilot di dialog_cerita.py +
cerita_vol3.py), mengubahnya, lalu menulis ulang cerita_vol3.py berisi ke-67 bab (pilot di dialog_cerita.py dikosongkan).

Pemakaian: py _kerja/revisi_vol3.py   (lalu dialog_cerita.py tulis → bangun_modul → …)
Sudah dijalankan 2026-11-04; disimpan sebagai catatan perubahan per baris.
"""
import os, re, sys
K = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, K)
import dialog_cerita

B = {k: [v[0], [[d[0], d[1], [list(l) for l in d[2]]] for d in v[1]]]
     for k, v in dialog_cerita.BARU.items() if k.startswith('C')}
assert len(B) == 67, len(B)


def cari(code, zh):
    for d in B[code][1]:
        for i, l in enumerate(d[2]):
            if l[1] == zh:
                return d[2], i
    raise SystemExit(f'{code}: tidak ketemu {zh}')


def ganti(code, zh, baru_zh, baru_id, sp=None):
    L, i = cari(code, zh)
    L[i] = [sp or L[i][0], baru_zh, baru_id]


def sisip(code, zh_jangkar, sp, zh, idn):
    L, i = cari(code, zh_jangkar)
    L.insert(i + 1, [sp, zh, idn])


def hapus(code, zh):
    L, i = cari(code, zh)
    del L[i]


def scene(code, s):
    B[code][0] = s


def ganti_sp(code, lama, baru):
    for d in B[code][1]:
        for l in d[2]:
            if l[0] == lama:
                l[0] = baru


# C03 — yang mencuci baju Dawen; mereka serumah, jadi tidak bertanya letak mesin cuci; 早飯 → 早餐
ganti('C03', '好。你把碗洗了，我把衣服洗一洗。', '好。你把碗洗了，我把衣服放進洗衣機。昨天的衣服呢？',
      'Oke. Kamu cuci piringnya, aku masukkan baju ke mesin cuci. Baju kemarin di mana?')
ganti('C03', '好。洗衣機在哪裡？', '在門口，都乾了。你先拿進來吧。', 'Di depan pintu, sudah kering semua. Kamu ambil masuk dulu saja.', sp='志明')
ganti('C03', '在門口。昨天的衣服都乾了，我先拿進來。', '好！', 'Oke!', sp='王大文')
ganti('C03', '好。弄完了，我們去吃早飯吧！', '好。弄完了，我們去吃早餐吧！', 'Oke. Setelah beres, kita sarapan yuk!')
# C06 — tisu toilet: 包
ganti('C06', '只有一個了。我們去超市買日用品吧。', '只有一包了。我們去超市買日用品吧。', 'Tinggal satu bungkus. Ayo kita beli kebutuhan sehari-hari di supermarket.')
# C07 — pola judul (lamanya + 沒 + V + 了) benar-benar dipakai & logis; 出門 tetap muncul; satu minggu ↔ dua malam konsisten
scene('C07', 'Dua malam berturut-turut Dawen tidak tidur di ranjang karena mengerjakan PR dan belajar untuk ujian; '
             'pagi ini Zhiming menemukannya tertidur di meja. Di kampus Meimei melihatnya lelah, dan Dawen berjanji '
             'tidur lebih awal.')
ganti('C07', '大文，快起床！八點了！', '大文，快起床！八點了！你在桌子上睡覺？', 'Dawen, cepat bangun! Sudah jam delapan! Kamu tidur di meja?')
ganti('C07', '啊，我沒聽見鬧鐘！', '啊！我寫功課寫到半夜，就在桌子上睡覺了，沒聽見鬧鐘！', 'Aduh! Aku mengerjakan PR sampai tengah malam, lalu tertidur di meja, tidak dengar alarm!')
ganti('C07', '九點上課，你還沒出門呢！', '九點上課，八點半要出門，快一點！', 'Kuliah jam sembilan, jam setengah sembilan harus berangkat, cepat sedikit!')
hapus('C07', '我昨天半夜兩點才上床……')
ganti('C07', '寫功課。這兩天我每天兩點才睡覺。', '寫功課，準備考試。前天晚上我也沒上床……', 'Mengerjakan PR, belajar untuk ujian. Malam kemarin lusa aku juga tidak tidur di ranjang…')
ganti('C07', '這幾天我都很晚才睡覺。昨天上床以後，枕頭也不舒服……', '我兩天沒睡覺了！前天沒上床，昨天也是在桌子上睡覺的，還做了一個夢。',
      'Aku sudah dua hari tidak tidur! Kemarin lusa tidak tidur sama sekali, kemarin juga tidurnya di meja, mimpi pula.')
ganti('C07', '我還做了一個夢，夢見考試！時鐘上已經兩點了，我還沒寫完。', '夢見什麼？', 'Mimpi apa?', sp='李美美')
sisip('C07', '夢見什麼？', '王大文', '夢見考試！時鐘上已經兩點了，我還沒寫完。', 'Mimpi ujian! Di jam sudah pukul dua, aku belum selesai menulis.')
ganti('C07', '好，今天十點我就上床！', '好，今天十點我就上床！我很想我的枕頭！', 'Oke, hari ini jam sepuluh aku langsung ke ranjang! Aku kangen bantalku!')
# C08 — tidak mengulang pertanyaan C07; 好好 (C43) dihindari
ganti('C08', '大文，你昨天晚上幾點睡覺？', '大文，你今天看起來還是很累。', 'Dawen, hari ini kamu masih kelihatan capek.')
ganti('C08', '兩點！這幾天，我每天都很晚才睡覺。', '對！這幾天，我每天都很晚才睡覺。', 'Iya! Beberapa hari ini aku selalu tidur larut.')
ganti('C08', '說了。他們說十點以後不唱了。今天晚上我可以好好睡覺了！', '說了。他們說十點以後不唱了。今天晚上我可以早點睡覺了！',
      'Sudah. Mereka bilang setelah jam sepuluh tidak menyanyi lagi. Malam ini aku bisa tidur lebih awal!')
# C09 — Dawen orang Jakarta (B06); desa = rumah nenek (B12)
ganti('C09', '我在印尼住在鄉下，比較喜歡那樣的生活。', '我小時候常常去印尼的鄉下，在奶奶家住。我比較喜歡那樣的生活。',
      'Waktu kecil aku sering ke desa di Indonesia, menginap di rumah nenek. Aku lebih suka kehidupan seperti itu.')
# C12 — pewawancara bukan 王先生; 是…的 untuk detail masa lalu; judul disesuaikan (Annie besar di Jakarta)
ganti_sp('C12', '王先生', '張小姐')
ganti('C12', '你什麼時候來臺灣？', '你是什麼時候來臺灣的？', 'Kapan Anda datang ke Taiwan?')
# C13 — Dawen sudah ikut Imlek di rumah Meimei (B44) → foto Imlek waktu Meimei kecil
ganti('C13', '大文，你看，這是過年的時候我們家的照片。', '大文，你看，這是我小時候，我們家過年的照片。',
      'Dawen, lihat, ini foto keluargaku waktu Tahun Baru Imlek, waktu aku masih kecil.')
# C15 — cita-cita Dawen tetap guru Mandarin (B11)
ganti('C15', '我爸爸是商人，我外公以前是工人。爸爸希望我也當商人。你呢？', '我爸爸是商人，我外公以前是工人。爸爸希望我也當商人，可是我想當中文老師。你呢？',
      'Ayahku pedagang, kakekku dulu buruh. Ayah berharap aku juga jadi pedagang, tapi aku ingin jadi guru Mandarin. Kamu?')
# C16 — atasan = 黃先生 (sama dengan B11)
ganti_sp('C16', '王先生', '黃先生')
# C18 — Meimei suka film (A06, A11, C65): sekarang 'akhir-akhir ini jarang'
scene('C18', 'Dawen baru menonton film Amerika di bioskop, tetapi akhir-akhir ini Meimei jarang menonton film dan lebih '
             'suka berita dan majalah. Selera mereka berbeda, lalu mereka sepakat bermain game di rumah karena akhir '
             'pekan akan sangat panas.')
ganti('C18', '是嗎？我覺得美國電影不太有意思。', '是嗎？我最近不太看電影。', 'Oh ya? Akhir-akhir ini aku jarang nonton film.')
# C21 — 還是…吧 (C25) dihindari
ganti('C21', '今天我還是騎自行車吧！希望明年能夠自己騎機車去學校。', '今天我騎自行車就好！希望明年能夠自己騎機車去學校。',
      'Hari ini aku naik sepeda saja! Semoga tahun depan aku bisa naik motor sendiri ke kampus.')
# C22 — orang Indonesia tidak butuh visa pulang ke Indonesia; kata inti 簽證 tetap dipakai dengan benar
scene('C22', 'Dawen bersiap pulang ke Indonesia untuk pernikahan kakaknya: tiket pesawatnya baru didapat dan kopernya '
             'kurang, jadi Meimei meminjamkan koper. Setibanya di Indonesia ia menelepon Meimei.')
ganti('C22', '不，我明天才出國。簽證昨天才拿到。', '不，我明天才出國。飛機票昨天才拿到。', 'Bukan, aku baru berangkat besok. Tiket pesawatnya baru kudapat kemarin.')
sisip('C22', '不，我明天才出國。飛機票昨天才拿到。', '李美美', '你要簽證嗎？', 'Kamu perlu visa?')
sisip('C22', '你要簽證嗎？', '王大文', '不用，我是印尼人，回印尼不需要簽證。', 'Tidak, aku orang Indonesia, pulang ke Indonesia tidak perlu visa.')
# C25 — Annie tinggal di asrama
scene('C25', 'Meimei mengajak Dawen ke pesta ulang tahun Annie hari Sabtu. Dawen sudah janji menonton film sore itu, '
             'jadi mereka mengatur jadwal, lalu berencana membeli hadiah bersama.')
ganti('C25', '大文，星期六安妮家有生日派對，我們一起去，好不好？', '大文，星期六是安妮的生日，晚上有生日派對，我們一起去，好不好？',
      'Dawen, Sabtu ulang tahun Annie, malamnya ada pesta, kita pergi bareng, mau?')
# C27 — diskusi untuk laporan BERIKUTNYA (laporan lama sudah dinilai)
ganti('C27', '大文，昨天下午你為什麼沒來？我們要談報告的事。', '大文，昨天下午你為什麼沒來？我們要談下一個報告的事。',
      'Dawen, kemarin sore kenapa kamu tidak datang? Kita mau membahas laporan berikutnya.')
# C29 — kata inti 藥局 dipakai di dialog
ganti('C29', '我的感冒還沒好……', '我的感冒還沒好……藥房的藥我也吃完了。', 'Fluku belum sembuh… obat dari apotek juga sudah habis.')
ganti('C29', '學校旁邊有一家藥房，現在應該還開著，我陪你去吧！', '學校旁邊有一家藥局，現在應該還開著，我陪你去吧！',
      'Di sebelah kampus ada apotek, sekarang mestinya masih buka, aku temani kamu ke sana!')
# C30 — Dawen suka olahraga (A06, B01); V一V (C44) dihindari
ganti('C30', '你要多動一動，身體才會好。走，我們去公園散步！', '你要多動，身體才會好。走，我們去公園散步！',
      'Kamu harus banyak bergerak, baru badanmu sehat. Ayo, kita jalan-jalan ke taman!')
ganti('C30', '你以前說運動很無聊！', '你以前說你很忙，沒有時間運動！', 'Dulu kamu bilang kamu sibuk, tidak ada waktu olahraga!')
# C31 — kalimat judul ada di dialog
ganti('C31', '大文，你不是說今天要早點來嗎？現在八點半了！', '大文，你不是說八點上課嗎？現在八點半了！',
      'Dawen, bukannya kamu bilang kuliahnya jam delapan? Sekarang sudah jam setengah sembilan!')
# C32 — dua baris berturut Meimei digabung
hapus('C32', '寒假跟我去臺南玩，好不好？')
ganti('C32', '有時候在家看書，有時候跟朋友出去玩。', '有時候在家看書，有時候跟朋友出去玩。寒假跟我去臺南玩，好不好？',
      'Kadang membaca di rumah, kadang main keluar dengan teman. Liburan musim dingin ikut aku ke Tainan, mau?')
# C33 — 陳 terlalu banyak → 林教授
for zh, idn in [('對。陳教授說我的中文程度很高，我希望得到他的幫助。', 'Iya. Profesor Lin bilang tingkat Mandarinku tinggi, aku berharap mendapat bantuannya.'),
                ('陳教授的辦公室就在那邊，你現在去問他吧！', 'Kantor Profesor Lin ada di sana, tanya dia sekarang saja!')]:
    ganti('C33', zh, zh.replace('陳教授', '林教授'), idn)
scene('C33', B['C33'][0].replace('profesornya', 'Profesor Lin'))
# C34 — dua baris berturut guru digabung
hapus('C34', '你也可以去上書法課，寫書法對學漢字很有幫助。')
ganti('C34', '不行，拼音只能幫你念。不會的字，你可以查字典，試試看。', '不行，拼音只能幫你念。不會的字，你可以查字典，試試看。你也可以去上書法課，寫書法對學漢字很有幫助。',
      'Tidak bisa, pinyin hanya membantu membaca. Huruf yang belum kamu tahu, coba cari di kamus. Kamu juga bisa ikut kelas kaligrafi, menulis kaligrafi sangat membantu belajar Hanzi.')
# C38 — 一切 dipakai secara wajar
ganti('C38', '不包括，一切都是學生說的。', '不包括，都是學生說的。', 'Tidak termasuk, ini semua jawaban mahasiswa.')
sisip('C38', '對……從今天起，我要早點睡覺！', '陳老師', '很好！大家要記得，健康比一切都重要。', 'Bagus! Semuanya ingat ya, kesehatan lebih penting dari segalanya.')
# C40 — kata inti 打折 dipakai
ganti('C40', '大文，百貨公司今天週年慶，衣服都打八折！', '大文，百貨公司今天週年慶，衣服都打折，打八折！',
      'Dawen, hari ini mal merayakan ulang tahunnya, semua baju diskon, diskon dua puluh persen!')
# C41 — bukan musim dingin pertama (B18–B20)
scene('C41', 'Musim dingin datang lagi dan pakaian musim dingin Dawen sudah usang. Meimei membantunya membeli pakaian '
             'hangat: sweter, sarung tangan, kaus kaki, sepatu, sandal, dan piyama.')
# C43 — kata inti 主人 dipakai dengan benar (pemilik hewan), bukan 'pemilik toko'
ganti('C43', '老闆娘，您是這個店的主人嗎？', '老闆娘，這隻小貓好可愛！它的主人是您嗎？', 'Bu, kucing kecil ini lucu sekali! Ibu pemiliknya?')
sisip('C43', '老闆娘，這隻小貓好可愛！它的主人是您嗎？', '老闆娘', '對！它每天都跟我一起做生意。', 'Iya! Setiap hari dia ikut berjualan bersama saya.')
sisip('C43', '對！它每天都跟我一起做生意。', '李美美', '您在這裡做生意多久了？', 'Ibu sudah berapa lama berjualan di sini?')
ganti('C43', '對。我在這裡做了二十年的生意了。', '我在這裡做了二十年的生意了。', 'Saya sudah berjualan di sini dua puluh tahun.')
# C44 — C41 membeli sweter hitam → terlalu gelap; kolokasi 買不慣 & 換了換 diperbaiki; di rumah (bukan asrama)
scene('C44', 'Sweter yang Dawen beli kemarin kekecilan. Ia menukarnya di toko, memilih warna yang sedang tren, lalu di '
             'rumah Zhiming memuji sweter barunya.')
ganti('C44', '對。這個顏色太淺了，有沒有深一點的？', '對。這個顏色太深了，有沒有淺一點的？', 'Iya. Warnanya terlalu gelap, ada yang lebih terang?')
ganti('C44', '有，這件深藍色的現在很流行。你試穿看看吧。', '有，這件淺藍色的現在很流行。你試穿看看吧。', 'Ada, yang biru muda ini sedang tren. Coba dipakai.')
ganti('C44', '住慣了。可是我還買不慣這裡的衣服，大小常常買錯。', '住慣了，也吃慣了。可是這裡衣服的大小，我還不習慣，常常買錯。',
      'Sudah terbiasa tinggal, juga sudah terbiasa makanannya. Tapi ukuran baju di sini aku belum terbiasa, sering salah beli.')
ganti('C44', '昨天買的太小了，今天我去換了換，顏色也換了。', '昨天買的太小了，今天我去換了，顏色也換了。', 'Yang kemarin kekecilan, hari ini kutukar, warnanya juga kuganti.')
ganti('C44', '深藍色很適合你，現在很流行。', '淺藍色很適合你，現在很流行。', 'Biru muda cocok sekali untukmu, sedang tren sekarang.')
# C54 — 美麗 terlalu formal untuk seruan; tetap dipakai sebagai kata sifat atributif
ganti('C54', '好美麗！月亮也很大。', '好美！月亮也很大。', 'Indah sekali! Bulannya juga besar.')
ganti('C54', '那我們每個季節都來吧！', '美麗的花、美麗的山……那我們每個季節都來吧！', 'Bunga yang indah, gunung yang indah… kalau begitu kita datang setiap musim ya!')
# C55 — tanpa stereotip negatif; 自由 dipakai sebagai candaan
ganti('C55', '在印尼，很多人很自由地丟垃圾……', '在印尼，很多地方的垃圾都放在一起。', 'Di Indonesia, di banyak tempat sampahnya dicampur jadi satu.')
sisip('C55', '在臺灣不行，連一個小瓶子都要放對地方。', '王大文', '在臺灣丟垃圾，真不自由！', 'Buang sampah di Taiwan, sungguh tidak bebas!')
sisip('C55', '在臺灣丟垃圾，真不自由！', '李美美', '可是環境很乾淨啊！', 'Tapi lingkungannya bersih, kan!')
# C56 — makan malam Imlek = makan bersama; Dawen sudah pernah ikut Imlek di rumah Meimei (B44)
scene('C56', 'Dawen mengenang Tahun Baru Imlek tahun lalu di rumah Meimei. Meimei menjelaskan tradisi malam Imlek: '
             'hidangan khas dan siapa yang datang duluan harus membantu memasak. Dawen bercerita tentang perayaan di '
             'Indonesia, lalu Meimei mengundangnya lagi.')
ganti('C56', '美美，春節是臺灣最重要的節日嗎？', '美美，去年在你家過年很好玩！春節是臺灣最重要的節日嗎？',
      'Meimei, Imlek tahun lalu di rumahmu seru sekali! Imlek itu hari raya terpenting di Taiwan?')
ganti('C56', '你們吃什麼？', '去年你們吃了很多菜，都是什麼菜？', 'Tahun lalu kalian makan banyak hidangan, apa saja?')
ganti('C56', '誰先吃？', '去年我到的時候，菜都做好了。', 'Tahun lalu waktu aku sampai, masakannya sudah siap semua.')
ganti('C56', '我們家誰先到，誰就先吃！', '對，我們家誰先到，誰就先幫忙做菜！', 'Iya, di keluarga kami siapa yang datang duluan, dia yang duluan membantu memasak!')
ganti('C56', '今年除夕，你也來我家吧！', '今年除夕，你早一點來我家吧！', 'Malam Imlek tahun ini, datang lebih awal ke rumahku ya!')
# C59 — usulan lanjut setelah pendapat Meimei
ganti('C59', '那麼，你有什麼建議？', '那麼，環保要寫什麼？你有什麼建議？', 'Kalau begitu, soal lingkungan mau menulis apa? Kamu ada saran?')


# ---- tulis ulang cerita_vol3.py (67 bab) & kosongkan pilot di dialog_cerita.py ----
def q(s):
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"


out = ['"""Data 情境對話 berbasis cerita Vol.3/A2 (dipakai oleh dialog_cerita.py).', '',
       'Format sama dengan BARU di dialog_cerita.py: kode → (scene Indonesia, [(tempat, judul Indonesia, [(pembicara, zh, id)])]).',
       'Berisi ke-67 bab (pilot C24 C30 C44 C61 C63 C64 dipindah dari dialog_cerita.py pada revisi 2026-11-04).',
       'Revisi 2026-11-04 (laporan review Carli): lihat _kerja/revisi_vol3.py.', '"""', '', 'BARU = {']
for code in sorted(B):
    sc, dialogs = B[code]
    out.append(f'    {q(code)}: ({q(sc)}, [')
    for place, tid, lines in dialogs:
        out.append(f'        ({q(place)}, {q(tid)}, [')
        for sp, zh, idn in lines:
            out.append(f'            ({q(sp)}, {q(zh)}, {q(idn)}),')
        out.append('        ]),')
    out.append('    ]),')
out.append('}')
open(os.path.join(K, 'cerita_vol3.py'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')

p = os.path.join(K, 'dialog_cerita.py')
s = open(p, encoding='utf-8').read()
a = s.index('\nBARU = {\n') + 1
z = s.index('\n}\n', a) + 3
if "'C24'" in s[a:z]:
    s = s[:a] + 'BARU = {}   # pilot Vol.3 (C24 C30 C44 C61 C63 C64) dipindah ke cerita_vol3.py (2026-11-04)\n' + s[z:]
    open(p, 'w', encoding='utf-8').write(s)
print('cerita_vol3.py ditulis ulang:', len(B), 'bab')
