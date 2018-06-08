from pylab import *
import ctcsound as csound

code = '''
sr = 40000
nchnls = 2
0dbfs=1
ksmps = 1

opcode Tone,a,ak
setksmps 1
ay init 0
ax,kf xin
kt = 2 - cos(2*$M_PI*kf/sr)
kb = sqrt(kt^2 - 1) - kt
ka = 1 + kb
ay = ax*ka - ay*kb
   xout ay
endop

opcode Atone,a,ak
setksmps 1
ay init 0
ax,kf xin
kt = 2 + cos(2*$M_PI*kf/sr)
kb = kt - sqrt(kt^2 - 1) 
ka = 1 - kb
ay = ax*ka - ay*kb
   xout ay
endop

instr 1
 a1 init 1
 alp = Tone(a1,5000)
 ahp = Atone(a1,15000)
 out(alp,ahp)
 a1 = 0
endin
schedule(1,0,1)
'''



N=16384
figure(figsize=(8,4))
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
title('low pass')
sig = sigs[0:nchnls*N:nchnls]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-12,5)
ylabel("amp", size=16)
yticks([])
xticks([])
plt.axvline(5000, color='k', linestyle='--')
xlim(0,20000)


subplot(nchnls,1,2)
title('high pass')
sig = sigs[1:nchnls*N+1:nchnls]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-12,5)
ylabel("amp ", size=16)
xlabel("freq (Hz)", size=16)
yticks([])
xticks(arange(3)*10000)
xlim(0,20000)
plt.axvline(15000, color='k', linestyle='--')

tight_layout()
show()
