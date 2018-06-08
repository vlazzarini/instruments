import pylab as pl

sr = 44100
fr = 441
amp = 0.75

def sinosc(amp,freq,ph,sr):
    incr = freq*2*pl.pi/sr
    out = pl.zeros(sr)
    for i in range(0,sr):
      out[i] = pl.sin(ph)
      ph += incr                
    out *= amp
    return out

def oscil(amp,freq,ph,tab,sr):
    incr = freq*len(tab)/sr
    out = pl.zeros(sr)
    for i in range(0,sr):
      out[i] = tab[int(ph)%len(tab)]
      ph += incr                
    out *= amp
    return out

def phasor(ph,freq,sr):
    incr = freq/sr
    ph += incr
    return ph - int(ph)    

def oscil2(amp,freq,ph,tab,sr):
    out = pl.zeros(sr)
    for i in range(0,sr):
      ph = phasor(ph,freq,sr)
      out[i] = tab[int(ph*len(tab))]
    out *= amp
    return out

def oscili(amp,freq,ph,tab,sr):
    size = len(tab)-1
    out = pl.zeros(sr)
    for i in range(0,sr):
      ph = phasor(ph,freq,sr)
      pos = size*ph
      posi = int(pos)
      frac = pos - posi
      out[i] = tab[posi] + frac*(tab[posi+1] - tab[posi])              
    out *= amp
    return out
        

tab = pl.sin(2*pl.pi*pl.arange(0,10001)/10000.)
out = oscili(amp,fr,-fr/sr,tab,sr)

pl.plot(out[0:441])
pl.tight_layout()
pl.show()
