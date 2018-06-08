from pylab import *
import ctcsound as csound

code = '''
nchnls=4
instr 1
 iamp = p4
 ifo = p5
 ifc = p6
 ia2 = (1-p7)
 iatt = p8
 
 kfc  = ifc;// expseg(ifc,iatt,ifc*2,p3-iatt,ifc)
 iN = int(8*ifc/(2*ifo)) - 1
 ia =  10^(-3/iN)
 ka = ia
 kasq = ka*ka
 iasq2 = ia2*ia2
 
 aph  = phasor(ifo)
 asw  = tablei:a(aph,-1,1,0,1)
 aco  = tablei:a(aph,-1,1,0.25,1)
 asb = asw/(1 - 2*ka*aco + kasq)

 kfr  = kfc/ifo
 kfn  = int(kfr)
 kam  = kfr - kfn

 asw1 = tablei:a(aph*kfn,-1,1,0,1)
 asw2 = tablei:a(aph*(kfn+1),-1,1,0,1)
 aden = (1 - 2*ia2*aco + iasq2)
 adb1 = (1-iasq2)*asw1/aden
 adb2 = (1-iasq2)*asw2/aden
 adb =  (1-kam)*adb1 + kam*adb2

 ksc1 = sqrt(1-kasq)
 isc2 = sqrt((1-iasq2)/(1+iasq2))
 amix = (1-p7)*asb/ksc1 + p7*adb/isc2
 asig = linenr(amix*iamp/4,iatt,0.1,0.01)

     outch(p9,asig)
     
endin

schedule(1,0,2,0dbfs/10,200,3000,0.9,0.1,1)
schedule(1,0,2,0dbfs/10,200,3000,0.7,0.1,2)
schedule(1,0,2,0dbfs/10,200,3000,0.4,0.1,3)
schedule(1,0,2,0dbfs/10,200,3000,0.1,0.1,4)
'''

N=32768
figure(figsize=(8,8))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
nchnls = cs.nchnls()
sr = cs.sr()
sigs = zeros(sr*nchnls)
n = 0
for i in range(0,int(len(sigs)/(nchnls*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1

win = zeros(N)+1 #hanning(N)
subplot(nchnls,1,1)
title('res = 0.9')
sig = sigs[0:nchnls*N:nchnls]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-')
ylim(-40,5)
ylabel("amp", size=16)
yticks([])
xticks(arange(4)*5000)
xlim(0,15000)


subplot(nchnls,1,2)
title('res = 0.7')
sig = sigs[1:nchnls*N+1:nchnls]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-')
ylim(-40,5)
ylabel("amp", size=16)
yticks([])
xticks(arange(4)*5000)
xlim(0,15000)

subplot(nchnls,1,3)
title('res = 0.4')
sig = sigs[2:nchnls*N+2:nchnls]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-')
ylim(-40,5)
ylabel("amp ", size=16)
yticks([])
xticks(arange(4)*5000)
xlim(0,15000)

subplot(nchnls,1,4)
title('res = 0.1')
sig = sigs[3:nchnls*N+3:nchnls]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-')
ylim(-40,5)
ylabel("amp ", size=16)
xlabel("freq (Hz)", size=16)
yticks([])
xticks(arange(4)*5000)
xlim(0,15000)

tight_layout()
show()
