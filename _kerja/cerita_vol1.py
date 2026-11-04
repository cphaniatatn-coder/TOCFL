"""Data 情境對話 Vol.1/A0 (dipakai oleh dialog_cerita.py). Format sama dengan BARU di dialog_cerita.py.

Riwayat:
- 2026-10-26: 13 bab ditulis ulang berbasis cerita (A09 A10 A13 A16–A25); dialog hasil edit Carli tidak disentuh.
- 2026-11-04 (pilot revisi): SEMUA 25 bab di sini, mengikuti laporan Carli 《TOCFL 模組 Vol.1–3 對話審查報告》
  + koreksi level TBCL. Tokoh tetap: keluarga Dawen di Indonesia, 5 orang (ayah, ibu, 哥哥, 姊姊 = 王小文, Dawen;
  TANPA adik); keluarga Meimei di 臺中, 4 orang (ayah, ibu, adik 小明, Meimei; TANPA kakak); Meimei orang Taiwan
  (penutur asli, teman sekelas Dawen); Dawen di A08/A09 tinggal di kamar asrama (B07 pindah ke apartemen);
  Meimei suka olahraga tapi tidak suka main bola, makan daging, suka film.
- Di A0 TIDAK dipakai: 了 (kecuali ungkapan tetap 感冒了/生病了/下雨了 + catatan 💡), 太…了, V得, 會 'akan',
  好嗎, 是…的, 在+tempat+V, 一下, 才/就 'baru/sudah' sebelum babnya; 吧 mulai A11, 也 mulai A06.
  Kata fungsi L1 yang polanya baru diajarkan di L2/L3 diberi catatan 💡 di _kerja/catatan_kata.json.
"""

