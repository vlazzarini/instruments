#import pylab as pl
#fig = pl.figure()
#t = pl.arange(0,10000)
#pl.plot(pl.cos(t),pl.sin(t))
#pl.show()

import pylab as pl
import matplotlib
fig = pl.figure(figsize=(8,8))
ax = fig.add_subplot(1, 1, 1)

circ1 = pl.Circle((0, 0), radius=1,linestyle='--', edgecolor='k', facecolor='none')
angle = matplotlib.patches.Wedge((0, 0), 0.1, 0, 45, edgecolor='k', linewidth=1, facecolor='none')

pl.text(0.53,0.53,r'$z = a + jb$', fontsize="16")
pl.text(0.52,0.43,r'$(= Ae^{j\phi})$', fontsize="16")
pl.plot([0.5,0.5],[0.5,0.5], 'ko')
pl.plot([0,0.5],[0,0.5], 'k')

pl.vlines(0,0,0.5, 'k')
pl.text(-0.06,0.48,r'$b$', fontsize="16")
pl.plot([0,0],[0.5,0.5], 'k.')
pl.hlines(0,0,0.5, 'k')
pl.plot([0.499,0.499],[-0.002,-0.002], 'k.')

pl.text(0.48,-0.07,r'$a$', fontsize="16")
pl.vlines(0.5,0,0.5,'k',linestyle='--')
pl.plot([0,0.5],[0.5,0.5],'k--')

pl.text(0.1,0.03, r'$\phi$', fontsize=16)
pl.text(0.21,0.28,r'$A$', fontsize="16")

pos = [pl.cos(pl.pi/4),pl.sin(pl.pi/4)]
pl.text(pos[0]+0.03, pos[1]+.03,r'$e^{j\phi}$', fontsize="16")
pl.plot(pos[0]-0.001,pos[1]-0.001,'ko')

pos = [1,0]
pl.text(pos[0]+0.03, pos[1]+.03,r'$e^{j2\pi}$', fontsize="16")
pl.plot(pos[0],pos[1],'ko')

pos = [0,1]
pl.text(pos[0]+0.03, pos[1]+.03,r'$e^{j\pi/2}$', fontsize="16")
pl.plot(pos[0],pos[1],'ko')

pos = [-1,0]
pl.text(pos[0]-0.12, pos[1]+.03,r'$e^{j\pi}$', fontsize="16")
pl.plot(pos[0],pos[1],'ko')

pos = [0,-1]
pl.text(pos[0]+0.03, pos[1]-.12,r'$e^{j3\pi/2}$', fontsize="16")
pl.plot(pos[0],pos[1],'ko')


pl.text(0.53,-0.48,r'$\overline{z} = a - jb$', fontsize="16")
pl.text(0.52,-0.58,r'$(= Ae^{-j\phi})$', fontsize="16")
pl.plot([0.5,0.5],[-0.5,-0.5], 'ko')


pl.text(-0.615,-0.52,r'$-z$', fontsize="16")
pl.plot([-0.5,-0.5],[-0.5,-0.5], 'ko')

pl.text(-0.615,0.48,r'$-\overline{z}$', fontsize="16")
pl.plot([-0.5,-0.5],[0.5,0.5], 'ko')


ax.add_patch(circ1)
ax.add_patch(angle)
pl.yticks([-1,0,1])
pl.xticks([-1,0,1])
pl.grid(True)

pl.ylim(-1.2, 1.2)
pl.xlim(-1.2, 1.2)
pl.tight_layout()
pl.show()

