# Créé par GENERAL STORES, le 15/12/2023 en Python 3.7
from tkinter import *
import math

# Fonction pour calculer le code de couleur
def code_couleur(resistance):
    couleurs = ["noir", "marron", "rouge", "orange", "jaune", "vert", "bleu", "violet", "gris", "blanc"]
    chiffres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    multiplicateurs = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
    tolerance = ["", "±1%", "±2%", "", "", "±0.5%", "±0.25%", "±0.1%", "±0.05%", ""]

    # Calcul du code de couleur
    if resistance >= 0 and resistance <= 9.9:
        chiffre1 = 0
        chiffre2 = chiffres[round(resistance)]
        multiplicateur = 0
    elif resistance >= 10 and resistance <= 99:
        chiffre1 = chiffres[math.floor(resistance/10)]
        chiffre2 = chiffres[round(resistance%10)]
        multiplicateur = 1
    elif resistance >= 100 and resistance <= 999:
        chiffre1 = chiffres[math.floor(resistance/100)]
        chiffre2 = chiffres[math.floor((resistance%100)/10)]
        multiplicateur = 2
    elif resistance >= 1000 and resistance <= 9999:
        chiffre1 = chiffres[math.floor(resistance/1000)]
        chiffre2 = chiffres[math.floor((resistance%1000)/100)]
        multiplicateur = 3
    elif resistance >= 10000 and resistance <= 99999:
        chiffre1 = chiffres[math.floor(resistance/10000)]
        chiffre2 = chiffres[math.floor((resistance%10000)/1000)]
        multiplicateur = 4
    elif resistance >= 100000 and resistance <= 999999:
        chiffre1 = chiffres[math.floor(resistance/100000)]
        chiffre2 = chiffres[math.floor((resistance%100000)/10000)]
        multiplicateur = 5
    elif resistance >= 1000000 and resistance <= 9999999:
        chiffre1 = chiffres[math.floor(resistance/1000000)]
        chiffre2 = chiffres[math.floor((resistance%1000000)/100000)]
        multiplicateur = 6
    elif resistance >= 10000000 and resistance <= 99999999:
        chiffre1 = chiffres[math.floor(resistance/10000000)]
        chiffre2 = chiffres[math.floor((resistance%10000000)/1000000)]
        multiplicateur = 7
    elif resistance >= 100000000 and resistance <= 999999999:
        chiffre1 = chiffres[math.floor(resistance/100000000)]
        chiffre2 = chiffres[math.floor((resistance%100000000)/10000000)]
        multiplicateur = 8
    else:
        chiffre1 = 0
        chiffre2 = 0
        multiplicateur = 0

    # Affichage du code de couleur
    code = couleurs[chiffre1] + " " + couleurs[chiffre2] + " " + couleurs[multiplicateur] + " " + tolerance[multiplicateur]
    return code

# Fonction pour afficher le code de couleur
def afficher_code():
    resistance = float(entree.get())
    code = code_couleur(resistance)
    canvas.itemconfig(rectangle, fill=code)
    label.config(text=code)

# Création de l'interface graphique
fenetre = Tk()
fenetre.title("Code de couleur")

canvas = Canvas(fenetre, width=400, height=200)
canvas.pack()

rectangle = canvas.create_rectangle(50, 50, 150, 150, fill="white")

entree = Entry(fenetre)
entree.pack()

bouton = Button(fenetre, text="Afficher le code de couleur", command=afficher_code)
bouton.pack()

label = Label(fenetre, text="resistance")
label.pack()

fenetre.mainloop()