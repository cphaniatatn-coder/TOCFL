"""Data 情境對話 berbasis cerita Vol.2/A1 (keputusan Carli 2026-10-23; dipakai oleh dialog_cerita.py).

Format sama dengan BARU di dialog_cerita.py: kode → (scene Indonesia, [(tempat, judul Indonesia, [(pembicara, zh, id)])]).
Catatan urutan grammar A1: 了 baru B09, 在 + tempat + V baru B08, V得 B15, 比 B19, 太…了 B20, 有(一)點 B20,
是…的 B33, 一…就 B34 — bab sebelumnya menghindarinya.
"""

BARU = {
    'B04': ('Malam hari Meimei mengerjakan PR dari situs web guru, tetapi internet di rumahnya lambat. Ia menelepon '
            'Dawen yang sedang online, lalu baterai ponselnya hampir habis; mereka melanjutkan obrolan sebentar lagi.', [
        ('晚上，打電話', 'Malam hari, menelepon', [
            ('李美美', '喂，大文，你在做什麼呢？', 'Halo, Dawen, kamu lagi ngapain?'),
            ('王大文', '我在上網呢。你呢？', 'Aku lagi internetan. Kamu?'),
            ('李美美', '我在寫功課，可是最近我家的網路很慢，我不能上老師的網站。', 'Aku lagi mengerjakan PR, tapi belakangan internet di rumahku lambat, aku tidak bisa membuka situs guru.'),
            ('王大文', '我正在看老師的網站呢。你要看哪個問題？', 'Aku sedang buka situs guru. Kamu mau lihat pertanyaan yang mana?'),
            ('李美美', '第三個。', 'Yang ketiga.'),
            ('王大文', '等一下……第三個問題是：「你最近在做什麼？」', 'Sebentar… Pertanyaan ketiga: "Belakangan ini kamu sedang sibuk apa?"'),
            ('李美美', '啊，這個我會！謝謝你！', 'Ah, yang ini aku bisa! Terima kasih!'),
            ('李美美', '啊，我的手機快沒電啦！我們一會兒再聊吧。', 'Aduh, baterai HP-ku hampir habis! Nanti kita ngobrol lagi ya.'),
            ('王大文', '好啊，一會兒再打給我。', 'Oke, nanti telepon aku lagi.'),
        ]),
        ('十點，美美又打電話', 'Jam sepuluh, Meimei menelepon lagi', [
            ('李美美', '喂，大文，你還在上網嗎？', 'Halo, Dawen, kamu masih internetan?'),
            ('王大文', '沒有，我在跟志明聊天呢。你的功課呢？', 'Tidak, aku lagi ngobrol dengan Zhiming. PR-mu bagaimana?'),
            ('李美美', '都會啦！老師的問題很容易。', 'Sudah bisa semua! Pertanyaan guru gampang.'),
            ('王大文', '真好！志明說，他的功課還有很多呀！', 'Enak sekali! Kata Zhiming, PR-nya masih banyak!'),
            ('李美美', '那你們不要聊天啦，快去寫功課吧！', 'Kalau begitu kalian jangan ngobrol terus, cepat kerjakan PR!'),
        ]),
    ]),
    'B06': ('Pesta penyambutan mahasiswa internasional. Annie baru datang dan belum mengenal siapa pun; Meimei '
            'memperkenalkannya kepada Dawen yang juga dari Indonesia, lalu mereka berkenalan dengan keluarga guru.', [
        ('在歡迎會', 'Di pesta penyambutan', [
            ('李美美', '你好，你是新同學嗎？歡迎你！', 'Halo, kamu mahasiswa baru? Selamat datang!'),
            ('安妮', '對，我叫安妮。很高興認識你！', 'Iya, namaku Annie. Senang berkenalan denganmu!'),
            ('李美美', '我叫美美，我也很高興認識你。今天有各國的學生，也有老師們。', 'Aku Meimei, aku juga senang berkenalan. Hari ini ada mahasiswa dari berbagai negara, juga para guru.'),
            ('安妮', '人很多，可是我不認識別人。', 'Orangnya banyak, tapi aku tidak kenal yang lain.'),
            ('李美美', '沒關係！你是哪國人？', 'Tidak apa-apa! Kamu orang mana?'),
            ('安妮', '我是印尼人。', 'Aku orang Indonesia.'),
            ('李美美', '那邊的大文也是印尼人！大文，這是安妮。', 'Dawen di sana juga orang Indonesia! Dawen, ini Annie.'),
            ('王大文', '你好！你也是印尼人嗎？我是雅加達人。', 'Halo! Kamu juga orang Indonesia? Aku dari Jakarta.'),
            ('安妮', '我也是雅加達人！很高興見到你。', 'Aku juga dari Jakarta! Senang bertemu denganmu.'),
            ('王大文', '我們的同學們都很好，你可以交很多朋友。', 'Teman-teman kita semuanya baik, kamu bisa punya banyak teman.'),
        ]),
        ('陳老師的家人', 'Keluarga Guru Chen', [
            ('安妮', '那邊的大人和小朋友們是誰？', 'Orang dewasa dan anak-anak di sana siapa?'),
            ('王大文', '他們是陳老師的家人。那個老人是老師的爸爸。', 'Mereka keluarga Guru Chen. Kakek itu ayah guru.'),
            ('李美美', '老師的爸爸很喜歡跟年輕人聊天。我們也去吧！', 'Ayah guru suka sekali ngobrol dengan anak muda. Ayo kita ke sana juga!'),
            ('陳老師', '安妮，歡迎你！這是我爸爸，這兩個是我的兒子。', 'Annie, selamat datang! Ini ayah saya, dua anak ini anak laki-laki saya.'),
            ('安妮', '老先生好！小朋友們好！', 'Selamat sore, Pak! Halo, adik-adik!'),
            ('陳老師', '其他的新同學呢？', 'Mahasiswa baru yang lain di mana?'),
            ('李美美', '他們在那邊跟大家聊天呢。安妮今天也認識很多新朋友！', 'Mereka lagi ngobrol dengan semua orang di sana. Annie hari ini juga kenalan dengan banyak teman baru!'),
            ('安妮', '對，我今天很高興！老先生，我們下次見面再聊吧！', 'Iya, hari ini aku senang sekali! Kakek, lain kali kita bertemu dan mengobrol lagi ya!'),
        ]),
    ]),
    'B08': ('Meimei pertama kali datang ke apartemen baru Dawen di lantai tujuh. Lift-nya tidak bisa dipakai, dan '
            'di dalam rumah jendela, AC, dan lampu ternyata menyala semua karena teman sekamarnya lupa.', [
        ('在大樓樓下', 'Di lantai bawah gedung', [
            ('李美美', '大文，你家在幾樓？', 'Dawen, rumahmu di lantai berapa?'),
            ('王大文', '在七樓。可是今天電梯不能坐，我們走樓梯吧。', 'Di lantai tujuh. Tapi hari ini lift-nya tidak bisa dipakai, kita naik tangga saja.'),
            ('李美美', '七樓！好高啊！你家樓上還有人嗎？', 'Lantai tujuh! Tinggi sekali! Di atas rumahmu masih ada orang?'),
            ('王大文', '有，樓上住著一個老先生。他每天都走樓梯！', 'Ada, di lantai atas tinggal seorang kakek. Dia setiap hari naik tangga!'),
        ]),
        ('在大文家', 'Di rumah Dawen', [
            ('李美美', '你看，窗戶開著，冷氣也開著！', 'Lihat, jendelanya terbuka, AC-nya juga menyala!'),
            ('王大文', '燈也開著！家裡沒有人啊！', 'Lampunya juga menyala! Di rumah tidak ada orang!'),
            ('李美美', '是你的室友嗎？', 'Teman sekamarmu, ya?'),
            ('王大文', '對，志明早上很忙。', 'Iya, Zhiming pagi-pagi sibuk.'),
            ('李美美', '這是書房嗎？', 'Ini ruang belajar?'),
            ('王大文', '對，我晚上常常在書房看書。洗手間在書房對面。', 'Iya, malam hari aku sering membaca di ruang belajar. Toiletnya di seberang ruang belajar.'),
            ('李美美', '我想喝水。冰箱在哪裡？', 'Aku mau minum. Kulkasnya di mana?'),
            ('王大文', '在飯廳，在桌子和窗戶中間。', 'Di ruang makan, di antara meja dan jendela.'),
            ('李美美', '冷氣開著，可是還很熱！', 'AC-nya menyala, tapi masih panas!'),
            ('王大文', '窗戶也開著啊！', 'Jendelanya juga terbuka!'),
            ('王大文', '我們去樓下的咖啡店坐一下吧。', 'Kita duduk sebentar di kedai kopi di bawah saja yuk.'),
            ('李美美', '好！我們坐電梯吧。', 'Oke! Kita naik lift ya.'),
            ('王大文', '電梯今天不能坐啊！', 'Lift-nya hari ini kan tidak bisa dipakai!'),
        ]),
    ]),
    'B13': ('Dawen mendaftar kelas tenis kampus. Petugas memintanya mengisi formulir: alamat, nomor telepon, umur, '
            'dan foto. Besoknya ia bercerita kepada Meimei tentang kelas itu.', [
        ('在學校辦公室', 'Di kantor kampus', [
            ('小姐', '你好，你要參加網球課嗎？', 'Halo, kamu mau ikut kelas tenis?'),
            ('王大文', '對。請問要寫什麼？', 'Iya. Permisi, apa saja yang harus ditulis?'),
            ('小姐', '請寫你的名字、地址和電話號碼。', 'Silakan tulis nama, alamat, dan nomor telepon.'),
            ('王大文', '我住在臺北市中山路二十號。要寫幾樓嗎？', 'Saya tinggal di Jalan Zhongshan nomor dua puluh, Kota Taipei. Perlu ditulis lantai berapa?'),
            ('小姐', '要，全部都要寫。你的手機號碼是多少？', 'Perlu, semuanya harus ditulis. Nomor HP-mu berapa?'),
            ('王大文', '零九一二、三四五、六七八。', 'Nol sembilan satu dua, tiga empat lima, enam tujuh delapan.'),
            ('小姐', '好。你今年幾歲？', 'Baik. Tahun ini umurmu berapa?'),
            ('王大文', '二十歲。', 'Dua puluh tahun.'),
            ('小姐', '這張照片是你嗎？樣子很不一樣！', 'Foto ini kamu? Tampangnya beda sekali!'),
            ('王大文', '是我，那是我十多歲的照片。', 'Itu saya, itu foto waktu saya belasan tahun.'),
        ]),
        ('第二天，在學校', 'Keesokan harinya, di kampus', [
            ('李美美', '大文，網球課有多少人？', 'Dawen, kelas tenisnya berapa orang?'),
            ('王大文', '三十多個人。所有的人都是我們學校的學生。', 'Tiga puluhan orang. Semuanya mahasiswa kampus kita.'),
            ('李美美', '一個星期上幾次課？', 'Seminggu berapa kali pertemuan?'),
            ('王大文', '兩次，一次一個多小時。', 'Dua kali, sekali lebih dari satu jam.'),
            ('李美美', '網球課的人全部都是外國人嗎？', 'Peserta kelas tenis semuanya orang asing?'),
            ('王大文', '不是，二十多個是臺灣人。', 'Bukan, dua puluhan orang Taiwan.'),
            ('李美美', '很好！我會打網球，我們可以一起打！', 'Bagus! Aku bisa main tenis, kita bisa main bersama!'),
        ]),
    ]),
    'B19': ('Musim dingin di Taipei. Suara Dawen serak karena masuk angin; ia membandingkan dinginnya Taipei dengan '
            'Jakarta, lalu Meimei mengajaknya ke Kaohsiung di selatan yang lebih hangat.', [
        ('冬天，在學校', 'Musim dingin, di kampus', [
            ('李美美', '大文，你的聲音怎麼跟平常不一樣？', 'Dawen, suaramu kenapa beda dari biasanya?'),
            ('王大文', '我感冒了。臺北的冬天比雅加達冷！', 'Aku masuk angin. Musim dingin di Taipei lebih dingin daripada Jakarta!'),
            ('李美美', '雅加達沒有冬天啊！今天比昨天更冷。', 'Jakarta kan tidak ada musim dingin! Hari ini lebih dingin daripada kemarin.'),
            ('王大文', '臺中也跟臺北一樣冷嗎？', 'Taichung juga sama dinginnya dengan Taipei?'),
            ('李美美', '不一樣。臺北在北部，臺中在臺北的南邊，比較不冷。', 'Tidak sama. Taipei di bagian utara, Taichung di sebelah selatan Taipei, tidak terlalu dingin.'),
        ]),
        ('看地圖', 'Melihat peta', [
            ('王大文', '我想去比較熱的地方。', 'Aku ingin pergi ke tempat yang lebih hangat.'),
            ('李美美', '那我們去高雄吧！高雄在臺灣的南邊，比臺中更熱。', 'Kalau begitu kita ke Kaohsiung saja! Kaohsiung di selatan, lebih hangat daripada Taichung.'),
            ('王大文', '高雄跟雅加達一樣熱嗎？', 'Kaohsiung sama panasnya dengan Jakarta?'),
            ('李美美', '不一樣！雅加達是世界上很熱的地方。', 'Tidak sama! Jakarta itu salah satu tempat yang panas di dunia.'),
            ('王大文', '對，可是我現在很想雅加達的天氣！', 'Iya, tapi sekarang aku kangen sekali cuaca Jakarta!'),
            ('李美美', '週末我們坐火車去高雄。臺灣的東邊也很漂亮，下次再去。', 'Akhir pekan kita naik kereta ke Kaohsiung. Bagian timur juga indah, lain kali kita ke sana.'),
        ]),
    ]),
    'B24': ('Besok ulang tahun Zhiming. Dawen dan Meimei membeli kue yang tidak terlalu manis; di pesta, Zhiming '
            'membalas dengan camilan khas Taiwan yang baunya menyengat.', [
        ('在甜點店', 'Di toko kue', [
            ('王大文', '美美，明天是志明的生日，我想買一個蛋糕。', 'Meimei, besok ulang tahun Zhiming, aku mau beli kue.'),
            ('李美美', '這家店的蛋糕又香又好吃。', 'Kue di toko ini harum dan enak.'),
            ('王大文', '可是志明不喜歡很甜的東西。', 'Tapi Zhiming tidak suka yang terlalu manis.'),
            ('店員', '這個蛋糕不太甜，糖很少。', 'Kue ini tidak terlalu manis, gulanya sedikit.'),
            ('王大文', '好，我要這個。美美，你喜歡什麼甜點？', 'Oke, saya mau yang ini. Meimei, kamu suka makanan penutup apa?'),
            ('李美美', '我喜歡冰淇淋和蛋糕。', 'Aku suka es krim dan kue.'),
            ('王大文', '那我們也買兩個冰淇淋吧！', 'Kalau begitu kita beli dua es krim juga!'),
        ]),
        ('第二天，在家', 'Keesokan harinya, di rumah', [
            ('志明', '謝謝你們！這個蛋糕的味道很好，不太甜。', 'Terima kasih! Rasa kuenya enak, tidak terlalu manis.'),
            ('王大文', '我們還買了點心，有甜的，也有鹹的。', 'Kami juga beli camilan, ada yang manis, ada juga yang asin.'),
            ('志明', '我也買了一個點心，你們吃一點吧！', 'Aku juga beli camilan, kalian makan sedikit ya!'),
            ('李美美', '啊，好臭啊！', 'Aduh, bau sekali!'),
            ('志明', '這個點心又臭又香，臺灣人很喜歡吃。', 'Camilan ini bau tapi harum, orang Taiwan suka sekali.'),
            ('王大文', '……有一點辣，也有一點酸，很好吃！', '…Agak pedas, juga agak asam, enak sekali!'),
        ]),
    ]),
}

