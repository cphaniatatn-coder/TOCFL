"""Buat css/kai.css — font 標楷體 untuk teks Mandarin, sedikit diperbesar lewat size-adjust.

    py _kerja/buat_font_css.py

- 'KaiLocal' = 標楷體 bawaan sistem (DFKai-SB di Windows, BiauKai di macOS).
- 'KaiWeb'   = LXGW WenKai TC dari Google Fonts, cadangan untuk HP tanpa 標楷體.
  Aturan @font-face Google disalin (bobot 400 saja) supaya bisa diberi size-adjust.
Keduanya hanya dipakai untuk hanzi/zhuyin; huruf Latin tetap font biasa (lihat --zh di style.css).
Ubah BESAR untuk mengatur ukuran hanzi di seluruh app, lalu jalankan ulang skrip ini.
"""
import os, re, urllib.request

BESAR = '110%'
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = 'https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC:wght@400&display=swap'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
# hanzi, zhuyin, tanda nada zhuyin, tanda baca CJK & bentuk lebar
CJK = 'U+02C7, U+02C9-02CB, U+02D9, U+2E80-2FDF, U+3000-303F, U+3100-312F, U+31A0-31BF, U+3400-4DBF, U+4E00-9FFF, U+F900-FAFF, U+FF00-FFEF, U+20000-2FA1F'

css = urllib.request.urlopen(urllib.request.Request(URL, headers={'User-Agent': UA})).read().decode('utf-8')
faces = re.findall(r'@font-face \{.*?\}', css, re.S)
assert faces and all('woff2' in f for f in faces), 'format Google Fonts berubah'
web = [f.replace("font-family: 'LXGW WenKai TC';", "font-family: 'KaiWeb';")
        .replace('  font-display: swap;', f'  font-display: swap;\n  size-adjust: {BESAR};') for f in faces]

out = f"""/* DIBUAT OTOMATIS oleh _kerja/buat_font_css.py — jangan diedit langsung. */
@font-face {{
  font-family: 'KaiLocal';
  src: local('DFKai-SB'), local('DFKaiShu-SB-Estd-BF'), local('標楷體'), local('BiauKai'), local('Kaiti TC Regular'), local('STKaitiTC-Regular');
  size-adjust: {BESAR};
  unicode-range: {CJK};
}}
""" + '\n'.join(web) + '\n'
open(f'{R}/css/kai.css', 'w', encoding='utf-8').write(out)
print(f'css/kai.css: 1 font lokal + {len(web)} potongan KaiWeb, size-adjust {BESAR}')
