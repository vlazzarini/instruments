import pylab as pl

sr = 44100.
fc = 500.

def mod1(x): return x - pl.floor(x)

t = pl.arange(0,sr)

def pd(x,d):
	if x < d:		return (0.5*x)/d
	else:			return (0.5)*(x-d)/(1-d) + 0.5
        
def phasor(ph,freq,sr):
    incr = freq/sr
    ph += incr
    return ph - pl.floor(ph)   

        
s = pl.zeros(sr)
ph = 0.0
for n in t:
   ph = phasor(ph,fc,sr)
   s[n] = pl.cos(2*pl.pi*pd(ph,0.9))


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
