import pylab as pl

sr = 44100.
end = sr/50
pi = pl.pi
t =  pl.arange(0,end)
partials = [(1.,100.,-pi/2),
            (0.5,300.,0),
            (0.25,500.,-pi/2),
		    (0.1,700.,0),
            (0.05,800.,0),
		    (0.01,900.,-pi/2)]

s = pl.zeros(end)


pl.subplot(211)
pl.title("separate partials")
pl.xlim(0,end)
for n in partials:
      a,f,ph = n
      p = a*pl.cos(2*pi*f*t/sr + ph)
      pl.plot(t, p)
      s += p
      
pl.subplot(212)
pl.title("waveform")
pl.xlim(0,end)
pl.plot(t, s)
pl.tight_layout()
pl.show()
