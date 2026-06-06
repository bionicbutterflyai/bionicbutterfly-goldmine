import json
bars=json.loads(open('/home/claude/dpmo_win.json').read())
bars_js=json.dumps(bars)
levels_js=open('/home/claude/levels.json').read()

ENTRY=30350.0; EXIT=30451.0; SL=ENTRY-10.0
PTS=round(EXIT-ENTRY,1); RR=round(PTS/10.0,1); PNL_MAX=PTS*2.0
CAP=40.0; MICROS=5; CAP_USD=CAP*2.0*MICROS
sp=[b['sma'] for b in bars if b['et'] in ('10:56','10:57','10:58') and b['sma']]
SPINE=round(sum(sp)/len(sp),2); ABOVE=round(ENTRY-SPINE,1)

html=f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>bionicbutterfly — DPMO Trade Lesson (June 4)</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Spline+Sans+Mono:wght@400;500;600&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap');
:root{{--bg:#0a0e14;--panel:#0f1620;--grid:#1a2330;--ink:#e6edf3;--dim:#7d8da3;--spine:#4d9fff;
--alert:#d4a017;--pull:#9b6dff;--accent:#9b6dff;--warn:#e5a73c;
--dbull:#2e8b6f;--vbull:#39ff88;--dbear:#b04449;--vbear:#ff4db8;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:radial-gradient(ellipse at top,#11192480,var(--bg)),var(--bg);color:var(--ink);
font-family:'Spline Sans Mono',monospace;padding:28px;min-height:100vh;}}
.wrap{{max-width:1060px;margin:0 auto;}}
.provbar{{background:#0c1622;border:1px solid #1f3347;border-left:3px solid var(--spine);border-radius:8px;
padding:9px 14px;font-size:11.5px;line-height:1.55;color:#bcd2e6;margin-bottom:14px;}}
.provbar b{{color:var(--spine);}}
.head{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px;flex-wrap:wrap;gap:8px;}}
.title{{font-family:'Fraunces',serif;font-size:26px;font-weight:600;letter-spacing:-0.5px;}} .title .o{{color:var(--accent);}}
.meta{{font-size:12px;color:var(--dim);}}
.verdict-bar{{display:flex;gap:10px;margin:16px 0;flex-wrap:wrap;}}
.leg{{flex:1;min-width:120px;background:var(--panel);border:1px solid var(--grid);border-radius:10px;padding:12px 14px;}}
.leg .k{{font-size:10px;letter-spacing:1.2px;color:var(--dim);text-transform:uppercase;}}
.leg .v{{font-size:14px;font-weight:600;margin-top:4px;}} .leg .s{{font-size:9.5px;color:var(--dim);margin-top:3px;}}
.leg.miss .v{{color:var(--warn);}} .leg.gate .v{{color:var(--vbull);}} .leg.bias .v{{color:var(--vbull);}}
.leg.max .v{{color:var(--accent);}} .leg.cap .v{{color:var(--vbull);}}
.chartcard{{background:var(--panel);border:1px solid var(--grid);border-radius:14px;padding:18px;overflow:hidden;}}
svg{{width:100%;height:auto;display:block;}}
.legend{{display:flex;gap:13px;margin-top:14px;flex-wrap:wrap;font-size:10.5px;}}
.legend span{{display:flex;align-items:center;gap:6px;color:var(--dim);}}
.sw{{width:11px;height:11px;border-radius:2px;display:inline-block;}} .dot{{width:10px;height:10px;border-radius:50%;display:inline-block;}}
.line-key{{width:15px;height:0;border-top:2px dashed;display:inline-block;}}
.lesson{{margin-top:18px;background:linear-gradient(135deg,#14101e,var(--panel));border:1px solid #2a2140;
border-left:3px solid var(--accent);border-radius:10px;padding:18px 20px;}}
.lesson .who{{font-size:11px;letter-spacing:2px;color:var(--accent);text-transform:uppercase;margin-bottom:8px;}}
.lesson p{{font-size:14px;line-height:1.65;margin-bottom:10px;}} .lesson .hl{{color:var(--spine);font-weight:600;}}
.lesson em{{color:var(--vbull);font-style:normal;}} .lesson .vib{{color:var(--vbull);font-weight:600;}}
.gapnote{{margin-top:14px;background:#1a140a;border:1px solid #3a2e15;border-left:3px solid var(--warn);
border-radius:8px;padding:12px 16px;font-size:12.5px;line-height:1.6;color:#e8d9b8;}} .gapnote b{{color:var(--warn);}}
.math{{margin-top:14px;font-size:11px;color:var(--dim);line-height:1.7;border-top:1px solid var(--grid);padding-top:12px;}}
.math code{{color:var(--ink);}} .math b{{color:var(--ink);}}
.fade{{animation:rise .7s ease both;}} @keyframes rise{{from{{opacity:0;transform:translateY(8px);}}to{{opacity:1;transform:none;}}}}
.lvls .lv{{transition:opacity .25s ease;}}
.lvls:hover .lv{{opacity:.12;}}
.lvls .lv:hover{{opacity:1;}}
</style></head><body><div class="wrap">
<div class="provbar fade"><b>KITCHEN SINK v2 — ALL STRAT LEVELS ON (now with multi-day data).</b> Same June 4 trade &amp; v6 DPMO candles, with the full computable strat layered on: London / Pre-Market / Yellow / Red / IB / Weekly-IB, Prev-Day H/L &amp; Close, Overnight H/L, Anchored + Session VWAP, Quarterly 9:23 &amp; 10:53. Off-screen levels are edge-tagged (most prior-day structure sits ABOVE — June 4 traded in a lower value area). <b>Only proxy:</b> "4d-Hi*" = 4-day high, not true ATH (needs full history). This is the case FOR fill-on-relevance.</div>
<div class="head fade"><div class="title"><span class="o">bionicbutterfly</span> · DPMO Trade Lesson</div>
<div class="meta">MNQ 06-26 · JUN 4 2026 · LONG · 1-MIN · ET</div></div>
<div class="verdict-bar fade">
<div class="leg miss"><div class="k">Behavior (engine)</div><div class="v">⚠ no fresh break</div><div class="s">false neg vs gate</div></div>
<div class="leg gate"><div class="k">3-green gate</div><div class="v">✓ aligned 10:57</div><div class="s">candle+cloud+DPMO</div></div>
<div class="leg bias"><div class="k">Bias</div><div class="v">✓ bullish</div></div>
<div class="leg max"><div class="k">Move available</div><div class="v">+{PTS:.0f} pts</div><div class="s">{RR}R · ${PNL_MAX:.0f}/contract</div></div>
<div class="leg cap"><div class="k">Realistic capture</div><div class="v">~+{CAP:.0f} pts</div><div class="s">{MICROS} micros · ~${CAP_USD:.0f} (illus.)</div></div>
</div>
<div class="chartcard fade"><svg id="chart" viewBox="0 0 1000 602" preserveAspectRatio="xMidYMid meet"></svg>
<div class="legend">
<span><i class="sw" style="background:var(--dbull)"></i> DPMO bull</span>
<span><i class="sw" style="background:var(--vbull)"></i> bull + high-vol</span>
<span><i class="sw" style="background:var(--dbear)"></i> DPMO bear</span>
<span><i class="sw" style="background:var(--vbear)"></i> bear + high-vol</span>
<span><i class="line-key" style="border-color:var(--spine)"></i> 144</span>
<span><i class="dot" style="background:var(--alert)"></i> Alert</span>
<span><i class="dot" style="background:var(--pull)"></i> Pullback</span>
<span><i class="line-key" style="border-color:#e5484d"></i> Exit (GEX) / Stop</span>
</div></div>
<div class="lesson fade"><div class="who">From the data</div>
<p id="lessonText"></p><div class="gapnote" id="gapNote"></div><div class="math" id="mathNote"></div></div>
</div>
<script>
const bars={bars_js};
const ENTRY={ENTRY},EXIT={EXIT},SL={SL};
const COL={{bull:'#2e8b6f',vbull:'#39ff88',bear:'#b04449',vbear:'#ff4db8',flat:'#48566a'}};
const W=1000,H=580,padL=8,padR=80,gut=120;
// price pane
const pT=22,pB=372; const oT=410,oB=560;   // oscillator pane
const plotW=W-padL-padR-gut;
const idxOf=et=>bars.findIndex(b=>b.et===et);
const svg=document.getElementById('chart'),NS='http://www.w3.org/2000/svg';
const el=(t,a)=>{{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);return e;}};
const txt=(x,y,s,a={{}})=>{{const t=el('text',Object.assign({{x,y,'font-family':'Spline Sans Mono'}},a));t.textContent=s;svg.appendChild(t);return t;}};
const x=i=>padL+(i+0.5)/bars.length*plotW;
const cw=Math.max(2,plotW/bars.length*0.58);
// price scale
const pr=bars.flatMap(b=>[b.h,b.l]).concat([SL,EXIT]);
const pMin=Math.min(...pr)-5,pMax=Math.max(...pr)+5;
const y=p=>pT+(pMax-p)/(pMax-pMin)*(pB-pT);
// gridlines
for(let g=Math.ceil(pMin/25)*25;g<pMax;g+=25){{svg.appendChild(el('line',{{x1:padL,y1:y(g),x2:padL+plotW,y2:y(g),stroke:'#1a2330','stroke-width':1}}));txt(W-padR+6,y(g)+4,g,{{fill:'#5a6b80','font-size':11}});}}
// EMA 20/50 cloud — FILL ONLY, no outlines (matches the DPMO pane's fill-only style)
for(let i=0;i<bars.length-1;i++){{const a=bars[i],b=bars[i+1];const up=((a.e20-a.e50)+(b.e20-b.e50))/2>=0;
 const poly=`${{x(i)}},${{y(a.e20)}} ${{x(i+1)}},${{y(b.e20)}} ${{x(i+1)}},${{y(b.e50)}} ${{x(i)}},${{y(a.e50)}}`;
 svg.appendChild(el('polygon',{{points:poly,fill:up?'#2ecc8f':'#e5484d','fill-opacity':0.18,stroke:'none'}}));}}
txt(x(bars.length-1)-2,y(bars[bars.length-1].e20)-4,'20/50',{{fill:'#7d8da3','font-size':9,'text-anchor':'end'}});
// exit/stop zones
const ix=x(idxOf('10:56'));
svg.appendChild(el('rect',{{x:ix,y:y(EXIT),width:padL+plotW-ix,height:y(ENTRY)-y(EXIT),fill:'#2ecc8f','fill-opacity':0.05}}));
svg.appendChild(el('rect',{{x:ix,y:y(ENTRY),width:padL+plotW-ix,height:y(SL)-y(ENTRY),fill:'#e5484d','fill-opacity':0.07}}));
svg.appendChild(el('line',{{x1:ix,y1:y(EXIT),x2:padL+plotW,y2:y(EXIT),stroke:'#e5484d','stroke-width':1.4,'stroke-dasharray':'2 2'}}));
txt(padL+plotW+8,y(EXIT)+3,'EXIT '+EXIT+' · GEX',{{fill:'#e5484d','font-size':9.5,'font-weight':600}});
svg.appendChild(el('line',{{x1:ix,y1:y(SL),x2:padL+plotW,y2:y(SL),stroke:'#e5484d','stroke-width':1.1,'stroke-dasharray':'5 4'}}));
txt(padL+plotW+8,y(SL)+12,'SL '+SL+' (40t)',{{fill:'#e5484d','font-size':9.5}});
// 144 spine
let ds='';bars.forEach((b,i)=>{{if(b.sma)ds+=(ds?'L':'M')+x(i)+','+y(b.sma)+' ';}});
svg.appendChild(el('path',{{d:ds,fill:'none',stroke:'#4d9fff','stroke-width':2.4,'stroke-dasharray':'7 4'}}));

// ===== KITCHEN-SINK: all strat levels layered on (drawn under candles) =====
const LV={levels_js};
(function(){{
 const gx=padL+plotW+8;               // gutter label x (left-anchored, in the black free space)
 const inView=p=>p>=pMin&&p<=pMax;
 const lvls=el('g',{{'class':'lvls'}}); svg.appendChild(lvls);
 const grp=()=>{{const g=el('g',{{'class':'lv'}});lvls.appendChild(g);return g;}};
 const gtxt=(g,xx,yy,s,a)=>{{const e=el('text',Object.assign({{x:xx,y:yy,'font-family':'Spline Sans Mono'}},a));e.textContent=s;g.appendChild(e);return e;}};
 LV.hlines.forEach(h=>{{
  const g=grp();
  if(inView(h.price)){{
   const wt=h.merged?2.0:1.1, op=h.merged?0.95:0.8, plbl=h.price_lbl||h.price;
   g.appendChild(el('line',{{x1:padL,y1:y(h.price),x2:padL+plotW,y2:y(h.price),stroke:h.color,'stroke-width':wt,'stroke-opacity':op,'stroke-dasharray':h.merged?'none':h.dash}}));
   g.appendChild(el('line',{{x1:padL,y1:y(h.price),x2:padL+plotW,y2:y(h.price),stroke:'transparent','stroke-width':10}})); // hover hit-area
   gtxt(g,gx,y(h.price)+3,h.label+' '+plbl,{{fill:h.color,'font-size':8.5,'font-weight':600}});
  }} else {{
   const top=h.price>pMax; const ey=top?pT+10:pB-4;
   gtxt(g,padL+4,ey,(top?'↑ ':'↓ ')+h.label+' '+h.price+(top?' (above)':' (below)'),{{fill:h.color,'font-size':8,'font-weight':600}});
  }}
 }});
 // Anchored VWAP (from 9:30) — weight matched to the 144
 {{const g=grp();let av='';LV.avwap.forEach(a=>{{const i=idxOf(a.et);if(i>=0)av+=(av?'L':'M')+x(i)+','+y(a.p)+' ';}});
  g.appendChild(el('path',{{d:av,fill:'none',stroke:'#ff4db8','stroke-width':2.4,'stroke-dasharray':'4 3','stroke-opacity':0.95}}));
  }}
 // Session VWAP (anchored 6pm prior day) — weight matched to the 144
 if(LV.svwap){{const g=grp();let sv='';LV.svwap.forEach(a=>{{const i=idxOf(a.et);if(i>=0)sv+=(sv?'L':'M')+x(i)+','+y(a.p)+' ';}});
  g.appendChild(el('path',{{d:sv,fill:'none',stroke:'#d8dee6','stroke-width':2.4,'stroke-dasharray':'5 4','stroke-opacity':0.9}}));
  }}
}})();
// candles — coloured by DPMO state
bars.forEach((b,i)=>{{const col=COL[b.st]||COL.flat;
 svg.appendChild(el('line',{{x1:x(i),y1:y(b.h),x2:x(i),y2:y(b.l),stroke:col,'stroke-width':1}}));
 const yo=y(b.o),yc=y(b.c);
 svg.appendChild(el('rect',{{x:x(i)-cw/2,y:Math.min(yo,yc),width:cw,height:Math.max(1.5,Math.abs(yc-yo)),fill:col,rx:0.5}}));
}});
// above-144 bracket far-left
(function(){{const i=idxOf('10:56'),px=x(i),yTop=y(ENTRY),yBot=y(bars[i].sma),bx=padL+8;
 svg.appendChild(el('line',{{x1:bx,y1:yTop,x2:bx,y2:yBot,stroke:'#e5a73c','stroke-width':1.2,'stroke-dasharray':'3 3'}}));
 svg.appendChild(el('line',{{x1:bx,y1:yTop,x2:bx+6,y2:yTop,stroke:'#e5a73c','stroke-width':1.2}}));
 svg.appendChild(el('line',{{x1:bx,y1:yBot,x2:bx+6,y2:yBot,stroke:'#e5a73c','stroke-width':1.2}}));
 txt(bx+10,(yTop+yBot)/2-2,'{ABOVE:.0f} pts',{{fill:'#e5a73c','font-size':10,'font-weight':600}});
 txt(bx+10,(yTop+yBot)/2+10,'above 144',{{fill:'#e5a73c','font-size':8.5}});}})();
// markers
function mk(et,price,color,dir,label){{const i=idxOf(et);if(i<0)return;const px=x(i),py=y(price);
 const ay=dir==='down'?py-26:py+26;
 svg.appendChild(el('line',{{x1:px,y1:ay,x2:px,y2:dir==='down'?py-6:py+6,stroke:color,'stroke-width':2}}));
 svg.appendChild(el('circle',{{cx:px,cy:py,r:3.5,fill:color,stroke:'#0f1620','stroke-width':1.5}}));
 const ly=dir==='down'?ay-4:ay+13;txt(px,ly,label,{{fill:color,'font-size':10,'font-weight':600,'text-anchor':'middle'}});
 txt(px,ly+11,et,{{fill:'#7d8da3','font-size':8.5,'text-anchor':'middle'}});}}
mk('10:23',bars[idxOf('10:23')].l,'#d4a017','down','ALERT');
mk('10:48',bars[idxOf('10:48')].l,'#9b6dff','down','PULLBACK');
mk('10:57',ENTRY,'#39ff88','down','ENTRY');
mk('11:14',EXIT,'#e5484d','up','EXIT');
// ---- oscillator pane ----
svg.appendChild(el('line',{{x1:padL,y1:oT-8,x2:padL+plotW,y2:oT-8,stroke:'#1a2330','stroke-width':1}}));
txt(padL,oT-12,'DPMO 20/50/7  (cloud = pmo − signal)',{{fill:'#7d8da3','font-size':9.5}});
const dv=bars.flatMap(b=>[b.pmo,b.sig]);const dMin=Math.min(...dv),dMax=Math.max(...dv);const pad=(dMax-dMin)*0.15||0.01;
const oy=v=>oT+(dMax+pad-v)/((dMax+pad)-(dMin-pad))*(oB-oT);
// zero line
svg.appendChild(el('line',{{x1:padL,y1:oy(0),x2:padL+plotW,y2:oy(0),stroke:'#ffffff','stroke-opacity':0.5,'stroke-width':1,'stroke-dasharray':'2 3'}}));
txt(W-padR+6,oy(0)+4,'0',{{fill:'#8a9bb0','font-size':9}});
// cloud fill pmo vs sig, coloured by sign(d) — fill only, vibrant, NO lines (matches Mark's TV: cloud+zero only)
for(let i=0;i<bars.length-1;i++){{const a=bars[i],b=bars[i+1];const up=(a.d+b.d)/2>=0;
 const poly=`${{x(i)}},${{oy(a.pmo)}} ${{x(i+1)}},${{oy(b.pmo)}} ${{x(i+1)}},${{oy(b.sig)}} ${{x(i)}},${{oy(a.sig)}}`;
 svg.appendChild(el('polygon',{{points:poly,fill:up?'#2ecc8f':'#e5484d','fill-opacity':0.9,stroke:'none'}}));}}
// mark the cross at entry on oscillator
const cx=x(idxOf('10:57'));svg.appendChild(el('line',{{x1:cx,y1:oT,x2:cx,y2:oB,stroke:'#39ff88','stroke-width':1,'stroke-dasharray':'2 3','stroke-opacity':0.7}}));
txt(cx+3,oB-4,'cloud→green 10:57',{{fill:'#39ff88','font-size':8.5}});
// time axis along the bottom (like TV) — every 6th bar
bars.forEach((b,i)=>{{ if(i%6===0 || i===bars.length-1){{
 svg.appendChild(el('line',{{x1:x(i),y1:oB+3,x2:x(i),y2:oB+7,stroke:'#3a4658','stroke-width':1}}));
 txt(x(i),oB+18,b.et,{{fill:'#7d8da3','font-size':9,'text-anchor':'middle'}});
}} }});

document.getElementById('lessonText').innerHTML=
 `Morning sold to ~30152, then the reclaim set up. <span class="hl">Alert</span> ~10:23 as price held back over the 144; <span class="hl">pullback</span> into ~30287 by 10:48; then the gate completed — <em>candle, the 20/50 cloud, and the DPMO cloud all green</em>. `+
 `Watch the lower pane: the DPMO cloud flips <em>green at 10:57</em>, and one minute later the <span class="vib">11:00 bar prints vibrant green on ~11.8k volume</span> (your high-volume tell). Price ran to the heavy <em>GEX level at 30451</em>, where you exited ahead of the rollover — <em>+101 points</em> available.`;
document.getElementById('gapNote').innerHTML=
 `<b>⚠ Engine flag (false negative):</b> the deterministic engine reports <b>no fresh 144 break</b> before entry (~{ABOVE:.0f} pts above the spine) and marks the behaviour leg missing — but that's a <b>false negative</b> vs the 3-green gate, which credits the patience that placed the entry at the real breakout, not a fresh-break chase. A cue to teach the engine.`;
document.getElementById('mathNote').innerHTML=
 `<b>Reconciliation</b> — entry <code>{ENTRY:.0f}</code> → exit <code>{EXIT:.0f}</code> = <code>+{PTS:.0f} pts</code>; stop <code>{SL:.0f}</code> = <code>10 pts</code> → max <code>{RR}R</code>; MNQ <code>$2/pt</code> → <code>${PNL_MAX:.0f}/contract</code> max. `+
 `<b>Move ≠ bank:</b> {MICROS} micros, scale + scratch to B/E + re-enter + trail → ~<code>{CAP:.0f} pts</code> captured (~70% of an avg ~75-pt move) ≈ <code>${CAP_USD:.0f}</code>. Honest number is the smaller one.`;
</script></body></html>"""
open('/home/claude/trade_lesson_june4_kitchensink.html','w').write(html)
print("wrote v4. spine",SPINE,"above",ABOVE)
