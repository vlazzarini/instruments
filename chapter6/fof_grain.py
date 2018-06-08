import pylab as pl

sr = 40000.
f1 = 1000
N = 1000

pl.figure(figsize=(8,5))

t = pl.arange(0,N)
w = 2*pl.pi*f1*t/sr

sinw = pl.sin(w)
env = pl.zeros(N)
R2 = 0.997
R1 = 0.99
for i in range(0, N):
    if i < N*0.9:
     env[i] = R2**i-R1**i
    else:
     env[i] = (R2**i-R1**i)*(-(i-N*0.9)/(N*0.1)+1)
s = sinw*env
s = s/abs(max(s))
pl.xticks([])
pl.yticks([])
pl.ylim(-1.1,1.1)   
pl.plot(t[0:N]/sr,s[0:N], 'k-')

pl.tight_layout()
pl.show()

