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

def spec_env(frame,coefs):
    mags = abs(frame)
    N = len(mags)
    ceps = pl.rfft(pl.log(mags[:N-1]))
    ceps[coefs:] = 0
    mags[:N-1] = pl.exp(pl.irfft(ceps))
    return mags
    
N = 1024
D = 4
H = N//D
zdbfs = 32768
(sr,in1) = wf.read(sys.argv[1])
(sr,in2) = wf.read(sys.argv[2])
L1 = len(in1)
L2 = len(in2)
if L2 > L1: L = L2
else: L = L1
signal1 = pl.zeros(L)
signal2 = pl.zeros(L)
signal1[:len(in1)] = in1/zdbfs
signal2[:len(in2)] = in2/zdbfs
output = pl.zeros(L)
win = pl.hanning(N)
scal = 1.5*D/4

for n in range(0,L,H):
    if(L-n < N): break
    frame1 = stft(signal1[n:n+N],win,n)
    frame2 = stft(signal2[n:n+N],win,n)
    mags = abs(frame1)
    env1 = spec_env(frame1,20)
    env2 = spec_env(frame2,20)
    phs = pl.angle(frame1)
    if(min(env1) > 0):
     frame = p2r(mags*env2/env1,phs)
    else:
     frame = p2r(mags*env2,phs)
    output[n:n+N] += istft(frame,win,n)

a = max(signal1)
b = max(output)
c = a/b     
output = pl.array(output*zdbfs*c/scal,dtype='int16')
wf.write(sys.argv[3],sr,output)


