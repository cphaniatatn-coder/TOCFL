"""Perbaikan kewajaran dialog (2026-09-28): daftar perubahan per baris + penerap yang menjaga format tulisan tangan.

Setiap perubahan: (modul, dialog, baris, aksi, pembicara, zh, terjemahan Indonesia)
  aksi 'ubah'  = ganti baris itu (pembicara None = tetap)
       'sisip' = sisipkan baris baru SESUDAH baris itu
       'pecah' = baris itu dan sesudahnya dipindah ke dialog baru (zh = tempat, id = judul Indonesia)
       'tempat'= ganti nama tempat dialog (zh = tempat baru)
       'hapus' = hapus baris itu
Pinyin dibuat otomatis (pypinyin + sandhi 一/不 + bacaan Taiwan) lalu dicek pisah() di bangun_modul.py.

Pemakaian: py _kerja/dialog_natural.py          (pratinjau pinyin)
           py _kerja/dialog_natural.py tulis    (terapkan ke _kerja/isi/*.json)
"""
import glob, json, os, re, sys
from pypinyin import pinyin, Style

K = os.path.dirname(os.path.abspath(__file__))

UBAH = [
    ('A09', 0, 1, 'ubah', None, '有床、桌子、椅子，還有一個電視。', 'Ada tempat tidur, meja, kursi, dan juga sebuah TV.'),
    ('A09', 1, 3, 'ubah', None, '是，她喜歡看電視。電視在床前面。', 'Iya, dia suka nonton TV. TV-nya di depan tempat tidur.'),
    ('A10', 0, 3, 'ubah', None, '你好早！你晚上幾點睡覺？', 'Pagi sekali! Malam kamu tidur jam berapa?'),
    ('A13', 1, 7, 'ubah', None, '我不知道。我們去問老師吧。', 'Tidak tahu. Ayo kita tanya guru.'),
    ('A17', 1, 2, 'ubah', '王大文', '美美，牛肉麵怎麼吃？', 'Meimei, mi daging sapi makannya bagaimana?'),
    ('A17', 1, 3, 'ubah', '李美美', '你先吃麵，然後喝湯。別吃太快，我吃飯很慢！', 'Makan minya dulu, lalu minum kuahnya. Jangan terlalu cepat, aku makannya lambat!'),
    ('A22', 1, 1, 'ubah', None, '你是不是生病？你沒吃早餐嗎？', 'Kamu sakit, ya? Kamu tidak sarapan?'),
    ('A23', 0, 2, 'ubah', None, '你不舒服，應該告訴老師。', 'Kamu tidak enak badan, sebaiknya bilang ke guru.'),
    ('A23', 1, 2, 'ubah', None, '你是感冒。你應該多休息，多喝水。', 'Kamu kena flu. Sebaiknya banyak istirahat dan minum air.'),
    ('A25', 0, 3, 'pecah', None, '晚上，打電話', 'Malam, menelepon'),
    ('B02', 1, 2, 'ubah', None, '我也喜歡聽音樂，也喜歡看故事書。', 'Aku juga suka dengar musik, juga suka baca buku cerita.'),
    ('B02', 1, 3, 'ubah', None, '你看，這本書的圖很漂亮！', 'Lihat, gambar di buku ini cantik!'),
    ('B02', 1, 3, 'sisip', '王大文', '對！美美，我們一起照相吧。', 'Iya! Meimei, ayo kita foto bareng.'),
    ('B02', 1, 4, 'sisip', '李美美', '好！然後你給我一張相片吧。', 'Oke! Nanti kasih aku satu fotonya, ya.'),
    ('B04', 0, 4, 'ubah', None, '我們一會兒再聊吧！', 'Nanti kita ngobrol lagi, ya!'),
    ('B06', 1, 2, 'ubah', None, '那邊的大人和小朋友們是誰？', 'Orang dewasa dan anak-anak di sana siapa?'),
    ('B06', 1, 4, 'ubah', None, '今天有各國的學生，大家見面都很高興！我們也去跟別人聊天吧！', 'Hari ini ada mahasiswa dari berbagai negara, semua senang bertemu! Ayo kita juga ngobrol dengan yang lain!'),
    ('B09', 1, 2, 'ubah', None, '好。天氣太熱了，我們開窗戶吧。你把燈關了，好不好？', 'Oke. Panas sekali, kita buka jendela saja. Tolong matikan lampunya, ya?'),
    ('B10', 1, 4, 'ubah', None, '週一我很忙，週日有空。這個禮拜天我跟你去慢跑吧！', 'Senin aku sibuk, Minggu senggang. Minggu ini aku ikut jogging!'),
    ('B11', 1, 3, 'ubah', None, '謝謝！可是我的中文還不夠好，你有什麼好辦法？', 'Makasih! Tapi Mandarinku belum cukup bagus, kamu punya cara yang bagus?'),
    ('B13', 0, 4, 'ubah', None, '好。你們的中文課有幾個學生？', 'Oke. Kelas Mandarinmu ada berapa murid?'),
    ('B13', 0, 5, 'ubah', None, '有二十多個。男生有八個，女生有十多個。', 'Dua puluh lebih. Laki-lakinya delapan, perempuannya sepuluh lebih.'),
    ('B14', 1, 5, 'ubah', None, '一部分學生的成績很好。這所學校很不錯。', 'Sebagian murid nilainya bagus. Sekolah ini cukup bagus.'),
    ('B16', 0, 3, 'ubah', None, '你要用功。每天寫新字，就會記得。', 'Harus rajin. Tulis karakter baru tiap hari, nanti pasti ingat.'),
    ('B17', 0, 0, 'tempat', None, '在圖書館', ''),
    ('B17', 0, 1, 'ubah', None, '圖書館的書很多，我們一起找吧。', 'Buku di perpustakaan banyak, ayo cari bareng.'),
    ('B19', 1, 0, 'ubah', None, '你看這張圖：印尼在臺灣的南邊。世界真大！', 'Lihat gambar ini: Indonesia di sebelah selatan Taiwan. Dunia ini luas sekali!'),
    ('B19', 1, 3, 'ubah', None, '火車站的聲音比公園大，我比較喜歡公園！', 'Suara di stasiun lebih keras daripada di taman, aku lebih suka taman!'),
    ('B21', 1, 3, 'ubah', None, '你兩雙都買吧！我去旁邊的店買兩支筆。', 'Beli dua-duanya saja! Aku ke toko sebelah beli dua pulpen.'),
    ('B24', 0, 3, 'ubah', None, '味道很好！可是糖放得太多了，我少吃一點。', 'Rasanya enak! Tapi gulanya terlalu banyak, aku makan sedikit saja.'),
    ('B24', 1, 3, 'ubah', None, '你看，那個點心的味道很臭，可是很好吃！', 'Lihat, kudapan itu baunya busuk, tapi enak!'),
    ('B26', 1, 2, 'ubah', None, '我要西瓜的。我不喜歡喝汽水和啤酒。這裡的香蕉好吃嗎？', 'Aku mau yang semangka. Aku tidak suka soda dan bir. Pisang di sini enak?'),
    ('B27', 0, 0, 'ubah', None, '美美，夜市的人好多！你想吃什麼？', 'Meimei, pasar malam ramai sekali! Kamu mau makan apa?'),
    ('B27', 0, 1, 'ubah', None, '夜市的小吃有很多種。我們買饅頭和餃子吧！', 'Jajanan pasar malam banyak macamnya. Kita beli mantou dan pangsit, yuk!'),
    ('B27', 1, 3, 'ubah', None, '你可以幫我買一個三明治嗎？', 'Bisa belikan aku satu sandwich?'),
    ('B28', 1, 4, 'ubah', None, '吃飯以後，我們去茶館喝茶，好嗎？', 'Setelah makan kita minum teh di kedai teh, ya?'),
    ('B28', 1, 4, 'sisip', '李美美', '好啊。可是那家飯店的茶館那麼貴，我們去別的吧。', 'Boleh. Tapi kedai teh di hotel itu mahal sekali, kita ke tempat lain saja.'),
    ('B30', 1, 2, 'ubah', None, '從你們宿舍向左轉，是不是有一家超商？', 'Dari asramamu belok kiri, ada minimarket, kan?'),
    ('B30', 1, 3, 'ubah', None, '對，我明天上課以前去買東西。', 'Iya, besok sebelum kelas aku belanja ke sana.'),
    ('B31', 1, 2, 'ubah', None, '好。公共汽車很方便，司機也很好。', 'Oke. Bus kota praktis, sopirnya juga baik.'),
    ('B33', 1, 4, 'sisip', '王大文', '有！我在夜市吃了很多小吃，還交了新朋友。', 'Ada! Aku makan banyak jajanan di pasar malam, juga dapat teman baru.'),
    ('B36', 1, 1, 'ubah', None, '可以。你要寫信給誰？', 'Boleh. Mau menulis surat ke siapa?'),
    ('B36', 1, 2, 'ubah', None, '給我媽媽。我也要去銀行拿錢。銀行幾點開？', 'Untuk ibuku. Aku juga mau ambil uang di bank. Bank buka jam berapa?'),
    ('B39', 1, 3, 'ubah', None, '大文，你的頭髮上都是水，你很熱嗎？別怕，我在這裡。', 'Dawen, rambutmu basah semua, kamu kepanasan? Jangan takut, aku di sini.'),
    ('B41', 1, 1, 'ubah', None, '太好了！昨天她哭了，今天笑了。你做了什麼？', 'Bagus! Kemarin dia menangis, hari ini tersenyum. Kamu melakukan apa?'),
    ('B41', 1, 2, 'ubah', None, '很多事！比方說，我送她一個生日蛋糕，她很高興。', 'Banyak! Misalnya, aku memberinya kue ulang tahun, dia senang sekali.'),
    ('B42', 0, 3, 'ubah', None, '我不告訴你！你看，老師走進教室了，我們快去上課吧。', 'Tidak kuberi tahu! Lihat, guru sudah masuk kelas, ayo cepat masuk.'),
    ('B42', 1, 2, 'ubah', None, '她不笨，她很聰明，她的心也很好。今天她從書包裡拿出她昨天買的書，送給我了！', 'Dia tidak bodoh, dia pintar, hatinya juga baik. Hari ini dia mengeluarkan buku yang kemarin dibelinya dari tas, lalu memberikannya padaku!'),
    ('B45', 0, 1, 'ubah', None, '我認為多說最重要。', 'Menurut saya banyak bicara paling penting.'),
    ('B45', 0, 2, 'ubah', None, '這個想法很好。美美呢？', 'Ide ini bagus. Meimei?'),
    ('B46', 0, 0, 'ubah', None, '姊姊，我不知道要去哪裡念書。', 'Kak, aku tidak tahu mau kuliah di mana.'),
    ('C03', 1, 2, 'ubah', None, '好。可是這個袋子太小了。', 'Oke. Tapi kantong ini terlalu kecil.'),
    ('C05', 0, 2, 'ubah', None, '鎖了。你把信箱裡的信放在我的桌子上，好嗎？', 'Sudah. Tolong surat di kotak surat taruh di mejaku, ya?'),
    ('C06', 1, 2, 'ubah', None, '房東笑著說我們的浴室很乾淨！', 'Pemilik rumah bilang sambil tersenyum bahwa kamar mandi kita bersih!'),
    ('C07', 1, 2, 'ubah', None, '你應該早點睡覺。是不是枕頭不舒服？你常常做夢嗎？', 'Sebaiknya tidur lebih awal. Bantalnya tidak nyaman, ya? Kamu sering mimpi?'),
    ('C09', 1, 3, 'ubah', None, '我也想去印尼過那樣的生活，冬天也不冷！', 'Aku juga ingin ke Indonesia menjalani hidup seperti itu, musim dingin pun tidak dingin!'),
    ('C12', 1, 0, 'ubah', None, '你今年幾歲？', 'Tahun ini umur Anda berapa?'),
    ('C12', 1, 5, 'ubah', None, '去過。那時我年紀很小，才八歲，當時我不會說中文。', 'Pernah. Waktu itu saya masih kecil, baru delapan tahun, saat itu belum bisa bahasa Mandarin.'),
    ('C14', 1, 3, 'ubah', None, '五口人。我外婆已經是老太太了，她也要來。', 'Lima jiwa. Nenekku sudah sepuh, dia juga akan datang.'),
    ('C15', 0, 3, 'ubah', None, '不只是錢，我也想練習中文。來喝咖啡的客人都是臺灣人。', 'Bukan cuma uang, aku juga ingin berlatih Mandarin. Tamu yang minum kopi orang Taiwan semua.'),
    ('C15', 1, 2, 'ubah', None, '我爸爸是商人，我爺爺以前是工人。爸爸希望我以後也當商人……', 'Ayahku pedagang, kakekku dulu buruh. Ayah berharap nanti aku juga jadi pedagang…'),
    ('C15', 1, 3, 'ubah', None, '別想那麼多了！今天我替我媽媽去市場買菜，你要一起去嗎？', 'Jangan dipikirkan terlalu banyak! Hari ini aku menggantikan ibuku belanja ke pasar, mau ikut?'),
    ('C18', 1, 3, 'ubah', None, '好吧！新聞說明天熱得不得了，我們就在家玩遊戲吧。', 'Baiklah! Berita bilang besok panas luar biasa, kita main game di rumah saja.'),
    ('C21', 1, 3, 'ubah', None, '你說得很清楚，我都聽得懂。你的中文很標準，我也想說得跟你一樣好！', 'Kamu bicara jelas, aku paham semua. Mandarinmu baku sekali, aku juga ingin bicara sebagus kamu!'),
    ('C23', 1, 0, 'hapus', None, '', ''),
    ('C23', 1, 2, 'sisip', '李美美', '對！我們要好好利用這個假日！', 'Betul! Kita harus memanfaatkan libur ini sebaik-baiknya!'),
    ('C28', 0, 3, 'ubah', None, '流鼻水，也頭痛。', 'Pilek, juga sakit kepala.'),
    ('C29', 1, 0, 'ubah', None, '大文，你的臉色好多了！', 'Dawen, wajahmu sudah jauh lebih segar!'),
    ('C33', 0, 1, 'ubah', None, '明年六月。從明年起，我就不是學生了！', 'Juni tahun depan. Mulai tahun depan, aku bukan mahasiswa lagi!'),
    ('C36', 1, 1, 'ubah', None, '有。高級班的中文比較正式，還可以學到很多方面的知識，像是現代文化。', 'Ada. Mandarin di kelas lanjut lebih formal, juga bisa belajar pengetahuan dari banyak bidang, seperti budaya modern.'),
    ('C38', 1, 2, 'ubah', None, '許多同學說他們很忙，當中一半每天睡覺的時間只有六個小時。', 'Banyak teman bilang mereka sibuk, di antaranya setengah hanya tidur enam jam sehari.'),
    ('C41', 0, 3, 'ubah', None, '謝謝。我還要買手套和襪子。金色的上衣太貴了，我不買。', 'Makasih. Aku juga mau beli sarung tangan dan kaus kaki. Atasan emas itu terlalu mahal, aku tidak beli.'),
    ('C41', 1, 2, 'ubah', None, '這裡也有睡衣嗎？', 'Di sini ada piyama juga?'),
    ('C41', 1, 3, 'ubah', None, '有，那套睡衣看起來很舒服。', 'Ada, setelan piyama itu kelihatan nyaman.'),
    ('C42', 1, 0, 'ubah', '王大文', '美美，在臺灣吃飯要給小費嗎？', 'Meimei, makan di Taiwan perlu kasih tip?'),
    ('C42', 1, 1, 'ubah', '李美美', '不用。你不知道嗎？', 'Tidak perlu. Kamu tidak tahu?'),
    ('C42', 1, 2, 'ubah', '王大文', '我以為要給。你付錢了沒有？', 'Kukira perlu. Kamu sudah bayar belum?'),
    ('C42', 1, 3, 'ubah', '李美美', '付了。店員刷了一下我的信用卡。', 'Sudah. Kasir sudah menggesek kartu kreditku.'),
    ('C43', 1, 3, 'ubah', None, '對。我做生意做了二十年了。你們要好好地看！', 'Iya. Saya sudah berdagang dua puluh tahun. Lihat baik-baik ya!'),
    ('C44', 1, 2, 'ubah', None, '我看了看時鐘，現在三點鐘了，我們上課吧！', 'Aku lihat jam, sudah jam tiga, ayo masuk kelas!'),
    ('C50', 1, 1, 'ubah', None, '有。你有什麼問題，都可以提出來。', 'Ada. Kalau ada pertanyaan apa pun, silakan sampaikan.'),
    ('C51', 1, 1, 'ubah', None, '你手上的信封裡是什麼？', 'Amplop di tanganmu isinya apa?'),
    ('C51', 1, 2, 'ubah', None, '是兩封信，我要寄給媽媽。她收到了一定很高興。', 'Dua surat, mau kukirim ke ibu. Kalau diterima, dia pasti senang.'),
    ('C52', 1, 2, 'ubah', None, '沒有。我以為錢包丟了，後來找著了，在沙發底下。', 'Tidak. Kukira dompetku hilang, ternyata ketemu, di bawah sofa.'),
    ('C56', 1, 4, 'ubah', None, '有，可是東方的節日我也很喜歡。今年除夕，我可以去你家嗎？', 'Ada, tapi hari raya Timur juga kusukai. Malam Imlek tahun ini, boleh aku ke rumahmu?'),
    ('C56', 1, 4, 'sisip', '李美美', '當然可以！你想吃什麼，我們就做什麼！', 'Tentu boleh! Kamu mau makan apa, akan kami masakkan!'),
    ('C59', 1, 1, 'ubah', None, '老師，您願意幫我們看報告嗎？', 'Bu, Ibu bersedia membantu memeriksa laporan kami?'),
    ('C60', 1, 2, 'ubah', None, '我了解。你搬家是很自然的事。', 'Aku mengerti. Wajar kalau kamu pindah.'),
    ('C61', 0, 2, 'ubah', None, '這類的書我也不喜歡。我們去吃點心吧？', 'Buku jenis ini aku juga tidak suka. Kita makan kudapan, yuk?'),
    ('C61', 0, 3, 'ubah', None, '我中午吃得太飽，現在什麼都吃不下了。另外，我還得寫作業。', 'Siang tadi aku makan terlalu kenyang, sekarang tidak muat apa-apa lagi. Selain itu, aku masih harus mengerjakan PR.'),
    ('C63', 1, 0, 'ubah', None, '等到晚上，我請你吃飯吧。', 'Nanti malam, aku traktir makan ya.'),
    ('C63', 1, 2, 'ubah', None, '我沒有帶傘！你怎麼笑了起來？', 'Aku tidak bawa payung! Kenapa kamu malah tertawa?'),
]

