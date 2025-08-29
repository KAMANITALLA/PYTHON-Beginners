# Créé par GENERAL STORES, le 15/12/2023 en Python 3.7
from tkinter import *
'''
def colors():
    a=str(lb1).split(',')
    pal=['black','maroon','red','orange','yellow','green','blue','purple','grey','white']
    for i in range(3):
        for j in range(10):
            if a[i]==pal[j]:'''
# Fonction pour calculer le code de couleur du résistor
def calculate_resistor_code():
    resistance = entry.get()
    colors = {'0': 'noir', '1': 'marron', '2': 'rouge', '3': 'orange', '4': 'jaune', '5': 'vert', '6': 'bleu', '7': 'violet', '8': 'gris', '9': 'blanc'}

    first_digit = colors[resistance[0]]
    second_digit = colors[resistance[1]]
    multiplier = colors[str(len(resistance) - 2)]

    code_label.config(text=f"Code de couleur : {first_digit} {second_digit} {multiplier}")

    canvas.itemconfig(ligne.append(can1.create_rectangle(85, 30 , 85+12 , 70 , fill='black', width=0)), fill=first_digit)


fen1 = Tk()
fen1.title('COULEURES D UN RESISTOR A 3 ANNEAUX ')

can1=Canvas(fen1,bg='ivory',width=250,height=100)
can1.grid(row=1, column=1, columnspan=3, pady=5, padx=5)
can1.create_line(10,50,240,50,width=5)
can1.create_rectangle(65, 30, 185, 70,fill='light grey',width=2)

ligne=[]
ligne.append(can1.create_rectangle(85, 30 , 85+12 , 70 , fill='black', width=0))
ligne.append(can1.create_rectangle(85+24, 30 , 85+24+12 , 70 , fill='black', width=0))
ligne.append(can1.create_rectangle(150, 30 , 150+12 , 70 , fill='black', width=0))
'''
ligne=[]
for x in range(85,150,24):
    ligne.append(can1.create_rectangle(x, 30 , x+12 , 70 , fill='black', width=0))
'''

lb1= Label(fen1,text="Entrer une resistance :").grid(row =2 , column=1 )
zonetext1=Entry(fen1).grid(row =2 , column =2)
lb3= Label(fen1, text="Ohms(s)").grid(row=2 , column=3)
'''
pal=['black','maroon','red','orange','yellow','green','blue','purple','grey','white']

a=str(lb1).split(',')
for i in range(3):
    for j in range(10):
        if a[i]==pal[j]:
            for x in range(85,150):
                ligne.append(can1.create_rectangle(x, 30 , x+12 , 70 , fill=pal[j], width=0))'''

'''lb2= Label(fen1,text="Entrer son incertitude :").grid(row =3 , column=1)
zonetext2=Entry(fen1).grid(row =3 , column =2)
lb4= Label(fen1, text=" % ").grid(row=3 , column=3)'''

btn=Button(fen1, text="Afficher" , bg='grey' , command=calculate_resistor_code).grid(row=4 , column=2)


fen1.mainloop()
fen1.destroy()


