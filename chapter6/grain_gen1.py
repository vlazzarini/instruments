import pylab as pl
from scipy import signal
import ctcsound as csound

code = '''
ksmps=1
instr 1
 aenv = poscil(p4,1/p3,p7)
 asig = poscil(aenv,p5,p6)
   out(asig)
endin
if1 = ftgen(0,0,16384,20,2,1)
if2 = ftgen(0,0,16384,20,3,1)
if3 = ftgen(0,0,16384,20,6,1)

icnt init 0
ist init 0
igs = 0.025
iv = 1
iv2 = 200
while icnt < 2000 do
   ifi = iv + rnd(iv)
   igf = iv2 + rnd(iv2)
   schedule(1,ist,igs,0dbfs/4,igf,-1,if1)
   ist += 1/ifi
   icnt += 1
   iv += 0.1
   iv2 += 1
od
'''


N=16384

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sig = pl.zeros(sr*20)
n = 0
for i in range(0,int(len(sig)/(cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1

    
    
pl.figure(figsize=(8,3))

pl.ylabel("freq (Hz)", size=16)
pl.xlabel("time (s)",size=16)

pl.specgram(sig[0:12*sr],1024,sr)
#pl.pcolormesh(t, f, Scc)
#pl.plot(bins,spec[0:N/2], 'k-')
#pl.ylim(-60, 1)
#pl.ylabel("amp (dB)", size=16)
#pl.yticks([])
#pl.xlabel("freq (Hz)", size=16)
#pl.xticks()
pl.xlim(0,1)
pl.ylim(0,10000)

pl.tight_layout()
pl.show()

