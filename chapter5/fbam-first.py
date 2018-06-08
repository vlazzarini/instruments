from pylab import *
from scipy import *

sr = 44100
fo = 441.
N = sr/int(fo)
t = arange(sr+N)
w = 2*pi*fo/sr
a = cos(w*t)
beta = 1.0
z = zeros(sr+N)
y = zeros(sr+N)
tmp = zeros(sr+N)

coefs  = []
# 1st coef is 1 
# this creates the coefficient signals
# recursively
coefs.append(ones(sr+N))
for i in range(1, N):
  if i > 1:
    coefs.append(beta*a[N-i:sr-i]*coefs[i-1])
  else:
    coefs.append(beta*a[N:sr])

b = 1.
for i in a[0:N]:
    b *= i*beta

# filter
x = a
for n in t[0:sr/4]:
   tmp[n] = x[n-1] - x[n]
   for k in range(0,N):
      c = coefs[k]
      if n-k < 0:
         s = 0.0
      else: s = tmp[n-k]
      if (n-k-1) < 0:
         s1 = 0.0
      else: s1 = tmp[n-k-1]
      z[n] += -c[n]*s 

   if n-N > 0:  
       y[n] = z[n] + b*y[n-N]
   else: 
       y[n] = z[n]

# Now we generate the FBAM signal
# it should match the filter
x = a
fbam = zeros(sr)
for n in t[0:sr/4]:
 if n > 0:
  fbam[n] = x[n-1] - x[n] - x[n]*fbam[n-1]
 else: fbam[n] = x[n]
xax = 1000.*t[0:500]/sr
xlabel("time (msecs)")
ylabel("amplitude")
plot(xax,y[0:500],"k-")
plot(xax,fbam[0:500],"k.")
xlim(0, 1000.*500/sr)
grid()
show()
