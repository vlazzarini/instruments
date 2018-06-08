from pylab import *
from scipy import *

sr = 44100
fo = 441.
N = sr/int(fo)
t = arange(sr+N)
w = 2*pi*fo/sr
a = cos(w*t)
z = zeros(sr+N)
y = zeros(sr+N)

coefs  = []
# 1st coef is 1 
# this creates the coefficient signals
# recursively
coefs.append(ones(sr+N))
for i in range(1, N):
  if i > 1:
    coefs.append(a[N-i:sr-i]*coefs[i-1])
  else:
    coefs.append(a[N:sr])

b = 1.
for i in a[0:N]:
    b *= i

# filter
x = a
for n in t[0:sr/4]:
   for k in range(0,N):
      c = coefs[k]
      if n-k < 0:
         s = 0.0
      else: s = x[n-k]
      z[n] += c[n]*s
   if n-N > 0:  
       y[n] = z[n] + b*y[n-N]
   else: 
       y[n] = z[n]

# Now we generate the FBAM signal
# it should match the filter
fbam = zeros(sr)
for n in t[0:sr/4]:
 if n > 0:
  fbam[n] = x[n] + a[n]*fbam[n-1]
 else: fbam[n] = x[n]
xax = 1000.*t[0:500]/sr
xlabel("time (msecs)")
ylabel("amplitude")
plot(xax,y[0:500]/max(y),"k-")
plot(xax,fbam[0:500]/max(fbam),"k.")
xlim(0, 1000.*500/sr)
grid()
show()
