import pylab as pl

def reorder(s):
    N = len(s)
    o = s.copy()
    j = 0
    for i in range(0,N-N//4):
      if j > i:
        o[i] = s[j]
        o[j] = s[i]
      m = N//2
      while m >= 2 and j >= m:
        j -= m
        m = m//2 
      j += m
      #print(o)

    return o

s = pl.arange(0,64)
d = reorder(s)
print(d)
