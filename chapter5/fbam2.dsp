declare name 		"fbam";
declare version 	"1.0";
declare author 		"V Lazzarini";
declare license 	"LGPL";
declare copyright 	"(c)VL 2011";

//-----------------------------------------------
// 		 Oscillator
//-----------------------------------------------

import("music.lib");

vol = hslider("amp", 0.1, 0, 1, 0.001) : lp(10);
freq = hslider("freq [unit:Hz]", 440,110,880,1) : lp(10);
beta = hslider("beta", 1,0,1,0.001) : lp(10);

lp(freq) = *(1 - a1) : + ~ *(a1) with 
   { C = 2. - cos(2.*PI*freq/SR); 
     a1 = C - sqrt(C*C - 1.); };
rms = fabs : lp(10);
balance(sig, comp) =  sig*rms(comp)/(rms(sig)+0.000001);
fbam2(beta) = ((+(1))*(_) ~ (_ <: _ + _')*(beta));
process = vol*(osci(freq) <: fbam2(beta),_ : balance);

