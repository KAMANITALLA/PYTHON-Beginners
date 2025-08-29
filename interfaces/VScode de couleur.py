# Créé par GENERAL STORES, le 15/12/2023 en Python 3.7
import tkinter as tk

# Fonction pour calculer le code de couleur du résistor
def calculate_resistor_code():
    resistance = entry.get()
    colors = {'0': 'noir', '1': 'marron', '2': 'rouge', '3': 'orange', '4': 'jaune', '5': 'vert', '6': 'bleu', '7': 'violet', '8': 'gris', '9': 'blanc'}

    first_digit = colors[resistance[0]]
    second_digit = colors[resistance[1]]
    multiplier = colors[str(len(resistance) - 2)]

    code_label.config(text=f"Code de couleur : {first_digit} {second_digit} {multiplier}")

# Création de l'interface graphique
root = tk.Tk()
root.title("Code de couleur d'un résistor")

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

label = tk.Label(root, text="Entrez la valeur de la résistance :")
label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculer", command=calculate_resistor_code)
calculate_button.pack()

code_label = tk.Label(root, text="Code de couleur :")
code_label.pack()

root.mainloop()