# --- pinyin otomatis ---
from pypinyin import load_phrases_dict
KATA_PY = {  # bacaan Taiwan / nada netral sesuai data yang sudah ada
    '睡覺': 'shuì jiào', '姊姊': 'jiě jie', '乾淨': 'gān jìng', '認為': 'rèn wéi', '以為': 'yǐ wéi', '頭髮': 'tóu fǎ',
    '相片': 'xiàng piàn', '休息': 'xiū xí', '舒服': 'shū fu', '東西': 'dōng xi', '爸爸': 'bà ba', '媽媽': 'mā ma',
    '爺爺': 'yé ye', '謝謝': 'xiè xie', '枕頭': 'zhěn tou', '記得': 'jì de', '覺得': 'jué de', '找著': 'zhǎo zháo',
    '一會兒': 'yí huìr', '不得了': 'bù dé liǎo', '還得': 'hái děi', '好好': 'hǎo hǎo', '這個': 'zhè ge', '那個': 'nà ge',
    '比較': 'bǐ jiào', '了解': 'liǎo jiě', '小朋友': 'xiǎo péng yǒu', '朋友': 'péng yǒu',
}
load_phrases_dict({k: [[x] for x in v.replace('huìr', 'huì').split()] for k, v in KATA_PY.items() if 'huìr' not in v})
NAMA = {'大文': 'Dà wén', '美美': 'Měi měi', '志明': 'Zhì míng', '安妮': 'Ān nī', '小明': 'Xiǎo míng', '臺灣': 'Tái wān',
        '臺灣': 'Tái wān', '臺北': 'Tái běi', '臺中': 'Tái zhōng', '印尼': 'Yìn ní', '雅加達': 'Yǎ jiā dá', '中文': 'Zhōng wén'}
