import pylab as pl
import scipy.io.wavfile as wf
import sys

def stft(x,w,n):
    N = len(w)
    X = pl.rfft(x*w)
    k = pl.arange(0,N/2+1)    
    return X*pl.exp(-2*pl.pi*1j*k*n/N)

def istft(X,w,n):    
    N = len(w)
    k = pl.arange(0,N/2+1)   
    xn = pl.irfft(X*pl.exp(2*pl.pi*1j*k*n/N))
    return xn*w

def modpi(x):
   if x >= pl.pi: x -= 2*pl.pi
   if x < -pl.pi: x += 2*pl.pi
   return x
unwrap = pl.vectorize(modpi)

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
     X = stft(x,self.win,self.n)
     delta = pl.angle(X) - self.phs
     self.phs = pl.angle(X)
     delta = unwrap(delta)
     freqs = self.fc + delta*self.sr/(2*pl.pi*self.h) 
     self.n += self.h
     return abs(X),freqs

   def synthesis(self,amps,freqs):
      delta = (freqs - self.fc)*(2*pl.pi*self.h)/self.sr
      self.phs += delta
      X = amps*pl.cos(self.phs) + 1j*amps*pl.sin(self.phs)
      y = istft(X,self.win,self.n)
      self.n += self.h
      return y

def scale(amps,freqs,p):
    N = len(freqs)
    a,f = pl.zeros(N),pl.zeros(N)
    for i in range(0, N):
       n = int((i*p))
       if n > 0 and n < N-1:
          f[n] = p*freqs[i]
          a[n] = amps[i]  
    return a,f

N = 1024
D = 8
H = N//D
zdbfs = 32768
(sr,signal) = wf.read(sys.argv[2])
signal = signal/zdbfs
L = len(signal)
output = pl.zeros(L)
win = pl.hanning(N)
scal = 1.5*D/4

pva = Pvoc(win,H,sr)
pvs = Pvoc(win,H,sr)
trans = float(sys.argv[1])

for n in range(0,L,H):
    if(L-n < N): break
    amps,freqs = pva.analysis(signal[n:n+N])
    amps,freqs = scale(amps,freqs,trans)
    output[n:n+N] += pvs.synthesis(amps,freqs)

output = pl.array(output*zdbfs/scal,dtype='int16')
wf.write(sys.argv[3],sr,output)

import os
try:
 os.spawnlp(os.P_WAIT, 'sndfile-play', 'sndfile-play', sys.argv[3])
except:
 pass
