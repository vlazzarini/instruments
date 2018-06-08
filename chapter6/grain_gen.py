import pylab as pl
import ctcsound as csound

code = '''
ksmps=1
instr 1
irt = p6/p5
a1   = phasor(p5,p9)
aenv = tablei:a(a1,p8,1,0,1)
asig = tablei:a(a1*irt,p7,1,0,1)
   out(p4*asig*aenv)
endin
;if3 = ftgen(0,0,16384,20,6,1)
if3 = ftgen(0,0,16384,7,1,16384,1)
schedule(1,0,60,0dbfs/2,150,2000,-1,if3,0)
;schedule(1,0,60,0dbfs/2,150,2000,-1,if3,0.5)
'''


N=16384

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sig = pl.zeros(sr)
n = 0
for i in range(0,int(len(sig)/(cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1

    
    
pl.figure(figsize=(8,5))

pl.subplot(211)
pl.yticks([])
pl.xlabel("time (s)")
start = 0
end = 880      
pl.plot(pl.arange(0,end)/sr,sig[start:start+end], 'k-')


N = 32768
start = 0
x = pl.arange(0,N/2)
bins = x*sr/N
win = pl.hanning(N)
scal = N*pl.sqrt(pl.mean(win**2))
sig1 = sig[start:N+start]
window = pl.fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*pl.log10(mags/max(mags))

pl.subplot(212)
pl.xlim(0,20000)
pl.plot(bins,spec[0:N/2], 'k-')
pl.ylim(-60, 1)
#pl.ylabel("amp (dB)", size=16)
pl.yticks([])
pl.xlabel("freq (Hz)", size=16)
pl.xticks()


pl.tight_layout()
pl.show()

