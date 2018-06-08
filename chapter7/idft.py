import pylab as pl

def dft(s):
   N = len(s)
   out = pl.zeros(N)+0j;
   t = pl.arange(0,N)
   for k in range(0,N):
     out[k] = sum(s*(pl.cos(2*pl.pi*k*t/N)
                     - 1j*pl.sin(2*pl.pi*k*t/N)))
   return out/N

def idft(s):
   N = len(s)
   out = pl.zeros(N);
   k = pl.arange(0,N)
   for t in range(0,N):
     out[t] = sum(s*(pl.cos(2*pl.pi*k*t/N)
                     + 1j*pl.sin(2*pl.pi*k*t/N)))
   return out.real

T = 100
t  = pl.arange(0,T)


pl.figure(figsize=(8,5))

pl.subplot(211)
sig = 0.5+0.5*pl.sin(2*pl.pi*3.333*t/T)
pl.plot(t,sig, 'k-', linewidth=1)

pl.subplot(212)
spec = dft(sig)
#spec = dft(sig)
spec2 = pl.zeros(len(spec))+0j
spec2[1:T-1] =  0.5*spec[1:T-1]  - 0.25*spec[:T-2] - 0.25*spec[2:T]
spec2[0] =  0.5*spec[0] - 0.25*spec[1] - 0.25*spec[T-1]
spec2[T-1] =  spec[T-1] - 0.25*spec[T-2]  - 0.25*spec[0]
#
sig2 = idft(spec2)
#pl.stem(abs(spec2[0:T/2]), 'k-', linewidth=1)

pl.plot(sig2, 'k-', linewidth=1)

pl.tight_layout()
pl.show()

