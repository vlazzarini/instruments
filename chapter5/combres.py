from pylab import *
from scipy.io import wavfile 
import sys

figure(figsize=(8,3))
N=32768
sr = 40000
win = zeros(N)+1 #hanning(N)
start = 0 
#subplot(2,1,1)
sig = zeros(sr)
sig[0] = 1.0
end = 40
print  float(sr)/end 
dela = zeros(end)
g = 0.99
pos = 0
for i in range(0,sr): 
    out = dela[pos]
    dela[pos] = sig[i] + dela[pos]*g
    sig[i] = out
    if pos == end-1 : pos= 0
    else: pos+=1

x = arange(0,1000)
#(markerLines, stemLines, baseLines) = stem(x/40000., sig[0:1000], linefmt='k-', markerfmt='k')
#setp(stemLines,linewidth=2)
#setp(baseLines,color='black')
#setp(markerLines,markersize = 0)
#ylabel("amp", size=16)
#xlabel("time (sec)", size=16)
#ylim(0,1.1)
#xticks([0.001,0.005,0.010,0.015,0.020])
#yticks([])
#plt.axvline(5000, color='k', linestyle='--')



#subplot(2,1,2)
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[start:N+start]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-50,3)
xlim(0,20000)
ylabel("amp", size=16)
xlabel("freq (Hz)", size=16)
yticks([])
xticks([])
xticks(arange(1,4)*5000)

tight_layout()
show()
