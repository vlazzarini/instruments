from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import *

fig = plt.figure()
ax = axes3d.Axes3D(fig)

x = np.linspace(0, 10, 100)
for i in range(0,6):
 z = jn(i,x)
 ax.plot(x, np.zeros(len(x))+i, z, zdir='z', color='k', linewidth=2)

ax.set_xlim3d(0, 10)
ax.set_xticks(np.arange(0,10))
ax.set_ylim3d(0, 5)
ax.set_zlim3d(-0.6, 1)

ax.set_xlabel("index $I$")
ax.set_ylabel("order n")
ax.set_yticklabels(['0','1','2','3','4','5'])
plt.show()
