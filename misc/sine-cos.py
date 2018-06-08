import pylab

fig = pylab.figure(figsize=(8,8))
c = pylab.cos(4*pylab.pi*pylab.arange(0,1000)/1000)
s = pylab.sin(4*pylab.pi*pylab.arange(0,1000)/1000)
c1 = pylab.cos(4*pylab.pi*pylab.arange(0,1750)/1000)
s1 = pylab.sin(4*pylab.pi*pylab.arange(0,1750)/1000)


pylab.subplot(221)

pylab.axis('off')
pylab.xticks([])
pylab.yticks([])
pylab.xlim(-1.1,1.1)
pylab.ylim(-0.3,2)
pylab.plot(c, pylab.arange(0,1000)/1000., 'k',linewidth=2)
pylab.plot(c1, pylab.arange(0,1750)/1000., 'k:', linewidth=1)
pylab.arrow(0,0,0,1.7, linestyle='dotted')
pylab.arrow(1,-0.2,-2,0) 
pylab.arrow(-1,-0.2,2,0) 

pylab.subplot(224)
pylab.axis('off')
pylab.xticks([])
pylab.yticks([])
pylab.axis('off')
pylab.xlim(-0.3,2)
pylab.ylim(-1.1,1.1)
pylab.plot(pylab.arange(0,1000)/1000.,s,'k', linewidth=2)
pylab.plot(pylab.arange(0,1750)/1000.,s1,'k:', linewidth=1)
pylab.arrow(0,0,1.7,0, linestyle='dotted')
pylab.arrow(-0.2,-1,0,2) 
pylab.arrow(-0.2,1,0,-2) 

pylab.subplot(223)
pylab.ylim(-1.1,1.1)
pylab.xlim(-1.1,1.1)
pylab.axis('off')
pylab.plot(c,s,'k', linewidth=2)
pylab.arrow(-1,0,2,0, linestyle='dotted') 
pylab.arrow(1,0,-2,0, linestyle='dotted')
pylab.arrow(0,-1,0,2, linestyle='dotted') 
pylab.arrow(0,1,0,-2, linestyle='dotted')

pylab.annotate('',
            xy=(pylab.pi/8.+0.1,1),      # theta, radius
            xytext=(pylab.pi/8-0.1,1),   # theta, radius
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)

pylab.annotate('',
            xy=(3*pylab.pi/8.+0.1,1),      # theta, radius
            xytext=(3*pylab.pi/8-0.1,1),   # theta, radius
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)

pylab.annotate('',
            xy=(5*pylab.pi/8.+0.1,1),      # theta, radius
            xytext=(5*pylab.pi/8-0.1,1),   # theta, radius
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)

pylab.annotate('',
            xy=(7*pylab.pi/8.+0.1,1),      # theta, radius
            xytext=(7*pylab.pi/8-0.1,1),   # theta, radius
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)

pylab.annotate('',
            xy=(9*pylab.pi/8.+0.1,1),      # theta, radius
            xytext=(9*pylab.pi/8-0.1,1),   # theta, radius
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)

pylab.annotate('',
            xy=(11*pylab.pi/8.+0.1,1),      # theta, radius
            xytext=(11*pylab.pi/8-0.1,1),   # theta, radius
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)

pylab.annotate('',
            xy=(13*pylab.pi/8.+0.1,1),      # theta, radius
            xytext=(13*pylab.pi/8-0.1,1),   # theta, radius
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)

pylab.annotate('',
            xy=(15*pylab.pi/8.+0.1,1),      # theta, radius
            xytext=(15*pylab.pi/8-0.1,1),   # theta, radius
            xycoords='polar',
            textcoords='polar',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            clip_on=True)

pylab.show()
