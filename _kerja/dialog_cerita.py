"""Tulis ulang 情境對話 berbasis cerita (keputusan Carli 2026-10-22).

Dialog lama Vol.3 banyak yang lompat topik (baris hanya ada untuk memamerkan satu kata). Dialog baru:
satu alur utuh (tujuan → masalah → penyelesaian); adegan kedua = kelanjutan sebab-akibat/waktu, bukan topik baru;
kata inti & 2 poin grammar dipakai secara alami; baris terakhir menuntaskan cerita.

BARU[kode] = (scene Indonesia, [(tempat, judul Indonesia, [(pembicara, zh, terjemahan Indonesia), ...]), ...])
Pinyin dibuat otomatis (buat_py di dialog_natural.py) lalu dicek pisah() di bangun_modul.py.
Modul mini (tocfl-mini) TIDAK disinkron ulang — instrumen uji coba dibekukan.

Pemakaian: py _kerja/dialog_cerita.py          (pratinjau)
           py _kerja/dialog_cerita.py tulis    (terapkan ke _kerja/isi/*.json)
"""
import json, re, sys

import dialog_natural
from dialog_natural import cari_file

dialog_natural.NAMA['北投'] = 'Běi tóu'
# bacaan yang ditebak salah oleh pypinyin: (potongan zh, pinyin salah, pinyin benar)
PERBAIKI = [('毛很長', 'máo hěn zhǎng', 'máo hěn cháng'), ('認識', 'rèn shí', 'rèn shì')]


def buat_py(zh):
    py = dialog_natural.buat_py(zh)
    for kunci, salah, benar in PERBAIKI:
        if kunci in zh:
            py = py.replace(salah, benar)
    return py

