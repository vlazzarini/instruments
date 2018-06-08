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
fo = 440.
w = 2*pi*fo/sr
w2 = w*1.414
# 16-bit RIFF-Wave file output
def output(file, x, amp=10000):
  wavfile.write(file,sr,array(x*amp, dtype='int16'))

# synthesis algorithm
sig = zeros(len(t))

delay = 0.0
ph = 0.0
ph2 = 0.0
beta = 1
for i in t:
   sig[i] = cos(ph) + beta*cos(ph2)*delay
   delay = sig[i]
   ph += w
   ph2 += w2

sig = sig/max(sig)
# output(name,sig)

win = hanning(N)
spec = fft(win*sig[0:N])
mags = sqrt(spec[0:N/2].real**2 + spec[0:N/2].imag**2)
scal = N*sqrt(mean(win**2))

# DFT dB mags plot
subplot(211)
title("%i-point Magnitude DFT(dB)" % N)
plot(bins, 20*log10(mags/scal), 'k-')
xlim(0,3000)
ylim(-60,0)

# waveform plot
subplot(212)
title("waveform (100ms segment)")
plot(t[0:441]/sr,sig[441:882],'k-')
ylim(-1.1,1.1)

# play it on linux
if (sys.platform[:5] == 'linux'): 
  os.spawnlp(os.P_NOWAIT, 'aplay', 'aplay', name)

show()
