import sys
sys.path.insert(0,'.')
from engine import text_img, wrap, paste_c, font
from PIL import Image, ImageDraw
W,H=1080,1350
INK=(11,11,15); LIME=(182,255,59); OFF=(242,241,236); RED=(255,59,48); MUT=(150,150,150)
def para(im, txt, sz, y, col, maxw=900, lh=1.25, squeeze=0.95, bold=False, align="left", x0=90):
    for ln in wrap(txt.split(" "), sz, maxw, squeeze):
        ti=text_img(ln, sz, col, squeeze, bold)
        x = x0 if align=="left" else (W-ti.width)//2
        im.alpha_composite(ti,(int(x),int(y))); y+=int(sz*lh)
    return y
def slide(n, total, title, body=None, lines=None, hook=False, sub=None, cta=False):
    im=Image.new("RGBA",(W,H),(LIME if cta else INK)+(255,)); d=ImageDraw.Draw(im)
    fg = INK if cta else OFF
    # en-tête
    im.alpha_composite(text_img("REPFIX",40,LIME if not cta else INK,0.9),(90,70))
    pg=text_img(f"{n}/{total}",40,MUT if not cta else INK,0.9); im.alpha_composite(pg,(W-90-pg.width,70))
    if hook:
        y=330
        for ln in wrap(title.split(" "),120,900,0.84):
            ti=text_img(ln,120,OFF,0.84); im.alpha_composite(ti,((W-ti.width)//2,y)); y+=136
        if sub:
            si=text_img(sub,52,INK,0.92); bw=si.width+60
            d.rounded_rectangle(((W-bw)//2,y+40,(W+bw)//2,y+40+si.height+40),24,fill=LIME)
            im.alpha_composite(si,((W-si.width)//2,y+60))
        sw=text_img("SWIPE  >>>",46,LIME,0.9); im.alpha_composite(sw,((W-sw.width)//2,1180))
        return im
    y=230
    for ln in wrap(title.split(" "),92,900,0.84):
        ti=text_img(ln,92,fg,0.84)
        if not cta: d.rectangle((86,y+58,90+ti.width+6,y+96),fill=(60,80,20))
        im.alpha_composite(ti,(90,y)); y+=104
    y+=50
    if body: y=para(im, body, 56, y, fg)
    if lines:
        for a,b,c in lines:
            d.rounded_rectangle((90,y,990,y+130),28,fill=(30,30,36) if not cta else INK)
            im.alpha_composite(text_img(a,54,c,0.9),(130,y+38))
            bi=text_img(b,54,OFF,0.9); im.alpha_composite(bi,(950-bi.width,y+38)); y+=150
    return im
def build(name, slides):
    import os; os.makedirs(name,exist_ok=True)
    for i,s in enumerate(slides,1):
        s.convert("RGB").save(f"{name}/{i:02d}.jpg",quality=93)
A="rfx-c01-courbatures"; T=6
build(A,[
 slide(1,T,"TES COURBATURES NE PROUVENT RIEN",hook=True,sub="(et c'est une bonne nouvelle)"),
 slide(2,T,"Pourquoi t'as des courbatures ?",body="Surtout quand tu fais un exercice nouveau, ou quand tu ralentis la descente. Ton corps n'est pas habitué, c'est tout."),
 slide(3,T,"Pourquoi elles disparaissent",body="Après 2 ou 3 séances du même exercice, ton corps s'adapte. Moins de courbatures, ça veut pas dire moins de muscle."),
 slide(4,T,"Le vrai signe de progrès",body="Tes charges ou tes répétitions montent d'une semaine à l'autre. Pas la douleur du lendemain."),
 slide(5,T,"Ce que tu fais maintenant",lines=[("1","Garde ton programme",LIME),("2","Note tes charges",LIME),("3","+1 rep ou +1 kg",LIME)]),
 slide(6,T,"Écris REP en commentaire",body="Je t'envoie l'appli. Et abonne-toi pour plus de conseils sport.",cta=True),
])
B="rfx-c02-test-gainage"; T=5
build(B,[
 slide(1,T,"TU TIENS COMBIEN DE TEMPS EN GAINAGE ?",hook=True,sub="Teste-toi, chrono en main"),
 slide(2,T,"La bonne position",body="Avant-bras au sol, coudes sous les épaules. Fesses serrées, ventre rentré, corps bien droit. Tu arrêtes dès que le bassin tombe."),
 slide(3,T,"Ton niveau",lines=[("< 30 s","Débutant",RED),("30 s à 1 min","Correct",OFF),("1 à 2 min","Solide",LIME),("> 2 min","Machine",LIME)]),
 slide(4,T,"Pour progresser",body="3 séries à 80 % de ton temps max, 3 fois par semaine. Ajoute 5 secondes chaque semaine."),
 slide(5,T,"Dis ton temps en commentaire",body="Et écris REP, je t'envoie l'appli. Abonne-toi pour plus de conseils sport.",cta=True),
])
