import pylab as pl

sr = 44100.
f1 = 3000
f2 = 2000.
N = 3#int((sr/2 - f1)/f2)

t = pl.arange(0,sr)
s = pl.zeros(sr)
w = 2*pl.pi*f1*t/sr
o = 2*pl.pi*f2*t/sr
a = 0.5
        
sinw = pl.sin(w)
sinwmo = pl.sin((w-o))
sinwn1o = pl.sin((w+(N+1)*o))
sinwno =  pl.sin((w+N*o))
den = 1.- 2*a*pl.cos(o) + a*a
scal = pl.sqrt((1.-a*a)/(1. - a**(2.*N+2)))
s = scal*(sinw - a*sinwmo - a**(N+1)*(sinwn1o - a*sinwno))/den 
    
    
pl.figure(figsize=(8,5))

pl.subplot(211)               
pl.plot(t[0:440]/sr,s[0:440], 'k-')
pl.ylim(-1.1,1.1)
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
