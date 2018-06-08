Errata for Computer Music Instruments: Foundations, Design and Development (Springer)
======

Chapter 2
--------

* listing 2.2: ```CsoundPerformanceThread(self.cs.csound())``` should be
```CsoundPerformanceThread(cs.csound())```.

* listing 2.8: the line ```self.cs.start()``` needs to be added after ```if res == 0: ```
(on a higher indentation level, same as the following line).

* listing 2.9: ```level = self.cs.controlChannel("meter")``` should be
```level, err = self.cs.controlChannel("meter")```.

* listing 2.13: the line ```def move(self,event):``` is extraneous.

These code lines for shapes.py are correct in Appendix B.
