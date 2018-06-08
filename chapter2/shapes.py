import tkinter
import ctcsound

code = '''
sr=44100
ksmps=64
nchnls=1
0dbfs=1


gar init 0
gifbam2 faustcompile {{
beta = hslider("beta", 0, 0, 2, 0.001);
fbam2(b) = *~(((\(x).(x + x'))*b)+1);              
process = fbam2(beta);
}}, "-vec -lv 1"            

gar init 0
instr 1
ival = p4
kp chnget "pitch"
kp tonek kp, 10, 1
kv chnget "volume"
kv tonek kv, 10
ain oscili 1, p5*kp, -1, 0.25
ib, asig faustaudio gifbam2,ain
kb1 expsegr ival,0.01,ival,30,0.001,0.2,0.001
faustctl ib,"beta",kb1
asig balance asig, ain
kenv expsegr 1,20,0.001,0.2,0.001 
aenv2 linsegr 0,0.015,0,0.001,p4,0.2,p4
aout = asig*aenv2*kenv*0.4*kv
 out  aout   
gar += aout
endin

instr 100

a1,a2 reverbsc gar,gar,0.7,2000
amix = (a1+a2)/2
out amix
ks rms gar+amix
chnset ks, "meter"
gar = 0                                      
endin

schedule(100,0,-1)
'''

class Application(tkinter.Frame):
 def move(self,event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    item = canvas.find_withtag("current")[0]
    canvas.coords(item, x+10, y+10, x-10, y-10)
    self.cs.setControlChannel("pitch", 0.5+1.5*x/self.size)
    self.cs.setControlChannel("volume", 2.0*(self.size-y)/self.size)

 def play(self,event):
    note = event.widget.find_withtag("current")[0]
    self.canvas.itemconfigure(note, fill="red")
    self.perf.inputMessage("i1 0 -1 0.5 440")

 def stop(self,event):
    note = event.widget.find_withtag("current")[0]
    self.canvas.itemconfigure(note, fill="black")
    self.perf.inputMessage("i-1 0 0.5 440")

 def createCanvas(self):
    self.size = 600
    self.canvas = tkinter.Canvas(self,height=self.size,
                                 width=self.size,
                                 bg="violet")
    self.canvas.pack()

 def createCircle(self):
      circle = self.canvas.create_oval(self.size/2-10,
                                     self.size/2-10,
                                     self.size/2+10,
                                     self.size/2+10,
                                     fill="black")

      self.canvas.tag_bind(circle,"<ButtonPress>",
                           self.play)
      self.canvas.tag_bind(circle,"<B1-Motion>",
                           self.move)
      self.canvas.tag_bind(circle,"<ButtonRelease>",
                           self.stop)

 def createMeter(self):
  iw = 10
  self.vu = []
  for i in range(0, self.size, iw):
   self.vu.append(self.canvas.create_rectangle(i,
        self.size-40,i+iw,self.size,fill="grey"))

 def drawMeter(self):
    level,err = self.cs.controlChannel("meter")
    cnt = 0
    level *= 16000
    red = (self.size/10)*0.8
    yellow = (self.size/10)*0.6
    for i in self.vu:
      if level > cnt*100:
       if cnt > red:
        self.canvas.itemconfigure(i, fill="red")
       elif cnt > yellow:
        self.canvas.itemconfigure(i, fill="yellow")
       else:
        self.canvas.itemconfigure(i, fill="blue")
      else:
       self.canvas.itemconfigure(i, fill="grey")
      cnt  = cnt + 1
    self.master.after(50,self.drawMeter)

 def quit(self):
    self.perf.stop()
    self.perf.join()
    self.master.destroy()

 def createEngine(self):
    self.cs = ctcsound.Csound()
    res = self.cs.compileOrc(code)
    self.cs.setOption('-odac')
    if res == 0:
     self.cs.start()
     self.cs.setControlChannel('pitch', 1.0)
     self.cs.setControlChannel('volume', 1.0)
     self.perf = ctcsound.CsoundPerformanceThread(self.cs.csound())
     self.perf.play()
     return True
    else:
     return False   

 def __init__(self,master=None):
    tkinter.Frame.__init__(self,master)
    self.master.title('Csound + Tkinter: '
     'just click and play')
    self.master = master
    self.pack()
    self.createCanvas()  
    self.createCircle()
    self.createMeter()
    if self.createEngine() is True:
      self.drawMeter()
      self.master.protocol('WM_DELETE_WINDOW',
                           self.quit)
      self.master.mainloop()
    else: self.master.quit()

Application(tkinter.Tk())

