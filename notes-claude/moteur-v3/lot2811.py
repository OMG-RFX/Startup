# Lot RepFix 29-33 (28/11) : formats viraux SANS VOIX (lisibles sans le son), phonk en fond.
# 29 simulation lent vs rapide · 30 POV jambes · 31 quiz vrai/faux · 32 simulation sommeil 6h vs 8h · 33 tier list
# Usage : python3 lot2811.py 29   -> v29_video.mp4 (image seule, le son est ajouté par mix_muet.sh)
import sys, math, subprocess
from PIL import Image, ImageDraw
from engine import W, H, FPS, BG, INK, LIME, RED, GREY, text_img, wrap, paste_c, rrect, ease, pop, draw_x, draw_check

DARK = (11, 11, 15)
WHITE = (242, 241, 236)
ORANGE = (255, 140, 40)
MID = (60, 60, 70)

def out_pipe(path):
    return subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                             "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                             "-crf", "16", "-pix_fmt", "yuv420p", path], stdin=subprocess.PIPE)

def progress(d, t, dur, dark):
    d.rectangle((0, 0, W, 16), fill=MID if dark else GREY)
    d.rectangle((0, 0, int(W * t / dur), 16), fill=LIME)

def lines_c(im, txt, sz, col, cy, maxw=960, lh=None, sc=1.0, squeeze=0.86):
    lines = wrap(txt.split(" "), sz, maxw, squeeze)
    lh = lh or int(sz * 1.14)
    y0 = cy - (len(lines) - 1) * lh / 2
    for i, ln in enumerate(lines):
        paste_c(im, text_img(ln, sz, col, squeeze), W / 2, y0 + i * lh, sc)

def cta(im, d, t, t0, dark, extra=None):
    """Fin commune : écris REP + abonne-toi (fond vert citron)."""
    d.rectangle((0, 20, W, H), fill=LIME)
    sc = pop(t, t0, 0.22)
    if extra:
        lines_c(im, extra, 70, INK, 420)
    paste_c(im, text_img("ÉCRIS", 170, INK, 0.84), W / 2, 680, sc)
    box = text_img("« REP »", 250, LIME, 0.84)
    bw, bh = box.width + 90, box.height + 60
    rrect(d, (W / 2 - bw / 2, 930 - bh / 2, W / 2 + bw / 2, 930 + bh / 2), 40, INK)
    paste_c(im, box, W / 2, 930, sc)
    paste_c(im, text_img("en commentaire, je t'envoie l'appli", 62, INK, 0.9, bold=False), W / 2, 1150)
    if t > t0 + 0.8:
        paste_c(im, text_img("+ abonne-toi pour plus de conseils sport", 54, INK, 0.9), W / 2, 1290, pop(t, t0 + 0.8))
    paste_c(im, text_img("REPFIX", 46, INK, 0.9), W / 2, 1800)

# ---------- bonhomme bâton qui fait un curl ----------
def stick_curl(d, cx, base_y, phase, col_body, col_muscle, glow, droop=0.0, s=1.0):
    """phase 0 = bras tendu, 1 = bras fléchi. glow 0..1 = biceps qui s'allume."""
    wdt = int(14 * s)
    head_y = base_y - 470 * s + droop * 25 * s
    d.ellipse((cx - 42 * s, head_y - 42 * s, cx + 42 * s, head_y + 42 * s), outline=col_body, width=wdt)
    neck = (cx, head_y + 42 * s); hip = (cx, base_y - 190 * s)
    d.line((neck, hip), fill=col_body, width=wdt)
    d.line((hip, (cx - 60 * s, base_y)), fill=col_body, width=wdt)
    d.line((hip, (cx + 60 * s, base_y)), fill=col_body, width=wdt)
    sh = (cx, head_y + 80 * s)
    elbow = (cx + 25 * s, sh[1] + 120 * s)
    ang = math.radians(90 - 150 * phase)  # 90° = vers le bas, -60° = remonté
    hand = (elbow[0] + 115 * s * math.cos(ang) * 0.35 + 40 * s * phase, elbow[1] + 115 * s * math.sin(ang))
    mc = tuple(int(col_body[i] + (col_muscle[i] - col_body[i]) * glow) for i in range(3))
    d.line((sh, elbow), fill=mc, width=int(wdt * (1 + 0.9 * glow)))
    d.line((elbow, hand), fill=col_body, width=wdt)
    d.ellipse((hand[0] - 22 * s, hand[1] - 22 * s, hand[0] + 22 * s, hand[1] + 22 * s), fill=col_body)
    d.line((hand[0] - 34 * s, hand[1], hand[0] + 34 * s, hand[1]), fill=col_body, width=int(10 * s))
    # autre bras le long du corps
    d.line((sh, (cx - 40 * s, sh[1] + 210 * s)), fill=col_body, width=wdt)

