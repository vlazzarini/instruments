import ctcsound as csound
import pylab as pl

code = '''
instr 1
 out(vco2(p4,p5))
endin
schedule(1,0,1,0dbfs,100)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sig = pl.zeros(cs.ksmps()*88)
n = 0
for i in range(0,88):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1

x = pl.arange(0, len(sig))/cs.sr()        
pl.figure(figsize=(8,3))
pl.xlabel("time (s)")
pl.tight_layout()     
pl.plot(x,sig,'k')
pl.show()
