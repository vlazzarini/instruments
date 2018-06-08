import pylab as pl

sr = 44100.
fr = 100.
N = sr/(fr*2)

t = pl.arange(0,sr)
s = pl.zeros(sr)
w = 2*pl.pi*fr/sr
        
for n in t:
    den = pl.sin(w*n/2.)
    if abs(den) > 0.0002:
     s[n] = (1./(2*N)) * (pl.sin((2*N+1)*w*n/2.)/den - 1.)
    else: s[n] = 1. 

pl.figure(figsize=(8,3))               
pl.plot(t[0:440]/sr,s[220:660], 'k-')
pl.xlabel("time (s)", size=16)
pl.tight_layout()
pl.show()

