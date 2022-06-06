from cProfile import label
import tkinter as tki
from tkinter import Label
import os
import ab, random
class kolo:
    k1=0
    k2=0
    k3=0
class l:
    t=0
    t1=0
    t2=0
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
        button5 = tki.Button(self, text="50%", command=lambda:kolo1(),height=10,width=20)
        button5.place(x=100,y=300)
        button6 = tki.Button(self, text="telefon do przyjaciela", command=lambda:kolo2(),height=10,width=20)
        button6.place(x=300,y=300)
        button7= tki.Button(self, text="pytanie do publiczności", command=lambda:kolo3(),height=10,width=20)
        button7.place(x=100,y=500)
        l.t=button5
        l.t1=button6
        l.t2=button7
def function(self):
    ab.function(self)
    if kolo.k1==1:
        text_label=l.t
        text_label.config(text="Koło 50/50 zostało użyte")
    if kolo.k2==1:
        text=l.t1
        text.config(text="Koło telefon do \n przyjaciela zostało użyte")
    if kolo.k3==1:
        text=l.t2
        text.config(text="Koło pytanie do  \n publiczności zostało użyte")
def kolo1():
    if kolo.k1==0:
        odp_p=ab.procent_50()
        text_label=l.t
        if odp_p=="a":
            a1=["b","c","d"]
            r1=random.choice(a1)
            print("Pozostałe odpowiedźi: ",odp_p,r1)
            text_label.config(text="Pozostałe odpowiedźi "+odp_p+" "+r1)
        if odp_p=="b":
            a2=["a","c","d"]
            r2=random.choice(a2)
            print("Pozostałe odpowiedźi: ",odp_p,r2)
            text_label.config(text="Pozostałe odpowiedźi "+odp_p+" "+r2)
        if odp_p=="c":
            a3=["a","b","d"]
            r3=random.choice(a3)
            print("Pozostałe odpowiedźi: ",odp_p,r3)
            text_label.config(text="Pozostałe odpowiedźi "+odp_p+" "+r3)
        if odp_p=="d":
            a4=["a","b","c"]
            r4=random.choice(a4)
            print("Pozostałe odpowiedźi: ",odp_p,r4)
            text_label.config(text="Pozostałe odpowiedźi "+odp_p+" "+r4)
        kolo.k1=1
    else:
        text_label=l.t
        text_label.config(text="Koło zostało użyte")
def kolo2():
    if kolo.k2==0:
        text1=l.t1
        a1=["a","b","c","d"]
        test=random.choice(a1)
        text1.config(text="Myślę ze prawidłowa \n odpowiedż jest "+ test)
        kolo.k2=1
    else:
        text1=l.t1
        text1.config(text="Koło zostało użyte")
def kolo3():
    if kolo.k3==0:
        text1=l.t2
        odp_p=ab.procent_50()
        if odp_p=="a":
            a=60
            b=25
            c=10
            d=5
            text1.config(text="Liczby procentowe \n a="+str(a)+" b="+str(b)+" c="+str(c)+" d="+str(d))
        if odp_p=="b":
            a=28
            b=30
            c=27
            d=15
            text1.config(text="Liczby procentowe \n a="+str(a)+" b="+str(b)+" c="+str(c)+" d="+str(d))
        if odp_p=="c":
            a=20
            b=13
            c=42
            d=25
            text1.config(text="Liczby procentowe \n a="+str(a)+" b="+str(b)+" c="+str(c)+" d="+str(d))
        if odp_p=="d":
            a=2
            b=3
            c=5
            d=90
            text1.config(text="Liczby procentowe \n a="+str(a)+" b="+str(b)+" c="+str(c)+" d="+str(d))
        kolo.k3=1     
    else:
        text1=l.t2
        text1.config(text="Koło zostało użyte")
    





root = tki.Tk()
root.wm_title("Milionerzy")
root.resizable(width=False, height=False)
root.geometry("500x700")
app = Window(root)
# set window title
root.wm_title("Milionerzy")
# show window
root.mainloop()