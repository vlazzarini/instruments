from pylab import *
import ctcsound as csound

code = '''
sr = 44100
0dbfs = 1
nchnls = 2
instr 1
 irt = p5
 is = p7
 as  = diskin:a("flutec3.wav",p4/cpspch(9.00))
 kcps,kamp ptrack as,512 
 anx = p6; linen(p6,4,p3,2)
 adt = oscili(-is*anx/($M_PI*kcps),kcps/irt)
 adt = 0.5 + adt*0.5 + 1/kr
 adp = delayr:a(1) 
 adel = deltap3(adt) 
    delayw (as) 
 amod = oscili(anx,kcps/irt,-1,0.25)
       outch(p8,adel*exp(amod-anx)) 
endin
schedule(1,0,filelen("flutec3.wav"),440,1,3,-1,1)
schedule(1,0,filelen("flutec3.wav"),440,1,3,1,2)
'''


N=16384
figure(figsize=(8,5))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sigs = zeros(7*sr*2)
n = 0
for i in range(0,int(len(sigs)/(2*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1

win = zeros(N)+1 #hanning(N)
subplot(2,1,1)
title('lower sidebands')
st = 44100
sig = sigs[st:st+2*N:2]
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
yticks([])
xticks([])
xlim(0,20000)


subplot(2,1,2)
title('upper sidebands')
sig = sigs[st+1:st+2*N+1:2]
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
