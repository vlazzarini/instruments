declare name 		"fbam";
declare version 	"1.0";
declare author 		"V Lazzarini";
declare license 	"LGPL";
declare copyright 	"(c)VL 2011";

//-----------------------------------------------
// 		 Oscillator
//-----------------------------------------------

midigate	= button ("gate");                             	// MIDI keyon-keyoff
midifreq	= hslider("freq[unit:Hz]", 440, 20, 20000, 1); 	// MIDI keyon key
midigain	= hslider("gain", 0.5, 0, 10, 0.01);	       	// MIDI keyon velocity

freq1 = midifreq;
freq2 = midifreq;
vol = midigain;
a = hslider("a", 1,0,1,0.001);

PI = 3.141592653589793;
sr = 44100;
mod1(a) = a - floor(a);
incr(freq) =  freq / float(sr);
phasor(freq) =  incr(freq) : (+ : mod1) ~ _ ;
w = 2*PI*phasor(freq1);
th = 2*PI*phasor(freq2);
sig = sin(w)*(1. - a*a)/(1. - 2*a*cos(th) + a*a);
process = vol*sig*gate;

