import pylab as pl
import ctcsound as csound

code = '''
nchnls = 2
0dbfs=1
instr 1
 a1 = oscili(p6,p7)
 out(oscili(p4,p5+a1),a1)
endin
schedule(1,0,1,0dbfs/2,100,50,5)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
N = int(sr)
sig = pl.zeros(N)
n = 0
for i in range(0,int(len(sig)/(2*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1


pl.figure(figsize=(8,3))
pl.title('FM')
t = pl.arange(0,len(sig)/2)/float(sr)
pl.xlim(0, max(t))
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.plot(t,sig[0::2])
pl.plot(t,sig[1::2]/50, 'k', linewidth=2)

               

pl.show()
