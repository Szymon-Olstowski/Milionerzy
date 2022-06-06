import tkinter as tki
import random
import sqlite3
import pygame,time
conn = sqlite3.connect('coin.db')
c = conn.cursor()
tab=[]
pygame.mixer.init()
class licz:
    meh = 0
class pyt:
    nrpyt= 0
class window:
    win=0
class test:
    a=0
class kwota:
    k=0
class gwarant:
    g=0
def pyt_tres(numer):
    c.execute("SELECT * FROM Pytania WHERE nr_pyt=?",(numer,))
    wyniki=c.fetchone()
    return wyniki
def spr(numer,ilosc):
    reset = 0
    licz.meh = reset
    for i in tab:
        if i!=numer:
            licz.meh=licz.meh+1
    spr1(ilosc,numer)
def spr1(ilosc,numer):
    licz1=licz.meh
    if len(tab)==licz1:
        tab.append(numer)
        print("muha",tab)
        wyniki=pyt_tres(numer)
        pyt.nrpyt=0
        pyt.nrpyt=numer
        print(wyniki)
    else:
        numer=random.randint(1,ilosc[0]-1)
        spr(numer,ilosc)
def muzyka():
        pygame.mixer.music.queue("loop_muzyka.mp3",loops=99)

def function(self):
    c.execute("SELECT COUNT() FROM Pytania")
    ilosc=c.fetchone()
    print(self)
    if tab:
        print(len(tab))
        numer=pyt.nrpyt
        print("Pytanie ",numer)
        c.execute("SELECT p_odp FROM Pytania WHERE nr_pyt=?",(numer,))
        odp_p=c.fetchone()
        if odp_p[0]==self:
            print("Prawidłowa odpowiedz")
            #prawidłowa odp
            if len(tab)==12: #zmiana gdy ilosć pytań powyżej 12 to if len(tab)==12
                pygame.mixer.music.load('1milon_zł.mp3')
                pygame.mixer.music.play()
                label=test.a
                label.config(text="Wygraleś 1000000 zł")
                print("Koniec pytań")
            else:
                pygame.mixer.music.load('poprawna_odp.mp3')
                pygame.mixer.music.play()
                numer=random.randint(1,ilosc[0]-1)
                spr(numer,ilosc)
                p_nr=len(tab)
                c.execute("SELECT * FROM Kwoty WHERE nr=?",(p_nr,))
                nr_p=c.fetchone()
                spr_gwarant=nr_p[2]
                kwota.k=str(nr_p[1])
                if spr_gwarant=="tak":
                    gwarant.g=str(nr_p[1])
                #następne pytanie
                pygame.mixer.music.queue('next_pytanie.mp3')
                time.sleep(5)
                click_action()
                muzyka()
        else:
            #błędna odpowiedź
            pygame.mixer.music.load('błedna_odp.mp3')
            pygame.mixer.music.play()
            print("Nieprawdłowa odpowiedź. Prawidłowa odpowiedź to: ",odp_p)
            label=test.a
            wygrana=gwarant.g
            label.config(text="Nieprawdłowa odpowiedź. Prawidłowa odpowiedź to: "+str(odp_p)+"\n"+
            " Wygrałeś "+wygrana+" zł.")
    
    else:
        numer=random.randint(1,ilosc[0]-1)
        tab.append(numer)
        pyt.nrpyt=0
        pyt.nrpyt=numer
        print("muha",tab)
        wyniki=pyt_tres(numer)
        print(wyniki)
        window.win = tki.Toplevel()
        p_nr=len(tab)
        c.execute("SELECT * FROM Kwoty WHERE nr=?",(p_nr,))
        nr_p=c.fetchone()
        kwota.k=str(nr_p[1])
        popup_window()
def click_action():
    label=test.a
    numer=pyt.nrpyt
    pytanie= pyt_tres(numer)
    kwoty=kwota.k
    label.config(text="Pytanie za "+kwoty+" zł\n"+pytanie[1]+" A: "+pytanie[2]+" B: "+pytanie[3]+" C: "+pytanie[4]+" D: "+pytanie[5])
def popup_window():
    okno=window.win
    label = tki.Label(okno, text="MUCHA")
    label.pack(fill='x', padx=50, pady=5)
    test.a=label
    click_action()
def procent_50():
    numer=pyt.nrpyt
    c.execute("SELECT p_odp FROM Pytania WHERE nr_pyt=?",(numer,))
    odp_p=c.fetchone()
    return odp_p[0]
