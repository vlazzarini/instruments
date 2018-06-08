import pylab as pl

def bitrev(s):
    N = len(s)
    j = 0
    for i in range(0,N):
      if j > i:
        tmp = s[j]
        s[j] = s[i]
        s[i] = tmp
      m = N//2
      while m >= 2 and j >= m:
        j -= m
        m = m//2 
      j += m
    return s

def fft(s):
   N = len(s)
   sig = bitrev(s) + 0j
   w = complex(0,0) 
   n = 1
   while n < N:
    o = pl.pi/n
    wp = pl.cos(o) + pl.sin(o)*1j
    w = 1
    n2 = n*2
    for m in range(0, n):
     for k in range(m,N,n2):
       i = k + n
       even, odd = sig[k], w*sig[i]
       sig[k] = even + odd
       sig[i] = even - odd
     w *= wp
    n = n2
   return sig/N

def dft(s):
   N = len(s)
   out = pl.zeros(N)*1j;
   for k in range(0,N):
    for t in range(0,N):
      out[k] += s[t]*(pl.cos(2*pl.pi*k*t/N)
                     - 1j*pl.sin(2*pl.pi*k*t/N))
   return out/N

T = 100
saw = pl.zeros(T)
t  = pl.arange(0,T)
N = T // 2 
for k in range(1,N):
    saw += (1/k)*pl.sin(2*pl.pi*k*t/T)
saw += 0.001 + 0.001*pl.cos(pl.pi*t/T)
saw *= 2/(pl.pi)    

spec = dft(saw)
print(abs(spec[0]))
phs = pl.angle(spec)

pl.figure(figsize=(8,3))
pl.stem(t,phs, 'k-', linewidth=1)
pl.ylim(-pl.pi-0.5, +pl.pi+0.5)
pl.tight_layout()
pl.show()

