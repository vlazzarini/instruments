import pylab as pl
import ctcsound as csound

code = '''
instr 1
 out(rand:a(p4))
endin
schedule(1,0,2,0dbfs)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
N = 2**15
sr = cs.sr()
sig = pl.zeros(N)
n = 0
for i in range(0,int(len(sig)/cs.ksmps())):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1

pl.figure(figsize=(8,5))
pl.subplot(211)
pl.title('waveform')
end = sr/4
t = pl.arange(0,end)/float(sr)
pl.xlim(0, t[end-1])
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.plot(t,sig[0:end], 'k')
               
pl.subplot(212)
pl.title('spectrum')
x = pl.arange(0,N/2)
bins = x*sr/N
spec = pl.fft(sig/max(sig))
mags = abs(spec/N)
spec = 20*pl.log10(mags/max(mags))


pl.ylim(-60, 1)
pl.ylabel("amp (dB)")
pl.xlabel("freq (Hz)")
pl.xlim(0,20000)
pl.tight_layout()
pl.plot(bins[0:N/2],spec[0:N/2], 'k-')
pl.show()
