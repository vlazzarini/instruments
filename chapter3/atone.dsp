import("math.lib");
fc = hslider("freq",0,0,20000,1);
cost = cos(2*PI*fc/SR);
c = 2 - cost  - (sqrt((2 - cost)^2 - 1));
f(x) = x - x';
process = _ + (_ <: (_ - _')*c) ~ *(c);
