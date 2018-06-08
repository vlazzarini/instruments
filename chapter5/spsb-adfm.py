from pylab import *
import ctcsound as csound

code = '''
sr = 44100
0dbfs = 1
nchnls=4
instr 1
 irt = p5
 as  = diskin:a("flutec3.wav",p4/cpspch(9.00))
 kcps,kamp ptrack as,512 
 anx = p6;linen(p6,4,p3,2)
 amod = oscili(anx/(2*$M_PI),kcps/irt)
 acos = tablei:a(amod,-1,1,0.25,1)
 asin = tablei:a(amod,-1,1,0,1)
 aae,abe hilbert acos
 aao,abo hilbert asin
 ac,ad hilbert as
 aeu = aae*ac - abe*ad
 aou = aao*ac - abo*ad
 ael = aae*ac + abe*ad
 aol = aao*ac + abo*ad
     out(aeu,aou,ael,aol)
endin    
schedule(1,0,filelen("flutec3.wav"),440,1,3) 
'''


N=16384
figure(figsize=(8,8))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sigs = zeros(7*sr*4)
n = 0
for i in range(0,int(len(sigs)/(4*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1

win = zeros(N)+1 #hanning(N)
subplot(4,1,1)
title('even,upper')
st = 44100
sig = sigs[st:st+4*N:4]
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

win = zeros(N)+1 #hanning(N)
subplot(4,1,2)
title('odd,upper')
st = 44100
sig = sigs[st+1:st+4*N:4]
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

win = zeros(N)+1 #hanning(N)
subplot(4,1,3)
title('even,lower')
st = 44100
sig = sigs[st+2:st+4*N:4]
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




subplot(4,1,4)
title('odd, lower')
sig = sigs[st+3:st+4*N+1:4]
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