# ---- kelompok 1 (B01–B17) ----
BARU.update({
    'B01': ('Minggu pertama kuliah. Di dekat kolam renang kampus Meimei dan Dawen saling bertanya olahraga apa yang '
            'bisa mereka lakukan dan berjanji berlatih bersama, tetapi keesokan harinya kaki Meimei sakit.', [
        ('在學校的游泳池旁邊', 'Di samping kolam renang kampus', [
            ('李美美', '大文，你會游泳嗎？', 'Dawen, kamu bisa berenang?'),
            ('王大文', '會，我很喜歡游泳。學校的游泳池很大，我常常來游。你呢？', 'Bisa, aku suka sekali berenang. Kolam renang kampus besar, aku sering berenang ke sini. Kamu?'),
            ('李美美', '我不會游泳，可是我會打網球。', 'Aku tidak bisa berenang, tapi aku bisa main tenis.'),
            ('王大文', '我不會打網球，我會踢足球，也會打籃球。', 'Aku tidak bisa main tenis, aku bisa main sepak bola, juga basket.'),
            ('李美美', '臺灣人很喜歡棒球，你會打棒球嗎？', 'Orang Taiwan suka sekali bisbol, kamu bisa main bisbol?'),
            ('王大文', '不會，可是我想學。你每天運動嗎？', 'Tidak bisa, tapi aku ingin belajar. Kamu olahraga setiap hari?'),
            ('李美美', '對，我每天早上慢跑。', 'Iya, aku jogging setiap pagi.'),
            ('王大文', '我也喜歡跑步！明天下午我們一起去跑步，好不好？', 'Aku juga suka lari! Besok sore kita lari bersama, mau?'),
            ('李美美', '好！', 'Boleh!'),
        ]),
        ('第二天，打電話', 'Keesokan harinya, menelepon', [
            ('李美美', '大文，對不起，今天我不能去跑步，我的腳很痛。', 'Dawen, maaf, hari ini aku tidak bisa lari, kakiku sakit.'),
            ('王大文', '沒關係，你應該多休息。', 'Tidak apa-apa, kamu sebaiknya banyak istirahat.'),
            ('李美美', '謝謝。星期六我能去。', 'Terima kasih. Hari Sabtu aku bisa pergi.'),
            ('王大文', '好！星期六早上七點，學校門口見，怎麼樣？', 'Oke! Sabtu jam tujuh pagi ketemu di gerbang kampus, bagaimana?'),
            ('李美美', '好！我們先跑步，然後你教我游泳吧！', 'Oke! Kita lari dulu, habis itu kamu ajari aku berenang ya!'),
        ]),
    ]),
    'B02': ('Kampus mengadakan piknik akhir pekan. Meimei mengajak Dawen ikut; di taman mereka berfoto dan '
            'mendengarkan seorang guru bercerita untuk anak-anak.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，這個星期六你有空嗎？', 'Dawen, Sabtu ini kamu ada waktu?'),
            ('王大文', '有空。你想做什麼？', 'Ada. Kamu mau ngapain?'),
            ('李美美', '學校有一個活動，大家一塊兒去公園野餐。你要不要參加？', 'Kampus ada acara, semua piknik bareng ke taman. Kamu mau ikut?'),
            ('王大文', '要！我要參加。我可以帶什麼？', 'Mau! Aku ikut. Aku bisa bawa apa?'),
            ('李美美', '你帶喝的吧，我要帶水果。', 'Kamu bawa minuman saja, aku bawa buah.'),
            ('王大文', '好！我也要照相！', 'Oke! Aku juga mau foto-foto!'),
        ]),
        ('星期六，在公園', 'Hari Sabtu, di taman', [
            ('王大文', '這裡好漂亮！美美，我給你照相吧。', 'Di sini cantik sekali! Meimei, aku fotokan kamu ya.'),
            ('李美美', '好！……我想看相片。', 'Oke! …Aku mau lihat fotonya.'),
            ('王大文', '你看，很好看吧！', 'Lihat, bagus kan!'),
            ('李美美', '很好看！你看那邊，孩子們在畫圖。', 'Bagus sekali! Lihat di sana, anak-anak lagi menggambar.'),
            ('王大文', '旁邊的孩子們在聽老師說故事。', 'Anak-anak di sebelahnya sedang mendengarkan guru bercerita.'),
            ('李美美', '我也想聽故事！走，我們一塊兒去聽吧！', 'Aku juga mau dengar ceritanya! Ayo, kita dengarkan bareng!'),
        ]),
    ]),
    'B03': ('Dawen ingin menonton pertandingan bisbol pertamanya di Taiwan. Mereka membeli tiket lebih awal, lalu di '
            'stadion ikut bersorak untuk tim yang sedang berada di peringkat dua.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，這個星期天有棒球比賽，我想到球場去看。', 'Meimei, Minggu ini ada pertandingan bisbol, aku ingin nonton ke stadion.'),
            ('李美美', '好！我也要去。門票多少錢？', 'Boleh! Aku juga mau ikut. Tiket masuknya berapa?'),
            ('王大文', '一張票三百塊。這是我第一次看棒球比賽！', 'Satu tiket tiga ratus. Ini pertama kalinya aku nonton bisbol!'),
            ('李美美', '星期天人很多，我們早一點到球場去買票吧。', 'Hari Minggu ramai, kita ke stadion lebih awal untuk beli tiket ya.'),
        ]),
        ('星期天，在球場', 'Hari Minggu, di stadion', [
            ('李美美', '加油！加油！', 'Ayo! Semangat!'),
            ('王大文', '他們現在是第幾名？', 'Mereka sekarang peringkat berapa?'),
            ('李美美', '第二名。今天他們能拿第一名！', 'Peringkat dua. Hari ini mereka bisa dapat peringkat satu!'),
            ('王大文', '加油！加油！', 'Ayo! Semangat!'),
            ('李美美', '你聽，大家的加油聲好大！', 'Dengar, sorakan semua orang keras sekali!'),
            ('王大文', '他們真棒！這一場比賽很好看。', 'Mereka hebat! Pertandingan ini seru sekali.'),
            ('李美美', '下次我們再到球場來看吧！', 'Lain kali kita nonton ke stadion lagi ya!'),
            ('王大文', '好！下一場我也要來！', 'Oke! Pertandingan berikutnya aku juga mau datang!'),
        ]),
    ]),
    'B05': ('Dawen bertamu ke rumah keluarga Meimei di Taichung: disambut ibu Meimei, memberi oleh-oleh, makan '
            'malam bersama, lalu berpamitan dengan sopan.', [
        ('在美美家門口', 'Di depan rumah Meimei', [
            ('美美的媽媽', '歡迎歡迎！請進，請到客廳坐。', 'Selamat datang! Silakan masuk, silakan duduk di ruang tamu.'),
            ('王大文', '李太太，您好！不好意思，今天麻煩您。', 'Selamat sore, Bu Li! Maaf, hari ini merepotkan Ibu.'),
            ('美美的媽媽', '不麻煩！請坐，請喝茶。', 'Tidak repot! Silakan duduk, silakan minum teh.'),
            ('王大文', '謝謝。這是印尼的咖啡，送您。', 'Terima kasih. Ini kopi Indonesia, untuk Ibu.'),
            ('美美的媽媽', '你太客氣啦！謝謝你。', 'Kamu terlalu sungkan! Terima kasih.'),
        ]),
        ('在飯廳', 'Di ruang makan', [
            ('美美的媽媽', '大文，請到飯廳吃飯。請多吃，不要客氣！', 'Dawen, silakan makan di ruang makan. Makan yang banyak, jangan sungkan!'),
            ('王大文', '謝謝，菜很好吃！', 'Terima kasih, masakannya enak sekali!'),
            ('李美美', '我媽媽很會做菜。', 'Ibuku jago masak.'),
            ('王大文', '不好意思，九點我要坐火車，明天早上我要去看朋友。', 'Maaf, jam sembilan saya harus naik kereta, besok pagi saya mau menemui teman.'),
            ('美美的媽媽', '請不要走路去火車站，美美送你去。', 'Jangan jalan kaki ke stasiun, biar Meimei mengantarmu.'),
            ('王大文', '謝謝您！祝您週末快樂！', 'Terima kasih, Bu! Selamat berakhir pekan!'),
            ('美美的媽媽', '不客氣，歡迎你再來！', 'Sama-sama, lain kali datang lagi ya!'),
        ]),
    ]),
    'B07': ('Dawen pindah dari asrama ke apartemen sewaan di lantai tujuh bersama teman sekamarnya, Zhiming. Pada hari '
            'pindahan, mereka memilah barang milik siapa, dan pemilik rumah datang menyambut.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你要搬家嗎？', 'Dawen, kamu mau pindahan?'),
            ('王大文', '對，這個星期六搬。宿舍的屋子太小，我想租房子。', 'Iya, Sabtu ini pindah. Kamar asrama terlalu kecil, aku ingin menyewa rumah.'),
            ('李美美', '你的新家在哪裡？', 'Rumah barumu di mana?'),
            ('王大文', '在學校旁邊的大樓，七樓。我跟志明一起租。', 'Di gedung sebelah kampus, lantai tujuh. Aku menyewa bersama Zhiming.'),
            ('李美美', '志明是你的室友嗎？房租多少錢？', 'Zhiming teman sekamarmu? Sewanya berapa?'),
            ('王大文', '對。一個月一萬二，我們一個人六千。', 'Iya. Dua belas ribu sebulan, kami masing-masing enam ribu.'),
            ('李美美', '不貴！房東好不好？', 'Tidak mahal! Pemilik rumahnya baik?'),
            ('王大文', '很好，房東是張太太，她很客氣。', 'Baik sekali, pemiliknya Bu Zhang, orangnya sopan.'),
        ]),
        ('星期六，在大樓的大門', 'Hari Sabtu, di pintu gerbang gedung', [
            ('志明', '大文，車上的東西都是你的嗎？', 'Dawen, barang-barang di mobil semuanya punyamu?'),
            ('王大文', '不都是我的。椅子和電腦是我的，電視是宿舍的。', 'Tidak semuanya punyaku. Kursi dan komputernya punyaku, televisinya punya asrama.'),
            ('志明', '宿舍的電視？', 'Televisi asrama?'),
            ('王大文', '對，明天我要拿去宿舍。', 'Iya, besok mau kubawa ke asrama.'),
            ('房東', '歡迎你們！這是大樓的大門。屋子裡的桌子是我的，你們可以用。', 'Selamat datang! Ini pintu gerbang gedung. Meja di dalam rumah punya saya, kalian boleh pakai.'),
            ('王大文', '謝謝您！', 'Terima kasih, Bu!'),
            ('志明', '大文，車上的東西很多，我們快搬吧！', 'Dawen, barang di mobil banyak, ayo cepat kita angkut!'),
        ]),
    ]),
    'B09': ('Seminggu setelah pindahan, apartemen Dawen masih berantakan. Meimei membantu bersih-bersih, lalu AC-nya '
            'rusak; Dawen menelepon pemilik rumah.', [
        ('在大文家', 'Di rumah Dawen', [
            ('李美美', '大文，你們搬來一個星期了，屋子還不乾淨！', 'Dawen, kalian sudah pindah seminggu, rumahnya masih belum bersih!'),
            ('王大文', '對，我最近很忙。', 'Iya, akhir-akhir ini aku sibuk.'),
            ('李美美', '我來幫你吧！你洗衣服，我洗碗。', 'Biar aku bantu! Kamu cuci baju, aku cuci piring.'),
            ('王大文', '謝謝你幫忙！', 'Terima kasih sudah membantu!'),
            ('李美美', '碗都乾淨了！要放在哪裡？', 'Mangkuknya sudah bersih semua! Ditaruh di mana?'),
            ('王大文', '放在桌子上吧。我去掛衣服。', 'Taruh di meja saja. Aku jemur bajunya dulu.'),
            ('李美美', '你看，屋子乾淨了！', 'Lihat, rumahnya sudah bersih!'),
        ]),
        ('下午', 'Sore hari', [
            ('王大文', '好熱啊！冷氣怎麼不冷？', 'Panas sekali! AC-nya kenapa tidak dingin?'),
            ('李美美', '冷氣壞了！', 'AC-nya rusak!'),
            ('王大文', '我打電話請房東幫忙。', 'Aku telepon pemilik rumah minta bantuan.'),
            ('房東', '好，明天我帶人來看。今天你們先開窗戶吧。', 'Baik, besok saya bawa orang untuk memeriksanya. Hari ini kalian buka jendela dulu saja.'),
            ('李美美', '大文，你把燈關了吧，燈也很熱。', 'Dawen, matikan lampunya, lampunya juga panas.'),
            ('王大文', '好。這個窗戶要拉，對嗎？', 'Oke. Jendela ini harus ditarik, ya?'),
            ('李美美', '對！……開了，不熱了！', 'Iya! …Sudah terbuka, tidak panas lagi!'),
            ('王大文', '謝謝你今天的幫助！我請你喝咖啡。', 'Terima kasih atas bantuanmu hari ini! Aku traktir kopi.'),
        ]),
    ]),
    'B10': ('Pagi hari Zhiming menunggu lama di depan kamar mandi karena Dawen mandi lama. Mereka membicarakan '
            'kebiasaan masing-masing, lalu membuat jadwal mandi untuk seminggu.', [
        ('早上，在家', 'Pagi hari, di rumah', [
            ('志明', '大文，快一點！我要上課！', 'Dawen, cepat sedikit! Aku mau kuliah!'),
            ('王大文', '對不起！我出來了。', 'Maaf! Aku sudah keluar.'),
            ('志明', '你每天洗澡洗多久？', 'Setiap hari kamu mandi berapa lama?'),
            ('王大文', '平常洗二十分鐘。', 'Biasanya dua puluh menit.'),
            ('志明', '二十分鐘？好久啊！我總是洗五分鐘。', 'Dua puluh menit? Lama sekali! Aku selalu lima menit.'),
            ('王大文', '這是我的習慣。在印尼，我一天洗澡洗兩次。', 'Ini kebiasaanku. Di Indonesia, aku mandi dua kali sehari.'),
            ('志明', '白天你可以洗兩次，可是早上我要先洗！', 'Siang hari kamu boleh mandi dua kali, tapi pagi hari aku mandi duluan!'),
        ]),
        ('晚上，下課以後', 'Malam hari, sepulang kuliah', [
            ('王大文', '志明，平常早上你先洗，晚上我洗，好嗎？', 'Zhiming, biasanya pagi kamu duluan, malam aku, bagaimana?'),
            ('志明', '好。下課以後你一直上網，上三個小時，你可以晚一點洗。', 'Oke. Sepulang kuliah kamu terus internetan sampai tiga jam, kamu bisa mandi lebih malam.'),
            ('王大文', '可是週一早上我也有課。', 'Tapi hari Senin pagi aku juga ada kuliah.'),
            ('志明', '那週一你早一點起床！', 'Kalau begitu hari Senin kamu bangun lebih pagi!'),
            ('王大文', '好。週日呢？', 'Oke. Kalau hari Minggu?'),
            ('志明', '這個禮拜天，你可以洗一個小時！', 'Minggu ini, kamu boleh mandi satu jam!'),
            ('王大文', '好！最後一個問題：洗澡以後，誰洗洗手間？', 'Asyik! Pertanyaan terakhir: habis mandi, siapa yang membersihkan kamar mandi?'),
            ('志明', '你！', 'Kamu!'),
        ]),
    ]),
    'B11': ('Hari pertama Dawen magang di sebuah perusahaan. Atasannya menjelaskan jam kerja; sepulang kerja Meimei '
            'bertanya bagaimana harinya dan apa rencananya ke depan.', [
        ('第一天，在公司', 'Hari pertama, di perusahaan', [
            ('王先生', '大文，歡迎你來我們公司！', 'Dawen, selamat datang di perusahaan kami!'),
            ('王大文', '謝謝您！我很高興有這個機會。', 'Terima kasih, Pak! Saya senang sekali mendapat kesempatan ini.'),
            ('王先生', '我們從早上九點工作到下午五點。你的辦公室在三樓。', 'Kami bekerja dari jam sembilan pagi sampai jam lima sore. Kantormu di lantai tiga.'),
            ('王大文', '好。我沒有工作經驗，有問題可以問您嗎？', 'Baik. Saya belum punya pengalaman kerja, kalau ada pertanyaan boleh tanya Bapak?'),
            ('王先生', '可以。你的中文能力很好，下個星期開始，你可以一個人工作。', 'Boleh. Kemampuan Mandarinmu bagus, mulai minggu depan kamu bisa bekerja sendiri.'),
        ]),
        ('下班以後', 'Sepulang kerja', [
            ('李美美', '大文，你下班了嗎？第一天上班怎麼樣？', 'Dawen, sudah pulang kerja? Hari pertama kerja bagaimana?'),
            ('王大文', '很好！可是從九點工作到五點，好累！', 'Bagus! Tapi kerja dari jam sembilan sampai jam lima, capek sekali!'),
            ('李美美', '你以後想在公司上班嗎？', 'Nanti kamu ingin kerja di perusahaan?'),
            ('王大文', '不想，我想當老師，教中文。我的計畫是：明年開始教印尼人中文。', 'Tidak, aku ingin jadi guru, mengajar Mandarin. Rencanaku: tahun depan mulai mengajar Mandarin untuk orang Indonesia.'),
            ('李美美', '在公司上班，你的中文也會進步。這是好辦法！', 'Dengan kerja di perusahaan, Mandarinmu juga akan maju. Ini cara yang bagus!'),
            ('王大文', '對！可是當老師錢不多啊。', 'Iya! Tapi jadi guru uangnya tidak banyak, lho.'),
            ('李美美', '沒關係，你喜歡就好！', 'Tidak apa-apa, yang penting kamu suka!'),
        ]),
    ]),
    'B12': ('Meimei melihat album foto lama keluarga Dawen. Dawen bercerita tentang kakek-neneknya, anjingnya waktu '
            'kecil, dan keluarga besarnya di Indonesia.', [
        ('在大文家，看照片', 'Di rumah Dawen, melihat foto', [
            ('李美美', '大文，這張照片上的人是誰？', 'Dawen, orang di foto ini siapa?'),
            ('王大文', '是我爺爺和奶奶。我爺爺以前是醫生，後來當老師。', 'Kakek dan nenekku. Dulu kakekku dokter, kemudian jadi guru.'),
            ('李美美', '你很像你爺爺！', 'Kamu mirip sekali dengan kakekmu!'),
            ('王大文', '對，我媽媽也說我像爺爺。', 'Iya, ibuku juga bilang aku mirip kakek.'),
            ('李美美', '這隻狗是你家的嗎？', 'Anjing ini punya keluargamu?'),
            ('王大文', '對。小時候，我每天跟這隻狗一起玩。現在它住在我叔叔家。', 'Iya. Waktu kecil, setiap hari aku main dengan anjing ini. Sekarang dia tinggal di rumah pamanku.'),
        ]),
        ('說家人', 'Bercerita tentang keluarga', [
            ('李美美', '你的家庭很大嗎？', 'Keluargamu besar?'),
            ('王大文', '很大！我有兩個伯伯、三個叔叔、四個阿姨。從前我們都住在一起。', 'Besar sekali! Aku punya dua kakak ayah, tiga adik ayah, dan empat bibi. Dulu kami semua tinggal bersama.'),
            ('李美美', '好多人！我沒去過印尼，以前只看過印尼的照片。', 'Banyak sekali! Aku belum pernah ke Indonesia, dulu hanya pernah lihat foto Indonesia.'),
            ('王大文', '下次你跟我去印尼吧！我奶奶家有兩隻貓，還有馬！', 'Lain kali ikut aku pulang ke Indonesia! Di rumah nenekku ada dua kucing, ada kuda juga!'),
            ('李美美', '真的嗎？我沒看過馬！', 'Serius? Aku belum pernah lihat kuda!'),
        ]),
    ]),
    'B14': ('Pagi hari Annie dan Meimei melihat anak-anak SD berangkat sekolah dengan tas besar. Mereka lalu '
            'membandingkan sekolah di Taiwan dan Indonesia.', [
        ('早上，在路上', 'Pagi hari, di jalan', [
            ('安妮', '美美，你看，那幾個小朋友的書包好大！', 'Meimei, lihat, tas sekolah beberapa anak itu besar sekali!'),
            ('李美美', '他們是小學的學生。臺灣的小學每天七點多就上學。', 'Mereka murid SD. SD di Taiwan setiap hari mulai masuk jam tujuh lewat.'),
            ('安妮', '他們幾年級？', 'Mereka kelas berapa?'),
            ('李美美', '差不多是三、四年級。', 'Kira-kira kelas tiga atau empat.'),
            ('安妮', '他們的書包裡有幾本書？', 'Di tas mereka ada berapa buku?'),
            ('李美美', '十幾本吧！這所小學的功課很多。', 'Belasan buku, mungkin! SD ini PR-nya banyak.'),
        ]),
        ('在學校', 'Di kampus', [
            ('李美美', '安妮，你以前的高中，一個班有幾個學生？', 'Annie, di SMA-mu dulu, satu kelas ada berapa murid?'),
            ('安妮', '三十幾個，一半是女生。臺灣呢？', 'Tiga puluhan, setengahnya perempuan. Di Taiwan?'),
            ('李美美', '我們班有四十幾個學生。你們幾月開學？', 'Kelasku ada empat puluhan murid. Kalian mulai sekolah bulan apa?'),
            ('安妮', '印尼七月開學。', 'Di Indonesia mulai bulan Juli.'),
            ('李美美', '臺灣九月開學。開學以後，大家都很忙。', 'Di Taiwan mulai bulan September. Setelah mulai sekolah, semua orang sibuk.'),
            ('安妮', '你以前的成績好嗎？', 'Nilaimu dulu bagus?'),
            ('李美美', '一部分很好，一部分不好！', 'Sebagian bagus, sebagian tidak!'),
        ]),
    ]),
    'B15': ('Seusai kelas Meimei memuji bahasa Mandarin Dawen, dan mereka membicarakan bahasa yang bisa mereka '
            'kuasai. Di kelas berikutnya Guru Chen meminta Dawen bercerita dalam bahasa Mandarin.', [
        ('下課，在教室', 'Setelah kelas, di ruang kelas', [
            ('李美美', '大文，你中文說得很好！', 'Dawen, Mandarinmu bagus sekali!'),
            ('王大文', '哪裡哪裡，我每天練習。', 'Ah, tidak juga, aku berlatih setiap hari.'),
            ('李美美', '你會說什麼語言？', 'Kamu bisa bahasa apa saja?'),
            ('王大文', '印尼話和英語。日文我只會說「你好」。', 'Bahasa Indonesia dan Inggris. Bahasa Jepang aku hanya bisa bilang "halo".'),
            ('李美美', '安妮呢？', 'Kalau Annie?'),
            ('王大文', '安妮會說德文和法文！她說得很快。', 'Annie bisa bahasa Jerman dan Prancis! Dia bicaranya cepat sekali.'),
        ]),
        ('上課', 'Di kelas', [
            ('陳老師', '大文，請你用中文講你的週末。', 'Dawen, coba ceritakan akhir pekanmu dalam bahasa Mandarin.'),
            ('王大文', '好。週末我跟朋友去公園野餐，大家都很高興。', 'Baik. Akhir pekan saya piknik ke taman dengan teman, semua senang sekali.'),
            ('陳老師', '你講得很清楚！可是這個字你寫得不清楚。', 'Ceritamu jelas sekali! Tapi huruf ini tulisanmu kurang jelas.'),
            ('王大文', '對不起，這個字我不會寫。', 'Maaf, huruf ini saya tidak bisa menulisnya.'),
            ('陳老師', '沒關係，你可以用字典學。', 'Tidak apa-apa, kamu bisa belajar pakai kamus.'),
            ('王大文', '好，我晚上用字典練習。', 'Baik, nanti malam saya berlatih pakai kamus.'),
        ]),
    ]),
    'B16': ('Minggu depan ada ujian Mandarin, dan Dawen sering lupa huruf. Ia meminta saran dari kakak tingkatnya, '
            'Anan; sehari sebelum ujian Meimei memastikan Dawen sudah siap.', [
        ('在學校', 'Di kampus', [
            ('王大文', '安安，下個星期要考中文，可是中文字很難，我常常忘。我要怎麼學？', 'Anan, minggu depan ujian Mandarin, tapi huruf Mandarin susah, aku sering lupa. Aku harus belajar bagaimana?'),
            ('陳安安', '你要每天念書，一天寫十個字。', 'Kamu harus belajar setiap hari, sehari tulis sepuluh huruf.'),
            ('王大文', '寫十個字，我就會記得嗎？', 'Kalau tulis sepuluh huruf, aku akan ingat?'),
            ('陳安安', '你也要常常看，常常用。學習語言，這個方法最簡單。', 'Kamu juga harus sering lihat dan sering pakai. Untuk belajar bahasa, cara ini paling sederhana.'),
            ('王大文', '好，我要努力！', 'Baik, aku akan berusaha keras!'),
        ]),
        ('考試前一天', 'Sehari sebelum ujian', [
            ('李美美', '大文，明天考試，你準備了嗎？', 'Dawen, besok ujian, kamu sudah siap?'),
            ('王大文', '準備了！這個星期我每天都很用功。', 'Sudah! Minggu ini aku rajin belajar setiap hari.'),
            ('李美美', '考試的字你都會寫嗎？', 'Huruf-huruf untuk ujian kamu bisa tulis semua?'),
            ('王大文', '都會寫！安安的方法很好。', 'Bisa semua! Cara Anan bagus.'),
            ('李美美', '別忘了，考試需要帶筆。', 'Jangan lupa, ujian perlu bawa pulpen.'),
            ('王大文', '我記得！', 'Aku ingat!'),
        ]),
    ]),
    'B17': ('Dawen mencari buku pelajarannya yang hilang di perpustakaan bersama Meimei. Setelah ketemu, mereka ke '
            'toko buku untuk membeli koran yang dibutuhkan untuk tugas.', [
        ('在圖書館', 'Di perpustakaan', [
            ('王大文', '美美，你看見我的課本了嗎？', 'Meimei, kamu lihat buku pelajaranku?'),
            ('李美美', '沒看見。是什麼課本？', 'Tidak lihat. Buku pelajaran apa?'),
            ('王大文', '中文課本。明天上課要用。', 'Buku Mandarin. Besok dipakai di kelas.'),
            ('李美美', '我們找一找吧。', 'Ayo kita cari.'),
            ('王大文', '……我找到了！在椅子上。', '…Ketemu! Di atas kursi.'),
            ('李美美', '真好！那我的本子呢？', 'Syukurlah! Lalu buku catatanku?'),
            ('王大文', '在你的書包裡，我看見了。', 'Di tasmu, aku lihat tadi.'),
        ]),
        ('在書店', 'Di toko buku', [
            ('李美美', '今天的作業是看報紙，寫五行字。', 'Tugas hari ini membaca koran, lalu menulis lima baris.'),
            ('王大文', '這家書店有中文報紙嗎？', 'Toko buku ini ada koran Mandarin?'),
            ('李美美', '你聽，那位先生說有。', 'Dengar, bapak itu bilang ada.'),
            ('王大文', '我聽到了！報紙在門口。', 'Aku dengar! Korannya di dekat pintu.'),
            ('李美美', '我買到了！', 'Aku sudah dapat!'),
            ('王大文', '我也買到了。我們去圖書館寫作業吧。', 'Aku juga sudah dapat. Ayo kita ke perpustakaan mengerjakan tugas.'),
        ]),
    ]),
})

