# RepFix format v3 (25/11) : fond clair, gros texte dès la 1re image, barre de progression,
# corrections numérotées, sous-titres par groupes de mots avec mot actif surligné.
import sys, json, math, subprocess
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BG = (242, 241, 236)      # #F2F1EC
INK = (11, 11, 15)        # #0B0B0F
LIME = (182, 255, 59)     # #B6FF3B
RED = (255, 59, 48)
GREY = (222, 220, 212)
FB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
_fc = {}
def font(sz, bold=True):
    k = (sz, bold)
    if k not in _fc: _fc[k] = ImageFont.truetype(FB if bold else FR, sz)
    return _fc[k]

def text_img(txt, sz, color, squeeze=0.86, bold=True):
    """Texte serré horizontalement (look condensé type Helvetica Bold resserrée)."""
    f = font(sz, bold)
    l, t, r, b = f.getbbox(txt)
    im = Image.new("RGBA", (r - l + 8, b - t + 8), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((4 - l, 4 - t), txt, font=f, fill=color)
    return im.resize((max(1, int(im.width * squeeze)), im.height), Image.LANCZOS)

def wrap(words, sz, maxw, squeeze=0.86):
    lines, cur = [], []
    for w in words:
        test = " ".join(cur + [w])
        if cur and text_img(test, sz, INK, squeeze).width > maxw:
            lines.append(" ".join(cur)); cur = [w]
        else:
            cur.append(w)
    if cur: lines.append(" ".join(cur))
    return lines

def paste_c(base, im, cx, cy, scale=1.0):
    if scale != 1.0:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.LANCZOS)
    base.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

def rrect(d, box, r, fill):
    d.rounded_rectangle(box, r, fill=fill)

