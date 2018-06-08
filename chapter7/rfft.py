import pylab as pl

def reorder(s):
    N = len(s)
    o = s.copy()
    j = 0
    for i in range(0,N):
      if j > i:
        o[i] = s[j]
        o[j] = s[i]
      m = N//2
      while m >= 2 and j >= m:
        j -= m
        m = m//2 
      j += m
    return o

def fft(s):
   N = len(s)
   sig = reorder(s) + 0j
   l2N = int(pl.log2(N))
   for n in [2**x for x in range(0,l2N)]:
    o = pl.pi/n
    wp = pl.cos(o) + pl.sin(o)*1j
    w = 1+0j
    for m in range(0, n):
     for k in range(m,N,n*2):
       i = k + n
       even, odd = sig[k], w*sig[i]
       sig[k] = even + odd
       sig[i] = even - odd
     w *= wp
   return sig/N

def rfft(s):
    N = len(s)
    sig = s[:N:2] + s[1:N:2]*1j
    s = fft(sig)
    N = N//2
    o = pl.pi/N
    w = complex(1,0)
    R = s[0].real*0.5
    I = s[0].imag*0.5
    zero =  R + I 
    nyqs =  R - I
    s[0] = zero.real + 1j*nyqs.real
    wp = pl.cos(o) + pl.sin(o)*1j
    w *= wp
    for i in range(1,N//2+1):
        j = N - i
        R = 0.5*(s[i] + s[j].conjugate())
        I = 0.5j*(s[j].conjugate() - s[i])
        s[i] = R + w*I
        s[j] = (R - w*I).conjugate()
        w *= wp
    return s

T = 128
saw = pl.zeros(T)
t  = pl.arange(0,T)
N = T//2
for k in range(1,N):
    saw += (1/k)*pl.sin(2*pl.pi*k*t/T)
saw *= 2/(pl.pi)    

spec = rfft(saw)
mags = abs(spec)
scal = max(mags)

pl.figure(figsize=(8,3))
pl.stem(t[0:N],mags/scal, 'k-')
pl.ylim(0,1.1)
pl.xlim(0,N)

pl.tight_layout()
pl.show()
