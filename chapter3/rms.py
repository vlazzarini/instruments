import pylab as pl

def rms(sig):
    sum = 0.0
    for samp in sig:
        sum += samp**2
    return pl.sqrt(sum/len(sig))

end = 1000
t = pl.arange(0,end)
print(rms(pl.sin(2*pl.pi*t/end)))  
