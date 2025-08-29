# Créé par GENERAL STORES, le 15/12/2023 en Python 3.7
import tkinter as tk

# Fonction pour calculer le code de couleur du résistor
def calculate_resistor_code():
    resistance = entry.get()
    colors = {'0': 'black', '1': 'maroon', '2': 'red', '3': 'orange', '4': 'yellow', '5': 'green', '6': 'blue', '7': 'purple', '8': 'grey', '9': 'white'}

    first_band_color = colors[resistance[0]]
    second_band_color = colors[resistance[1]]
    third_band_color = colors[str(len(resistance) - 2)]

    # Dessiner le résistor avec les nouvelles couleurs
    canvas.itemconfig(r1, fill=first_band_color)
    canvas.itemconfig(r2, fill=second_band_color)
    canvas.itemconfig(r3, fill=third_band_color)

# Création de l'interface graphique
root = tk.Tk()
root.title("Code de couleur d'un résistor")

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Dessin des résistances initiallement toutes gris
r1 = canvas.create_rectangle(50, 50, 100, 150, fill="gray")
r2 = canvas.create_rectangle(100, 50, 150, 150, fill="gray")
r3 = canvas.create_rectangle(150, 50, 200, 150, fill="gray")

label = tk.Label(root, text="Entrez la valeur de la résistance :")
label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculer", command=calculate_resistor_code)
calculate_button.pack()

root.mainloop()
