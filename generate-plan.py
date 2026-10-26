from pathlib import Path
from html import escape
s=['''<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="1080" viewBox="0 0 1400 1080"><defs><pattern id="grid" width="25" height="25" patternUnits="userSpaceOnUse"><path d="M25 0H0V25" fill="none" stroke="#e9f0f2" stroke-width=".6"/></pattern><marker id="arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto-start-reverse"><path d="M7 1L1 4L7 7" fill="none" stroke="#32867f" stroke-width="1"/></marker></defs><rect width="1400" height="1080" fill="white"/><rect x="22" y="22" width="1356" height="1036" fill="url(#grid)" stroke="#7e9aa5"/><style>text{font-family:Arial,sans-serif;fill:#264b5b}.part{fill:#e5edf0;stroke:#426b7b;stroke-width:1.6}.motor{fill:#cfe6e3;stroke:#288b80;stroke-width:1.6}.stem{fill:#edf3f5;stroke:#426b7b;stroke-width:1.4}.dim{fill:none;stroke:#32867f;stroke-width:1}.ext{stroke:#91b3b8;stroke-width:.8}.label{fill:#32867f;font-size:14px}.small{font-size:12px;fill:#7c929b}.centre{stroke:#95b1b9;stroke-dasharray:8 4 2 4;stroke-width:.8}</style>''']
def text(x,y,t,size=14,anchor='start',cls='',rotate=None):
    rot=f' transform="rotate({rotate} {x} {y})"' if rotate else ''
    s.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" class="{cls}"{rot}>{escape(t)}</text>')
def line(x1,y1,x2,y2,cls='ext'):
    s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"/>')
