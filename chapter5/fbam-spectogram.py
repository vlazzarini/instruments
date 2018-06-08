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
N    = 1024

# time in samples
t    = arange(0,44100)

# bin frequencies
bins = t[0:N/2]*sr/N

# synthesis parameters
fo = 500
w = 2*pi*fo/sr

# 16-bit RIFF-Wave file output
def output(file, x, amp=10000):
  wavfile.write(file,sr,array(x*amp, dtype='int16'))

# synthesis algorithm
sig = zeros(len(t))

delay = 0.0
ph = 0.0
beta = 0.0
betainc = 1./(44100 - 1024)
for i in t:
   sig[i] = cos(ph)*(1 + beta*delay)
   delay = sig[i]
   ph += w
   if(i > 1024): beta += (betainc)



scale = (1. - beta*cos(w*t))

figure(figsize=(8,3))
sig = sig/max(sig)
# output(name,sig)

#win = hanning(N)
#spec = fft(win*sig[1024:N+1024])
#mags = sqrt(spec[0:N/2].real**2 + spec[0:N/2].imag**2)
#scal = N*sqrt(mean(win**2))

# DFT dB mags plot
#subplot(211)
#title("%i-point Magnitude DFT(dB)" % N)
#plot(bins, 20*log10(mags/scal), 'k-')
#xlim(0,sr/2)
#ylim(-220,0)

# waveform plot
#subplot(212)
#title("waveform (100ms segment)")
#plot(t[1000:1000+441]/sr,sig[1000:1000+441],'k-')
#ylim(-1.1,1.1)

# play it on linux
if (sys.platform[:5] == 'linux'): 
  os.spawnlp(os.P_NOWAIT, 'aplay', 'aplay', name)

specgram(sig[0:44100],2048,sr,noverlap=256,cmap=cm.gray)
#colorbar(ticks=[0,-12,-24,-36,-48,-60,-72,-84,-96])
ylim(0,10000)
clim(-180,0)
xlabel("time (s)", size=16)
ylabel("freq (Hz)", size=16)
xticks([0.2,0.4,0.6,0.8], size=16)
xlim(0,0.8)
yticks(size=12)
tight_layout()



show()
