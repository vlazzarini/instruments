import pylab as pl

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
 
N = 1024
D = 16
H = N//D
win = pl.hanning(N)
sr = 44100
f = 50
t = pl.arange(0,sr)
L = sr
t = pl.arange(0,L) 
input = pl.sin(2*pl.pi*f*t/sr)
output = pl.zeros(L)
scal = 1.5*D/4
pva = Pvoc(win,H,sr)
pvs = Pvoc(win,H,sr)
bin = round(N*f/sr)

for n in range(0,L,H):
    if(L-n < N): break
    amps,freqs = pva.analysis(input[n:n+N])
    print(round(freqs[bin]))
    output[n:n+N] += pvs.synthesis(amps,freqs)

#pl.figure(figsize=(8,3))
#pl.ylim(-1.1,1.1)
#pl.plot((output/scal),'k-')
#pl.show()
