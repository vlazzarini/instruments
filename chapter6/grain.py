import pylab as pl

sr = 40000.
f1 = 400
f2 = 40.
N = int((sr/2 - f1)/f2)

t = pl.arange(0,sr)
w = 2*pl.pi*f1*t/sr
o = 2*pl.pi*f2*t/sr
a = 0.4
if a > 10**(-3./N):
    a = 10**(-3./N)
    
sinw = pl.sin(w)
den = 0.5 - 0.5*pl.cos(o) 
s = sinw*den
    
pl.figure(figsize=(8,3))
              
pl.plot(t[0:1000]/sr,s[0:1000], 'k-')
pl.xlabel("time (s)")


pl.tight_layout()
pl.show()

