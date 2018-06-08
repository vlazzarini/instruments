import pylab as pl

sr = 44100
fc = 500
t = pl.arange(0,sr)

def vps(x,d,v):
	if x < d:		return (v*x)/d
	else:			return (1-v)*(x-d)/(1-d) + v
        
def phasor(ph,freq,sr):
    incr = freq/sr
    ph += incr
    return ph - pl.floor(ph)   
        
s = pl.zeros(sr)
ph = 0.0
for n in t:
   ph = phasor(ph,fc,sr)
   s[n] = pl.cos(2*pl.pi*vps(ph,0.3,1.5))


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
 f = pl.arange(0,N/2)
 bins = f*sr/N
 win = pl.hanning(N)
 scal = N*pl.sqrt(pl.mean(win**2))
 sig = s[start:start+N]
 window = pl.fft(sig*win/max(sig))
 mags = abs(window/scal)
 spec = 20*pl.log10(mags/max(mags))
 pl.plot(bins,spec[0:N//2], 'k-')
 pl.ylim(-60, 1)
 pl.ylabel("amp (dB)", size=16)
 pl.xlabel("freq (Hz)", size=16)
 pl.yticks()
 pl.xticks()
 pl.xlim(0,sr/2)

 pl.tight_layout()
 pl.show()

plot_signal(s,sr)
