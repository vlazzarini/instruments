import pylab as pl
import scipy.io.wavfile as wf
import sys

def pconv(input,ir,S=1024):
    N = len(ir)
    L = len(input)
    M = S*2

    P = int(pl.ceil(N/S))
    H = pl.zeros((P,M//2+1)) + 0j
    X = pl.zeros((P,M//2+1)) + 0j
    x = pl.zeros(M)
    o = pl.zeros(M)
    s = pl.zeros(S)
    
    for i in range(0,P):
        p = (P-1-i)*S
        ll = len(ir[p:p+S])
        x[:ll] = ir[p:p+S]
        H[i] = pl.rfft(x)
        
    y = pl.zeros(L+N-1)
    n = S   
    for p in range(0,L+N-S,S):
      if p > L:
        x = pl.zeros(M)
      else:       
       if n+p > L:
         n = L - p
         x[n:] = pl.zeros(M-n)
       x[:n] = input[p:p+n]
      X[i] = pl.rfft(x)
      O = pl.zeros(M//2+1) + 0j 
      for j in range(0,P):
        k = (j+i+1)%P
        O += H[j]*X[k]
      o = pl.irfft(O)
      y[p:p+S] = o[:S] + s
      s = o[S:]
      i = (i+1)%P
       
    return y

(sr,x1) = wf.read(sys.argv[1])
(sr,x2) = wf.read(sys.argv[2])

scal = 32768
L1 = len(x1)
L2 = len(x2)
y = pl.zeros(L1+L2-1)
p = 1
m = 0
if L1 > L2:
 for n in [32,128,1024,L2]:
  if L2 < n:
    y[m:L2+n-m-1] += pconv(x1[m:],x2[m:]/scal,p)
    break
  else:
    y[m:L2+n-m-1] += pconv(x1[m:],x2[m:n]/scal,p)
  p,m = n,n
 a = max(x1)
else:
 for n in [32,128,1024,L1]:
  if L1 <= n:
    y[m:L2+n-m-1] += pconv(x2[m:],x1[m:]/scal,p)
    break
  else:
    y[m:L2+n-m-1] += pconv(x2[m:],x1[m:n]/scal,p)
  p,m = n,n
 a = max(x2)
s = max(y)
scal = a/s
out = pl.array(y*scal,dtype='int16')
wf.write(sys.argv[3],sr,out)

