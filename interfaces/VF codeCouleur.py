# Créé par GENERAL STORES, le 26/11/2024 en Python 3.7
# Vfinal code couleur
import tkinter as tk
def calculate_resistor_code():
    resistance = zonetext1.get()
    colors = {'0': 'black', '1': 'maroon', '2': 'red', '3': 'orange', '4': 'yellow', '5': 'green', '6': 'blue', '7': 'purple', '8': 'grey', '9': 'white'}

    first_band_color = colors[resistance[0]]
    second_band_color = colors[resistance[1]]
    third_band_color = colors[resistance[2]]
    fourth_band_color = colors[str(len(resistance) - 1)]

    # Dessiner le résistor avec les nouvelles couleurs
    canvas.itemconfig(r1, fill=first_band_color)
    canvas.itemconfig(r2, fill=second_band_color)
    canvas.itemconfig(r3, fill=third_band_color)
    canvas.itemconfig(r4, fill=fourth_band_color)

# Création de l'interface graphique
root = tk.Tk()
root.title("Code de couleur d'un résistor")
canvas = tk.Canvas(root, width=250, height=100)

canvas.create_line(10,50,240,50,width=5)
canvas.grid(row=1, column=1, columnspan=3, pady=5, padx=5)
canvas.create_rectangle(65, 30, 185, 70,fill='light grey',width=2)

# Dessin des résistances initiallement toutes noire
r1=canvas.create_rectangle(85, 30 , 85+12 , 70 , fill='black', width=0)
r2=canvas.create_rectangle(85+24, 30 , 85+24+12 , 70 , fill='black', width=0)
r3=canvas.create_rectangle(85+48, 30 , 85+48+12 , 70 , fill='black', width=0)
r4=canvas.create_rectangle(160, 30 , 160+12 , 70 , fill='black', width=0)
canvas.pack()

#creation et positionnement des champs d'affichages et de saisie
label= tk.Label(root,text="Entrer une valeur de resistance(en Ohms):")
#label.grid(row=2 , column=1)
zonetext1= tk.Entry(root)
#zonetext1.grid_bbox(column=2, row=2)
label.pack()
zonetext1.pack()

# creation du bouton
calculate_button = tk.Button(root, text="Calculer", command=calculate_resistor_code)
calculate_button.pack()

root.mainloop()
root.destroy()