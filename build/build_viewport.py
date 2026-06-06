import json
img=json.load(open('/home/claude/imgs.json'))
HTML=r'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>bionicbutterfly — Lesson Viewport</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Spline+Sans+Mono:wght@400;500;600&family=Fraunces:opsz,wght@9..144,500;9..144,600&display=swap');
:root{--bg:#0a0e14;--panel:#0f1620;--panel2:#0c1320;--grid:#1a2330;--ink:#e6edf3;--dim:#7d8da3;
 --accent:#9b6dff;--tv:#4d9fff;--bm:#39ff88;--gex:#e5a73c;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:radial-gradient(ellipse at top,#11192480,var(--bg)),var(--bg);color:var(--ink);
 font-family:'Spline Sans Mono',monospace;min-height:100vh;padding:26px;}
.wrap{max-width:1180px;margin:0 auto;}
.brand{font-family:'Fraunces',serif;font-size:23px;font-weight:600;letter-spacing:-0.4px;}
.brand .o{color:var(--accent);}
.sub{font-size:11.5px;color:var(--dim);margin:3px 0 16px;}
.cuebar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px;align-items:center;}
.cuelbl{font-size:10px;letter-spacing:1.4px;text-transform:uppercase;color:var(--dim);margin-right:4px;}
.cue{font-family:inherit;font-size:11.5px;padding:7px 14px;border-radius:8px;cursor:pointer;transition:.15s;
 background:transparent;border:1px solid var(--grid);color:var(--dim);}