def ease(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3

def pop(t, t0, dur=0.16):
    """échelle 0.82 -> 1.06 -> 1.0"""
    x = (t - t0) / dur
    if x <= 0: return 0.82
    if x >= 1: return 1.0
    return 0.82 + 0.24 * ease(min(1, x * 1.3)) - 0.06 * max(0, x - 0.7) / 0.3

def load_words(path):
    out = []
    for item in open(path, encoding="utf-8").read().strip().split("|"):
        p = item.rsplit(" ", 2)
        if p[0] in (":", "«", "»"): continue
        out.append((p[0], float(p[1]), float(p[2])))
    return out

def chunks(words, maxw=3):
    res, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= maxw or w[0][-1] in ".,?!" :
            res.append(cur); cur = []
    if cur: res.append(cur)
    return res

def draw_x(d, cx, cy, s, col=RED, wdt=26):
    d.line((cx - s, cy - s, cx + s, cy + s), fill=col, width=wdt)
    d.line((cx - s, cy + s, cx + s, cy - s), fill=col, width=wdt)

def draw_check(d, cx, cy, s, col=INK, wdt=26):
    d.line((cx - s, cy, cx - s * 0.3, cy + s * 0.7, cx + s, cy - s * 0.7), fill=col, width=wdt, joint="curve")

def render(cfg, words, dur, out_raw):
    secs = cfg["sections"]
    ch = chunks(words)
    starts = [c[0][1] for c in ch]
    nframes = int(math.ceil(dur * FPS))
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                          "-crf", "16", "-pix_fmt", "yuv420p", out_raw], stdin=subprocess.PIPE)
    for fi in range(nframes):
        t = fi / FPS
        sec = secs[0]
        for s in secs:
            if t >= s["t"]: sec = s
        kind = sec["kind"]
        bgc = LIME if kind == "cta" else BG
        im = Image.new("RGBA", (W, H), bgc + (255,))
        d = ImageDraw.Draw(im)
        tin = t - sec["t"]
        # barre de progression (rétention)
        d.rectangle((0, 0, W, 16), fill=GREY if kind != "cta" else (150, 210, 40))
        d.rectangle((0, 0, int(W * t / dur), 16), fill=INK if kind == "cta" else LIME)
        d.rectangle((0, 16, int(W * t / dur), 20), fill=INK)

        if kind == "hook":
            # 1re image = texte plein écran (pas d'attente)
            lines = wrap(sec["big"].split(" "), 150, 940)
            y0 = 700 - (len(lines) * 170) / 2
            for i, ln in enumerate(lines):
                paste_c(im, text_img(ln, 150, INK, 0.84), W / 2, y0 + i * 170)
            if sec.get("x"):
                sc = pop(t, 0.0, 0.25)
                draw_x(d, W / 2, 1230, int(120 * sc), RED, 34)
            if sec.get("sub"):
                sub = text_img(sec["sub"], 64, INK, 0.9)
                bw = sub.width + 60
                rrect(d, (W / 2 - bw / 2, 1420, W / 2 + bw / 2, 1530), 22, LIME)
                paste_c(im, sub, W / 2, 1475)
        elif kind == "cta":
            sc = pop(t, sec["t"], 0.22)
            paste_c(im, text_img("ÉCRIS", 170, INK, 0.84), W / 2, 640, sc)
            box = text_img("« REP »", 260, LIME, 0.84)
            bw, bh = box.width + 90, box.height + 60
            rrect(d, (W / 2 - bw / 2, 900 - bh / 2, W / 2 + bw / 2, 900 + bh / 2), 40, INK)
            paste_c(im, box, W / 2, 900, sc)
            paste_c(im, text_img("en commentaire, je t'envoie l'appli", 62, INK, 0.9, bold=False), W / 2, 1120)
            if t > sec.get("t2", 1e9):
                paste_c(im, text_img("+ abonne-toi pour plus de conseils sport", 54, INK, 0.9), W / 2, 1260, pop(t, sec["t2"]))
        else:
            # gros numéro en fond
            if sec.get("num"):
                paste_c(im, text_img(str(sec["num"]), 900, GREY, 0.9), W / 2, 1080)
            # pastille d'en-tête
            if kind in ("bad", "fix"):
                lab = ("À ÉVITER" if kind == "bad" else "À FAIRE") + (f"  {sec['num']}/{cfg['n']}" if sec.get("num") else "")
                li = text_img(lab, 64, (255, 255, 255) if kind == "bad" else INK, 0.9)
                bw = li.width + 150
                x0 = W / 2 - bw / 2
                rrect(d, (x0, 230, x0 + bw, 340), 55, RED if kind == "bad" else LIME)
                if kind == "bad": draw_x(d, x0 + 62, 285, 20, (255, 255, 255), 12)
                else: draw_check(d, x0 + 62, 285, 22, INK, 12)
                im.alpha_composite(li, (int(x0 + 115), int(285 - li.height / 2)))
            elif kind in ("intro", "tip", "save"):
                lab = {"intro": "LE PLAN", "tip": "RETIENS ÇA", "save": "📌 ENREGISTRE"}[kind]
                if kind == "save": lab = "ENREGISTRE"
                li = text_img(lab, 64, (255, 255, 255), 0.9)
                bw = li.width + 90
                rrect(d, (W / 2 - bw / 2, 230, W / 2 + bw / 2, 340), 55, INK)
                paste_c(im, li, W / 2, 285)
            # titre de section (résumé en gros)
            if sec.get("title"):
                sc = pop(t, sec["t"], 0.2)
                lines = wrap(sec["title"].split(" "), 104, 960)
                for i, ln in enumerate(lines):
                    col = RED if kind == "bad" else INK
                    ti = text_img(ln, 104, col, 0.84)
                    cy = 470 + i * 118
                    if kind == "fix":
                        d.rectangle((W / 2 - ti.width * sc / 2 - 14, cy - 10, W / 2 + ti.width * sc / 2 + 14, cy + 50), fill=LIME)
                    paste_c(im, ti, W / 2, cy, sc)
            # planning (vidéo 3 jours)
            if sec.get("plan"):
                for j, (day, what, tt) in enumerate(cfg["plan"]):
                    if t < tt: continue
                    y = 760 + j * 190
                    a = ease((t - tt) / 0.25)
                    x = int(80 - (1 - a) * 300)
                    rrect(d, (x, y, x + 920, y + 160), 34, INK)
                    im.alpha_composite(text_img(day, 70, LIME, 0.86), (x + 40, y + 42))
                    wi = text_img(what, 70, (255, 255, 255), 0.86)
                    im.alpha_composite(wi, (x + 880 - wi.width, y + 42))
            # sous-titres : groupe de mots, mot actif surligné
            ci = max(0, sum(1 for s in starts if s <= t + 0.02) - 1)
            if starts and t >= starts[0] - 0.05 and ci < len(ch):
                grp = ch[ci]
                sz = 92
                cap_y = 1500 if sec.get("plan") else 1330
                imgs = [text_img(w[0].upper(), sz, INK, 0.86) for w in grp]
                gap = 26
                total = sum(i.width for i in imgs) + gap * (len(imgs) - 1)
                if total > 1000:
                    sz = int(sz * 1000 / total); imgs = [text_img(w[0].upper(), sz, INK, 0.86) for w in grp]
                    total = sum(i.width for i in imgs) + gap * (len(imgs) - 1)
                x = W / 2 - total / 2
                sc = pop(t, grp[0][1], 0.12)
                for wi_, w in zip(imgs, grp):
                    active = w[1] <= t + 0.03
                    if active and w is [g for g in grp if g[1] <= t + 0.03][-1]:
                        d.rounded_rectangle((x - 12, cap_y - wi_.height / 2 - 10, x + wi_.width + 12, cap_y + wi_.height / 2 + 10), 18, fill=LIME)
                    im.alpha_composite(wi_ if active else Image.blend(wi_, Image.new("RGBA", wi_.size, (0, 0, 0, 0)), 0.55),
                                       (int(x), int(cap_y - wi_.height / 2)))
                    x += wi_.width + gap
        # signature
        if kind != "hook":
            paste_c(im, text_img("REPFIX", 46, INK, 0.9), W / 2, 1800)
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()

if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1], encoding="utf-8"))
    words = load_words(cfg["words"])
    render(cfg, words, cfg["dur"], cfg["out"])
