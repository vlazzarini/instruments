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
fo = 5000
w = 2*pi*fo/sr
fm = fo/10
o = 2*pi*fm/sr
fc = fo
Q = 2.5
I = 2
# 16-bit RIFF-Wave file output
def output(file, x, amp=10000):
  wavfile.write(file,sr,array(x*amp, dtype='int16'))
figure(figsize=(8,5))
# synthesis algorithm
sig = zeros(len(t))

y2 = 0.0
y1 = 0.0
ph = 0.0
ph2 = 0.0
beta = 1.
for i in t:
   x = cos(ph)
   f = fc + I*fm*cos(ph2)
   r = exp(-pi*(f/Q)/sr)
   a1 = ((4*r*r)/(1 + r*r))*cos(2*pi*f/sr)
   a2 = r*r
   y = x + a1*y1 - a2*y2
   y2 = y1
   y1 = y
   sig[i] = y
   ph += w
   ph2 += o


scale = 1;#(1. - beta*cos(w*t))


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
plot(t[0:end]/sr,sig[30000:end+30000],'k-')
yticks()
ylabel("amp", size=16)
xlabel("time", size=16)

ylim(-1.1,1.1)

# play it on linux
if (sys.platform[:5] == 'linux'): 
  os.spawnlp(os.P_NOWAIT, 'aplay', 'aplay', name)
tight_layout()
show()
