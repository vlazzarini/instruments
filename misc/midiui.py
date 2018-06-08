import tkinter
import mido
import sys

class Application(tkinter.Frame):
    def note(self,event,num):
     if self.on > 0: 
        self.o.send(mido.Message('note_off',
                              note=self.on,
                              velocity=90))
     self.o.send(mido.Message('note_on',
                              note=num,
                              velocity=90))
     self.on = num
        
    def createButton(self,n):
     button = tkinter.Button(self,text='%d' % n)
     f = lambda e: self.note(e,n)
     button.bind(sequence="<ButtonPress>",func=f)
     button.pack(side='left')

    def quit(self):
      self.o.send(mido.Message('note_off',
                              note=self.on,
                              velocity=90))
      self.master.destroy()


    def __init__(self,master=tkinter.Tk()):
     tkinter.Frame.__init__(self,master)
     self.master = master
     self.master.title('MIDI Keys')
     self.pack(padx=20,pady=20)
     self.notes = [60,62,64,65,67,69,71,72]
     for i in self.notes:
         self.createButton(i)
     self.on = 0
     if len(sys.argv) > 1:
      self.o = mido.open_output(sys.argv[1])
     else:
      self.o = mido.open_output()   
     self.master.protocol('WM_DELETE_WINDOW',
                           self.quit)
     self.master.mainloop()

Application()
