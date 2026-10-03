import os
body=open('otter_paths.txt').read()
OUT=os.path.expanduser('~/personal/alto-site/drafts')
INK='#151716'; MUTED='#6b706d'; THREAD='#cf3f31'; SKY='#f6f7f4'; WATER='#e8efee'; WALL='#cfdcdd'; WAVE='#9fb9bf'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=EB+Garamond:ital,wght@1,400&display=swap">'
def otter(tx,ty,k,bg,cid):
    # otter coords -> scene; clip removes the generated water + old thread; patch rounds the paw
    return f'''<clipPath id="{cid}"><rect x="400" y="600" width="1610" height="1060"/></clipPath>
<g transform="translate({tx},{ty}) scale({k})"><g clip-path="url(#{cid})"><g fill="{INK}">{body}</g></g>
<rect x="1940" y="1320" width="120" height="300" fill="{bg}"/>
<path d="M1880,1280 C1960,1330 1970,1470 1930,1580" fill="none" stroke="{INK}" stroke-width="40" stroke-linecap="round"/></g>'''
def paw(tx,ty,k): return (tx+1930*k, ty+1440*k)
def cursor(x,y,s=1): return f'<path transform="translate({x},{y}) scale({s})" d="M0 0 L0 27 L7 21 L12 32 L17 30 L12 19 L21 19 Z" fill="{INK}" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/>'
def knot(x,y,bg): return f'<circle cx="{x}" cy="{y}" r="7" fill="{bg}" stroke="{THREAD}" stroke-width="3"/>'
Q=[('Harness','How can an agent browse for hours','and still be trusted?'),
   ('Interface','How do you talk with an agent that works','for hours, and understand what it did?'),
   ('Eval','How do you measure a good experience,','not just a right answer?')]
