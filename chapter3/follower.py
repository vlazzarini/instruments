import pylab as pl
import ctcsound as csound

code = '''
nchnls = 2
gSname = "/Users/victor/audio/pianoc2.wav"
instr 1
 asig = diskin:a(gSname)*2
 k1  = rms(asig)*2
 out(oscili(k1,p4),asig)
endin
schedule(1,0,filelen(gSname),500)
'''

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
N = int(sr*7*2)
sig = pl.zeros(N)
n = 0
for i in range(0,int(len(sig)/(2*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1


pl.figure(figsize=(8,5))
pl.subplot(211)
pl.title('original')
t = pl.arange(0,len(sig)/2)/float(sr)
pl.xlim(0, max(t))
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.plot(t,sig[1::2], 'k')
               
pl.subplot(212)
start = int(sr)
pl.title('envelope-followed sine')
t = pl.arange(0,len(sig)/2)/float(sr)
pl.xlim(0, max(t))
pl.ylim(-1.1,1.1)
pl.xlabel("time (s)")
pl.tight_layout()
pl.plot(t,sig[0::2], 'k')

pl.show()
