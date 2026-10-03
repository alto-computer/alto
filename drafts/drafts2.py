import os
exec(open('drafts.py').read().split('# ---------- A. Surface ----------')[0])
def otterM(X,ty,k,bg,cid):  # mirrored: paw on the otter's left
    return f'<g transform="translate({X},0) scale(-1,1) translate({-X},0)">'+otter(X-1805*k,ty,k,bg,cid).replace(f'translate({X-1805*k},{ty})',f'translate({X-1805*k},{ty})')+'</g>'
# simpler: mirror whole otter group around its own center
def mirrored(tx,ty,k,bg,cid):
    cx=tx+1205*k
    return f'<g transform="translate({2*cx},0) scale(-1,1)">{otter(tx,ty,k,bg,cid)}</g>', (2*cx-(tx+1930*k), ty+1440*k)

# ---------- A. Surface: calm above, the work below ----------
k=.26; tx=120-400*k; ty=430-1660*k; px,py=paw(tx,ty,k)
wave="M0,430 C160,418 320,442 480,430 S800,418 960,430 S1280,442 1440,430"
X=640; TX=600
rows=''; ys=[520,628,736]
for (n,a,b),y in zip(Q,ys):
    rows+=knot(TX,y,WATER)+f'<text class="geo" x="{X}" y="{y+5}" font-size="14" font-weight="500" letter-spacing="2.4" fill="{MUTED}">{n.upper()}</text>'
    rows+=f'<text class="ren" x="{X+150}" y="{y+8}" font-size="26" fill="{INK}">{a}</text><text class="ren" x="{X+150}" y="{y+40}" font-size="26" fill="{INK}">{b}</text>'
thread=f"M{px},{py} C{px+30},{py+40} {TX},{py+20} {TX},470 L{TX},{ys[-1]+70}"
svgA=f'''<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Alto">
<rect width="1440" height="900" fill="{SKY}"/>
{otter(tx,ty,k,SKY,'a')}
<path d="{wave} L1440,900 L0,900 Z" fill="{WATER}"/><path d="{wave}" fill="none" stroke="{WAVE}" stroke-width="3"/>
<text class="geo" x="{X-6}" y="290" font-size="132" font-weight="600" letter-spacing="-3" fill="{INK}">Alto</text>
<text class="geo" x="{X}" y="350" font-size="27" fill="{MUTED}">A browser harness that keeps you in the loop.</text>
<path d="{thread}" fill="none" stroke="{THREAD}" stroke-width="4" stroke-linecap="round"/>
{rows}{cursor(TX-1,ys[-1]+66,.9)}
<text class="geo" x="{X}" y="860" font-size="15" fill="{MUTED}">© 2026 Alto Computer</text>
<a href="https://x.com/altodotcomputer"><text class="geo" x="1320" y="860" font-size="15" text-anchor="end" fill="{INK}">@altodotcomputer</text></a>
</svg>'''
open(f'{OUT}/a-surface.html','w').write(page('Alto · Surface',f'linear-gradient({SKY} 50%,{WATER} 50%)',svgA))

# ---------- C. Nap: mascot first, thread reads left to right ----------
k=.32; tx=720-1205*k; ty=100-600*k
og,(px,py)=mirrored(tx,ty,k,SKY,'c')
wy=ty+1655*k
cx=[300,720,1140]; RY=716
thread=f"M{px},{py} C{px-10},{py+170} {cx[0]-120},{RY} {cx[0]-60},{RY} L{cx[2]+150},{RY}"
cs=''
for (n,a,b),x in zip(Q,cx):
    cs+=knot(x,RY,SKY)+f'<text class="geo" x="{x}" y="{RY+48}" text-anchor="middle" font-size="14" font-weight="500" letter-spacing="2.4" fill="{MUTED}">{n.upper()}</text>'
    cs+=f'<text class="ren" x="{x}" y="{RY+84}" text-anchor="middle" font-size="22" fill="{INK}">{a}</text><text class="ren" x="{x}" y="{RY+112}" text-anchor="middle" font-size="22" fill="{INK}">{b}</text>'
