from pylab import *
from scipy import *

sr = 44100
fo = 441
N = sr/int(fo)
beta = 1.
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
    coefs.append(beta*a[N-i:sr-i]*coefs[i-1])
  else:
    coefs.append(beta*a[N:sr])

b = 1.
for i in a[0:N]:
    b *= i*beta

print b

# filter freq response function
def freq_resp(n,w,coefs,b):
   num = complex(0.,0.)
   N = len(coefs)
   for i in range(0,N):
       a = coefs[i]
       num += a[n]*exp(complex(0.,-w*i))
   return num/(1.-b*exp(complex(0.,-w*N))) 

# calculate mags & phases for w=f0 
mags = zeros(sr)
phs = zeros(sr)
for i in t[0:sr/4]:
    fres = freq_resp(i,w,coefs,b)
    mags[i] = abs(fres)
    phs[i] = arctan2(fres.imag,fres.real)

# generate a signal using AM+PM
ampm = mags*cos(w*t[0:sr]+phs)

# Now we generate the FBAM signal
# it should match the filter
fbam = zeros(sr)
x = a
for n in t[0:sr/4]:
 if n > 0:
  fbam[n] = x[n] + beta*a[n]*fbam[n-1]
 else: fbam[n] = x[n]

xax = 1000.*t[0:500]/sr
xlabel("time (msecs)")
ylabel("amplitude")
plot(xax,ampm[0:500]/max(ampm), "k-")
plot(xax,fbam[0:500]/max(ampm), "k.")
xlim(0, 1000.*500/sr)
grid()
show()