def rect(x,y,w,h,cls='part'):
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="{cls}"/>')
def circle(x,y,r,cls='part'):
    s.append(f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/>')
def dh(x1,x2,y,oy1,oy2,label):
    line(x1,oy1,x1,y+6);line(x2,oy2,x2,y+6)
    s.append(f'<path d="M{x1} {y}H{x2}" class="dim" marker-start="url(#arrow)" marker-end="url(#arrow)"/>')
    text((x1+x2)/2,y-8,label,14,'middle','label')
def dv(x,y1,y2,ox,label):
    line(ox,y1,x+5,y1);line(ox,y2,x+5,y2)
    s.append(f'<path d="M{x} {y1}V{y2}" class="dim" marker-start="url(#arrow)" marker-end="url(#arrow)"/>')
    text(x-8,(y1+y2)/2,label,14,'middle','label',-90)
text(48,61,'HIDROTRACK / CARRUAJE PORTA INSTRUMENTO',24)
text(48,87,'HT–01 · Propuesta conceptual para banco hidrométrico',14)
text(1348,60,'REVISIÓN 01',14,'end');text(1348,84,'COTAS EN mm · NO MEDIR SOBRE EL DIBUJO',12,'end','small')
line(22,110,1378,110)
text(62,142,'01 / VISTA FRONTAL',16);text(775,142,'02 / VISTA LATERAL',16)
# Front projection: horizontal Y, vertical Z. Contact rail = y 300 px.
k=.30;fx=350;z0=320
Y=lambda mm:fx+mm*k
Z=lambda mm:z0-mm*k
# Frame and wheel supports.
rect(Y(-800),Z(205),1600*k,60*k)
for y in [-780,780]:rect(Y(y-20),Z(205),40*k,60*k)
for y in [-700,700]:
    rect(Y(y-30),Z(120),60*k,120*k)
    rect(Y(y-46),Z(131),12*k,142*k)
    rect(Y(y-45),Z(161),90*k,55*k)
    rect(Y(y-35),Z(0),70*k,20*k)
line(Y(-750),Z(60),Y(750),Z(60),'centre')
rect(Y(745),Z(78),80*k,36*k,'motor')
rect(Y(830),Z(80),40*k,40*k,'motor')
text(Y(850),Z(110),'S01',10,'middle')
rect(Y(-650),Z(240),300*k,35*k)
rect(Y(-625),Z(440),250*k,195*k,'motor')
rect(Y(-60),Z(250),120*k,45*k,'motor')
rect(Y(-10),Z(250),20*k,1050*k,'stem')
rect(Y(-35),Z(-730),70*k,60*k,'motor')
circle(Y(0),Z(-800),26*k)
line(Y(-65),Z(-800),Y(65),Z(-800),'part');line(Y(0),Z(-865),Y(0),Z(-735),'part')
line(Y(0),Z(280),Y(0),Z(-890),'centre')
dh(Y(-800),Y(800),172,Z(205),Z(205),'1 600 — ancho del bastidor')
dh(Y(-700),Y(700),361,Z(0),Z(0),'1 400 — ejes de rieles')
dv(642,Z(250),Z(-800),Y(35),'1 050 — vástago')
text(62,605,'Eje del instrumento: 800 mm bajo el contacto de rodadura.',12,cls='small')
text(62,624,'Motor esquemático: altura máxima 440 mm sobre el contacto.',12,cls='small')
# side view X/Z
sx=1030;X=lambda mm:sx+mm*k
rect(X(-325),Z(205),650*k,60*k)
for x in [-225,225]:
    circle(X(x),Z(60),60*k);circle(X(x),Z(60),23*k)
    rect(X(x-50),Z(161),100*k,55*k)
rect(X(40),Z(240),280*k,35*k)
rect(X(65),Z(440),230*k,195*k,'motor')
rect(X(-60),Z(250),120*k,45*k,'motor')
rect(X(-10),Z(250),20*k,1050*k,'stem')
rect(X(-75),Z(-774),150*k,52*k,'stem')
rect(X(-125),Z(-720),8*k,160*k,'motor')
s.append(f'<path d="M{X(100)} {Z(-790)}L{X(200)} {Z(-740)}V{Z(-860)}L{X(100)} {Z(-810)}Z" class="part"/>')
dh(X(-325),X(325),175,Z(205),Z(205),'650')
dh(X(-225),X(225),370,Z(60),Z(60),'450 — entre ejes')
dv(1220,Z(0),Z(-800),X(0),'800 — hasta eje del instrumento')
line(800,Z(0),1170,Z(0),'centre');text(805,Z(0)-8,'CONTACTO DE RODADURA / COTA 0',10,cls='small')
text(800,600,'Ø120 — ruedas (pestaña esquemática Ø142)',12,cls='small')
text(800,620,'Ø20 — vástago propuesto',12,cls='small')
line(22,652,1378,652)
text(62,686,'03 / VISTA SUPERIOR',16);text(775,686,'04 / REFERENCIA DE LA PISCINA',16)
# plan Y horizontal, X vertical
py=815;PX=lambda mm:py+mm*k
for y in [-780,780]:rect(Y(y-20),PX(-325),40*k,650*k)
for x in [-305,305]:rect(Y(-760),PX(x-20),1520*k,40*k)
rect(Y(-760),PX(-35),1520*k,70*k)
for x in [-225,225]:
    for y in [-700,700]:rect(Y(y-30),PX(x-60),60*k,120*k)
rect(Y(830),PX(205),40*k,40*k,'motor');rect(Y(745),PX(207),80*k,36*k,'motor');
rect(Y(-625),PX(65),250*k,230*k,'motor');rect(Y(-70),PX(-60),140*k,120*k,'motor');circle(Y(0),PX(0),10*k,'stem')
line(Y(-850),PX(0),Y(850),PX(0),'centre')
line(Y(0),PX(-360),Y(0),PX(360),'centre')
dh(Y(-800),Y(800),948,PX(325),PX(325),'1 600')
dv(660,PX(-325),PX(325),Y(800),'650')
text(62,982,'Marco abierto · travesaño central · cuatro ruedas',12,cls='small')
# pool plan proportion 8m : 1.2m at 0.05 px/mm
rect(835,772,400,60,'stem')
s.append('<rect x="835" y="772" width="400" height="60" fill="#dff1f3" stroke="#6b9eaa"/>')
line(835,767,1235,767,'part');line(835,837,1235,837,'part')
rect(1013.75,762,32.5,80,'motor')
dh(835,1235,735,772,772,'8 000 — largo interior indicado')
dv(1280,772,832,1235,'1 200')
text(835,881,'Profundidad interior propuesta: 1 000',14)
text(835,904,'Altura de agua propuesta: 800 · borde libre: 200',13)
text(835,927,'Contacto de riel supuesto: 100 sobre el borde.',12,cls='small')
text(835,950,'Eje del molinete: 500 bajo la superficie del agua.',12,cls='small')
text(835,973,'El largo útil de ensayo depende de límites y frenado.',12,cls='small')
line(22,1000,1378,1000)
text(48,1024,'DISEÑO CONCEPTUAL — NO APTO PARA FABRICACIÓN SIN REVISIÓN MECÁNICA',13)
text(48,1045,'Validar cargas, rigidez, rieles, transmisión y dimensiones reales. Vistas con escalas de representación diferentes.',11,cls='small')
text(1348,1034,'Axl André Coronado Telles · HT–01',12,'end')
s.append('</svg>')
Path('carruaje-plano.svg').write_text(''.join(s))
