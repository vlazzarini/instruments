import pylab as pl

sr = 44100.
fc = 500.

t = pl.arange(0,sr)
w = 2*pl.pi*fc*t/sr

def f(x): return x*0.7 + 0.4*x**5 + 0.2*x**3 + 0.1*x**2 + 0.05*x**4
scal = 1./abs(f(0.5))
s = scal*f(0.5*pl.sin(w))


pl.figure(figsize=(8,3))

sig = s
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

pl.tight_layout()
pl.show()