.cue:hover{border-color:var(--accent);color:var(--ink);}
.cue.on{background:var(--accent);border-color:var(--accent);color:#0a0512;font-weight:600;}
.viewport{position:relative;width:100%;height:min(66vh,640px);min-height:380px;
 border:1px solid var(--grid);border-radius:14px;background:var(--panel2);overflow:hidden;}
.pane{position:absolute;border:1px solid #243246;border-radius:10px;overflow:hidden;cursor:pointer;
 background:#05080d;transition:left .45s cubic-bezier(.4,0,.2,1),top .45s cubic-bezier(.4,0,.2,1),
 width .45s cubic-bezier(.4,0,.2,1),height .45s cubic-bezier(.4,0,.2,1),opacity .3s ease;}
.pane.drag{border-color:var(--bm);box-shadow:0 0 0 2px var(--bm) inset;}
.pane img.shot{width:100%;height:100%;object-fit:contain;display:block;background:#05080d;}
.pane .tag{position:absolute;top:9px;left:11px;font-size:10px;letter-spacing:1.4px;text-transform:uppercase;
 font-weight:600;z-index:3;background:#05080dcc;padding:2px 7px;border-radius:5px;}
.p-tv .tag{color:var(--tv);} .p-bm .tag{color:var(--bm);} .p-gex .tag{color:var(--gex);}
.pane .rep{position:absolute;top:8px;right:10px;z-index:4;background:#16202ecc;border:1px solid #2c3e54;
 color:var(--dim);font-family:inherit;font-size:10px;padding:4px 9px;border-radius:6px;cursor:pointer;transition:.15s;}
.pane .rep:hover{color:var(--ink);border-color:var(--accent);}
.pane .back{position:absolute;top:8px;right:10px;z-index:5;background:#16202e;border:1px solid #2c3e54;
 color:var(--ink);font-family:inherit;font-size:10.5px;padding:5px 11px;border-radius:7px;cursor:pointer;
 opacity:0;pointer-events:none;transition:.2s;}
.pane.full .back{opacity:1;pointer-events:auto;} .pane.full .rep{display:none;}
.cap{margin-top:12px;font-size:12px;color:#aab9cc;line-height:1.55;min-height:34px;}
.cap b{color:var(--ink);} .cap .k{color:var(--accent);font-weight:600;}
.note{margin-top:8px;font-size:10px;color:#5d6b80;line-height:1.5;}
</style></head>
<body><div class="wrap">
 <div class="brand"><span class="o">bionicbutterfly</span> · Lesson Viewport</div>
 <div class="sub">Same triptych for intake and playback — your charts stay where you put them. Drop / paste / replace to upload; click a pane or a lesson cue to bring it full-size.</div>
 <div class="cuebar">
  <span class="cuelbl">Lesson cue</span>
  <button class="cue on" data-go="overview">Overview</button>
  <button class="cue" data-go="tv">&ldquo;Look at the strat chart&hellip;&rdquo;</button>
  <button class="cue" data-go="bm">&ldquo;Now the Bookmap&hellip;&rdquo;</button>
  <button class="cue" data-go="gex">&ldquo;And the GEX&hellip;&rdquo;</button>
 </div>
 <div class="viewport" id="vp">
  <div class="pane p-tv" data-key="tv"><span class="tag">TradingView &middot; strat</span>
   <button class="rep" data-rep>&#8645; replace</button><button class="back" data-back>&larr; overview</button>
   <img class="shot" alt="TradingView chart" src="__TV__"><input type="file" accept="image/*" hidden></div>
  <div class="pane p-bm" data-key="bm"><span class="tag">Bookmap &middot; liquidity</span>
   <button class="rep" data-rep>&#8645; replace</button><button class="back" data-back>&larr; overview</button>
   <img class="shot" alt="Bookmap chart" src="__BM__"><input type="file" accept="image/*" hidden></div>
  <div class="pane p-gex" data-key="gex"><span class="tag">GEX &middot; gamma</span>
   <button class="rep" data-rep>&#8645; replace</button><button class="back" data-back>&larr; overview</button>
   <img class="shot" alt="GEX chart" src="__GEX__"><input type="file" accept="image/*" hidden></div>
 </div>
 <div class="cap" id="cap"></div>
 <div class="note">Real June 4 charts, embedded. The cue buttons stand in for the narration timeline; in production the same cue points drive both this expand/collapse and the in-chart highlight-and-fade. Charts here are display placeholders for whatever Suzy uploads to each pane.</div>
</div>
<script>
const REST={tv:[34,0,66,100],bm:[0,0,32,49],gex:[0,51,32,49]};
const CAPS={
 overview:'<b>Overview.</b> Your three charts at rest, exactly where you placed them. Home base between callouts \u2014 nothing to read yet.',
 tv:'<span class="k">\u201cLook at the strat chart\u2026\u201d</span> The TradingView read fills the screen so Suzy follows the 144, zones and DPMO without squinting.',
 bm:'<span class="k">\u201cNow the Bookmap\u2026\u201d</span> Bookmap full-size \u2014 is there a liquidity wall above/below acting as target or magnet? Coach asks what she sees.',
 gex:'<span class="k">\u201cAnd the GEX\u2026\u201d</span> GEX takes over \u2014 gamma walls / HVL as the pin or the level price ran to (Jun 4 exit sat on a GEX level).'};
const cap=document.getElementById('cap');
function setRect(p,r){p.style.left=r[0]+'%';p.style.top=r[1]+'%';p.style.width=r[2]+'%';p.style.height=r[3]+'%';}
function go(s){
 document.querySelectorAll('.cue').forEach(c=>c.classList.toggle('on',c.dataset.go===s));
 document.querySelectorAll('.pane').forEach(p=>{const k=p.dataset.key;
  if(s==='overview'){p.style.opacity=1;p.style.zIndex=1;p.classList.remove('full');setRect(p,REST[k]);}
  else if(k===s){p.style.opacity=1;p.style.zIndex=2;p.classList.add('full');setRect(p,[0,0,100,100]);}
  else{p.style.opacity=0;p.style.zIndex=0;p.classList.remove('full');setRect(p,REST[k]);}});
 cap.innerHTML=CAPS[s];}
document.querySelectorAll('.pane').forEach(p=>{
 const file=p.querySelector('input[type=file]'),imgEl=p.querySelector('img.shot');
 const load=f=>{const fr=new FileReader();fr.onload=()=>{const im=new Image();
   im.onload=()=>{let w=im.naturalWidth,h=im.naturalHeight;if(w<=1400){imgEl.src=fr.result;return;}
     const nh=Math.round(h*1400/w);const cv=document.createElement('canvas');cv.width=1400;cv.height=nh;
     cv.getContext('2d').drawImage(im,0,0,1400,nh);imgEl.src=cv.toDataURL('image/jpeg',0.82);};
   im.onerror=()=>imgEl.src=fr.result;im.src=fr.result;};fr.readAsDataURL(f);};
 p.addEventListener('click',e=>{if(e.target.hasAttribute('data-back')||e.target.hasAttribute('data-rep'))return;
   if(!p.classList.contains('full'))go(p.dataset.key);});
 p.querySelector('[data-rep]').addEventListener('click',e=>{e.stopPropagation();file.click();});
 p.querySelector('[data-back]').addEventListener('click',e=>{e.stopPropagation();go('overview');});
 file.addEventListener('change',e=>{if(e.target.files[0])load(e.target.files[0]);});
 p.addEventListener('dragover',e=>{e.preventDefault();p.classList.add('drag');});
 p.addEventListener('dragleave',()=>p.classList.remove('drag'));
 p.addEventListener('drop',e=>{e.preventDefault();p.classList.remove('drag');
   const f=[...e.dataTransfer.files].find(f=>f.type.startsWith('image/'));if(f)load(f);});
 p.addEventListener('mouseenter',()=>window._hov=p);
 p.querySelector('img.shot').onerror=function(){this.style.display='none';};
});
window.addEventListener('paste',e=>{const it=[...(e.clipboardData?.items||[])].find(i=>i.type.startsWith('image/'));
 if(!it||!window._hov)return;const f=it.getAsFile();if(f){const im=new Image();const fr=new FileReader();
 fr.onload=()=>{im.onload=()=>{let w=im.naturalWidth,h=im.naturalHeight;const t=window._hov.querySelector('img.shot');
   if(w<=1400){t.src=fr.result;return;}const nh=Math.round(h*1400/w);const cv=document.createElement('canvas');
   cv.width=1400;cv.height=nh;cv.getContext('2d').drawImage(im,0,0,1400,nh);t.src=cv.toDataURL('image/jpeg',0.82);};
   im.src=fr.result;};fr.readAsDataURL(f);}});
document.querySelectorAll('.cue').forEach(c=>c.addEventListener('click',()=>go(c.dataset.go)));
go('overview');
</script></body></html>'''
HTML=HTML.replace('__TV__',img['tv']).replace('__BM__',img['bm']).replace('__GEX__',img['gex'])
open('/mnt/user-data/outputs/lesson_viewport.html','w').write(HTML)
print('built lesson_viewport.html', len(HTML)//1024,'KB')