BARU = {
    'C24': ('Meimei mengajak ke pemandian air panas Beitou, tetapi berita memperkirakan topan datang. Mereka membuat '
            'rencana bersyarat, lalu memantau arah topan sampai Jumat malam.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，這個週末我們去北投的溫泉吧！', 'Dawen, akhir pekan ini kita ke pemandian air panas di Beitou yuk!'),
            ('王大文', '好啊！可是新聞說，週末大概會有颱風。', 'Boleh! Tapi kata berita, akhir pekan kemungkinan ada topan.'),
            ('李美美', '真的嗎？颱風現在在哪裡？', 'Serius? Topannya sekarang di mana?'),
            ('王大文', '颱風的中心在臺灣的南方，方向是往北。', 'Pusat topannya di sebelah selatan Taiwan, arahnya ke utara.'),
            ('李美美', '要是颱風來了，我們就不去了。', 'Kalau topannya datang, kita tidak jadi pergi.'),
            ('王大文', '好，我們星期五晚上再看一次新聞。', 'Oke, Jumat malam kita lihat berita sekali lagi.'),
        ]),
        ('星期五晚上，打電話', 'Jumat malam, menelepon', [
            ('李美美', '大文，你看新聞了嗎？颱風的方向變了！', 'Dawen, sudah lihat berita? Arah topannya berubah!'),
            ('王大文', '看了！颱風往東走了，不會來臺北。', 'Sudah! Topannya bergerak ke timur, tidak akan ke Taipei.'),
            ('李美美', '太好了！明天幾度？', 'Bagus! Besok berapa derajat?'),
            ('王大文', '大概二十度，不冷也不熱。溫泉的地點離捷運站遠嗎？', 'Sekitar dua puluh derajat, tidak dingin juga tidak panas. Lokasi pemandiannya jauh dari stasiun MRT?'),
            ('李美美', '不遠，走路五分鐘。下雨的話，我們就坐計程車。', 'Tidak jauh, jalan kaki lima menit. Kalau hujan, kita naik taksi saja.'),
            ('王大文', '好！聽說春季去溫泉最舒服，可是我等不了了！', 'Oke! Katanya ke pemandian air panas paling enak di musim semi, tapi aku sudah tidak sabar!'),
        ]),
    ]),
    'C30': ('Dawen duduk seharian menghafal untuk ujian sampai punggung dan kakinya sakit. Meimei mengajaknya jalan di '
            'taman, dan Dawen akhirnya mau berolahraga setiap hari.', [
        ('在宿舍', 'Di asrama', [
            ('李美美', '大文，你從早上到現在一直坐著，都沒動！', 'Dawen, dari pagi sampai sekarang kamu duduk terus, tidak bergerak sama sekali!'),
            ('王大文', '明天要考試，我還有很多東西要背。', 'Besok ujian, masih banyak yang harus kuhafal.'),
            ('李美美', '你一直低頭看電腦，眼睛不累嗎？', 'Kamu terus menunduk lihat komputer, matamu tidak capek?'),
            ('王大文', '眼睛很累，背和腿也很痛，痛死了！', 'Mataku capek sekali, punggung dan kaki juga sakit, sakit sekali!'),
            ('李美美', '你要多動一動，身體才會好。走，我們去公園散步！', 'Kamu harus lebih banyak bergerak, baru badanmu sehat. Ayo, kita jalan-jalan ke taman!'),
            ('王大文', '好吧。休息一下，才背得好。', 'Ya sudah. Istirahat sebentar, baru bisa menghafal dengan baik.'),
        ]),
        ('在公園', 'Di taman', [
            ('王大文', '走了半個小時，我的腿不痛了！', 'Setelah jalan setengah jam, kakiku tidak sakit lagi!'),
            ('李美美', '對吧！聽說常常運動的小孩，身高會比較高。', 'Tuh kan! Katanya anak yang sering olahraga, badannya lebih tinggi.'),
            ('王大文', '我已經二十二歲了，不會再長高了。', 'Aku sudah dua puluh dua tahun, tidak akan bertambah tinggi lagi.'),
            ('李美美', '你看那隻小狗，毛很長，跑得多快！', 'Lihat anjing kecil itu, bulunya panjang, larinya cepat sekali!'),
            ('王大文', '小狗都天天運動，我明天也要來散步。', 'Anjing kecil saja olahraga tiap hari, besok aku juga mau jalan-jalan ke sini.'),
            ('李美美', '你不是說運動很無聊嗎？', 'Bukannya kamu bilang olahraga itu membosankan?'),
            ('王大文', '我才不覺得無聊呢！跟你一起走，很有意思。', 'Aku sama sekali tidak merasa bosan! Jalan bareng kamu itu menyenangkan.'),
        ]),
    ]),
    'C44': ('Sweter yang Dawen beli kemarin kekecilan. Ia menukarnya di toko, memilih warna yang sedang tren, lalu di '
            'asrama Zhiming memuji sweter barunya.', [
        ('在衣服店', 'Di toko pakaian', [
            ('王大文', '小姐，我昨天在這裡買了這件毛衣，可是太小了。可以換一換嗎？', 'Mbak, kemarin saya beli sweter ini di sini, tapi terlalu kecil. Boleh ditukar?'),
            ('店員', '我看一看……可以。你要大一點的嗎？', 'Saya lihat sebentar… Boleh. Mau yang lebih besar?'),
            ('王大文', '對。這個顏色太淺了，有沒有深一點的？', 'Iya. Warna ini terlalu muda, ada yang lebih tua?'),
            ('店員', '有，這件深藍色的現在很流行。你試穿看看吧。', 'Ada, yang biru tua ini sedang tren. Coba dipakai saja.'),
            ('王大文', '剛好！前面這個圓圓的口袋也很特別。', 'Pas! Saku bulat di depannya juga unik.'),
            ('店員', '你的中文說得很好。你在臺灣住慣了嗎？', 'Bahasa Mandarin Anda bagus. Sudah terbiasa tinggal di Taiwan?'),
            ('王大文', '住慣了。可是我還買不慣這裡的衣服，大小常常買錯。', 'Sudah. Tapi saya masih belum terbiasa membeli baju di sini, ukurannya sering salah beli.'),
            ('店員', '沒關係，買錯了可以來換。我們六點鐘關門。', 'Tidak apa-apa, kalau salah beli boleh datang menukar. Kami tutup jam enam.'),
        ]),
        ('回到宿舍', 'Kembali ke asrama', [
            ('志明', '大文，你的新毛衣很好看！', 'Dawen, sweter barumu bagus!'),
            ('王大文', '昨天買的太小了，今天我去換了換，顏色也換了。', 'Yang kubeli kemarin terlalu kecil, hari ini aku tukar, warnanya juga kuganti.'),
            ('志明', '深藍色很適合你，現在很流行。', 'Biru tua cocok untukmu, sekarang sedang tren.'),
        ]),
    ]),
    'C61': ('Dawen tidak sanggup melanjutkan buku sejarah untuk tugas laporan. Meimei menyemangatinya dan meminjamkan '
            'novel; keesokan harinya Dawen justru membaca novel itu sampai larut malam.', [
        ('在圖書館', 'Di perpustakaan', [
            ('李美美', '大文，那本書你看完了嗎？', 'Dawen, buku itu sudah selesai kamu baca?'),
            ('王大文', '還沒。這本書相當無聊，我看不下去了。', 'Belum. Buku ini cukup membosankan, aku tidak sanggup melanjutkan.'),
            ('李美美', '可是老師說報告要用這本書，你還是要看下去。', 'Tapi kata guru laporannya harus pakai buku ini, kamu tetap harus terus membacanya.'),
            ('王大文', '我知道……可是這類的書，我真的不喜歡。', 'Aku tahu… tapi buku jenis ini aku benar-benar tidak suka.'),
            ('李美美', '另外，我有一本小說，很好看，你要不要？', 'Selain itu, aku punya satu novel, bagus sekali, kamu mau?'),
            ('王大文', '要！可是我的書包太小了，兩本書放不下。', 'Mau! Tapi tasku terlalu kecil, dua buku tidak muat.'),
            ('李美美', '我的書包放得下，我幫你拿。', 'Tasku muat, aku bawakan.'),
        ]),
        ('第二天', 'Keesokan harinya', [
            ('李美美', '大文，你看起來很累。', 'Dawen, kamu kelihatan capek.'),
            ('王大文', '你的小說太好看了，我一直看下去，看到半夜兩點！', 'Novelmu bagus sekali, aku terus membacanya sampai jam dua pagi!'),
            ('李美美', '那歷史書呢？', 'Lalu buku sejarahnya?'),
            ('王大文', '……今天晚上一定看完。', '…Malam ini pasti kuselesaikan.'),
        ]),
    ]),
    'C63': ('Dawen lupa bahwa hari ini ulang tahun Meimei dan baru teringat. Ia mentraktir sepulang kuliah, tetapi '
            'di jalan tiba-tiba hujan — dan Meimei malah tertawa.', [
        ('在學校', 'Di kampus', [
            ('李美美', '大文，今天是什麼日子，你知道嗎？', 'Dawen, hari ini hari apa, kamu tahu?'),
            ('王大文', '今天？星期五……我完全不知道。', 'Hari ini? Jumat… aku sama sekali tidak tahu.'),
            ('李美美', '上個月你說，今天要請我吃飯……', 'Bulan lalu kamu bilang hari ini mau mentraktirku makan…'),
            ('王大文', '啊，我想起來了！今天是你的生日！生日快樂！', 'Ah, aku ingat! Hari ini ulang tahunmu! Selamat ulang tahun!'),
            ('李美美', '原來你真的忘記了！', 'Ternyata kamu benar-benar lupa!'),
            ('王大文', '對不起！等到下課，我請你吃你最喜歡的牛肉麵。', 'Maaf! Nanti setelah kuliah selesai, aku traktir mi daging sapi kesukaanmu.'),
            ('李美美', '好，這次別再忘記了！', 'Oke, kali ini jangan lupa lagi!'),
        ]),
        ('下課以後，在路上', 'Sepulang kuliah, di jalan', [
            ('王大文', '你看，下起雨來了！我們都沒帶傘……', 'Lihat, mulai hujan! Kita berdua tidak bawa payung…'),
            ('李美美', '真好玩！', 'Seru sekali!'),
            ('王大文', '你怎麼笑起來了？下雨有什麼好玩的？', 'Kenapa kamu malah tertawa? Hujan apanya yang seru?'),
            ('李美美', '我想起來了，去年我的生日也下雨！', 'Aku jadi ingat, ulang tahunku tahun lalu juga hujan!'),
        ]),
    ]),
    'C64': ('Dawen tanpa sengaja bertemu teman SD-nya dari Indonesia di sebuah kedai kopi di Taipei, lalu bercerita '
            'kepada Meimei tentang pertemuan itu.', [
        ('在學校', 'Di kampus', [
            ('王大文', '美美，昨天在咖啡店，我見到了國小的同學！', 'Meimei, kemarin di kedai kopi aku ketemu teman SD-ku!'),
            ('李美美', '真的嗎？你們多久沒見面了？', 'Serius? Sudah berapa lama kalian tidak bertemu?'),
            ('王大文', '十年了！我們聊起了小時候的事，聊了三個小時。', 'Sepuluh tahun! Kami mengobrol tentang masa kecil, sampai tiga jam.'),
            ('李美美', '他還記得你小時候的樣子嗎？', 'Dia masih ingat kamu waktu kecil seperti apa?'),
            ('王大文', '記得！他說起我以前上課常常睡覺，我們都笑了。', 'Ingat! Dia cerita dulu aku sering tidur di kelas, kami berdua tertawa.'),
            ('李美美', '他怎麼也在臺灣？', 'Kenapa dia juga ada di Taiwan?'),
            ('王大文', '他考上了臺灣的大學，來這裡念書。他說他已經愛上臺灣了！', 'Dia diterima di universitas di Taiwan, datang ke sini untuk kuliah. Katanya dia sudah jatuh cinta pada Taiwan!'),
            ('李美美', '太好了！下次帶他來，我也想認識他。', 'Bagus! Lain kali ajak dia, aku juga mau kenalan.'),
        ]),
    ]),
}


