import pylab as pl

T = 1000
t  = pl.arange(0,T)
env = pl.zeros(T)

pl.figure(figsize=(8,5))

for i in t:
   if i >= T*0.25 and i < T*0.83:
    env[i] = 1

pl.subplot(211)
sig = pl.sin(2*pl.pi*4*t/T)
pl.ylim(-1.1,1.1)
pl.plot(t,sig, 'k-', linewidth=1)
pl.plot(t,env, 'k--', linewidth=1)

pl.subplot(212)
pl.ylim(-1.1,1.1)
pl.plot(t,sig*env, 'k-', linewidth=1)

pl.tight_layout()
pl.show()

