import pylab as pl
import ctcsound as csound

code = '''
nchnls=2
is = 16384
i1 ftgen 1,0,is,5,0.001,is*0.8,0.001,is*0.2,1
ift vco2init 1,2
instr 1
ift vco2ift p5,0,1/3
aph phasor p5
krt = 0
asig tablei aph*(krt+3.5),ift,1,0,1
asig1 tablei aph,ift,1,0,1
asy tablei aph,1,1,0,1
   out(p4*(1-asy)*asig,p4*asig1)
endin
schedule(1,0,1,0dbfs,60)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
N = int(sr)//10
sig = pl.zeros(N)
n = 0
for i in range(0,int(len(sig)/(2*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1

pl.figure(figsize=(8,3))
pl.title('hard sync')
t = pl.arange(0,N//2)/float(sr)
pl.xlim(0, max(t))
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.plot(t,sig[1::2], 'k--', linewidth=1)
pl.plot(t,sig[0::2])

            
pl.show()
