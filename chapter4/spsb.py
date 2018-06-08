import pylab as pl
from scipy.signal import hilbert

sr = 44100.
fc = 3000
fm = 500.

t = pl.arange(0,sr)
w = 2*pl.pi*fc*t/sr
o = 2*pl.pi*fm*t/sr
I = 3.5

sod = pl.sin(I*pl.sin(o))
sev = pl.cos(I*pl.sin(o))
qsod = pl.imag(hilbert(sod))
qsev = pl.imag(hilbert(sev))
sinw = pl.sin(w)
cosw = pl.cos(w)

sue = sev*sinw + qsev*cosw 
suo = sod*sinw + qsod*cosw
sle = sev*sinw - qsev*cosw
slo = sod*sinw - qsod*cosw

pl.figure(figsize=(8,5))

pl.subplot(221)
sig = sue
pl.title("upper,even")               
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
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.ylabel("amp (dB)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,6000)

pl.subplot(222)
sig = suo
pl.title("upper,odd")                 
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
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.yticks()
pl.xticks()
pl.xlim(0,6000)

pl.subplot(223)
sig = sle
pl.title("lower,even")                 
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
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.ylabel("amp (dB)", size=16)
pl.xlabel("freq (Hz)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,6000)

pl.subplot(224)
sig = slo
pl.title("lower,odd")                 
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
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
pl.xlabel("freq (Hz)", size=16)
pl.yticks()
pl.xticks()
pl.xlim(0,6000)

pl.tight_layout()
pl.show()