def tulis_dialog(dialogs):
    out = []
    for tempat, judul, baris in dialogs:
        ls = [json.dumps({'sp': sp, 'zh': zh, 'py': buat_py(zh), 'id': idn}, ensure_ascii=False) for sp, zh, idn in baris]
        out.append('  {"place": ' + json.dumps(tempat, ensure_ascii=False) + ', "title_id": '
                   + json.dumps(judul, ensure_ascii=False) + ', "lines": [\n   ' + ',\n   '.join(ls) + '\n  ]}')
    return '[\n' + ',\n'.join(out) + '\n ]'


def main(tulis):
    for code, (scene, dialogs) in BARU.items():
        f, _ = cari_file(code)
        s = open(f, encoding='utf-8', newline='').read()
        a = s.index(f'"code": "{code}"')
        z = s.find('"code": "', a + 10); z = len(s) if z < 0 else z
        sc = re.compile(r'"scene": "(?:[^"\\]|\\.)*"').search(s, a, z)
        s = s[:sc.start()] + '"scene": ' + json.dumps(scene, ensure_ascii=False) + s[sc.end():]
        z = s.find('"code": "', a + 10); z = len(s) if z < 0 else z
        d0 = s.index('"dialogs": ', a, z) + len('"dialogs": ')
        t = s.index('"tasks"', d0, z)
        d1 = s.rindex(']', d0, t) + 1
        s = s[:d0] + tulis_dialog(dialogs) + s[d1:]
        json.loads(s)
        if tulis:
            open(f, 'w', encoding='utf-8', newline='').write(s)
        print(('ditulis ' if tulis else 'cek ok ') + code)
        if not tulis:
            for _, _, baris in dialogs:
                for sp, zh, _ in baris:
                    print('  ', zh, '|', buat_py(zh))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main(len(sys.argv) > 1 and sys.argv[1] == 'tulis')
