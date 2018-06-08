import pylab as pl

sr = 40000.
f1 = 1000
N = 1000

pl.figure(figsize=(8,5))

t = pl.arange(0,N)
w = 2*pl.pi*f1*t/sr

sinw = pl.sin(w)


pl.subplot(221)
env = pl.zeros(N)
R2 = 0.99
R1 = 0.97
for i in range(0, N):
    env[i] = R2**i-R1**i
s = sinw*env
s = s/abs(max(s))
pl.xticks([])
pl.yticks([])
pl.ylim(-1.1,1.1)   
pl.plot(t[0:N]/sr,s[0:N], 'k-')
pl.subplot(222)
env = pl.zeros(N)

for i in range(0, N):
   if i < N/8:
    env[i] = i/(N/8)
   elif i >= N/8 and i < 3*N/4:
    env[i] = 1
   elif i >= 3*N/4:
    env[i] =  1 - (i-3*N/4)/(N/4)
      
s = sinw*env
pl.xticks([])
pl.yticks([])
pl.ylim(-1.1,1.1)      
pl.plot(t[0:N]/sr,s[0:N], 'k-')
pl.subplot(223)
env = pl.zeros(N)

for i in range(0, N):
   if i < N/2:
    env[i] = i/(N/2)
   else:
    env[i] = 1 - (i-N/2)/(N/2)

s = sinw*env
pl.xticks([])
pl.yticks([])
pl.ylim(-1.1,1.1)   
pl.plot(t[0:N]/sr,s[0:N], 'k-')


pl.subplot(224)
env = pl.zeros(N)

for i in range(0, N):
    env[i] = pl.exp(-(((i - N/2)/(N/10))**2)/0.4)
    
s = env*pl.sin(w)
pl.xticks([])
pl.yticks([])
pl.ylim(-1.1,1.1)     
pl.plot(t[0:N]/sr,s[0:N], 'k-')


pl.tight_layout()
pl.show()

