import pylab as pl
import ctcsound as csound

code = '''
nchnls = 2
0dbfs=1
instr 1
 asig1 = linen(1,0.1,p3,0.5)
 asig2 = adsr(0.1,0.2,0.7,0.1)
 out(asig2,asig1)
endin
schedule(1,0,1)
instr 2
 asig1 = linen(1,0.1,p3,0.5)*oscili(1,p4)
 asig2 = adsr(0.1,0.2,0.7,0.1)*oscili(1,p4)
 out(asig2,asig1)
endin
schedule(2,1,1,100)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
N = int(sr)*4
sig = pl.zeros(N)
n = 0
for i in range(0,int(len(sig)/(2*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1


pl.figure(figsize=(8,5))
pl.subplot(211)
pl.title('trapezoidal')
t = pl.arange(0,len(sig)/4)/float(sr)
pl.xlim(0, max(t))
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.plot(t,sig[1:sr*2+1:2], 'k')
pl.plot(t,sig[sr*2+1::2])
               
pl.subplot(212)
pl.title('ADSR')
t = pl.arange(0,len(sig)/4)/float(sr)
pl.xlim(0, max(t))
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.tight_layout()
pl.plot(t,sig[0:sr*2:2], 'k')
pl.plot(t,sig[sr*2::2])

pl.show()