def page(title,bodybg,svg):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>{FONTS}<style>html,body{{height:100%;margin:0}} body{{background:{bodybg};overflow:hidden}} svg{{display:block;width:100%;height:100%}}
.geo{{font-family:Jost,Futura,"Avenir Next",sans-serif}} .ren{{font-family:"EB Garamond",Garamond,Georgia,serif;font-style:italic}}</style></head><body>{svg}</body></html>'''

# ---------- A. Surface ----------
k=.27; tx=860; ty=448-1660*k; px,py=paw(tx,ty,k)
wave="M0,448 C160,436 320,460 480,448 S800,436 960,448 S1280,460 1440,448"
cols=[1010,590,170]  # thread travels right->left, away from the otter
thread=f"M{px},{py} C{px+30},{py+60} {px+10},{py+120} {px-60},560 L{cols[2]-40},560"
qs=''
for (n,a,b),x in zip(Q,cols):
    qs+=knot(x,560,WATER)+f'<text class="geo" x="{x}" y="616" font-size="15" font-weight="500" letter-spacing="2.4" fill="{INK}">{n.upper()}</text>'
    qs+=f'<text class="ren" x="{x}" y="660" font-size="27" fill="{INK}">{a}</text><text class="ren" x="{x}" y="696" font-size="27" fill="{INK}">{b}</text>'
svgA=f'''<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Alto">
<rect width="1440" height="900" fill="{SKY}"/>
{otter(tx,ty,k,SKY,'a')}
<path d="{wave} L1440,900 L0,900 Z" fill="{WATER}"/><path d="{wave}" fill="none" stroke="{WAVE}" stroke-width="3"/>
<text class="geo" x="160" y="250" font-size="132" font-weight="600" letter-spacing="-3" fill="{INK}">Alto</text>
<text class="geo" x="166" y="312" font-size="28" fill="{MUTED}">A browser harness that keeps you in the loop.</text>
<path d="{thread}" fill="none" stroke="{THREAD}" stroke-width="4" stroke-linecap="round"/>
{qs}{cursor(cols[2]-58,552,.9)}
<text class="geo" x="160" y="850" font-size="15" fill="{MUTED}">© 2026 Alto Computer</text>
<a href="https://x.com/altodotcomputer"><text class="geo" x="1280" y="850" font-size="15" text-anchor="end" fill="{INK}">@altodotcomputer</text></a>
</svg>'''
open(f'{OUT}/a-surface.html','w').write(page('Alto · Surface',f'linear-gradient({SKY} 50%,{WATER} 50%)',svgA))

# ---------- B. Loop ----------
k=.22; tx=1000-400*k-0; ty=120-600*k
px,py=paw(tx,ty,k)
# tagline with fixed lengths so the loop lands on "loop"
pre="A browser harness that keeps you in the"; word="loop."
prew=560; wordw=72; lx=170; ly=360
loopx=lx+prew+10; lcx=loopx+wordw/2
thread=(f"M{px},{py} C{px+40},{py+70} {px+20},{ly-120} {lcx+40},{ly-56} "
        f"C{lcx-60},{ly-70} {loopx-40},{ly-10} {loopx-10},{ly+16} "
        f"C{loopx+30},{ly+48} {loopx+wordw+50},{ly+36} {loopx+wordw+40},{ly-10} "
        f"C{loopx+wordw+30},{ly-50} {lcx-10},{ly-60} {lcx-30},{ly-20} "
        f"C{lcx-60},{ly+40} {lx+40},{ly+70} 120,470 L120,700")
rows=''
for i,(n,a,b) in enumerate(Q):
    y=500+i*86
    rows+=knot(120,y,SKY)+f'<text class="geo" x="160" y="{y+5}" font-size="14" font-weight="500" letter-spacing="2.4" fill="{MUTED}">{n.upper()}</text>'
    rows+=f'<text class="ren" x="300" y="{y+8}" font-size="26" fill="{INK}">{a} {b}</text>'
svgB=f'''<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Alto">
<rect width="1440" height="900" fill="{SKY}"/>
{otter(tx,ty,k,SKY,'b')}
<text class="geo" x="164" y="270" font-size="132" font-weight="600" letter-spacing="-3" fill="{INK}">Alto</text>
<text class="geo" x="{lx}" y="{ly}" font-size="28" fill="{MUTED}" textLength="{prew}" lengthAdjust="spacingAndGlyphs">{pre}</text>
<text class="geo" x="{loopx}" y="{ly}" font-size="28" font-weight="500" fill="{INK}" textLength="{wordw}" lengthAdjust="spacingAndGlyphs">{word}</text>
<path d="{thread}" fill="none" stroke="{THREAD}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
{rows}{cursor(112,700,.9)}
<text class="geo" x="164" y="850" font-size="15" fill="{MUTED}">© 2026 Alto Computer</text>
<a href="https://x.com/altodotcomputer"><text class="geo" x="1280" y="850" font-size="15" text-anchor="end" fill="{INK}">@altodotcomputer</text></a>
</svg>'''
open(f'{OUT}/b-loop.html','w').write(page('Alto · Loop',SKY,svgB))

# ---------- C. Nap (mascot first, like Capy) ----------
k=.34; w=1610*k; tx=720-(400+805)*k; ty=110-600*k
px,py=paw(tx,ty,k)
cx=[300,720,1140]
thread=f"M{px},{py} C{px+50},{py+80} {px+40},700 1200,700 L{cx[0]-90},700"
cs=''
for (n,a,b),x in zip(Q,cx):
    cs+=knot(x,700,SKY)+f'<text class="geo" x="{x}" y="748" text-anchor="middle" font-size="14" font-weight="500" letter-spacing="2.4" fill="{MUTED}">{n.upper()}</text>'
    cs+=f'<text class="ren" x="{x}" y="784" text-anchor="middle" font-size="22" fill="{INK}">{a}</text><text class="ren" x="{x}" y="812" text-anchor="middle" font-size="22" fill="{INK}">{b}</text>'
svgC=f'''<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Alto">
<rect width="1440" height="900" fill="{SKY}"/>
<path d="M330,{ty+1655*k} C470,{ty+1640*k} 560,{ty+1668*k} 720,{ty+1655*k} S980,{ty+1640*k} 1110,{ty+1655*k}" fill="none" stroke="{WAVE}" stroke-width="3" stroke-linecap="round"/>
{otter(tx,ty,k,SKY,'c')}
<text class="geo" x="720" y="560" text-anchor="middle" font-size="96" font-weight="600" letter-spacing="-2" fill="{INK}">Alto</text>
<text class="geo" x="720" y="612" text-anchor="middle" font-size="25" fill="{MUTED}">A browser harness that keeps you in the loop.</text>
<path d="{thread}" fill="none" stroke="{THREAD}" stroke-width="3.5" stroke-linecap="round"/>
{cs}{cursor(cx[0]-108,692,.85)}
<a href="https://x.com/altodotcomputer"><text class="geo" x="720" y="870" text-anchor="middle" font-size="15" fill="{MUTED}">@altodotcomputer</text></a>
</svg>'''
open(f'{OUT}/c-nap.html','w').write(page('Alto · Nap',SKY,svgC))
print('ok')
