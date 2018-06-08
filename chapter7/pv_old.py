# phase vocoder example
# (c) V Lazzarini, 2010
# GNU Public License
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import sys
from scipy import *
from pylab import *
from scipy.io import wavfile

N = 2048
H = N/4

# read input and get the timescale factor
(sr,signalin) = wavfile.read(sys.argv[2])
L = len(signalin)
tscale = float(sys.argv[1])

# signal blocks for processing and output
phi2,phi  = zeros(N//2+1),zeros(N//2+1)+0j
out = zeros(N//2+1, dtype=complex)
sigout = zeros(L/tscale+N)

# max input amp, window
amp = max(signalin)
win = hanning(N) 

p1 = 0
p2 = 0
p = 0
pp = 0
while p < L-(N+H): 
   # take the spectra of two consecutive windows
   p1 = int(p)
   spec1 =  rfft(win*signalin[p1:p1+N])
   spec2 =  rfft(win*signalin[p1+H:p1+N+H])
   # take their phase difference and integrate
   diff = (angle(spec2) - angle(spec1))
   phi  = exp(1j*phi2)
           
   for i in range(0,N//2+1):
       if(i == 0):
        phi2[i] = angle(phi[i]-phi[i+1])
       elif(i ==  N//2):
        phi2[i] = angle(phi[i]-phi[i-1])
       else:
        phi2[i] = angle(-phi[i-1]+phi[i]-phi[i+1])
        
   phi2 += diff
   out.real, out.imag = cos(phi2), sin(phi2)
   # inverse FFT and overlap-add
   sigout[pp:pp+N] += win*irfft(abs(spec2)*out)
   pp += H
   p += H*tscale

#  write file to output, scaling it to original amp
wavfile.write(sys.argv[3],sr,array(amp*sigout/max(sigout), dtype='int16'))

#  play it using a libsndfile utility
import os
try:
 os.spawnlp(os.P_WAIT, 'sndfile-play', 'sndfile-play', sys.argv[3])
except:
 pass
