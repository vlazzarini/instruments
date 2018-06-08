from pylab import *
import ctcsound as csound

N = 2**24


code = '''
instr 1
a1 rand p4
   out a1
endin
schedule(1,0,2,0dbfs)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sig = zeros(N+1)
n = 0
for i in range(0,int(len(sig)/cs.ksmps())):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1
        
sr = int(cs.sr())
subplot(211)
start = 0
x = arange(0,N/2)
bins = x*sr/N
win = hanning(N)
scal = N*sqrt(mean(win**2))
sig1 = sig[start:N+start]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
logm = log(mags)
ceps = rfft(logm)
ceps2 = zeros(len(ceps))
ceps2[0:60] = ceps[0:60]
specenv = exp(irfft(ceps2))
spec1 = 20*log10(specenv/max(specenv))
plot(bins[0:N/2],spec1[0:N/2], 'k-', linewidth=2)
ylim(-30, 1)
ylabel("amp (dB)")
xlabel("freq (Hz)")
yticks(size=16)
xticks(size=16)
xlim(0,20000)

subplot(212)
t = arange(0,N)/float(sr)
xlim(0, t[N-1])
ylim(-1.1,1.1)
plot(t,sig[0:N], 'k')


show()
