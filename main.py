import tkinter as tki
import os
import a
class Window(tki.Frame):
    def __init__(self, master=None):
        tki.Frame.__init__(self, master)        
        self.master = master
        self.pack(fill=tki.BOTH, expand=1)
        button = tki.Button(self, text="B", command=lambda:function('b'),height=5,width=20)
        button.place(x=100, y=200)
        button2 = tki.Button(self, text="A", command=lambda:function('a'),height=5,width=20)
        button2.place(x=100,y=100)
        button3 = tki.Button(self, text="D", command=lambda:function('d'),height=5,width=20)
        button3.place(x=300,y=200)
        button4 = tki.Button(self, text="C", command=lambda:function('c'),height=5,width=20)
        button4.place(x=300,y=100)

def function(self):
    a.function(self)
    
root = tki.Tk()
root.wm_title("Milionerzy")
root.resizable(width=False, height=False)
root.geometry("500x500")
app = Window(root)
# set window title
root.wm_title("Milionerzy")

# show window
root.mainloop()