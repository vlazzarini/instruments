#
# FBAM as FIR+IIR cascade
#
from numpy import pi,cos
from scipy.signal import *
from pylab import *

f0 = 2*500.
fs = 44100.
w = 2*pi*f0/fs
N = int(fs/f0)
t = arange(0,4,f0/fs)

a = cos(2*pi*t)   # coefficients
x = cos(2*pi*t)   # input
B = 1             # beta


# -- straight FBAM
fbam = zeros(len(t))
fbam[0] = x[0]
for n in range(1,len(t)):
   fbam[n] = x[n] + B*a[n]*fbam[n-1]

# -- FIR coefficients
def b(k,n):
   bk = 1
   for m in range(1,k+1):
      bk *= B*cos(w*(n-m+1))
   return bk

# -- recursive part
aN = prod(B*a[1:N+1])

# -- equivalent filter
pltv = zeros(len(t))
for n in range(0,len(t)):
   xz = 0
   for k in range(1,N+1):
      if (n-k) >= 0:
         xz += b(k,n)*x[n-k]
   if (n-N) > 0:  yz = aN*pltv[n-N]
   else:          yz = 0
   pltv[n] = x[n] + xz + yz


# -- plotting
fig = figure()
plot(t,fbam,'r--',lw=2)
plot(t,pltv,'k:',lw=2)
grid(True)

show()