PUNC = {'，': ', ', '。': '. ', '！': '! ', '？': '? ', '、': ', ', '：': ': ', '「': ' "', '」': '" ', '……': '…… '}
NADA4 = re.compile('[àèìòùǜ]')


def _suku(p):
    """Suku kata per hanzi untuk satu potongan tanpa tanda baca."""
    sy = [x[0] for x in pinyin(p, style=Style.TONE)]
    for k, v in KATA_PY.items():          # paksa bacaan kata tertentu
        i = p.find(k)
        while i >= 0:
            vs = v.split()
            if k == '一會兒':
                sy[i:i + 3] = ['yí', 'huìr', '']
            else:
                sy[i:i + len(k)] = vs
            i = p.find(k, i + 1)
    for i, ch in enumerate(p):
        prev, nxt = p[i - 1] if i else '', p[i + 1] if i + 1 < len(p) else ''
        if ch == '個': sy[i] = 'ge'
        if ch == '和': sy[i] = 'hàn'
        if ch == '誰': sy[i] = 'shéi'
        if ch == '得' and prev and sy[i] == 'dé' and p[i - 1:i + 1] not in ('不得',): sy[i] = 'de'
        if ch == '地' and prev and prev == prev and p[i - 2:i] in ('好好', '慢慢') : sy[i] = 'de'
        if ch == '著' and sy[i] in ('zhù', 'zhuó', 'zháo') and p[i - 1:i + 1] != '找著': sy[i] = 'zhe'
        if ch == '不' and nxt and NADA4.search(sy[i + 1]): sy[i] = 'bú'
        if ch == '一':
            if prev in ('週', '期', '第', '十') or nxt in '二三四五六七八九十零月號' or not nxt:
                sy[i] = 'yī'
            else:
                sy[i] = 'yí' if NADA4.search(sy[i + 1]) else 'yì'
    return [s for s in sy if s], sy


