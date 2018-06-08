from pylab import *
import ctcsound as csound

code = '''
sr = 44100
0dbfs = 1
nchnls = 2
gifbam faustcompile {{
beta = hslider("beta", 0, 0, 10, 0.001);
fbam(b) = ((+(1))*(_)~*(b));              
process = fbam(beta);
}}, "-vec -lv 1"

instr 1
ain = diskin:a("flutec3.wav",p5/cpspch(9.00))
ib,asig faustaudio gifbam,ain
kb = p6
faustctl(ib,"beta",kb)
asig = balance(asig,ain)
     out(ain,asig*p4)
endin
schedule(1,0,7,1,440,3)
'''


N=32768
figure(figsize=(8,5))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sigs = zeros(7*sr*2)
n = 0
for i in range(0,int(len(sigs)/(4*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1

win = zeros(N)+1 #hanning(N)
subplot(2,1,1)
title('Original')
st = 44100
sig = sigs[st:st+2*N:2]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=1)
ylim(-60,1)
ylabel("amp", size=16)
yticks([])
xticks([])
xlim(0,20000)


subplot(2,1,2)
title('Adaptive FBAM')
sig = sigs[st+1:st+2*N+1:2]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=1)
ylim(-60,1)
ylabel("amp", size=16)
xlabel("freq", size=16)
yticks([])
xticks(arange(3)*10000)
xlim(0,20000)
tight_layout()
show()
