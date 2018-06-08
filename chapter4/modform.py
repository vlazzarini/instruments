import pylab as pl

sr = 44100.
fc = 3000.
fm = 100.

t = pl.arange(0,sr)
w = 2*pl.pi*fc*t/sr
o = 2*pl.pi*fm*t/sr

bw = 1000
g = pl.exp(-fm/(.29*bw))
g2 = 2*pl.sqrt(g)/(1.-g)
I = g2*g2/2
scal = 1./pl.exp(I)
s = scal*pl.exp(I*pl.cos(o))*pl.cos(w)

pl.figure(figsize=(8,5))

pl.subplot(211)               
pl.plot(t[0:440]/sr,s[220:660], 'k-')
pl.xlabel("time (s)")

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

pl.subplot(212) 
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.ylabel("amp (dB)", size=16)
pl.xlabel("freq (Hz)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,sr/2)

pl.tight_layout()
pl.show()
