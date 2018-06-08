##################################################
#
# copyright (c)Victor Lazzarini, 2008
#
# Free Software, licensed by the GNU Public License
###################################################
from pylab import *
from scipy.signal import *
from scipy.io import wavfile
import os
import sys

# output filename
name = 'fbam.wav'
# DSP parameters
sr   = 44100.
N    = 16384

# time in samples
t    = arange(0,44100)

# bin frequencies
bins = t[0:N/2]*sr/N

# synthesis parameters
fo = 250
w = 2*pi*fo/sr
fc = 5000
wc = 2*pi*fc/sr


# 16-bit RIFF-Wave file output
def output(file, x, amp=10000):
  wavfile.write(file,sr,array(x*amp, dtype='int16'))
figure(figsize=(8,5))
# synthesis algorithm
sig = zeros(len(t))

delay = 0.0
ph = 0.0
ph2 = 0.0
beta = 0.9
for i in t:
   sig[i] = cos(ph) + cos(ph2)*beta*delay
   delay = sig[i]
   ph += wc
   ph2 += w



scale = (1. - beta*cos(w*t))


sig = sig/max(abs(sig))
# output(name,sig)

win = hanning(N)
spec = fft(win*sig[1024:N+1024])
mags = sqrt(spec[0:N/2].real**2 + spec[0:N/2].imag**2)
scal = N*sqrt(mean(win**2))

# DFT dB mags plot
subplot(211)
plot(bins, 20*log10(mags/scal), 'k-')
yticks([0, -30, -60, -90])
xticks(arange(3)*5000)
xlim(0,10000)
ylim(-90,0)
ylabel("amp (dB)", size=16)
xlabel("freq", size=16)

# waveform plot
subplot(212)
end = 441
plot(t[0:end]/sr,sig[441:end+441],'k-')
yticks()
ylabel("amp", size=16)
xlabel("time", size=16)

ylim(-1.1,1.1)

# play it on linux
if (sys.platform[:5] == 'linux'): 
  os.spawnlp(os.P_NOWAIT, 'aplay', 'aplay', name)
tight_layout()
show()
