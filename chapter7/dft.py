import pylab as pl
import time

def dft(s):
   N = len(s)
   out = pl.zeros(N)+0j;
   t = pl.arange(0,N)
   for k in range(0,N):
     out[k] = pl.sum(s*(pl.cos(2*pl.pi*k*t/N)
                     - 1j*pl.sin(2*pl.pi*k*t/N)))
   return out/N

T = 1000
saw = pl.zeros(T)
t  = pl.arange(0,T)
N = T // 2
for k in range(1,N):
    saw += (1/k)*pl.sin(2*pl.pi*k*t/T)
saw *= 2/(pl.pi)    

tim = time.clock()
spec = dft(saw)
print(time.clock() - tim)
mags = abs(spec)
scal = max(mags)

pl.figure(figsize=(8,3))
pl.stem(t,mags/scal, 'k-', linewidth=1)
pl.ylim(0,1.1)
pl.tight_layout()
pl.show()

