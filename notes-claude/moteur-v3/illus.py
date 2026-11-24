# Illustrations vectorielles flat (dessinées à 3x puis réduites, bords lisses)
from PIL import Image, ImageDraw
import math
INK=(11,11,15); LIME=(182,255,59); OFF=(242,241,236); RED=(255,59,48); GR=(60,60,70); DG=(30,30,36)
S=3
def canvas(w,h): 
    im=Image.new("RGBA",(w*S,h*S),(0,0,0,0)); return im, ImageDraw.Draw(im)
def done(im): return im.resize((im.width//S, im.height//S), Image.LANCZOS)
def L(d,pts,col,w): 
    p=[(x*S,y*S) for x,y in pts]; d.line(p,fill=col,width=int(w*S),joint="curve")
    for x,y in p: r=w*S/2; d.ellipse((x-r,y-r,x+r,y+r),fill=col)
def C(d,x,y,r,col,outline=None,w=0): d.ellipse(((x-r)*S,(y-r)*S,(x+r)*S,(y+r)*S),fill=col,outline=outline,width=int(w*S))
def R(d,box,rad,col,outline=None,w=0): d.rounded_rectangle([v*S for v in box],int(rad*S),fill=col,outline=outline,width=int(w*S))
def P(d,pts,col): d.polygon([(x*S,y*S) for x,y in pts],fill=col)

def bolt(d,x,y,s,col):
    P(d,[(x,y),(x+s*0.5,y),(x+s*0.2,y+s*0.45),(x+s*0.55,y+s*0.45),(x-s*0.1,y+s*1.1),(x+s*0.1,y+s*0.6),(x-s*0.2,y+s*0.6)],col)

def biceps(pain=True):  # bras contracté avec éclairs de douleur
    im,d=canvas(560,420)
    # avant-bras vertical + bras horizontal
    L(d,[(90,330),(320,330)],OFF,90)        # bras
    L(d,[(320,330),(345,150)],OFF,78)       # avant-bras
    C(d,352,112,56,OFF)                     # poing
    d.chord([120*S,200*S,320*S,400*S],180,360,fill=OFF)   # biceps gonflé au-dessus du bras
    L(d,[(185,262),(250,250)],INK,9)
    if pain:
        bolt(d,150,90,95,RED); bolt(d,450,170,80,RED); bolt(d,60,180,60,RED)
    return done(im)

def dumbbell_slow():   # haltère + flèche descente lente
    im,d=canvas(560,420)
    R(d,(150,170,410,200),12,OFF)
    for x in (120,150,380,410): pass
    R(d,(100,110,150,260),18,LIME); R(d,(410,110,460,260),18,LIME)
    R(d,(70,135,105,235),14,LIME); R(d,(455,135,490,235),14,LIME)
    # flèche vers le bas pointillée
    for i in range(4): R(d,(268,280+i*28,292,298+i*28),6,OFF)
    P(d,[(250,400),(310,400),(280,415)],OFF); P(d,[(245,395),(315,395),(280,418)],OFF)
    t=Image.new("RGBA",(1,1)); return done(im)

def soreness_bars():   # séances 1-2-3 : douleur qui baisse
    im,d=canvas(620,420)
    vals=[300,170,70]; labels=["S1","S2","S3"]
    for i,v in enumerate(vals):
        x=90+i*170
        R(d,(x,360-v,x+110,360),20,RED if i==0 else (255,140,100) if i==1 else LIME)
    L(d,[(60,370),(580,370)],GR,8)
    # flèche descendante
    L(d,[(120,30),(520,230)],OFF,10); P(d,[(530,235),(490,250),(505,210)],OFF)
    return done(im)

def progress_chart():  # charges qui montent
    im,d=canvas(620,420)
    vals=[110,160,210,270,330]
    for i,v in enumerate(vals):
        x=70+i*105; R(d,(x,370-v,x+75,370),16,GR if i<4 else LIME)
    pts=[(70+i*105+37,370-v-30) for i,v in enumerate(vals)]
    L(d,pts,LIME,10)
    for x,y in pts: C(d,x,y,14,LIME)
    L(d,[(40,378),(600,378)],GR,8)
    return done(im)

def notebook():  # carnet + check
    im,d=canvas(560,420)
    R(d,(150,30,420,400),26,OFF)
    for i in range(6): C(d,150,70+i*58,12,INK)
    for i in range(3):
        y=100+i*95
        R(d,(195,y,245,y+50),10,LIME); L(d,[(205,y+26),(218,y+40),(238,y+12)],INK,8)
        R(d,(265,y+14,385,y+36),10,(190,190,190))
    return done(im)

def comment_rep():  # bulle commentaire REP
    im,d=canvas(560,380)
    R(d,(60,40,500,280),60,INK); P(d,[(130,270),(220,270),(110,350)],INK)
    return done(im)

def stopwatch():
    im,d=canvas(460,460)
    R(d,(195,20,265,60),12,OFF); R(d,(218,55,242,85),6,OFF)
    C(d,230,260,170,OFF); C(d,230,260,140,INK)
    d.pieslice([(230-140)*S,(260-140)*S,(230+140)*S,(260+140)*S],-90,150,fill=LIME)
    C(d,230,260,105,INK)
    L(d,[(230,260),(230,175)],OFF,14); C(d,230,260,18,OFF)
    L(d,[(355,115),(385,85)],OFF,22)
    return done(im)

def plank(good=True):  # silhouette gainage vue de côté
    im,d=canvas(900,330)
    col=OFF
    L(d,[(40,300),(870,300)],GR,8)                 # sol
    # avant-bras au sol
    L(d,[(170,285),(290,285)],col,40)
    # bras (coude sous épaule)
    L(d,[(180,285),(195,175)],col,46)
    # tronc droit épaule->hanche->chevilles
    hip=(470,195) if good else (470,250)
    L(d,[(200,165),hip],col,78)
    L(d,[hip,(760,262)],col,56)
    L(d,[(760,262),(800,285)],col,34)
    C(d,135,150,48,col)                            # tête
    if good:
        for x in range(120,820,46): R(d,(x,108,x+24,116),3,LIME)   # ligne droite guide
    return done(im)

def gauge():
    im,d=canvas(560,330)
    box=[90*S,60*S,470*S,440*S]
    cols=[RED,OFF,LIME,(120,200,20)]
    for i,c in enumerate(cols): d.arc(box,180+i*45,180+(i+1)*45-3,fill=c,width=55*S)
    a=math.radians(180+150); L(d,[(280,250),(280+150*math.cos(a),250+150*math.sin(a))],OFF,14); C(d,280,250,24,OFF)
    return done(im)

def calendar_up():
    im,d=canvas(560,420)
    R(d,(90,70,400,380),28,OFF); R(d,(90,70,400,140),28,LIME); R(d,(90,110,400,140),0,LIME)
    for r in range(3):
        for c in range(4):
            x=120+c*70; y=170+r*65
            R(d,(x,y,x+45,y+42),10,LIME if (r*4+c)%4==0 else (200,200,200))
    L(d,[(330,330),(470,170)],LIME,18); P(d,[(495,140),(500,215),(440,185)],LIME)
    return done(im)
