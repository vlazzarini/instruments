import pylab as pl
import scipy.io.wavfile as wf
import sys

def stft(x,w):
    X = pl.rfft(x*w)   
    return X

def istft(X,w):    
    xn = pl.irfft(X)
    return xn*w
  
N = 1024
D = 8
H = N//D
zdbfs = 32768
(sr,signal) = wf.read(sys.argv[2])
signal = signal/zdbfs
L = len(signal)
win = pl.hanning(N)
Z = pl.zeros(N//2+1)+0j+10e-20
np = 0
ts = float(sys.argv[1])
output = pl.zeros(int(L/ts)+N)
ti = int(ts*H)
scal = 3*D/4

def plock(x):
    N = len(x)
    y = pl.zeros(N)+0j
    y[0], y[N-1] = x[0], x[N-1]
    y[1:N-1] = x[1:N-1] - (x[0:N-2] + x[2:N])
    return y

Z = pl.zeros(N//2+1)+0j+10e-20
for n in range(0,L-(N+H),ti):
    X1 = stft(signal[n:n+N],win)
    X2 = stft(signal[n+H:n+H+N],win)
    Y = X2*(Z/X1)*abs(X1/Z)
    Z = plock(Y)               
    output[np:np+N] += istft(Y,win)
    np += H

output = pl.array(output*zdbfs/scal,dtype='int16')
wf.write(sys.argv[3],sr,output)

import os
try:
 os.spawnlp(os.P_WAIT, 'sndfile-play', 'sndfile-play', sys.argv[3])
except:
 pass
