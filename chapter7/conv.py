import pylab as pl
import scipy.io.wavfile as wf
import sys

def conv(input,ir):
    N = len(ir)
    L = len(input)
    M = 2
    while(M <= 2*N-1): M *= 2
        
    h = pl.zeros(M)
    x = pl.zeros(M)
    y = pl.zeros(L+N-1)

    h[0:N] = ir
    H = pl.rfft(h)
    n = N
    for p in range(0,L,N):
     if p+n > L:
          n = L-p
          x[n:] = pl.zeros(M-n)
     x[0:n] = input[p:p+n]
     y[p:p+2*n-1] += pl.irfft(H*pl.rfft(x))[0:2*n-1]
         
    return y

(sr,x1) = wf.read(sys.argv[1])
(sr,x2) = wf.read(sys.argv[2])

scal = 32768
if len(x1) > len(x2):
 y = conv(x1,x2/scal)
 a = max(x1)
else:
 y = conv(x2, x1/scal)    
 a = max(x2)

s = max(y)
out = pl.array(y*a/s,dtype='int16')
wf.write(sys.argv[3],sr,out)

