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
            ('陳老師', '安妮，歡迎你！這是我爸爸，這是我的兒子們。', 'Annie, selamat datang! Ini ayah saya, ini anak-anak saya.'),
            ('安妮', '老先生好！小朋友們好！', 'Selamat sore, Pak! Halo, adik-adik!'),
            ('陳老師', '其他的新同學呢？', 'Mahasiswa baru yang lain di mana?'),
            ('李美美', '他們在那邊跟大家聊天呢。安妮今天也認識很多新朋友！', 'Mereka lagi ngobrol dengan semua orang di sana. Annie hari ini juga kenalan dengan banyak teman baru!'),
            ('安妮', '對，我今天很高興！我們下個星期見面吧！', 'Iya, hari ini aku senang sekali! Minggu depan kita ketemu lagi ya!'),
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
    'B13': ('Dawen mendaftar kelas renang kampus. Petugas memintanya mengisi formulir: alamat, nomor telepon, umur, '
            'dan foto. Besoknya ia bercerita kepada Meimei tentang kelas itu.', [
        ('在學校辦公室', 'Di kantor kampus', [
            ('小姐', '你好，你要參加游泳課嗎？', 'Halo, kamu mau ikut kelas renang?'),
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
            ('李美美', '大文，游泳課有多少人？', 'Dawen, kelas renangnya berapa orang?'),
            ('王大文', '三十多個人。所有的人都是我們學校的學生。', 'Tiga puluhan orang. Semuanya mahasiswa kampus kita.'),
            ('李美美', '一個星期上幾次課？', 'Seminggu berapa kali pertemuan?'),
            ('王大文', '兩次，一次一個多小時。', 'Dua kali, sekali lebih dari satu jam.'),
            ('李美美', '游泳課的人全部都是外國人嗎？', 'Peserta kelas renang semuanya orang asing?'),
            ('王大文', '不是，二十多個是臺灣人。', 'Bukan, dua puluhan orang Taiwan.'),
            ('李美美', '很好！下個月我也想參加。', 'Bagus! Bulan depan aku juga mau ikut.'),
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
        ('第二天，在宿舍', 'Keesokan harinya, di asrama', [
            ('志明', '謝謝你們！這個蛋糕的味道很好，不太甜。', 'Terima kasih! Rasa kuenya enak, tidak terlalu manis.'),
            ('王大文', '我們還買了點心，有甜的，也有鹹的。', 'Kami juga beli camilan, ada yang manis, ada juga yang asin.'),
            ('志明', '我也買了一個點心，你們吃一點吧！', 'Aku juga beli camilan, kalian makan sedikit ya!'),
            ('李美美', '啊，好臭啊！', 'Aduh, bau sekali!'),
            ('志明', '這個點心又臭又香，臺灣人很喜歡吃。', 'Camilan ini bau tapi harum, orang Taiwan suka sekali.'),
            ('王大文', '……有一點辣，也有一點酸，很好吃！', '…Agak pedas, juga agak asam, enak sekali!'),
        ]),
    ]),
}
