"""Data 情境對話 berbasis cerita Vol.1/A0 (keputusan Carli 2026-10-26; dipakai oleh dialog_cerita.py).

Format sama dengan BARU di dialog_cerita.py. Dialog yang dulu diedit Carli (A01–A08, A11, A12, A14, A15) TIDAK
ditulis ulang — hanya 13 bab di bawah. Di A0 belum ada 了, 在+tempat+V, 過, V得, 比 (kecuali bacaan A19), 太…了,
是…的, 一…就; kata 回 (B30), 遠/近 (B29), 一起 & 昨天/明天 (A11), 上課/學校 (A12), 可以 (A14), 杯子 (A15),
東西 (A18), 手機/朋友 (A25) dipakai hanya mulai babnya.
"""

BARU = {
    'A09': ('Lanjutan kunjungan Meimei ke rumah Dawen. Mereka mau menonton film di kamar Dawen, lalu '
            'mencari adik perempuan Dawen, Xiaowen, yang sedang bersembunyi.', [
        ('在大文的房間', 'Di kamar Dawen', [
            ('李美美', '大文，你的房間很大！桌子上有電視！', 'Dawen, kamarmu besar sekali! Di atas meja ada televisi!'),
            ('王大文', '我們看電影！你拿椅子。', 'Ayo kita nonton film! Kamu ambil kursi.'),
            ('李美美', '好。椅子在哪裡？', 'Oke. Kursinya di mana?'),
            ('王大文', '在床旁邊。椅子在電視前面，好嗎？', 'Di samping tempat tidur. Kursinya di depan televisi, ya?'),
            ('李美美', '好！你妹妹也喜歡看電影嗎？', 'Oke! Adikmu juga suka nonton film?'),
            ('王大文', '喜歡。小文！小文！……她在哪裡？', 'Suka. Xiaowen! Xiaowen! …Dia di mana?'),
        ]),
        ('小文在哪裡？', 'Xiaowen di mana?', [
            ('李美美', '她在床下嗎？', 'Dia di bawah tempat tidur?'),
            ('王大文', '不在床下。', 'Tidak ada di bawah tempat tidur.'),
            ('李美美', '在門後嗎？', 'Di belakang pintu?'),
            ('王大文', '也不在門後。', 'Di belakang pintu juga tidak ada.'),
            ('李美美', '你看，桌子下有一個人！', 'Lihat, di bawah meja ada orang!'),
            ('王大文', '小文！你在桌子下！', 'Xiaowen! Kamu di bawah meja!'),
            ('李美美', '你妹妹很喜歡玩！', 'Adikmu suka sekali bermain!'),
        ]),
    ]),
    'A10': ('Dawen datang terlambat dan mengantuk karena setiap hari tidur jam dua pagi. Meimei mengajaknya '
            'berolahraga pagi, dan keesokan paginya Dawen benar-benar datang ke taman.', [
        ('早上，在教室', 'Pagi hari, di kelas', [
            ('李美美', '大文，你好晚！現在九點二十分。', 'Dawen, kamu telat sekali! Sekarang jam sembilan lewat dua puluh.'),
            ('王大文', '我八點半起床。', 'Aku bangun jam setengah sembilan.'),
            ('李美美', '你每天晚上幾點睡覺？', 'Setiap malam kamu tidur jam berapa?'),
            ('王大文', '兩點。我晚上喜歡看電影。', 'Jam dua. Malam hari aku suka nonton film.'),
            ('李美美', '兩點？太晚！我每天晚上十一點睡覺，早上六點半起床。', 'Jam dua? Terlalu malam! Setiap malam aku tidur jam sebelas, pagi bangun jam setengah tujuh.'),
            ('王大文', '你好早！你早上做什麼？', 'Pagi sekali! Pagi-pagi kamu ngapain?'),
            ('李美美', '我早上運動。你也早上運動！', 'Pagi hari aku olahraga. Kamu juga olahraga pagi!'),
            ('王大文', '好！', 'Oke!'),
        ]),
        ('早上六點半，在公園', 'Jam setengah tujuh pagi, di taman', [
            ('李美美', '大文！你好早！', 'Dawen! Pagi sekali kamu!'),
            ('王大文', '我六點起床！', 'Aku bangun jam enam!'),
            ('李美美', '好！現在我們運動！', 'Bagus! Sekarang kita olahraga!'),
            ('王大文', '……美美，現在幾點？我想睡覺！', '…Meimei, sekarang jam berapa? Aku ngantuk!'),
            ('李美美', '現在六點四十分！你晚上要早睡覺！', 'Sekarang jam enam lewat empat puluh! Malam hari kamu harus tidur lebih awal!'),
        ]),
    ]),
    'A13': ('Dawen dan Meimei tidak mengerti sebuah kalimat di buku. Mereka menyiapkan pena dan kertas, lalu '
            'bertanya kepada Guru Chen cara menulis dan arti sebuah huruf.', [
        ('下課的時候', 'Saat istirahat', [
            ('王大文', '美美，這個句子是什麼意思？', 'Meimei, kalimat ini artinya apa?'),
            ('李美美', '我看……我不懂。這個字我不知道。', 'Coba kulihat… aku tidak mengerti. Huruf ini aku tidak tahu.'),
            ('王大文', '我們問老師吧。', 'Kita tanya guru saja.'),
            ('李美美', '好。你有筆和紙嗎？', 'Oke. Kamu punya pena dan kertas?'),
            ('王大文', '有，我有兩枝筆。你用這枝。', 'Ada, aku punya dua pena. Kamu pakai yang ini.'),
        ]),
        ('問老師', 'Bertanya kepada guru', [
            ('王大文', '老師，我們有問題。這個字怎麼寫？', 'Bu, kami punya pertanyaan. Huruf ini ditulis bagaimana?'),
            ('陳老師', '你們看這張紙，我寫。這是「書」。', 'Lihat kertas ini, saya tuliskan. Ini "書".'),
            ('李美美', '「書」是什麼意思？', '"書" artinya apa?'),
            ('陳老師', '你看，這是一本書。', 'Lihat, ini sebuah buku.'),
            ('王大文', '懂！謝謝老師。', 'Mengerti! Terima kasih, Bu.'),
            ('陳老師', '不懂，你們再問我。', 'Kalau tidak mengerti, tanya saya lagi.'),
        ]),
    ]),
    'A16': ('Jam dua belas siang Dawen lapar sekali karena tidak pernah sarapan. Mereka makan siang bersama, dan '
            'Dawen makan begitu banyak sampai tidak mau memikirkan makan malam.', [
        ('中午十二點', 'Jam dua belas siang', [
            ('王大文', '美美，我很餓！我們去吃午餐吧。', 'Meimei, aku lapar sekali! Ayo kita makan siang.'),
            ('李美美', '好！你不吃早餐嗎？', 'Oke! Kamu tidak sarapan?'),
            ('王大文', '我早上不餓，我不吃早餐。', 'Pagi hari aku tidak lapar, aku tidak sarapan.'),
            ('李美美', '你應該吃早餐！我早餐吃蛋，喝牛奶。', 'Kamu harus sarapan! Aku sarapan telur dan minum susu.'),
        ]),
        ('吃午餐', 'Makan siang', [
            ('李美美', '你想吃什麼？', 'Kamu mau makan apa?'),
            ('王大文', '我想吃雞肉和飯。你呢？', 'Aku mau makan ayam dan nasi. Kamu?'),
            ('李美美', '我不吃肉，我吃魚和菜，也喝湯。', 'Aku tidak makan daging, aku makan ikan dan sayur, juga minum sup.'),
            ('王大文', '……我很飽！', '…Aku kenyang sekali!'),
            ('李美美', '晚餐你想吃什麼？', 'Makan malam kamu mau makan apa?'),
            ('王大文', '晚餐？我現在很飽，不想吃！', 'Makan malam? Sekarang aku kenyang sekali, tidak mau makan!'),
            ('李美美', '晚上你一定很餓！', 'Nanti malam kamu pasti lapar sekali!'),
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
            ('王大文', '好吃！臺灣的小吃很好吃，我也喜歡臺灣的麵包。', 'Enak! Jajanan Taiwan enak, aku juga suka roti Taiwan.'),
            ('李美美', '別吃太快！我吃飯很慢。', 'Jangan makan terlalu cepat! Aku makannya pelan.'),
            ('王大文', '這個餐廳很好。明天我們跟陳老師一起去吧！', 'Restoran ini bagus. Besok kita ke sini bersama Guru Chen ya!'),
        ]),
    ]),
    'A18': ('Sebelum ujian Dawen membeli pena di toko dekat kampus: menanyakan harga, memilih yang murah, membayar, '
            'dan menerima kembalian. Di luar toko ia bercerita kepada Meimei.', [
        ('在店裡', 'Di dalam toko', [
            ('王大文', '先生，請問這枝筆多少錢？', 'Pak, permisi, pena ini berapa?'),
            ('老闆', '這枝一百二十塊。', 'Yang ini seratus dua puluh.'),
            ('王大文', '好貴！那枝呢？', 'Mahal sekali! Kalau yang itu?'),
            ('老闆', '那枝便宜，八十塊。', 'Yang itu murah, delapan puluh.'),
            ('王大文', '我買兩枝。一共多少錢？', 'Saya beli dua. Totalnya berapa?'),
            ('老闆', '一共一百六十塊。', 'Totalnya seratus enam puluh.'),
            ('王大文', '給你兩百塊。', 'Ini dua ratus.'),
            ('老闆', '找你四十塊。謝謝！', 'Kembaliannya empat puluh. Terima kasih!'),
        ]),
        ('在店門口', 'Di depan toko', [
            ('李美美', '大文，你買什麼東西？', 'Dawen, kamu beli apa?'),
            ('王大文', '我買兩枝筆和紙。明天考試！', 'Aku beli dua pena dan kertas. Besok ujian!'),
            ('李美美', '這個店的東西貴嗎？', 'Barang di toko ini mahal?'),
            ('王大文', '一些東西很貴，筆很便宜。我只買便宜的！', 'Beberapa barang mahal, penanya murah. Aku cuma beli yang murah!'),
            ('李美美', '你的錢夠嗎？', 'Uangmu cukup?'),
            ('王大文', '夠！', 'Cukup!'),
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
            ('李美美', '你看，這個白的很好看。', 'Lihat, yang putih ini bagus.'),
            ('王大文', '好看，可是很貴！', 'Bagus, tapi mahal!'),
            ('李美美', '那個黑的比這個便宜。', 'Yang hitam itu lebih murah daripada ini.'),
            ('王大文', '好，我買黑的！', 'Oke, aku beli yang hitam!'),
        ]),
    ]),
    'A20': ('Dawen dan Meimei bercerita cara mereka pergi ke kampus, lalu Meimei menjelaskan bagaimana ia pulang '
            'ke rumah orang tuanya di Taichung.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你每天怎麼來學校？', 'Dawen, setiap hari kamu ke kampus naik apa?'),
            ('王大文', '我坐公車來。公車站在我家門口。你呢？', 'Aku naik bus. Halte busnya di depan rumahku. Kamu?'),
            ('李美美', '我住在學校附近，我走路來學校。', 'Aku tinggal di dekat kampus, aku jalan kaki ke kampus.'),
            ('王大文', '走路很方便！', 'Jalan kaki praktis sekali!'),
        ]),
        ('說去臺中', 'Membicarakan perjalanan ke Taichung', [
            ('王大文', '美美，你爸爸媽媽在臺中，你怎麼去臺中？', 'Meimei, orang tuamu di Taichung, kamu ke Taichung naik apa?'),
            ('李美美', '我坐火車去。因為火車很快，所以我坐火車。', 'Aku naik kereta. Karena kereta cepat, jadi aku naik kereta.'),
            ('王大文', '你不坐飛機嗎？', 'Kamu tidak naik pesawat?'),
            ('李美美', '不坐。有時候我爸爸開車來臺北，我坐他的車子去臺中。', 'Tidak. Kadang-kadang ayahku menyetir ke Taipei, aku ikut mobilnya ke Taichung.'),
            ('王大文', '我爸爸也有一輛車子。我不坐計程車，計程車很貴！', 'Ayahku juga punya satu mobil. Aku tidak naik taksi, taksi mahal!'),
        ]),
    ]),
    'A21': ('Dawen dan Meimei mau naik kereta ke Taichung, tetapi tidak tahu jalan ke stasiun. Mereka bertanya kepada '
            'seorang bapak, lalu sempat salah jalan lagi sebelum akhirnya melihat stasiun.', [
        ('在路上', 'Di jalan', [
            ('王大文', '先生，請問，火車站怎麼走？', 'Pak, permisi, ke stasiun kereta lewat mana?'),
            ('先生', '你們從這裡出去，走右邊的路。', 'Dari sini kalian keluar, lewat jalan sebelah kanan.'),
            ('王大文', '右邊？', 'Sebelah kanan?'),
            ('先生', '對，走五分鐘就到。火車站在路的左邊。', 'Iya, jalan lima menit langsung sampai. Stasiunnya di sebelah kiri jalan.'),
            ('王大文', '謝謝您！', 'Terima kasih, Pak!'),
        ]),
        ('十分鐘以後', 'Sepuluh menit kemudian', [
            ('李美美', '大文，你看到火車站嗎？', 'Dawen, kamu lihat stasiunnya?'),
            ('王大文', '火車站在哪裡？我們又走錯路！', 'Stasiunnya di mana? Kita salah jalan lagi!'),
            ('李美美', '這是什麼地方？', 'Ini tempat apa?'),
            ('王大文', '我不知道。……你看，我看見火車站！在那裡，左邊！', 'Aku tidak tahu. …Lihat, aku lihat stasiunnya! Di sana, sebelah kiri!'),
            ('李美美', '好，我們馬上去！', 'Oke, kita langsung ke sana!'),
        ]),
    ]),
    'A22': ('Dawen merasa tidak enak badan di kampus: kepala, mata, dan hidungnya tidak nyaman. Saat istirahat ia '
            'makin lemas, sampai tidak bisa mendengar Meimei dengan jelas.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你今天怎麼樣？', 'Dawen, hari ini kamu bagaimana?'),
            ('王大文', '我不舒服，我頭很痛。', 'Aku tidak enak badan, kepalaku sakit sekali.'),
            ('李美美', '你感冒嗎？', 'Kamu masuk angin?'),
            ('王大文', '可能是。我很累，眼睛也很痛。', 'Mungkin. Aku capek sekali, mataku juga sakit.'),
            ('李美美', '鼻子呢？', 'Hidungmu?'),
            ('王大文', '鼻子也不舒服。', 'Hidungku juga tidak enak.'),
        ]),
        ('下課的時候', 'Saat istirahat', [
            ('李美美', '大文，你的身體怎麼樣？', 'Dawen, badanmu bagaimana?'),
            ('王大文', '很不好。我的手和腳都很累。', 'Tidak baik. Tangan dan kakiku lemas semua.'),
            ('李美美', '你生病！你應該去睡覺。', 'Kamu sakit! Kamu harus tidur.'),
            ('王大文', '什麼？我沒聽見。我的耳朵也不舒服！', 'Apa? Aku tidak dengar. Telingaku juga tidak enak!'),
            ('李美美', '我說：你應該去睡覺！', 'Kubilang: kamu harus tidur!'),
        ]),
    ]),
    'A23': ('Dawen masih sakit tetapi bilang tidak apa-apa. Meimei membujuknya memberi tahu guru dan pergi ke dokter; '
            'dokter memberinya obat dan menyuruhnya istirahat.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你應該去看病！', 'Dawen, kamu harus pergi berobat!'),
            ('王大文', '為什麼？我沒事。', 'Kenapa? Aku tidak apa-apa.'),
            ('李美美', '你頭痛，眼睛也痛。你生病，大家都很怕！', 'Kepalamu sakit, matamu juga sakit. Kamu sakit, semua orang khawatir!'),
            ('王大文', '好，我自己告訴老師。你等我，我們一起去看病。', 'Baiklah, aku sendiri yang memberi tahu guru. Tunggu aku, kita pergi berobat bersama.'),
        ]),
        ('看醫生', 'Ke dokter', [
            ('醫生', '你好，你哪裡不舒服？', 'Halo, bagian mana yang tidak enak?'),
            ('王大文', '醫生，我頭痛，也很累。', 'Dokter, kepala saya sakit, juga capek sekali.'),
            ('醫生', '你是感冒。你應該多休息，多喝水。', 'Kamu masuk angin. Kamu harus banyak istirahat dan banyak minum air.'),
            ('醫生', '這是藥，早上、中午、晚上吃。', 'Ini obatnya, diminum pagi, siang, dan malam.'),
            ('王大文', '謝謝醫生！', 'Terima kasih, Dokter!'),
            ('李美美', '大文，今天你應該休息，別看電影！', 'Dawen, hari ini kamu harus istirahat, jangan nonton film!'),
            ('王大文', '好，我去睡覺！', 'Oke, aku tidur!'),
        ]),
    ]),
    'A24': ('Hari yang panas sekali. Meimei mengajak Dawen ke gunung yang udaranya segar; keesokan harinya di gunung '
            'angin bertiup kencang dan tiba-tiba hujan turun.', [
        ('在學校外面', 'Di luar kampus', [
            ('王大文', '今天好熱！', 'Hari ini panas sekali!'),
            ('李美美', '對，臺灣的天氣很熱。印尼熱不熱？', 'Iya, cuaca Taiwan panas sekali. Indonesia panas tidak?'),
            ('王大文', '印尼也很熱。', 'Indonesia juga panas sekali.'),
            ('李美美', '明天我們一起去山上吧！山上不熱，空氣也很好。', 'Besok kita ke gunung yuk! Di gunung tidak panas, udaranya juga segar.'),
            ('王大文', '好！明天下雨嗎？', 'Oke! Besok hujan?'),
            ('李美美', '不下雨。', 'Tidak hujan.'),
        ]),
        ('第二天，在山上', 'Keesokan harinya, di gunung', [
            ('王大文', '山上好冷！風很大！', 'Di gunung dingin sekali! Anginnya kencang sekali!'),
            ('李美美', '對，山上很冷，山下很熱。', 'Iya, di gunung dingin, di bawah panas.'),
            ('王大文', '你看，山上的花很漂亮！', 'Lihat, bunga-bunga di gunung cantik sekali!'),
            ('李美美', '這個山不高，很低，可是我最喜歡這個山。', 'Gunung ini tidak tinggi, rendah, tapi aku paling suka gunung ini.'),
            ('王大文', '……美美，下雨！你說不下雨！', '…Meimei, hujan! Katamu tidak hujan!'),
            ('李美美', '我們快走路下山吧！', 'Ayo cepat kita jalan turun gunung!'),
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
