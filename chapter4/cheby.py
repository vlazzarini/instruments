import pylab as pl
import numpy.polynomial.chebyshev as chb
def chebygen(amps):
  return lambda x: chb.chebval(x,amps)

sr = 44100.
fc = 500.
N = int(sr/(2*fc)) 
amps = pl.zeros(N)
for i in range(1,N):
   amps[i] = 1./i

t = pl.arange(0,sr)
w = 2*pl.pi*fc*t/sr

f = chebygen(amps)
scal = 1./abs(f(1.0))
s = scal*f(pl.cos(w))


pl.figure(figsize=(8,3))

sig = s
N = 32768
start = 0
x = pl.arange(0,N//2)
bins = x*sr/N
win = pl.hanning(N)
scal = N*pl.sqrt(pl.mean(win**2))
sig1 = sig[start:N+start]
window = pl.fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*pl.log10(mags/max(mags))


pl.plot(bins,spec[0:N//2], 'k-')
pl.ylim(-60, 1)
pl.ylabel("amp (dB)", size=16)
pl.xlabel("freq (Hz)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,10000)

pl.tight_layout()
pl.show()
