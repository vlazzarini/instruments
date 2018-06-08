import sys
from scipy import *
from pylab import *
from scipy.io import wavfile


# read impulse and signal input
(sr,impulse) = wavfile.read(sys.argv[1])
(sr,signalin) = wavfile.read(sys.argv[2])

S = len(impulse) # impulse length
L = len(signalin) # signal length
print S
print L

# find fftsize as the next power of 2
# beyond S*2-1
N = 2
while(N <= S*2-1): N *= 2

# signal blocks for FFT
imp = zeros(N)
sig = zeros(N)

# output signal & amplitude
sigout = zeros(L+S-1)
amp = max(signalin)

# copy impulse for FFT
imp[0:S] = impulse/32768.
spec_imp = rfft(imp)

p = 0
for i in range(0, L/S):
   sig[0:S] = signalin[p:p+S]/32768.0 # get block from input
   # perform convolution and overlap-add
   a =  irfft(spec_imp*rfft(sig))
   sigout[p:p+2*S] += a[0:2*S]
   p += S

#  write file to output, scaling it to original amp
wavfile.write(sys.argv[3],sr,array(sigout*amp, dtype='int16'))

