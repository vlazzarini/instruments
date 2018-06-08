import pylab as pl
import ctcsound as csound

code = '''
0dbfs = 1
instr 1
 a1 oscili 1,p6
 out(randi(p4,p5)*a1)
endin
schedule(1,0,2,0dbfs,500,1000)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
N = 8192
sr = cs.sr()
sig = pl.zeros(N)
n = 0
for i in range(0,int(len(sig)/cs.ksmps())):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1

pl.figure(figsize=(8,3))
pl.title('Noise RM spectrum')
x = pl.arange(0,N/2)
bins = x*sr/N
spec = pl.fft(sig/max(sig))
mags = abs(spec/N)
logm = pl.log(mags)
ceps = pl.rfft(logm)
ceps2 = pl.zeros(len(ceps))
ceps2[0:50] = ceps[0:50]
specenv = pl.exp(pl.irfft(ceps2))
spec1 = 20*pl.log10(mags/max(mags))

pl.ylim(-60, 1)
pl.ylabel("amp (dB)")
pl.xlabel("freq (Hz)")
pl.xlim(0,2000)
pl.tight_layout()
pl.plot(bins[0:N/2],spec1[0:N/2], 'k-', linewidth=2)
pl.show()
