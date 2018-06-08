from pylab import *
import ctcsound as csound

code = '''
sr = 40000
nchnls = 4
0dbfs=1
ksmps = 1
instr 1
 a1 init 1
 alp = butterbp(a1,2000,1000)
 ahp = butterbp(a1,6000,1000)
 abp = butterbp(a1,10000,1000)
 out(alp,ahp,abp,abp+ahp+alp)
 a1 = 0
endin
schedule(1,0,1)
'''



N=16384
figure(figsize=(8,8))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sigs = zeros(sr*4)
n = 0
for i in range(0,int(len(sigs)/(4*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1

win = zeros(N)+1 #hanning(N)
subplot(4,1,1)
title('cf=2kHz')
sig = sigs[0:4*N:4]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-60,5)
ylabel("amp", size=16)
yticks([])
xticks([])
plt.axvline(2000, color='k', linestyle='--')
xlim(0,20000)


subplot(4,1,2)
title('cf=4kHz')
sig = sigs[1:4*N+1:4]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-60,5)
ylabel("amp", size=16)
yticks([])
xticks([])
plt.axvline(6000, color='k', linestyle='--')
xlim(0,20000)

subplot(4,1,3)
title('cf=6kHz')
sig = sigs[2:4*N+2:4]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-60,5)
ylabel("amp ", size=16)
yticks([])
xticks([])
xlim(0,20000)
plt.axvline(10000, color='k', linestyle='--')


subplot(4,1,4)
title('parallel connection')
sig = sigs[3:4*N+3:4]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-60,5)
ylabel("amp ", size=16)
xlabel("freq (Hz)", size=16)
yticks([])
xticks(arange(3)*10000)
xlim(0,20000)
plt.axvline(2000, color='k', linestyle='--')
plt.axvline(6000, color='k', linestyle='--')
plt.axvline(10000, color='k', linestyle='--')
tight_layout()
show()
