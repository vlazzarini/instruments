import pylab as pl

sr = 44100.
f1 = 3000
f2 = 200.
N = int((sr/2 - f1)/f2)

t = pl.arange(0,sr)
w = 2*pl.pi*f1*t/sr
o = 2*pl.pi*f2*t/sr
a = 0.4
if a > 10**(-3./N):
    a = 10**(-3./N)
    
sinw = pl.sin(w)
den = 1.- 2*a*pl.cos(o) + a*a
scal = pl.sqrt((1.-a*a)/(1+a*a))
s = scal*(1-a*a)*sinw/den 
    
pl.figure(figsize=(8,5))

pl.subplot(211)               
pl.plot(t[0:440]/sr,s[0:440]/max(abs(s)), 'k-')
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
pl.ylim(-90, 0)
pl.ylabel("amp (dB)", size=16)
pl.xlabel("freq (Hz)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,sr/2)

pl.tight_layout()
pl.show()

