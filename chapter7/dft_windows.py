import pylab as pl

def dft(s):
   N = len(s)
   out = pl.zeros(N)*1j;
   for k in range(0,N):
    for t in range(0, N):
     out[k] += s[t]*(pl.cos(2*pl.pi*k*t/N)
                     - 1j*pl.sin(2*pl.pi*k*t/N))
   return out/N

def idft(s):
   N = len(s)
   out = pl.zeros(N);
   for t in range(0,N):
    for k in range(0, N):
     out[k] += s[t]*(pl.cos(2*pl.pi*k*t/N)
                     + 1j*pl.sin(2*pl.pi*k*t/N))
   return out.real


t  = pl.arange(0,100)
T = 100


pl.figure(figsize=(8,5))
sig = pl.sin(2*pl.pi*25.5*t/T)

pl.subplot(211)

spec = dft(sig)
mags = abs(spec)
scal = max(mags)

pl.stem(t[0:T/2],(mags/scal)[0:T/2], 'k-', linewidth=1)
pl.ylim(0,1.1)

pl.subplot(212)

spec = dft(sig*(0.5-0.5*pl.cos(2*pl.pi*t/T)))
mags = abs(spec)
scal = max(mags)

pl.stem(t[0:T/2],(mags/scal)[0:T/2], 'k-', linewidth=1)
pl.ylim(0,1.1)

pl.tight_layout()
pl.show()

