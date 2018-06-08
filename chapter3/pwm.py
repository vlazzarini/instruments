import pylab as pl
import ctcsound as csound

code = '''
nchnls = 2
0dbfs=1
instr 1
 a1 = vco2(p4,p5,2,0.5)
 a2 = vco2(p4,p5,2,0.1)
 out(a1,a2)
endin
schedule(1,0,1,0dbfs*.9,60)
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
pl.title('PWM')
t = pl.arange(0,N//2)/float(sr)
pl.xlim(0, max(t))
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.plot(t,sig[1::2], 'k--', linewidth=2)
pl.plot(t,sig[0::2])

               

pl.show()
