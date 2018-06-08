from pylab import *
from scipy import ndimage

def f(x): return x*0.7 + 0.4*x**5 + 0.2*x**3 + 0.1*x**2 + 0.05*x**4
    
subplot(2,2,1)
t = (2*pi*arange(0, 1000)/1000.)
plot(sin(t),t/(2*pi),  'k', linewidth=2)
plt.axvline(0, color='k', linestyle='--')
xlim(-1.1, 1.1)
ylim(1, 0)

subplot(2,2,3)
t = arange(0.,2000)/1000. - 1.
scal = abs(max(f(t)))
plot(t, f(t)/scal, 'k', linewidth=2)
plt.axvline(0, color='k', linestyle='--')
plt.axhline(0, color='k', linestyle='--')
ylim(-1.1,1.1)
xlim(-1.1,1.1)

subplot(2,2,4)
t = (2*pi*arange(0, 1000)/1000.)
plot(t/(2*pi),f(sin(t))/scal,  'k', linewidth=2)
plt.axhline(0, color='k', linestyle='--')
ylim(-1.1, 1.1)
tight_layout()
show()
