import pylab as pl

saw = pl.zeros(10000)
t  = pl.arange(0,10000)
T = 5000
N = 1000
for k in range(1,N+1):
    saw += (1/k)*pl.sin(2*pl.pi*k*t/T)
saw *= 2/(pl.pi)    
    
pl.figure(figsize=(8,3))    
pl.plot(t/T, saw, 'k-', linewidth=2)

pl.tight_layout()
pl.show()

