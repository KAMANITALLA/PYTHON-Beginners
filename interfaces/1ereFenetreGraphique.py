# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7
from tkinter import *
import math
def Periode():
    zonetext3.insert(10,str(2*math.pi*math.sqrt(eval(zonetext1.get())/eval(zonetext2.get()))))

fen  = Tk()
fen.title(" Essaie periode")

lb1= Label(fen,text="Entrer une longueur :")
lb2= Label(fen,text="Entrer une pesanteur :")
lb3= Label(fen,text="Valeur de la periode:")

zonetext1=Entry(fen)
zonetext2=Entry(fen)
zonetext3=Entry(fen)

B=Button(fen, text =" Periode ", command=Periode)

lb1.grid(row =0)
lb2.grid(row =1)
lb3.grid(row =4)

zonetext1.grid(row =0 , column =1)
zonetext2.grid(row =1 , column =1)
zonetext3.grid(row =4 , column =1)

B.grid(row =3 , column =1)

fen.mainloop()


