##################################################
#
# copyright (c)Victor Lazzarini, 2008
#
# Free Software, licensed by the GNU Public License
###################################################
from pylab import *
from scipy.signal import *
from scipy.io import wavfile
import os
import sys
import ctcsound as csound

code = '''
sr = 44100
0dbfs = 1
nchnls = 1

instr 1
 setksmps(1)
 aout init 0
 ib = p6/($M_PI*p5)
 as  = diskin:a("flutec3.wav",p5/cpspch(9.00))
 kb = ib; linen(ib,0.1,p3,0.4)
 adt = kb*(1-aout)/2 + 2/sr
 adp  = delayr:a(1) 
 aout = deltap3(adt) 
    delayw(as)
 asig = 1
       out(aout*asig) 
endin
schedule(1,0,5,0dbfs/2,440,0.7)
'''

N=32768
figure(figsize=(8,5))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sigs = zeros(7*sr)
n = 0
for i in range(0,int(len(sigs)/(cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1


sig = sigs/max(abs(sigs))
# output(name,sig)

win = hanning(N)
spec = fft(win*sig[sr:N+sr])
mags = sqrt(spec[0:N/2].real**2 + spec[0:N/2].imag**2)
scal = N*sqrt(mean(win**2))

# DFT dB mags plot
subplot(211)
x = arange(0,N/2)
bins = x*sr/N
mags = mags/max(abs(mags))
plot(bins, 20*log10(mags), 'k-')
yticks([0, -30, -60])
xticks(arange(3)*5000)
xlim(0,20000)
ylim(-60,0)
ylabel("amp (dB)", size=16)
xlabel("freq", size=16)

# waveform plot
subplot(212)
end = 441
s = sig[sr:441+sr]
plot(x[0:end]/sr,s/abs(max(s)),'k-')
yticks()
ylabel("amp", size=16)
xlabel("time", size=16)

ylim(-1.1,1.1)

tight_layout()
show()