def curl_phase(t, up, down):
    per = up + down
    x = t % per
    return ease(x / up) if x < up else 1 - ease((x - up) / down)

def simulation(n, cfg):
    dur = cfg["dur"]; p = out_pipe(f"v{n}_video.mp4")
    A, B = LIME, ORANGE
    T_SIM, T_VERD, T_CTA = 2.6, 12.6, 16.2
    for fi in range(int(dur * FPS)):
        t = fi / FPS
        im = Image.new("RGBA", (W, H), DARK + (255,)); d = ImageDraw.Draw(im)
        progress(d, t, dur, True)
        if t >= T_CTA:
            cta(im, d, t, T_CTA, True, cfg["cta_extra"]); p.stdin.write(im.convert("RGB").tobytes()); continue
        # titre 2 couleurs (dès la 1re image)
        ta = text_img(cfg["a"], 120, A, 0.84); tv = text_img(" vs ", 90, WHITE, 0.84); tb = text_img(cfg["b"], 120, B, 0.84)
        tot = ta.width + tv.width + tb.width; x = W / 2 - tot / 2
        for img in (ta, tv, tb):
            im.alpha_composite(img, (int(x), int(150 - img.height / 2))); x += img.width
        paste_c(im, text_img(cfg["question"], 58, WHITE, 0.9, bold=False), W / 2, 260)
        # projecteurs
        for cx, col in ((290, A), (790, B)):
            cone = Image.new("RGBA", (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(cone)
            cd.polygon(((cx - 40, 330), (cx + 40, 330), (cx + 230, 1060), (cx - 230, 1060)), fill=(255, 255, 255, 22))
            cd.ellipse((cx - 230, 1030, cx + 230, 1090), fill=(255, 255, 255, 30))
            im.alpha_composite(cone)
        tsim = max(0.0, t)
        for k, (cx, col) in enumerate(((290, A), (790, B))):
            up, down = cfg["tempo"][k]
            ph = curl_phase(tsim + k * 0.3, up, down)
            stick_curl(d, cx, 1050, ph, WHITE, col, 0.35 + 0.65 * ph, droop=cfg.get("droop", [0, 0])[k], s=1.0)
            paste_c(im, text_img(cfg["labels"][k], 46, col, 0.9), cx, 1130)
            if cfg.get("zzz") and k == 0 and int(t * 2) % 2 == 0:
                paste_c(im, text_img("z z z", 54, (150, 150, 170), 0.9), cx + 110, 560)
        # compteur de semaines + barres
        prog = ease((t - T_SIM) / (T_VERD - T_SIM - 0.6)) if t > T_SIM else 0.0
        week = 1 + int(round(prog * (cfg["weeks"] - 1)))
        if t > T_SIM - 0.3:
            wk = text_img(f"SEMAINE {week} / {cfg['weeks']}", 64, DARK, 0.9)
            rrect(d, (W / 2 - wk.width / 2 - 40, 1205, W / 2 + wk.width / 2 + 40, 1295), 45, WHITE)
            paste_c(im, wk, W / 2, 1250)
        for j, (name, va, vb) in enumerate(cfg["bars"]):
            y = 1360 + j * 135
            paste_c(im, text_img(name.upper(), 40, (180, 180, 190), 0.9), W / 2, y)
            for k, (v, col) in enumerate(((va, A), (vb, B))):
                x0 = 80 if k == 0 else 560; bw = 440
                rrect(d, (x0, y + 32, x0 + bw, y + 72), 20, MID)
                fill = int(bw * v * prog)
                if fill > 24: rrect(d, (x0, y + 32, x0 + fill, y + 72), 20, col)
        if t >= T_VERD:
            a = ease((t - T_VERD) / 0.3)
            ov = Image.new("RGBA", (W, H), (11, 11, 15, int(250 * a))); im.alpha_composite(ov); d = ImageDraw.Draw(im)
            sc = pop(t, T_VERD, 0.25)
            rrect(d, (90, 620, W - 90, 680), 30, LIME) if False else None
            paste_c(im, text_img("VERDICT", 70, DARK, 0.9), W / 2, 640, sc) if False else None
            lab = text_img("VERDICT", 66, DARK, 0.9)
            rrect(d, (W / 2 - lab.width / 2 - 45, 560, W / 2 + lab.width / 2 + 45, 660), 50, LIME)
            paste_c(im, lab, W / 2, 610)
            lines_c(im, cfg["verdict"], 96, WHITE, 860, sc=sc)
            if t > T_VERD + 1.3:
                lines_c(im, cfg["verdict2"], 64, LIME, 1180, sc=pop(t, T_VERD + 1.3))
        paste_c(im, text_img("REPFIX", 46, (120, 120, 130), 0.9), W / 2, 1830)
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()

# ---------- 30 : POV (fond clair, liste qui se remplit) ----------
def pov(n):
    dur = 17.0; p = out_pipe(f"v{n}_video.mp4")
    days = [("LUNDI", "biceps", 0.0), ("MARDI", "pecs + biceps", 1.1), ("MERCREDI", "bras (encore)", 2.2),
            ("JEUDI", "biceps", 3.3), ("VENDREDI", "jambes ?", 4.4)]
    T_STAMP, T_RES, T_FIX, T_CTA = 5.6, 7.4, 11.0, 15.0
    for fi in range(int(dur * FPS)):
        t = fi / FPS
        im = Image.new("RGBA", (W, H), BG + (255,)); d = ImageDraw.Draw(im)
        progress(d, t, dur, False)
        if t >= T_CTA:
            cta(im, d, t, T_CTA, False, "Tag le pote qui saute les jambes"); p.stdin.write(im.convert("RGB").tobytes()); continue
        if t < T_RES:
            paste_c(im, text_img("POV :", 120, INK, 0.84), W / 2, 200)
            lines_c(im, "ta semaine de muscu", 80, INK, 330)
            for j, (day, what, tt) in enumerate(days):
                if t < tt: continue
                a = ease((t - tt) / 0.25); y = 470 + j * 190; x = int(80 - (1 - a) * 300)
                last = j == 4
                rrect(d, (x, y, x + 920, y + 160), 34, INK)
                im.alpha_composite(text_img(day, 66, LIME, 0.86), (x + 40, y + 46))
                wi = text_img(what, 66, WHITE, 0.86)
                im.alpha_composite(wi, (x + 880 - wi.width, y + 46))
            if t >= T_STAMP:
                sc = pop(t, T_STAMP, 0.2) * 1.0
                st = text_img("ANNULÉ", 150, RED, 0.84)
                st = st.rotate(-12, expand=True, resample=Image.BICUBIC)
                paste_c(im, st, W / 2 + 120, 470 + 4 * 190 + 80, sc)
            lines_c(im, "(tout le monde a un pote comme ça)", 50, (120, 120, 120), 1600)
        elif t < T_FIX:
            paste_c(im, text_img("RÉSULTAT :", 110, INK, 0.84), W / 2, 230)
            sc = pop(t, T_RES, 0.3)
            cx, cy = W / 2, 760
            # gros haut du corps, jambes en allumettes
            d.ellipse((cx - 60, cy - 330, cx + 60, cy - 210), outline=INK, width=14)
            d.polygon(((cx - 300, cy - 190), (cx + 300, cy - 190), (cx + 90, cy + 220), (cx - 90, cy + 220)), fill=INK)
            d.line(((cx - 300, cy - 180), (cx - 380, cy + 160)), fill=INK, width=60)
            d.line(((cx + 300, cy - 180), (cx + 380, cy + 160)), fill=INK, width=60)
            d.line(((cx - 40, cy + 220), (cx - 70, cy + 640)), fill=INK, width=8)
            d.line(((cx + 40, cy + 220), (cx + 70, cy + 640)), fill=INK, width=8)
            if t > T_RES + 1.0:
                lines_c(im, "le poulet qui marche sur des cure-dents", 72, RED, 1560, sc=pop(t, T_RES + 1.0))
        else:
            lab = text_img("LA SOLUTION", 64, INK, 0.9)
            rrect(d, (W / 2 - lab.width / 2 - 45, 230, W / 2 + lab.width / 2 + 45, 340), 55, LIME)
            paste_c(im, lab, W / 2, 285)
            sc = pop(t, T_FIX, 0.25)
            lines_c(im, "LES JAMBES = LA MOITIÉ DE TON CORPS", 104, INK, 620, sc=sc)
            if t > T_FIX + 1.2:
                lines_c(im, "Au moins 1 vraie séance jambes par semaine. Squat, fentes, soulevé de terre roumain.", 66, INK, 1080, sc=pop(t, T_FIX + 1.2))
            draw_check(d, W / 2, 1450, 70, INK, 26) if t > T_FIX + 2.2 else None
        if t < T_CTA:
            paste_c(im, text_img("REPFIX", 46, INK, 0.9), W / 2, 1800)
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()

# ---------- 31 : quiz vrai / faux (fond sombre, compte à rebours) ----------
def quiz(n):
    qs = [("Si t'as pas de courbatures, ta séance n'a servi à rien", False, "Les courbatures ne mesurent pas tes progrès."),
          ("Dormir 7 à 9 h t'aide à prendre du muscle", True, "C'est pendant la nuit que tu récupères."),
          ("Il faut manger toutes les 3 h sinon tu perds tes muscles", False, "Ce qui compte : tes protéines sur la journée.")]
    T0, QD = 2.4, 4.6
    T_SCORE = T0 + QD * 3; T_CTA = T_SCORE + 1.8; dur = T_CTA + 2.6
    p = out_pipe(f"v{n}_video.mp4")
    for fi in range(int(dur * FPS)):
        t = fi / FPS
        im = Image.new("RGBA", (W, H), DARK + (255,)); d = ImageDraw.Draw(im)
        progress(d, t, dur, True)
        if t >= T_CTA:
            cta(im, d, t, T_CTA, True, "Ton score sur 3 en commentaire"); p.stdin.write(im.convert("RGB").tobytes()); continue
        paste_c(im, text_img("VRAI", 130, LIME, 0.84), W / 2 - 230, 200)
        paste_c(im, text_img("ou", 80, WHITE, 0.84), W / 2, 205)
        paste_c(im, text_img("FAUX ?", 130, RED, 0.84), W / 2 + 250, 200)
        if t < T0:
            lines_c(im, "3 questions. Compte tes points.", 72, WHITE, 760)
            lines_c(im, "90 % des gens se trompent à la 1re", 60, (170, 170, 180), 900)
        elif t < T_SCORE:
            qi = int((t - T0) // QD); tq = t - T0 - qi * QD
            q, ans, why = qs[qi]
            paste_c(im, text_img(f"QUESTION {qi + 1}/3", 56, (170, 170, 180), 0.9), W / 2, 420)
            rrect(d, (70, 500, W - 70, 1000), 50, (28, 28, 36))
            lines_c(im, f"« {q} »", 82, WHITE, 750, maxw=880, sc=pop(t, T0 + qi * QD, 0.2))
            if tq < 3.0:
                k = 3 - int(tq)
                r = 110; cx, cy = W / 2, 1250
                d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=MID, width=16)
                d.arc((cx - r, cy - r, cx + r, cy + r), -90, -90 + 360 * (1 - (tq % 1.0)), fill=LIME, width=16)
                paste_c(im, text_img(str(k), 130, WHITE, 0.9), cx, cy)
            else:
                sc = pop(t, T0 + qi * QD + 3.0, 0.2)
                lab = text_img("VRAI" if ans else "FAUX", 150, DARK if ans else WHITE, 0.84)
                col = LIME if ans else RED
                rrect(d, (W / 2 - lab.width / 2 - 60, 1150, W / 2 + lab.width / 2 + 60, 1340), 50, col)
                paste_c(im, lab, W / 2, 1245, sc)
                lines_c(im, why, 60, WHITE, 1490, maxw=900)
        else:
            lines_c(im, "Alors, combien sur 3 ?", 100, WHITE, 800, sc=pop(t, T_SCORE, 0.25))
        paste_c(im, text_img("REPFIX", 46, (120, 120, 130), 0.9), W / 2, 1830)
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()

# ---------- 33 : tier list (fond clair, les éléments tombent dans les rangs) ----------
def tier(n):
    tiers = [("S", LIME), ("A", (120, 220, 255)), ("B", (255, 214, 90)), ("C", ORANGE), ("D", RED)]
    items = [("Progresser", 0), ("Protéines", 0), ("Dormir 7-9 h", 1),
             ("Régularité", 1), ("Créatine", 2), ("Le pump", 3), ("BCAA", 4), ("Brûleur de graisse", 4)]
    T0, STEP = 2.0, 1.45
    T_CTA = T0 + STEP * len(items) + 1.6; dur = T_CTA + 2.6
    p = out_pipe(f"v{n}_video.mp4")
    rows_y = [520 + i * 230 for i in range(5)]
    for fi in range(int(dur * FPS)):
        t = fi / FPS
        im = Image.new("RGBA", (W, H), BG + (255,)); d = ImageDraw.Draw(im)
        progress(d, t, dur, False)
        if t >= T_CTA:
            cta(im, d, t, T_CTA, False, "Pas d'accord ? Dis-le en commentaire"); p.stdin.write(im.convert("RGB").tobytes()); continue
        paste_c(im, text_img("TIER LIST", 120, INK, 0.84), W / 2, 170)
        lines_c(im, "ce qui fait VRAIMENT prendre du muscle", 64, INK, 300)
        for i, (lab, col) in enumerate(tiers):
            y = rows_y[i]
            rrect(d, (40, y, 200, y + 210), 24, col)
            paste_c(im, text_img(lab, 120, INK, 0.9), 120, y + 105)
            rrect(d, (215, y, W - 40, y + 210), 24, (226, 224, 216))
        cnt = [0] * 5
        for j, (name, ti) in enumerate(items):
            tt = T0 + j * STEP
            if t < tt: continue
            k = cnt[ti]; cnt[ti] += 1
            chip = text_img(name, 54 if len(name) < 12 else 46, WHITE, 0.88)
            cw = min(400, chip.width + 40); x = 235 + k * 415; y = rows_y[ti] + 105
            a = ease((t - tt) / 0.3); yy = y - (1 - a) * 300
            rrect(d, (x, yy - 60, x + 400, yy + 60), 20, INK)
            if chip.width > 370: chip = chip.resize((370, int(chip.height * 370 / chip.width)), Image.LANCZOS)
            paste_c(im, chip, x + 200, yy, pop(t, tt, 0.2))
        if t < T0:
            lines_c(im, "Tu serais d'accord ?", 70, RED, 1720)
        else:
            paste_c(im, text_img("REPFIX", 46, INK, 0.9), W / 2, 1800)
        p.stdin.write(im.convert("RGB").tobytes())
    p.stdin.close(); p.wait()

SIM = {
    29: dict(dur=19.0, a="LENT", b="RAPIDE", question="Sur le curl biceps, lequel gagne ?",
             tempo=[(1.0, 3.0), (0.5, 0.5)], labels=["1 s monte · 3 s descend", "0,5 s · 0,5 s"], weeks=8,
             bars=[("Temps sous tension", 0.95, 0.45), ("Muscle", 0.82, 0.8), ("Puissance", 0.5, 0.92)],
             verdict="MÊME MUSCLE SI TU VAS PRÈS DE L'ÉCHEC", verdict2="Le seul vrai piège : lâcher la descente.",
             cta_extra="Toi, t'es team LENT ou team RAPIDE ?"),
    32: dict(dur=19.0, a="6 H", b="8 H", question="Même programme. Seul le sommeil change.",
             tempo=[(1.2, 1.2), (0.8, 0.8)], labels=["6 h de sommeil", "8 h de sommeil"], weeks=12, droop=[1, 0], zzz=True,
             bars=[("Récupération", 0.5, 0.92), ("Force", 0.62, 0.88), ("Énergie", 0.42, 0.9)],
             verdict="TU GRANDIS PAS À LA SALLE. TU GRANDIS AU LIT.", verdict2="Vise 7 à 9 h par nuit.",
             cta_extra="Tu dors combien d'heures, toi ?"),
}

if __name__ == "__main__":
    n = int(sys.argv[1])
    if n in SIM: simulation(n, SIM[n])
    elif n == 30: pov(n)
    elif n == 31: quiz(n)
    elif n == 33: tier(n)
