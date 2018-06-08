import pylab as pl

amps = pl.array([10**(x/20) for x in range(0,60,1)]) 

def db2amp(amp):
    return 20*pl.log10(1/amp)

pl.figure(figsize=(8,3))
pl.plot(1/amps, db2amp(amps), 'k.')
pl.xlim(0,1.01)
pl.ylim(-61,3)
pl.yticks([-60,-54,-48,-42,-36,-30,-24,-18,-12,-6,0])
pl.xticks([0.125,0.25,0.5,1.0])
pl.vlines(1.0,-61,3)
pl.vlines(0.5,-61,3)
pl.vlines(0.25,-61,3)
pl.vlines(0.125,-61,3)
pl.vlines(0.0625,-61,3)
pl.vlines(0.0625/2,-61,3)
pl.vlines(0.0625/4,-61,3)
pl.xlabel('amplitude (fs=1.0)')
pl.ylabel('dB')
pl.tight_layout()
pl.show()
