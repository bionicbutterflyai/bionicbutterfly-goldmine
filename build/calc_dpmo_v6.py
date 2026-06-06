import json

rows=[]
with open('/mnt/user-data/uploads/MNQ_06-26_060426_v2_Last.txt') as f:
    for line in f:
        line=line.strip()
        if not line: continue
        p=line.split(';')
        ts=p[0].split(' ')[1]; o,h,l,c,v=map(float,p[1:6])
        rows.append([ts,o,h,l,c,v])

n=len(rows)
close=[r[4] for r in rows]; vol=[r[5] for r in rows]

# --- calc_csf: alpha = 2/length (Pine custom smoother) ---
def csf_series(src, length):
    sm=2.0/length; out=[0.0]*len(src); prev=0.0
    for i,s in enumerate(src):
        prev=(s-prev)*sm+prev; out[i]=prev
    return out

# --- ta.ema: alpha = 2/(length+1), seed = first value ---
def ema_series(src, length):
    a=2.0/(length+1); out=[0.0]*len(src); prev=src[0]
    for i,s in enumerate(src):
        prev = a*s + (1-a)*prev if i>0 else s
        out[i]=prev
    return out

# i = close/close[1]*100 ; first bar -> close/close*100 = 100
iarr=[100.0]+[ (close[k]/close[k-1])*100.0 for k in range(1,n) ]
pmol2 = csf_series([x-100.0 for x in iarr], 20)      # length1 = 20
pmo   = csf_series([10.0*x for x in pmol2], 50)       # length2 = 50
pmols = ema_series(pmo, 7)                            # signal = 7
d     = [pmo[k]-pmols[k] for k in range(n)]

ema20 = ema_series(close, 20)
ema50 = ema_series(close, 50)

# 144 SMA
sma=[None]*n
for i in range(n):
    if i>=143: sma[i]=round(sum(close[i-143:i+1])/144,2)

# Pine ta.highest(volume,10) includes current bar
def highest10(i):
    lo=max(0,i-9); return max(vol[lo:i+1])

# bar state: vibrant if vol >= highest10 (and sign of d); else dull by sign of d
def barstate(i):
    hv = vol[i] >= highest10(i)
    if d[i] > 0:  return ('vbull' if hv else 'bull')
    if d[i] < 0:  return ('vbear' if hv else 'bear')
    return 'flat'

# build window (export UTC 14:18 -> 15:22). Export is CLOSE-stamped; TV is OPEN-stamped,
# so the bar's TV/open time = UTC - 4h - 1min. Relabel only; candle order/index unchanged.
def et_open(stamp):
    tot=(int(stamp[:2])-4)*60 + int(stamp[2:4]) - 1   # UTC->ET, then close->open (-1 min)
    return f'{(tot//60)%24:02d}:{tot%60:02d}'
out=[]
for i,r in enumerate(rows):
    hh=r[0][:2]; mm=r[0][2:4]; hhmm=hh+mm
    if '1418'<=hhmm<='1522':
        et=et_open(r[0])
        out.append({'et':et,'o':r[1],'h':r[2],'l':r[3],'c':r[4],'v':int(r[5]),
                    'sma':sma[i],'e20':round(ema20[i],2),'e50':round(ema50[i],2),
                    'pmo':round(pmo[i],4),'sig':round(pmols[i],4),'d':round(d[i],4),
                    'st':barstate(i)})

open('/home/claude/dpmo_win.json','w').write(json.dumps(out))
print('window bars',len(out))
# pmo range for oscillator pane scaling
pr=[b['pmo'] for b in out]+[b['sig'] for b in out]
print('pmo/sig range',round(min(pr),3),round(max(pr),3))
# debug table around the trade (ET 10:50 -> 11:05) for Mark to compare to TV
print('\nET     close      d       vol   hi10   state')
for b in out:
    if '10:50'<=b['et']<='11:05':
        i=[k for k,r in enumerate(rows) if et_open(r[0])==b['et']][0]
        print(f"{b['et']}  {b['c']:>8}  {b['d']:>7.3f}  {b['v']:>5}  {int(highest10(i)):>5}  {b['st']}")
