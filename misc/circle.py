#import pylab as pl
#fig = pl.figure()
#t = pl.arange(0,10000)
#pl.plot(pl.cos(t),pl.sin(t))
#pl.show()

import pylab as pl
import matplotlib
fig = pl.figure(figsize=(6,6))
ax = fig.add_subplot(1, 1, 1)
pl.text(0.72, 0.42, r'$r=1$', fontsize=16)

pl.text(1, 1, r'$\frac{\pi}{2}$', fontsize=24)
pl.text(0.5*pl.cos(pl.pi/4)+0.51,0.5*pl.sin(pl.pi/4)+0.5, r'$b$', fontsize=16)
pl.text(1.01,0.51, r'$a$', fontsize=16)
pl.text(1.04, 1, r'$rad$', fontsize=12)
circ1 = pl.Circle((0.5, 0.5), radius=0.5, edgecolor='k', facecolor='none')
angle = matplotlib.patches.Wedge((0.5, 0.5), 0.5, 0, 45, edgecolor='k', linewidth=2, facecolor='none')
angle2 = matplotlib.patches.Wedge((0.5, 0.5), 0.65, 0, 90, linestyle='--', edgecolor='k', linewidth=2, facecolor='none')
ax.add_patch(circ1)
ax.add_patch(angle)
ax.add_patch(angle2)
pl.plot([0.5*pl.cos(pl.pi/4)+0.5,0.5*pl.sin(pl.pi/4)+0.5], [0.5*pl.cos(pl.pi/4)+0.5,0.5*pl.sin(pl.pi/4)+0.5],'ko')
pl.plot([1,1], [0.5,0.5],'ko')
pl.text(0.97, 0.7, r'$\overline{ab}=\frac{\pi}{4}$', fontsize=16)
pl.yticks([0,0.5,1],['','',''])
pl.xticks([0,0.5,1],['','',''])
pl.grid(True)

pl.ylim(-.17, 1.17)
pl.xlim(-.17, 1.17)
pl.tight_layout()
pl.show()

