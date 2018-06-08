from pylab import *
from scipy.io import wavfile
import sys
name = sys.argv[1]

def rms(sig):
    sum = 0.0
    for samp in sig:
        sum += samp**2
    return sqrt(sum/len(sig))


figure(figsize=(8,3))
(sr,sig) = wavfile.read(name)

sig = sig/max(sig)
plot(arange(0,len(sig))/float(sr), sig, 'k', linewidth=1)
N = 256
env = zeros(len(sig))
for i in range(0,len(sig),N):
    r = rms(sig[i:i+N])
    for n in range(0,N):
       env[i+n] = r
       
plot(arange(0,len(sig))/float(sr), env, linewidth=2)
ylim(-1.1, 1.1)
xticks([])
tight_layout()
show()
