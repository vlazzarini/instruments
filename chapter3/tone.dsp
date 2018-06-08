import("math.lib");
fc = hslider("freq",0,0,20000,1);
cost = cos(2*PI*fc/SR);
c = 2 - cost  - (sqrt((2 - cost)^2 - 1));
process = _ + *(1.-c) ~ *(c);
