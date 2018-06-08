from pylab import *
import ctcsound as csound

code = '''
sr = 40000
0dbfs = 1
ksmps = 1
nchnls = 4
opcode Filter,a,akk
 as,kf,kbw xin
 as = reson(as,kf,kbw,1)
 as = reson(as,kf,kbw,1)
    xout(as)
endop

instr 1
kf[][] init 5,5
kb[][] init 5,5
ka[][] init 5,5

kf[][] fillarray 	800,1150,2800,3700,4950,
                    450,800,2830,3500,4950,
						400,1600,2700,3500,4950,
						350,1700,2700,3700,4950,						
						325,700,2530,3500,4950						
kb[][] fillarray 	80,90,120,130,140,
						70,80,100,130,135,
						60,80,120,150,200,
						50,100,120,150,200,
						50,60,170,180,200
ka[][] fillarray		0,4,20,36,60,
					 	0,9,16,28,55,
					  	0,24,30,35,60,
					  	0,20,30,36,60,
					  	0,12,30,40,64

kv = p5


kf0 = kf[kv][0]
kf1 = kf[kv][1]
kf2 = kf[kv][2]
kf3 = kf[kv][3]
kf4 = kf[kv][4]

kb0 = kb[kv][0]
kb1 = kb[kv][1]
kb2 = kb[kv][2]
kb3 = kb[kv][3]
kb4 = kb[kv][4]

ka0 = ampdb(-ka[kv][0])
ka1 = ampdb(-ka[kv][1])
ka2 = ampdb(-ka[kv][2])
ka3 = ampdb(-ka[kv][3])
ka4 = ampdb(-ka[kv][4])


a1 init 1

af1 = Filter(a1*ka0,kf0,kb0)
af2 = Filter(a1*ka1,kf1,kb1)
af3 = Filter(a1*ka2,kf2,kb2)
af4 = Filter(a1*ka3,kf3,kb3)
af5 = Filter(a1*ka4,kf4,kb4)

    amix = af1+af2+af3+af4+af5  
    outch p6,amix
a1 = 0
endin
schedule(1,0,1,0dbfs,0,1)
schedule(1,0,1,0dbfs,3,2)
schedule(1,0,1,0dbfs,4,3)
schedule(1,0,1,0dbfs,1,4)
'''



N=16384
figure(figsize=(8,8))
cs = csound.Csound()
cs.setOption('-n')
cs.compileOrc(code)
cs.start()
spout = cs.spout()
sr = cs.sr()
sigs = zeros(sr*4)
n = 0
for i in range(0,int(len(sigs)/(4*cs.ksmps()))):
    cs.performKsmps()
    for i in spout: 
        sigs[n] = i/cs.get0dBFS()
        n+=1

win = zeros(N)+1 #hanning(N)
subplot(4,1,1)
title('a')
sig = sigs[0:4*N:4]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-90,1)
ylabel("amp", size=16)
yticks([])
xticks([])

xlim(0,6000)


subplot(4,1,2)
title('i')
sig = sigs[1:4*N+1:4]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-90,1)
ylabel("amp", size=16)
yticks([])
xticks([])

xlim(0,6000)

subplot(4,1,3)
title('o')
sig = sigs[2:4*N+2:4]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-90,1)
ylabel("amp ", size=16)
yticks([])
xticks([])
xlim(0,6000)


subplot(4,1,4)
title('u')
sig = sigs[3:4*N+3:4]
x = arange(0,N/2)
bins = x*sr/N
scal = N*sqrt(mean(win**2))
sig1 = sig[0:N]
window = fft(sig1*win/max(sig1))
mags = abs(window/scal)
spec = 20*log10(mags/max(mags))
plot(bins,spec[0:N/2], 'k-', linewidth=2)
ylim(-90,1)
ylabel("amp ", size=16)
xlabel("freq (Hz)", size=16)
yticks([])
xticks(arange(3)*6000)
xlim(0,6000)
tight_layout()
show()
