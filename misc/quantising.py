from pylab import *
from scipy.io import wavfile
import sys
name = sys.argv[1]

figure(figsize=(8,5))
(sr,sig) = wavfile.read(name)
start = 44100
dur = 100
wave = sig[start:dur+start]
wave = 0.9*wave/float(max(wave))
dirac = zeros(dur)
for i in range(0,len(dirac)):
    if i%5 == 0:
        dirac[i] = 1


plot(wave*15, 'k', linewidth=2)
xlim(0,dur)
quantised = round_((dirac*wave)*15)
markerline, stemlines, baseline = stem(quantised, 'k', markerfmt=' ')
setp(baseline, 'color', 'k', 'linewidth', 1)
xlim(0,dur)
ylim(-16, 15)
xticks([])
yticks(arange(-16,16,1), ["%d" % (x) for x in range(0,33)])
grid()
tight_layout()
show()
