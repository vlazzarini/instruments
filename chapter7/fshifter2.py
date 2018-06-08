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

def plock(phs):
    N = len(phs)
    c = p2r(pl.ones(N),phs) 
    phi = pl.zeros(N)           
    for i in range(0,N):
       if(i == 0): y = c[i] - c[i+1] 
       elif(i ==  N-1): y = c[i] - c[i-1]
       else: y = c[i] - (c[i-1] + c[i+1])
       phi[i] = pl.angle(y)
    return phi

class Pvoc:
   def __init__(self,w,h,sr):
     N = len(w)
     self.win = w
     self.phs = pl.zeros(N//2+1)
     self.h = h
     self.n = 0
     self.fc = pl.arange(N//2+1)*sr/N
     self.sr = sr

   def analysis(self,x):
     X = stft(x,self.win)
     delta = pl.angle(X) - self.phs
     self.phs = pl.angle(X)
     return abs(X),delta

   def synthesis(self,amps,freqs):
      self.phs += freqs
      phs = plock(self.phs) 
      X = amps*pl.cos(phs) + 1j*amps*pl.sin(phs)
      y = istft(X,self.win)
      return y



N = 1024
D = 8
H = N//D
zdbfs = 32768
(sr,signal) = wf.read(sys.argv[2])
signal = signal/zdbfs
L = len(signal)
output = pl.zeros(L)
win = pl.hanning(N)

pva = Pvoc(win,H,sr)
pvs = Pvoc(win,H,sr)
trans = float(sys.argv[1])

def scale(amps,freqs,p):
    N = len(freqs)
    a,f = pl.zeros(N),pl.zeros(N)
    for i in range(0, N):
       n = int((i*p))
       if n > 0 and n < N-1:
          f[n] = p*freqs[i]
          a[n] = amps[i]  
    return a,f

def spec_env(amps,coefs):
    N = len(amps)
    mags = amps.copy()
    sm = 10**(-13)
    ceps = pl.rfft(pl.log(mags[0:N-1]+sm))
    ceps[coefs:] = 0
    mags[:N-1] = pl.exp(pl.irfft(ceps))
    return mags+sm

for n in range(0,L,H):
    if(L-n < N): break
    amps,freqs = pva.analysis(signal[n:n+N])
    env1 = spec_env(amps,40)
    amps,freqs = scale(amps,freqs,trans)
    env2 = spec_env(amps,40)
    output[n:n+N] += pvs.synthesis(amps,freqs)

scal = max(output)/max(signal)    
output = pl.array(output*zdbfs/scal,dtype='int16')
wf.write(sys.argv[3],sr,output)

import os
try:
 os.spawnlp(os.P_WAIT, 'sndfile-play', 'sndfile-play', sys.argv[3])
except:
 pass
