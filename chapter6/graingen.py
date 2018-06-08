import random as rnd
import ctcsound as csound

code = '''
ksmps=1
gifg = ftgen(0,0,16384,20,6,1)
gifw = ftgen(0,0,0,1,"fox.wav",0,0,1)
instr 1
 ibas = sr/ftlen(gifw)
 aenv = poscil(p4,1/p3,gifg)
 asig = poscil(aenv,p5*ibas,gifw,p6)
   out(asig)
endin
'''

def schedule(p2,p3,p4,p5,p6):
  return "i1 %f %f %f %f %f \n" % (p2,p3,p4,p5,p6)
  
cs = csound.Csound()
cs.setOption('-odac')
a = cs.get0dBFS()
sc = "" 
st = 0.0
gs = 0.5
v = 1.0
tg = 16000
for i in range(0,tg):
   f = v + rnd.random()*v
   gf = 1 + rnd.gauss(0,0.04)
   pos = 2*i/tg + rnd.gauss(0,0.025)
   print(pos)
   sc += schedule(st,gs,a/4,gf,pos)
   st += 1/f
   if v < 1000: v += 0.1
   if gs > 0.05: gs -= 0.001
            
cs.readScore(sc)      
cs.compileOrc(code)
cs.start()
cs.perform()

