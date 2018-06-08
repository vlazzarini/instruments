from pylab import *
from scipy.io import wavfile
import sys
name = sys.argv[1]

figure(figsize=(8,3))
(sr,sig) = wavfile.read(name)
start = 0
dur = 2048
plot(sig[start:dur+start]/32768., 'k', linewidth=2)
xlim(0,dur)
ylim(-1.1, 1.1)
xticks([])
tight_layout()
show()
