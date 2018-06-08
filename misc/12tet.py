import pylab as pl
import matplotlib as m

frs = pl.array([2**(x/12) for x in range(0,88,1)])

def _12TET(fs):
    return 12*pl.log2(fs/27.5)

pl.figure(figsize=(8,3))
pl.plot(frs*27.5, _12TET(frs*27.5), 'k.')
pl.vlines(3520,0,90)
pl.vlines(1760,0,90)
pl.vlines(880,0,90)
pl.vlines(440,0,90)
pl.vlines(220,0,90)
pl.vlines(110,0,90)
pl.vlines(55,0,90)
#pl.xlim(20,3500)
pl.yticks([x*12 for x in range(1,8)])
pl.xticks([220*2**(x) for x in range(0,5)])
pl.xlabel('frequency (Hz,A4=440)')
pl.ylabel('12TET pitch')
pl.tight_layout()
pl.show()
