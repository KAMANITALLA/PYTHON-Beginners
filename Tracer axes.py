# Créé par GENERAL STORES, le 15/12/2023 en Python 3.7
from random import randrange
from tkinter import *

def drawline():
    global x1,y1,x2,y2,coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    x1,y1,x2,y2=x1+90,y1-90,x2-90,y2+90

def changecolor():
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c=randrange(8)
    coul=pal[c]

x1,y1,x2,y2=10,100,190,100
coul='black'

fen1 = Tk()
fen1.title('CANVAS')

can1=Canvas(fen1,bg='dark grey',height=200,width=200)

can1.pack(side=LEFT)
bou1=Button(fen1,bg='yellow',text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2=Button(fen1,bg='green',text='Tracer une ligne',command=drawline)
bou2.pack(side=BOTTOM)
bou3=Button(fen1,bg='sky blue',text='Autre couleur',command=changecolor)
bou3.pack()
fen1.mainloop()
fen1.destroy()
