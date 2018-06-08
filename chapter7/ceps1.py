from pylab import *
from scipy.io import wavfile 
import numpy
import sys
name = sys.argv[1]

# for true envelope set jutsceps = False
(sr,sig) = wavfile.read(name)
N = 2048
coefs =20
start = sr#0#int(0.1*sr)
x = arange(0,N)
bins = x*sr/N
win = hanning(N)
scal = N*sqrt(mean(win**2))
sig1 = sig[start:N+start]
slice = fft(sig1*win)
mags = abs(slice/scal)
lmags = log(mags[:N/2])
thresh = 0.1*log(10)
go = True
justceps = False
while(go):
 go = False
 ceps = ifft(lmags)
 for i in x[:N/2]:
     if(i > coefs and i < N/2-coefs): ceps[i] = 0.0
 form = fft(ceps).real
 if (justceps): break
 for i in x[:N/2]:
      if lmags[i] < form[i]: lmags[i] = form[i]
      diff = (log(mags[i]) - form[i])
      if diff  >  thresh: 
        go = True
figure(figsize=(8,3))
form = exp(form)
formdb = 20*log10(form[0:N/3])
magsdb = 20*log10(mags[0:N/3])
maxf = max(formdb)
maxm = max(magsdb)
if maxf > maxm: maxa = maxf
else: maxa = maxm
plot(bins[0:N/3],formdb[0:N/3]/max(formdb), color='black', linewidth=2)
plot(bins[0:N/3],magsdb[0:N/3]/max(magsdb),color='blue')
#ylim(-50, 1)
yticks([])
xlim(0, bins[N/3])
tight_layout()
show()