def buat_py(zh):
    hasil = ''
    for p in re.split(r'(……|[，。！？、：「」])', zh):
        if not p:
            continue
        if p in PUNC:
            hasil = hasil.rstrip() + PUNC[p]
            continue
        _, sy = _suku(p)
        kata = []
        i = 0
        while i < len(p):
            n = next((n for n in sorted(NAMA, key=len, reverse=True) if p.startswith(n, i)), None)
            if n:
                kata.append(NAMA[n]); i += len(n)
            else:
                kata.append(sy[i]); i += 1
        hasil += ' '.join(k for k in kata if k) + ' '
    hasil = re.sub(r'\s+', ' ', hasil).strip().replace('" ', '"', 1) if hasil.count('"') == 0 else re.sub(r'\s+', ' ', hasil).strip()
    hasil = re.sub(r' ([,.!?:])', r'', hasil)
    return re.sub(r'(^|[.!?…] |")([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ])', lambda m: m.group(1) + m.group(2).upper(), hasil)


# --- penerap format-aman ---
def rentang_objek(s, i):
    a = s.rfind('{', 0, i)
    d, j = 0, a
    while True:
        if s[j] == '{': d += 1
        elif s[j] == '}':
            d -= 1
            if d == 0: return a, j + 1
        elif s[j] == '"':
            j += 1
            while s[j] != '"':
                j += 2 if s[j] == '\\' else 1
        j += 1


