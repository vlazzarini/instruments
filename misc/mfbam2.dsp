import("music.lib");

gate = button ("gate") : lp(10);    
velo = hslider("gain", 0.1, 0, 1, 0.001);
freq = hslider("freq[unit:Hz]",440,27.5,4435,1);
beta = hslider("beta[midi:ctrl 1]",90,0,127,1)
       : *(1./127) : lp(3);

lp(freq) = *(1 - a1) : + ~ *(a1) with 
   { C = 2. - cos(2.*PI*freq/SR); 
     a1 = C - sqrt(C*C - 1.); };
 
rms = fabs : lp(10);
balance(sig, comp) =  sig*rms(comp)/(rms(sig)+0.000001);
fbam2(beta) = ((+(1))*(_) ~ (_ <: _ + _')*(beta));
process = velo*gate*(osci(freq) <: fbam2(beta),_ : balance);

