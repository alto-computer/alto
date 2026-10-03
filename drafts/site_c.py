import os
exec(open('drafts.py').read().split('# ---------- A. Surface ----------')[0])
SITE=os.path.expanduser('~/personal/alto-site')
G='#efefed'      # ground, a calm warm grey
INK2='#161817'; MUT='#6c706d'; WAVE2='#a9bcc0'
def mirrored(tx,ty,k,bg,cid):
    cx=tx+1205*k
    return f'<g transform="translate({2*cx},0) scale(-1,1)">{otter(tx,ty,k,bg,cid)}</g>', (2*cx-(tx+1930*k), ty+1440*k)
k=.25; tx=720-1205*k; ty=40-600*k
og,(px,py)=mirrored(tx,ty,k,G,'c')
wy=ty+1655*k
cx=[290,720,1150]; RY=566
thread=f"M{px},{py} C{px-10},{py+150} {cx[0]-120},{RY} {cx[0]-60},{RY} L{cx[2]+130},{RY}"
cs=''
for (n,a,b),x in zip(Q,cx):
    cs+=knot(x,RY,G)+f'<text class="geo" x="{x}" y="{RY+48}" text-anchor="middle" font-size="15" font-weight="500" letter-spacing="2.6" fill="{MUT}">{n.upper()}</text>'
    cs+=f'<text class="ren" x="{x}" y="{RY+88}" text-anchor="middle" font-size="25" fill="{INK2}">{a}</text><text class="ren" x="{x}" y="{RY+120}" text-anchor="middle" font-size="25" fill="{INK2}">{b}</text>'
scene=f'''<svg class="scene" viewBox="0 60 1440 660" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Clew the otter floats on calm water holding a red thread. The thread drops into a line that passes three questions and ends at a cursor.">
<path d="M440,{wy} C540,{wy-10} 620,{wy+10} 720,{wy} S900,{wy-10} 1000,{wy}" fill="none" stroke="{WAVE2}" stroke-width="3" stroke-linecap="round"/>
{og}
<text class="geo" x="720" y="{wy+96}" text-anchor="middle" font-size="96" font-weight="500" letter-spacing="-1.5" fill="{INK2}">Alto</text>
<text class="geo" x="720" y="{wy+148}" text-anchor="middle" font-size="27" fill="{MUT}">A browser harness that keeps you in the loop.</text>
<path d="{thread}" fill="none" stroke="{THREAD}" stroke-width="3.2" stroke-linecap="round"/>
{cs}{cursor(cx[2]+130,RY-8,.8)}
</svg>'''
ICON_HOME='<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'
ICON_BLOG='<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M13 8H7"/><path d="M17 12H7"/>'
X_LOGO='<path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/>'
def nav(active):
    def item(href,label,icon,on):
        cls=' class="on" aria-current="page"' if on else ''
        return f'<a href="{href}"{cls}><svg viewBox="0 0 24 24" aria-hidden="true">{icon}</svg>{label}</a>'
    return f'<nav aria-label="Main">{item("index.html","Home",ICON_HOME,active=="home")}{item("blog.html","Blog",ICON_BLOG,active=="blog")}</nav>'
CSS=f'''
/* Layout: nav top right, the otter scene centred in the space left over, footer on the baseline. Everything fits one screen. */
:root{{--ground:{G}; --ink:{INK2}; --muted:{MUT}; --pill:#e2e2df; --thread:{THREAD}; --thread-soft:#f3c4bd;
  --geo:"Jost","Futura","Avenir Next",system-ui,sans-serif; --ren:"EB Garamond",Garamond,Georgia,serif; color-scheme:light}}
*{{box-sizing:border-box}}
html,body{{height:100%;margin:0}}
body{{background:var(--ground);color:var(--ink);font-family:var(--geo);-webkit-font-smoothing:antialiased}}
.frame{{height:100%;max-width:1120px;margin:0 auto;padding:22px 32px 26px;display:flex;flex-direction:column}}
.geo{{font-family:var(--geo)}} .ren{{font-family:var(--ren);font-style:italic}}
nav{{display:flex;justify-content:flex-end;gap:6px}}
nav a{{display:inline-flex;align-items:center;gap:7px;padding:7px 12px;border-radius:9px;font-size:15px;color:var(--muted);text-decoration:none;transition:background .15s,color .15s}}
nav a svg{{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round}}
nav a:hover{{color:var(--ink);background:var(--pill)}}
nav a.on{{color:var(--ink);background:var(--pill)}}
nav a.on svg path:last-child{{fill:var(--thread-soft)}}
nav a.on svg{{stroke:var(--ink)}}
main{{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}}
.scene{{width:100%;height:100%;max-height:680px;display:block}}
footer{{display:flex;justify-content:space-between;align-items:center;gap:16px;font-size:14px;color:var(--muted)}}
footer a{{display:inline-flex;align-items:center;gap:7px;color:var(--muted);text-decoration:none}}
footer a:hover{{color:var(--ink)}} footer svg{{width:13px;height:13px;fill:currentColor}}
a:focus-visible{{outline:2px solid var(--thread);outline-offset:2px}}
@media (prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
'''
def doc(title,active,inner,extra=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title><meta name="description" content="A browser harness that keeps you in the loop.">
<link rel="icon" type="image/png" href="assets/avatar.png">{FONTS}<style>{CSS}{extra}</style></head><body><div class="frame">
{nav(active)}<main>{inner}</main>
<footer><span>© 2026 Alto Computer</span><a href="https://x.com/altodotcomputer"><svg viewBox="0 0 24 24" aria-hidden="true">{X_LOGO}</svg>@altodotcomputer</a></footer>
</div></body></html>'''
open(f'{SITE}/index.html','w').write(doc('Alto','home',scene))
blog_extra='.empty{text-align:center;display:grid;gap:10px;justify-items:center} .empty img{width:120px;height:auto;margin-bottom:6px} .empty h1{font-weight:500;font-size:34px;margin:0;letter-spacing:-.01em} .empty p{margin:0;color:var(--muted);font-size:17px}'
blog='<div class="empty"><img src="assets/otter.svg" alt=""><h1>Notes</h1><p>Measurements and findings from building Alto. The first note is on its way.</p></div>'
open(f'{SITE}/blog.html','w').write(doc('Alto · Notes','blog',blog,blog_extra))
print('ok')
