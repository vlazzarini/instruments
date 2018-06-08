import pylab as pl
import scipy.io.wavfile as wf
import sys

def stft(x,w,n):
    N = len(w)
    X = pl.rfft(w*x)
    k = pl.arange(0,N/2+1)    
    return X*pl.exp(2*pl.pi*1j*k*n/N)

def istft(X,w,n):    
    N = len(w)
    k = pl.arange(0
                  ,N/2+1)   
    xn = pl.irfft(X*pl.exp(-2*pl.pi*1j*k*n/N))
    return xn*w

def p2r(mags, phs):
    return mags*pl.cos(phs) + 1j*mags*pl.sin(phs)  

def mask(mags,fc):
    m = pl.zeros(N//2+1)
    d = int((fc/2)*N/sr)
    b = int(fc*N/sr) 
    m[b-d:b+d] = pl.hanning(2*d)
    mags *= m
    return mags

N = 1024
D = 4
H = N//D
zdbfs = 32768
(sr,signal) = wf.read(sys.argv[1])
signal = signal/zdbfs
L = len(signal)
output = pl.zeros(L)
win = pl.hanning(N)
scal = 1.5*D/4

fc = 1000
fe = 5000
incr = (fe - fc)*(H/L)

for n in range(0,L,H):
    if(L-n < N): break
    frame = stft(signal[n:n+N],win,n)
    mags = abs(frame)
    phs = pl.angle(frame)
    mags = mask(mags,fc)
    fc += incr
    frame = p2r(mags,phs)
    output[n:n+N] += istft(frame,win,n)

output = pl.array(output*zdbfs/scal,dtype='int16')
wf.write(sys.argv[2],sr,output)