svgC=f'''<svg viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Alto">
<rect width="1440" height="900" fill="{SKY}"/>
<path d="M360,{wy} C500,{wy-12} 600,{wy+12} 720,{wy} S960,{wy-12} 1080,{wy}" fill="none" stroke="{WAVE}" stroke-width="3" stroke-linecap="round"/>
{og}
<text class="geo" x="720" y="{wy+92}" text-anchor="middle" font-size="92" font-weight="600" letter-spacing="-2" fill="{INK}">Alto</text>
<text class="geo" x="720" y="{wy+140}" text-anchor="middle" font-size="24" fill="{MUTED}">A browser harness that keeps you in the loop.</text>
<path d="{thread}" fill="none" stroke="{THREAD}" stroke-width="3.5" stroke-linecap="round"/>
{cs}{cursor(cx[2]+150,RY-8,.85)}
</svg>'''
open(f'{OUT}/c-nap.html','w').write(page('Alto · Nap',SKY,svgC))

# ---------- B. Note: plain prose, the thread is the underline ----------
note=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Alto · Note</title>{FONTS}<style>
:root{{--sky:{SKY};--ink:{INK};--muted:{MUTED};--thread:{THREAD}}}
html,body{{height:100%;margin:0}} body{{background:var(--sky);color:var(--ink);font-family:Jost,Futura,"Avenir Next",sans-serif;display:flex;flex-direction:column;overflow:hidden}}
.wrap{{flex:1;display:flex;flex-direction:column;padding:32px 36px}}
.otter{{width:92px;height:auto}}
main{{flex:1;display:flex;flex-direction:column;justify-content:center;max-width:780px;gap:22px}}
.lead{{font-size:clamp(26px,2.6vw,34px);font-weight:500;line-height:1.3;margin:0;letter-spacing:-.01em}}
.loop{{position:relative;white-space:nowrap}}
.loop svg{{position:absolute;left:-2%;bottom:-.42em;width:104%;height:.5em;overflow:visible}}
p{{font-size:clamp(19px,1.8vw,23px);line-height:1.45;margin:0;color:var(--ink)}}
.q{{font-family:"EB Garamond",Garamond,Georgia,serif;font-style:italic;font-size:clamp(22px,2vw,26px)}}
.k{{font-style:normal;font-family:Jost,sans-serif;font-size:.62em;letter-spacing:.16em;color:var(--muted);margin-right:.7em;vertical-align:.15em}}
footer{{display:flex;justify-content:space-between;font-size:15px;color:var(--muted)}} footer a{{color:var(--ink);text-decoration:none}}
</style></head><body><div class="wrap">
<img class="otter" src="../assets/otter.svg" alt="Clew the otter">
<main>
<p class="lead">Alto is a browser harness that <span class="loop">keeps you in the loop.<svg viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M2,12 C60,6 120,16 180,9 S260,7 298,11" fill="none" stroke="{THREAD}" stroke-width="5" stroke-linecap="round"/></svg></span></p>
<p>Agents can now browse for hours. The longer they go, the harder it is to know what they did. We are working on three questions.</p>
<p class="q"><span class="k">HARNESS</span>How can an agent browse for hours and still be trusted?</p>
<p class="q"><span class="k">INTERFACE</span>How do you talk with an agent that works for hours, and understand what it did?</p>
<p class="q"><span class="k">EVAL</span>How do you measure a good experience, not just a right answer?</p>
</main>
<footer><span>© 2026 Alto Computer</span><a href="https://x.com/altodotcomputer">@altodotcomputer</a></footer>
</div></body></html>'''
open(f'{OUT}/b-note.html','w').write(note)
if os.path.exists(f'{OUT}/b-loop.html'): os.remove(f'{OUT}/b-loop.html')
print('ok')
