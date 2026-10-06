"""Soal latihan grammar tambahan modul mini (tahap 語法聚焦) → _kerja/mini/latihan_grammar.json.

    py _kerja/mini/latihan_grammar.py      → tulis JSON + periksa kosakata (kata belum diajarkan sampai bab itu)

Setiap soal: q (teks Mandarin, atau dict id/en/vi bila berisi petunjuk), o (3 pilihan; jawaban benar ditulis PERTAMA,
urutan diputar otomatis), why (penjelasan id/en/vi). Dipasang oleh buat_mini.py sebagai grammar[i].latihan
(dan modul.catatan[0].latihan untuk kunci "bab").
"""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
M = os.path.dirname(os.path.abspath(__file__)); K = os.path.dirname(M)
sys.path.insert(0, K)

TAMBAHAN = {'A10': {'刻', '一刻', '三刻', '差', '零'}, 'A18': {'零'}}   # dikenalkan sebagai "kosakata tambahan" di catatan bab
BENAR = {'id': 'Mana yang BENAR?', 'en': 'Which one is CORRECT?', 'vi': 'Câu nào ĐÚNG?'}
def t(i, e, v): return {'id': i, 'en': e, 'vi': v}
def s(q, o, why): return {'q': q, 'o': o, 'why': why}

L = {
'A02': {
 'g1': [s('他是外國人（　）？', ['嗎', '呢', '哪'], t('Pertanyaan ya/tidak: kalimat pernyataan + 嗎.', 'Yes/no question: statement + 嗎.', 'Câu hỏi có/không: câu trần thuật + 嗎.')),
        s(BENAR, ['你是臺灣人嗎？', '你是嗎臺灣人？', '嗎你是臺灣人？'], t('嗎 diletakkan di akhir kalimat pernyataan.', '嗎 goes at the end of the statement.', '嗎 đặt ở cuối câu trần thuật.')),
        s(t('你會說中文嗎？ — Jawaban "ya":', '你會說中文嗎？ — Answer "yes":', '你會說中文嗎？ — Trả lời "có":'), ['會。', '是。', '嗎。'], t('Jawab dengan mengulang kata kerjanya: 會.', 'Answer by repeating the verb: 會.', 'Trả lời bằng cách lặp lại động từ: 會.')),
        s(BENAR, ['你說英文嗎？', '嗎你說英文？', '你嗎說英文？'], t('嗎 selalu di akhir kalimat; urutan kata lainnya tidak berubah.', '嗎 always goes at the end; the word order does not change.', '嗎 luôn ở cuối câu; trật tự từ không đổi.'))],
 'g2': [s('你是（　）國人？', ['哪', '嗎', '這'], t('哪 + 國 + 人 menanyakan kewarganegaraan.', '哪 + 國 + 人 asks about nationality.', '哪 + 國 + 人 hỏi quốc tịch.')),
        s(BENAR, ['你是哪國人？', '你是哪國人嗎？', '哪國人是你？'], t('Kata tanya 哪 tidak dipakai bersama 嗎.', 'The question word 哪 is not used with 嗎.', 'Từ để hỏi 哪 không dùng cùng 嗎.')),
        s('她是（　）國人？', ['哪', '這', '嗎'], t('這 = ini, bukan kata tanya; yang menanyakan adalah 哪.', '這 = this, not a question word; 哪 is the one that asks.', '這 = này, không phải từ để hỏi; từ để hỏi là 哪.')),
        s(t('Jawaban yang cocok untuk 你是哪國人？', 'A suitable answer to 你是哪國人？', 'Câu trả lời phù hợp cho 你是哪國人？'), ['我是印尼人。', '我說英文。', '我會說中文。'], t('哪國人 menanyakan negara asal, jadi dijawab dengan nama negara + 人.', '哪國人 asks for the country, so answer with the country + 人.', '哪國人 hỏi nước nào, nên trả lời bằng tên nước + 人.'))]},
'A04': {
 'bab': [s(t('22 個人 =', '22 個人 =', '22 個人 ='), ['二十二個人', '兩十兩個人', '二十兩個人'], t('2 di posisi puluhan dan satuan selalu 二, walau sebelum kata bantu bilangan.', 'A 2 in the tens and units place is always 二, even before a measure word.', 'Số 2 ở hàng chục và đơn vị luôn là 二, kể cả trước lượng từ.')),
         s(t('12 個孩子 =', '12 個孩子 =', '12 個孩子 ='), ['十二個孩子', '十兩個孩子', '一兩個孩子'], t('12 = 十二; 兩 hanya untuk angka 2 yang berdiri sendiri.', '12 = 十二; 兩 is only for a stand-alone 2.', '12 = 十二; 兩 chỉ dùng cho số 2 đứng một mình.')),
         s(BENAR, ['我家有兩個孩子。', '我家有二個孩子。', '我家有兩孩子。'], t('Jumlah + kata bantu: 兩個 (bukan 二個); kata bantu 個 tidak boleh hilang.', 'Quantity + measure word: 兩個 (not 二個); the measure word 個 cannot be left out.', 'Số lượng + lượng từ: 兩個 (không phải 二個); không được bỏ lượng từ 個.')),
         s(t('Menghitung: 一、（　）、三、四', 'Counting: 一、（　）、三、四', 'Đếm: 一、（　）、三、四'), ['二', '兩', '十'], t('Menghitung angka memakai 二.', 'Counting uses 二.', 'Đếm số dùng 二.')),
         s(t('"ayahku" (paling wajar dalam percakapan) =', '"my dad" (most natural in speech) =', '"bố tôi" (tự nhiên nhất khi nói) ='), ['我爸爸', '爸爸我', '我是爸爸'], t('Anggota keluarga + kata ganti: 的 biasanya dihilangkan: 我爸爸.', 'Family member + pronoun: 的 is usually dropped: 我爸爸.', 'Người trong gia đình + đại từ: thường lược 的: 我爸爸.')),
         s(BENAR, ['我家有五個人。', '家我有五個人。', '我家的有五個人。'], t('我家 = rumah/keluarga-ku (的 dihilangkan).', '我家 = my home/family (的 dropped).', '我家 = nhà tôi (lược 的).')),
         s(t('"nama-ku" =', '"my name" =', '"tên của tôi" ='), ['我的名字', '我名字的', '名字我的'], t('Untuk barang biasa 的 tidak dihilangkan: 我的名字.', 'For ordinary things 的 is not dropped: 我的名字.', 'Với đồ vật thông thường không lược 的: 我的名字.')),
         s(t('"ibu Meimei" =', '"Meimei\'s mum" =', '"mẹ của Mỹ Mỹ" ='), ['美美的媽媽', '媽媽美美的', '美美媽媽的'], t('Pemiliknya nama → 的 tetap dipakai: 美美的媽媽.', 'The owner is a name → keep 的: 美美的媽媽.', 'Chủ sở hữu là tên → giữ 的: 美美的媽媽.'))],
 'g1': [s('我家有五（　）人。', ['個', '幾', '兩'], t('Orang memakai kata bantu bilangan 個; 幾 = berapa, 兩 = dua.', 'People take the measure word 個; 幾 = how many, 兩 = two.', 'Người dùng lượng từ 個; 幾 = mấy, 兩 = hai.')),
        s(t('我有（　）個哥哥。 (dua)', '我有（　）個哥哥。 (two)', '我有（　）個哥哥。 (hai)'), ['兩', '二', '十'], t('Di depan kata bantu bilangan, angka 2 dibaca 兩.', 'Before a measure word, 2 is 兩.', 'Trước lượng từ, số 2 đọc là 兩.')),
        s(BENAR, ['我沒有哥哥。', '我有哥哥沒有。', '沒有我哥哥有。'], t('沒有 + benda = tidak punya (bukan 不有).', '沒有 + noun = do not have (never 不有).', '沒有 + danh từ = không có (không nói 不有).')),
        s('你家有（　）個人？ — 五個。', ['幾', '什麼', '哪'], t('幾 menanyakan jumlah kecil dan dipakai dengan kata bantu bilangan.', '幾 asks about a small number and takes a measure word.', '幾 hỏi số lượng nhỏ và đi với lượng từ.'))],
 'g2': [s('24 =', ['二十四', '四十二', '兩十四'], t('Puluhan dulu lalu satuan: 二十 + 四. 20 dibaca 二十, bukan 兩十.', 'Tens first, then units: 二十 + 四. 20 is 二十, not 兩十.', 'Hàng chục trước, hàng đơn vị sau: 二十 + 四. 20 là 二十, không phải 兩十.')),
        s('12 =', ['十二', '二十', '一二'], t('十二 = 10 + 2; 二十 = 2 × 10.', '十二 = 10 + 2; 二十 = 2 × 10.', '十二 = 10 + 2; 二十 = 2 × 10.')),
        s('70 =', ['七十', '十七', '七一'], t('七十 = 7 × 10; 十七 = 17.', '七十 = 7 × 10; 十七 = 17.', '七十 = 7 × 10; 十七 = 17.')),
        s('99 =', ['九十九', '九九十', '十九九'], t('九十 (90) + 九 (9).', '九十 (90) + 九 (9).', '九十 (90) + 九 (9).'))]},
'A09': {
 'g1': [s('電視（　）桌子上。', ['在', '有', '是'], t('Benda + 在 + tempat: bendanya sudah diketahui, yang disebut letaknya.', 'Thing + 在 + place: the thing is known, you state where it is.', 'Vật + 在 + nơi chốn: đã biết vật, nói nó ở đâu.')),
        s('桌子上（　）一個電視。', ['有', '在', '是'], t('Tempat + 有 + benda: menyebut apa yang ada di tempat itu.', 'Place + 有 + thing: says what is at that place.', 'Nơi chốn + 有 + vật: nói ở đó có gì.')),
        s(BENAR, ['電視在床前面。', '電視床前面在。', '在電視床前面。'], t('Urutan: benda + 在 + patokan + kata posisi.', 'Order: thing + 在 + reference + position word.', 'Trật tự: vật + 在 + vật mốc + từ chỉ vị trí.')),
        s(t('"Kursi ada di bawah meja" =', '"The chair is under the table" =', '"Cái ghế ở dưới bàn" ='), ['椅子在桌子下。', '桌子在椅子下。', '椅子下在桌子。'], t('Benda yang dicari (椅子) di depan, patokannya (桌子) sesudah 在.', 'The thing (椅子) comes first, the reference (桌子) after 在.', 'Vật cần nói (椅子) đứng trước, vật mốc (桌子) sau 在.'))]},
'B04': {
 'bab': [
         s(t('我們一起去吃飯（　）！ (mengajak)', '我們一起去吃飯（　）！ (suggesting)', '我們一起去吃飯（　）！ (rủ rê)'), ['吧', '嗎', '呢'], t('吧 untuk ajakan: "yuk".', '吧 for a suggestion: "let\'s".', '吧 dùng để rủ: "nhé".')),
         s(t('你是美美（　）？ (sudah menduga, minta dipastikan)', '你是美美（　）？ (guessing, asking to confirm)', '你是美美（　）？ (đoán, muốn xác nhận)'), ['吧', '呢', '啦'], t('吧 di pertanyaan = "…, kan?" (sudah menduga jawabannya).', '吧 in a question = "…, right?" (you already guess the answer).', '吧 trong câu hỏi = "…, phải không?" (đã đoán được câu trả lời).')),
         s(t('A：我們一起去看電影，好不好？ B：好（　）！ (setuju dengan senang hati)', 'A：我們一起去看電影，好不好？ B：好（　）！ (gladly agreeing)', 'A：我們一起去看電影，好不好？ B：好（　）！ (vui vẻ đồng ý)'), ['啊', '嗎', '呢'], t('好啊！ = setuju dengan ramah; 好吧 = "ya sudah, boleh deh".', '好啊！ = warm agreement; 好吧 = "well, OK then".', '好啊！ = đồng ý thân thiện; 好吧 = "thôi được".')),
         s(t('最近很忙（　）！每天都有很多功課。 (seruan/keluhan)', '最近很忙（　）！每天都有很多功課。 (exclamation/complaint)', '最近很忙（　）！每天都有很多功課。 (cảm thán/than phiền)'), ['啊', '吧', '嗎'], t('啊 menambah perasaan pada pernyataan: "sibuk banget!"', '啊 adds feeling to a statement: "SO busy!"', '啊 thêm cảm xúc cho câu: "bận quá!"')),
         s(t('我的手機沒電（　）！ (keadaan baru, nada mengeluh)', '我的手機沒電（　）！ (new situation, complaining)', '我的手機沒電（　）！ (tình huống mới, than phiền)'), ['啦', '吧', '嗎'], t('啦 = 了 + 啊: memberitahu keadaan baru dengan nada santai/mengeluh.', '啦 = 了 + 啊: announces a new situation casually/complaining.', '啦 = 了 + 啊: báo tình huống mới với giọng thoải mái/than phiền.')),
         s(t('你在跟誰聊天（　）？ (bertanya dengan nada akrab)', '你在跟誰聊天（　）？ (asking in a friendly tone)', '你在跟誰聊天（　）？ (hỏi giọng thân mật)'), ['呀', '吧', '啦'], t('呀 (= 啊) membuat pertanyaan terdengar akrab; 吧 untuk dugaan, 啦 untuk keadaan baru.', '呀 (= 啊) makes a question sound friendly; 吧 is for guesses, 啦 for new situations.', '呀 (= 啊) làm câu hỏi thân mật; 吧 dùng để đoán, 啦 cho tình huống mới.')),
         s(BENAR, ['你是大文吧？', '你是大文吧嗎？', '你吧是大文？'], t('吧 menggantikan 嗎 bila sudah menduga; keduanya tidak digabung, dan partikel selalu di akhir.', '吧 replaces 嗎 when you already guess; they are never combined, and particles always go at the end.', '吧 thay cho 嗎 khi đã đoán; không ghép hai từ, và trợ từ luôn ở cuối câu.'))],
 'g1': [s('他（　）看電視，不能聊天。', ['在', '有', '是'], t('在 + V = sedang melakukan.', '在 + V = be doing.', '在 + V = đang làm.')),
        s(BENAR, ['我在家看書。', '我看書在家。', '我家在看書。'], t('在 + tempat diletakkan SEBELUM kata kerja.', '在 + place comes BEFORE the verb.', '在 + nơi chốn đặt TRƯỚC động từ.')),
        s('你打電話的時候，我（　）上網。', ['正在', '最近', '一會'], t('正在 menekankan "tepat pada saat itu".', '正在 stresses "right at that moment".', '正在 nhấn mạnh "đúng vào lúc đó".')),
        s(BENAR, ['他在跟美美聊天。', '他聊天在跟美美。', '他跟美美聊天在。'], t('在 + (跟 orang) + V: 在 tetap di depan kelompok kata kerja.', '在 + (跟 person) + V: 在 stays in front of the verb phrase.', '在 + (跟 người) + V: 在 đứng trước cụm động từ.'))],
 'g2': [s('我很好，你（　）？', ['呢', '嗎', '啦'], t('N + 呢？ = "bagaimana dengan …?"', 'N + 呢？ = "what about …?"', 'N + 呢？ = "còn … thì sao?"')),
        s('他在做什麼（　）？', ['呢', '嗎', '吧'], t('Kalimat dengan kata tanya (什麼) memakai 呢, bukan 嗎.', 'A sentence with a question word (什麼) takes 呢, not 嗎.', 'Câu có từ để hỏi (什麼) dùng 呢, không dùng 嗎.')),
        s(BENAR, ['他在睡覺呢。', '他呢在睡覺。', '他在呢睡覺。'], t('呢 di akhir kalimat 在 + V memberi nuansa "sedang" yang santai.', '呢 at the end of 在 + V gives a casual "in the middle of" feel.', '呢 ở cuối câu 在 + V tạo sắc thái "đang" tự nhiên.')),
        s(BENAR, ['你最近忙嗎？', '你最近忙呢嗎？', '你最近呢忙？'], t('Pertanyaan ya/tidak memakai 嗎; 呢 tidak digabung dengan 嗎.', 'Yes/no questions take 嗎; 呢 is not combined with 嗎.', 'Câu hỏi có/không dùng 嗎; không ghép 呢 với 嗎.'))]},
'B19': {
 'g1': [s(BENAR, ['台北比雅加達冷一點。', '台北比雅加達一點冷。', '台北比雅加達很冷。'], t('Selisih (一點) diletakkan SESUDAH kata sifat; 很 tidak dipakai dalam kalimat 比.', 'The difference (一點) goes AFTER the adjective; 很 is not used in 比 sentences.', 'Mức chênh lệch (一點) đặt SAU tính từ; không dùng 很 trong câu 比.')),
        s(t('台北（　）雅加達熱。 (Taipei tidak sepanas Jakarta)', '台北（　）雅加達熱。 (Taipei is not as hot as Jakarta)', '台北（　）雅加達熱。 (Đài Bắc không nóng bằng Jakarta)'), ['沒有', '不有', '沒是'], t('Negasi perbandingan: A 沒有 B (那麼) + Vs.', 'Negative comparison: A 沒有 B (那麼) + Vs.', 'So sánh phủ định: A 沒有 B (那麼) + Vs.')),
        s('雅加達比台北（　）熱。', ['更', '很', '太'], t('Di kalimat 比 dipakai 更 (lebih lagi), bukan 很/太.', 'In 比 sentences use 更 (even more), not 很/太.', 'Trong câu 比 dùng 更 (càng), không dùng 很/太.')),
        s('這三個國家，印尼（　）熱。', ['最', '比', '跟'], t('最 = paling, untuk tiga hal atau lebih.', '最 = the most, for three or more things.', '最 = nhất, dùng cho ba thứ trở lên.'))],
 'g2': [s('我跟哥哥（　）高。', ['一樣', '很', '比'], t('A 跟 B 一樣 + Vs = A sama … dengan B.', 'A 跟 B 一樣 + Vs = A is as … as B.', 'A 跟 B 一樣 + Vs = A … bằng B.')),
        s(BENAR, ['台北跟台中不一樣。', '台北不跟台中一樣。', '台北跟台中一樣不。'], t('Negasi diletakkan tepat sebelum 一樣.', 'The negation goes right before 一樣.', 'Từ phủ định đặt ngay trước 一樣.')),
        s(BENAR, ['我跟他一樣高。', '我跟他一樣很高。', '我一樣跟他高。'], t('Sesudah 一樣 langsung kata sifat, tanpa 很.', 'After 一樣 comes the adjective directly, without 很.', 'Sau 一樣 là tính từ, không thêm 很.')),
        s('這件衣服（　）那件一樣貴。', ['跟', '比', '很'], t('A 跟 B 一樣 + Vs; 比 dipakai bila ada yang "lebih".', 'A 跟 B 一樣 + Vs; 比 is used when one is "more".', 'A 跟 B 一樣 + Vs; 比 dùng khi có cái "hơn".'))]},
'B20': {
 'bab': [s('這件外套太大了，我要小一點（　）。', ['的', '了', '嗎'], t('Vs + 的 = "yang …"; kata bendanya (外套) dihilangkan.', 'Vs + 的 = "the … one"; the noun (外套) is dropped.', 'Vs + 的 = "cái …"; lược danh từ (外套).')),
         s(BENAR, ['我要大的。', '我要大。', '我要的大。'], t('Yang dihilangkan hanya bendanya; 的 harus tetap ada.', 'Only the noun is dropped; 的 must stay.', 'Chỉ lược danh từ; 的 phải giữ lại.')),
         s(t('這兩件外套，你要哪件？ — 我要（　）。 (yang hitam)', '這兩件外套，你要哪件？ — 我要（　）。 (the black one)', '這兩件外套，你要哪件？ — 我要（　）。 (cái màu đen)'), ['黑的', '黑', '很黑'], t('Warna + 的 = "yang (warna) itu".', 'Colour + 的 = "the (colour) one".', 'Màu + 的 = "cái màu đó".')),
         s(t('這個手錶是（　）。 (punyaku)', '這個手錶是（　）。 (mine)', '這個手錶是（　）。 (của tôi)'), ['我的', '我', '的我'], t('Pemilik + 的 bisa berdiri sendiri: 我的 = punyaku.', 'Owner + 的 can stand alone: 我的 = mine.', 'Chủ sở hữu + 的 đứng một mình: 我的 = của tôi.')),
         s(BENAR, ['這件是新的，那件是舊的。', '這件是新，那件是舊。', '這件新的是，那件舊的是。'], t('是 + Vs的 = "(ini) yang …"; tanpa 的, 是 + Vs tidak wajar.', '是 + Vs的 = "(this is) the … one"; without 的, 是 + Vs is unnatural.', '是 + Vs的 = "(đây là) cái …"; không có 的 thì 是 + Vs không tự nhiên.'))],
 'g1': [s('這件外套太大（　）！', ['了', '嗎', '呢'], t('Pola: 太 + Vs + 了.', 'Pattern: 太 + Vs + 了.', 'Mẫu: 太 + Vs + 了.')),
        s('這件太大了，我要（　）一點的。', ['小', '大', '太'], t('Sesudah mengeluh 太…了, minta yang lebih pas: Vs + 一點的.', 'After complaining with 太…了, ask for a better fit: Vs + 一點的.', 'Sau khi chê 太…了, xin cái vừa hơn: Vs + 一點的.')),
        s(BENAR, ['這個帽子太貴了。', '這個帽子太了貴。', '這個帽子貴太了。'], t('太 di depan kata sifat, 了 di akhir.', '太 before the adjective, 了 at the end.', '太 trước tính từ, 了 ở cuối.')),
        s(t('有沒有（　）一點的？ (meminta yang lebih kecil)', '有沒有（　）一點的？ (asking for a smaller one)', '有沒有（　）一點的？ (xin cái nhỏ hơn)'), ['小', '太小', '小了'], t('有沒有 + Vs + 一點的？ untuk menanyakan barang yang lebih ….', '有沒有 + Vs + 一點的？ asks for a … one.', '有沒有 + Vs + 一點的？ để hỏi cái … hơn.'))],
 'g2': [s('這件裙子（　）貴，我不買。', ['有一點', '一點', '太了'], t('有(一)點 + Vs (sebelum kata sifat) = agak, untuk hal yang kurang disukai.', '有(一)點 + Vs (before the adjective) = a bit, for something unwelcome.', '有(一)點 + Vs (trước tính từ) = hơi, cho điều không mong muốn.')),
        s('這件太貴了，有沒有便宜（　）的？', ['一點', '有一點', '太'], t('Vs + 一點 (sesudah kata sifat) untuk meminta yang lebih ….', 'Vs + 一點 (after the adjective) to ask for a … one.', 'Vs + 一點 (sau tính từ) để xin cái … hơn.')),
        s(BENAR, ['今天有一點冷。', '今天一點冷。', '今天冷有一點。'], t('Keluhan "agak": 有一點 + Vs.', 'A mild complaint: 有一點 + Vs.', 'Chê nhẹ "hơi": 有一點 + Vs.')),
        s('這件外套（　）大，我想試小一點的。', ['有一點', '一點', '太'], t('有一點 + Vs untuk keluhan; 太 butuh 了 (太大了).', '有一點 + Vs for a complaint; 太 needs 了 (太大了).', '有一點 + Vs để chê; 太 cần có 了 (太大了).'))]},
'B30': {
 'g1': [s('（　）學校往東走。', ['從', '往', '在'], t('從 + titik awal; 往 + arah.', '從 + starting point; 往 + direction.', '從 + điểm xuất phát; 往 + hướng.')),
        s('從這裡（　）前走，到路口右轉。', ['往', '從', '到'], t('往 + arah + V: 往前走.', '往 + direction + V: 往前走.', '往 + hướng + V: 往前走.')),
        s('到了第二個路口（　）左轉。', ['往', '從', '在'], t('…路口 + 往 + kiri/kanan + 轉. 到了 boleh diganti 在 di depan 路口.', '…路口 + 往 + left/right + 轉. 到了 can be replaced by 在 before 路口.', '…路口 + 往 + trái/phải + 轉. Có thể thay 到了 bằng 在 trước 路口.')),
        s(t('他到學校（　）了。 (pembicara tidak di sekolah)', '他到學校（　）了。 (the speaker is not at school)', '他到學校（　）了。 (người nói không ở trường)'), ['去', '來', '往'], t('去 = menjauhi pembicara; 來 = mendekati pembicara.', '去 = away from the speaker; 來 = towards the speaker.', '去 = rời xa người nói; 來 = về phía người nói.'))],
 'g2': [s('我住（　）台北。', ['在', '到', '往'], t('V在 + tempat untuk tempat tinggal/posisi akhir.', 'V在 + place for where someone lives or ends up.', 'V在 + nơi chốn chỉ nơi ở/vị trí cuối.')),
        s('他走（　）路口了。', ['到', '在', '往'], t('V到 + tempat = sampai di tempat itu dengan bergerak.', 'V到 + place = reach that place by moving.', 'V到 + nơi chốn = đi đến nơi đó.')),
        s('請坐（　）這裡。', ['在', '往', '從'], t('坐在 + tempat = duduk di ….', '坐在 + place = sit at ….', '坐在 + nơi chốn = ngồi ở ….')),
        s('我晚上十點回（　）家。', ['到', '往', '從'], t('回到 + tempat = sudah sampai kembali di ….', '回到 + place = get back to ….', '回到 + nơi chốn = về đến ….'))]},
'B33': {
 'bab': [s('你是（　）來的？ — 我是坐公車來的。', ['怎麼', '哪裡', '誰'], t('Detail cara/kendaraan ditanyakan dengan 怎麼: 你是怎麼來的？', 'The manner/vehicle is asked with 怎麼: 你是怎麼來的？', 'Hỏi cách thức/phương tiện bằng 怎麼: 你是怎麼來的？')),
         s('你是跟（　）一起來的？ — 我是跟我姊姊一起來的。', ['誰', '哪', '怎麼'], t('Detail "dengan siapa" ditanyakan dengan 跟誰.', 'The detail "with whom" is asked with 跟誰.', 'Chi tiết "với ai" hỏi bằng 跟誰.')),
         s(t(BENAR['id'] + ' (rencana besok)', BENAR['en'] + ' (a plan for tomorrow)', BENAR['vi'] + ' (kế hoạch ngày mai)'), ['我明天去台中。', '我是明天去台中的。', '我明天是去台中的了。'], t('是…的 hanya untuk yang sudah terjadi; rencana memakai kalimat biasa.', '是…的 is only for what has happened; plans use a plain sentence.', '是…的 chỉ dùng cho việc đã xảy ra; kế hoạch dùng câu thường.')),
         s('A：你去台中了嗎？ B：去了。 A：你是怎麼去（　）？', ['的', '了', '嗎'], t('Kabar dulu dengan 了, lalu detail dengan 是…的.', 'News first with 了, then details with 是…的.', 'Báo tin trước bằng 了, rồi hỏi chi tiết bằng 是…的.')),
         s(t('我（　）從台中回來，現在有一點累。 (baru saja)', '我（　）從台中回來，現在有一點累。 (just now)', '我（　）從台中回來，現在有一點累。 (vừa mới)'), ['剛剛', '本來', '當然'], t('剛剛 + V = baru saja.', '剛剛 + V = just now.', '剛剛 + V = vừa mới.')),
         s(t('我（　）以為台中很遠，可是坐火車很快。 (tadinya)', '我（　）以為台中很遠，可是坐火車很快。 (originally)', '我（　）以為台中很遠，可是坐火車很快。 (lúc đầu)'), ['本來', '剛剛', '已經'], t('本來 = tadinya, lalu berubah (sering + 可是).', '本來 = originally, then it changed (often + 可是).', '本來 = lúc đầu, rồi thay đổi (thường + 可是).')),
         s(t('A：你是坐飛機來的嗎？ B：（　）是坐飛機來的！ (tentu saja)', 'A：你是坐飛機來的嗎？ B：（　）是坐飛機來的！ (of course)', 'A：你是坐飛機來的嗎？ B：（　）是坐飛機來的！ (tất nhiên)'), ['當然', '好像', '本來'], t('當然 = tentu saja.', '當然 = of course.', '當然 = tất nhiên.')),
         s(t('我只會說幾句中文，可是大家（　）都懂。 (sepertinya)', '我只會說幾句中文，可是大家（　）都懂。 (it seems)', '我只會說幾句中文，可是大家（　）都懂。 (hình như)'), ['好像', '當然', '已經'], t('好像 = sepertinya (dugaan pembicara).', '好像 = it seems (the speaker\'s impression).', '好像 = hình như (cảm nhận của người nói).')),
         s(t('我（　）他是日本人，可是他是韓國人。 (mengira, ternyata salah)', '我（　）他是日本人，可是他是韓國人。 (thought wrongly)', '我（　）他是日本人，可是他是韓國人。 (tưởng sai)'), ['以為', '當然', '好像'], t('以為 = mengira, dan ternyata salah.', '以為 = thought (wrongly).', '以為 = tưởng (nhưng sai).')),
         s(t('你（　）去過很多地方旅行了嗎？ (sudah)', '你（　）去過很多地方旅行了嗎？ (already)', '你（　）去過很多地方旅行了嗎？ (đã)'), ['已經', '剛剛', '本來'], t('已經 + V + 了 = sudah.', '已經 + V + 了 = already.', '已經 + V + 了 = đã.'))],
 'g1': [s('你是怎麼來（　）？', ['的', '了', '嗎'], t('是…的 menanyakan cara/waktu kejadian yang sudah lewat.', '是…的 asks how/when a past event happened.', '是…的 hỏi cách thức/thời gian của sự việc đã qua.')),
        s('我（　）坐公車來的。', ['是', '在', '有'], t('是 + cara (坐公車) + V + 的.', '是 + manner (坐公車) + V + 的.', '是 + cách thức (坐公車) + V + 的.')),
        s(BENAR, ['我不是坐飛機來的。', '我是不坐飛機來的。', '我沒是坐飛機來的。'], t('Negasinya 不是…的.', 'The negative is 不是…的.', 'Phủ định là 不是…的.')),
        s('你坐火車（　）坐公車？', ['還是', '也', '都'], t('還是 dipakai di pertanyaan pilihan (A atau B?).', '還是 is used in choice questions (A or B?).', '還是 dùng trong câu hỏi lựa chọn (A hay B?).'))],
 'g2': [s('我昨天買（　）兩本書。', ['了', '的', '在'], t('V了 + jumlah untuk tindakan yang sudah selesai.', 'V了 + amount for a finished action.', 'V了 + số lượng cho hành động đã xong.')),
        s(BENAR, ['我每天坐四十分鐘的車。', '我每天坐了四十分鐘的車。', '我每天了坐四十分鐘的車。'], t('Kebiasaan (每天) tidak memakai 了.', 'Habits (每天) do not take 了.', 'Thói quen (每天) không dùng 了.')),
        s(t('我學了兩年中文（　）。 (dan masih belajar sampai sekarang)', '我學了兩年中文（　）。 (and still learning now)', '我學了兩年中文（　）。 (và vẫn đang học)'), ['了', '的', '嗎'], t('V了 + durasi + 了 = sampai sekarang dan masih berlangsung.', 'V了 + duration + 了 = up to now and still going on.', 'V了 + thời lượng + 了 = tính đến nay và vẫn tiếp diễn.')),
        s('我（　）吃了三個包子。', ['已經', '正在', '一會'], t('已經 + V了 = sudah.', '已經 + V了 = already.', '已經 + V了 = đã.'))]},
'B40': {
 'g1': [s('因為下雨，（　）我們不去公園。', ['所以', '但是', '雖然'], t('因為 + alasan，所以 + akibat.', '因為 + reason，所以 + result.', '因為 + nguyên nhân，所以 + kết quả.')),
        s('我今天不能來，（　）我感冒了。', ['因為', '所以', '但是'], t('Alasan boleh disebut sesudah akibat: …，因為….', 'The reason can come after the result: …，因為….', 'Có thể nói nguyên nhân sau kết quả: …，因為….')),
        s(BENAR, ['因為他生病，所以沒去上課。', '所以他生病，因為沒去上課。', '因為所以他生病沒去上課。'], t('因為 di bagian alasan, 所以 di bagian akibat.', '因為 marks the reason, 所以 the result.', '因為 ở vế nguyên nhân, 所以 ở vế kết quả.')),
        s('我沒去上課，（　）因為我感冒了。', ['是', '在', '有'], t('Akibat dulu, lalu "…，是因為 + alasan".', 'Result first, then "…，是因為 + reason".', 'Kết quả trước, sau đó "…，是因為 + nguyên nhân".'))],
 'g2': [s('他很高，（　）不會打籃球。', ['但是', '因為', '所以'], t('但是 menghubungkan dua hal yang berlawanan.', '但是 links two contrasting facts.', '但是 nối hai ý trái ngược.')),
        s('雖然下雨，（　）我還是去學校。', ['但是', '所以', '因為'], t('Bila ada 雖然, kalimat kedua wajib memakai 但是/可是/不過.', 'With 雖然, the second clause must have 但是/可是/不過.', 'Có 雖然 thì vế sau bắt buộc có 但是/可是/不過.')),
        s(BENAR, ['雖然很貴，但是很好吃。', '雖然很貴，所以很好吃。', '但是很貴，雖然很好吃。'], t('雖然 … 但是 …: "meskipun …, tetapi …".', '雖然 … 但是 …: "although …, (but) …".', '雖然 … 但是 …: "tuy …, nhưng …".')),
        s(t('他八點上課，可是十點（　）來。 (terlambat)', '他八點上課，可是十點（　）來。 (late)', '他八點上課，可是十點（　）來。 (muộn)'), ['才', '就', '也'], t('才 = lebih lambat dari seharusnya.', '才 = later than it should be.', '才 = muộn hơn bình thường.'))],
 'bab': [s(t('他八點半（　）來了。 (lebih awal)', '他八點半（　）來了。 (earlier than expected)', '他八點半（　）來了。 (sớm hơn dự đoán)'), ['就', '才', '也'], t('就 + V + 了 = lebih cepat/awal dari dugaan.', '就 + V + 了 = sooner/earlier than expected.', '就 + V + 了 = sớm hơn dự đoán.')),
         s(t('他十點（　）來。 (terlambat)', '他十點（　）來。 (late)', '他十點（　）來。 (muộn)'), ['才', '就', '已經'], t('才 = lebih lambat dari dugaan; kalimat 才 tidak ditutup 了.', '才 = later than expected; 才 sentences do not end in 了.', '才 = muộn hơn dự đoán; câu có 才 không kết thúc bằng 了.')),
         s(t('現在（　）八點，還早。', '現在（　）八點，還早。', '現在（　）八點，還早。'), ['才', '就', '已經'], t('才 + angka = pembicara merasa masih kecil/awal.', '才 + number = the speaker feels it is still small/early.', '才 + số = người nói thấy vẫn còn ít/sớm.'))]},
'C04': {
 'g1': [s('請把書放（　）書架上。', ['在', '了', '得'], t('把 + O + 放在 + tempat.', '把 + O + 放在 + place.', '把 + O + 放在 + nơi chốn.')),
        s(BENAR, ['把椅子放在客廳。', '把椅子放。', '放把椅子在客廳。'], t('Sesudah 把 + O, kata kerja tidak boleh berdiri sendiri.', 'After 把 + O, the verb cannot stand alone.', 'Sau 把 + O, động từ không được đứng một mình.')),
        s(BENAR, ['別把包包放在椅子底下。', '把包包別放在椅子底下。', '把別包包放在椅子底下。'], t('Larangan/negasi (別、沒、不) diletakkan SEBELUM 把.', 'Prohibition/negation (別、沒、不) goes BEFORE 把.', 'Từ ngăn cấm/phủ định (別、沒、不) đặt TRƯỚC 把.')),
        s('爸爸（　）沙發放在客廳裡了。', ['把', '被', '在'], t('S + 把 + O + V + 在 + tempat: fokus pada apa yang dilakukan pelaku.', 'S + 把 + O + V + 在 + place: focus on what the doer did.', 'S + 把 + O + V + 在 + nơi chốn: tập trung vào việc người làm đã làm.'))],
 'g2': [s('請把桌子搬（　）院子去。', ['到', '在', '從'], t('把 + O + V到 + tempat + 去.', '把 + O + V到 + place + 去.', '把 + O + V到 + nơi chốn + 去.')),
        s(t('把這張椅子拿到這裡（　）。 (ke arah pembicara)', '把這張椅子拿到這裡（　）。 (towards the speaker)', '把這張椅子拿到這裡（　）。 (về phía người nói)'), ['來', '去', '到'], t('來 = mendekati pembicara; 去 = menjauhi.', '來 = towards the speaker; 去 = away.', '來 = về phía người nói; 去 = rời xa.')),
        s(BENAR, ['把櫃子搬到樓上去。', '把櫃子搬樓上到去。', '搬到樓上把櫃子去。'], t('Urutan: 把 + O + V + 到 + tempat + 來/去.', 'Order: 把 + O + V + 到 + place + 來/去.', 'Trật tự: 把 + O + V + 到 + nơi chốn + 來/去.')),
        s(t('我把書拿（　）來了。 (keluar)', '我把書拿（　）來了。 (out)', '我把書拿（　）來了。 (ra)'), ['出', '上', '在'], t('V + 出 + 來 = mengeluarkan (ke arah pembicara).', 'V + 出 + 來 = take out (towards the speaker).', 'V + 出 + 來 = lấy ra (về phía người nói).'))]},
'C16': {
 'g1': [s('明天開會，你（　）九點到。', ['必須', '不用', '不必'], t('必須 + V = harus (wajib).', '必須 + V = must.', '必須 + V = phải (bắt buộc).')),
        s(BENAR, ['你必須寫報告。', '必須你寫報告。', '你寫報告必須。'], t('必須 diletakkan sesudah subjek, sebelum kata kerja.', '必須 goes after the subject, before the verb.', '必須 đặt sau chủ ngữ, trước động từ.')),
        s('今天工作很多，我（　）加班。', ['必須', '不用', '不必'], t('Pekerjaan banyak → wajib lembur: 必須.', 'Lots of work → must work overtime: 必須.', 'Nhiều việc → phải tăng ca: 必須.')),
        s('老闆（　）我們每天寫報告。', ['要求', '必須', '不用'], t('要求 + orang + V = meminta/menuntut seseorang melakukan …; 必須 tidak diikuti orang.', '要求 + person + V = require someone to …; 必須 is not followed by a person.', '要求 + người + V = yêu cầu ai làm …; 必須 không đi với người.'))],
 'g2': [s('明天是星期天，你（　）來公司。', ['不用', '必須', '要求'], t('不用 + V = tidak perlu.', '不用 + V = no need to.', '不用 + V = không cần.')),
        s('我必須帶書嗎？ — （　），老師會給你。', ['不用', '不必須', '沒必須'], t('Negasi 必須 adalah 不用/不必, bukan 不必須.', 'The negative of 必須 is 不用/不必, not 不必須.', 'Phủ định của 必須 là 不用/不必, không phải 不必須.')),
        s(BENAR, ['你不必加班。', '你不必須加班。', '你不加班不必。'], t('不必 + V = tidak perlu (sedikit lebih formal dari 不用).', '不必 + V = need not (a bit more formal than 不用).', '不必 + V = không cần (trang trọng hơn 不用 một chút).')),
        s('報告已經寫完了，你（　）再寫了。', ['不用', '必須', '要求'], t('Sudah selesai → tidak perlu lagi: 不用.', 'Already done → no need any more: 不用.', 'Đã xong → không cần nữa: 不用.'))]},
'C24': {
 'g1': [s('要是下雨，我們（　）不去了。', ['就', '才', '也'], t('要是 + syarat，(S) + 就 + akibat.', '要是 + condition，(S) + 就 + result.', '要是 + điều kiện，(S) + 就 + kết quả.')),
        s('（　）颱風來了，學校就不上課。', ['要是', '所以', '但是'], t('要是 = kalau (pengandaian), pasangannya 就.', '要是 = if (supposition), paired with 就.', '要是 = nếu (giả định), đi cặp với 就.')),
        s(BENAR, ['要是你有空，我們就去溫泉。', '要是你有空，就我們去溫泉。', '你有空要是，我們就去溫泉。'], t('就 diletakkan SESUDAH subjek kalimat kedua.', '就 goes AFTER the subject of the second clause.', '就 đặt SAU chủ ngữ của vế sau.')),
        s(t('（　）明天天氣好，我們就去山上。 (sedikit lebih formal dari 要是)', '（　）明天天氣好，我們就去山上。 (a bit more formal than 要是)', '（　）明天天氣好，我們就去山上。 (trang trọng hơn 要是 một chút)'), ['如果', '所以', '但是'], t('如果 = 要是; 要是 lebih lisan, 如果 sedikit lebih formal.', '如果 = 要是; 要是 is more colloquial, 如果 a bit more formal.', '如果 = 要是; 要是 khẩu ngữ hơn, 如果 trang trọng hơn.'))],
 'g2': [s('下雨（　），我們就不去。', ['的話', '的', '了'], t('Syarat + 的話 = kalau ….', 'Condition + 的話 = if ….', 'Điều kiện + 的話 = nếu ….')),
        s(BENAR, ['有空的話，你來吧。', '的話有空，你來吧。', '有空，的話你來吧。'], t('的話 diletakkan di AKHIR bagian syarat.', '的話 goes at the END of the condition.', '的話 đặt ở CUỐI vế điều kiện.')),
        s('要是你不舒服的話，就（　）家休息吧。', ['回', '從', '往'], t('…的話，就 + V: "kalau …, ya …".', '…的話，就 + V: "if …, then …".', '…的話，就 + V: "nếu …, thì …".')),
        s('颱風來了的話，我們（　）不去溫泉了。', ['就', '才', '再'], t('…的話 juga berpasangan dengan 就.', '…的話 also pairs with 就.', '…的話 cũng đi cặp với 就.'))]},
'C28': {
 'g1': [s('我的藥（　）弟弟吃掉了。', ['被', '把', '在'], t('S (yang mengalami) + 被 + pelaku + V.', 'S (affected) + 被 + doer + V.', 'S (bị tác động) + 被 + người làm + V.')),
        s('弟弟（　）我的糖果吃掉了。', ['把', '被', '在'], t('Pelaku + 把 + O + V: fokus pada apa yang dilakukan pelaku.', 'Doer + 把 + O + V: focus on what the doer did.', 'Người làm + 把 + O + V: tập trung vào việc người làm.')),
        s('我被這個感冒弄（　）很累。', ['得', '的', '了'], t('被 + N + V得 + akibat.', '被 + N + V得 + result.', '被 + N + V得 + kết quả.')),
        s(BENAR, ['我的蛋糕被弟弟吃了。', '我的蛋糕被吃弟弟了。', '被我的蛋糕弟弟吃了。'], t('Urutan: S + 被 + pelaku + V (+ hasil/了).', 'Order: S + 被 + doer + V (+ result/了).', 'Trật tự: S + 被 + người làm + V (+ kết quả/了).'))],
 'g2': [s('錢都用（　）了。', ['掉', '到', '在'], t('V + 掉 = sampai habis/hilang.', 'V + 掉 = until it is gone.', 'V + 掉 = đến hết/mất.')),
        s('蛋糕被弟弟吃（　）了，一點都沒有了。', ['掉', '得', '在'], t('吃掉 = dimakan sampai habis.', '吃掉 = eaten up.', '吃掉 = ăn hết.')),
        s(BENAR, ['我沒吃完。', '我不吃完了。', '我吃沒完。'], t('Hasil yang tidak tercapai: 沒 + V + hasil.', 'A result not reached: 沒 + V + result.', 'Kết quả chưa đạt: 沒 + V + kết quả.')),
        s(t('太多了，我吃（　）完。 (tidak sanggup menghabiskan)', '太多了，我吃（　）完。 (cannot finish)', '太多了，我吃（　）完。 (ăn không hết)'), ['不', '沒', '了'], t('V + 不 + hasil = tidak bisa mencapai hasil itu.', 'V + 不 + result = unable to reach that result.', 'V + 不 + kết quả = không thể đạt kết quả đó.'))]},
'C40': {
 'g1': [s('天氣一天（　）一天熱。', ['比', '跟', '很'], t('一 + M + 比 + 一 + M + Vs = makin lama makin ….', '一 + M + 比 + 一 + M + Vs = more and more ….', '一 + M + 比 + 一 + M + Vs = ngày càng ….')),
        s('這家店的東西一件比一件（　）。', ['便宜', '很便宜', '便宜一點'], t('Sesudah 一 M 比一 M langsung kata sifat, tanpa 很.', 'After 一 M 比一 M comes the adjective directly, without 很.', 'Sau 一 M 比一 M là tính từ, không thêm 很.')),
        s(BENAR, ['人越來越多。', '人越多來越。', '人來越越多。'], t('越來越 + Vs = makin lama makin ….', '越來越 + Vs = more and more ….', '越來越 + Vs = ngày càng ….')),
        s(BENAR, ['夜市一天比一天熱鬧。', '夜市一天熱鬧比一天。', '夜市比一天一天熱鬧。'], t('Urutan: 一天比一天 + Vs.', 'Order: 一天比一天 + Vs.', 'Trật tự: 一天比一天 + Vs.'))],
 'g2': [s('這雙鞋大（　）一點，我要小一點的。', ['了', '的', '得'], t('Vs + 了一點 = sedikit kelewat dari yang diinginkan.', 'Vs + 了一點 = a bit more than wanted.', 'Vs + 了一點 = hơi quá so với mong muốn.')),
        s(BENAR, ['這件衣服貴了一點。', '這件衣服一點貴了。', '這件衣服了貴一點。'], t('Urutan: Vs + 了 + 一點.', 'Order: Vs + 了 + 一點.', 'Trật tự: Vs + 了 + 一點.')),
        s(t('這件衣服有一點大 ≈ ?', '這件衣服有一點大 ≈ ?', '這件衣服有一點大 ≈ ?'), ['這件衣服大了一點。', '這件衣服大一點了。', '這件衣服一點大。'], t('Vs了一點 ≈ 有一點 + Vs.', 'Vs了一點 ≈ 有一點 + Vs.', 'Vs了一點 ≈ 有一點 + Vs.')),
        s(t('這雙比那雙大（　）。 (sedikit lebih besar)', '這雙比那雙大（　）。 (a little bigger)', '這雙比那雙大（　）。 (to hơn một chút)'), ['一點', '有一點', '很'], t('A 比 B + Vs + 一點.', 'A 比 B + Vs + 一點.', 'A 比 B + Vs + 一點.'))]},
'C58': {
 'g1': [s('這家店不但便宜，（　）東西很好吃。', ['而且', '但是', '所以'], t('不但 … 而且 …: bukan hanya …, bahkan ….', '不但 … 而且 …: not only …, but also ….', '不但 … 而且 …: không những …, mà còn ….')),
        s(t(BENAR['id'] + ' (subjek sama)', BENAR['en'] + ' (same subject)', BENAR['vi'] + ' (cùng chủ ngữ)'), ['他不但會說中文，而且會說英文。', '不但他會說中文，而且會說英文。', '他會說中文不但，而且會說英文。'], t('Subjek sama → 不但 diletakkan SESUDAH subjek.', 'Same subject → 不但 goes AFTER the subject.', 'Cùng chủ ngữ → 不但 đặt SAU chủ ngữ.')),
        s(t(BENAR['id'] + ' (subjek berbeda)', BENAR['en'] + ' (different subjects)', BENAR['vi'] + ' (khác chủ ngữ)'), ['不但我去了，而且他也去了。', '我不但去了，而且他也去了。', '我去了不但，他而且也去了。'], t('Subjek berbeda → 不但 diletakkan SEBELUM subjek pertama.', 'Different subjects → 不但 goes BEFORE the first subject.', 'Khác chủ ngữ → 不但 đặt TRƯỚC chủ ngữ thứ nhất.')),
        s(t('（　）你還記得我的生日！ (tak disangka)', '（　）你還記得我的生日！ (unexpectedly)', '（　）你還記得我的生日！ (không ngờ)'), ['沒想到', '不但', '而且'], t('沒想到 = tak disangka.', '沒想到 = unexpectedly / I didn\'t expect.', '沒想到 = không ngờ.'))],
 'g2': [s('我很開心，（　）很輕鬆。', ['而且', '但是', '所以'], t('而且 = lagi pula, menambah hal yang searah.', '而且 = moreover, adds something in the same direction.', '而且 = hơn nữa, thêm ý cùng chiều.')),
        s(BENAR, ['這件衣服很漂亮，而且不貴。', '這件衣服很漂亮，而且很貴不。', '而且這件衣服很漂亮不貴。'], t('而且 di awal bagian kedua.', '而且 starts the second part.', '而且 đứng đầu vế sau.')),
        s('他不只會唱歌，（　）會跳舞。', ['而且', '可是', '所以'], t('不只 … 而且 … ≈ 不但 … 而且 ….', '不只 … 而且 … ≈ 不但 … 而且 ….', '不只 … 而且 … ≈ 不但 … 而且 ….')),
        s('這家店很近，（　）很便宜。', ['而且', '可是', '因為'], t('Dua hal positif → 而且; 可是 untuk hal yang berlawanan.', 'Two positive points → 而且; 可是 is for contrast.', 'Hai ý tích cực → 而且; 可是 dùng cho ý trái ngược.'))]},
'A10': {
 'bab': [s(t('"Februari" =', '"February" =', '"tháng Hai" ='), ['二月', '兩月', '兩個月'], t('Nama bulan memakai 二: 二月; 兩個月 = dua bulan (lama).', 'Month names use 二: 二月; 兩個月 = two months (duration).', 'Tên tháng dùng 二: 二月; 兩個月 = hai tháng (khoảng thời gian).')),
         s(t('"dua hari" =', '"two days" =', '"hai ngày" ='), ['兩天', '二天', '二號'], t('Lama waktu = 兩 + 天; 二號 = tanggal 2.', 'Duration = 兩 + 天; 二號 = the 2nd (date).', 'Khoảng thời gian = 兩 + 天; 二號 = ngày 2.')),
         s(t('"pukul 12" =', '"12 o\'clock" =', '"12 giờ" ='), ['十二點', '十兩點', '兩點'], t('12 = 十二 (2 di posisi satuan tetap 二); 兩點 = pukul 2.', '12 = 十二 (a 2 in the units place stays 二); 兩點 = 2 o\'clock.', '12 = 十二 (số 2 hàng đơn vị vẫn là 二); 兩點 = 2 giờ.')),
         s(t('Urutan yang BENAR untuk "pukul 7 pagi, 6 Oktober":', 'The CORRECT order for "7 a.m., 6 October":', 'Trật tự ĐÚNG của "7 giờ sáng, ngày 6 tháng 10":'), ['十月六號早上七點', '早上七點十月六號', '七點早上六號十月'], t('Dari besar ke kecil: bulan → tanggal → bagian hari → jam.', 'From big to small: month → date → part of day → hour.', 'Từ lớn đến nhỏ: tháng → ngày → buổi → giờ.')),
         s(BENAR, ['我每天早上七點起床。', '我每天起床早上七點。', '我七點起床每天早上。'], t('Keterangan waktu (每天早上七點) diletakkan SEBELUM kata kerja.', 'The time expression (每天早上七點) goes BEFORE the verb.', 'Trạng ngữ thời gian (每天早上七點) đặt TRƯỚC động từ.')),
         s(BENAR, ['晚上十點', '十點晚上', '十晚上點'], t('Bagian hari (晚上) sebelum jam (十點).', 'Part of the day (晚上) before the hour (十點).', 'Buổi (晚上) đứng trước giờ (十點).')),
         s('2:00 =', ['兩點', '二點', '兩點半'], t('Jam 2 = 兩點 (bukan 二點); 兩點半 = 2.30.', '2 o\'clock = 兩點 (not 二點); 兩點半 = 2:30.', '2 giờ = 兩點 (không nói 二點); 兩點半 = 2:30.')),
         s('6:30 =', ['六點半', '半六點', '六點三十半'], t('半 = setengah, diletakkan sesudah 點.', '半 = half, placed after 點.', '半 = rưỡi, đặt sau 點.')),
         s('7:15 =', ['七點一刻', '七點半', '一刻七點'], t('一刻 = 15 menit, sesudah 點: 七點一刻.', '一刻 = 15 minutes, after 點: 七點一刻.', '一刻 = 15 phút, sau 點: 七點一刻.')),
         s('7:55 =', ['差五分八點', '差五分七點', '八點五十五分'], t('差五分八點 = kurang 5 menit pukul 8 = 7.55; 八點五十五分 = 8.55.', '差五分八點 = five to eight = 7:55; 八點五十五分 = 8:55.', '差五分八點 = tám giờ kém năm = 7:55; 八點五十五分 = 8:55.')),
         s('8:05 =', ['八點零五分', '八點五十分', '五點八分'], t('Menit di bawah 10 boleh memakai 零: 八點零五分.', 'Minutes under 10 may take 零: 八點零五分.', 'Phút dưới 10 có thể thêm 零: 八點零五分.')),
         s('我每天運動三十（　）。', ['分鐘', '點', '半'], t('Lama waktu: 分鐘 (sesudah kata kerja); titik waktu: 點.', 'Duration: 分鐘 (after the verb); point in time: 點.', 'Khoảng thời gian: 分鐘 (sau động từ); thời điểm: 點.'))]},
'A18': {
 'bab': [s('202 =', ['兩百零二', '兩百零兩', '兩百二'], t('Di depan 百 → 兩; angka 2 di belakang tetap 二. 兩百二 = 220.', 'Before 百 → 兩; a final 2 stays 二. 兩百二 = 220.', 'Trước 百 → 兩; số 2 phía sau vẫn là 二. 兩百二 = 220.')),
         s('300 =', ['三百', '三十', '三千'], t('百 = ratus: 三百 = 300; 三十 = 30; 三千 = 3.000.', '百 = hundred: 三百 = 300; 三十 = 30; 三千 = 3,000.', '百 = trăm: 三百 = 300; 三十 = 30; 三千 = 3.000.')),
         s('2,000 =', ['兩千', '兩百', '兩萬'], t('千 = ribu; angka 2 di depan 千 dibaca 兩.', '千 = thousand; 2 before 千 is 兩.', '千 = nghìn; số 2 trước 千 đọc là 兩.')),
         s('10,000 =', ['一萬', '十千', '一千'], t('10.000 = 一萬 (bukan 十千): Mandarin menghitung per empat digit.', '10,000 = 一萬 (not 十千): Chinese counts in groups of four digits.', '10.000 = 一萬 (không phải 十千): tiếng Trung đếm theo nhóm bốn chữ số.')),
         s('25,000 =', ['兩萬五千', '二十五千', '兩千五百'], t('2|5000 → 兩萬 + 五千.', '2|5000 → 兩萬 + 五千.', '2|5000 → 兩萬 + 五千.')),
         s('1,200,000 =', ['一百二十萬', '一千二百萬', '十二萬'], t('120|0000 → 一百二十 + 萬.', '120|0000 → 一百二十 + 萬.', '120|0000 → 一百二十 + 萬.')),
         s('105 =', ['一百零五', '一百五', '一百五十'], t('Nol di tengah dibaca 零; 一百五 = 150.', 'A middle zero is read 零; 一百五 = 150.', 'Số 0 ở giữa đọc là 零; 一百五 = 150.')),
         s(t('一個八十塊，我買兩個。一共多少錢？', '一個八十塊，我買兩個。一共多少錢？', '一個八十塊，我買兩個。一共多少錢？'), ['一百六十塊', '八十塊', '兩百塊'], t('一共 = totalnya: 80 × 2 = 160 = 一百六十塊.', '一共 = in total: 80 × 2 = 160 = 一百六十塊.', '一共 = tổng cộng: 80 × 2 = 160 = 一百六十塊.')),
         s('這個多少錢？ — 這個一百二十（　）。', ['塊', '個', '點'], t('Satuan uang dalam percakapan: 塊.', 'The spoken money unit: 塊.', 'Đơn vị tiền khi nói: 塊.')),
         s(t('給你兩百塊。— 找你四十塊。 Harga barangnya:', '給你兩百塊。— 找你四十塊。 The price was:', '給你兩百塊。— 找你四十塊。 Giá món đồ là:'), ['一百六十塊', '兩百四十塊', '四十塊'], t('200 − 40 = 160 = 一百六十塊.', '200 − 40 = 160 = 一百六十塊.', '200 − 40 = 160 = 一百六十塊.'))]},
'A24': {
 'bab': [s(t('今天好（　）！ (panas sekali)', '今天好（　）！ (so hot)', '今天好（　）！ (nóng quá)'), ['熱', '冷', '下雨'], t('好 + kata sifat = sangat … (seruan): 好熱！', '好 + adjective = so … (exclamation): 好熱！', '好 + tính từ = … quá (cảm thán): 好熱！')),
         s('明天天氣（　）？ — 很冷。', ['怎麼樣', '什麼', '哪'], t('天氣怎麼樣？ = cuacanya bagaimana?', '天氣怎麼樣？ = how is the weather?', '天氣怎麼樣？ = thời tiết thế nào?')),
         s('今天熱（　）熱？', ['不', '沒', '很'], t('Pertanyaan A-不-A: 熱不熱？', 'A-not-A question: 熱不熱？', 'Câu hỏi A-不-A: 熱不熱？')),
         s(BENAR, ['今天風很大。', '今天很風大。', '今天大風很。'], t('Angin kencang = 風很大.', 'Strong wind = 風很大.', 'Gió to = 風很大.')),
         s(BENAR, ['明天不下雨。', '明天下不雨。', '明天雨不下。'], t('下雨 kata kerja; negasinya 不下雨.', '下雨 is a verb; its negative is 不下雨.', '下雨 là động từ; phủ định là 不下雨.')),
         s('臺灣很熱，印尼（　）很熱。', ['也', '最', '不'], t('也 = juga (sama dengan yang disebut sebelumnya).', '也 = also (the same as what came before).', '也 = cũng (giống điều nói trước).')),
         s('明天不下雨，（　）風很大。', ['可是', '也', '最'], t('可是 menghubungkan dua keadaan yang berlawanan.', '可是 links two contrasting conditions.', '可是 nối hai tình trạng trái ngược.')),
         s(BENAR, ['台北七月最熱。', '台北最七月熱。', '台北七月熱最。'], t('最 diletakkan tepat sebelum kata sifat.', '最 goes right before the adjective.', '最 đặt ngay trước tính từ.')),
         s('今天不熱，可是有一點（　）。', ['冷', '很冷', '太冷'], t('有一點 + kata sifat (tanpa 很/太).', '有一點 + adjective (without 很/太).', '有一點 + tính từ (không có 很/太).'))]},
}


