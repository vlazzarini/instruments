declare name 		"fbam";
declare version 	"1.0";
declare author 		"V Lazzarini";
declare license 	"LGPL";
declare copyright 	"(c)VL 2011";

//-----------------------------------------------
// 		 Oscillator
//-----------------------------------------------

import("music.lib");

vol = hslider("amp", 0.1, 0, 1, 0.001)  : lp(10);
freq = hslider("freq [unit:Hz]", 440, 110, 880, 1) : lp(10);
cf = hslider("freq [unit:Hz]", 1000, 600, 6000, 1) : lp(10);
beta = hslider("beta", 1,0,1,0.001) : lp(10);

lp(freq) = *(1 - a1) : + ~ *(a1) with 
   { C = 2. - cos(2.*PI*freq/SR); 
     a1 = C - sqrt(C*C - 1.); };
rms = fabs : lp(10);
balance(sig, comp) =  sig*rms(comp)/(rms(sig)+0.000001);
fbam(beta) = ((+(1))*(_)~*(beta));
k = int(cf/freq);
g = cf/freq - k;
mod = (1-g)*osci(k*freq)+g*osci((k+1)*freq);
process = vol*(osci(freq) <: mod*fbam(beta),_ : balance);

