import pylab as pl
import ctcsound as csound

code = '''
nchnls = 3
0dbfs=1
instr 1
 a1 = oscili(p6,p7)
 a2 = oscili(p4,p5)
 out(a2*a1,a2,a1)
endin
schedule(1,0,1,0dbfs,400,0dbfs,300)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
N = int(sr)*3
sig = pl.zeros(N)
n = 0
for i in range(0,int(len(sig)/(3*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1


pl.figure(figsize=(8,3))
pl.title('RM')
t = pl.arange(0,882)/float(sr)
pl.xlim(0, max(t))
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.plot(t,sig[0:len(t)*3:3], linewidth=2)
pl.plot(t,sig[1:len(t)*3+1:3], 'k')
pl.plot(t,sig[2:len(t)*3+2:3], 'k', ls='dotted')
               

pl.show()
