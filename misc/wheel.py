import pylab

pylab.figure(figsize=(12,5))
c = pylab.cos(2*pylab.pi*pylab.arange(0,1000)/1000)
s = pylab.sin(2*pylab.pi*pylab.arange(0,1000)/1000)
s1 = pylab.sin(2*pylab.pi*pylab.arange(0,1300)/1000)
pi = pylab.pi

pylab.subplot(121)
pylab.ylim(-1.1,1.1)
pylab.xlim(-1.1,1.1)
pylab.axis('off')
pylab.plot(c,s,'k', linewidth=2)
pylab.arrow(-1,0,2-0.1,0, head_width=0) 
pylab.arrow(1,0,-2+0.1,0, head_width=0)
pylab.arrow(0,-1,0,2-0.1, head_width=0.0)
pylab.arrow(0,1,0,-2+0.1, head_width=0.0)
pylab.arrow(0,0,pylab.cos(pi/4),pylab.sin(pi/4), head_width=0) 
pylab.arrow(0,0,-pylab.cos(pi/4),pylab.sin(pi/4), head_width=0)
pylab.arrow(0,0,-pylab.cos(pi/4),-pylab.sin(pi/4), head_width=0) 
pylab.arrow(0,0,pylab.cos(pi/4),-pylab.sin(pi/4), head_width=0)


pylab.vlines(pylab.cos(pi/4), 0, pylab.sin(pi/4), linestyles='dashed')

pylab.plot([1], [0], marker='o', markersize=8)
pylab.plot([pylab.cos(pi/4)], [pylab.sin(pi/4)], marker='o', markersize=8)
pylab.plot([pylab.cos(pi/2)], [pylab.sin(pi/2)], marker='o', markersize=8)
pylab.plot([pylab.cos(3*pi/4)], [pylab.sin(3*pi/4)], marker='o', markersize=8)
pylab.plot([pylab.cos(pi)], [pylab.sin(pi)], marker='o', markersize=8)
pylab.plot([pylab.cos(3*pi/4)], [-pylab.sin(3*pi/4)], marker='o', markersize=8)
pylab.plot([pylab.cos(pi/2)], [-pylab.sin(pi/2)], marker='o', markersize=8)
pylab.plot([pylab.cos(pi/4)], [-pylab.sin(pi/4)], marker='o', markersize=8)


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


pylab.subplot(122)
pylab.axis('off')
pylab.xticks([])
pylab.yticks([])
pylab.axis('off')
pylab.ylim(-1.1,1.1)
pylab.xlim(-0.1,1.1)
pylab.plot(pylab.arange(0,1000)/1000.,s,'k', linewidth=2)
pylab.plot(pylab.arange(0,1300)/1000.,s1,'k:', linewidth=1)
pylab.arrow(0,0,1.7,0, linestyle='dotted')
pylab.plot([0], [0], marker='o', markersize=8)
pylab.plot([1/8], [pylab.sin(pi/4)], marker='o', markersize=8)
pylab.plot([1/4], [pylab.sin(pi/2)], marker='o', markersize=8)
pylab.plot([3/8], [pylab.sin(3*pi/4)], marker='o', markersize=8)
pylab.plot([1/2], [pylab.sin(pi)], marker='o', markersize=8)
pylab.plot([5/8], [-pylab.sin(3*pi/4)], marker='o', markersize=8)
pylab.plot([3/4], [-pylab.sin(pi/2)], marker='o', markersize=8)
pylab.plot([7/8], [-pylab.sin(pi/4)], marker='o', markersize=8)
pylab.plot([1], [0], marker='o', markersize=8)
pylab.vlines(0.125, 0, pylab.sin(pi/4), linestyles='dashed')


pylab.show()
