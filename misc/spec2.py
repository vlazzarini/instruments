from pylab import *
from scipy.io import wavfile 
import sys
name1 = sys.argv[1]
name2 = sys.argv[2]
N=16384

figure(figsize=(8,5))
subplot(2,1,1)
(sr,sig) = wavfile.read(name1)
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
ylim(-60,3)
ylabel("amp", size=16)
yticks([])
xticks(arange(4)*5000, ['','',''])
xlim(0,20000)


subplot(2,1,2)
(sr,sig) = wavfile.read(name2)
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
ylim(-60,3)
ylabel("amp ", size=16)
xlabel("freq (Hz)", size=16)
yticks([])
xticks(arange(4)*5000)
xlim(0,20000)

tight_layout()
show()
