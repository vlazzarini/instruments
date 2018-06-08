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

T = 40
t  = pl.arange(0,T)
pi = pl.pi
sig = pl.cos(2*pi*5*t/T) + pl.sin(2*pi*15*t/T) + pl.cos(2*pi*10*t/T - pl.pi/4)


spec = dft(sig)

pl.figure(figsize=(10,5))
pl.subplot(221)
pl.title('Real (cosines)')
pl.ylim(-1,1)
pl.stem(t,spec.real, 'k-', linewidth=1)
pl.subplot(222)
pl.title('Imaginary (sines)')
pl.ylim(-1,1)
pl.stem(t,spec.imag, 'k-', linewidth=1)
pl.subplot(223)
pl.title('Magnitudes')
pl.ylim(0,1.1)
pl.stem(t,abs(spec), 'k-', linewidth=1)
pl.subplot(224)
pl.title('Phases')
pl.ylim(0,1.1)
j = 0
for i in abs(spec):
    if abs(i) < 0.1: spec[j] = 0 + 0j
    j+=1        
pl.stem(t,pl.angle(spec), 'k-', linewidth=1)
pl.ylim(-pi,pi)
pl.tight_layout()
pl.show()

