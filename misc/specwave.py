from pylab import *
from scipy.io import wavfile 
import sys
name = sys.argv[1]
figure(figsize=(8,5))
(sr,sig) = wavfile.read(name)
N = 2048
start = 0
dur = sr/20
subplot(211)
plot(sig[start:dur+start], 'k', linewidth=2)
ylabel("amplitude", size=16)
xlabel("time (secs)", size=16)
xlim(0,dur)
ylim(-1.1, 1.1)
xticks([0,dur/2,dur], [0, '%.3f' % (dur/(2.*sr)), '%.2f' % (dur/float(sr))])
subplot(212)
specgram(sig[0:sr*2],2048,sr,noverlap=256,cmap=cm.Greys)
yticks([2500,5000,7500,10000,12500,15000], ['2.5', '5', '7.5', '10', '12.5', '15'])
ylim(0,15000)
xlim(0,dur/float(sr))
ylabel("frequency (kHz)", size=16)
xlabel("time (secs)", size=16)
tight_layout()
show()
