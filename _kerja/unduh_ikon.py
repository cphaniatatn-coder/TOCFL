"""Unduh SVG Twemoji (CC-BY 4.0, https://github.com/jdecked/twemoji) untuk semua emoji
yang dipakai di data/modul_vol*.json + ikon UI (UI_EMOJI). Disimpan di img/twemoji/<kode>.svg.
Aturan nama file sama dengan js/pic.js: FE0F dibuang bila tidak ada ZWJ (200D)."""
import json, os, re, sys, urllib.request
K = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(K)
OUT = f'{R}/img/twemoji'
BASE = 'https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/'
UI_EMOJI = ('🧑 👩 👧 👦 👨 👩‍🏫 👨‍💼 👩‍💼 🧔 👩‍🦱 🧑‍⚕️ 👩‍⚕️ 👩‍🦳 🧓 🧑‍🎓 🧑‍✈️ 👮 '
            '🪪 👋 🏠 🛋️ 💼 🏢 ⚽ 🎬 🚆 🗺️ 🤝 💬 🩺 💊 🏫 📚 🛍️ 💳 🍜 🥢 🏦 📮 🚨 ⚠️ ⛰️ 🌳 🌏 ♻️ 🧧 🏮 😊 💭 📱 💻 '
            '🎯 🎧 📖 🧩 🪞 🏆 ⏱️ 📝 🔁 ✅ ❌ 🔥 🌟 🗂️ 🔊 🏁')
MOD = {0x200d, 0xfe0f, 0x20e3} | set(range(0x1f3fb, 0x1f400)) | set(range(0xe0020, 0xe0080))

def clusters(s):
    out, cur, join = [], '', False
    for ch in s:
        cp = ord(ch)
        if cur and (cp in MOD or join):
            cur += ch
        else:
            if cur: out.append(cur)
            cur = ch
        join = cp == 0x200d
    if cur: out.append(cur)
    return out

def is_emoji(c):
    cp = ord(c[0])
    return cp >= 0x2190 and not (0x3000 <= cp <= 0x9fff or 0xff00 <= cp <= 0xffef)

def kode(c):
    if '‍' not in c: c = c.replace('️', '')
    return '-'.join(f'{ord(x):x}' for x in c)

semua = set(clusters(UI_EMOJI.replace(' ', '')))
for v in (1, 2, 3):
    txt = open(f'{R}/data/modul_vol{v}.json', encoding='utf-8').read()
    for icon in re.findall(r'"icon": "([^"]*)"', txt):
        semua.update(clusters(icon))
emoji = sorted(c for c in semua if is_emoji(c))
gagal = []
for c in emoji:
    f = f'{OUT}/{kode(c)}.svg'
    if os.path.exists(f): continue
    try:
        urllib.request.urlretrieve(BASE + kode(c) + '.svg', f)
    except Exception:
        gagal.append(c)
print(len(emoji), 'emoji;', len(os.listdir(OUT)), 'file SVG; gagal:', ' '.join(gagal) or 'tidak ada')
