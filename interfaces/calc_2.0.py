# Créé par GENERAL STORES, le 15/01/2024 en Python 3.7
import tkinter as tk

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    result.set(float(num1.get()) / float(num2.get()))

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Variables pour stocker les nombres et le résultat
num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

# Création des champs de saisie et des boutons
tk.Label(root, text="Nombre 1").grid(row=0, column=0)
tk.Entry(root, textvariable=num1).grid(row=0, column=1)
tk.Label(root, text="Nombre 2").grid(row=1, column=0)
tk.Entry(root, textvariable=num2).grid(row=1, column=1)
tk.Button(root, text="Addition", command=add).grid(row=2, column=0)
tk.Button(root, text="Soustraction", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiplication", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Division", command=divide).grid(row=3, column=1)
tk.Label(root, text="Résultat").grid(row=4, column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=4, column=1)

# Lancement de la boucle principale
root.mainloop()

