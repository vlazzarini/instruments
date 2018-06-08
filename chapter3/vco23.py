import ctcsound as csound
import pylab as pl

code = '''
instr 1
 out(vco2(p4,p5,p6))
endin
schedule(1,0,1,0dbfs,100,12)
schedule(1,1,1,0dbfs,100,10)
schedule(1,2,1,0dbfs,100,6)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sig = pl.zeros(int(cs.sr()*3))
n = 0
for i in range(0,int(len(sig)/cs.ksmps())):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1
        
x = pl.arange(0,1000)/cs.sr()        
pl.figure(figsize=(8,6))

pl.subplot(311)

pl.xlim(0,max(x))  
pl.plot(x,sig[:1000],'k')
pl.subplot(312)

pl.xlim(0,max(x))  
start = cs.sr()
pl.plot(x,sig[start:start+1000],'k')
pl.subplot(313)

pl.ylim(-.1,1.1)
pl.xlim(0,max(x))  
start = cs.sr()*2
scal = max(sig[start:start+1000])
pl.plot(x,sig[start:start+1000]/scal,'k')
pl.xlabel("time (s)")
pl.tight_layout()   
pl.show()
