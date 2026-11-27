# Carrousels TikTok RepFix du 27/11 : 5 formats différents (banque-formats-viraux.md)
# c03 vrai/faux · c04 POV · c05 tier list · c06 note iPhone · c07 faux SMS
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "carrousel.py")).read()
exec(src.split('\nA="rfx-c01')[0])          # récupère slide(), para(), place(), build() sans relancer c01/c02
from PIL import Image, ImageDraw
import illus
from illus import canvas, done, L, C, R, P, GR

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
GRN = (52, 199, 89); BLUE = (10, 132, 255); GBUB = (229, 229, 234)

def header(im, n, total, dark=True, brand=LIME):
    im.alpha_composite(text_img("REPFIX", 40, brand, 0.9), (90, 70))
    pg = text_img(f"{n}/{total}", 40, MUT if dark else (120, 120, 120), 0.9); im.alpha_composite(pg, (W-90-pg.width, 70))

def centered(im, txt, sz, y, col, maxw=900, sq=0.86, lh=1.13):
    for ln in wrap(txt.split(" "), sz, maxw, sq):
        ti = text_img(ln, sz, col, sq); im.alpha_composite(ti, ((W-ti.width)//2, int(y))); y += int(sz*lh)
    return y

# ---------- illustrations nouvelles ----------
def big_q():
    im, d = canvas(460, 420)
    C(d, 150, 210, 130, RED); C(d, 330, 210, 130, LIME)
    t1 = text_img("?", 230, OFF, 1); t2 = text_img("?", 230, INK, 1)
    im2 = done(im); im2.alpha_composite(t1, (150-t1.width//2, 210-t1.height//2)); im2.alpha_composite(t2, (330-t2.width//2, 210-t2.height//2))
    return im2

def stamp(word, col):
    t = text_img(word, 130, col, 0.9)
    im = Image.new("RGBA", (t.width+80, t.height+50), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((4, 4, im.width-4, im.height-4), 26, outline=col, width=12)
    im.alpha_composite(t, (40, 25))
    return im.rotate(-8, expand=True, resample=Image.BICUBIC)

def top_heavy():   # bonhomme énorme en haut, jambes allumettes
    im, d = canvas(520, 560)
    P(d, [(90, 120), (430, 120), (330, 330), (190, 330)], OFF)          # buste en V géant
    C(d, 260, 70, 50, OFF)                                               # tête
    L(d, [(100, 135), (40, 300)], OFF, 70); L(d, [(420, 135), (480, 300)], OFF, 70)   # bras énormes
    C(d, 40, 320, 34, OFF); C(d, 480, 320, 34, OFF)
    L(d, [(230, 330), (225, 530)], OFF, 9); L(d, [(290, 330), (295, 530)], OFF, 9)    # jambes allumettes
    L(d, [(225, 530), (200, 540)], OFF, 9); L(d, [(295, 530), (320, 540)], OFF, 9)
    for x, y in ((150, 460), (370, 460)): illus.bolt(d, x, y-40, 60, RED)
    return done(im)

def squat_fig():   # squat de profil, cuisses en vert
    im, d = canvas(520, 480)
    L(d, [(60, 450), (470, 450)], GR, 8)
    C(d, 240, 90, 44, OFF)
    L(d, [(250, 140), (190, 280)], OFF, 60)                  # dos penché
    L(d, [(140, 160), (360, 160)], OFF, 18); R(d, (110, 125, 150, 195), 10, LIME); R(d, (350, 125, 390, 195), 10, LIME)  # barre
    L(d, [(190, 280), (330, 300)], LIME, 56)                 # cuisse
    L(d, [(330, 300), (300, 440)], OFF, 44)                  # tibia
    L(d, [(300, 440), (360, 448)], OFF, 22)
    return done(im)

def pill_tub():
    im, d = canvas(420, 460)
    R(d, (110, 40, 310, 100), 18, LIME); R(d, (90, 100, 330, 420), 40, OFF)
    R(d, (120, 200, 300, 300), 14, INK)
    t = text_img("CRÉATINE", 34, LIME, 0.9); im2 = done(im); im2.alpha_composite(t, (210-t.width//2, 250-t.height//2)); return im2

def flame_x():
    im, d = canvas(420, 420)
    P(d, [(210, 40), (300, 200), (280, 330), (140, 330), (120, 200), (170, 150)], (255, 140, 60))
    P(d, [(210, 170), (250, 260), (240, 320), (180, 320), (170, 260)], (255, 210, 90))
    L(d, [(80, 80), (340, 360)], RED, 26); L(d, [(340, 80), (80, 360)], RED, 26)
    return done(im)

# ---------- c03 VRAI OU FAUX ----------
def vf(n, T, claim, verdict, expl):
    im = Image.new("RGBA", (W, H), INK+(255,)); header(im, n, T)
    tag = text_img("VRAI OU FAUX ?", 50, INK, 0.9); d = ImageDraw.Draw(im)
    d.rounded_rectangle((90, 170, 90+tag.width+50, 170+tag.height+34), 20, fill=LIME); im.alpha_composite(tag, (115, 187))
    y = centered(im, "« " + claim + " »", 78, 320, OFF, 880, 0.86, 1.15)
    st = stamp(verdict, RED if verdict == "FAUX" else LIME)
    im.alpha_composite(st, ((W-st.width)//2, y+30)); y += st.height+80
    para(im, expl, 52, y, OFF, 880, 1.25)
    return im

def c03():
    T = 5; name = f"{OUT}/rfx-c03-vrai-ou-faux"
    build(name, [
        slide(1, T, "VRAI OU FAUX : 3 IDÉES REÇUES DE SALLE", hook=True, sub="Réponds dans ta tête avant de swiper", il=big_q()),
        vf(2, T, "Il faut manger toutes les 3 heures pour prendre du muscle", "FAUX",
           "Ce qui compte : tes protéines et tes calories sur toute la journée. 3 repas ou 6 repas, c'est comme tu préfères."),
        vf(3, T, "Avec des abdos tous les jours, tu perds ton ventre", "FAUX",
           "On ne choisit pas où on perd le gras. Les abdos renforcent, c'est ton alimentation qui fait fondre le ventre."),
        vf(4, T, "La créatine est un des compléments les plus étudiés", "VRAI",
           "3 à 5 g par jour, tous les jours. Un peu plus de force et de répétitions. Pas besoin de « phase de charge »."),
        slide(5, T, "T'avais combien de bonnes réponses ?", body="Dis ton score en commentaire. Et écris REP, je t'envoie l'appli.", cta=True, il=illus.comment_rep()),
    ])

# ---------- c04 POV ----------
def c04():
    T = 5; name = f"{OUT}/rfx-c04-pov-jambes"
    build(name, [
        slide(1, T, "POV : 45 MIN DE BICEPS, 0 MIN DE JAMBES", hook=True, sub="(on se reconnaît tous)", il=top_heavy()),
        slide(2, T, "Le problème", body="Tes jambes, c'est presque la moitié de tes muscles. Les zapper, c'est freiner tout ton physique, pas juste le bas.", il=top_heavy()),
        slide(3, T, "La séance jambes minimum", lines=[("1", "Squat ou presse", LIME), ("2", "Fentes", LIME), ("3", "Soulevé jambes tendues", LIME)], il=squat_fig()),
        slide(4, T, "L'astuce anti-flemme", body="Mets ta séance jambes en début de semaine. Le lundi, t'as encore la motivation. Le vendredi, t'as que des excuses.", il=illus.calendar_up()),
        slide(5, T, "Tague le pote qui zappe les jambes", body="Et écris REP en commentaire, je t'envoie l'appli.", cta=True, il=illus.comment_rep()),
    ])

# ---------- c05 TIER LIST ----------
def tier_slide(n, T):
    im = Image.new("RGBA", (W, H), INK+(255,)); header(im, n, T); d = ImageDraw.Draw(im)
    y = 170
    for ti in wrap("TIER LIST DES COMPLÉMENTS".split(" "), 80, 900, 0.84):
        t = text_img(ti, 80, OFF, 0.84); im.alpha_composite(t, (90, y)); y += 92
    y += 30
    rows = [("S", LIME, "Créatine"), ("A", (120, 220, 90), "Whey (si tu manques de protéines)"),
            ("B", (255, 214, 10), "Caféine avant la séance"), ("C", (255, 149, 0), "BCAA"),
            ("D", RED, "« Brûle-graisse »")]
    for letter, col, txt in rows:
        d.rounded_rectangle((90, y, 990, y+160), 24, fill=(30, 30, 36))
        d.rounded_rectangle((90, y, 250, y+160), 24, fill=col); d.rectangle((220, y, 250, y+160), fill=col)
        lt = text_img(letter, 100, INK, 0.9); im.alpha_composite(lt, (170-lt.width//2, y+80-lt.height//2))
        lines = wrap(txt.split(" "), 50, 690, 0.9); yy = y+80-len(lines)*30
        for ln in lines:
            im.alpha_composite(text_img(ln, 50, OFF, 0.9), (285, yy)); yy += 60
        y += 180
    return im

def c05():
    T = 5; name = f"{OUT}/rfx-c05-tier-list-complements"
    build(name, [
        slide(1, T, "TIER LIST DES COMPLÉMENTS", hook=True, sub="Ce qui vaut vraiment ton argent", il=pill_tub()),
        tier_slide(2, T),
        slide(3, T, "Pourquoi la créatine en S", body="3 à 5 g par jour, tous les jours, à n'importe quelle heure. Pas chère, très étudiée : plus de force et de répétitions.", il=pill_tub()),
        slide(4, T, "Pourquoi les brûle-graisse en D", body="Souvent de la caféine vendue très cher. Ce qui fait perdre du gras, c'est ton assiette, pas une gélule.", il=flame_x()),
        slide(5, T, "T'es d'accord avec ce classement ?", body="Dis-le en commentaire. Et écris REP, je t'envoie l'appli.", cta=True, il=illus.comment_rep()),
    ])

# ---------- c06 NOTE IPHONE ----------
NBG = (255, 255, 255); NYEL = (227, 170, 0); NTXT = (20, 20, 22); NMUT = (142, 142, 147)
def note(n, T, items, title=None, il=None, last=False):
    im = Image.new("RGBA", (W, H), NBG+(255,)); d = ImageDraw.Draw(im)
    im.alpha_composite(text_img("<  Notes", 46, NYEL, 1, False), (50, 60))
    im.alpha_composite(text_img("OK", 46, NYEL, 1), (W-130, 60))
    pg = text_img(f"{n}/{T}", 36, NMUT, 1, False); im.alpha_composite(pg, ((W-pg.width)//2, 68))
    y = 170
    if title:
        im.alpha_composite(text_img("27 novembre 2026 à 08:52", 34, NMUT, 1, False), (70, y)); y += 70
        for ln in wrap(title.split(" "), 76, 940, 0.95):
            im.alpha_composite(text_img(ln, 76, NTXT, 0.95), (70, y)); y += 88
        y += 30
    for num, head, body in items:
        im.alpha_composite(text_img(f"{num}. {head}", 58, NTXT, 0.95), (70, y)); y += 76
        for ln in wrap(body.split(" "), 50, 920, 1.0):
            im.alpha_composite(text_img(ln, 50, (60, 60, 67), 1.0, False), (70, y)); y += 64
        y += 44
    if last:
        d.rounded_rectangle((60, y, 1020, y+150), 26, fill=LIME)
        t = text_img("Écris REP, je t'envoie l'appli", 54, INK, 0.92); im.alpha_composite(t, ((W-t.width)//2, y+75-t.height//2)); y += 190
    if il is not None:
        place(im, il, y+20, 1300, 380)
    return im

def ink_on_white(il):   # recolore une illus claire pour fond blanc
    px = il.load()
    for x in range(il.width):
        for yy in range(il.height):
            r, g, b, a = px[x, yy]
            if a and r > 200 and g > 200 and b > 200: px[x, yy] = (40, 40, 46, a)
    return il

def c06():
    T = 5; name = f"{OUT}/rfx-c06-note-1re-annee"
    build(name, [
        note(1, T, [], title="Ce que j'aurais aimé savoir à ma 1re année de salle", il=ink_on_white(illus.notebook())),
        note(2, T, [(1, "Note tes charges", "Sinon tu ne sais jamais si tu progresses. Bats ton record la fois d'après."),
                    (2, "Les jambes, c'est pas optionnel", "1 séance par semaine minimum. Personne ne regrette.")], il=ink_on_white(squat_fig())),
        note(3, T, [(3, "La technique avant le poids", "L'ego lifting, c'est la blessure assurée. Contrôle la descente."),
                    (4, "Dors 7 à 9 heures", "C'est pendant le sommeil que tu récupères et que tu construis.")], il=ink_on_white(illus.progress_chart())),
        note(4, T, [(5, "Assez de protéines", "Autour de 1,6 g par kilo de poids de corps par jour."),
                    (6, "Simple > parfait", "Un programme simple que tu tiens bat un programme parfait que tu lâches.")], il=ink_on_white(pill_tub())),
        note(5, T, [(7, "Ne plus improviser", "Savoir quoi faire à chaque séance, c'est ce qui m'a fait passer un cap.")], last=True, il=ink_on_white(illus.calendar_up())),
    ])

# ---------- c07 FAUX SMS ----------
def sms(n, T, msgs, cta=False, top=None):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 255)); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 230), fill=(22, 22, 24))
    im.alpha_composite(text_img("<", 60, BLUE, 1), (40, 115))
    C2 = 64; d.ellipse((W//2-C2//2*1-10, 40, W//2+C2//2+10, 40+C2+20), fill=(110, 110, 120))
    t = text_img("K", 48, OFF, 1); im.alpha_composite(t, (W//2-t.width//2, 62))
    t = text_img("Kylian (salle)", 36, OFF, 1, False); im.alpha_composite(t, (W//2-t.width//2, 140))
    pg = text_img(f"REPFIX  {n}/{T}", 32, LIME, 0.9); im.alpha_composite(pg, (W-60-pg.width, 125))
    y = 290
    if top:
        t = text_img(top, 34, NMUT, 1, False); im.alpha_composite(t, (W//2-t.width//2, y)); y += 80
    for who, txt in msgs:
        me = who == "moi"
        lines = wrap(txt.split(" "), 56, 640, 1.0)
        tis = [text_img(l, 56, OFF if me else INK, 1.0, False) for l in lines]
        bw = max(t.width for t in tis)+70; bh = len(tis)*70+50
        x0 = W-60-bw if me else 60
        d.rounded_rectangle((x0, y, x0+bw, y+bh), 44, fill=BLUE if me else GBUB)
        yy = y+25
        for t in tis: im.alpha_composite(t, (x0+35, yy)); yy += 70
        y += bh+30
    if cta:
        d.rounded_rectangle((60, y+40, 1020, y+220), 30, fill=LIME)
        t = text_img("Écris REP en commentaire", 64, INK, 0.9); im.alpha_composite(t, ((W-t.width)//2, y+90))
        t = text_img("et abonne-toi pour plus de conseils sport", 40, INK, 0.95, False); im.alpha_composite(t, ((W-t.width)//2, y+168))
    return im

def c07():
    T = 5; name = f"{OUT}/rfx-c07-sms-pote-stagne"
    build(name, [
        sms(1, T, [("lui", "Frérot je stagne depuis 3 mois"), ("lui", "Je comprends pas, je vais à la salle tous les jours"),
                   ("moi", "Tu notes tes séances ?"), ("lui", "Non je fais au feeling")], top="Hier 23:47"),
        sms(2, T, [("moi", "Tu dors combien ?"), ("lui", "5 h, je joue tard"), ("moi", "..."), ("lui", "Quoi ?")]),
        sms(3, T, [("moi", "Et les jambes ?"), ("lui", "Les quoi ?"), ("moi", "Ok je vois")]),
        sms(4, T, [("moi", "3 règles : note tout, dors 7 h minimum, jambes 1 fois par semaine"), ("lui", "Et je retiens tout ça comment ?")]),
        sms(5, T, [("moi", "Je t'envoie l'appli qui fait tout ça pour toi"), ("lui", "Envoie !!")], cta=True),
    ])

if __name__ == "__main__":
    which = sys.argv[2:] or ["c03", "c04", "c05", "c06", "c07"]
    for w in which: globals()[w]()
