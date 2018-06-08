SR = 44100;
mod1(a) = a - floor(a);
freq = 440;
incr(fr) =  fr / float(SR);
phasor(fr,ph) =  incr(fr) : (+ : mod1) ~ _ :
+(ph) : mod1;
process = phasor(freq,0.5);
