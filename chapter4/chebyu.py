import pylab as pl
import scipy.special as sp

def chebygen(amps):
  N = 40000
  p = pl.arange(-N,N+1)
  c = pl.zeros(len(p))
  n = 0
  for i in amps:
      c += sp.eval_chebyu(n-1,p/N)*i
      n += 1  
  return pl.vectorize(lambda x: c[int(x*N+N)])

sr = 44100.
fc = 100.
N = int(sr/(2*fc)) 
amps = pl.zeros(N)
for i in range(1,N):
   amps[i] = 1./i

t = pl.arange(0,sr)
w = 2*pl.pi*fc*t/sr

f = chebygen(amps)
scal = 2/pl.pi
s = scal*pl.sin(w)*f(pl.cos(w))


pl.figure(figsize=(8,3))

sig = s
#N = 32768
#start = 0
#x = pl.arange(0,N//2)
#bins = x*sr/N
#win = pl.hanning(N)
#scal = N*pl.sqrt(pl.mean(win**2))
#sig1 = sig[start:N+start]
#window = pl.fft(sig1*win/max(sig1))
#mags = abs(window/scal)
#spec = 20*pl.log10(mags/max(mags))

#pl.subplot(211)
#pl.plot(bins,spec[0:N//2], 'k-')
#pl.ylim(-60, 1)
#pl.ylabel("amp (dB)", size=16)
#pl.xlabel("freq (Hz)", size=16)
#pl.yticks()
#pl.xticks()
#pl.xlim(0,10000)

#pl.subplot(212)
pl.plot(pl.arange(0,880)/sr,sig[0:880], 'k-')
pl.xlim(0,880/sr)
pl.ylim(-1.1,1.1)
pl.yticks()
pl.xticks()

pl.tight_layout()
pl.show()