BARU = {
    'A01': ('Hari pertama kuliah di Taipei. Dawen, mahasiswa asing yang belajar bahasa Mandarin, berkenalan dengan '
            'Meimei, teman sekelasnya yang orang Taiwan, lalu dengan Pak Chen di kantor kampus.', [
        ('早上，在教室', 'Pagi hari, di kelas', [
            ('王大文', '早安！', 'Selamat pagi!'),
            ('李美美', '早安！', 'Selamat pagi!'),
            ('王大文', '你好！我姓王，我叫王大文。你叫什麼名字？', 'Halo! Marga saya Wang, nama saya Wang Dawen. Siapa namamu?'),
            ('李美美', '我姓李，我是李美美。', 'Marga saya Li, saya Li Meimei.'),
            ('王大文', '美美，你好！', 'Halo, Meimei!'),
        ]),
        ('在辦公室', 'Di kantor kampus', [
            ('王大文', '先生，您好！您貴姓？', 'Halo, Pak! Boleh tahu marga Bapak?'),
            ('陳先生', '我姓陳。你叫什麼名字？', 'Marga saya Chen. Siapa namamu?'),
            ('王大文', '我叫王大文。', 'Nama saya Wang Dawen.'),
            ('陳先生', '王大文，再見！', 'Sampai jumpa, Wang Dawen!'),
            ('王大文', '謝謝您！陳先生，再見！', 'Terima kasih, Pak! Sampai jumpa, Pak Chen!'),
        ]),
    ]),
    'A02': ('Istirahat di sela kuliah. Meimei bertanya asal negara Dawen, lalu di luar kelas Dawen menyapa '
            'mahasiswa asing yang belum ia kenal dan bertanya asal negaranya.', [
        ('在教室', 'Di kelas', [
            ('李美美', '大文，你是哪國人？', 'Dawen, kamu orang mana?'),
            ('王大文', '我是印尼人。你是臺灣人嗎？', 'Aku orang Indonesia. Kamu orang Taiwan?'),
            ('李美美', '是，我是臺灣人。你會說中文嗎？', 'Iya, aku orang Taiwan. Kamu bisa berbahasa Mandarin?'),
            ('王大文', '我會說中文。', 'Aku bisa berbahasa Mandarin.'),
        ]),
        ('在教室外面', 'Di luar kelas', [
            ('王大文', '美美，他是外國人嗎？', 'Meimei, dia orang asing?'),
            ('李美美', '是的。', 'Iya.'),
            ('王大文', '你好！請問，你是哪國人？', 'Halo! Permisi, kamu orang mana?'),
            ('美國學生', '你好！我是美國人。', 'Halo! Aku orang Amerika.'),
            ('王大文', '她呢？她是哪國人？', 'Kalau dia (perempuan)? Dia orang mana?'),
            ('美國學生', '她是日本人。她說日語、英文和中文。', 'Dia orang Jepang. Dia berbahasa Jepang, Inggris, dan Mandarin.'),
        ]),
    ]),
    'A03': ('Meimei melihat foto keluarga di ponsel Dawen. Mereka saling menunjuk foto dan bertanya siapa orang di '
            'dalamnya.', [
        ('大文的家人', 'Keluarga Dawen', [
            ('李美美', '大文，這是誰？', 'Dawen, ini siapa?'),
            ('王大文', '這是我爸爸。', 'Ini ayahku.'),
            ('李美美', '這是你媽媽嗎？', 'Ini ibumu?'),
            ('王大文', '是的。這是我哥哥。', 'Iya. Ini kakak laki-lakiku.'),
            ('李美美', '那是誰？你妹妹嗎？', 'Itu siapa? Adik perempuanmu?'),
            ('王大文', '她是我姊姊，她叫王小文。', 'Dia kakak perempuanku, namanya Wang Xiaowen.'),
            ('李美美', '你的家人是印尼人嗎？', 'Keluargamu orang Indonesia?'),
            ('王大文', '是，我們是印尼人。', 'Iya, kami orang Indonesia.'),
        ]),
        ('美美的家人', 'Keluarga Meimei', [
            ('王大文', '美美，這是你的家人嗎？', 'Meimei, ini keluargamu?'),
            ('李美美', '這是我爸爸、媽媽，還有我弟弟。', 'Ini ayah dan ibuku, dan juga adik laki-lakiku.'),
            ('王大文', '你弟弟叫什麼名字？', 'Siapa nama adikmu?'),
            ('李美美', '他叫李小明。', 'Namanya Li Xiaoming.'),
        ]),
    ]),
    'A04': ('Lanjutan obrolan foto keluarga: Dawen dan Meimei menghitung anggota keluarga, lalu bertanya kepada '
            'Pak Chen tentang anak-anaknya.', [
        ('在教室', 'Di kelas', [
            ('李美美', '大文，你家有幾個人？', 'Dawen, keluargamu ada berapa orang?'),
            ('王大文', '一，二，三，四，五！我家有五個人：爸爸、媽媽、哥哥、姊姊，和我。',
             'Satu, dua, tiga, empat, lima! Keluargaku lima orang: ayah, ibu, kakak laki-laki, kakak perempuan, dan aku.'),
            ('李美美', '你有弟弟嗎？', 'Kamu punya adik laki-laki?'),
            ('王大文', '我沒有弟弟。你家有幾個人？', 'Aku tidak punya adik laki-laki. Keluargamu berapa orang?'),
            ('李美美', '我家有四個人。我有一個弟弟。', 'Keluargaku empat orang. Aku punya satu adik laki-laki.'),
        ]),
        ('在辦公室', 'Di kantor kampus', [
            ('王大文', '陳先生，您有孩子嗎？', 'Pak Chen, Bapak punya anak?'),
            ('陳先生', '有，我有三個孩子，兩個兒子，一個女兒。', 'Ada, saya punya tiga anak: dua putra, satu putri.'),
            ('王大文', '您太太是臺灣人嗎？', 'Istri Bapak orang Taiwan?'),
            ('陳先生', '是，她是臺灣人。', 'Iya, dia orang Taiwan.'),
        ]),
    ]),
    'A05': ('Ulang tahun Dawen di kelas. Meimei memberi ucapan, mereka saling menanyakan umur dan tanggal lahir, '
            'lalu membicarakan ayah Meimei.', [
        ('在教室，大文的生日', 'Di kelas, ulang tahun Dawen', [
            ('李美美', '大文，生日快樂！', 'Dawen, selamat ulang tahun!'),
            ('王大文', '謝謝！', 'Terima kasih!'),
            ('李美美', '你今年幾歲？', 'Tahun ini umurmu berapa?'),
            ('王大文', '我今年二十歲。你呢？', 'Tahun ini aku dua puluh tahun. Kamu?'),
            ('李美美', '我十九歲。', 'Aku sembilan belas tahun.'),
            ('王大文', '你的生日是幾月幾號？', 'Ulang tahunmu tanggal berapa bulan apa?'),
            ('李美美', '我的生日是十一月九號。', 'Ulang tahunku tanggal 9 November.'),
        ]),
        ('說美美的家人', 'Membicarakan keluarga Meimei', [
            ('王大文', '美美，你爸爸今年多大？', 'Meimei, ayahmu tahun ini umurnya berapa?'),
            ('李美美', '他五十歲。', 'Dia lima puluh tahun.'),
            ('王大文', '你爸爸的生日是幾月幾號？', 'Ulang tahun ayahmu tanggal berapa?'),
            ('李美美', '一月一號。明年一月一號，他五十一歲。', '1 Januari. Tanggal 1 Januari tahun depan, umurnya 51 tahun.'),
        ]),
    ]),
    'A06': ('Sepulang kuliah Dawen dan Meimei saling bercerita tentang hobi dan rencana akhir pekan. Ternyata '
            'keduanya suka olahraga dan suka menonton film.', [
        ('下課以後', 'Sepulang kelas', [
            ('李美美', '大文，你喜歡運動嗎？', 'Dawen, kamu suka olahraga?'),
            ('王大文', '喜歡！我喜歡打球。你呢？', 'Suka! Aku suka main bola. Kamu?'),
            ('李美美', '我也喜歡運動，我不喜歡打球。', 'Aku juga suka olahraga, (tapi) aku tidak suka main bola.'),
            ('王大文', '那你喜歡做什麼？', 'Lalu kamu suka melakukan apa?'),
            ('李美美', '我愛看電影和聽音樂，也喜歡唱歌和跳舞。', 'Aku suka sekali nonton film dan mendengarkan musik, juga suka bernyanyi dan menari.'),
            ('王大文', '我不唱歌，也不跳舞。我喜歡聽歌。', 'Aku tidak menyanyi, juga tidak menari. Aku suka mendengarkan lagu.'),
        ]),
        ('說週末', 'Membicarakan akhir pekan', [
            ('王大文', '美美，你週末想要做什麼？', 'Meimei, akhir pekan kamu mau melakukan apa?'),
            ('李美美', '我週末想要看電影。你呢？', 'Akhir pekan aku mau nonton film. Kamu?'),
            ('王大文', '我想要運動，也想要看電影！', 'Aku mau olahraga, juga mau nonton film!'),
        ]),
    ]),
    'A07': ('Dawen dan Meimei melihat foto keluarga masing-masing dan saling mendeskripsikan penampilan orang: '
            'tinggi, pendek, kurus, gemuk, dan mirip siapa.', [
        ('美美的家人', 'Keluarga Meimei', [
            ('王大文', '美美，這是誰？她很漂亮！', 'Meimei, ini siapa? Dia cantik!'),
            ('李美美', '她是我媽媽。', 'Dia ibuku.'),
            ('王大文', '你媽媽高不高？', 'Ibumu tinggi atau tidak?'),
            ('李美美', '她很高。我弟弟像我媽媽，也很高。', 'Dia tinggi. Adikku mirip ibuku, juga tinggi.'),
            ('王大文', '你像不像你媽媽？', 'Kamu mirip ibumu atau tidak?'),
            ('李美美', '不像，我像我爸爸。我很矮。', 'Tidak, aku mirip ayahku. Aku pendek.'),
        ]),
        ('大文的家人', 'Keluarga Dawen', [
            ('李美美', '這個人是你哥哥嗎？他真高！', 'Orang ini kakakmu? Tinggi sekali!'),
            ('王大文', '是，他很高，也很瘦。', 'Iya, dia tinggi, juga kurus.'),
            ('李美美', '你們一樣高嗎？', 'Kalian sama tinggi?'),
            ('王大文', '不一樣。我哥哥很高，我很矮，也很胖！', 'Tidak sama. Kakakku tinggi, aku pendek, juga gemuk!'),
        ]),
    ]),
    'A08': ('Di kelas Dawen dan Meimei bertukar informasi tempat tinggal. Sepulang kuliah Meimei mampir ke kamar '
            'asrama Dawen.', [
        ('在教室', 'Di kelas', [
            ('李美美', '大文，你住在哪裡？', 'Dawen, kamu tinggal di mana?'),
            ('王大文', '我住在臺北。你家在哪裡？', 'Aku tinggal di Taipei. Rumahmu di mana?'),
            ('李美美', '我家在臺中，我住在臺北。', 'Rumah keluargaku di Taichung, aku tinggal di Taipei.'),
            ('王大文', '你住幾樓？', 'Kamu tinggal di lantai berapa?'),
            ('李美美', '我住五樓，房子裡面有兩個房間。你呢？', 'Lantai lima, di dalam rumahnya ada dua kamar. Kamu?'),
            ('王大文', '我住八樓。', 'Lantai delapan.'),
        ]),
        ('在大文的房間門口', 'Di depan kamar Dawen (asrama)', [
            ('李美美', '大文！我在門口。', 'Dawen! Aku di depan pintu.'),
            ('王大文', '好，我去開門。……請進！', 'Oke, aku bukakan pintunya. …Silakan masuk!'),
            ('李美美', '你的房間很漂亮！附近有公園嗎？', 'Kamarmu bagus! Di dekat sini ada taman?'),
            ('王大文', '有，附近有一個公園。', 'Ada, di dekat sini ada sebuah taman.'),
            ('李美美', '你的家人也住在臺北嗎？', 'Keluargamu juga tinggal di Taipei?'),
            ('王大文', '不，他們住在印尼。', 'Tidak, mereka tinggal di Indonesia.'),
        ]),
    ]),
    'A09': ('Adik Meimei, Xiaoming, sedang berkunjung ke Taipei. Meimei mengajaknya ke kamar asrama Dawen untuk '
            'menonton film, lalu Xiaoming bersembunyi dan mereka mencarinya.', [
        ('在大文的房間', 'Di kamar Dawen', [
            ('李美美', '大文，桌子上有電視！你喜歡看電影嗎？', 'Dawen, di atas meja ada televisi! Kamu suka nonton film?'),
            ('王大文', '喜歡！我們看電影！你拿椅子。', 'Suka! Ayo kita nonton film! Kamu ambil kursi.'),
            ('李美美', '好。椅子在哪裡？', 'Oke. Kursinya di mana?'),
            ('王大文', '在床旁邊。你弟弟也喜歡看電影嗎？', 'Di samping tempat tidur. Adikmu juga suka nonton film?'),
            ('李美美', '喜歡。小明！小明！……他在哪裡？', 'Suka. Xiaoming! Xiaoming! …Dia di mana?'),
        ]),
        ('小明在哪裡？', 'Xiaoming di mana?', [
            ('王大文', '他在電視前面嗎？', 'Dia di depan televisi?'),
            ('李美美', '不在。在床下嗎？……也不在床下。', 'Tidak ada. Di bawah tempat tidur? …Di bawah tempat tidur juga tidak ada.'),
            ('王大文', '在門後嗎？', 'Di belakang pintu?'),
            ('李美美', '不在門後。', 'Tidak ada di belakang pintu.'),
            ('王大文', '你看，桌子下有一個人！', 'Lihat, di bawah meja ada orang!'),
            ('李美美', '小明！你在桌子下！', 'Xiaoming! Kamu di bawah meja!'),
            ('王大文', '你弟弟很喜歡玩！', 'Adikmu suka sekali bermain!'),
        ]),
    ]),
    'A10': ('Dawen datang terlambat dan mengantuk karena setiap hari tidur jam dua pagi. Meimei mengajaknya '
            'berolahraga pagi, dan keesokan paginya Dawen benar-benar datang ke taman.', [
        ('早上，在教室', 'Pagi hari, di kelas', [
            ('李美美', '大文，你好晚！現在九點二十分。', 'Dawen, kamu telat sekali! Sekarang jam sembilan lewat dua puluh.'),
            ('王大文', '我八點半起床。', 'Aku bangun jam setengah sembilan.'),
            ('李美美', '你每天晚上幾點睡覺？', 'Setiap malam kamu tidur jam berapa?'),
            ('王大文', '兩點。我晚上喜歡看電影。', 'Jam dua. Malam hari aku suka nonton film.'),
            ('李美美', '兩點？很晚！我每天晚上十一點睡覺，早上六點半起床。', 'Jam dua? Malam sekali! Setiap malam aku tidur jam sebelas, bangun jam setengah tujuh pagi.'),
            ('王大文', '你好早！你早上做什麼？', 'Pagi sekali! Pagi-pagi kamu ngapain?'),
            ('李美美', '我早上去公園運動。大文，你也去！', 'Pagi hari aku olahraga ke taman. Dawen, kamu juga ikut!'),
            ('王大文', '好！', 'Oke!'),
        ]),
        ('早上六點半，在公園', 'Jam setengah tujuh pagi, di taman', [
            ('李美美', '大文！你好早！', 'Dawen! Pagi sekali kamu!'),
            ('王大文', '我六點起床！', 'Aku bangun jam enam!'),
            ('李美美', '很好！現在我們去運動！', 'Bagus sekali! Sekarang ayo kita olahraga!'),
            ('王大文', '……美美，現在幾點？我想睡覺！', '…Meimei, sekarang jam berapa? Aku ngantuk!'),
            ('李美美', '現在六點四十分！晚上不看電影，十一點睡覺！', 'Sekarang jam enam lewat empat puluh! Nanti malam jangan nonton film, tidur jam sebelas!'),
        ]),
    ]),
    'A11': ('Hari Jumat sepulang kuliah Dawen mengajak Meimei menonton film hari Sabtu. Setelah menonton, mereka '
            'berjanji berolahraga bersama di taman hari Minggu.', [
        ('星期五，在教室', 'Jumat, di kelas', [
            ('王大文', '美美，今天星期幾？', 'Meimei, hari ini hari apa?'),
            ('李美美', '今天星期五。', 'Hari ini Jumat.'),
            ('王大文', '明天星期六，我們一起去看電影吧！', 'Besok Sabtu, kita nonton film bareng yuk!'),
            ('李美美', '好！明天幾點？', 'Oke! Besok jam berapa?'),
            ('王大文', '下午兩點。', 'Jam dua siang.'),
            ('李美美', '好。你想看什麼電影？', 'Oke. Kamu mau nonton film apa?'),
            ('王大文', '我想看美國電影。', 'Aku mau nonton film Amerika.'),
        ]),
        ('星期六，看電影以後', 'Sabtu, setelah nonton', [
            ('李美美', '大文，你常常去公園嗎？', 'Dawen, kamu sering ke taman?'),
            ('王大文', '常常去。我星期一和星期五早上去公園運動，昨天早上我也去。',
             'Sering. Senin dan Jumat pagi aku olahraga ke taman, kemarin pagi aku juga pergi.'),
            ('李美美', '明天是星期天，我們一起去吧！', 'Besok hari Minggu, kita pergi bareng yuk!'),
            ('王大文', '好喔，我們一起去！', 'Oke deh, ayo kita pergi bareng!'),
        ]),
    ]),
    'A12': ('Awal semester. Meimei memperkenalkan Dawen kepada guru mereka, lalu mereka membicarakan jadwal kuliah '
            'dan ruang kelas.', [
        ('在教室門口', 'Di depan pintu kelas', [
            ('李美美', '大文，這是我們的老師，陳老師。', 'Dawen, ini guru kita, Bu Chen.'),
            ('王大文', '陳老師好！我叫王大文，我是印尼學生。', 'Selamat pagi, Bu Chen! Saya Wang Dawen, mahasiswa dari Indonesia.'),
            ('陳老師', '你好！你是哪個大學的學生？', 'Halo! Kamu mahasiswa universitas mana?'),
            ('王大文', '我是臺北大學的學生，美美是我的同學。', 'Saya mahasiswa Universitas Taipei, Meimei teman sekelas saya.'),
            ('陳老師', '你學什麼？', 'Kamu belajar apa?'),
            ('王大文', '我學中文。', 'Saya belajar bahasa Mandarin.'),
        ]),
        ('下課以後', 'Sepulang kelas', [
            ('王大文', '美美，我們幾點上課？', 'Meimei, kita masuk kelas jam berapa?'),
            ('李美美', '早上九點上課，十二點下課。', 'Masuk jam sembilan pagi, selesai jam dua belas.'),
            ('王大文', '陳老師教什麼課？', 'Bu Chen mengajar kelas apa?'),
            ('李美美', '她教中文課。她很忙，她晚上也工作。', 'Dia mengajar kelas bahasa Mandarin. Dia sibuk, malam juga bekerja.'),
            ('王大文', '我們的教室在哪裡？', 'Ruang kelas kita di mana?'),
            ('李美美', '教室在三樓。學校的功課很多，我每天晚上寫功課。', 'Di lantai tiga. Tugas kuliahnya banyak, setiap malam aku mengerjakan PR.'),
        ]),
    ]),
    'A13': ('Dawen tidak mengerti sebuah kalimat di buku. Meimei, yang orang Taiwan, mengerti kalimatnya tetapi '
            'tidak bisa menjelaskannya dalam bahasa Inggris, jadi mereka bertanya kepada Guru Chen.', [
        ('下課的時候', 'Saat istirahat', [
            ('王大文', '美美，這個句子是什麼意思？', 'Meimei, kalimat ini artinya apa?'),
            ('李美美', '我看……這個句子，我不會用英文說。', 'Coba kulihat… kalimat ini, aku tidak bisa menjelaskannya dalam bahasa Inggris.'),
            ('王大文', '我們問老師吧。', 'Kita tanya guru saja.'),
            ('李美美', '好。你有筆和紙嗎？', 'Oke. Kamu punya pena dan kertas?'),
            ('王大文', '有，我有兩枝筆。你用這枝。', 'Ada, aku punya dua pena. Kamu pakai yang ini.'),
        ]),
        ('問老師', 'Bertanya kepada guru', [
            ('王大文', '老師，我們有問題。這個字是什麼意思？', 'Bu, kami punya pertanyaan. Huruf ini artinya apa?'),
            ('陳老師', '這是「書」。你看，這是一本書。', 'Ini "書". Lihat, ini sebuah buku.'),
            ('王大文', '喔，書！這個字怎麼寫？', 'Oh, buku! Huruf ini ditulis bagaimana?'),
            ('陳老師', '你們看這張紙，我寫。', 'Lihat kertas ini, saya tuliskan.'),
            ('王大文', '我懂！謝謝老師！', 'Saya mengerti! Terima kasih, Bu!'),
            ('陳老師', '有問題，再問我。', 'Kalau ada pertanyaan, tanya saya lagi.'),
        ]),
    ]),
    'A14': ('Sehari sebelum ujian Mandarin. Dawen cemas; Meimei menenangkannya dan membantu memeriksa kalimatnya.', [
        ('考試的前一天', 'Sehari sebelum ujian', [
            ('李美美', '大文，明天考試，你怕不怕？', 'Dawen, besok ujian, kamu takut tidak?'),
            ('王大文', '我很怕！中文考試非常難。', 'Takut sekali! Ujian Mandarin susah banget.'),
            ('李美美', '我覺得說中文很容易，寫字很難。', 'Menurutku berbicara bahasa Mandarin mudah, menulis karakternya yang susah.'),
            ('王大文', '對！今天我得寫很多字！你會寫這個字嗎？', 'Betul! Hari ini aku harus menulis banyak karakter! Kamu bisa menulis karakter ini?'),
            ('李美美', '會！你看，我寫。', 'Bisa! Lihat, kutuliskan.'),
        ]),
        ('在教室', 'Di kelas', [
            ('王大文', '美美，這個句子對不對？', 'Meimei, kalimat ini benar tidak?'),
            ('李美美', '不對，這是錯字。', 'Salah, ini karakter yang keliru.'),
            ('王大文', '我可以問老師嗎？', 'Aku boleh tanya guru?'),
            ('李美美', '可以。明天考試，你應該問老師。', 'Boleh. Besok ujian, sebaiknya kamu tanya guru.'),
            ('王大文', '對！明天我一定可以！', 'Betul! Besok aku pasti bisa!'),
        ]),
    ]),
    'A15': ('Dawen dan Meimei memesan minuman di kedai kopi dekat kampus: memilih minuman, es, susu, dan tingkat '
            'manis.', [
        ('在咖啡店', 'Di kedai kopi', [
            ('店員', '您好！您要喝什麼？', 'Halo! Mau minum apa?'),
            ('王大文', '我要一杯咖啡。', 'Saya mau secangkir kopi.'),
            ('店員', '咖啡要冰嗎？', 'Kopinya pakai es?'),
            ('王大文', '要冰。要一點牛奶，別太甜。', 'Pakai es. Tambah sedikit susu, jangan terlalu manis.'),
            ('店員', '小姐，您要喝茶還是咖啡？', 'Mbak, mau minum teh atau kopi?'),
            ('李美美', '我要一杯茶，少一點冰。', 'Saya mau segelas teh, esnya sedikit saja.'),
        ]),
        ('喝咖啡的時候', 'Sambil minum kopi', [
            ('王大文', '美美，你喝酒嗎？', 'Meimei, kamu minum alkohol?'),
            ('李美美', '我不喝酒。我每天喝牛奶。', 'Aku tidak minum alkohol. Setiap hari aku minum susu.'),
            ('王大文', '我每天喝兩杯咖啡！', 'Aku minum dua cangkir kopi sehari!'),
        ]),
    ]),
    'A16': ('Jam dua belas siang Dawen lapar sekali karena tidak pernah sarapan. Mereka makan siang bersama, dan '
            'Dawen makan begitu banyak sampai tidak mau makan malam.', [
        ('中午十二點', 'Jam dua belas siang', [
            ('王大文', '美美，我很餓！我們去吃飯吧！', 'Meimei, aku lapar sekali! Ayo kita makan!'),
            ('李美美', '好！你不吃早餐嗎？', 'Oke! Kamu tidak sarapan?'),
            ('王大文', '我早上不餓，我不吃早餐。', 'Pagi hari aku tidak lapar, aku tidak sarapan.'),
            ('李美美', '你應該吃早餐！我每天早上吃蛋，喝牛奶。', 'Kamu harus sarapan! Setiap pagi aku makan telur dan minum susu.'),
        ]),
        ('吃午餐', 'Makan siang', [
            ('李美美', '午餐你想吃什麼？', 'Makan siang kamu mau makan apa?'),
            ('王大文', '我想吃雞肉和飯。你呢？', 'Aku mau makan daging ayam dan nasi. Kamu?'),
            ('李美美', '我今天不想吃肉，我吃菜，也喝湯。', 'Hari ini aku tidak ingin makan daging, aku makan sayur, juga minum sup.'),
            ('王大文', '這裡的雞肉很好吃！……我很飽！晚餐我不吃！', 'Daging ayam di sini enak sekali! …Aku kenyang sekali! Makan malam aku tidak makan!'),
            ('李美美', '不吃晚餐？晚上你一定很餓！', 'Tidak makan malam? Malam nanti kamu pasti lapar sekali!'),
        ]),
    ]),
    'A17': ('Dawen dan Meimei makan siang di warung mi: memesan mi dan bakpao, meminta sumpit, lalu Meimei '
            'mengajari cara makan mi daging sapi.', [
        ('在麵店', 'Di warung mi', [
            ('老闆', '你好！幾位？', 'Halo! Berapa orang?'),
            ('王大文', '兩位。', 'Dua orang.'),
            ('老闆', '請進。要吃什麼？', 'Silakan masuk. Mau makan apa?'),
            ('王大文', '我要一碗牛肉麵。', 'Saya mau semangkuk mi daging sapi.'),
            ('李美美', '我要一碗湯麵和兩個包子。', 'Saya mau semangkuk mi kuah dan dua bakpao.'),
            ('王大文', '先生，我們沒有筷子。', 'Pak, kami tidak punya sumpit.'),
            ('老闆', '好，筷子在這裡。', 'Baik, sumpitnya di sini.'),
        ]),
        ('吃麵的時候', 'Saat makan mi', [
            ('王大文', '美美，牛肉麵怎麼吃？', 'Meimei, mi daging sapi dimakan bagaimana?'),
            ('李美美', '你先吃麵，然後喝湯。', 'Makan minya dulu, lalu minum kuahnya.'),
            ('王大文', '好吃！臺灣的小吃很好吃，我也喜歡臺灣的麵包。', 'Enak! Jajanan Taiwan enak sekali, aku juga suka roti Taiwan.'),
            ('李美美', '別吃太快！我吃飯很慢。', 'Jangan makan terlalu cepat! Aku makannya pelan.'),
            ('王大文', '這個餐廳的菜很好吃。明天我們跟陳老師一起去吧！', 'Masakan restoran ini enak sekali. Besok kita ajak Guru Chen ke sini, yuk!'),
        ]),
    ]),
    'A18': ('Sebelum ujian Dawen membeli pena di toko dekat kampus: menanyakan harga, memilih yang murah, membayar, '
            'dan menerima kembalian. Di luar toko ia bercerita kepada Meimei.', [
        ('在店裡', 'Di dalam toko', [
            ('王大文', '先生，請問這枝筆多少錢？', 'Pak, permisi, pena ini berapa?'),
            ('老闆', '這枝一百二十元。', 'Yang ini seratus dua puluh dolar.'),
            ('王大文', '好貴！那枝呢？', 'Mahal sekali! Kalau yang itu?'),
            ('老闆', '那枝便宜，八十塊。', 'Yang itu murah, delapan puluh.'),
            ('王大文', '我買兩枝。一共多少錢？', 'Saya beli dua. Totalnya berapa?'),
            ('老闆', '一共一百六十塊。', 'Totalnya seratus enam puluh.'),
            ('王大文', '給你兩百塊。', 'Ini dua ratus.'),
            ('老闆', '找你四十塊。謝謝！', 'Kembaliannya empat puluh. Terima kasih!'),
        ]),
        ('在店門口', 'Di depan toko', [
            ('李美美', '大文，你買什麼東西？', 'Dawen, kamu beli apa?'),
            ('王大文', '我買兩枝筆。明天考試！', 'Aku beli dua pena. Besok ujian!'),
            ('李美美', '這個店的東西貴嗎？', 'Barang di toko ini mahal?'),
            ('王大文', '很貴！一枝筆一百二十塊！我只買便宜的。', 'Mahal! Satu pena seratus dua puluh dolar! Aku cuma beli yang murah.'),
            ('李美美', '我也想買紙。我只有五十塊，夠嗎？', 'Aku juga mau beli kertas. Aku cuma punya lima puluh dolar, cukup?'),
            ('王大文', '夠！紙很便宜。', 'Cukup! Kertas murah.'),
        ]),
    ]),
    'A19': ('Dawen dan Meimei berbelanja: Dawen memilih baju yang ukurannya pas, lalu di toko sepatu ia ingin '
            'mengganti sepatunya yang sudah usang.', [
        ('在衣服店', 'Di toko baju', [
            ('李美美', '大文，你想買什麼？', 'Dawen, kamu mau beli apa?'),
            ('王大文', '我想買這件衣服。', 'Aku mau beli baju ini.'),
            ('李美美', '你喜歡紅的還是白的？', 'Kamu suka yang merah atau yang putih?'),
            ('王大文', '我喜歡白的。可是這件有點小。', 'Aku suka yang putih. Tapi yang ini agak kecil.'),
            ('李美美', '你穿大的吧！大的不錯。', 'Coba pakai yang besar! Yang besar bagus.'),
            ('王大文', '好，我買大的。', 'Oke, aku beli yang besar.'),
        ]),
        ('在鞋子店', 'Di toko sepatu', [
            ('王大文', '美美，你的鞋子很漂亮！是新的嗎？', 'Meimei, sepatumu cantik sekali! Baru, ya?'),
            ('李美美', '是新的。我的舊鞋子是黑的。', 'Iya, baru. Sepatu lamaku yang hitam.'),
            ('王大文', '我的鞋子很舊，我也想買新鞋子。', 'Sepatuku sudah usang, aku juga mau beli sepatu baru.'),
            ('李美美', '你看，白的很好看。', 'Lihat, yang putih bagus.'),
            ('王大文', '好看，可是很貴！', 'Bagus, tapi mahal!'),
            ('李美美', '黑的比白的便宜。', 'Yang hitam lebih murah daripada yang putih.'),
            ('王大文', '好，我買黑的！', 'Oke, aku beli yang hitam!'),
        ]),
    ]),
    'A20': ('Dawen dan Meimei bercerita cara mereka pergi ke kampus, lalu Meimei menjelaskan bagaimana ia pulang '
            'ke rumah orang tuanya di Taichung.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你每天怎麼來學校？', 'Dawen, setiap hari kamu ke kampus naik apa?'),
            ('王大文', '我坐公車來。公車站在學校門口，很方便。你呢？', 'Aku naik bus. Halte busnya di depan gerbang kampus, praktis. Kamu?'),
            ('李美美', '我住在學校附近，我走路來學校。', 'Aku tinggal di dekat kampus, aku jalan kaki ke kampus.'),
            ('王大文', '走路也很方便！', 'Jalan kaki juga praktis!'),
        ]),
        ('說去臺中', 'Membicarakan perjalanan ke Taichung', [
            ('王大文', '美美，你爸爸媽媽在臺中，你怎麼去臺中？', 'Meimei, orang tuamu di Taichung, kamu ke Taichung naik apa?'),
            ('李美美', '我坐火車。因為火車很快，所以我喜歡坐火車。', 'Aku naik kereta. Karena kereta cepat, jadi aku suka naik kereta.'),
            ('王大文', '你不坐計程車嗎？', 'Kamu tidak naik taksi?'),
            ('李美美', '不坐，計程車很貴！我爸爸有一輛車子，有時候他開車來臺北。', 'Tidak, taksi mahal! Ayahku punya mobil, kadang-kadang dia menyetir ke Taipei.'),
            ('王大文', '我家人在印尼，我坐飛機去看他們。', 'Keluargaku di Indonesia, aku naik pesawat untuk menjenguk mereka.'),
        ]),
    ]),
    'A21': ('Dawen dan Meimei mau naik kereta ke Taichung. Di taman mereka bertanya jalan ke stasiun kepada seorang '
            'bapak, tetapi setelah keluar mereka berjalan ke arah yang salah dan kembali lagi ke taman sebelum '
            'akhirnya melihat stasiun.', [
        ('在公園', 'Di taman', [
            ('王大文', '先生，請問，火車站怎麼走？', 'Pak, permisi, ke stasiun kereta lewat mana?'),
            ('先生', '你們從這個門出去，火車站就在路的右邊。', 'Kalian keluar dari pintu ini, stasiunnya ada di sebelah kanan jalan.'),
            ('王大文', '右邊？不是左邊？', 'Sebelah kanan? Bukan kiri?'),
            ('先生', '對，是右邊。走五分鐘就到。', 'Iya, kanan. Jalan lima menit langsung sampai.'),
            ('王大文', '謝謝您！', 'Terima kasih, Pak!'),
        ]),
        ('火車站在哪裡？', 'Stasiunnya di mana?', [
            ('李美美', '大文，你看到火車站嗎？', 'Dawen, kamu lihat stasiunnya?'),
            ('王大文', '沒有。這是什麼地方？……你看，這裡又是公園！', 'Tidak. Ini tempat apa? …Lihat, ini taman lagi!'),
            ('李美美', '大文，我們走左邊！先生說右邊！', 'Dawen, kita jalan ke kiri! Bapak tadi bilang kanan!'),
            ('王大文', '對！我們走右邊。……你看，我看見火車站！在那裡！', 'Iya! Kita ke kanan. …Lihat, aku lihat stasiunnya! Di sana!'),
            ('李美美', '好，我們馬上去！', 'Oke, kita langsung ke sana!'),
        ]),
    ]),
    'A22': ('Dawen merasa tidak enak badan di kampus: kepala, mata, dan hidungnya tidak nyaman. Saat istirahat ia '
            'makin lemas, sampai tidak bisa mendengar Meimei dengan jelas.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你今天不舒服嗎？', 'Dawen, hari ini kamu tidak enak badan?'),
            ('王大文', '我很不舒服，我頭很痛。', 'Aku tidak enak badan sekali, kepalaku sakit sekali.'),
            ('李美美', '你感冒了嗎？', 'Kamu masuk angin?'),
            ('王大文', '可能是。我很累，眼睛也很痛。', 'Mungkin. Aku capek sekali, mataku juga sakit.'),
            ('李美美', '鼻子呢？', 'Hidungmu?'),
            ('王大文', '鼻子也不舒服。', 'Hidungku juga tidak enak.'),
        ]),
        ('下課的時候', 'Saat istirahat', [
            ('李美美', '大文，你的身體怎麼樣？', 'Dawen, badanmu bagaimana?'),
            ('王大文', '很不好。我的手和腳都很累。', 'Tidak baik. Tangan dan kakiku lemas semua.'),
            ('李美美', '你生病了！你應該去睡覺。', 'Kamu sakit! Kamu harus tidur.'),
            ('王大文', '什麼？我沒聽見。我的耳朵也不舒服！', 'Apa? Aku tidak dengar. Telingaku juga tidak enak!'),
            ('李美美', '我說：你應該去睡覺！', 'Kubilang: kamu harus tidur!'),
        ]),
    ]),
    'A23': ('Dawen masih sakit tetapi bilang tidak apa-apa. Meimei memberi tahu guru lalu mengajaknya ke dokter; '
            'dokter memberinya obat dan menyuruhnya istirahat.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你的頭還痛嗎？', 'Dawen, kepalamu masih sakit?'),
            ('王大文', '還很痛……可是我沒事。', 'Masih sakit sekali… tapi aku tidak apa-apa.'),
            ('李美美', '大家都說你應該去看病！', 'Semua orang bilang kamu harus pergi berobat!'),
            ('王大文', '為什麼？我自己休息就好。', 'Kenapa? Aku istirahat sendiri saja sudah cukup.'),
            ('李美美', '我去告訴老師。你等我，我們一起去！', 'Aku beri tahu guru dulu. Tunggu aku, kita pergi bersama!'),
            ('王大文', '好吧……謝謝你。', 'Baiklah… terima kasih.'),
        ]),
        ('看醫生', 'Ke dokter', [
            ('醫生', '你好，你哪裡不舒服？', 'Halo, bagian mana yang tidak enak?'),
            ('王大文', '醫生，我頭痛，也很累。', 'Dokter, kepala saya sakit, juga capek sekali.'),
            ('醫生', '你是感冒。你應該多休息，多喝水。這是藥，早上、中午、晚上吃。',
             'Kamu masuk angin. Kamu harus banyak istirahat dan banyak minum air. Ini obatnya, diminum pagi, siang, dan malam.'),
            ('王大文', '謝謝醫生！', 'Terima kasih, Dokter!'),
            ('李美美', '大文，今天你應該休息，別看電影！', 'Dawen, hari ini kamu harus istirahat, jangan nonton film!'),
            ('王大文', '好，我去睡覺！', 'Oke, aku tidur!'),
        ]),
    ]),
    'A24': ('Hari yang panas sekali. Dawen mengajak ke gunung, tetapi Meimei tidak mau karena terlalu panas dan '
            'mengajak pergi hari Sabtu; hari Sabtu di gunung angin bertiup kencang dan tiba-tiba hujan turun.', [
        ('在學校外面', 'Di luar kampus', [
            ('王大文', '今天好熱！我們去山上吧！', 'Hari ini panas sekali! Kita ke gunung, yuk!'),
            ('李美美', '今天？不要，走路很熱，也很累。', 'Hari ini? Jangan, jalan kaki panas, juga capek.'),
            ('王大文', '可是山上空氣很好，花也很漂亮。', 'Tapi di gunung udaranya segar, bunganya juga cantik.'),
            ('李美美', '星期六天氣不熱，我們星期六去吧！現在我們去喝冰茶。', 'Hari Sabtu cuacanya tidak panas, kita pergi hari Sabtu saja! Sekarang kita minum teh dingin.'),
            ('王大文', '好！星期六下雨嗎？', 'Oke! Hari Sabtu hujan?'),
            ('李美美', '不下雨。', 'Tidak hujan.'),
        ]),
        ('星期六，在山上', 'Hari Sabtu, di gunung', [
            ('王大文', '山上好冷！風很大！', 'Di gunung dingin sekali! Anginnya kencang sekali!'),
            ('李美美', '你看，這裡的花很漂亮！', 'Lihat, bunga di sini cantik sekali!'),
            ('王大文', '這裡的山都很低，走路不累。我最喜歡山上！', 'Gunung di sini rendah-rendah, jalan kaki tidak capek. Aku paling suka di gunung!'),
            ('李美美', '……大文，下雨了！', '…Dawen, hujan turun!'),
            ('王大文', '你說不下雨！', 'Katamu tidak hujan!'),
            ('李美美', '我們快下山吧！', 'Ayo cepat kita turun gunung!'),
        ]),
    ]),
    'A25': ('Dawen menelepon Meimei saat Meimei sedang di kelas, lalu menelepon lagi malam harinya. Keesokan harinya '
            'ia memperkenalkan temannya, Zhiming, kepada Meimei.', [
        ('下午，打電話', 'Sore hari, menelepon', [
            ('王大文', '美美，你好！我是大文。', 'Meimei, halo! Ini Dawen.'),
            ('李美美', '大文！對不起，我現在上課，不能說話。', 'Dawen! Maaf, aku sedang di kelas, tidak bisa bicara.'),
            ('王大文', '沒關係。晚上我打電話給你。', 'Tidak apa-apa. Nanti malam aku telepon kamu.'),
        ]),
        ('晚上，打電話', 'Malam hari, menelepon', [
            ('李美美', '大文，你打電話給我，什麼事？', 'Dawen, kamu meneleponku, ada apa?'),
            ('王大文', '明天我帶一個朋友去學校，我給你介紹。', 'Besok aku bawa seorang teman ke kampus, akan kuperkenalkan padamu.'),
            ('李美美', '好！明天學校見！', 'Oke! Sampai ketemu besok di kampus!'),
        ]),
        ('第二天，在學校', 'Keesokan harinya, di kampus', [
            ('王大文', '美美，我給你介紹，這是我的朋友志明。', 'Meimei, kuperkenalkan, ini temanku Zhiming.'),
            ('志明', '你好！我叫志明，我是臺灣人。', 'Halo! Namaku Zhiming, aku orang Taiwan.'),
            ('李美美', '你好！你也是學生嗎？', 'Halo! Kamu juga mahasiswa?'),
            ('志明', '是，我學英文。', 'Iya, aku belajar bahasa Inggris.'),
            ('李美美', '你有手機嗎？我打電話給你。', 'Kamu punya HP? Nanti aku telepon kamu.'),
            ('志明', '有。', 'Punya.'),
            ('李美美', '今天我請你們喝咖啡！', 'Hari ini aku traktir kalian minum kopi!'),
        ]),
    ]),
}
