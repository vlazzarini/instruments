import pylab as pl

sr = 44100.
end = sr/50
pi = pl.pi
t =  pl.arange(0,end)
f = 100 
amps = [1.,0,1./3,0,1./5,0,1./7,0,1./9.]
ph = -pi/2
s = pl.zeros(end)

pl.subplot(311)
pl.title("harmonics")
pl.xlim(0,end)
k = 1
for a in amps:
    p = a*pl.cos(2*pi*f*k*t/sr + ph)
    pl.plot(t, p)
    s += p
    k += 1
      
pl.subplot(312)
pl.title("square wave")
pl.xlim(0,end)
pl.plot(t, s)
pl.subplot(313)
pl.title("spectrum")

end = len(amps)+1
pl.xlim(0,end)
pl.ylim(0,1.1)
pl.stem(pl.arange(1,end),amps,markerfmt=" ")
pl.tight_layout()
pl.show()
