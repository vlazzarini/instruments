from pylab import *
from scipy.io import wavfile
import sys
name = sys.argv[1]

figure(figsize=(8,6))
(sr,sig) = wavfile.read(name)
start = 44100
dur = 200
wave = sig[start:dur+start]
wave = wave/float(max(wave))
dirac = zeros(dur)
for i in range(0,len(dirac)):
    if i%5 == 0:
        dirac[i] = 1

subplot(311)
markerline, stemlines, baseline = stem(dirac, 'k', markerfmt=' ')
setp(baseline, 'color', 'k', 'linewidth', 1)
xlim(0,dur)
ylim(-0.1, 1.1)
xticks([])
tight_layout()
subplot(312)
plot(wave, 'k', linewidth=2)
xlim(0,dur)
ylim(-1.1, 1.1)
xticks([])
tight_layout()
subplot(313)
markerline, stemlines, baseline = stem(dirac*wave, 'k', markerfmt=' ')
setp(baseline, 'color', 'k', 'linewidth', 1)
xlim(0,dur)
ylim(-1.1, 1.1)
xticks([])
tight_layout()
show()
