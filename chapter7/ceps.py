import pylab as pl

def dft(s):
   N = len(s)
   out = pl.zeros(N)*1j;
   for k in range(0,N):
    for t in range(0, N):
     out[k] += s[t]*(pl.cos(2*pl.pi*k*t/N)
                     - 1j*pl.sin(2*pl.pi*k*t/N))
   return out/N

saw = pl.zeros(100)
t  = pl.arange(0,100)
T = 100
N = T // 2
for k in range(1,N):
    saw += (1/k)*pl.sin(2*pl.pi*k*t/T)
saw *= 2/(pl.pi)    

spec = dft(saw)
mags = abs(spec)
scal = max(mags)

pl.figure(figsize=(8,3))
pl.stem(t,mags/scal, 'k-', linewidth=1)
pl.ylim(0,1.1)
pl.tight_layout()
pl.show()

