"""Revisi dialog Vol.2/A1 berdasarkan laporan review Carli (《TOCFL 模組 Vol.1–3 對話審查報告》, 2026-11-04)
+ koreksi level TBCL. Sekali jalan: mengubah BARU di cerita_vol2.py lalu menulis ulang file itu (urut kode).

Pemakaian: py _kerja/revisi_vol2.py   (lalu dialog_cerita.py tulis → bangun_modul → …)
Sudah dijalankan 2026-11-04; disimpan sebagai catatan perubahan per baris.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cerita_vol2 import BARU

B = {k: [v[0], [[d[0], d[1], [list(l) for l in d[2]]] for d in v[1]]] for k, v in BARU.items()}
cek = []


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


def judul(code, n, place, tid):
    B[code][1][n][0], B[code][1][n][1] = place, tid


def scene(code, s):
    B[code][0] = s


def ganti_sp(code, lama, baru):
    for d in B[code][1]:
        for l in d[2]:
            if l[0] == lama:
                l[0] = baru


# B01 — Situasi (bukan 'minggu pertama' lagi), 好不好 (C25) & …，怎麼樣 (B28) dihindari
scene('B01', 'Semester baru dimulai. Di dekat kolam renang kampus Meimei dan Dawen saling bertanya olahraga apa yang '
             'bisa mereka lakukan dan berjanji berlatih bersama, tetapi keesokan harinya kaki Meimei sakit.')
ganti('B01', '我也喜歡跑步！明天下午我們一起去跑步，好不好？', '我也喜歡跑步！明天下午我們一起去跑步吧！', 'Aku juga suka lari! Besok sore kita lari bersama, yuk!')
ganti('B01', '好！星期六早上七點，學校門口見，怎麼樣？', '好！星期六早上七點，學校門口見！', 'Oke! Sabtu jam tujuh pagi, ketemu di gerbang kampus!')
# B02 — V的 (B07) dihindari
ganti('B02', '你帶喝的吧，我要帶水果。', '你帶水吧，我要帶水果。', 'Kamu bawa air minum saja, aku bawa buah.')
# B03
ganti('B03', '第二名。今天他們能拿第一名！', '第二名。今天他們一定能拿第一名！', 'Peringkat dua. Hari ini mereka pasti bisa dapat peringkat satu!')
# B04 — kata inti 一下子 dipakai; dua baris berturut Meimei digabung
ganti('B04', '我在寫功課，可是最近我家的網路很慢，我不能上老師的網站。',
      '我在寫功課，可是最近我家的網路一下子好，一下子不好，我不能上老師的網站。',
      'Aku lagi mengerjakan PR, tapi belakangan internet di rumahku sebentar lancar, sebentar putus, aku tidak bisa membuka situs guru.')
hapus('B04', '啊，這個我會！謝謝你！')
ganti('B04', '啊，我的手機快沒電啦！我們一會兒再聊吧。', '這個我會！謝謝你！啊，我的手機快沒電啦！我們一會兒再聊吧。',
      'Yang ini aku bisa! Terima kasih! Aduh, baterai HP-ku hampir habis! Nanti kita ngobrol lagi ya.')
# B06 — V到 (B17) dihindari; 老人 tidak diucapkan di depan orangnya; 也 tanpa acuan dibuang
ganti('B06', '我也是雅加達人！很高興見到你。', '我也是雅加達人！很高興認識你。', 'Aku juga dari Jakarta! Senang berkenalan denganmu.')
ganti('B06', '他們是陳老師的家人。那個老人是老師的爸爸。', '他們是陳老師的家人。那位老先生是老師的爸爸。', 'Mereka keluarga Guru Chen. Bapak tua itu ayah guru.')
ganti('B06', '老師的爸爸很喜歡跟年輕人聊天。我們也去吧！', '老師的爸爸是很年輕的老人，很喜歡跟年輕人聊天。我們也去吧！',
      'Ayah guru itu orang tua yang berjiwa muda, suka sekali ngobrol dengan anak muda. Ayo kita ke sana juga!')
ganti('B06', '他們在那邊跟大家聊天呢。安妮今天也認識很多新朋友！', '他們在那邊跟大家聊天呢。安妮今天認識很多新朋友！',
      'Mereka lagi ngobrol dengan semua orang di sana. Annie hari ini kenalan dengan banyak teman baru!')
# B07
ganti('B07', '對，這個星期六搬。宿舍的屋子太小，我想租房子。', '對，這個星期六搬。宿舍的房間太小，我想租房子。',
      'Iya, Sabtu ini pindah. Kamar asrama terlalu kecil, aku ingin menyewa rumah.')
# B08 — PW+V著+N (C06) dihindari; dua baris berturut Dawen dipecah
ganti('B08', '有，樓上住著一個老先生。他每天都走樓梯！', '有，樓上有一個老先生。他每天都走樓梯！', 'Ada, di lantai atas ada seorang kakek. Dia setiap hari naik tangga!')
ganti('B08', '我們去樓下的咖啡店坐一下吧。', '我們去樓下的咖啡店坐吧。', 'Kita duduk di kedai kopi di bawah saja yuk.', sp='李美美')
ganti('B08', '好！我們坐電梯吧。', '好！我們坐電梯吧。', 'Oke! Kita naik lift ya.', sp='王大文')
ganti('B08', '電梯今天不能坐啊！', '電梯今天不能坐啊！', 'Lift-nya hari ini kan tidak bisa dipakai!', sp='李美美')
# B09 — konstruksi 把 (C03) dihindari; kata 把 dipakai sebagai kata bantu bilangan
ganti('B09', '大文，你把燈關了吧，燈也很熱。', '大文，你關燈吧，燈也很熱。', 'Dawen, matikan lampunya, lampunya juga panas.')
sisip('B09', '放在桌子上吧。我去掛衣服。', '李美美', '這把椅子呢？', 'Kursi ini bagaimana?')
sisip('B09', '這把椅子呢？', '王大文', '放在窗戶旁邊。', 'Taruh di samping jendela.')
# B10 — …，好嗎？ (B28) dihindari
ganti('B10', '志明，平常早上你先洗，晚上我洗，好嗎？', '志明，平常早上你先洗，晚上我洗，可以嗎？', 'Zhiming, biasanya pagi kamu duluan, malam aku, boleh?')
# B11 — atasan = 黃先生 (bukan semarga Dawen); alur percakapan dibetulkan; 會 'akan' (B18) dihindari
ganti_sp('B11', '王先生', '黃先生')
scene('B11', 'Hari pertama Dawen magang di sebuah perusahaan. Atasannya, Pak Huang, menjelaskan jam kerja; sepulang '
             'kerja Meimei bertanya bagaimana harinya dan apa rencananya ke depan.')
ganti('B11', '在公司上班，你的中文也會進步。這是好辦法！', '當老師很好！', 'Jadi guru itu bagus!')
ganti('B11', '對！可是當老師錢不多啊。', '可是當老師錢不多啊。', 'Tapi jadi guru uangnya tidak banyak, lho.')
ganti('B11', '沒關係，你喜歡就好！', '沒關係，你喜歡就好！現在在公司上班，你每天都可以說中文。',
      'Tidak apa-apa, yang penting kamu suka! Sekarang kerja di perusahaan, kamu bisa berbahasa Mandarin setiap hari.')
# B13 — orang dewasa: 多大, bukan 幾歲
ganti('B13', '好。你今年幾歲？', '好。你今年多大？', 'Baik. Tahun ini umurmu berapa?')
# B15
ganti('B15', '大文，請你用中文講你的週末。', '大文，請你用中文介紹你的週末。', 'Dawen, coba perkenalkan akhir pekanmu dalam bahasa Mandarin.')
# B16 — 陳 terlalu banyak → 高安安
ganti_sp('B16', '陳安安', '高安安')
# B17 — V一下 (C02) & V一V (C44) dihindari
ganti('B17', '我們找一找吧。', '我們一起找吧。', 'Ayo kita cari bersama.')
ganti('B17', '我們問一下那位先生。……他說有！', '我們問那位先生吧。……他說有！', 'Kita tanya bapak itu saja. …Dia bilang ada!')
# B18 — salju di musim dingin (bukan musim gugur); peringatan 'gunung dingin' diucapkan dulu di adegan 1
scene('B18', 'Awal musim dingin, udara mulai dingin. Koran mengabarkan akhir pekan ini di gunung akan turun salju; '
             'Dawen yang belum pernah melihat salju pergi ke gunung bersama Meimei — sudah diingatkan, tetapi ia hanya '
             'memakai satu lapis baju.')
judul('B18', 0, '冬天，在學校', 'Musim dingin, di kampus')
ganti('B18', '對，秋天了，天氣也變冷了。', '對，冬天了，天氣也變冷了。', 'Iya, sudah musim dingin, cuacanya juga jadi dingin.')
ganti('B18', '要是不下雪，我們就去看山上的樹。', '要是不下雪，我們就去看山上的樹。山上會很冷，你要穿很多衣服！',
      'Kalau tidak turun salju, kita lihat pohon-pohon di gunung saja. Di gunung akan dingin sekali, kamu harus pakai banyak baju!')
ganti('B18', '春天和夏天，山上也很漂亮。我們再來吧！', '春天、夏天和秋天，山上也很漂亮。我們再來吧！',
      'Musim semi, musim panas, dan musim gugur gunungnya juga indah. Kita datang lagi ya!')
# B19 — kata inti 西 dipakai
ganti('B19', '週末我們坐火車去高雄。臺灣的東邊也很漂亮，下次再去。', '週末我們坐火車去高雄。臺灣的東邊和西邊也都很漂亮，下次再去。',
      'Akhir pekan kita naik kereta ke Kaohsiung. Bagian timur dan barat Taiwan juga indah, lain kali kita ke sana.')
# B20 — 濕 = TBCL Level 3 (C11) → tidak dipakai; V一下 (C02) & 看不清楚 (C21) dihindari
ganti('B20', '你試一下這件外套吧。', '你試這件外套吧。', 'Coba jaket ini.')
ganti('B20', '我的裙子濕了！', '我的裙子上都是水！', 'Rokku kena air semua!')
ganti('B20', '我的眼鏡也濕了，我看不清楚。', '我的眼鏡上也都是水！', 'Kacamataku juga kena air semua!')
ganti('B20', '我們在店裡等一下吧。', '我們在店裡等吧。', 'Kita tunggu di dalam toko saja.')
ganti('B20', '好。我先脫帽子，帽子太濕了。', '好。我先脫帽子。', 'Oke. Aku lepas topi dulu.')
ganti('B20', '你看一下手錶，現在幾點？', '你看手錶，現在幾點？', 'Coba lihat jam tanganmu, sekarang jam berapa?')
# B22 — konsisten supermarket; 商店 tetap muncul; janji 'beli sedikit' diucapkan dulu
ganti('B22', '百貨公司的東西都很貴。學校旁邊的那家商店最便宜。', '百貨公司的東西都很貴。學校旁邊有很多商店，那家超市最便宜。',
      'Barang di mal semuanya mahal. Di sebelah kampus ada banyak toko, supermarket itu yang paling murah.')
sisip('B22', '好，我們去那家超市。', '志明', '可是這次我們少買一點吧！', 'Tapi kali ini kita beli sedikit saja ya!')
# B23 — kata inti 客人; dua baris berturut pemilik toko dipisah
sisip('B23', '好，請你給我信用卡。', '王大文', '給你。', 'Ini.')
ganti('B23', '謝謝！歡迎你們下次再來！', '謝謝！你們是我今天最好的客人，歡迎下次再來！',
      'Terima kasih! Kalian pelanggan terbaik saya hari ini, lain kali datang lagi ya!')
# B24 — 不太 (C18) dihindari; 臭豆腐 = 小吃, bukan 點心
ganti('B24', '這個蛋糕不太甜，糖很少。', '這個蛋糕糖很少，不會太甜。', 'Kue ini gulanya sedikit, tidak terlalu manis.')
ganti('B24', '謝謝你們！這個蛋糕的味道很好，不太甜。', '謝謝你們！這個蛋糕的味道很好，糖很少！', 'Terima kasih! Rasa kuenya enak, gulanya sedikit!')
ganti('B24', '我也買了一個點心，你們吃一點吧！', '我也買了臺灣的小吃，你們吃一點吧！', 'Aku juga beli jajanan Taiwan, kalian makan sedikit ya!')
ganti('B24', '這個點心又臭又香，臺灣人很喜歡吃。', '這個小吃又臭又香，臺灣人很喜歡吃。', 'Jajanan ini bau tapi harum, orang Taiwan suka sekali.')
# B25 — …，好嗎？ (B28) dihindari
ganti('B25', '我炒青菜，你炸雞，好嗎？', '我炒青菜，你炸雞，可以嗎？', 'Aku tumis sayur, kamu goreng ayam, boleh?')
# B26
ganti('B26', '我要一杯西瓜的果汁。', '我要一杯西瓜果汁。', 'Aku mau segelas jus semangka.')
# B27 — dibawa ke rumah Dawen (sesuai dialog)
scene('B27', 'Malam hari di pasar malam: Dawen dan Meimei membeli pangsit dan mantou untuk dibawa pulang ke rumah '
             'Dawen, lalu merencanakan sarapan besok pagi di pasar.')
# B28 — 這麼 (dekat); pertanyaan pilihan = 還是; 或是 dalam usulan
ganti('B28', '這間餐廳這麼大！人也那麼多！', '這間餐廳這麼大！人也這麼多！', 'Restoran ini besar sekali! Orangnya juga banyak sekali!')
ganti('B28', '我們先看菜單吧。你要吃飯或是吃麵？', '我們先看菜單吧。你要吃飯還是吃麵？', 'Kita lihat menu dulu. Kamu mau makan nasi atau mi?')
ganti('B28', '吃飯以後，我們去茶館喝茶，好嗎？', '吃飯以後，我們去茶館或是咖啡店，好嗎？', 'Habis makan, kita ke kedai teh atau kedai kopi, ya?')
# B29 — yang memperkirakan jarak = Dawen (sesuai Situasi)
scene('B29', 'Meimei tiba dengan kereta jam lima. Dawen melihat peta dan bilang stasiunnya dekat, tetapi ternyata '
             'perjalanannya jauh lebih lama daripada yang ia katakan kepada Annie.')
B['B29'][1][0][2] = [
    ['安妮', '大文，美美幾點到車站？', 'Dawen, Meimei sampai di stasiun jam berapa?'],
    ['王大文', '五點。', 'Jam lima.'],
    ['安妮', '車站離這裡遠不遠？', 'Stasiunnya jauh tidak dari sini?'],
    ['王大文', '你看地圖，不遠，很近。', 'Lihat peta, tidak jauh, dekat sekali.'],
    ['安妮', '從這裡走路要多久？', 'Dari sini jalan kaki berapa lama?'],
    ['王大文', '十分鐘吧。', 'Sepuluh menit, mungkin.'],
    ['安妮', '那我們四點半離開，好嗎？', 'Kalau begitu kita berangkat jam setengah lima, ya?'],
    ['王大文', '好！', 'Oke!'],
]
ganti('B29', '地圖上很近，可是走路好遠啊！', '大文，你說很近，可是走路好遠啊！', 'Dawen, katamu dekat, tapi jalan kakinya jauh sekali!')
# B30 — VP 的 N (B42) dihindari
ganti('B30', '回到了！可是我回家的路走錯了。', '回到家了！可是我走錯路了。', 'Sudah sampai! Tapi aku salah jalan.')
ganti('B30', '你走錯的路很好吃啊！', '你走錯路，可是吃了很多好吃的！', 'Kamu salah jalan, tapi makan banyak yang enak!')
# B32 — tiga jam sebelum penerbangan internasional; buku dititipkan dulu, baru tidak perlu bayar
scene('B32', 'Dawen pulang ke Indonesia untuk liburan. Meimei mengantarnya ke bandara naik taksi; di bandara koper '
             'Dawen kelebihan berat, jadi ia menitipkan beberapa buku kepada Meimei.')
ganti('B32', '十點。現在八點，還早。', '十點。現在七點，還早。', 'Jam sepuluh. Sekarang jam tujuh, masih lama.')
ganti('B32', '美美，這幾本書你帶回去吧。', '五百塊？好貴！美美，這幾本書你帶回去吧。', 'Lima ratus? Mahal sekali! Meimei, buku-buku ini kamu bawa pulang saja ya.')
sisip('B32', '五百塊？好貴！美美，這幾本書你帶回去吧。', '小姐', '好，現在不重了。', 'Baik, sekarang tidak berat lagi.')
# B33 — kakak baru datang kemarin malam; adegan 2 seminggu kemudian
judul('B33', 1, '一個星期以後', 'Seminggu kemudian')
# B34 — 片 + 草地
ganti('B34', '你看，那片草上有很多鳥！', '你看，那片草地上有很多鳥！', 'Lihat, di padang rumput itu banyak burung!')
# B35 — 早飯 → 早餐; 要 + orang + VP dihindari; kata inti 旅館
ganti('B35', '好。你們住幾天？', '好。歡迎來我們的旅館！你們住幾天？', 'Baik. Selamat datang di penginapan kami! Kalian menginap berapa hari?')
ganti('B35', '沒關係，明天你請我吃早飯吧！', '沒關係，明天你請我吃早餐吧！', 'Tidak apa-apa, besok kamu traktir aku sarapan ya!')
ganti('B35', '我媽媽讓我跟你們一起來，可是她要我每天打電話給她。', '我媽媽讓我跟你們一起來，可是我每天要打電話給她。',
      'Ibuku mengizinkan aku pergi bersama kalian, tapi setiap hari aku harus meneleponnya.')
# B37
ganti('B37', '我們先打電話給銀行，然後去夜市問一下。', '我們先打電話給銀行，然後去夜市問老闆。', 'Kita telepon bank dulu, lalu tanya pemilik kios di pasar malam.')
# B41 — peristiwa lampau → 了1 (sudah diajarkan di B33)
ganti('B41', '我送她一個生日蛋糕，她很高興，她說她不生氣了。', '我送了她一個生日蛋糕，她很高興，她說她不生氣了。',
      'Aku memberinya kue ulang tahun, dia senang sekali, katanya dia sudah tidak marah lagi.')
# B43 — 中文比賽 (bukan 說話比賽)
judul('B43', 0, '中文比賽以前', 'Sebelum lomba bahasa Mandarin')
judul('B43', 1, '中文比賽以後', 'Setelah lomba bahasa Mandarin')
# B44 — 還 (bukan 又: Annie belum makan pangsit sebelumnya)
ganti('B44', '我在宿舍看電視，又吃了很多餃子！', '我在宿舍看電視，還吃了很多餃子！', 'Aku nonton TV di asrama, dan juga makan banyak pangsit!')
# B46 — sesuai judul: 臺灣
ganti('B46', '好！我決定了，就去臺北念書！', '好！我決定了，就去臺灣念書！', 'Oke! Aku sudah memutuskan, aku kuliah di Taiwan saja!')


# ---- tulis ulang cerita_vol2.py ----
def q(s):
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"


out = ['"""Data 情境對話 berbasis cerita Vol.2/A1 (keputusan Carli 2026-10-23; dipakai oleh dialog_cerita.py).',
       '',
       'Format sama dengan BARU di dialog_cerita.py: kode → (scene Indonesia, [(tempat, judul Indonesia, [(pembicara, zh, id)])]).',
       'Catatan urutan grammar A1: 了 baru B09, 在 + tempat + V baru B08, V得 B15, 比 B19, 太…了 B20, 有(一)點 B20,',
       '是…的 B33, 一…就 B34 — bab sebelumnya menghindarinya. Juga dihindari sebelum babnya: …，好嗎？/怎麼樣 (B28),',
       '好不好 (C25), VP 的 N (B42), V一下 (C02), 不太 (C18), PW+V著+N (C06), konstruksi 把 (C03).',
       'Revisi 2026-11-04 (laporan review Carli): lihat _kerja/revisi_vol2.py.',
       '"""', '', 'BARU = {']
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
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cerita_vol2.py')
open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('cerita_vol2.py ditulis ulang:', len(B), 'bab')
