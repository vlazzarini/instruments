from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import *
from pylab import *
from scipy.io import wavfile
name = sys.argv[1]
(sr,sig) = wavfile.read(name)
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
