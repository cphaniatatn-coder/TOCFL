"""Data 情境對話 berbasis cerita Vol.3 (lanjutan pilot; dipakai oleh dialog_cerita.py).

Format sama dengan BARU di dialog_cerita.py: kode → (scene Indonesia, [(tempat, judul Indonesia, [(pembicara, zh, id)])]).
"""

BARU = {
    'C01': ('Jam tujuh malam di dapur asrama. Zhiming baru pulang kuliah dan belum makan; Annie menyisakan nasi goreng '
            'untuknya. Setelah makan dan mencuci piring, mereka menonton film sampai selesai.', [
        ('晚上七點，宿舍廚房', 'Jam tujuh malam, dapur asrama', [
            ('志明', '安妮，你吃過飯了嗎？', 'Annie, kamu sudah makan?'),
            ('安妮', '吃過了，剛才在廚房吃的。你呢？', 'Sudah, tadi makan di dapur. Kamu?'),
            ('志明', '我剛下課，現在才要吃。', 'Aku baru selesai kuliah, sekarang baru mau makan.'),
            ('安妮', '廚房裡還有一些炒飯，我做得太多了。你吃吧！', 'Di dapur masih ada nasi goreng, aku masak kebanyakan. Makan saja!'),
            ('志明', '太好了！謝謝你！', 'Asyik! Terima kasih!'),
            ('志明', '炒飯都吃光了，太好吃了！碗我自己洗。', 'Nasi gorengnya habis kumakan, enak sekali! Mangkuknya kucuci sendiri.'),
            ('安妮', '好，洗完了放在餐桌上就好。', 'Oke, selesai dicuci taruh saja di meja makan.'),
            ('志明', '你功課寫完了嗎？', 'PR-mu sudah selesai?'),
            ('安妮', '寫完了。明天的考試，我也準備了。', 'Sudah. Ujian besok juga sudah kusiapkan.'),
            ('志明', '那我們接著看電影吧！', 'Kalau begitu, habis ini kita nonton film yuk!'),
        ]),
        ('在客廳', 'Di ruang tamu', [
            ('安妮', '好啊！這部電影你看過了嗎？', 'Boleh! Film ini kamu sudah pernah nonton?'),
            ('志明', '沒看過。你呢？', 'Belum pernah. Kamu?'),
            ('安妮', '去年看過一次，可是我很想再看一次。', 'Tahun lalu pernah sekali, tapi aku ingin nonton lagi.'),
            ('志明', '電影幾點結束？', 'Filmnya selesai jam berapa?'),
            ('安妮', '十一點。看完電影，你早點回家睡覺吧，明天還要考試！', 'Jam sebelas. Habis nonton, kamu cepat pulang dan tidur ya, besok masih ada ujian!'),
        ]),
    ]),
    'C02': ('Zhiming mengeluhkan kamar Dawen yang berantakan. Saat membereskannya, mereka sadar perabotnya sudah tua '
            'dan lemarinya rusak, jadi akhir pekan mereka pergi ke toko perabot.', [
        ('在家', 'Di rumah', [
            ('志明', '大文，你的房間又亂又髒！', 'Dawen, kamarmu berantakan dan kotor!'),
            ('王大文', '對不起，我最近太忙了。', 'Maaf, akhir-akhir ini aku terlalu sibuk.'),
            ('志明', '你的書別放在沙發上，放在書架上吧。', 'Bukumu jangan ditaruh di sofa, taruh di rak buku saja.'),
            ('王大文', '書架太小了，我的書太多。', 'Rak bukunya terlalu kecil, bukuku terlalu banyak.'),
            ('志明', '衣服也別放在椅子上，要掛在衣架上。', 'Baju juga jangan ditaruh di kursi, harus digantung di hanger.'),
            ('王大文', '好，我現在就去掛。', 'Oke, sekarang juga kugantung.'),
            ('志明', '你看一下，這個櫃子也壞了。', 'Coba lihat, lemari ini juga rusak.'),
            ('王大文', '對，我們的家具都太舊了。', 'Iya, perabot kita semuanya terlalu tua.'),
            ('志明', '週末我們去看一下新的書架和櫃子吧。', 'Akhir pekan kita lihat-lihat rak buku dan lemari baru yuk.'),
        ]),
        ('週末，在家具店', 'Akhir pekan, di toko perabot', [
            ('王大文', '志明，你看，這個書架很大，也不貴。', 'Zhiming, lihat, rak buku ini besar, juga tidak mahal.'),
            ('志明', '好！可是別買太多，我們的房間不大。', 'Oke! Tapi jangan beli terlalu banyak, kamar kita tidak besar.'),
            ('王大文', '我們再看一下書桌。', 'Kita lihat meja belajar juga.'),
            ('志明', '好，我們趕快看，商店六點關門。', 'Oke, kita cepat lihat, tokonya tutup jam enam.'),
        ]),
    ]),
    'C03': ('Sabtu pagi Dawen dan Zhiming membagi tugas rumah: mencuci piring dan baju. Saat membuang sampah, '
            'kantongnya robek, jadi mereka membereskannya bersama.', [
        ('星期六早上，在家', 'Sabtu pagi, di rumah', [
            ('志明', '大文，家裡太髒了，我們一起弄一弄吧。', 'Dawen, rumah terlalu kotor, ayo kita bereskan bersama.'),
            ('王大文', '好。你把碗洗了，我把衣服洗一洗。', 'Oke. Kamu cuci mangkuknya, aku cuci baju.'),
            ('志明', '好。洗衣機在哪裡？', 'Oke. Mesin cucinya di mana?'),
            ('王大文', '在門口。昨天的衣服都乾了，我先拿進來。', 'Di dekat pintu. Baju kemarin sudah kering semua, kuambil masuk dulu.'),
        ]),
        ('在門口', 'Di depan pintu', [
            ('志明', '碗都洗了。大文，垃圾呢？', 'Mangkuk sudah dicuci semua. Dawen, sampahnya?'),
            ('王大文', '我來拿出去……啊！袋子破了！', 'Biar aku yang bawa keluar… Ah! Kantongnya robek!'),
            ('志明', '沒關係，我們用別的袋子裝吧。', 'Tidak apa-apa, kita masukkan ke kantong lain saja.'),
            ('王大文', '可是這個袋子太小了。', 'Tapi kantong ini terlalu kecil.'),
            ('志明', '那就用兩個。你把垃圾裝一裝，我把地上弄乾淨。', 'Kalau begitu pakai dua. Kamu masukkan sampahnya, aku bersihkan lantainya.'),
            ('王大文', '好。弄完了，我們去吃早飯吧！', 'Oke. Selesai ini, kita pergi sarapan ya!'),
        ]),
    ]),
    'C04': ('Dawen dan Zhiming pindah dari apartemen ke rumah dua lantai berhalaman. Mereka menata perabot, tetapi lemarinya terlalu '
            'berat; Meimei datang dan membantu membawanya ke lantai atas.', [
        ('搬家', 'Pindahan', [
            ('王大文', '志明，我們把沙發放在客廳吧。', 'Zhiming, sofanya kita taruh di ruang tamu saja.'),
            ('志明', '好。這個櫃子呢？', 'Oke. Lemari ini?'),
            ('王大文', '把櫃子搬到樓上的臥室去吧。', 'Lemarinya kita angkat ke kamar tidur di lantai atas.'),
            ('志明', '這個櫃子太重了！我們先把它放在樓下的房間吧。', 'Lemari ini terlalu berat! Kita taruh dulu di kamar lantai bawah.'),
        ]),
        ('美美來了', 'Meimei datang', [
            ('李美美', '大文，這座房子很漂亮！一共有幾層？', 'Dawen, rumah ini cantik sekali! Ada berapa lantai?'),
            ('王大文', '兩層。樓下有客廳和廚房，樓上有三個臥房。', 'Dua lantai. Di bawah ada ruang tamu dan dapur, di atas ada tiga kamar tidur.'),
            ('李美美', '還有一個大院子！', 'Ada halaman besar juga!'),
            ('王大文', '對。美美，你可以幫我們搬櫃子嗎？', 'Iya. Meimei, bisa bantu kami mengangkat lemari?'),
            ('李美美', '好！我們三個人一起把它搬到樓上去。', 'Boleh! Kita bertiga angkat ke atas bersama.'),
            ('志明', '小心，椅子底下有很多書！', 'Hati-hati, di bawah kursi banyak buku!'),
        ]),
    ]),
    'C05': ('Dawen akan ke Taichung beberapa hari dan menitipkan kunci kepada Zhiming. Lalu ketahuan uang sakunya '
            'sudah habis, dan Zhiming meminjamkan uang.', [
        ('在家門口', 'Di depan pintu rumah', [
            ('王大文', '志明，我明天去臺中，三天以後回來。我把鑰匙交給你。', 'Zhiming, besok aku ke Taichung, tiga hari lagi pulang. Kuncinya kutitipkan padamu.'),
            ('志明', '好。信箱裡的信呢？', 'Oke. Surat di kotak surat bagaimana?'),
            ('王大文', '請你把信放在我的桌子上。', 'Tolong taruh suratnya di mejaku.'),
            ('志明', '沒問題。你的房間鎖了嗎？', 'Tidak masalah. Kamarmu sudah dikunci?'),
            ('王大文', '鎖了。', 'Sudah.'),
            ('志明', '去臺中，你的零用錢夠嗎？', 'Ke Taichung, uang sakumu cukup?'),
            ('王大文', '啊……我這個月把零用錢都用完了，口袋裡只有一百塊！', 'Ah… bulan ini uang sakuku sudah habis, di saku cuma ada seratus dolar!'),
            ('志明', '那你怎麼去？', 'Lalu kamu pergi pakai apa?'),
            ('王大文', '媽媽說她會把錢寄給我，可是明天才到。', 'Kata ibu dia akan mengirim uang, tapi baru sampai besok.'),
            ('志明', '我先把五百塊借給你吧。', 'Kupinjamkan lima ratus dulu saja.'),
            ('王大文', '謝謝！回來以後，我一定還你。', 'Terima kasih! Setelah pulang, pasti kukembalikan.'),
        ]),
    ]),
    'C06': ('Perlengkapan kamar mandi Dawen dan Zhiming hampir habis. Mereka mendaftar barang yang perlu dibeli, lalu '
            'berbelanja kebutuhan sehari-hari di supermarket.', [
        ('在家', 'Di rumah', [
            ('志明', '大文，浴室裡沒有牙膏了！', 'Dawen, di kamar mandi pasta giginya habis!'),
            ('王大文', '肥皂也用完了。廁所的衛生紙呢？', 'Sabun juga habis. Tisu toiletnya?'),
            ('志明', '只有一個了。我們去超市買日用品吧。', 'Tinggal satu. Kita ke supermarket beli kebutuhan sehari-hari yuk.'),
            ('王大文', '好。浴室裡放著兩條毛巾、一個牙刷，毛巾夠了。', 'Oke. Di kamar mandi ada dua handuk dan satu sikat gigi, handuknya cukup.'),
            ('志明', '洗髮精和沐浴乳也不多了。', 'Sampo dan sabun cair juga tinggal sedikit.'),
        ]),
        ('在超市', 'Di supermarket', [
            ('志明', '你看，那邊站著很多人，他們在買什麼？', 'Lihat, di sana banyak orang berdiri, mereka beli apa?'),
            ('王大文', '洗髮精今天比較便宜！我們買兩瓶。', 'Sampo hari ini lebih murah! Kita beli dua botol.'),
            ('志明', '好。我也要買一個新的牙刷。', 'Oke. Aku juga mau beli sikat gigi baru.'),
            ('王大文', '東西都買了。我拿著東西，你去付錢吧。', 'Semua sudah dibeli. Aku pegang barangnya, kamu yang bayar ya.'),
        ]),
    ]),
    'C07': ('Dawen kesiangan karena sepekan begadang mengerjakan PR; Zhiming membangunkannya. Di kampus Meimei '
            'melihatnya lelah, dan Dawen berjanji tidur lebih awal.', [
        ('早上，在家', 'Pagi, di rumah', [
            ('志明', '大文，快起床！八點了！', 'Dawen, cepat bangun! Sudah jam delapan!'),
            ('王大文', '啊，我沒聽見鬧鐘！', 'Ah, aku tidak dengar alarmnya!'),
            ('志明', '九點上課，你還沒出門呢！', 'Jam sembilan kuliah, kamu belum berangkat juga!'),
            ('王大文', '我昨天半夜兩點才上床……', 'Kemarin aku baru naik ke kasur jam dua pagi…'),
            ('志明', '你這一週每天都很晚睡覺。夜晚都在做什麼？', 'Minggu ini kamu tiap hari tidur larut. Malam-malam kamu ngapain?'),
            ('王大文', '寫功課。這兩天我每天兩點才睡覺。', 'Mengerjakan PR. Dua hari ini aku baru tidur jam dua pagi.'),
        ]),
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你怎麼了？好像很累。', 'Dawen, kenapa kamu? Kelihatannya capek sekali.'),
            ('王大文', '這幾天我都很晚才睡覺。昨天上床以後，枕頭也不舒服……', 'Beberapa hari ini aku selalu tidur larut malam. Kemarin setelah naik ke kasur, bantalnya juga tidak nyaman…'),
            ('王大文', '我還做了一個夢，夢見考試！時鐘上已經兩點了，我還沒寫完。', 'Aku juga mimpi, mimpi ujian! Jam dinding sudah menunjuk jam dua, aku belum selesai menulis.'),
            ('李美美', '你太累了。今天晚上早點睡覺吧。', 'Kamu terlalu capek. Malam ini tidur lebih awal ya.'),
            ('王大文', '好，今天十點我就上床！', 'Oke, hari ini jam sepuluh aku sudah naik ke kasur!'),
        ]),
    ]),
    'C08': ('Tetangga Dawen bernyanyi setiap malam dan nyamuk tak berhenti mengganggu. Dawen dan Zhiming memutuskan '
            'bicara dengan tetangga; keesokan harinya Dawen bercerita hasilnya kepada Meimei.', [
        ('晚上，在家', 'Malam, di rumah', [
            ('王大文', '志明，鄰居又在唱歌了，吵死了！', 'Zhiming, tetangga nyanyi lagi, berisik sekali!'),
            ('志明', '對，他們每天晚上都唱個不停。', 'Iya, tiap malam mereka nyanyi tidak berhenti-henti.'),
            ('王大文', '我明天有考試，想早點睡覺。', 'Besok aku ujian, ingin tidur lebih awal.'),
            ('志明', '房間裡還有蚊子，飛個不停，我也累死了。', 'Di kamar juga ada nyamuk, terbang terus, aku juga capek sekali.'),
            ('王大文', '我們去跟鄰居說一下吧。', 'Ayo kita bilang ke tetangga.'),
        ]),
        ('第二天，在學校', 'Keesokan harinya, di kampus', [
            ('李美美', '大文，你昨天晚上幾點睡覺？', 'Dawen, semalam kamu tidur jam berapa?'),
            ('王大文', '兩點！這幾天，我每天都很晚才睡覺。', 'Jam dua! Beberapa hari ini aku tiap hari baru tidur larut.'),
            ('李美美', '為什麼？', 'Kenapa?'),
            ('王大文', '鄰居每天晚上唱歌，房間裡的蚊子也多死了。我的日子太難過了！', 'Tetangga tiap malam nyanyi, nyamuk di kamar juga banyak sekali. Hidupku susah sekali!'),
            ('李美美', '你跟鄰居說了嗎？', 'Kamu sudah bilang ke tetangga?'),
            ('王大文', '說了。他們說十點以後不唱了。今天晚上我可以好好睡覺了！', 'Sudah. Kata mereka setelah jam sepuluh tidak nyanyi lagi. Malam ini aku bisa tidur nyenyak!'),
        ]),
    ]),
    'C09': ('Dawen bingung memilih tempat tinggal tahun depan: di pusat kota atau di pinggiran. Ia dan Meimei '
            'membandingkan hidup di kota dan di desa, termasuk desa di Indonesia.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，明年你要住在市區還是鄉下？', 'Dawen, tahun depan kamu mau tinggal di pusat kota atau di desa?'),
            ('王大文', '我還不知道。市區的房屋太貴了，鄉下比市區便宜得多。', 'Aku belum tahu. Rumah di pusat kota terlalu mahal, di desa jauh lebih murah.'),
            ('李美美', '可是鄉下沒有市區那麼方便。', 'Tapi desa tidak senyaman pusat kota.'),
            ('王大文', '對，可是鄉下的環境好，夏天也涼快得多。', 'Iya, tapi lingkungan desa bagus, musim panas juga jauh lebih sejuk.'),
            ('李美美', '我一直住在城市，很喜歡城市的生活。', 'Aku selalu tinggal di kota, aku suka sekali kehidupan kota.'),
            ('王大文', '我在印尼住在鄉下，比較喜歡那樣的生活。', 'Di Indonesia aku tinggal di desa, aku lebih suka kehidupan seperti itu.'),
            ('李美美', '印尼的鄉下跟臺灣的鄉下不同嗎？', 'Desa di Indonesia beda dengan desa di Taiwan?'),
            ('王大文', '很不同。印尼的鄉下沒有臺灣這麼冷！', 'Beda sekali. Desa di Indonesia tidak sedingin di Taiwan!'),
            ('李美美', '那你就住鄉下吧！週末我去找你，也過過這樣的生活。', 'Kalau begitu tinggal di desa saja! Akhir pekan aku main ke tempatmu, ikut merasakan hidup seperti ini.'),
        ]),
    ]),
    'C10': ('Menjelang akhir bulan Dawen hanya makan bakpao karena uang bulanannya menipis. Meimei melihat buku harian '
            'pengeluarannya dan mengusulkan memasak bersama.', [
        ('月底，在學校', 'Akhir bulan, di kampus', [
            ('李美美', '大文，你怎麼每天都吃饅頭？', 'Dawen, kenapa kamu tiap hari makan bakpao?'),
            ('王大文', '到月底了，我的生活費不夠了。', 'Sudah akhir bulan, biaya hidupku tidak cukup.'),
            ('李美美', '你一個月花多少錢？', 'Sebulan kamu menghabiskan berapa?'),
            ('王大文', '一般是一萬五。可是東西越來越貴了！', 'Biasanya lima belas ribu. Tapi barang-barang makin lama makin mahal!'),
            ('李美美', '加上房租呢？', 'Ditambah sewa?'),
            ('王大文', '兩萬多。我經常在日記裡寫我花了多少錢，你看。', 'Dua puluh ribu lebih. Aku sering menulis pengeluaranku di buku harian, lihat.'),
        ]),
        ('看大文的日記', 'Melihat buku harian Dawen', [
            ('李美美', '咖啡、電影、衣服……你越買越多！', 'Kopi, film, baju… kamu makin lama makin banyak belanja!'),
            ('王大文', '對，錢越來越少。', 'Iya, uangnya makin lama makin sedikit.'),
            ('李美美', '下個月我們一起做飯吧，比較便宜。', 'Bulan depan kita masak bareng saja, lebih murah.'),
            ('王大文', '好！下個月我也不買咖啡了。', 'Oke! Bulan depan aku juga tidak beli kopi lagi.'),
        ]),
    ]),
    'C11': ('Guru mengumumkan study tour ke gunung dan meminta semua membawa jas hujan dan payung. Keesokan paginya '
            'langit mendung, dan Meimei mengingatkan Dawen membawa payung.', [
        ('上課的時候', 'Saat pelajaran', [
            ('陳老師', '同學們，明天我們去山上。山上很涼，請大家多穿一點衣服。', 'Anak-anak, besok kita ke gunung. Di gunung sejuk, semuanya tolong pakai baju lebih tebal.'),
            ('王大文', '老師，要帶傘嗎？', 'Bu, perlu bawa payung?'),
            ('陳老師', '要。山上的天氣常常變，晴天也會下雨。請大家帶雨衣和雨傘。', 'Perlu. Cuaca di gunung sering berubah, cerah pun bisa hujan. Semuanya tolong bawa jas hujan dan payung.'),
        ]),
        ('第二天早上，在大文家門口', 'Keesokan paginya, di depan rumah Dawen', [
            ('李美美', '大文，今天是陰天，別忘了帶傘！', 'Dawen, hari ini mendung, jangan lupa bawa payung!'),
            ('王大文', '好……啊，外面已經下雨了！', 'Oke… ah, di luar sudah hujan!'),
            ('李美美', '你的鞋子都溼了！別再走路了，我們坐車去學校吧。', 'Sepatumu sudah basah semua! Jangan jalan kaki lagi, kita naik kendaraan ke kampus saja.'),
            ('王大文', '好。希望山上是晴天！', 'Oke. Semoga di gunung cerah!'),
        ]),
    ]),
    'C12': ('Annie diwawancarai untuk beasiswa: ia menceritakan tempat lahir, bahasa ibu, kapan pindah ke Taipei, '
            'riwayat sekolah, dan perjalanannya ke Tiongkok daratan semasa kecil.', [
        ('面試', 'Wawancara', [
            ('王先生', '請你介紹一下自己。', 'Silakan perkenalkan diri Anda.'),
            ('安妮', '我叫安妮，今年二十一歲，是大學生。我是在雅加達出生的。', 'Nama saya Annie, tahun ini dua puluh satu tahun, mahasiswi. Saya lahir di Jakarta.'),
            ('王先生', '你的母語是什麼？', 'Bahasa ibu Anda apa?'),
            ('安妮', '印尼話。我家是華人，所以我也會說一點中文。', 'Bahasa Indonesia. Keluarga saya keturunan Tionghoa, jadi saya juga bisa sedikit bahasa Mandarin.'),
            ('王先生', '你什麼時候來臺灣？', 'Kapan Anda datang ke Taiwan?'),
            ('安妮', '去年。我在雅加達長大，在那裡上國小和中學。', 'Tahun lalu. Saya besar di Jakarta, dan bersekolah SD sampai SMA di sana.'),
            ('王先生', '你去過大陸嗎？', 'Anda pernah ke Tiongkok daratan?'),
            ('安妮', '去過一次。當時我年紀很小，只有八歲。', 'Pernah sekali. Waktu itu saya masih kecil, baru delapan tahun.'),
            ('王先生', '好。請寫一下你的住址和電話。', 'Baik. Silakan tulis alamat dan nomor telepon Anda.'),
            ('安妮', '好。我的住址是臺北市中山路二十號。', 'Baik. Alamat saya Jalan Zhongshan nomor dua puluh, Kota Taipei.'),
        ]),
    ]),
    'C13': ('Meimei menunjukkan foto keluarga besarnya saat Tahun Baru Imlek. Dawen bertanya siapa saja mereka: kakek-nenek '
            'dari pihak ibu, paman dan bibi dari pihak ayah, lalu mereka membandingkan keluarga masing-masing.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你看，這是過年的時候我們家的照片。', 'Dawen, lihat, ini foto keluargaku waktu Tahun Baru Imlek.'),
            ('王大文', '好多人！他們都是你的家人嗎？', 'Banyak sekali orangnya! Semuanya keluargamu?'),
            ('李美美', '對，一共有好幾十個人。', 'Iya, totalnya ada beberapa puluh orang.'),
            ('王大文', '中間的老先生是誰？', 'Bapak tua di tengah itu siapa?'),
            ('李美美', '是我外公，旁邊是我外婆。他們有好幾個孫子和孫女，其中我是最大的。', 'Itu kakekku dari pihak ibu, di sebelahnya nenekku. Mereka punya beberapa cucu laki-laki dan perempuan, di antaranya aku yang paling tua.'),
            ('王大文', '這兩位呢？', 'Dua orang ini?'),
            ('李美美', '是我伯父和伯母。伯父是我爸爸的哥哥，伯母是他的太太。', 'Itu paman dan bibiku. Paman adalah kakak laki-laki ayahku, bibi adalah istrinya.'),
            ('王大文', '這位是你姑姑嗎？', 'Yang ini bibimu dari pihak ayah?'),
            ('李美美', '對，她是我爸爸的妹妹。爸爸的姊姊，我們叫她「姑媽」。', 'Iya, dia adik perempuan ayahku. Kakak perempuan ayah kami panggil gūmā.'),
            ('王大文', '你有兄弟嗎？', 'Kamu punya saudara laki-laki?'),
            ('李美美', '我只有一個弟弟，他叫小明。你呢？', 'Aku cuma punya satu adik laki-laki, namanya Xiaoming. Kamu?'),
            ('王大文', '我有一個哥哥和一個姊姊。我們家的人沒有你們家那麼多！', 'Aku punya satu kakak laki-laki dan satu kakak perempuan. Keluargaku tidak sebanyak keluargamu!'),
        ]),
    ]),
    'C14': ('Dawen mengabarkan kakak perempuannya akan menikah dengan teman sekelasnya di universitas. Minggu depan ia '
            'pulang ke Indonesia, dan neneknya yang sudah tua pun akan datang.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，我姊姊快要結婚了！', 'Meimei, kakak perempuanku sebentar lagi menikah!'),
            ('李美美', '真的嗎？什麼時候？', 'Serius? Kapan?'),
            ('王大文', '十二月十號。下個星期，我就要回印尼了。', 'Tanggal sepuluh Desember. Minggu depan aku sudah pulang ke Indonesia.'),
            ('李美美', '你姊姊的先生是誰？', 'Suami kakakmu siapa?'),
            ('王大文', '他叫做小林，是我姊姊大學的同班同學。', 'Namanya Xiaolin, teman sekelas kakakku di universitas.'),
            ('李美美', '他帥不帥？', 'Dia ganteng tidak?'),
            ('王大文', '很帥！我父母也很喜歡他。', 'Ganteng sekali! Orang tuaku juga suka padanya.'),
            ('李美美', '你家有幾口人？', 'Keluargamu ada berapa orang?'),
            ('王大文', '五口人：父親、母親、哥哥、姊姊和我。', 'Lima orang: ayah, ibu, kakak laki-laki, kakak perempuan, dan aku.'),
            ('李美美', '你外婆也會來嗎？', 'Nenekmu juga akan datang?'),
            ('王大文', '會！她已經是八十歲的老太太了，可是她說：「孫女結婚，我一定要去！」', 'Ya! Beliau sudah nenek-nenek berumur delapan puluh, tapi katanya: Cucuku menikah, aku pasti datang!'),
            ('李美美', '太好了！回來以後，給我看結婚的照片吧！', 'Bagus sekali! Pulangnya nanti, tunjukkan foto pernikahannya ya!'),
        ]),
    ]),
    'C15': ('Dawen sibuk bekerja paruh waktu di kedai kopi. Ia dan Meimei membicarakan tujuan bekerja dan cita-cita; '
            'Sabtu ini Dawen harus menggantikan temannya, jadi Meimei datang ke kedainya.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你最近怎麼這麼忙？', 'Dawen, akhir-akhir ini kenapa kamu sibuk sekali?'),
            ('王大文', '為了多一點零用錢，我去咖啡店打工了。', 'Supaya uang sakuku sedikit bertambah, aku kerja paruh waktu di kedai kopi.'),
            ('李美美', '你打工的目的只是錢嗎？', 'Tujuanmu kerja paruh waktu cuma uang?'),
            ('王大文', '也是為了練習中文。來喝咖啡的客人都是臺灣人。', 'Juga untuk latihan bahasa Mandarin. Pelanggan yang datang minum kopi semuanya orang Taiwan.'),
            ('李美美', '真好！你以後想做什麼？', 'Bagus! Nanti kamu mau jadi apa?'),
            ('王大文', '我爸爸是商人，我外公以前是工人。爸爸希望我也當商人。你呢？', 'Ayahku pedagang, kakek dari ibuku dulu buruh. Ayah ingin aku juga jadi pedagang. Kamu?'),
            ('李美美', '我想教書。為了當老師，我每天都很用功。', 'Aku ingin mengajar. Supaya bisa jadi guru, aku belajar giat setiap hari.'),
        ]),
        ('星期六，打電話', 'Sabtu, menelepon', [
            ('李美美', '大文，今天一起去看電影吧！', 'Dawen, hari ini nonton film yuk!'),
            ('王大文', '對不起，今天我要替一個朋友上班，他生病了。', 'Maaf, hari ini aku harus menggantikan seorang teman kerja, dia sakit.'),
            ('李美美', '好吧，那我去你的店裡喝咖啡！', 'Ya sudah, kalau begitu aku ke kedaimu minum kopi!'),
        ]),
    ]),
    'C16': ('Meimei mengajak makan malam, tetapi Dawen yang magang harus lembur menyelesaikan laporan untuk rapat. '
            'Keesokan harinya atasan memuji laporannya dan Dawen tidak perlu lembur, jadi ia menelepon Meimei.', [
        ('打電話', 'Menelepon', [
            ('李美美', '大文，今天晚上一起吃飯吧！', 'Dawen, malam ini makan bareng yuk!'),
            ('王大文', '對不起，我今天必須加班。', 'Maaf, hari ini aku harus lembur.'),
            ('李美美', '為什麼？', 'Kenapa?'),
            ('王大文', '明天早上要開會，我必須寫完報告。', 'Besok pagi ada rapat, aku harus menyelesaikan laporan.'),
            ('李美美', '好吧，別太累了。', 'Ya sudah, jangan terlalu capek.'),
        ]),
        ('第二天，在公司', 'Keesokan harinya, di kantor', [
            ('王先生', '大文，你的報告寫得很好。', 'Dawen, laporanmu bagus sekali.'),
            ('王大文', '謝謝！還有問題嗎？', 'Terima kasih! Masih ada masalah?'),
            ('王先生', '沒有。公司的要求，你都做得很好。今天你不用加班了。', 'Tidak ada. Semua permintaan perusahaan kamu kerjakan dengan baik. Hari ini kamu tidak perlu lembur.'),
            ('王大文', '太好了！明天還要開會嗎？', 'Bagus! Besok masih ada rapat?'),
            ('王先生', '不必，下個星期再開。', 'Tidak perlu, minggu depan saja.'),
        ]),
        ('下班以後，打電話', 'Sepulang kerja, menelepon', [
            ('王大文', '美美，今天我不用加班了！我們去吃飯吧！', 'Meimei, hari ini aku tidak perlu lembur! Ayo kita makan!'),
            ('李美美', '好啊！我在學校門口等你。', 'Ayo! Aku tunggu di depan kampus.'),
        ]),
    ]),
    'C17': ('Di klub hobi, Dawen dan Meimei membicarakan minat masing-masing: mendaki dan memotret. Akhir pekan mereka '
            'mendaki Yangmingshan; warga di sana ramah dan pemandangannya indah.', [
        ('在社團', 'Di klub', [
            ('李美美', '大文，你對什麼有興趣？', 'Dawen, kamu tertarik pada apa?'),
            ('王大文', '我對爬山很有興趣。你呢？', 'Aku sangat tertarik mendaki gunung. Kamu?'),
            ('李美美', '我對爬山沒有興趣，可是對拍照很有興趣。', 'Aku tidak tertarik mendaki, tapi sangat tertarik memotret.'),
            ('王大文', '那我們一起去陽明山吧！我爬山，你拍照。', 'Kalau begitu kita ke Yangmingshan bareng! Aku mendaki, kamu memotret.'),
            ('李美美', '好！週末去。', 'Oke! Akhir pekan ini.'),
        ]),
        ('在陽明山', 'Di Yangmingshan', [
            ('王大文', '美美，我們爬了兩個小時了，好累。', 'Meimei, kita sudah mendaki dua jam, capek sekali.'),
            ('李美美', '再走幾步就到了。', 'Beberapa langkah lagi sampai.'),
            ('王大文', '剛才那位老先生給我們水喝，他對我們很好。', 'Bapak tua tadi memberi kita air minum, beliau baik sekali pada kita.'),
            ('李美美', '對，這裡的人對客人都很客氣。', 'Iya, orang-orang di sini semuanya ramah pada tamu.'),
            ('李美美', '你看，這裡的風景好美！我要拍很多照片。', 'Lihat, pemandangan di sini indah sekali! Aku mau memotret banyak.'),
            ('王大文', '拍完了，我們在山上散步吧。', 'Selesai memotret, kita jalan-jalan santai di atas gunung ya.'),
        ]),
    ]),
    'C18': ('Dawen baru menonton film Amerika di bioskop, tetapi Meimei lebih suka berita dan majalah. Selera mereka '
            'berbeda, lalu mereka sepakat bermain game di rumah karena akhir pekan akan sangat panas.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，昨天我去電影院看了一部美國電影，有趣極了！', 'Meimei, kemarin aku nonton film Amerika di bioskop, seru sekali!'),
            ('李美美', '是嗎？我覺得美國電影不太有意思。', 'Oh ya? Menurutku film Amerika kurang menarik.'),
            ('王大文', '那你週末都做什麼？', 'Lalu akhir pekan kamu biasanya ngapain?'),
            ('李美美', '我喜歡在家看新聞、看雜誌。', 'Aku suka di rumah baca berita dan majalah.'),
            ('王大文', '看新聞？太無聊了！', 'Baca berita? Membosankan sekali!'),
            ('李美美', '不無聊，我覺得很有意思。你呢？', 'Tidak membosankan, menurutku menarik. Kamu?'),
            ('王大文', '我最喜歡玩遊戲，遊戲好玩得不得了！', 'Aku paling suka main game, game itu seru bukan main!'),
            ('李美美', '遊戲我不太會玩。', 'Aku kurang bisa main game.'),
            ('王大文', '這個週末我教你吧！', 'Akhir pekan ini aku ajari!'),
            ('李美美', '好吧。新聞說週末熱得不得了，我們就在家玩遊戲。', 'Boleh. Kata berita akhir pekan panasnya bukan main, kita main game di rumah saja.'),
        ]),
    ]),
    'C19': ('Dawen dan Meimei merencanakan hari libur: ke Museum Istana Nasional dulu, lalu ke pasar malam. Di pasar '
            'malam mereka makan sambil jalan dan menonton pertunjukan jalanan.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，這個假日我們去哪裡玩？', 'Dawen, libur kali ini kita main ke mana?'),
            ('王大文', '我想去故宮參觀，也想去逛夜市。', 'Aku ingin berkunjung ke Museum Istana, juga ingin jalan-jalan ke pasar malam.'),
            ('李美美', '那我們先去故宮，再去逛夜市吧！', 'Kalau begitu kita ke museum dulu, baru ke pasar malam!'),
            ('王大文', '好！故宮有很多有名畫家的畫。我們要訂票嗎？', 'Oke! Di museum ada banyak lukisan pelukis terkenal. Kita perlu pesan tiket?'),
            ('李美美', '要，我現在就上網訂。', 'Perlu, sekarang juga aku pesan online.'),
        ]),
        ('在夜市', 'Di pasar malam', [
            ('王大文', '人好多，到處都是人！', 'Ramai sekali, di mana-mana orang!'),
            ('李美美', '我們一邊逛一邊吃吧！', 'Kita jalan-jalan sambil makan yuk!'),
            ('王大文', '好。你看，那邊有人一邊唱歌一邊跳舞。', 'Oke. Lihat, di sana ada orang menyanyi sambil menari.'),
            ('李美美', '他同時做兩件事，舞也跳得很好！', 'Dia melakukan dua hal sekaligus, tariannya juga bagus!'),
            ('王大文', '今天太好玩了！', 'Hari ini seru sekali!'),
        ]),
    ]),
    'C20': ('Dawen dan Meimei naik MRT ke department store: masuk lewat pintu masuk, menunggu di peron yang ramai, lalu '
            'keluar di pintu keluar yang langsung menuju department store.', [
        ('在學校門口', 'Di depan kampus', [
            ('王大文', '美美，我們怎麼去百貨公司？', 'Meimei, kita ke department store naik apa?'),
            ('李美美', '搭捷運去比較快。', 'Naik MRT lebih cepat.'),
            ('王大文', '臺北的捷運跟雅加達的地鐵一樣嗎？', 'MRT Taipei sama dengan kereta bawah tanah Jakarta?'),
            ('李美美', '差不多。走吧，入口在那邊。', 'Kurang lebih. Ayo, pintu masuknya di sana.'),
        ]),
        ('在捷運站', 'Di stasiun MRT', [
            ('王大文', '月臺上人好多！', 'Di peron banyak sekali orang!'),
            ('李美美', '沒關係，班次很多，五分鐘就有一班。', 'Tidak apa-apa, jadwalnya banyak, tiap lima menit ada satu.'),
            ('王大文', '車上有座位嗎？', 'Di kereta ada tempat duduk?'),
            ('李美美', '沒有，我們站著吧。', 'Tidak ada, kita berdiri saja.'),
            ('王大文', '還有幾站？', 'Masih berapa stasiun lagi?'),
            ('李美美', '快到了……到了！我們從三號出口出去，可以直接到百貨公司。', 'Hampir sampai… sudah sampai! Kita keluar dari pintu keluar nomor tiga, bisa langsung ke department store.'),
        ]),
    ]),
    'C21': ('Meimei mengajari Dawen naik motor seperti kebanyakan orang Taiwan. Dawen takut karena lalu lintasnya '
            'semrawut, jadi mereka berlatih dulu di tempat parkir.', [
        ('在路上', 'Di jalan', [
            ('李美美', '大文，臺灣人都騎機車，你會騎嗎？', 'Dawen, orang Taiwan semuanya naik motor, kamu bisa?'),
            ('王大文', '不會。臺灣的交通太亂了，我騎不了機車。', 'Tidak bisa. Lalu lintas di Taiwan terlalu semrawut, aku tidak sanggup naik motor.'),
            ('李美美', '沒關係，我教你。', 'Tidak apa-apa, aku ajari.'),
            ('王大文', '可是公路上的速度太快了。', 'Tapi kecepatan di jalan raya terlalu tinggi.'),
            ('李美美', '我們先在停車場練習。', 'Kita latihan dulu di tempat parkir.'),
        ]),
        ('在停車場', 'Di tempat parkir', [
            ('李美美', '你看，這是我的摩托車。你坐在這裡。', 'Lihat, ini motorku. Kamu duduk di sini.'),
            ('王大文', '好。騎完了，機車要停在哪裡？', 'Oke. Setelah selesai, motornya diparkir di mana?'),
            ('李美美', '要停在停車場，路邊不能停。', 'Harus diparkir di tempat parkir, di pinggir jalan tidak boleh.'),
            ('王大文', '你說得很清楚，你的中文很標準，我都聽得懂。', 'Penjelasanmu jelas sekali, bahasa Mandarinmu baku, aku mengerti semuanya.'),
            ('李美美', '那你今天騎得了嗎？', 'Jadi hari ini kamu sanggup naik?'),
            ('王大文', '今天我還是騎自行車吧！希望明年能夠自己騎機車去學校。', 'Hari ini aku naik sepeda saja deh! Semoga tahun depan bisa naik motor sendiri ke kampus.'),
        ]),
    ]),
    'C22': ('Dawen bersiap pulang ke Indonesia untuk pernikahan kakaknya: visa baru selesai dan kopernya kurang, jadi '
            'Meimei meminjamkan koper. Setibanya di Indonesia ia menelepon Meimei.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你今天出國嗎？', 'Dawen, hari ini kamu berangkat ke luar negeri?'),
            ('王大文', '不，我明天才出國。簽證昨天才拿到。', 'Tidak, aku baru berangkat besok. Visanya baru kudapat kemarin.'),
            ('李美美', '行李準備了嗎？', 'Barang bawaanmu sudah disiapkan?'),
            ('王大文', '還沒。我才有一個箱子，不夠。', 'Belum. Aku cuma punya satu koper, tidak cukup.'),
            ('李美美', '我有一個大箱子，借給你吧！', 'Aku punya koper besar, kupinjamkan saja!'),
            ('王大文', '太好了，謝謝！', 'Bagus, terima kasih!'),
        ]),
        ('打電話', 'Menelepon', [
            ('王大文', '美美，我到印尼了！', 'Meimei, aku sudah sampai di Indonesia!'),
            ('李美美', '好快！臺灣和印尼的時差是幾個小時？', 'Cepat sekali! Perbedaan waktu Taiwan dan Indonesia berapa jam?'),
            ('王大文', '才一個小時。', 'Cuma satu jam.'),
            ('李美美', '你要在印尼留多久？', 'Kamu mau tinggal berapa lama di Indonesia?'),
            ('王大文', '留兩個星期。姊姊結婚以後，我就回臺灣。', 'Dua minggu. Setelah kakakku menikah, aku pulang ke Taiwan.'),
        ]),
    ]),
    'C23': ('Tiket pesawat ke Pulau Hijau (Lüdao) habis, jadi Dawen dan Meimei terpaksa naik kapal. Kapal hari itu pun '
            'penuh, tetapi mereka tetap membeli tiket untuk besok pagi.', [
        ('在旅行社', 'Di agen perjalanan', [
            ('王大文', '美美，去綠島的飛機票都賣完了！', 'Meimei, tiket pesawat ke Lüdao sudah habis terjual!'),
            ('李美美', '真的嗎？那船呢？', 'Serius? Kalau kapal?'),
            ('王大文', '船票也快要賣完了。', 'Tiket kapal juga hampir habis.'),
            ('李美美', '那我們只好坐船了。', 'Kalau begitu terpaksa kita naik kapal.'),
            ('王大文', '可是坐船要很久，我會不舒服。', 'Tapi naik kapal lama, aku bisa mabuk.'),
            ('李美美', '不管坐什麼，我都想去！', 'Naik apa pun, aku tetap mau pergi!'),
        ]),
        ('買船票', 'Membeli tiket kapal', [
            ('王大文', '小姐，還有船票嗎？', 'Mbak, masih ada tiket kapal?'),
            ('小姐', '今天的船客滿了，明天早上還有兩張。', 'Kapal hari ini sudah penuh, besok pagi masih ada dua.'),
            ('李美美', '明天的也好！不管多貴，我們都要買。', 'Besok juga tidak apa-apa! Semahal apa pun, kami beli.'),
            ('王大文', '對！我們要好好利用這個假日。', 'Betul! Kita harus memanfaatkan liburan ini sebaik-baiknya.'),
        ]),
    ]),
    'C25': ('Meimei mengajak Dawen ke pesta ulang tahun Annie hari Sabtu. Dawen sudah janji menonton film sore itu, '
            'jadi mereka mengatur jadwal, lalu berencana membeli hadiah bersama.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，星期六安妮家有生日派對，我們一起去，好不好？', 'Dawen, Sabtu ada pesta ulang tahun di rumah Annie, kita pergi bareng, ya?'),
            ('王大文', '好啊！派對幾點？', 'Boleh! Pestanya jam berapa?'),
            ('李美美', '晚上七點。', 'Jam tujuh malam.'),
            ('王大文', '可是星期六下午我跟朋友約了看電影。', 'Tapi Sabtu sore aku sudah janjian nonton film dengan teman.'),
            ('李美美', '是約會嗎？', 'Kencan, ya?'),
            ('王大文', '不是約會！是跟同學去看電影，五點結束。', 'Bukan kencan! Nonton film dengan teman sekelas, selesai jam lima.'),
            ('李美美', '那你還是先看電影，再來派對吧。', 'Kalau begitu, sebaiknya kamu nonton film dulu, baru datang ke pesta.'),
            ('王大文', '好。我們要帶禮物嗎？', 'Oke. Kita perlu bawa hadiah?'),
            ('李美美', '最好帶一個小禮物。我們一起去買，好不好？', 'Sebaiknya bawa hadiah kecil. Kita beli bareng, ya?'),
            ('王大文', '好！你明天有空嗎？下午或者晚上都可以。', 'Oke! Besok kamu ada waktu? Siang atau malam boleh.'),
            ('李美美', '明天下午有空。買完禮物，我請客，我們去喝咖啡！', 'Besok siang ada waktu. Selesai beli hadiah, aku traktir, kita minum kopi!'),
            ('王大文', '上次是你請客，這次我請！', 'Terakhir kamu yang traktir, kali ini aku!'),
        ]),
    ]),
    'C26': ('Meimei tidak bisa ikut mendaki karena ibunya menyuruhnya menemani neneknya yang sakit. Setelah akhir pekan, '
            'neneknya sudah membaik dan senang dikunjungi cucunya.', [
        ('星期五，在學校', 'Jumat, di kampus', [
            ('王大文', '美美，這個週末我們去爬山吧！', 'Meimei, akhir pekan ini kita mendaki yuk!'),
            ('李美美', '對不起，我不能去。媽媽讓我去陪奶奶。', 'Maaf, aku tidak bisa. Ibu menyuruhku menemani nenek.'),
            ('王大文', '奶奶怎麼了？', 'Nenekmu kenapa?'),
            ('李美美', '她生病了，一個人住，我們要照顧她。', 'Beliau sakit, tinggal sendirian, kami harus merawatnya.'),
            ('王大文', '你一個人去嗎？', 'Kamu pergi sendiri?'),
            ('李美美', '不，爸爸陪我去。', 'Tidak, ayah menemaniku.'),
            ('王大文', '你很關心奶奶。', 'Kamu sangat peduli pada nenekmu.'),
            ('李美美', '我小時候，奶奶一直在我身邊照顧我。', 'Waktu aku kecil, nenek selalu di sisiku merawatku.'),
        ]),
        ('星期一', 'Senin', [
            ('王大文', '美美，奶奶好一點了嗎？', 'Meimei, nenekmu sudah agak baikan?'),
            ('李美美', '好多了！她說：「你們來看我，讓我很高興。」', 'Jauh lebih baik! Beliau bilang: Kalian datang menjengukku, aku senang sekali.'),
            ('王大文', '你跟奶奶的關係很好。下次我也可以跟你去看她嗎？', 'Hubunganmu dengan nenek dekat sekali. Lain kali aku boleh ikut menjenguknya?'),
            ('李美美', '當然可以！', 'Tentu saja boleh!'),
        ]),
    ]),
    'C27': ('Dawen tidak datang ke diskusi tugas kelompok karena tidak membaca pesan Meimei — ia memakai earphone. '
            'Untungnya Meimei membawa kabar gembira: guru memuji laporan mereka.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，昨天下午你為什麼沒來？我們要談報告的事。', 'Dawen, kemarin sore kenapa kamu tidak datang? Kita mau membicarakan laporan.'),
            ('王大文', '什麼？我不知道！', 'Apa? Aku tidak tahu!'),
            ('李美美', '我傳簡訊給你了呢！你沒看到嗎？', 'Aku sudah kirim SMS ke kamu, lho! Kamu tidak lihat?'),
            ('王大文', '對不起，我一直戴著耳機聽音樂，沒聽見手機。', 'Maaf, aku terus pakai earphone dengar musik, tidak dengar ponselku.'),
            ('李美美', '你也沒回簡訊，真沒有禮貌！', 'Kamu juga tidak membalas SMS, tidak sopan sekali!'),
            ('王大文', '真對不起！報告怎麼樣了？', 'Benar-benar maaf! Laporannya bagaimana?'),
            ('李美美', '告訴你一個好消息：老師說我們的報告很好！', 'Kuberi tahu kabar baik: kata guru laporan kita bagus!'),
            ('王大文', '真的嗎？你在開玩笑吧？', 'Serius? Kamu bercanda, ya?'),
            ('李美美', '沒開玩笑！老師說我們合作得很好呢。', 'Tidak bercanda! Kata guru kerja sama kita bagus sekali, lho.'),
            ('王大文', '老師還說了什麼？', 'Guru bilang apa lagi?'),
            ('李美美', '她在報告上留下了一句話：「你們寫得真好！」', 'Beliau meninggalkan satu kalimat di laporan: Tulisan kalian bagus sekali!'),
        ]),
    ]),
    'C28': ('Dawen terkena flu berat di rumah dan Zhiming merawatnya. Malamnya Meimei menelepon: ia juga flu, dan '
            'obatnya dimakan adiknya yang mengira itu permen.', [
        ('在家', 'Di rumah', [
            ('志明', '大文，你怎麼了？', 'Dawen, kamu kenapa?'),
            ('王大文', '我發燒了，從昨天開始一直咳嗽。', 'Aku demam, sejak kemarin batuk terus.'),
            ('志明', '你一直在流汗。你流鼻水嗎？', 'Kamu terus berkeringat. Kamu pilek?'),
            ('王大文', '流鼻水，也頭痛。', 'Pilek, juga sakit kepala.'),
            ('志明', '你的病嚴重嗎？看醫生了嗎？', 'Sakitmu parah? Sudah ke dokter?'),
            ('王大文', '看了，醫生說不太嚴重，可是要多休息。', 'Sudah, kata dokter tidak terlalu parah, tapi harus banyak istirahat.'),
            ('志明', '那你今天別去上課了，我幫你跟老師說。', 'Kalau begitu hari ini jangan kuliah, nanti kubilang ke guru.'),
        ]),
        ('晚上，打電話', 'Malam, menelepon', [
            ('李美美', '大文，聽說你感冒了？我也感冒了！', 'Dawen, katanya kamu flu? Aku juga flu!'),
            ('王大文', '你吃藥了嗎？', 'Kamu sudah minum obat?'),
            ('李美美', '沒有！我的藥被弟弟吃掉了！', 'Belum! Obatku dimakan habis oleh adikku!'),
            ('王大文', '什麼？他為什麼吃你的藥？', 'Apa? Kenapa dia makan obatmu?'),
            ('李美美', '他以為是糖果。他沒事，可是我被這個感冒弄得好累。', 'Dia kira itu permen. Dia tidak apa-apa, tapi aku dibuat capek sekali oleh flu ini.'),
            ('王大文', '我的藥還有很多，明天我讓志明拿給你。', 'Obatku masih banyak, besok kusuruh Zhiming mengantarkannya padamu.'),
        ]),
    ]),
    'C29': ('Dawen membeli obat flu di apotek dan mendapat aturan minumnya. Keesokan harinya ia jauh lebih segar, '
            'sedangkan Meimei belum sembuh, jadi Dawen menemaninya ke apotek.', [
        ('在藥局', 'Di apotek', [
            ('王大文', '你好，我感冒了，要買感冒藥。', 'Halo, saya flu, mau beli obat flu.'),
            ('小姐', '你發燒嗎？', 'Anda demam?'),
            ('王大文', '昨天發燒，今天好一點了。', 'Kemarin demam, hari ini agak baikan.'),
            ('小姐', '這個藥應該飯後吃，一天三次。', 'Obat ini sebaiknya diminum sesudah makan, sehari tiga kali.'),
            ('王大文', '我應該吃幾天？', 'Saya sebaiknya minum berapa hari?'),
            ('小姐', '三天。三天以後，你應該就好了。', 'Tiga hari. Setelah tiga hari, seharusnya Anda sudah sembuh.'),
        ]),
        ('第二天，在學校', 'Keesokan harinya, di kampus', [
            ('李美美', '大文，你的臉色好多了！', 'Dawen, wajahmu jauh lebih segar!'),
            ('王大文', '對，我吃了藥，現在精神比較好了。', 'Iya, aku sudah minum obat, sekarang lebih bertenaga.'),
            ('李美美', '還發燒嗎？', 'Masih demam?'),
            ('王大文', '不發燒了，都正常了。你呢？', 'Sudah tidak demam, semua normal. Kamu?'),
            ('李美美', '我的感冒還沒好……', 'Fluku belum sembuh…'),
            ('王大文', '學校旁邊有一家藥房，現在應該還開著，我陪你去吧！', 'Di sebelah kampus ada apotek, sekarang seharusnya masih buka, aku temani kamu ke sana!'),
        ]),
    ]),
    'C31': ('Dawen terlambat masuk kelas karena hujan turun begitu ia keluar rumah. Di kelas sedang ada latihan soal; '
            'Dawen langsung menjawab dengan benar — tapi soal berikutnya tidak.', [
        ('在教室門口', 'Di depan kelas', [
            ('李美美', '大文，你不是說今天要早點來嗎？現在八點半了！', 'Dawen, bukannya kamu bilang hari ini mau datang lebih awal? Sekarang sudah jam setengah sembilan!'),
            ('王大文', '對不起！我才出門，就下雨了，結果公車也來晚了。', 'Maaf! Begitu aku keluar, langsung hujan, akhirnya busnya juga datang terlambat.'),
            ('陳老師', '大文，你又遲到了！快進來，我們在做題目。', 'Dawen, kamu terlambat lagi! Cepat masuk, kita sedang mengerjakan soal.'),
        ]),
        ('上課的時候', 'Saat pelajaran', [
            ('陳老師', '第三題，誰會回答？', 'Soal nomor tiga, siapa yang bisa menjawab?'),
            ('王大文', '我！答案是「三百」。', 'Saya! Jawabannya tiga ratus.'),
            ('陳老師', '對！大文立刻就回答了，很好。', 'Benar! Dawen langsung menjawab, bagus.'),
            ('李美美', '你才進教室，就答對了！', 'Kamu baru masuk kelas, langsung menjawab benar!'),
            ('王大文', '這個題目我昨天做過。', 'Soal ini kemarin sudah kukerjakan.'),
            ('陳老師', '那第四題呢？', 'Kalau soal nomor empat?'),
            ('王大文', '……這題我不會。', '…Yang ini saya tidak bisa.'),
        ]),
    ]),
    'C32': ('Semester hampir selesai. Dawen dan Meimei membicarakan kalender libur di Taiwan dan rencana mereka untuk '
            'libur musim dingin dan musim panas.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，這個學期快要結束了！寒假你要做什麼？', 'Dawen, semester ini hampir selesai! Libur musim dingin kamu mau ngapain?'),
            ('王大文', '我有時候想回家，有時候想去旅行，還不知道。', 'Kadang aku ingin pulang, kadang ingin jalan-jalan, belum tahu.'),
            ('李美美', '回印尼的飛機票貴嗎？', 'Tiket pulang ke Indonesia mahal?'),
            ('王大文', '寒假的飛機票很貴。暑假比較長，我暑假再回家。', 'Tiket saat libur musim dingin mahal. Libur musim panas lebih panjang, aku pulang waktu musim panas saja.'),
            ('李美美', '暑假你要做什麼？', 'Libur musim panas kamu mau ngapain?'),
            ('王大文', '我也要打工，也要學中文。你放假的時候做什麼？', 'Aku mau kerja paruh waktu, juga belajar Mandarin. Kalau libur, kamu ngapain?'),
            ('李美美', '有時候在家看書，有時候跟朋友出去玩。', 'Kadang di rumah membaca, kadang main keluar dengan teman.'),
            ('李美美', '寒假跟我去臺南玩，好不好？', 'Libur musim dingin ikut aku jalan-jalan ke Tainan, ya?'),
            ('王大文', '好啊！春假我們也可以去別的地方。', 'Boleh! Libur musim semi kita juga bisa pergi ke tempat lain.'),
            ('李美美', '春假只有幾天，去近一點的地方吧。', 'Libur musim semi cuma beberapa hari, ke tempat yang lebih dekat saja.'),
        ]),
    ]),
    'C33': ('Dawen akan lulus Juni tahun depan dan ingin meneliti pendidikan bahasa Mandarin untuk mahasiswa Indonesia. '
            'Meimei menyemangatinya untuk menemui profesornya.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你什麼時候畢業？', 'Dawen, kapan kamu lulus?'),
            ('王大文', '明年六月。從明年七月起，我就不是學生了！', 'Juni tahun depan. Mulai Juli tahun depan, aku bukan mahasiswa lagi!'),
            ('李美美', '畢業以後，你要做什麼？', 'Setelah lulus, kamu mau ngapain?'),
            ('王大文', '我想研究教育。', 'Aku ingin meneliti pendidikan.'),
            ('李美美', '研究什麼呢？', 'Meneliti apa?'),
            ('王大文', '題目就是「印尼學生怎麼學中文」。', 'Judulnya ya itu: Bagaimana mahasiswa Indonesia belajar Mandarin.'),
            ('李美美', '很有意思！你需要教授幫你嗎？', 'Menarik sekali! Kamu perlu bantuan profesor?'),
            ('王大文', '對。陳教授說我的中文程度很高，我希望得到他的幫助。', 'Iya. Profesor Chen bilang tingkat bahasa Mandarinku tinggi, aku berharap mendapat bantuannya.'),
            ('李美美', '陳教授的辦公室就在那邊，你現在去問他吧！', 'Kantor Profesor Chen ada di sana, sekarang saja kamu tanya beliau!'),
            ('王大文', '好！從今天起，我每天看三個小時的書。我說了，就一定要做到！', 'Oke! Mulai hari ini aku belajar tiga jam setiap hari. Yang sudah kukatakan pasti kulakukan!'),
            ('李美美', '你一定會成功！', 'Kamu pasti berhasil!'),
        ]),
    ]),
    'C34': ('Dawen sering salah menulis Hanzi dan meminta tips kepada guru. Guru menyarankan kelas kaligrafi, jadi '
            'Dawen mencobanya bersama Meimei.', [
        ('在教室', 'Di kelas', [
            ('王大文', '陳老師，漢字很難，我常常寫錯。我怎麼學？', 'Bu Chen, Hanzi sulit sekali, saya sering salah tulis. Bagaimana cara belajarnya?'),
            ('陳老師', '每個詞寫十遍，多寫寫、看看，就記得了。', 'Tiap kata tulis sepuluh kali, banyak menulis dan melihat, pasti ingat.'),
            ('王大文', '我可以只看拼音嗎？', 'Boleh saya lihat pinyinnya saja?'),
            ('陳老師', '不行，拼音只能幫你念。不會的字，你可以查字典，試試看。', 'Tidak boleh, pinyin cuma membantu membaca. Huruf yang tidak tahu, bisa dicari di kamus, coba saja.'),
            ('陳老師', '你也可以去上書法課，寫書法對學漢字很有幫助。', 'Kamu juga bisa ikut kelas kaligrafi, menulis kaligrafi sangat membantu belajar Hanzi.'),
        ]),
        ('在書法教室', 'Di kelas kaligrafi', [
            ('李美美', '大文，你想寫寫看書法嗎？', 'Dawen, kamu mau coba menulis kaligrafi?'),
            ('王大文', '好啊，我想試試看。這個字怎麼寫？我查一下。', 'Boleh, aku ingin mencoba. Huruf ini ditulis bagaimana? Kucari dulu.'),
            ('李美美', '慢慢寫……很好！', 'Tulis pelan-pelan… bagus!'),
            ('王大文', '寫了一個小時，好累，我們休息休息吧。', 'Sudah menulis satu jam, capek sekali, kita istirahat dulu yuk.'),
            ('李美美', '好。休息完了，你還要背二十個詞呢！', 'Oke. Setelah istirahat, kamu masih harus menghafal dua puluh kata!'),
            ('王大文', '好！那我們等一下再練習練習。', 'Oke! Nanti kita latihan lagi.'),
        ]),
    ]),
    'C35': ('Guru menjelaskan tata bahasa 叫 di papan tulis dengan beberapa contoh, lalu menyuruh murid berdiskusi '
            'berpasangan dan menulis karangan. Dawen dan Meimei memulai diskusi mereka.', [
        ('在教室', 'Di kelas', [
            ('陳老師', '同學們，請看黑板。今天的文法是「叫」，例如：「媽媽叫我去買東西。」', 'Anak-anak, lihat papan tulis. Tata bahasa hari ini 叫, misalnya: Ibu menyuruhku pergi belanja.'),
            ('王大文', '老師，可以給我們多一點例子嗎？', 'Bu, boleh beri kami contoh lebih banyak?'),
            ('陳老師', '可以。「老師叫學生寫作文。」', 'Boleh. Guru menyuruh murid menulis karangan.'),
            ('李美美', '老師，您也叫我們寫作文嗎？', 'Bu, Ibu juga menyuruh kami menulis karangan?'),
            ('陳老師', '對！我叫你們兩個人一起討論，然後寫作文。題目是「我的家」。', 'Betul! Saya suruh kalian berdua berdiskusi, lalu menulis karangan. Judulnya Rumahku.'),
        ]),
        ('下課以後', 'Sesudah kelas', [
            ('王大文', '美美，我們先討論一下吧。你想寫什麼？', 'Meimei, kita diskusi dulu yuk. Kamu mau menulis apa?'),
            ('李美美', '我想寫我的外公和外婆。你呢？', 'Aku ingin menulis tentang kakek dan nenekku. Kamu?'),
            ('王大文', '我想寫我在臺灣的「家」，就是我跟志明住的房子！', 'Aku mau menulis tentang rumahku di Taiwan, yaitu rumah yang kutinggali bersama Zhiming!'),
            ('李美美', '很好！寫完了，老師會幫我們改。', 'Bagus! Selesai menulis, guru akan membantu mengoreksi.'),
            ('王大文', '太好了！老師改了，我們就知道哪裡寫錯了。', 'Bagus! Setelah dikoreksi guru, kita jadi tahu bagian mana yang salah.'),
        ]),
    ]),
    'C36': ('Dawen dan Meimei membicarakan mata kuliah semester ini: selain kelas bahasa Mandarin, Dawen mengambil '
            'sejarah dan hukum, ikut kelas tingkat lanjut, dan berlatih lewat berita setiap hari.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你這個學期上什麼課？', 'Dawen, semester ini kamu ambil kuliah apa?'),
            ('王大文', '除了華語課以外，我還上歷史和法律。', 'Selain kelas bahasa Mandarin, aku juga ambil sejarah dan hukum.'),
            ('李美美', '法律？很難吧！', 'Hukum? Pasti sulit!'),
            ('王大文', '很難，可是可以學到很多方面的知識。', 'Sulit, tapi bisa belajar pengetahuan dari banyak bidang.'),
            ('李美美', '你學臺語嗎？', 'Kamu belajar bahasa Taiwan?'),
            ('王大文', '不學，可是我很想學，夜市的老闆都說臺語！', 'Tidak, tapi aku ingin sekali belajar, pedagang di pasar malam semua bicara bahasa Taiwan!'),
            ('李美美', '華語課有高級班嗎？', 'Kelas bahasa Mandarin ada kelas tingkat lanjut?'),
            ('王大文', '有，我在高級班。老師說的中文比較正式，我們也學現代的文化。', 'Ada, aku di kelas lanjut. Bahasa Mandarin guru lebih formal, kami juga belajar budaya modern.'),
            ('李美美', '除了上課，你還做什麼？', 'Selain kuliah, kamu ngapain lagi?'),
            ('王大文', '除了上課，我每天都看新聞，練習聽中文。', 'Selain kuliah, tiap hari aku menonton berita, berlatih mendengar bahasa Mandarin.'),
        ]),
    ]),
    'C37': ('Dawen membantu Xiaoming, adik Meimei, mengerjakan PR matematika: penjumlahan, pengurangan, perkalian, '
            'pembagian, dan bilangan desimal.', [
        ('在美美家', 'Di rumah Meimei', [
            ('王大文', '小明，今天的數學功課是什麼？', 'Xiaoming, PR matematika hari ini apa?'),
            ('小明', '加、減、乘、除。我覺得很困難。', 'Tambah, kurang, kali, bagi. Menurutku sulit sekali.'),
            ('王大文', '沒關係，我們一起做。三加五是多少？', 'Tidak apa-apa, kita kerjakan bersama. Tiga tambah lima berapa?'),
            ('小明', '是八！', 'Delapan!'),
            ('王大文', '很好。十減四呢？', 'Bagus. Sepuluh kurang empat?'),
            ('小明', '六。三乘四是十二，十二除四是三。', 'Enam. Tiga kali empat dua belas, dua belas dibagi empat tiga.'),
            ('王大文', '對！十和四差多少？', 'Betul! Sepuluh dan empat selisihnya berapa?'),
            ('小明', '差六！', 'Selisih enam!'),
        ]),
        ('做小數的題目', 'Mengerjakan soal desimal', [
            ('小明', '大文哥哥，二點五加一點五是多少？', 'Kak Dawen, dua koma lima tambah satu koma lima berapa?'),
            ('王大文', '你數數看。', 'Coba kamu hitung.'),
            ('小明', '……是四！', '…Empat!'),
            ('王大文', '對！你很認真，數學一定會越來越好。', 'Betul! Kamu tekun, matematikamu pasti makin lama makin bagus.'),
            ('小明', '大文哥哥，你的中文為什麼這麼好？', 'Kak Dawen, kenapa bahasa Mandarinmu bagus sekali?'),
            ('王大文', '因為我也很認真！', 'Karena aku juga tekun!'),
        ]),
    ]),
    'C38': ('Guru membagikan hasil tanya-jawab tentang kebiasaan mahasiswa di kelas: olahraga, kopi, dan jam tidur. '
            'Dawen ternyata termasuk yang kurang tidur.', [
        ('上課的時候', 'Saat pelajaran', [
            ('陳老師', '上個星期我問了我們班的同學一些問題。我們班有三十個學生，三分之一的學生每天運動。', 'Minggu lalu saya menanyakan beberapa hal ke teman-teman sekelas. Kelas kita ada tiga puluh murid, sepertiganya berolahraga setiap hari.'),
            ('王大文', '三分之一，那是十個學生！', 'Sepertiga, berarti sepuluh murid!'),
            ('陳老師', '對。還有，百分之八十的學生每天喝咖啡。', 'Betul. Lalu, delapan puluh persen murid minum kopi setiap hari.'),
            ('李美美', '老師，這包括您嗎？', 'Bu, itu termasuk Ibu?'),
            ('陳老師', '不包括，一切都是學生說的。', 'Tidak termasuk, semuanya dari jawaban murid.'),
            ('王大文', '睡覺呢？', 'Kalau tidur?'),
            ('陳老師', '許多同學說他們很忙，當中一半每天睡覺的時間只有六個小時。', 'Banyak murid bilang mereka sibuk, separuh di antaranya tidur cuma enam jam sehari.'),
            ('李美美', '大文，你也是那一半吧？', 'Dawen, kamu juga termasuk yang separuh itu, kan?'),
            ('王大文', '對……從今天起，我要早點睡覺！', 'Iya… mulai hari ini aku mau tidur lebih awal!'),
        ]),
    ]),
    'C39': ('Dawen mencari tempat tinggal yang lebih murah. Ia membandingkan sewa di Taipei dan Jakarta, lalu bersama '
            'Meimei melihat rumah yang punya potongan harga untuk pelajar muda.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，臺北的房租是雅加達的兩倍左右！', 'Meimei, sewa rumah di Taipei sekitar dua kali lipat Jakarta!'),
            ('李美美', '真的嗎？你現在的房租多少？', 'Serius? Sewamu sekarang berapa?'),
            ('王大文', '一萬塊左右。在雅加達，五千塊就夠了。', 'Sekitar sepuluh ribu. Di Jakarta, lima ribu sudah cukup.'),
            ('李美美', '你想找多少錢的房子？', 'Kamu mau cari rumah yang harganya berapa?'),
            ('王大文', '八千塊以下的。', 'Di bawah delapan ribu.'),
        ]),
        ('看房子', 'Melihat rumah', [
            ('李美美', '這個房子很好，可是房租九千塊以上。', 'Rumah ini bagus, tapi sewanya di atas sembilan ribu.'),
            ('王大文', '太貴了！', 'Terlalu mahal!'),
            ('李美美', '你看，這裡寫著：二十五歲以下的學生，可以便宜一千五百塊。', 'Lihat, di sini tertulis: pelajar di bawah dua puluh lima tahun dapat potongan seribu lima ratus.'),
            ('王大文', '我二十二歲！那就是七千五百塊左右。', 'Aku dua puluh dua tahun! Berarti sekitar tujuh ribu lima ratus.'),
            ('李美美', '還有，這裡離學校很近，走路十分鐘左右。', 'Lagi pula, dari sini ke kampus dekat, jalan kaki sekitar sepuluh menit.'),
            ('王大文', '好，就是這裡了！', 'Oke, di sini saja!'),
        ]),
    ]),
    'C40': ('Department store sedang merayakan ulang tahunnya dengan diskon besar. Dawen dan Meimei ikut antre, '
            'membandingkan harga, dan Meimei mencoba ukuran yang lebih kecil.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，百貨公司今天週年慶，衣服都打八折！', 'Dawen, department store hari ini ulang tahun, semua baju diskon dua puluh persen!'),
            ('王大文', '真的嗎？我們去逛街吧！', 'Serius? Ayo kita jalan-jalan belanja!'),
        ]),
        ('在百貨公司', 'Di department store', [
            ('李美美', '人好多，好熱鬧！大家都在排隊。', 'Ramai sekali! Semua orang antre.'),
            ('王大文', '你看，這裡的衣服一件比一件便宜！', 'Lihat, baju di sini makin lama makin murah!'),
            ('李美美', '這件外套打八折，還是貴了一點。', 'Jaket ini diskon dua puluh persen, tapi masih agak mahal.'),
            ('王大文', '那件呢？特價五百塊，很划算！', 'Yang itu? Harga spesial lima ratus, murah sekali!'),
            ('李美美', '可是那件大了一點。我想試穿小一點的。', 'Tapi yang itu agak besar. Aku mau coba yang lebih kecil.'),
            ('王大文', '好啊。我在這裡等你。你帶了現金嗎？', 'Boleh. Aku tunggu di sini. Kamu bawa uang tunai?'),
            ('李美美', '帶了。這件小一點的很好！我們去排隊付錢吧。', 'Bawa. Yang lebih kecil ini pas! Ayo antre bayar.'),
            ('王大文', '好，付完錢，我們再逛一下！', 'Oke, selesai bayar, kita jalan-jalan lagi sebentar!'),
        ]),
    ]),
    'C41': ('Ini musim dingin pertama Dawen di Taiwan. Meimei membantunya membeli pakaian hangat: sweter, sarung tangan, '
            'kaus kaki, sepatu, sandal, dan piyama.', [
        ('在衣服店', 'Di toko pakaian', [
            ('王大文', '美美，冬天快到了，這是我在臺灣的第一個冬天。我要買什麼？', 'Meimei, musim dingin hampir tiba, ini musim dingin pertamaku di Taiwan. Aku perlu beli apa?'),
            ('李美美', '你要買毛衣、手套和襪子。你看這件，紅紅的毛衣很漂亮。', 'Kamu perlu beli sweter, sarung tangan, dan kaus kaki. Lihat ini, sweter merah ini cantik sekali.'),
            ('王大文', '這件毛衣很適合你！我想要那件黑黑的。', 'Sweter ini cocok untukmu! Aku mau yang hitam itu.'),
            ('李美美', '好。那件金色的上衣呢？', 'Oke. Atasan emas yang itu?'),
            ('王大文', '金色的太貴了，我不買。', 'Yang emas terlalu mahal, aku tidak beli.'),
        ]),
        ('在鞋子店', 'Di toko sepatu', [
            ('王大文', '我的皮鞋舊了，拖鞋也壞了。', 'Sepatu kulitku sudah tua, sandalku juga rusak.'),
            ('李美美', '這雙皮鞋黑黑的，大小很合適。', 'Sepatu kulit hitam ini ukurannya pas.'),
            ('王大文', '穿了很舒服。這裡也有睡衣嗎？', 'Dipakai nyaman sekali. Di sini juga ada piyama?'),
            ('李美美', '有，那套睡衣看起來很好，晚上穿不會冷。', 'Ada, piyama itu kelihatannya bagus, dipakai malam tidak akan dingin.'),
            ('王大文', '好，都買了！今年冬天我不怕冷了！', 'Oke, semuanya kubeli! Musim dingin tahun ini aku tidak takut dingin!'),
        ]),
    ]),
    'C42': ('Di toko, Dawen tidak bisa membayar pakai kartu untuk belanja kecil, untung ia punya uang pas. Saat makan '
            'bersama Meimei, ia bertanya apakah di Taiwan perlu memberi tip.', [
        ('在店裡', 'Di toko', [
            ('店員', '一共三百二十塊。', 'Totalnya tiga ratus dua puluh.'),
            ('王大文', '可以刷卡嗎？', 'Bisa bayar pakai kartu?'),
            ('店員', '對不起，五百塊以下不能刷卡。你沒有零錢嗎？', 'Maaf, di bawah lima ratus tidak bisa pakai kartu. Anda tidak punya uang kecil?'),
            ('王大文', '有，我剛好有三百二十塊。', 'Ada, kebetulan saya pas punya tiga ratus dua puluh.'),
        ]),
        ('在餐廳', 'Di restoran', [
            ('王大文', '美美，在臺灣吃飯要給小費嗎？', 'Meimei, di Taiwan kalau makan perlu kasih tip?'),
            ('李美美', '不用。你不知道嗎？', 'Tidak perlu. Kamu tidak tahu?'),
            ('王大文', '不知道，我以為要給。', 'Tidak, kukira harus kasih.'),
            ('李美美', '你付錢了沒有？', 'Kamu sudah bayar belum?'),
            ('王大文', '還沒有。這裡可以刷卡嗎？', 'Belum. Di sini bisa pakai kartu?'),
            ('李美美', '可以，可是我已經付了，店員剛才刷了我的信用卡。今天我請你！', 'Bisa, tapi aku sudah bayar, tadi pelayan sudah menggesek kartuku. Hari ini aku traktir!'),
            ('王大文', '謝謝！那下次我請你。', 'Terima kasih! Lain kali aku yang traktir.'),
        ]),
    ]),
    'C43': ('Dawen dan Meimei berbelanja di pasar tradisional dan mampir ke toko buah milik ibu pemilik toko yang '
            'terkenal ramah dan sudah berjualan dua puluh tahun.', [
        ('在市場', 'Di pasar', [
            ('李美美', '大文，這個市場的老闆娘很有名。', 'Dawen, ibu pemilik toko di pasar ini terkenal.'),
            ('王大文', '為什麼？', 'Kenapa?'),
            ('李美美', '她每天都高高興興地做生意，大家都喜歡她。', 'Dia setiap hari berjualan dengan riang gembira, semua orang menyukainya.'),
        ]),
        ('在水果店', 'Di toko buah', [
            ('老闆娘', '你們好！今天的水果很好吃！', 'Halo! Buah hari ini enak-enak!'),
            ('王大文', '老闆娘，我要一籃蘋果。', 'Bu, saya mau sekeranjang apel.'),
            ('老闆娘', '好！你慢慢地看。', 'Baik! Silakan lihat pelan-pelan.'),
            ('李美美', '老闆娘，您是這個店的主人嗎？', 'Bu, Ibu pemilik toko ini?'),
            ('老闆娘', '對。我在這裡做了二十年的生意了。', 'Iya. Saya sudah berjualan di sini dua puluh tahun.'),
            ('王大文', '二十年！您每天都這麼高興嗎？', 'Dua puluh tahun! Ibu setiap hari segembira ini?'),
            ('老闆娘', '對啊！客人高興，我就高興。這個籃子送給你們，好好地吃吧！', 'Iya dong! Pelanggan senang, saya juga senang. Keranjang ini untuk kalian, makan yang enak ya!'),
        ]),
    ]),
    'C45': ('Saat makan siang bento di kampus, Dawen mengeluh bentonya terlalu asin. Meimei bercerita tentang tahu buatan '
            'ibunya dan mengundang Dawen makan di rumahnya akhir pekan.', [
        ('在學校吃午餐', 'Makan siang di kampus', [
            ('李美美', '大文，你今天吃什麼便當？', 'Dawen, hari ini kamu makan bento apa?'),
            ('王大文', '雞肉便當。什麼都好吃，就是太鹹了，米飯也太少。', 'Bento ayam. Semuanya enak, cuma terlalu asin, nasinya juga terlalu sedikit.'),
            ('李美美', '可能是醬和鹽放得太多了。', 'Mungkin kecap dan garamnya kebanyakan.'),
            ('王大文', '對，油也很多。我很想吃家裡做的菜。', 'Iya, minyaknya juga banyak. Aku kangen masakan rumah.'),
            ('李美美', '我媽媽做的豆腐，誰都喜歡。', 'Tahu buatan ibuku, siapa pun suka.'),
            ('王大文', '真的嗎？我也想吃！', 'Serius? Aku juga mau!'),
            ('李美美', '這個週末來我家吧，我媽媽會做好幾樣菜。', 'Akhir pekan ini datang ke rumahku saja, ibuku akan masak beberapa macam lauk.'),
            ('王大文', '太好了！要我帶什麼嗎？', 'Asyik! Aku perlu bawa sesuatu?'),
            ('李美美', '什麼都不用帶，人來就好！', 'Tidak perlu bawa apa-apa, datang saja!'),
        ]),
    ]),
    'C46': ('Dawen dan Meimei berbelanja di toko buah dan membicarakan buah-buahan Taiwan yang manis, terutama mangga.', [
        ('在水果店', 'Di toko buah', [
            ('王大文', '美美，臺灣的水果真多！', 'Meimei, buah di Taiwan banyak sekali!'),
            ('李美美', '對，臺灣的水果差不多都很甜，尤其是芒果。', 'Iya, buah Taiwan hampir semuanya manis, terutama mangga.'),
            ('王大文', '這裡的鳳梨和木瓜也很新鮮。', 'Nanas dan pepaya di sini juga segar.'),
            ('李美美', '我們買兩顆芒果和一個鳳梨吧。', 'Kita beli dua buah mangga dan satu nanas.'),
            ('王大文', '草莓和葡萄呢？', 'Stroberi dan anggur?'),
            ('李美美', '草莓差不多賣完了。橘子和番茄還有很多。', 'Stroberi hampir habis. Jeruk dan tomat masih banyak.'),
            ('王大文', '番茄也是水果嗎？', 'Tomat juga buah?'),
            ('李美美', '在臺灣，小番茄是水果！', 'Di Taiwan, tomat kecil itu buah!'),
            ('王大文', '真有意思！我最喜歡吃芒果，尤其是夏天的芒果。', 'Menarik! Aku paling suka mangga, terutama mangga musim panas.'),
            ('李美美', '好，今天我們就吃芒果！', 'Oke, hari ini kita makan mangga!'),
        ]),
    ]),
    'C47': ('Dawen memasak steak di dapur rumahnya untuk Meimei: menjelaskan cara memasaknya, tingkat kematangan, dan '
            'minuman. Meimei yang kelaparan ingin belajar resepnya.', [
        ('在大文家的廚房', 'Di dapur rumah Dawen', [
            ('李美美', '大文，你會做牛排嗎？', 'Dawen, kamu bisa masak steak?'),
            ('王大文', '會。做法很簡單：先放洋蔥，再放牛排。', 'Bisa. Caranya mudah: masukkan bawang bombai dulu, baru steaknya.'),
            ('李美美', '牛排要多熟？', 'Steaknya mau seberapa matang?'),
            ('王大文', '七分熟。你看，牛排做好了！', 'Tujuh puluh persen matang. Lihat, steaknya sudah jadi!'),
            ('李美美', '太好了，我餓壞了！', 'Asyik, aku lapar sekali!'),
            ('王大文', '豆子也熟了，正好可以吃。', 'Kacangnya juga sudah matang, pas bisa dimakan.'),
        ]),
        ('吃飯的時候', 'Saat makan', [
            ('王大文', '你要喝什麼？有蘋果汁。', 'Kamu mau minum apa? Ada jus apel.'),
            ('李美美', '不用，我泡了一杯茶。', 'Tidak usah, aku sudah menyeduh teh.'),
            ('王大文', '牛排好吃嗎？', 'Steaknya enak?'),
            ('李美美', '好吃極了！下次我也想學你的做法。', 'Enak sekali! Lain kali aku juga mau belajar caramu memasak.'),
            ('王大文', '好，下次你做，我等著吃！', 'Oke, lain kali kamu yang masak, aku tinggal makan!'),
        ]),
    ]),
    'C48': ('Dawen dan Meimei tiba di restoran populer: Meimei sudah memesan tempat. Paket terkenalnya berisi makanan '
            'laut, padahal Dawen tidak bisa makan makanan laut, jadi ia memilih paket daging sapi.', [
        ('在餐廳門口', 'Di depan restoran', [
            ('店員', '你好，請問幾位？', 'Halo, untuk berapa orang?'),
            ('王大文', '兩位。美美，你是不是訂位了？', 'Dua orang. Meimei, kamu sudah pesan tempat, kan?'),
            ('李美美', '是，我訂位了。七點，兩位，姓李。', 'Iya, sudah. Jam tujuh, dua orang, atas nama Li.'),
            ('店員', '好，這邊請。這是你們的位子。', 'Baik, silakan ke sini. Ini tempat duduk Anda.'),
        ]),
        ('在餐廳', 'Di restoran', [
            ('李美美', '這家的套餐很有名，有沙拉、海鮮和一杯果汁。', 'Paket di restoran ini terkenal, ada salad, makanan laut, dan segelas jus.'),
            ('王大文', '可是我不吃海鮮。', 'Tapi aku tidak makan makanan laut.'),
            ('李美美', '你是不是不能吃海鮮？', 'Kamu tidak bisa makan makanan laut, ya?'),
            ('王大文', '對，吃了海鮮，我會不舒服。', 'Iya, kalau makan makanan laut aku jadi tidak enak badan.'),
            ('李美美', '那你吃牛肉套餐吧，牛肉套餐沒有海鮮。', 'Kalau begitu kamu makan paket daging sapi saja, paket itu tidak ada makanan lautnya.'),
            ('王大文', '好。這裡的食物真好吃！', 'Oke. Makanan di sini enak sekali!'),
            ('李美美', '那下次我們再來吧！', 'Kalau begitu lain kali kita datang lagi!'),
        ]),
    ]),
    'C49': ('Dawen mengajak makan makanan cepat saji, tetapi Meimei menolak karena ia menjaga pola makan. Di minimarket, '
            'Meimei hanya membeli teh, dan Dawen mencoba teh oolong untuk pertama kali.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，我們中午去吃速食吧！', 'Meimei, siang ini kita makan makanan cepat saji yuk!'),
            ('李美美', '我一點也不想吃速食，速食對身體不好。', 'Aku sama sekali tidak mau makan makanan cepat saji, tidak baik untuk badan.'),
            ('王大文', '那你都吃什麼？', 'Lalu kamu biasanya makan apa?'),
            ('李美美', '我從來不吃速食，也從來不吃泡麵。早上我喝豆漿，吃一個餅。', 'Aku tidak pernah makan makanan cepat saji, juga tidak pernah makan mi instan. Pagi aku minum susu kedelai dan makan satu bing.'),
            ('王大文', '我昨天晚上吃了兩包泡麵……', 'Semalam aku makan dua bungkus mi instan…'),
            ('李美美', '你應該少吃一點泡麵！', 'Kamu harus kurangi makan mi instan!'),
        ]),
        ('在超商', 'Di minimarket', [
            ('王大文', '我要買餅乾和巧克力。你要嗎？', 'Aku mau beli biskuit dan cokelat. Kamu mau?'),
            ('李美美', '不要，這個星期我一點都沒吃甜的東西。', 'Tidak, minggu ini aku sama sekali tidak makan yang manis-manis.'),
            ('王大文', '那你喝什麼飲料？', 'Lalu kamu minum apa?'),
            ('李美美', '我只喝茶。你聞聞看，這杯烏龍茶的香味很好！', 'Aku cuma minum teh. Coba cium, aroma teh oolong ini enak sekali!'),
            ('王大文', '香味真好！我從來沒喝過烏龍茶，我也買一杯。', 'Aromanya harum sekali! Aku belum pernah minum teh oolong, aku juga beli segelas.'),
        ]),
    ]),
    'C50': ('Dawen mengurus izin tinggal (ARC) di kantor imigrasi. Fotonya kurang satu, jadi ia berfoto dulu, lalu '
            'bertanya tentang tempat pengurusan, layanan bahasa Inggris, dan lama prosesnya.', [
        ('在辦公室', 'Di kantor', [
            ('王大文', '你好，我要辦居留證。', 'Halo, saya mau mengurus kartu izin tinggal.'),
            ('小姐', '好。只要帶兩張照片，就可以辦。', 'Baik. Asalkan membawa dua lembar foto, sudah bisa diurus.'),
            ('王大文', '照片我只帶了一張……', 'Fotonya saya cuma bawa satu…'),
            ('小姐', '沒關係，樓下就可以拍照。', 'Tidak apa-apa, di lantai bawah bisa foto.'),
            ('王大文', '請問，可以在學校辦嗎？', 'Permisi, apa bisa diurus di kampus?'),
            ('小姐', '不行，只有在這裡才能辦。', 'Tidak bisa, hanya di sini baru bisa diurus.'),
        ]),
        ('拍完照片以後', 'Setelah berfoto', [
            ('王大文', '請問，這裡有英文服務嗎？我有一些問題。', 'Permisi, di sini ada layanan bahasa Inggris? Saya ada beberapa pertanyaan.'),
            ('小姐', '有。你有什麼問題，都可以提出來。', 'Ada. Kalau ada pertanyaan apa pun, silakan sampaikan.'),
            ('王大文', '辦居留證要多久？', 'Mengurus kartu izin tinggal butuh berapa lama?'),
            ('小姐', '只要一個星期就好了。', 'Cukup satu minggu saja.'),
            ('王大文', '太好了，謝謝！', 'Bagus, terima kasih!'),
        ]),
    ]),
    'C51': ('Surat yang Dawen kirim dari Indonesia baru sampai ke Meimei setelah Dawen kembali. Meimei mengenali tulisan '
            'tangannya; lalu Dawen ke bank untuk menabung dan mengirim surat untuk ibunya.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，我收到你的信了！是你在印尼寫的吧？', 'Dawen, suratmu sudah sampai! Kamu tulis di Indonesia, kan?'),
            ('王大文', '對！信封上沒有我的名字，你看得出來是我寫的嗎？', 'Iya! Di amplop tidak ada namaku, kamu bisa tahu itu tulisanku?'),
            ('李美美', '看得出來！你的字很特別。', 'Bisa! Tulisanmu khas sekali.'),
            ('王大文', '你什麼時候回信？', 'Kapan kamu membalas?'),
            ('李美美', '你都回來了，我還要回信嗎？', 'Kamu sudah pulang, aku masih perlu membalas?'),
            ('王大文', '要！我也想收到你的信。', 'Perlu! Aku juga ingin menerima suratmu.'),
        ]),
        ('在銀行門口', 'Di depan bank', [
            ('王大文', '我要去銀行存錢，你要一起去嗎？', 'Aku mau ke bank menabung, kamu mau ikut?'),
            ('李美美', '好。你手上的郵件是什麼？', 'Boleh. Kiriman di tanganmu itu apa?'),
            ('王大文', '是兩封信，我要寄給媽媽。她收到了一定很高興。', 'Dua surat, mau kukirim ke ibu. Kalau sudah diterima, beliau pasti senang.'),
        ]),
    ]),
    'C52': ('Meimei bercerita ada pencurian motor di dekat rumah Dawen; pencurinya ditangkap warga. Malamnya Dawen tidak bisa '
            'tidur karena takut, apalagi pagi harinya ia mengira dompetnya hilang.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，昨天晚上你家附近發生了一件事。', 'Dawen, semalam ada kejadian di dekat rumahmu.'),
            ('王大文', '什麼事？', 'Kejadian apa?'),
            ('李美美', '有人偷了一輛機車！', 'Ada yang mencuri motor!'),
            ('王大文', '真的嗎？小偷抓到了嗎？', 'Serius? Pencurinya tertangkap?'),
            ('李美美', '抓住了！小偷想跑，可是大家把他抓住了。', 'Tertangkap! Pencurinya mau kabur, tapi orang-orang menangkapnya.'),
        ]),
        ('第二天', 'Keesokan harinya', [
            ('王大文', '我昨天很怕，一直睡不著。', 'Kemarin aku takut sekali, tidak bisa tidur.'),
            ('李美美', '你的東西丟了嗎？', 'Barangmu ada yang hilang?'),
            ('王大文', '沒有。早上我以為錢包丟了，找了很久，後來找著了，在沙發底下！', 'Tidak. Pagi tadi kukira dompetku hilang, kucari lama, akhirnya ketemu, di bawah sofa!'),
            ('李美美', '你啊，以後東西別亂放！', 'Kamu ini, lain kali barang jangan ditaruh sembarangan!'),
        ]),
    ]),
    'C53': ('Topan melanda Taipei, dan Dawen ingin keluar membeli makanan. Meimei memperingatkannya agar tetap di '
            'dalam; setelah topan berlalu, Dawen berjanji tidak nekat lagi.', [
        ('颱風天，打電話', 'Hari topan, menelepon', [
            ('李美美', '大文，颱風來了，你在哪裡？', 'Dawen, topan datang, kamu di mana?'),
            ('王大文', '我在家。我想出去買吃的。', 'Aku di rumah. Aku mau keluar beli makanan.'),
            ('李美美', '別出門！颱風天出門會很危險的。', 'Jangan keluar! Keluar saat topan pasti berbahaya.'),
            ('王大文', '可是我的泡麵都吃完了……', 'Tapi mi instanku sudah habis…'),
            ('李美美', '你家樓下有超商，別去遠的地方。', 'Di bawah rumahmu ada minimarket, jangan pergi jauh-jauh.'),
            ('王大文', '好。我會保護好自己，窗戶也會關好。', 'Oke. Aku akan menjaga diri, jendela juga akan kututup rapat.'),
            ('李美美', '對，在家最安全。', 'Betul, di rumah paling aman.'),
        ]),
        ('颱風以後', 'Setelah topan', [
            ('王大文', '昨天的颱風真可怕！外面很多東西都壞了。', 'Topan kemarin mengerikan sekali! Di luar banyak barang yang rusak.'),
            ('李美美', '也許明天還會下雨。', 'Mungkin besok masih hujan.'),
            ('王大文', '沒關係，我會在家的。以後颱風天，我不再出門了！', 'Tidak apa-apa, aku pasti di rumah. Lain kali kalau topan, aku tidak akan keluar lagi!'),
        ]),
    ]),
    'C54': ('Dawen dan Meimei berkemah di gunung. Malam hari mereka beristirahat sambil melihat bintang dan bulan; '
            'paginya mereka melihat matahari terbit dan bunga-bunga.', [
        ('晚上，在山上', 'Malam, di gunung', [
            ('李美美', '大文，你看，天上有一顆一顆的星星！', 'Dawen, lihat, di langit ada bintang-bintang!'),
            ('王大文', '好美麗！月亮也很大。', 'Indah sekali! Bulannya juga besar.'),
            ('李美美', '走了一天，好累。我們坐下吧。', 'Jalan seharian, capek sekali. Kita duduk yuk.'),
            ('王大文', '好，把背包放下，休息一下。', 'Oke, taruh ranselnya, istirahat sebentar.'),
            ('李美美', '在城市看不到這麼多星星。', 'Di kota tidak bisa melihat bintang sebanyak ini.'),
        ]),
        ('第二天早上', 'Keesokan paginya', [
            ('王大文', '美美，快看！太陽出來了！', 'Meimei, cepat lihat! Mataharinya terbit!'),
            ('李美美', '好漂亮！', 'Cantik sekali!'),
            ('王大文', '你看那一朵一朵的花！多麼漂亮啊！', 'Lihat bunga-bunga itu! Betapa cantiknya!'),
            ('李美美', '臺灣每個季節都有不同的花。', 'Di Taiwan setiap musim ada bunga yang berbeda.'),
            ('王大文', '那我們每個季節都來吧！', 'Kalau begitu kita datang setiap musim!'),
        ]),
    ]),
    'C55': ('Dawen belajar memilah sampah di Taiwan: kertas dan botol harus dipisah. Ia lalu membandingkan masalah '
            'sampah di Indonesia dan Taiwan, dan ingin menularkan kebiasaan ini sepulang nanti.', [
        ('在大文家門口', 'Di depan rumah Dawen', [
            ('王大文', '美美，這個袋子裡的垃圾，不是紙，就是瓶子。都放在一起可以嗎？', 'Meimei, sampah di kantong ini kalau bukan kertas, ya botol. Boleh dicampur?'),
            ('李美美', '不行，紙和瓶子要放在不同的地方。', 'Tidak boleh, kertas dan botol harus ditaruh di tempat berbeda.'),
            ('王大文', '為什麼？', 'Kenapa?'),
            ('李美美', '為了環保。垃圾太多，會污染環境。', 'Demi lingkungan. Sampah terlalu banyak akan mencemari lingkungan.'),
            ('王大文', '在印尼，很多人很自由地丟垃圾……', 'Di Indonesia, banyak orang membuang sampah seenaknya…'),
            ('李美美', '在臺灣不行，連一個小瓶子都要放對地方。', 'Di Taiwan tidak boleh, bahkan satu botol kecil pun harus ditaruh di tempat yang benar.'),
        ]),
        ('在學校', 'Di kampus', [
            ('王大文', '印尼的垃圾問題很嚴重，連海邊都有很多垃圾。', 'Masalah sampah di Indonesia serius, bahkan di pantai pun banyak sampah.'),
            ('李美美', '臺灣以前也是。', 'Taiwan dulu juga begitu.'),
            ('王大文', '現在呢？', 'Sekarang?'),
            ('李美美', '現在社會上大家都很注意環保。', 'Sekarang semua orang di masyarakat sangat memperhatikan lingkungan.'),
            ('王大文', '我回印尼以後，也要告訴大家怎麼做！', 'Setelah pulang ke Indonesia, aku juga mau memberi tahu orang-orang caranya!'),
        ]),
    ]),
    'C56': ('Meimei menjelaskan tradisi malam Tahun Baru Imlek di keluarganya: hidangan khas dan siapa yang makan '
            'duluan. Dawen bercerita tentang perayaan di Indonesia, lalu Meimei mengundangnya.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，春節是臺灣最重要的節日嗎？', 'Meimei, Imlek itu hari raya paling penting di Taiwan?'),
            ('李美美', '對！除夕晚上，一家人一起吃晚飯。', 'Iya! Malam Tahun Baru, sekeluarga makan malam bersama.'),
            ('王大文', '你們吃什麼？', 'Kalian makan apa?'),
            ('李美美', '魚、雞、青菜等等，都是傳統的中式菜。', 'Ikan, ayam, sayuran, dan lain-lain, semuanya masakan Tionghoa tradisional.'),
            ('王大文', '誰先吃？', 'Siapa yang makan duluan?'),
            ('李美美', '我們家誰先到，誰就先吃！', 'Di keluargaku, siapa yang datang duluan, dia yang makan duluan!'),
            ('王大文', '真有意思！', 'Menarik sekali!'),
            ('李美美', '你們在印尼過春節嗎？', 'Di Indonesia kalian merayakan Imlek?'),
            ('王大文', '我家也過。東方的節日我們過，我們也有聖誕老人。', 'Keluargaku juga merayakan. Hari raya Timur kami rayakan, kami juga punya Sinterklas.'),
            ('李美美', '今年除夕，你來我家吧！', 'Malam Tahun Baru tahun ini, datang ke rumahku saja!'),
            ('王大文', '真的嗎？那我要帶什麼？', 'Serius? Lalu aku perlu bawa apa?'),
            ('李美美', '什麼都不用帶！你想吃什麼，我們就做什麼！', 'Tidak perlu bawa apa-apa! Kamu mau makan apa, itu yang kami masak!'),
        ]),
    ]),
    'C57': ('Menjelang ujian dan tenggat laporan, Dawen cemas di perpustakaan. Meimei menenangkannya, menjelaskan bahwa '
            'perasaan itu wajar, dan menyarankan bertanya langsung kepada guru.', [
        ('在圖書館', 'Di perpustakaan', [
            ('李美美', '大文，你怎麼了？你看起來很擔心。', 'Dawen, kenapa kamu? Kamu kelihatan cemas.'),
            ('王大文', '我不知道明天的考試難不難。', 'Aku tidak tahu ujian besok sulit atau tidak.'),
            ('李美美', '別擔心，你準備得很好，放心吧！', 'Jangan cemas, persiapanmu sudah bagus, tenang saja!'),
            ('王大文', '我不但擔心考試，還擔心報告。', 'Aku bukan cuma cemas soal ujian, tapi juga laporan.'),
            ('李美美', '報告怎麼了？', 'Laporannya kenapa?'),
            ('王大文', '我不知道報告要寫多少字，也不知道老師要什麼。好煩！', 'Aku tidak tahu laporannya harus berapa kata, juga tidak tahu guru maunya apa. Pusing!'),
            ('李美美', '別急。你害怕什麼？', 'Jangan panik. Kamu takut apa?'),
            ('王大文', '我害怕寫得不好。', 'Aku takut tulisanku jelek.'),
            ('李美美', '這個情形很正常，原因是你太認真了！你問老師就知道了。', 'Keadaan begini wajar, sebabnya kamu terlalu serius! Tanya saja guru, nanti tahu.'),
            ('王大文', '好，我現在就去問老師！', 'Oke, sekarang juga aku tanya guru!'),
        ]),
    ]),
    'C58': ('Pesta kejutan ulang tahun Dawen: Meimei dan Annie datang membawa hadiah dan kue. Ujian sudah selesai, '
            'jadi Dawen merasa lega dan sangat bahagia.', [
        ('大文的生日', 'Ulang tahun Dawen', [
            ('李美美', '大文，生日快樂！', 'Dawen, selamat ulang tahun!'),
            ('王大文', '哇，美美！還有安妮！沒想到你們不但來了，而且還帶了禮物！', 'Wah, Meimei! Ada Annie juga! Tidak kusangka kalian bukan cuma datang, tapi juga bawa hadiah!'),
            ('李美美', '今天是你的生日，我們當然要來！', 'Hari ini ulang tahunmu, tentu saja kami datang!'),
            ('王大文', '今天我的心情好得不得了！', 'Hari ini suasana hatiku bagus bukan main!'),
            ('安妮', '大文，你感覺怎麼樣？', 'Dawen, bagaimana perasaanmu?'),
            ('王大文', '考試考完了，很輕鬆，而且很開心！', 'Ujian sudah selesai, lega, dan senang sekali!'),
            ('李美美', '看到你開心，我也很開心。', 'Melihatmu senang, aku juga senang.'),
            ('安妮', '來吃蛋糕吧！這個蛋糕不只好看，而且好吃！', 'Ayo makan kue! Kue ini bukan cuma cantik, tapi juga enak!'),
            ('王大文', '謝謝你們！這是我在臺灣最開心的生日！', 'Terima kasih! Ini ulang tahun paling bahagia selama aku di Taiwan!'),
        ]),
    ]),
    'C59': ('Dawen dan Meimei memilih topik laporan kelompok, saling bertukar pendapat, lalu meminta persetujuan dan '
            'saran guru.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，我們的報告要寫什麼？我有兩個選擇：環保或是交通。', 'Meimei, laporan kita mau menulis apa? Aku punya dua pilihan: lingkungan atau lalu lintas.'),
            ('李美美', '我的看法是寫環保比較好。', 'Menurutku lebih baik menulis tentang lingkungan.'),
            ('王大文', '那麼，你有什麼建議？', 'Kalau begitu, kamu punya saran apa?'),
            ('李美美', '我建議我們先問問老師的意見。', 'Saranku kita tanya pendapat guru dulu.'),
        ]),
        ('在老師的辦公室', 'Di kantor guru', [
            ('王大文', '老師，我們想寫環保。您同意嗎？', 'Bu, kami ingin menulis tentang lingkungan. Ibu setuju?'),
            ('陳老師', '我同意，這個題目很好。', 'Saya setuju, topik ini bagus.'),
            ('李美美', '老師，您願意幫我們看報告嗎？', 'Bu, Ibu bersedia membantu membaca laporan kami?'),
            ('陳老師', '願意。寫完了，拿來給我看。', 'Bersedia. Kalau sudah selesai, bawa ke sini.'),
            ('王大文', '您還有什麼建議？', 'Ibu masih ada saran lain?'),
            ('陳老師', '同樣的字，別用太多次。', 'Kata yang sama jangan dipakai terlalu sering.'),
            ('王大文', '好，謝謝老師！', 'Baik, terima kasih, Bu!'),
        ]),
    ]),
    'C60': ('Meimei bertanya kenapa Dawen pindah dari rumah besar berhalaman. Dawen menjelaskan untung-ruginya tinggal di sana — '
            'tetangga yang bernyanyi tiap malam — dan rumah barunya ternyata dekat kampus.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你本來住在那座大房子，為什麼搬家？', 'Dawen, kamu tadinya tinggal di rumah besar itu, kenapa pindah?'),
            ('王大文', '其實住大房子有好處，也有壞處。', 'Sebenarnya tinggal di rumah besar ada untungnya, ada juga ruginya.'),
            ('李美美', '什麼好處？', 'Untungnya apa?'),
            ('王大文', '好處是很大，也有院子。壞處是房租貴，鄰居也太吵，影響我念書。', 'Untungnya luas dan ada halamannya. Ruginya sewanya mahal, tetangganya juga terlalu berisik, mengganggu belajarku.'),
            ('李美美', '你以前不是說那座房子很好嗎？', 'Bukannya dulu kamu bilang rumah itu bagus?'),
            ('王大文', '本來我也覺得很好，可是後來鄰居每天晚上都唱歌……', 'Awalnya aku juga merasa bagus, tapi kemudian tetangga nyanyi tiap malam…'),
            ('李美美', '我了解了。可惜那個院子很漂亮！', 'Aku mengerti. Sayang sekali, halamannya cantik!'),
            ('王大文', '還好，我的新家離學校很近，走路十分鐘。', 'Untungnya, rumah baruku dekat sekali dengan kampus, jalan kaki sepuluh menit.'),
            ('李美美', '那很好。其實搬家也是很自然的事。', 'Baguslah. Sebenarnya pindah rumah itu hal yang wajar.'),
        ]),
    ]),
    'C62': ('Dawen menjemput Annie di bandara; Annie pulang dari Indonesia membawa barang terlalu banyak. Keesokan '
            'harinya Annie ingin membelikan hadiah terima kasih, tetapi jam tangannya terlalu mahal.', [
        ('在機場', 'Di bandara', [
            ('安妮', '大文，謝謝你來接我！東西太多，我拿不動！', 'Dawen, terima kasih sudah menjemputku! Barangnya terlalu banyak, aku tidak kuat membawanya!'),
            ('王大文', '你帶來了什麼？', 'Kamu bawa apa saja?'),
            ('安妮', '書、衣服，還有很多印尼的點心。', 'Buku, baju, dan banyak kue Indonesia.'),
            ('王大文', '我幫你拿。好重！我也快拿不動了！', 'Aku bantu bawa. Berat sekali! Aku juga hampir tidak kuat!'),
            ('安妮', '我們坐計程車回去吧，我走不動了。', 'Kita naik taksi pulang saja, aku sudah tidak kuat jalan.'),
        ]),
        ('第二天，在百貨公司', 'Keesokan harinya, di department store', [
            ('安妮', '大文，昨天謝謝你。我想買一個禮物給你。', 'Dawen, terima kasih untuk kemarin. Aku ingin membelikanmu hadiah.'),
            ('王大文', '不用了！', 'Tidak usah!'),
            ('安妮', '你看這個手錶，好看嗎？', 'Lihat jam tangan ini, bagus?'),
            ('王大文', '好看，可是三萬塊，太貴了！你買不起，我也買不起。', 'Bagus, tapi tiga puluh ribu, terlalu mahal! Kamu tidak sanggup beli, aku juga tidak.'),
            ('安妮', '那我們去看便宜一點的吧。', 'Kalau begitu kita lihat yang lebih murah.'),
            ('王大文', '其實你帶來的印尼點心，就是最好的禮物！', 'Sebenarnya kue Indonesia yang kamu bawa itulah hadiah terbaik!'),
        ]),
    ]),
    'C65': ('Selesai ujian, Dawen dan Meimei makan di restoran prasmanan sepuasnya. Restoran penuh, piring Dawen '
            'penuh, lalu mereka merencanakan liburan untuk bersenang-senang sepuasnya.', [
        ('在餐廳', 'Di restoran', [
            ('李美美', '大文，這家餐廳是吃到飽的，今天我們吃個夠！', 'Dawen, restoran ini makan sepuasnya, hari ini kita makan sampai puas!'),
            ('王大文', '好！考試考完了，我要吃個夠！', 'Oke! Ujian sudah selesai, aku mau makan sepuasnya!'),
            ('李美美', '你看，餐廳的人好多，位子都坐滿了。', 'Lihat, restorannya ramai sekali, kursinya penuh semua.'),
            ('王大文', '還好我們訂位了。', 'Untung kita sudah pesan tempat.'),
            ('李美美', '你的盤子已經裝滿了！', 'Piringmu sudah penuh!'),
            ('王大文', '對，我要先吃肉，再吃蛋糕。', 'Iya, aku mau makan daging dulu, baru kue.'),
        ]),
        ('吃完以後', 'Selesai makan', [
            ('王大文', '我吃不下了……', 'Aku sudah tidak muat lagi…'),
            ('李美美', '放假了，你想做什麼？', 'Sudah libur, kamu mau ngapain?'),
            ('王大文', '我要玩個夠！', 'Aku mau main sepuasnya!'),
            ('李美美', '我要看電影看個夠！', 'Aku mau nonton film sepuasnya!'),
            ('王大文', '那放假的第一天，我們先去看電影吧！', 'Kalau begitu hari pertama libur, kita nonton film dulu!'),
        ]),
    ]),
    'C66': ('Menjelang ujian akhir, Dawen menanyakan aturan ujian dan pemilihan mata kuliah kepada guru. Lalu ia '
            'mengobrol dengan Meimei di kampus tentang persiapan ujian dan buku sejarah yang belum selesai dibaca.', [
        ('在教室', 'Di kelas', [
            ('王大文', '老師，考試的時候可以查資料嗎？', 'Bu, saat ujian boleh mencari bahan?'),
            ('陳老師', '不可以。考試的時候，你們要帶學生證。', 'Tidak boleh. Saat ujian, kalian harus membawa kartu mahasiswa.'),
            ('王大文', '好。老師，下個學期的課，我還沒選。', 'Baik. Bu, mata kuliah semester depan belum saya pilih.'),
            ('陳老師', '沒關係，你還有時間，星期五以前選就可以。', 'Tidak apa-apa, masih ada waktu, pilih sebelum hari Jumat saja.'),
        ]),
        ('在校園', 'Di kampus', [
            ('李美美', '大文，你考試準備得怎麼樣？', 'Dawen, persiapan ujianmu bagaimana?'),
            ('王大文', '還可以。我這幾天都在圖書館讀書。', 'Lumayan. Beberapa hari ini aku belajar di perpustakaan.'),
            ('李美美', '你還在讀那本歷史書嗎？', 'Kamu masih membaca buku sejarah itu?'),
            ('王大文', '還在讀，快讀完了！', 'Masih, hampir selesai!'),
            ('李美美', '讀完了，我們在校園裡走一走吧，今天天氣很好。', 'Kalau sudah selesai, kita jalan-jalan di kampus yuk, cuaca hari ini bagus.'),
            ('王大文', '好！', 'Oke!'),
        ]),
    ]),
    'C67': ('Dawen memesan bento lewat telepon untuk diantar dalam satu jam. Pesanan yang datang ternyata salah, '
            'tetapi Dawen sedang lapar dan tetap menerimanya.', [
        ('打電話到便當店', 'Menelepon toko bento', [
            ('王大文', '你好，我要一個牛肉便當。', 'Halo, saya pesan satu bento daging sapi.'),
            ('店員', '好。還要別的嗎？', 'Baik. Ada yang lain?'),
            ('王大文', '不要了。一個小時以內送得到嗎？', 'Tidak. Bisa diantar dalam satu jam?'),
            ('店員', '送得到，三十分鐘以內就到。', 'Bisa, dalam tiga puluh menit sudah sampai.'),
            ('王大文', '我家在學校旁邊，中山路二十號。', 'Rumah saya di sebelah kampus, Jalan Zhongshan nomor dua puluh.'),
        ]),
        ('在大文家門口', 'Di depan rumah Dawen', [
            ('店員', '先生，這是你要的便當。', 'Pak, ini bento pesanan Anda.'),
            ('王大文', '不對，我要的是牛肉的，這是雞肉的。', 'Bukan, yang saya pesan daging sapi, ini ayam.'),
            ('店員', '對不起！我整個下午都很忙，拿錯了。', 'Maaf! Saya sibuk sepanjang sore, jadi salah ambil.'),
            ('王大文', '沒關係，我正好很餓，雞肉的也可以。', 'Tidak apa-apa, kebetulan saya lapar, ayam juga boleh.'),
            ('店員', '謝謝你！下次我送你一杯飲料。', 'Terima kasih! Lain kali saya kasih bonus satu minuman.'),
        ]),
    ]),
}
