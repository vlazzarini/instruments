import pylab as pl

sr = 44100.
fc = 5000
fm = 500.

t = pl.arange(0,sr)
w = 2*pl.pi*fc*t/sr
o = 2*pl.pi*fm*t/sr
I = 3.5
s = 1
r = 1
scal = 1./(pl.exp(I))
sig = scal*pl.exp(I*r*pl.cos(o))*pl.cos(w + I*s*pl.sin(o))

pl.figure(figsize=(8,5))

pl.subplot(221)               
s = 0
r = 1
scal = 1./(pl.exp(I))
sig = scal*pl.exp(I*r*pl.cos(o))*pl.cos(w + I*s*pl.sin(o))
N = 32768
start = 0
x = pl.arange(0,N/2)
bins = x*sr/N
win = pl.hanning(N)
scal = N*pl.sqrt(pl.mean(win**2))
sig1 = sig[start:N+start]
window = pl.fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*pl.log10(mags/max(mags))
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.ylabel("amp (dB)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,10000)

pl.subplot(222)               
s = 1
r = 1
scal = 1./(pl.exp(I))
sig = scal*pl.exp(I*r*pl.cos(o))*pl.cos(w + I*s*pl.sin(o))
N = 32768
start = 0
x = pl.arange(0,N/2)
bins = x*sr/N
win = pl.hanning(N)
scal = N*pl.sqrt(pl.mean(win**2))
sig1 = sig[start:N+start]
window = pl.fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*pl.log10(mags/max(mags))
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.yticks()
pl.xticks()
pl.xlim(0,10000)

pl.subplot(223)               
s = 1
r = 0
scal = 1./(pl.exp(I))
sig = scal*pl.exp(I*r*pl.cos(o))*pl.cos(w + I*s*pl.sin(o))
N = 32768
start = 0
x = pl.arange(0,N/2)
bins = x*sr/N
win = pl.hanning(N)
scal = N*pl.sqrt(pl.mean(win**2))
sig1 = sig[start:N+start]
window = pl.fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*pl.log10(mags/max(mags))
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.ylabel("amp (dB)", size=16)
pl.xlabel("freq (Hz)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,10000)

pl.subplot(224)               
s = -1
r = 1
scal = 1./(pl.exp(I))
sig = scal*pl.exp(I*r*pl.cos(o))*pl.cos(w + I*s*pl.sin(o))
N = 32768
start = 0
x = pl.arange(0,N/2)
bins = x*sr/N
win = pl.hanning(N)
scal = N*pl.sqrt(pl.mean(win**2))
sig1 = sig[start:N+start]
window = pl.fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*pl.log10(mags/max(mags))
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.xlabel("freq (Hz)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,10000)



pl.tight_layout()
pl.show()