def tulis_objek(obj, contoh):
    if '\n' not in contoh:
        return json.dumps(obj, ensure_ascii=False)
    ind = re.search(r'\n(\s*)"', contoh).group(1)
    tutup = re.search(r'\n(\s*)\}$', contoh).group(1)
    return '{\n' + ',\n'.join(f'{ind}{json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}' for k, v in obj.items()) + '\n' + tutup + '}'


def cari_file(code):
    for f in sorted(glob.glob(f'{K}/isi/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        for m in (d['modules'] if 'modules' in d else [dict(d, code=os.path.basename(f)[:-5])]):
            if m['code'] == code:
                return f, m


def main(tulis):
    per_file = {}
    for u in UBAH:
        per_file.setdefault(cari_file(u[0])[0], []).append(u)
    for f, us in per_file.items():
        s = open(f, encoding='utf-8', newline='').read()
        for code, di, li, aksi, sp, zh, idn in us:
            dd = json.loads(s)   # keadaan terbaru (sesudah perubahan sebelumnya di file ini)
            m = next(x for x in (dd['modules'] if 'modules' in dd else [dict(dd, code=os.path.basename(f)[:-5])]) if x['code'] == code)
            d = m['dialogs'][di]
            l = d['lines'][li]
            # cari objek baris ini: zh-nya harus unik di dalam blok modul
            mulai = s.index(f'"code": "{code}"') if f'"code": "{code}"' in s else 0
            akhir = s.find('"code": "', mulai + 10); akhir = len(s) if akhir < 0 else akhir
            kunci = json.dumps(l['zh'], ensure_ascii=False)
            ds = s.find('"dialogs"', mulai, akhir); de = s.find('"tasks"', ds, akhir)
            mulai, akhir = ds, (akhir if de < 0 else de)
            pos = s.find(f'"zh": {kunci}', mulai, akhir)
            assert pos >= 0 and s.find(f'"zh": {kunci}', pos + 1, akhir) < 0, (code, l['zh'])
            a, b = rentang_objek(s, pos)
            lama = s[a:b]
            if aksi == 'ubah':
                baru = dict(json.loads(lama), zh=zh, py=buat_py(zh), id=idn)
                if sp: baru['sp'] = sp
                s = s[:a] + tulis_objek(baru, lama) + s[b:]
            elif aksi == 'sisip':
                baru = {'sp': sp, 'zh': zh, 'py': buat_py(zh), 'id': idn}
                sela = re.search(r',\s*$', s[:a]).group(0) if re.search(r',\s*$', s[:a]) else ',\n   '
                antara = s[b:s.find('{', b)] if s[b:].lstrip().startswith(',') else None
                pemisah = ',' + (re.search(r'\n\s*', s[a - 20:a]).group(0) if '\n' in s[a - 20:a] else ' ')
                s = s[:b] + pemisah + tulis_objek(baru, lama) + s[b:]
            elif aksi == 'hapus':
                kiri = re.search(r',\s*$', s[:a])
                if kiri:
                    s = s[:kiri.start()] + s[b:]
                else:
                    kanan = re.match(r'\s*,\s*', s[b:])
                    s = s[:a] + s[b + kanan.end():]
            elif aksi == 'tempat':
                p = s.rfind(f'"place": {json.dumps(d["place"], ensure_ascii=False)}', mulai, pos)
                assert p >= 0, (code, d['place'])
                s = s[:p] + f'"place": {json.dumps(zh, ensure_ascii=False)}' + s[p + len(f'"place": {json.dumps(d["place"], ensure_ascii=False)}'):]
            elif aksi == 'pecah':
                # tutup "lines" sebelum baris ini, buka dialog baru dengan tempat & judul baru
                prev_end = s.rfind('}', mulai, a) + 1
                ind_line = re.search(r'\n(\s*)$', s[:a])
                sela = s[prev_end:a]
                buka = '\n  ]},\n  {"place": ' + json.dumps(zh, ensure_ascii=False) + ', "title_id": ' + json.dumps(idn, ensure_ascii=False) + ', "lines": ['
                s = s[:prev_end] + buka + sela.replace(',', '', 1) + s[a:]
        json.loads(s)
        if tulis:
            open(f, 'w', encoding='utf-8', newline='').write(s)
        print(('ditulis ' if tulis else 'cek ok ') + os.path.basename(f))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'tulis':
        main(True)
    else:
        for u in UBAH:
            if u[3] in ('ubah', 'sisip'):
                print(u[0], u[1], u[2], u[3], u[5], '|', buat_py(u[5]))
        main(False)
