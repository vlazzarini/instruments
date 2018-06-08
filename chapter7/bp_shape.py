import pylab as pl

sr = 44100
N = 2048
fc = 1000
w = 500
mask = pl.zeros(N//2+1)
d = int(w*N/sr)
b = int(fc*N/sr)
mask[b-d:b+d] = pl.hanning(2*d)

pl.figure(figsize=(8,3))
pl.plot(pl.arange(0,N//2+1)*sr/N,mask, 'k-', linewidth=2)
pl.xlim(0,5000)
pl.tight_layout()
pl.show()

