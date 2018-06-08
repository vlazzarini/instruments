from pylab import *
import ctcsound as csound

code = '''
nchnls=4
instr 1
 indx = p6/(2*$M_PI)
 ifc = p5
 ifm = p5/p7
 irs = p8

 anv = 1;linen(1,irs,p3,0.1)
 afm = oscili(indx*anv,ifm)
 aph = phasor(ifc)
 acr = tablei:a(aph+afm,-1,
			1,0.25,1)
	outch(p9,anv*p4*acr)
endin
schedule(1,0,1,0dbfs/2,50,10,1.414,0.01,1)
schedule(1,0,1,0dbfs/2,cpspch(6.04),4,1.005,0.01,2)
schedule(1,0,1,0dbfs/2,cpspch(7.11),5,1.002/2,0.01,3)
schedule(1,0,1,0dbfs/2,cpspch(7.11),7,1.001,0.01,4)  
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
title('drum')
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
xticks(arange(4)*500)
xlim(0,2500)


subplot(nchnls,1,2)
title('bass')
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
xticks(arange(4)*500)
xlim(0,2500)

subplot(nchnls,1,3)
title('reeds')
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
xticks(arange(4)*2000)
xlim(0,8000)

subplot(nchnls,1,4)
title('brass')
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
xticks(arange(4)*2000)
xlim(0,8000)

tight_layout()
show()
