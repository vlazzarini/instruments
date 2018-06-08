import ctcsound as csound
import pylab as pl

code = '''
iN = 16384
isf ftgen 1,0,iN,7,-1,iN/4,1,iN/2,0.5,1,-0.5,iN/4-1,-1
ifn vco2init -1, 100,1.05,-1,-1,1
instr 1
 out(vco2(p4,p5,p6))
endin
schedule(1,0,1,0dbfs,100,14)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sig = pl.zeros(int(cs.sr()*2))
n = 0
for i in range(0,int(len(sig)/cs.ksmps())):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1
        
x = pl.arange(0,1000)/cs.sr()        
pl.figure(figsize=(8,6))

pl.subplot(211)

pl.xlim(0,max(x))  
pl.plot(x,sig[:1000],'k')
pl.subplot(212)

pl.subplot(212)
pl.xlim(0,max(x))  
start = cs.sr()
pl.xlabel("time (s)")
pl.plot(x,sig[start:start+1000],'k')


pl.tight_layout()   
pl.show()
