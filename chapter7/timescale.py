import pylab as pl
import scipy.io.wavfile as wf
import sys

def stft(x,w):
    X = pl.rfft(x*w)   
    return X

def istft(X,w):    
    xn = pl.irfft(X)
    return xn*w

def p2r(mags, phs):
    return mags*pl.cos(phs) + 1j*mags*pl.sin(phs) 
  
N = 1024
D = 8
H = N//D
zdbfs = 32768
(sr,signal) = wf.read(sys.argv[2])
signal = signal/zdbfs
L = len(signal)
win = pl.hanning(N)
phs = pl.zeros(N//2+1)
np = 0
ts = float(sys.argv[1])
output = pl.zeros(int(L/ts)+N)
ti = int(ts*H)
scal = 3*D/4

def plock(phs):
    N = len(phs)
    x = p2r(pl.ones(N),phs) 
    y = pl.zeros(N)+0j
    y[0], y[N-1] = x[0], x[N-1]          
    for i in range(1,N-1):
       y[i] = x[i] - (x[i-1] + x[i+1])
    return y

for n in range(0,L-(N+H),ti):
    X1 = stft(signal[n:n+N],win)
    X2 = stft(signal[n+H:n+H+N],win)
    diffs = pl.angle(X2) - pl.angle(X1)
    phs += diffs
    Y = p2r(abs(X2),phs)                         
    output[np:np+N] += istft(Y,win)
    phs = pl.angle(plock(phs))
    np += H
  
output = pl.array(output*zdbfs/scal,dtype='int16')
wf.write(sys.argv[3],sr,output)

import os
try:
 os.spawnlp(os.P_WAIT, 'sndfile-play', 'sndfile-play', sys.argv[3])
except:
 pass
