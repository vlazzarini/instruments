from pylab import *
import ctcsound as csound

code = '''
sr = 44100
0dbfs = 1
isiz = 16384
gid = 0.1
gifn = ftgen(0,0,isiz,7,0,isiz*gid,1,isiz*(1-gid),0)
instr 1
 as  = diskin:a("flutec3.wav",p4/cpspch(9.00))
 kcps,kamp ptrack as,512
 knv = (0.5-gid) 
 amod = oscili(knv,kcps,gifn)
 asin = sin(2*$M_PI*amod)
 acos = cos(2*$M_PI*amod)
 ai,ar hilbert as
   out(asin*ai - acos*ar) 
endin
schedule(1,0,filelen("flutec3.wav"),440)
'''


N=16384
figure(figsize=(8,3))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sigs = zeros(7*sr)
n = 0
for i in range(0,int(len(sigs)/(cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1

win = zeros(N)+1 #hanning(N)
st = 44100
sig = sigs[st:st+N]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=1)
ylim(-60,1)
ylabel("amp", size=16)
xlabel("freq", size=16)
yticks([])
xticks(arange(3)*10000)
xlim(0,20000)
tight_layout()
show()
