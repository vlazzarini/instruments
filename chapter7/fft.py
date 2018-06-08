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
   logN = int(pl.log2(N))
   for n in [2**x for x in range(0,logN)]:
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


def ifft(s):
   N = len(s)
   sig = reorder(s) 
   logN = int(pl.log2(N))
   for n in [2**x for x in range(0,logN)]:
    o = -pl.pi/n
    wp = pl.cos(o) + pl.sin(o)*1j
    w = 1+0j
    for m in range(0, n):
     for k in range(m,N,n*2):
       i = k + n
       even, odd = sig[k], w*sig[i]
       sig[k] = even + odd
       sig[i] = even - odd
     w *= wp
   return sig


def rfft(s):
    N = len(s)
    sig = s[:N:2] + s[1:N:2]*1j
    s = fft(sig)
    N = N//2
    w = complex(1,0)
    R = s[0].real*0.5
    I = s[0].imag*0.5
    zero =  R + I 
    nyqs =  R - I
    o = pl.pi/N
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

def irfft(s):
    N = len(s)
    w = complex(1,0)
    nyqs = s[0].imag
    zero = s[0].real 
    R = (zero + nyqs)
    I = 1j*(zero - nyqs)
    s[0] =  R + w*I
    o = -pl.pi/N
    wp = pl.cos(o) + pl.sin(o)*1j
    w *= wp
    for i in range(1,N//2+1):
        j = N - i
        R = 0.5*(s[i] + s[j].conjugate())
        I = 0.5j*(s[i] - s[j].conjugate())
        s[i] = R + w*I
        s[j] = (R - w*I).conjugate()
        w *= wp
    s = ifft(s)
    sig = pl.zeros(2*N)
    sig[0::2] = s.real
    sig[1::2] = s.imag 
    return sig
           
T = 512
t  = pl.arange(0,T)

def dft(s):
   N = len(s)
   out = pl.zeros(N)*1j;
   for k in range(0,N):
    for t in range(0, N):
     out[k] += s[t]*(pl.cos(2*pl.pi*k*t/N)
                     - 1j*pl.sin(2*pl.pi*k*t/N))
   return out/N

pl.figure(figsize=(8,5))
sig = pl.zeros(T)
N = T // 2
for k in range(1,N):
    sig += 2/(pl.pi*k)*pl.sin(2*pl.pi*k*t/T)
#sig = 0.5 + 0.5*sig*2/(pl.pi)
#sig = 0.5 + 0.5*pl.cos(2*pl.pi*10*t/T)

#sig = pl.sin(2*pl.pi*t/T)

pl.subplot(211)
import time
st = time.clock()
spec = rfft(sig)
print(time.clock() - st)
print(len(spec))
mags = abs(spec)
scal = max(mags)
print(spec[10].real)
pl.stem(t[0:T//2],(mags/scal)[0:T//2], 'k-', linewidth=1)
pl.ylim(0,1.1)
pl.xlim(0,T//2)
pl.subplot(212)

wav = irfft(spec)
pl.plot(t, wav, 'k-', linewidth=1)
pl.ylim(-1.1,1.1)
pl.xlim(0,T)
pl.tight_layout()
pl.show()

