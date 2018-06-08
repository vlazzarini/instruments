declare name 		"fbam-var1";
declare version 	"1.0";
declare author 		"V Lazzarini";
declare license 	"LGPL";
declare copyright 	"(c)VL 2011";

import("music.lib");

vol 			= hslider("amp", 0.1, 0, 1, 0.001)  : lp(10);
freq 			= hslider("freq [unit:Hz]", 440, 110, 880, 1) : lp(10);
beta                    = hslider("beta", 1,0,1,0.001) : lp(10);

lp(freq) = *(1 - a1) : + ~ *(a1) with 
   { C = 2. - cos(2.*PI*freq/SR); 
     a1 = C - sqrt(C*C - 1.); };
rms = fabs : lp(10);
balance(sig, comp) =  sig*rms(comp)/(rms(sig)+0.000001);
fbam(beta) =  _ <: ((+(1))*(_)*(-1) + _' ~*(beta));
process 		= vol*(osci(freq) <: fbam(beta),_ : balance);


