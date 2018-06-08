from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import *
from pylab import *
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
while icnt < 6000 do
   ifi = 300 + rnd(300)
   igf = 1000 + rnd(2000)
   schedule(1,ist,igs,0dbfs/4,igf,-1,if3)
   ist += 1/ifi
   icnt += 1
od
'''


N=16384

cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sig = zeros(sr*2)
n = 0
for i in range(0,int(len(sig)/(cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sig[n] = i/cs.get0dBFS()
        n+=1

    
    
N = 1024
hop = N/4
start = 0

fig = plt.figure()
ax = axes3d.Axes3D(fig)

x = np.linspace(N/4, 16, N/4)
for i in range(0,16):
 slice = sig[i*hop:N+i*hop]*hanning(N)
 ft = abs(fft(slice)[N/2:N/2+N/4])
 z = ft/max(ft)
 bins = x*sr/N
 ax.plot(bins, np.zeros(len(x))+i*float(hop)/sr, z, zdir='z', color='k', linewidth=1)

ax.set_xlim3d(0, sr/4)
#ax.set_xticks(np.arange(0,10))
#ax.set_ylim3d(0, 16*hop/sr)
#ax.set_zlim3d(0, 1)

ax.set_xlabel("frequency", size=16)
ax.set_ylabel("time", size=16)
#ax.set_zlabel("amp", size=16)
ax.set_yticks(np.arange(1,15,4)*float(hop)/sr)
ax.set_xticks(np.arange(0,5)*2500)

plt.show()

