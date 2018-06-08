import pylab as pl

def stft(x,w,n):
    N = len(w)
    X = pl.rfft(w*x)
    k = pl.arange(0,N/2+1)    
    return X*pl.exp(2*pl.pi*1j*k*n/N)

def istft(X,w,n):    
    N = len(w)
    k = pl.arange(0,N/2+1)   
    xn = pl.irfft(X*pl.exp(-2*pl.pi*1j*k*n/N))
    return xn*w

N = 1024
D = 4
H = N//D

t = pl.arange(0,N)
win = 0.5 - 0.5*pl.cos(2*pl.pi*t/N)

sr = 44100
f = 50
L = sr
t = pl.arange(0,L) 
input = pl.sin(2*pl.pi*f*t/sr)
output = pl.zeros(L)
x = pl.zeros(N)
scal = 1.5*D/4

for n in range(0,L,H):
    if(L-n < N): break
    frame = stft(input[n:n+N],win,n)
    output[n:n+N] += istft(frame,win,n)

pl.figure(figsize=(8,3))
pl.ylim(-1.1,1.1)
pl.plot(t/sr,output/scal,'k-')
pl.show()
