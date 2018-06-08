import pylab as pl

sr = 40000.
f1 = 1000
N = 400

pl.figure(figsize=(8,5))

t = pl.arange(0,N)
w = 2*pl.pi*f1*t/sr

sinw = pl.sin(w)
env = pl.zeros(N)
R2 = 0.99
R1 = 0.985
for i in range(0, N):
    if i < N*0.9:
     env[i] = R2**i-R1**i
    else:
     env[i] = (R2**i-R1**i)*(-(i-N*0.9)/(N*0.1)+1)
s = sinw*env
s = s/abs(max(s))

sig = pl.zeros(sr)
for i in range(0, int(sr)):
    sig[i] = s[i%N]

pl.subplot(211)
pl.yticks([])
pl.xlabel("time (s)",size=16)
pl.yticks([])
pl.ylim(-1.1,1.1)   
pl.plot(pl.arange(0,N*4)/sr,sig[0:N*4], 'k-')

pl.subplot(212)
N = 32768
start = 0
x = pl.arange(0,N/2)
bins = x*sr/N
win = pl.hanning(N)
scal = N*pl.sqrt(pl.mean(win**2))
sig1 = sig[start:N+start]
window = pl.fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*pl.log10(mags/max(mags))
pl.xlim(0,5000)
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
#pl.ylabel("amp (dB)", size=16)
pl.yticks([])
pl.xlabel("freq (Hz)", size=16)
pl.xticks()

pl.tight_layout()
pl.show()

