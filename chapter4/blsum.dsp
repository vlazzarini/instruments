declare name 		"fbam";
declare version 	"1.0";
declare author 		"V Lazzarini";
declare license 	"LGPL";
declare copyright 	"(c)VL 2011";

//-----------------------------------------------
// 		 Oscillator
//-----------------------------------------------

vol = hslider("amp", 0.1, 0, 1, 0.001);
freq1 = hslider("freq1[unit:Hz]",440,110,1760,1);
freq2 = hslider("freq2[unit:Hz]",440,110,1760,1);
a = hslider("a", 1,0,1,0.001);

PI = 3.141592653589793;
sr = 44100;
mod1(a) = a - floor(a);
incr(freq) =  freq / float(sr);
phasor(freq) =  incr(freq) : (+ : mod1) ~ _ ;
w = 2*PI*phasor(freq1);
th = 2*PI*phasor(freq2);
sig = sin(w)*(1. - a*a)/(1. - 2*a*cos(th) + a*a);
process = vol*sig;

