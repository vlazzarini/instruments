import("math.lib");
fc = hslider("freq",0,0,20000,1);
bw = hslider("bw",10,0.1,20000,1);
r = 1 - PI*(bw/SR);
cost = cos(2*PI*fc/SR);
b1 = (4*r*r/(1+r*r))*cost;
b2 = -2*r;
a = (1 - r*r)*sin(2*PI*fc/SR);
process = _ + *(a) ~ (_ <: (*(b1) + b2*_')) ;
