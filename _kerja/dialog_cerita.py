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

dialog_natural.NAMA.update({'北投': 'Běi tóu', '陽明山': 'Yáng míng shān', '中山路': 'Zhōng shān lù', '小林': 'Xiǎo lín',
                            '美國': 'Měi guó', '綠島': 'Lǜ dǎo', '故宮': 'Gù gōng', '日本': 'Rì běn', '臺南': 'Tái nán', '臺語': 'Tái yǔ',
                            '高雄': 'Gāo xióng', '陳老師': 'Chén lǎo shī', '淡水': 'Dàn shuǐ',
                            '英語': 'Yīng yǔ', '德文': 'Dé wén', '法文': 'Fǎ wén', '張太太': 'Zhāng tài tai',
                            '小文': 'Xiǎo wén', '英文': 'Yīng wén'})
# bacaan yang ditebak salah oleh pypinyin: (potongan zh, pinyin salah, pinyin benar)
PERBAIKI = [('毛很長', 'máo hěn zhǎng', 'máo hěn cháng'), ('認識', 'rèn shí', 'rèn shì'), ('乾了', 'qián le', 'gān le'),
            ('還你', 'hái nǐ', 'huán nǐ'), ('騎得了', 'qí de le', 'qí de liǎo'),
            ('比較長', 'bǐ jiào zhǎng', 'bǐ jiào cháng'), ('得到他', 'de dào', 'dé dào'),
            ('數數看', 'shù shù kàn', 'shǔ shǔ kàn'), ('哥哥', 'gē gē', 'gē ge'), ('興地', 'xìng dì', 'xìng de'),
            ('差不多', 'chà bu duō', 'chà bù duō'), ('姓李', 'xìng lǐ', 'xìng Lǐ'), ('餅乾', 'bǐng qián', 'bǐng gān'),
            ('照片', 'hào piān', 'hào piàn'), ('睡不著', 'shuì bú zhe', 'shuì bù zháo'), ('由地', 'yóu dì', 'yóu de'),
            ('宿舍', 'sù shě', 'sù shè'), ('哇', 'Wa,', 'Wā,'),
            ('教我', 'jiào wǒ', 'jiāo wǒ'), ('我得寫', 'wǒ de xiě', 'wǒ děi xiě'), ('王小文', 'wáng Xiǎo wén', 'Wáng Xiǎo wén'),
            ('說日語', 'shuō rì yǔ', 'shuō Rì yǔ'), ('一塊兒', 'kuài ér', 'kuàir'), ('差不多', 'Chà bu duō', 'Chà bù duō')]


def buat_py(zh):
    py = dialog_natural.buat_py(zh)
    for kunci, salah, benar in PERBAIKI:
        if kunci in zh:
            py = py.replace(salah, benar)
    return py

BARU = {}   # pilot Vol.3 (C24 C30 C44 C61 C63 C64) dipindah ke cerita_vol3.py (2026-11-04)


try:   # dialog lanjutan (setelah pilot disetujui) ada di file data terpisah
    from cerita_vol3 import BARU as _B3
    BARU.update(_B3)
except ImportError:
    pass
try:   # Vol.1/A0 berbasis cerita, 13 bab (dialog hasil edit Carli tidak disentuh; keputusan 2026-10-26)
    from cerita_vol1 import BARU as _B1
    BARU.update(_B1)
except ImportError:
    pass
try:   # Vol.2/A1 berbasis cerita (keputusan Carli 2026-10-23)
    from cerita_vol2 import BARU as _B2
    BARU.update(_B2)
except ImportError:
    pass

# Pola grammar per bab Vol.3 (pelengkap POLA_GRAMMAR di bangun_bank.py): dialog bab lebih awal sebaiknya tidak memakainya.
POLA_VOL3 = {
    r'把[^手]': 'C03', r'還沒': 'C07', r'越來越|越.{1,4}越': 'C10', r'的時候': 'C12', r'好幾': 'C13', r'其中': 'C13',
    r'快要|就要': 'C14', r'為了': 'C15', r'必須|不必': 'C16', r'極了|不得了': 'C18', r'先[^生]{1,12}再': 'C19',
    r'一邊': 'C19', r'[^\s]不了': 'C21', r'不管': 'C23', r'只好': 'C23', r'要是': 'C24', r'的話': 'C24',
    r'讓': 'C26', r'掉': 'C28', r'不是.{1,12}嗎': 'C31', r'有時候': 'C32', r'從.{1,6}起': 'C33',
    r'(看|試|聽|找|想|查)看': 'C34', r'除了': 'C36', r'分之': 'C38', r'倍|左右': 'C39', r'比一[件個天]': 'C40',
    r'了沒有': 'C42', r'慣': 'C44', r'什麼都': 'C45', r'尤其': 'C46', r'[餓累氣急嚇樂高]壞了': 'C47', r'是不是': 'C48',
    r'一點也|一點都|從來': 'C49', r'只要|只有.{1,10}才': 'C50', r'看得出|聽得出|看不出|聽不出': 'C51',
    r'[抓記站]住|睡不著|找著': 'C52', r'不再': 'C53', r'不是.{1,6}就是|連': 'C55', r'不但': 'C57', r'而且': 'C58',
    r'願意': 'C59', r'其實|本來': 'C60', r'下去|[放吃坐住]得下|[放吃坐住]不下': 'C61', r'[拿走搬]不動|買不起|買得起': 'C62',
    r'(?<!看)起來|起.來': 'C63', r'[考愛穿戴]上|[聊說談]起': 'C64', r'個夠|[裝坐住]滿': 'C65', r'以內': 'C67',
}


def cek_urutan(code, dialogs):
    """⚑ untuk pola yang baru diajarkan di bab Vol.3 sesudah `code` (tinjau manual; bisa kebetulan cocok)."""
    out = []
    for _, _, baris in dialogs:
        for _, zh, _ in baris:
            for pola, mulai in POLA_VOL3.items():
                m = re.search(pola, zh)
                if m and code < mulai:
                    out.append(f'  ⚑ {code}: 「{m.group(0)}」 baru di {mulai} — {zh}')
    return out


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
        a = s.find(f'"code": "{code}"'); a = max(a, 0)   # file satu modul (C01.json) tanpa kolom code
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
        for w in cek_urutan(code, dialogs):
            print(w)
        if not tulis:
            for _, _, baris in dialogs:
                for sp, zh, _ in baris:
                    print('  ', zh, '|', buat_py(zh))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main(len(sys.argv) > 1 and sys.argv[1] == 'tulis')
