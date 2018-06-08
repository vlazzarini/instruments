import pylab as pl

T = 64
t  = pl.arange(0,T)
env = pl.zeros(T)

pl.figure(figsize=(8,3))

sig = pl.sin(2*pl.pi*(T/4)*t/T)*pl.hanning(T)

pl.ylim(0,1.1)
pl.xlim(0,T//2)
pl.xticks([x for x in range(0,T//2+1,4)])
pl.stem(t[0:T//2],abs(pl.rfft(sig)/(T/4))[0:T//2], 'k-', linewidth=1)
pl.tight_layout()
pl.show()

