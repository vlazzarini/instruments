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
freq = hslider("freq [unit:Hz]",440,110,880,1) : lp(10);
beta = hslider("beta", 1,0,1,0.001) : lp(10);

lp(freq) = *(1 - a1) : + ~ *(a1) with 
   { C = 2. - cos(2.*PI*freq/SR); 
     a1 = C - sqrt(C*C - 1.); };

mod1(a) = a - floor(a);
incr(freq) =  freq / float(SR);
phasor(freq) =  incr(freq) : (+ : mod1) ~ _ ;
phi(w) = (_ : sin) + w  ~ *(beta); 
fbfm(f) = sin(phi(2*PI*phasor(f)));
process = vol*fbfm(freq);

