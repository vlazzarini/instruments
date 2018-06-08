from pylab import *
import ctcsound as csound

code = '''
sr = 44100
0dbfs = 1
nchnls = 2
gifl faustcompile {{
import("music.lib");
fc = hslider("fc",0,0,20000,1);
fm = hslider("fm",0,0,20000,1);
Q = hslider("Q",2.5,0.1,20000,1);
I = hslider("I",0,0,20000,1);
f = fc + I*fm*osci(fm);
r = exp(-PI*(f/Q)/SR);
cost = cos(2*PI*f/SR);
b1 = (4*r*r/(1+r*r))*cost;
b2 = -r*r;
a = 1;//(1 - r*r)*sin(2*PI*f/SR);
process = _ + *(a) ~ (_ <: (*(b1) + b2*_')) ;
}}, "-vec -lv 1"

opcode FMReson,a,akkkk
setksmps 1
as,kfc,kfm,kn,kq xin
ay1,ay2 init 0,0
af = kfc + oscili(kn*kfm,kfm,-1,0.25);
ar = exp(-$M_PI*(af/kq)/sr);
acost = cos(2*$M_PI*af/sr);
ac1 = (4*ar*ar/(1+ar*ar))*acost;
ac2 = ar*ar;
ay = as + ay1*ac1 - ay2*ac2
ay2 = ay1
ay1 = ay
xout ay
endop

instr 1
 indx = p6
 irat = p7
 iQ = p8
 kndx = p6;linen p6,4,p3,3
 ain diskin2 "flutec3.wav",p5/cpspch(9.00)
 kcps,kamp ptrack ain,512
 ib, asig faustaudio gifl,ain
 faustctl ib,"fm",kcps/irat
 faustctl ib,"fc",kcps
 faustctl ib,"I",kndx
 faustctl ib,"Q",iQ
 ;asig FMReson ain,p5,p5/irat,kndx,iQ
 asig balance asig, ain
 aenv linen p4,0.1,p3,0.1
     outs(ain,asig*aenv)
endin

schedule(1,0,7,0dbfs/2,440,2,1/sqrt(2),2.5,2)
'''

N=32768
figure(figsize=(8,5))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sigs = zeros(7*sr*2)
n = 0
for i in range(0,int(len(sigs)/(4*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1

win = zeros(N)+1 #hanning(N)
subplot(2,1,1)
title('Original')
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
xlim(0,10000)


subplot(2,1,2)
title('Reson FM')
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
xticks(arange(3)*5000)
xlim(0,10000)
tight_layout()
show()
