import("music.lib");
f = 2000.;
bw = 400;
r =  bw/SR;
w = f/SR;
process = (*(r) + _ :
                  _   + *(w) ~ (_ <: _ - w*_) :
                  _   + *(w) ~ (_ <: _ - w*_) :
		  _   + *(w) ~ (_ <: _ - w*_) :
		  _   + *(w) ~ (_ <: _ - w*_))
		  ~ (_ <: _ + _': *(0.5)) ;


