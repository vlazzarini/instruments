import tkinter

class Application(tkinter.Frame):
    def click(self,event):
     self.button.config(text='clicked (%d, %d)' % (event.x, event.y) )
        
    def createButton(self):
     self.button = tkinter.Button(self,text='click')
     self.button.bind(sequence="<ButtonPress>",func=self.click)
     self.button.pack()

     
    def __init__(self,master=tkinter.Tk()):
     tkinter.Frame.__init__(self,master)
     self.master = master
     self.master.title('Minimal Application')
     self.pack(padx=150,pady=20)
     self.createButton()
     self.master.mainloop()

Application()
