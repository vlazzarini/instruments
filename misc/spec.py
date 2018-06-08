from pylab import *
from scipy.io import wavfile 
import sys
name = sys.argv[1]

(sr,sig) = wavfile.read(name)
N = 4096
print len(sig)
start = 0
x = arange(0,N/2)
bins = x*sr/N
win = hanning(N)
scal = N*sqrt(mean(win**2))
sig1 = sig[start:N+start]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-')

ylim(-60, 1)
ylabel("amp (dB)", size=16)
xlabel("freq (Hz)", size=16)
yticks(size=16)
xticks(size=16)
xlim(0,5000)
show()
