from pylab import *
from scipy.io import wavfile 
import sys
name = sys.argv[1]
figure(figsize=(8,3))
(sr,sig) = wavfile.read(name)
N = 2048
start = 0
specgram(sig[0:sr*2],2048,sr,noverlap=256)
#colorbar(ticks=[0,-12,-24,-36,-48,-60,-72,-84,-96])
#ylim(0,5000)
#clim(-96,0)
#xlabel("time (s)", size=16)
#ylabel("freq (Hz)", size=16)
#xticks([0.2,0.4,0.6,0.8], size=16)
yticks(size=16)
#specgram(sig[0:sr],N,sr,noverlap=256,mode='magnitude',cmap=cm.gray)
yticks([2500,5000,7500], ['2.5', '5', '7.5'])
ylim(0,5000)
xlim(0,1.0)
ylabel("frequency (kHz)", size=16)
xlabel("time (secs)", size=16)
tight_layout()
show()