# ---- kelompok 2 (B18–B33) ----
BARU.update({
    'B18': ('Musim gugur, udara mulai dingin. Koran mengabarkan akhir pekan ini di gunung akan turun salju; Dawen yang '
            'belum pernah melihat salju pergi ke gunung bersama Meimei, padahal ia hanya memakai satu lapis baju.', [
        ('秋天，在學校', 'Musim gugur, di kampus', [
            ('王大文', '美美，你看，學校的樹變紅了！', 'Meimei, lihat, pohon-pohon di kampus berubah merah!'),
            ('李美美', '對，秋天了，天氣也變冷了。', 'Iya, sudah musim gugur, cuacanya juga jadi dingin.'),
            ('王大文', '臺灣的冬天會下雪嗎？', 'Musim dingin di Taiwan turun salju?'),
            ('李美美', '很少。可是報紙說，這個週末山上會下雪。', 'Jarang. Tapi kata koran, akhir pekan ini di gunung akan turun salju.'),
            ('王大文', '真的嗎？印尼沒有冬天，我沒看過雪！', 'Serius? Indonesia tidak punya musim dingin, aku belum pernah lihat salju!'),
            ('李美美', '如果下雪，我們就去山上看雪吧！', 'Kalau turun salju, kita pergi lihat salju ke gunung ya!'),
            ('王大文', '好！要是不下雪呢？', 'Oke! Kalau tidak turun salju?'),
            ('李美美', '要是不下雪，我們就去看山上的樹。', 'Kalau tidak turun salju, kita lihat pohon-pohon di gunung saja.'),
        ]),
        ('星期六，在山上', 'Hari Sabtu, di gunung', [
            ('王大文', '美美，你看！下雪了！', 'Meimei, lihat! Turun salju!'),
            ('李美美', '好漂亮！樹上都是雪。', 'Cantik sekali! Pohon-pohonnya penuh salju.'),
            ('王大文', '好冷啊！我只穿一件衣服。', 'Dingin sekali! Aku cuma pakai satu baju.'),
            ('李美美', '我說過山上會很冷！你明天會感冒。', 'Sudah kubilang di gunung akan dingin sekali! Besok kamu bakal masuk angin.'),
            ('王大文', '沒關係！這是我第一次看雪，我很高興！', 'Tidak apa-apa! Ini pertama kalinya aku lihat salju, aku senang sekali!'),
            ('李美美', '春天和夏天，山上也很漂亮。我們再來吧！', 'Musim semi dan musim panas gunungnya juga indah. Kita datang lagi ya!'),
        ]),
    ]),
    'B20': ('Setelah masuk angin, Dawen perlu jaket musim dingin. Ia mencoba beberapa jaket dan topi di toko bersama '
            'Meimei; saat keluar, hujan deras turun dan mereka menunggu di dalam toko.', [
        ('在衣服店', 'Di toko pakaian', [
            ('李美美', '大文，你感冒了，要買一件外套。', 'Dawen, kamu masuk angin, harus beli jaket.'),
            ('王大文', '對，我沒有冬天的衣服。', 'Iya, aku tidak punya baju musim dingin.'),
            ('李美美', '你試一下這件外套吧。', 'Coba jaket ini.'),
            ('王大文', '這件太大了！', 'Yang ini terlalu besar!'),
            ('李美美', '那件大衣呢？', 'Kalau mantel itu?'),
            ('王大文', '有點小，也有點貴。', 'Agak kecil, juga agak mahal.'),
            ('店員', '這件外套怎麼樣？不大也不小。', 'Bagaimana jaket ini? Tidak besar, tidak kecil.'),
            ('王大文', '很好！我要這件。', 'Pas! Saya ambil yang ini.'),
            ('李美美', '你戴這個帽子，也很好看。', 'Kamu pakai topi ini juga cocok.'),
            ('王大文', '好，帽子我也要。美美，你也要試褲子和裙子嗎？', 'Oke, topinya juga kuambil. Meimei, kamu juga mau coba celana dan rok?'),
            ('李美美', '不要，今天的錢都給你買衣服了！', 'Tidak, uang hari ini sudah habis buat beli bajumu!'),
        ]),
        ('在店門口', 'Di depan toko', [
            ('王大文', '啊，下大雨了！', 'Aduh, hujan deras!'),
            ('李美美', '我的裙子濕了！', 'Rokku basah!'),
            ('王大文', '我的眼鏡也濕了，我看不清楚。', 'Kacamataku juga basah, aku tidak bisa lihat dengan jelas.'),
            ('李美美', '我們在店裡等一下吧。', 'Kita tunggu sebentar di dalam toko saja.'),
            ('王大文', '好。我先脫帽子，帽子太濕了。', 'Oke. Aku lepas topi dulu, topinya terlalu basah.'),
            ('李美美', '你看一下手錶，現在幾點？', 'Coba lihat jam tanganmu, sekarang jam berapa?'),
            ('王大文', '五點。雨有點大，我們六點再走吧。', 'Jam lima. Hujannya agak deras, kita pergi jam enam saja.'),
        ]),
    ]),
    'B21': ('Masih di pusat perbelanjaan, Dawen membeli celana dengan ukuran dan warna yang ia mau, lalu Meimei '
            'memilih sepatu yang lebih ringan.', [
        ('在衣服店', 'Di toko pakaian', [
            ('店員', '先生，這條褲子怎麼樣？', 'Mas, bagaimana celana ini?'),
            ('王大文', '有點小，我要大一點的。', 'Agak kecil, saya mau yang lebih besar sedikit.'),
            ('店員', '你要藍色的還是黑色的？', 'Mau yang biru atau yang hitam?'),
            ('王大文', '藍色的。有綠色的嗎？', 'Yang biru. Ada yang hijau?'),
            ('店員', '有，綠色和黃色的都有。', 'Ada, hijau dan kuning ada semua.'),
            ('王大文', '我要綠色的，這個顏色很好看。', 'Saya mau yang hijau, warnanya bagus.'),
        ]),
        ('在鞋店', 'Di toko sepatu', [
            ('李美美', '我想買一雙鞋子。這雙太重了，我要輕一點的。', 'Aku mau beli sepasang sepatu. Yang ini terlalu berat, aku mau yang lebih ringan.'),
            ('店員', '這雙很輕。你喜歡什麼顏色？', 'Yang ini ringan sekali. Suka warna apa?'),
            ('李美美', '白色的還是紅色的？大文，你說呢？', 'Yang putih atau yang merah? Dawen, menurutmu?'),
            ('王大文', '白色的比較好看。', 'Yang putih lebih bagus.'),
            ('李美美', '好，我要白色的。', 'Oke, aku ambil yang putih.'),
            ('王大文', '我還要買兩支筆。我們去旁邊的書店吧。', 'Aku masih mau beli dua pulpen. Ayo ke toko buku sebelah.'),
        ]),
    ]),
    'B22': ('Kulkas di apartemen kosong. Dawen dan Zhiming memilih tempat belanja yang paling murah, lalu di '
            'supermarket mereka bersepakat belanja sedikit saja — tetapi pulang membawa tiga kantong.', [
        ('在家', 'Di rumah', [
            ('志明', '大文，冰箱裡都沒有東西了。', 'Dawen, di kulkas sudah tidak ada apa-apa.'),
            ('王大文', '我們去便利商店買吧，樓下就有一家。', 'Kita beli di minimarket saja, di bawah ada satu.'),
            ('志明', '超商很方便，可是東西比超市貴。', 'Minimarket praktis, tapi barangnya lebih mahal daripada supermarket.'),
            ('王大文', '那百貨公司裡的超市呢？', 'Kalau supermarket di dalam mal?'),
            ('志明', '百貨公司的東西都很貴。學校旁邊的那家商店最便宜。', 'Barang di mal semuanya mahal. Toko di sebelah kampus paling murah.'),
            ('王大文', '好，我們去那家超市。', 'Oke, kita ke supermarket itu.'),
        ]),
        ('在超市', 'Di supermarket', [
            ('志明', '我們多買一點水吧，一瓶十五塊，很便宜。', 'Kita beli air lebih banyak, satu botol lima belas, murah sekali.'),
            ('王大文', '好，買六瓶。還要一盒蛋和兩罐咖啡。', 'Oke, beli enam botol. Juga sekotak telur dan dua kaleng kopi.'),
            ('志明', '肉很貴，我們少買一點。', 'Dagingnya mahal, kita beli sedikit saja.'),
            ('店員', '你們要袋子嗎？一個袋子兩塊錢。', 'Mau pakai kantong? Satu kantong dua dolar.'),
            ('王大文', '要三個。', 'Mau tiga.'),
            ('志明', '三個？……好重！我們買了三袋東西！', 'Tiga? …Berat sekali! Kita beli tiga kantong barang!'),
            ('王大文', '你說要少買一點啊！', 'Kamu kan bilang mau beli sedikit!'),
        ]),
    ]),
    'B23': ('Dawen membeli ransel untuk liburan dan membayar dengan kartu kredit, sementara Meimei mendapat potongan '
            'harga untuk dompet kulit. Saat membayar, Dawen panik mengira dompetnya hilang.', [
        ('在包包店', 'Di toko tas', [
            ('王大文', '老闆，這個背包多少錢？', 'Pak, ransel ini berapa?'),
            ('老闆', '一千兩百塊。', 'Seribu dua ratus.'),
            ('王大文', '可以用信用卡付嗎？', 'Boleh bayar pakai kartu kredit?'),
            ('老闆', '可以。', 'Boleh.'),
            ('李美美', '老闆，這個皮包賣多少？', 'Pak, dompet kulit ini dijual berapa?'),
            ('老闆', '八百塊。你們是學生嗎？我算你七百。', 'Delapan ratus. Kalian mahasiswa? Saya hitung tujuh ratus saja.'),
            ('李美美', '謝謝！可以給我一個袋子嗎？', 'Terima kasih! Boleh minta satu kantong?'),
            ('老闆', '可以，我給你包。', 'Boleh, saya bungkuskan.'),
        ]),
        ('付錢的時候', 'Saat membayar', [
            ('王大文', '啊，我的錢包呢？我的信用卡在錢包裡！', 'Aduh, dompetku mana? Kartu kreditku di dompet!'),
            ('李美美', '在你的背包裡嗎？', 'Ada di ranselmu?'),
            ('王大文', '……在！在舊背包裡。', '…Ada! Di ransel lama.'),
            ('老闆', '好，請你給我信用卡。', 'Baik, silakan berikan kartu kreditnya.'),
            ('老闆', '謝謝！歡迎你們下次再來！', 'Terima kasih! Lain kali datang lagi ya!'),
        ]),
    ]),
    'B25': ('Dawen dan Zhiming memasak makan malam untuk Meimei di apartemen. Mereka membagi tugas, mencuci sayur '
            'sampai bersih, lalu makan bersama begitu masakan siap.', [
        ('在家', 'Di rumah', [
            ('志明', '大文，美美七點來，我們做什麼菜？', 'Dawen, Meimei datang jam tujuh, kita masak apa?'),
            ('王大文', '我炒青菜，你炸雞，好嗎？', 'Aku tumis sayur, kamu goreng ayam, bagaimana?'),
            ('志明', '好。青菜要先洗乾淨。', 'Oke. Sayurnya harus dicuci bersih dulu.'),
            ('王大文', '對。我洗了青菜就炒。刀子在哪裡？', 'Iya. Setelah sayurnya kucuci, langsung kutumis. Pisaunya di mana?'),
            ('志明', '在桌子上。我們也烤火腿吧！', 'Di meja. Kita panggang ham juga ya!'),
        ]),
        ('七點，美美來了', 'Jam tujuh, Meimei datang', [
            ('李美美', '好香啊！你們做了什麼菜？', 'Harum sekali! Kalian masak apa?'),
            ('王大文', '炒青菜、炸雞和烤火腿。', 'Tumis sayur, ayam goreng, dan ham panggang.'),
            ('李美美', '我要用叉子吃火腿。', 'Aku mau makan ham pakai garpu.'),
            ('志明', '叉子和湯匙都在盤子旁邊。', 'Garpu dan sendok ada di samping piring.'),
            ('李美美', '有冰塊嗎？我想喝冰水。', 'Ada es batu? Aku mau minum air dingin.'),
            ('王大文', '有！我們吃了飯就去樓下喝咖啡吧。', 'Ada! Habis makan kita langsung ngopi di bawah ya.'),
            ('李美美', '好！我吃飽了，菜都很好吃！', 'Oke! Aku sudah kenyang, masakannya enak semua!'),
        ]),
    ]),
    'B26': ('Siang yang panas. Dawen kehausan dan memilih minuman di kedai teh, lalu mereka membeli buah di kios '
            'sebelahnya.', [
        ('在飲料店', 'Di kedai minuman', [
            ('王大文', '好熱，我好渴！', 'Panas sekali, aku haus sekali!'),
            ('李美美', '你要紅茶還是奶茶？', 'Kamu mau teh hitam atau teh susu?'),
            ('王大文', '奶茶好喝嗎？', 'Teh susunya enak?'),
            ('李美美', '很好喝，可是很甜。', 'Enak sekali, tapi manis sekali.'),
            ('王大文', '多甜？', 'Semanis apa?'),
            ('李美美', '跟可樂一樣甜！', 'Semanis cola!'),
            ('王大文', '那我要紅茶。這裡有啤酒嗎？', 'Kalau begitu aku teh hitam. Di sini ada bir?'),
            ('店員', '對不起，我們不賣啤酒。我們也有果汁和汽水。', 'Maaf, kami tidak jual bir. Kami juga ada jus dan soda.'),
            ('李美美', '我要一杯西瓜的果汁。', 'Aku mau segelas jus semangka.'),
        ]),
        ('在水果店', 'Di toko buah', [
            ('王大文', '老闆，這裡的蘋果好吃嗎？', 'Pak, apel di sini enak?'),
            ('老闆', '很好吃，很甜，也很便宜。', 'Enak sekali, manis, juga murah.'),
            ('李美美', '香蕉呢？', 'Kalau pisang?'),
            ('老闆', '香蕉也很好吃。這個西瓜很大，可是很難拿。', 'Pisangnya juga enak. Semangka ini besar, tapi susah dibawa.'),
            ('王大文', '沒關係，我來拿！我要一個西瓜和五個蘋果。', 'Tidak apa-apa, biar aku yang bawa! Saya mau satu semangka dan lima apel.'),
        ]),
    ]),
    'B27': ('Malam hari di pasar malam: Dawen dan Meimei membeli pangsit dan mantou untuk dibawa ke asrama Meimei, '
            'lalu merencanakan sarapan besok pagi di pasar.', [
        ('在夜市', 'Di pasar malam', [
            ('王大文', '美美，夜市的人好多！你想吃什麼？', 'Meimei, pasar malamnya ramai sekali! Kamu mau makan apa?'),
            ('李美美', '夜市的小吃有很多種。我們先買餃子吧！', 'Jajanan di pasar malam banyak jenisnya. Kita beli pangsit dulu!'),
            ('王大文', '老闆，我要一份餃子，兩個饅頭。', 'Pak, saya mau seporsi pangsit, dua mantou.'),
            ('老闆', '好。要在這裡吃嗎？', 'Baik. Makan di sini?'),
            ('王大文', '不，我們要帶去宿舍吃。', 'Tidak, kami mau bawa ke asrama.'),
            ('李美美', '大文，你看，這道菜很好吃，我們也買一份吧！', 'Dawen, lihat, masakan ini enak, kita beli seporsi juga ya!'),
        ]),
        ('在路上', 'Di jalan', [
            ('李美美', '明天早上我要去市場買菜。你要來嗎？', 'Besok pagi aku mau belanja sayur ke pasar. Kamu mau ikut?'),
            ('王大文', '要！市場有漢堡和三明治嗎？', 'Mau! Di pasar ada hamburger dan sandwich?'),
            ('李美美', '沒有。早餐店有漢堡、三明治和熱狗，市場沒有。市場有饅頭。', 'Tidak ada. Hamburger, sandwich, dan hot dog ada di toko sarapan, di pasar tidak ada. Di pasar ada mantou.'),
            ('王大文', '好，明天我要吃市場的饅頭，後天要去早餐店吃三明治！', 'Oke, besok aku mau makan mantou di pasar, lusa mau makan sandwich di toko sarapan!'),
        ]),
    ]),
    'B28': ('Meimei mengajak Dawen makan di restoran terkenal. Di restoran mereka memilih dari menu, lalu mencari '
            'kedai teh yang tidak terlalu mahal.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，週末我們去那家餐廳吃飯，怎麼樣？', 'Dawen, akhir pekan kita makan di restoran itu, bagaimana?'),
            ('王大文', '好啊。那家餐廳有名嗎？', 'Boleh. Restoran itu terkenal?'),
            ('李美美', '很有名！他們的牛肉麵很特別。', 'Terkenal sekali! Mi daging sapinya istimewa.'),
            ('王大文', '那我們七點去，好嗎？', 'Kalau begitu kita pergi jam tujuh, ya?'),
            ('李美美', '好！', 'Oke!'),
        ]),
        ('在餐廳', 'Di restoran', [
            ('王大文', '這間餐廳這麼大！人也那麼多！', 'Restoran ini besar sekali! Orangnya juga banyak sekali!'),
            ('李美美', '我們先看菜單吧。你要吃飯或是吃麵？', 'Kita lihat menu dulu. Kamu mau makan nasi atau mi?'),
            ('王大文', '我要牛肉麵。你要吃別的嗎？', 'Aku mi daging sapi. Kamu mau yang lain?'),
            ('李美美', '我要餃子。今天我只吃了這一餐！', 'Aku pangsit. Hari ini aku baru makan sekali ini!'),
            ('王大文', '吃飯以後，我們去茶館喝茶，好嗎？', 'Habis makan, kita minum teh di kedai teh, ya?'),
            ('李美美', '好啊。可是那家飯店的茶館那麼貴，我們去別的吧。', 'Boleh. Tapi kedai teh di hotel itu mahal sekali, kita cari yang lain saja.'),
        ]),
    ]),
    'B29': ('Meimei tiba dengan kereta jam lima. Annie dan Dawen memperkirakan jarak ke stasiun dari peta, tetapi '
            'ternyata perjalanannya jauh lebih lama daripada yang Dawen katakan.', [
        ('看地圖', 'Melihat peta', [
            ('安妮', '大文，美美幾點到車站？', 'Dawen, Meimei sampai di stasiun jam berapa?'),
            ('王大文', '五點。車站離這裡遠不遠？', 'Jam lima. Stasiunnya jauh dari sini?'),
            ('安妮', '你看地圖，不遠，很近。', 'Lihat peta, tidak jauh, dekat sekali.'),
            ('王大文', '從這裡走路要多久？', 'Dari sini jalan kaki berapa lama?'),
            ('安妮', '十分鐘吧。', 'Sepuluh menit, mungkin.'),
            ('王大文', '那我們四點半離開，好嗎？', 'Kalau begitu kita berangkat jam setengah lima, ya?'),
        ]),
        ('在街上', 'Di jalan', [
            ('安妮', '我們走了二十分鐘，車站呢？', 'Kita sudah jalan dua puluh menit, stasiunnya mana?'),
            ('王大文', '先生，請問車站離這裡遠嗎？', 'Pak, permisi, stasiunnya jauh dari sini?'),
            ('先生', '不遠。你們從這條街走，過馬路就是車站。', 'Tidak jauh. Kalian lewat jalan ini, menyeberang jalan raya langsung stasiun.'),
            ('安妮', '大文，你說很近！', 'Dawen, katamu dekat!'),
            ('王大文', '哪有很遠？只有二十分鐘！', 'Mana ada jauh? Cuma dua puluh menit!'),
            ('安妮', '快走吧，美美在等我們！', 'Ayo cepat, Meimei sedang menunggu kita!'),
        ]),
    ]),
    'B30': ('Dawen menanyakan jalan ke perpustakaan baru. Malam harinya Meimei menelepon untuk memastikan ia sudah '
            'sampai di rumah — ternyata Dawen pulang lewat pasar malam.', [
        ('在路上', 'Di jalan', [
            ('王大文', '小姐，請問，圖書館怎麼走？', 'Mbak, permisi, ke perpustakaan lewat mana?'),
            ('小姐', '你從這裡往前走，到路口向右轉。', 'Dari sini jalan lurus, di persimpangan belok kanan.'),
            ('王大文', '第一個路口嗎？', 'Persimpangan pertama?'),
            ('小姐', '不是，第二個十字路口。你會經過一個公園。', 'Bukan, perempatan kedua. Kamu akan melewati sebuah taman.'),
            ('王大文', '我走到公園，就往右轉，對嗎？', 'Kalau sudah sampai di taman, saya belok kanan, ya?'),
            ('小姐', '對，圖書館在公園對面。', 'Betul, perpustakaannya di seberang taman.'),
        ]),
        ('晚上，打電話', 'Malam hari, menelepon', [
            ('李美美', '大文，你回到家了嗎？', 'Dawen, kamu sudah sampai di rumah?'),
            ('王大文', '回到了！可是我回家的路走錯了。', 'Sudah! Tapi jalan pulangku salah.'),
            ('李美美', '你從圖書館往哪裡走？', 'Dari perpustakaan kamu jalan ke arah mana?'),
            ('王大文', '我往左走，走到夜市，在夜市吃了東西，然後回家。', 'Aku jalan ke kiri, sampai di pasar malam, makan dulu di pasar malam, lalu pulang.'),
            ('李美美', '你走錯的路很好吃啊！', 'Jalan salahmu enak juga ya!'),
        ]),
    ]),
    'B31': ('Meimei pulang ke Taichung akhir pekan ini dan mengajak Dawen. Mereka membahas cara ke sana; sesampainya '
            'di Taichung, ayah Meimei menjemput dan sorenya mereka bersepeda ke taman.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，從臺北到臺中怎麼去？', 'Meimei, dari Taipei ke Taichung naik apa?'),
            ('李美美', '你可以坐火車，也可以坐巴士。巴士比較便宜。', 'Bisa naik kereta, bisa juga naik bus. Bus lebih murah.'),
            ('王大文', '巴士要多久？', 'Naik bus berapa lama?'),
            ('李美美', '兩個多小時。巴士從這條路走，很方便。', 'Dua jam lebih. Busnya lewat jalan ini, praktis sekali.'),
            ('王大文', '到了臺中，我怎麼去你家？', 'Sampai di Taichung, aku ke rumahmu bagaimana?'),
            ('李美美', '我爸爸開汽車來車站接我們。我家有兩臺汽車。', 'Ayahku menjemput kita ke stasiun naik mobil. Di rumahku ada dua mobil.'),
        ]),
        ('在臺中', 'Di Taichung', [
            ('王大文', '美美，你爸爸來接我們，謝謝他！', 'Meimei, ayahmu menjemput kita, terima kasih ya!'),
            ('李美美', '不客氣。下午我們騎腳踏車去公園吧！', 'Sama-sama. Sore ini kita bersepeda ke taman yuk!'),
            ('王大文', '好！從你家到公園遠嗎？', 'Oke! Dari rumahmu ke taman jauh?'),
            ('李美美', '不遠，從這條小路騎十分鐘就到。', 'Tidak jauh, lewat jalan kecil ini bersepeda sepuluh menit sampai.'),
            ('王大文', '你看，那部巴士好大！公共汽車也到公園嗎？', 'Lihat, bus itu besar sekali! Bus umum juga sampai ke taman?'),
            ('李美美', '到，可是公共汽車的司機開得很快，騎腳踏車比較好玩。', 'Sampai, tapi sopir bus umum menyetirnya cepat sekali, bersepeda lebih asyik.'),
        ]),
    ]),
    'B32': ('Dawen pulang ke Indonesia untuk liburan. Meimei mengantarnya ke bandara naik taksi; di bandara koper '
            'Dawen kelebihan berat dan ia harus menambah biaya.', [
        ('在大樓門口', 'Di depan gedung', [
            ('李美美', '大文，計程車來了，快上車！我們去機場。', 'Dawen, taksinya sudah datang, cepat naik! Kita ke bandara.'),
            ('王大文', '等一下！我的手機在樓上，我上去拿。', 'Tunggu sebentar! HP-ku di atas, aku naik ambil dulu.'),
            ('李美美', '快一點！', 'Cepat sedikit!'),
            ('王大文', '我來了！美美，這是你的書，還你。', 'Aku datang! Meimei, ini bukumu, kukembalikan.'),
            ('司機', '東西放進來吧。', 'Barangnya masukkan ke sini saja.'),
        ]),
        ('在機場', 'Di bandara', [
            ('王大文', '飛機幾點飛？', 'Pesawatnya terbang jam berapa?'),
            ('李美美', '十點。現在八點，還早。我們有空，去喝咖啡吧。', 'Jam sepuluh. Sekarang jam delapan, masih pagi. Kita ada waktu, ayo minum kopi.'),
            ('王大文', '好。咖啡店在對面，我們走過去吧。', 'Oke. Kedai kopinya di seberang, kita jalan ke sana.'),
            ('小姐', '先生，你的東西太重了，要加錢。', 'Pak, barang Anda terlalu berat, harus tambah biaya.'),
            ('王大文', '要加多少錢？', 'Tambah berapa?'),
            ('小姐', '五百塊。', 'Lima ratus.'),
            ('王大文', '美美，這幾本書你帶回去吧。', 'Meimei, buku-buku ini kamu bawa pulang saja ya.'),
            ('李美美', '好！到了印尼，打電話給我！', 'Oke! Sampai di Indonesia, telepon aku ya!'),
        ]),
    ]),
    'B33': ('Dawen baru kembali dari Indonesia bersama kakak perempuannya yang ingin berlibur di Taiwan. Annie '
            'menanyakan perjalanannya, dan Meimei bertanya tentang kakaknya.', [
        ('在學校', 'Di kampus', [
            ('安妮', '大文，你回來了！你是什麼時候回來的？', 'Dawen, kamu sudah kembali! Kapan kamu kembali?'),
            ('王大文', '我是昨天晚上回來的。', 'Aku kembali kemarin malam.'),
            ('安妮', '你是一個人回來的嗎？', 'Kamu kembali sendirian?'),
            ('王大文', '不是，我是跟我姊姊一起來的。她要在臺灣旅行。', 'Bukan, aku datang bersama kakak perempuanku. Dia mau jalan-jalan di Taiwan.'),
            ('安妮', '你們坐了幾個小時的飛機？', 'Kalian naik pesawat berapa jam?'),
            ('王大文', '坐了五個小時。', 'Lima jam.'),
        ]),
        ('下午', 'Sore hari', [
            ('李美美', '大文，你姊姊已經去了很多地方嗎？', 'Dawen, kakakmu sudah pergi ke banyak tempat?'),
            ('王大文', '對，她剛剛從淡水回來。她本來以為臺灣很小，可是她說好玩的地方很多。', 'Iya, dia baru saja kembali dari Tamsui. Awalnya dia kira Taiwan kecil, tapi katanya tempat seru banyak sekali.'),
            ('李美美', '她會說中文嗎？', 'Dia bisa bahasa Mandarin?'),
            ('王大文', '她只會說幾句，可是大家好像都懂！', 'Dia cuma bisa beberapa kalimat, tapi sepertinya semua orang mengerti!'),
            ('李美美', '當然懂！臺灣人很喜歡聽外國人說中文。', 'Tentu saja mengerti! Orang Taiwan suka sekali mendengar orang asing bicara Mandarin.'),
            ('王大文', '對了，她有一件事情想問你：哪個夜市好玩？', 'Oh iya, ada satu hal yang ingin dia tanyakan padamu: pasar malam mana yang seru?'),
        ]),
    ]),
})

