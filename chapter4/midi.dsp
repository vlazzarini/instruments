declare name 		"fbam";
declare version 	"1.0";
declare author 		"V Lazzarini";
declare license 	"LGPL";
declare copyright 	"(c)VL 2011";

// Simple Organ
midigate	= button ("gate");                             	// MIDI keyon-keyoff
midifreq	= hslider("freq[unit:Hz]", 440, 20, 20000, 1); 	// MIDI keyon key
midigain	= hslider("gain", 0.5, 0, 10, 0.01);	       	// MIDI keyon velocity

process = voice(midigate, midigain, midifreq) * hslider("volume", 0, 0, 1, 0.01);

// Implementation

phasor(f)   = f/fconstant(int fSamplingFreq, <math.h>) : (+,1.0:fmod) ~ _ ;
osc(f)      = phasor(f) * 6.28318530718 : sin;

timbre(freq)= osc(freq) + 0.5*osc(2.0*freq) + 0.25*osc(3.0*freq);

envelop(gate, gain) = gate * gain : smooth(0.9995)
                with { smooth(c) = * (1-c) : + ~ * (c) ; } ;

voice(gate, gain, freq) = envelop(gate, gain) * timbre(freq);