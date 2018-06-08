import pylab as pl

def plot_signal(s,sr,start=0,end=440,N=32768):
 '''plots the waveform and spectrum of a signal s
    with sampling rate sr, from a start to an
    end position (waveform), and from a start
    position with a N-point DFT (spectrum)'''
 pl.figure(figsize=(8,5))

 pl.subplot(211)
 sig = s[start:end]
 time = pl.arange(0,len(sig))/sr              
 pl.plot(time,sig, 'k-')
 pl.ylim(-1.1,1.1)
 pl.xlabel("time (s)")

 pl.subplot(212) 
 N = 32768
 win = pl.hanning(N)
 scal = N*pl.sqrt(pl.mean(win**2))
 sig = s[start:start+N]
 window = pl.rfft(sig*win/max(sig))
 f = pl.arange(0,len(window))
 bins = f*sr/N
 mags = abs(window/scal)
 spec = 20*pl.log10(mags/max(mags))
 pl.plot(bins,spec, 'k-')
 pl.ylim(-60, 1)
 pl.ylabel("amp (dB)", size=16)
 pl.xlabel("freq (Hz)", size=16)
 pl.yticks()
 pl.xticks()
 pl.xlim(0,sr/2)

 pl.tight_layout()
 pl.show()


sr = 44100
t = pl.arange(0,sr)
plot_signal(pl.cos(2*pl.pi*440*t/sr),sr)