# ---- kelompok 3 (B34–B46) ----
BARU.update({
    'B34': ('Dawen dan Meimei berwisata sehari ke pantai. Begitu turun dari bus mereka melihat laut; sorenya mereka '
            'berjalan ke tepi sungai dan mencoba memotret burung.', [
        ('在海邊', 'Di tepi laut', [
            ('王大文', '美美，你看！一下車就看到海了！', 'Meimei, lihat! Begitu turun dari bus langsung kelihatan laut!'),
            ('李美美', '風景真漂亮！我們走下去吧。', 'Pemandangannya indah sekali! Ayo kita turun ke sana.'),
            ('王大文', '好。這裡的草很綠，地上也很乾淨。', 'Oke. Rumput di sini hijau sekali, tanahnya juga bersih.'),
            ('李美美', '你看，海上有很多鳥。', 'Lihat, di atas laut banyak burung.'),
            ('王大文', '我一看到海，就很高興。', 'Begitu melihat laut, aku langsung senang.'),
            ('李美美', '我們坐下來休息一下吧。', 'Kita duduk istirahat sebentar yuk.'),
        ]),
        ('下午，在河邊', 'Sore hari, di tepi sungai', [
            ('李美美', '這條河一直到海。', 'Sungai ini mengalir terus sampai ke laut.'),
            ('王大文', '你看，那片草上有很多鳥！', 'Lihat, di padang rumput itu banyak burung!'),
            ('李美美', '好漂亮！我要照相，你不要走過去！', 'Cantik sekali! Aku mau memotret, kamu jangan ke sana!'),
            ('王大文', '好……啊，鳥一看到你，就飛走了！', 'Oke… Aduh, burungnya begitu melihatmu langsung terbang pergi!'),
        ]),
    ]),
    'B35': ('Dawen, Zhiming, dan Annie berlibur ke Hualien. Dawen melakukan check-in dan membayarkan kamar untuk '
            'kedua temannya; malam harinya Annie bercerita bahwa ibunya mengizinkannya ikut dengan satu syarat.', [
        ('在旅館', 'Di penginapan', [
            ('王大文', '你好，我們有三個人，我跟我的兩個朋友。', 'Halo, kami bertiga, saya dan dua teman saya.'),
            ('小姐', '好。你們住幾天？', 'Baik. Kalian menginap berapa hari?'),
            ('王大文', '兩天。我的朋友在外面，我可以替他們付錢嗎？', 'Dua hari. Teman saya di luar, boleh saya bayarkan untuk mereka?'),
            ('小姐', '行。', 'Boleh.'),
            ('王大文', '房間可以看到海嗎？', 'Dari kamar bisa melihat laut?'),
            ('小姐', '行，你們的房間在五樓，可以看到海。', 'Bisa, kamar kalian di lantai lima, bisa melihat laut.'),
        ]),
        ('晚上，在房間', 'Malam hari, di kamar', [
            ('志明', '大文，謝謝你替我付錢！', 'Dawen, terima kasih sudah membayarkan untukku!'),
            ('王大文', '沒關係，明天你請我吃早飯吧！', 'Tidak apa-apa, besok kamu traktir aku sarapan ya!'),
            ('安妮', '我媽媽讓我跟你們一起來，可是她要我每天打電話給她。', 'Ibuku mengizinkan aku pergi bersama kalian, tapi dia minta aku menelepon dia setiap hari.'),
            ('志明', '那你現在打吧！', 'Kalau begitu telepon sekarang saja!'),
            ('安妮', '好。我和媽媽說話，你們先睡覺吧。', 'Oke. Aku bicara dengan ibuku, kalian tidur duluan saja.'),
            ('王大文', '明天早上，我們和旅館的人一起去看海，行嗎？', 'Besok pagi kita lihat laut bersama orang penginapan, mau?'),
            ('志明', '行！', 'Mau!'),
        ]),
    ]),
    'B36': ('Dawen ingin mengirim surat dan teh untuk ibunya di Indonesia. Ia meminjam pulpen Meimei, menanyakan '
            'letak kantor pos, lalu mengirim paketnya.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，我可以借你的筆嗎？我要寫信給我媽媽。', 'Meimei, boleh pinjam pulpenmu? Aku mau menulis surat untuk ibuku.'),
            ('李美美', '可以。你要寄到印尼嗎？', 'Boleh. Mau dikirim ke Indonesia?'),
            ('王大文', '對。郵局在哪裡？', 'Iya. Kantor posnya di mana?'),
            ('李美美', '郵局在銀行旁邊。你也要去銀行嗎？', 'Kantor pos di sebelah bank. Kamu juga mau ke bank?'),
            ('王大文', '要，我要去拿錢。銀行幾點開？', 'Iya, aku mau ambil uang. Bank buka jam berapa?'),
            ('李美美', '九點。郵局八點就開了。', 'Jam sembilan. Kantor pos sudah buka jam delapan.'),
        ]),
        ('在郵局', 'Di kantor pos', [
            ('王大文', '你好，請問，寄信到印尼要多少錢？', 'Halo, permisi, kirim surat ke Indonesia berapa?'),
            ('小姐', '四十塊。', 'Empat puluh.'),
            ('王大文', '這裡可以買郵票嗎？', 'Di sini bisa beli perangko?'),
            ('小姐', '可以。你還要寄別的東西嗎？', 'Bisa. Masih mau kirim barang lain?'),
            ('王大文', '還要寄這個茶給我媽媽。', 'Masih mau kirim teh ini untuk ibu saya.'),
            ('小姐', '好，一共三百二十塊。', 'Baik, semuanya tiga ratus dua puluh.'),
            ('王大文', '謝謝！我媽媽一定很高興。', 'Terima kasih! Ibu saya pasti senang sekali.'),
        ]),
    ]),
    'B37': ('Di halte bus Dawen sadar dompetnya hilang. Meimei membantunya mengingat kapan terakhir memakainya; '
            'malamnya mereka kembali ke kios sate di pasar malam — dan dompetnya ada di sana.', [
        ('在公車站', 'Di halte bus', [
            ('王大文', '美美，我的錢包不見了！怎麼辦？', 'Meimei, dompetku hilang! Bagaimana ini?'),
            ('李美美', '你先坐下來。你的錢包掉在哪裡？', 'Kamu duduk dulu. Dompetmu jatuh di mana?'),
            ('王大文', '我不知道。可能掉在公車上，也可能被別人拿走了。', 'Aku tidak tahu. Mungkin jatuh di bus, mungkin juga diambil orang.'),
            ('李美美', '你最後一次用錢包，是什麼時候？', 'Terakhir kali kamu pakai dompet kapan?'),
            ('王大文', '昨天晚上，在夜市買烤肉。', 'Kemarin malam, waktu beli sate di pasar malam.'),
            ('李美美', '我們先打電話給銀行，然後去夜市問一下。', 'Kita telepon bank dulu, lalu tanya ke pasar malam.'),
        ]),
        ('晚上，在夜市', 'Malam hari, di pasar malam', [
            ('王大文', '老闆，請問，你看見一個黑色的錢包嗎？', 'Pak, permisi, Bapak lihat dompet hitam?'),
            ('老闆', '有！昨天你的錢包掉在地上，在火的旁邊！我拿給你。', 'Ada! Kemarin dompetmu jatuh di tanah, di dekat api! Saya ambilkan.'),
            ('王大文', '太好了！謝謝老闆！', 'Syukurlah! Terima kasih, Pak!'),
            ('李美美', '以後你的錢包要放在背包裡！', 'Lain kali dompetmu taruh di dalam ransel!'),
        ]),
    ]),
    'B38': ('Di tepi sungai Dawen ingin berenang, tetapi ada papan larangan. Keesokan harinya Guru Chen menjelaskan '
            'aturan ujian, dan Dawen bertanya apa saja yang boleh.', [
        ('在河邊', 'Di tepi sungai', [
            ('王大文', '天氣好熱，我想游泳！', 'Panas sekali, aku ingin berenang!'),
            ('李美美', '你看，那裡寫著：「這裡不能游泳」。', 'Lihat, di sana tertulis: "Dilarang berenang di sini".'),
            ('王大文', '為什麼不能？', 'Kenapa tidak boleh?'),
            ('李美美', '這條河的水很多，也很快。你要小心！', 'Air sungai ini banyak, arusnya juga deras. Kamu harus hati-hati!'),
            ('王大文', '好，不游了。', 'Oke, tidak jadi berenang.'),
            ('李美美', '那邊可以坐，我們去那邊休息吧。', 'Di sana boleh duduk, kita istirahat di sana saja.'),
        ]),
        ('第二天，在教室', 'Keesokan harinya, di kelas', [
            ('陳老師', '同學們注意，明天的考試很重要。', 'Anak-anak, perhatikan, ujian besok sangat penting.'),
            ('安妮', '老師，考試能帶字典嗎？', 'Bu, ujian boleh bawa kamus?'),
            ('陳老師', '不能。手機也不能帶。', 'Tidak boleh. HP juga tidak boleh dibawa.'),
            ('王大文', '能喝水嗎？', 'Boleh minum?'),
            ('陳老師', '能。', 'Boleh.'),
            ('王大文', '那……能睡覺嗎？', 'Kalau… boleh tidur?'),
            ('陳老師', '不能！', 'Tidak boleh!'),
        ]),
    ]),
    'B39': ('Pagi hari Zhiming melihat wajah Dawen pucat: perutnya sakit setelah makan banyak di pasar malam. Zhiming '
            'mengantarnya ke rumah sakit.', [
        ('在家', 'Di rumah', [
            ('志明', '大文，你怎麼了？你的臉很白！', 'Dawen, kamu kenapa? Wajahmu pucat sekali!'),
            ('王大文', '我肚子很痛。', 'Perutku sakit sekali.'),
            ('志明', '為什麼？你吃了什麼？', 'Kenapa? Kamu makan apa?'),
            ('王大文', '昨天晚上在夜市吃了很多東西。', 'Kemarin malam aku makan banyak di pasar malam.'),
            ('志明', '我們去醫院吧！', 'Ayo kita ke rumah sakit!'),
        ]),
        ('在醫院', 'Di rumah sakit', [
            ('志明', '護士小姐，我的朋友肚子很痛！', 'Suster, perut teman saya sakit sekali!'),
            ('護士', '你好，你是病人嗎？你怎麼了？', 'Halo, Anda pasiennya? Ada keluhan apa?'),
            ('王大文', '我肚子痛，頭也有點痛。', 'Perut saya sakit, kepala juga agak sakit.'),
            ('護士', '請你在這裡等一下，醫生馬上來。', 'Silakan tunggu di sini sebentar, dokter segera datang.'),
            ('志明', '大文，你的頭髮上都是水，你很熱嗎？', 'Dawen, rambutmu basah semua, kamu kepanasan?'),
            ('王大文', '不熱，我很冷……肚子好痛！', 'Tidak panas, aku kedinginan… Perutku sakit sekali!'),
            ('志明', '別怕，我在這裡。', 'Jangan takut, aku di sini.'),
        ]),
    ]),
    'B40': ('Masih sakit, Dawen menelepon Guru Chen untuk izin tidak masuk kelas. Sorenya Meimei datang menjenguk '
            'dan menasihatinya supaya tidur lebih awal.', [
        ('打電話給老師', 'Menelepon guru', [
            ('王大文', '陳老師，對不起，因為我生病了，所以今天不能上課。', 'Bu Chen, maaf, karena saya sakit, hari ini saya tidak bisa masuk kelas.'),
            ('陳老師', '沒關係，健康最重要。你要多休息。', 'Tidak apa-apa, kesehatan yang paling penting. Kamu harus banyak istirahat.'),
            ('王大文', '謝謝老師。但是明天有考試……', 'Terima kasih, Bu. Tapi besok ada ujian…'),
            ('陳老師', '你好了才來上課，以後再考。', 'Kamu masuk kelas lagi kalau sudah sembuh saja, ujiannya nanti.'),
        ]),
        ('美美來看大文', 'Meimei menjenguk Dawen', [
            ('李美美', '大文，你好一點了嗎？', 'Dawen, sudah agak baikan?'),
            ('王大文', '好一點了，不過還很累。', 'Sudah agak baikan, tapi masih capek sekali.'),
            ('李美美', '因為你常常很晚睡覺，所以身體不好。', 'Karena kamu sering tidur larut malam, makanya badanmu tidak sehat.'),
            ('王大文', '對。雖然功課很多，但是以後我要早一點睡覺。', 'Iya. Meskipun PR-nya banyak, mulai sekarang aku mau tidur lebih awal.'),
            ('李美美', '我給你帶了水果，多吃一點吧。', 'Aku bawakan buah, makan yang banyak ya.'),
        ]),
    ]),
    'B41': ('Dawen lupa ulang tahun Annie, dan Annie marah. Meimei menyarankan ia datang ke acara makan Annie '
            'dengan membawa hadiah; keesokan harinya mereka berbaikan.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，你為什麼很難過？', 'Dawen, kenapa kamu sedih?'),
            ('王大文', '安妮很生氣，因為我忘了她的生日。', 'Annie marah sekali, karena aku lupa ulang tahunnya.'),
            ('李美美', '你跟她說對不起了嗎？', 'Kamu sudah minta maaf padanya?'),
            ('王大文', '說了。雖然我說了對不起，可是她還很生氣。', 'Sudah. Meskipun aku sudah minta maaf, dia masih marah.'),
            ('李美美', '聽說她明天要請朋友吃飯，你也去吧，送她一個東西。', 'Dengar-dengar besok dia mau mentraktir teman-temannya makan, kamu datang juga, beri dia sesuatu.'),
            ('王大文', '送什麼好？', 'Bagusnya beri apa?'),
            ('李美美', '比方說，蛋糕或是花。她喜歡吃甜的。', 'Misalnya kue atau bunga. Dia suka yang manis-manis.'),
        ]),
        ('第二天', 'Keesokan harinya', [
            ('王大文', '美美，我跟安妮說話了！她笑了。', 'Meimei, aku sudah bicara dengan Annie! Dia tersenyum.'),
            ('李美美', '太好了！昨天她哭了，今天笑了。', 'Syukurlah! Kemarin dia menangis, hari ini tersenyum.'),
            ('王大文', '我送她一個生日蛋糕，她很高興，她說她不生氣了。', 'Aku memberinya kue ulang tahun, dia senang sekali, katanya dia sudah tidak marah lagi.'),
        ]),
    ]),
    'B42': ('Dawen menebak siapa gadis yang disukai Zhiming, teman sekamarnya. Keesokan harinya ia bertanya kepada '
            'Annie apa pendapatnya tentang Zhiming.', [
        ('在家', 'Di rumah', [
            ('王大文', '志明，你喜歡的人是誰？', 'Zhiming, orang yang kamu suka siapa?'),
            ('志明', '我不告訴你！', 'Tidak akan kuberi tahu!'),
            ('王大文', '是我們班的同學嗎？', 'Teman sekelas kita?'),
            ('志明', '她很聰明，也很可愛。她說的話都很有意思。', 'Dia pintar sekali, juga imut. Semua yang dia katakan menarik.'),
            ('王大文', '是安妮嗎？', 'Annie, ya?'),
            ('志明', '……你真不笨！', '…Kamu ternyata tidak bodoh!'),
        ]),
        ('第二天，在教室', 'Keesokan harinya, di kelas', [
            ('王大文', '安妮，你覺得志明這個人怎麼樣？', 'Annie, menurutmu Zhiming itu orangnya bagaimana?'),
            ('安妮', '他常常很奇怪，可是他的心很好。', 'Dia sering aneh, tapi hatinya baik.'),
            ('王大文', '他送你的書有用嗎？', 'Buku yang dia berikan padamu berguna?'),
            ('安妮', '很有用！你看，他今天也從書包裡拿出一本書給我。', 'Berguna sekali! Lihat, hari ini dia juga mengeluarkan sebuah buku dari tasnya untukku.'),
            ('王大文', '他是一個很好的朋友！', 'Dia teman yang baik sekali!'),
        ]),
    ]),
    'B43': ('Besok Dawen harus berpidato dalam bahasa Mandarin di depan kelas dan ia gugup sekali. Meimei '
            'menyemangatinya; setelah pidato, Dawen menyadari bahwa itu menyenangkan.', [
        ('說話比賽以前', 'Sebelum lomba pidato', [
            ('李美美', '大文，你看起來很緊張。', 'Dawen, kamu kelihatan gugup sekali.'),
            ('王大文', '對，明天我要在大家前面說中文，我不敢。', 'Iya, besok aku harus bicara Mandarin di depan semua orang, aku tidak berani.'),
            ('李美美', '你是很用功的學生，我相信你！', 'Kamu mahasiswa yang rajin, aku percaya padamu!'),
            ('王大文', '謝謝。你說的話聽起來很對。', 'Terima kasih. Kata-katamu kedengarannya benar.'),
            ('李美美', '喝一點這個茶吧，有一點苦，可是很好喝。', 'Minum sedikit teh ini, agak pahit, tapi enak.'),
        ]),
        ('說話比賽以後', 'Setelah lomba pidato', [
            ('王大文', '美美，我發現在大家前面說中文很有意思！', 'Meimei, ternyata bicara Mandarin di depan semua orang itu menyenangkan!'),
            ('李美美', '你今天很辛苦！', 'Hari ini kamu sudah bekerja keras!'),
            ('王大文', '老師高興地說：「大文，你說得很好！」', 'Guru berkata dengan gembira: "Dawen, kamu bicara dengan bagus sekali!"'),
            ('李美美', '你看，我說你可以吧！', 'Tuh kan, sudah kubilang kamu bisa!'),
        ]),
    ]),
    'B44': ('Menjelang Tahun Baru Imlek, Meimei mengajak Dawen merayakannya bersama keluarganya di Taichung. Setelah '
            'liburan, Dawen dan Annie saling bercerita.', [
        ('過年以前', 'Sebelum Tahun Baru Imlek', [
            ('王大文', '美美，臺灣人過年做什麼？', 'Meimei, orang Taiwan merayakan Tahun Baru dengan apa?'),
            ('李美美', '過年，有的人回家，有的人去旅行。', 'Saat Tahun Baru, sebagian orang pulang kampung, sebagian lagi bepergian.'),
            ('王大文', '你呢？', 'Kamu?'),
            ('李美美', '我回臺中，我們家人一起吃飯。你也來吧！', 'Aku pulang ke Taichung, keluargaku makan bersama. Kamu ikut juga ya!'),
            ('王大文', '好！我想看臺灣的新年文化。', 'Oke! Aku ingin melihat budaya Tahun Baru di Taiwan.'),
        ]),
        ('過年以後', 'Setelah Tahun Baru', [
            ('安妮', '大文，你過年又去臺中了嗎？', 'Dawen, Tahun Baru kemarin kamu ke Taichung lagi?'),
            ('王大文', '對，我又去了。美美的媽媽又做了很多菜！', 'Iya, aku ke sana lagi. Ibu Meimei memasak banyak sekali lagi!'),
            ('安妮', '我們班的同學，有的回國，有的在臺灣過年。', 'Teman-teman sekelas kita, ada yang pulang ke negaranya, ada yang merayakan di Taiwan.'),
            ('王大文', '你呢？', 'Kamu sendiri?'),
            ('安妮', '我在宿舍看電視，又吃了很多餃子！', 'Aku nonton TV di asrama, dan makan banyak pangsit lagi!'),
        ]),
    ]),
    'B45': ('Di kelas, Guru Chen meminta pendapat tentang cara terbaik belajar Mandarin. Sesudah kelas, Annie '
            'menanyakan arti sebuah huruf kepada Dawen.', [
        ('上課的時候', 'Saat pelajaran', [
            ('陳老師', '大家認為學中文最重要的是什麼？', 'Menurut kalian, hal terpenting dalam belajar Mandarin apa?'),
            ('王大文', '我認為多說最重要。', 'Menurut saya, banyak bicara yang paling penting.'),
            ('陳老師', '這個想法很好。安妮呢？', 'Pendapat yang bagus. Kalau Annie?'),
            ('安妮', '中文，我希望每天都能練習。', 'Bahasa Mandarin, saya berharap bisa berlatih setiap hari.'),
            ('李美美', '我願意每天跟大家練習！', 'Saya bersedia berlatih dengan semuanya setiap hari!'),
        ]),
        ('下課以後', 'Sesudah kelas', [
            ('安妮', '大文，這個字是什麼意思？', 'Dawen, huruf ini artinya apa?'),
            ('王大文', '我又不是老師！你問美美吧。', 'Aku kan bukan guru! Tanya Meimei saja.'),
            ('安妮', '美美又不在這裡！', 'Meimei kan tidak ada di sini!'),
            ('王大文', '好吧……這個字，我也不認識。', 'Ya sudah… huruf ini aku juga tidak tahu.'),
        ]),
    ]),
    'B46': ('Adik Annie di Indonesia bingung memilih tempat kuliah. Lewat telepon Annie bercerita tentang Taiwan, '
            'dan adiknya memutuskan untuk kuliah di Taiwan.', [
        ('打電話到印尼', 'Menelepon ke Indonesia', [
            ('安妮的弟弟', '姊姊，我不知道要去哪裡念書。', 'Kak, aku tidak tahu mau kuliah di mana.'),
            ('安妮', '你打算念什麼？', 'Kamu berencana kuliah apa?'),
            ('安妮的弟弟', '我打算學中文。我想去日本或是臺灣。', 'Aku berencana belajar Mandarin. Aku ingin ke Jepang atau Taiwan.'),
            ('安妮', '臺灣很好！我在臺灣念書，很高興。', 'Taiwan bagus! Aku kuliah di Taiwan, senang sekali.'),
            ('安妮的弟弟', '你在臺灣念書累不累？', 'Kuliah di Taiwan capek tidak?'),
            ('安妮', '不累！你來，我就帶你去夜市。', 'Tidak! Kalau kamu datang, aku langsung ajak kamu ke pasar malam.'),
            ('安妮的弟弟', '好！我決定了，就去臺灣念書！', 'Oke! Aku sudah memutuskan, aku kuliah di Taiwan saja!'),
        ]),
        ('第二天，在學校', 'Keesokan harinya, di kampus', [
            ('王大文', '安妮，你昨天沒來上課，怎麼了？', 'Annie, kemarin kamu tidak masuk kelas, kenapa?'),
            ('安妮', '我跟我弟弟打電話，打了三個小時！', 'Aku teleponan dengan adikku, sampai tiga jam!'),
            ('王大文', '他決定了嗎？', 'Dia sudah memutuskan?'),
            ('安妮', '決定了！他明年就來臺灣。', 'Sudah! Tahun depan dia datang ke Taiwan.'),
            ('王大文', '太好了！他來了，我們帶他去吃小吃！', 'Asyik! Kalau dia sudah datang, kita ajak dia makan jajanan!'),
        ]),
    ]),
})
