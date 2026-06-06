import json, datetime
F='/mnt/user-data/uploads/MNQ_06-26_June_Last.txt'
rows=[]
for line in open(F):
    line=line.strip()
    if not line: continue
    p=line.split(';'); d,t=p[0].split(' '); o,h,l,c,v=map(float,p[1:6])
    dt=datetime.datetime(int(d[:4]),int(d[4:6]),int(d[6:8]),int(t[:2]),int(t[2:4]))
    et=dt-datetime.timedelta(hours=4,minutes=1)
    rows.append((et,o,h,l,c,v))
D=lambda m,d,h,mi:datetime.datetime(2026,m,d,h,mi)
def HL(a,b):
    s=[r for r in rows if a<=r[0]<=b]; return (max(r[2] for r in s),min(r[3] for r in s)) if s else None
def closenear(target):
    s=[r for r in rows if r[0]<=target]; return round(s[-1][4],2) if s else None
def at_open(etstr):  # close price of the Jun-4 bar with this ET open-time
    hh,mm=map(int,etstr.split(':')); tgt=D(6,4,hh,mm)
    m=[r for r in rows if r[0]==tgt]; return round(m[0][4],2) if m else None
# window ET strings from the v6 dpmo window
win=json.loads(open('/home/claude/dpmo_win.json').read()); win_ets=[b['et'] for b in win]
def vwap_series(anchor):
    num=den=0;out={}
    for r in rows:
        if r[0]>=anchor and r[0]<=D(6,4,11,21):
            tp=(r[2]+r[3]+r[4])/3;num+=tp*r[5];den+=r[5]
            es=f'{r[0].hour:02d}:{r[0].minute:02d}'
            if r[0]>=D(6,4,10,17) and es in win_ets: out[es]=round(num/den,2)
    return out
lon=HL(D(6,4,3,0),D(6,4,3,29)); pm=HL(D(6,4,6,30),D(6,4,9,29))
yz=HL(D(6,4,9,0),D(6,4,9,29)); rz=HL(D(6,4,9,30),D(6,4,9,30)); ib=HL(D(6,4,9,30),D(6,4,10,29))
pd_rth=HL(D(6,3,9,30),D(6,3,15,59)); pd_eth=HL(D(6,2,18,0),D(6,3,17,0)); on=HL(D(6,3,18,0),D(6,4,9,29))
wib=HL(D(6,1,0,0),D(6,2,23,59)); hi4=round(max(r[2] for r in rows),2)
H=[
 {"label":"London H","price":round(lon[0],2),"color":"#2e8b6f","dash":"none"},
 {"label":"London L","price":round(lon[1],2),"color":"#2e8b6f","dash":"none"},
 {"label":"PreMkt H","price":round(pm[0],2),"color":"#4d9fff","dash":"none"},
 {"label":"PreMkt L","price":round(pm[1],2),"color":"#4d9fff","dash":"none"},
 {"label":"Yellow H","price":round(yz[0],2),"color":"#e5c12e","dash":"none"},
 {"label":"Yellow L","price":round(yz[1],2),"color":"#e5c12e","dash":"none"},
 {"label":"Red H","price":round(rz[0],2),"color":"#e5484d","dash":"none"},
 {"label":"Red L","price":round(rz[1],2),"color":"#e5484d","dash":"none"},
 {"label":"IB H","price":round(ib[0],2),"color":"#9b6dff","dash":"none"},
 {"label":"IB L","price":round(ib[1],2),"color":"#9b6dff","dash":"none"},
 {"label":"PD-RTH H","price":pd_rth[0],"color":"#d8dee6","dash":"6 4"},
 {"label":"PD-RTH L","price":pd_rth[1],"color":"#d8dee6","dash":"6 4"},
 {"label":"PD-ETH H","price":pd_eth[0],"color":"#d8dee6","dash":"none"},
 {"label":"PD-ETH L","price":pd_eth[1],"color":"#d8dee6","dash":"none"},
 {"label":"PD Close","price":closenear(D(6,3,16,0)),"color":"#39ff88","dash":"6 4"},
 {"label":"O/N H","price":round(on[0],2),"color":"#7d8da3","dash":"none"},
 {"label":"O/N L","price":round(on[1],2),"color":"#7d8da3","dash":"none"},
 {"label":"WklyIB H","price":round(wib[0],2),"color":"#9b6dff","dash":"7 5"},
 {"label":"WklyIB L","price":round(wib[1],2),"color":"#9b6dff","dash":"7 5"},
 {"label":"Q 9:23","price":at_open('09:23'),"color":"#39ff88","dash":"3 3"},
 {"label":"Q 10:53","price":at_open('10:53'),"color":"#39ff88","dash":"3 3"},
 {"label":"4d-Hi*","price":hi4,"color":"#e5a73c","dash":"2 4"},
]
levels={"hlines":[h for h in H if h["price"] is not None],
        "avwap":[{"et":k,"p":v} for k,v in sorted(vwap_series(D(6,4,9,30)).items())],
        "svwap":[{"et":k,"p":v} for k,v in sorted(vwap_series(D(6,3,18,0)).items())]}

# --- TICK-MERGE: collapse levels within ~4 ticks (MNQ tick=0.25 -> 1.0 pt) into one prominent line ---
TICK=0.25; MERGE_PTS=4*TICK   # 4 ticks = 1.0 pt
def merge(hl):
    hl=sorted(hl,key=lambda x:x["price"]); out=[]; i=0
    while i<len(hl):
        grp=[hl[i]]; j=i+1
        while j<len(hl) and hl[j]["price"]-grp[-1]["price"]<=MERGE_PTS:
            grp.append(hl[j]); j+=1
        if len(grp)==1: out.append(grp[0])
        else:
            ps=[g["price"] for g in grp]; lo,hi=min(ps),max(ps)
            label=" / ".join(g["label"] for g in grp)
            price_lbl=f"{lo:g}" if lo==hi else f"{lo:g}–{hi:g}"
            out.append({"label":label,"price":round(sum(ps)/len(ps),2),"price_lbl":price_lbl,
                        "color":grp[0]["color"],"dash":"none","merged":len(grp)})
        i=j
    return out
inview=[h for h in levels["hlines"] if 30248<=h["price"]<=30472]
offscreen=[h for h in levels["hlines"] if not (30248<=h["price"]<=30472)]
levels["hlines"]=merge(inview)+offscreen
open('/home/claude/levels.json','w').write(json.dumps(levels))
print("after merge:",len(levels['hlines']),"hlines (merged where within 4 ticks)")
