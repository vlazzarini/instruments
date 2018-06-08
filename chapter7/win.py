import pylab as pl

pi = pl.pi
T = 1000
t = pl.arange(0,T)
x = 0.51 - 0.49*pl.cos(2*pi*t/T)
y = pl.sin(2*pi*10*t/T)
X = pl.rfft(y*x)
pl.plot(pl.irfft(X))
pl.show()
