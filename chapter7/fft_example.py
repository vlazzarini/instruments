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


T = 128
saw = pl.zeros(T)
t  = pl.arange(0,T)
N = T//2
for k in range(1,N):
    saw += (1/k)*pl.sin(2*pl.pi*k*t/T)
saw *= 2/(pl.pi)    

spec = fft(saw)
mags = abs(spec)
scal = max(mags)

pl.figure(figsize=(8,3))
pl.stem(t,(mags/scal), 'k-')
pl.ylim(0,1.1)
pl.xlim(0,T)

pl.tight_layout()
pl.show()