def main():
    import cek_dialog as cd
    mods = cd.urutan()
    out, kamus, salah, n = {}, {}, 0, 0
    for kode, grup in L.items():
        ok = cd.kosakata_sampai(kode, mods) | TAMBAHAN.get(kode, set())
        out[kode] = {}
        for g, soal in grup.items():
            daftar = []
            for i, x in enumerate(soal):
                r = i % 3                                # jawaban benar diputar ke posisi A/B/C bergantian
                o = x['o'][-r:] + x['o'][:-r] if r else list(x['o'])
                q = x['q']
                for teks in [q if isinstance(q, str) else q['id']] + o:
                    zh = ''.join(re.findall(r'[一-鿿，。？！、（）]+', teks))
                    bad = cd.cek(zh, ok) if zh else []
                    if bad:
                        salah += 1; print(f'{kode} {g} #{i + 1}: kata belum diajarkan {bad} — {teks}')
                for tr in ([q] if isinstance(q, dict) else []) + [x['why']]:
                    kamus[tr['id']] = {'en': tr['en'], 'vi': tr['vi']}
                daftar.append({'q': q if isinstance(q, str) else q['id'], 'options': o, 'answer': o.index(x['o'][0]), 'why': x['why']['id']})
                n += 1
            out[kode][g] = daftar
    json.dump({'_keterangan': __doc__.strip().split('\n')[0], 'soal': out, 'kamus': kamus},
              open(f'{M}/latihan_grammar.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{n} soal ditulis ke _kerja/mini/latihan_grammar.json; masalah kosakata: {salah}')


if __name__ == '__main__':
    main()
