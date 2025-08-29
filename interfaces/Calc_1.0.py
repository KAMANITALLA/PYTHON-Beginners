# Créé par GENERAL STORES, le 15/12/2023 en Python 3.7

import math

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def racine_carree(a):
    return math.sqrt(a)

def exponentielle(a):
    return math.exp(a)

def logarithme(a):
    return math.log(a)

def sinus(a):
    return math.sin(a)

def cosinus(a):
    return math.cos(a)

def tangente(a):
    return math.tan(a)

print("Bienvenue dans la calculatrice scientifique!")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")
print("5. Racine carrée")
print("6. Exponentielle")
print("7. Logarithme")
print("8. Sinus")
print("9. Cosinus")
print("10. Tangente")

choix = input("Entrez votre choix (1-10) : ")

if choix in ('1', '2', '3', '4'):
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))

    if choix == '1':
        print(a, "+", b, "=", addition(a, b))

    elif choix == '2':
        print(a, "-", b, "=", soustraction(a, b))

    elif choix == '3':
        print(a, "*", b, "=", multiplication(a, b))

    elif choix == '4':
        print(a, "/", b, "=", division(a, b))

elif choix in ('5', '6', '7', '8', '9', '10'):
    a = float(input("Entrez un nombre : "))

    if choix == '5':
        print("La racine carrée de", a, "est", racine_carree(a))

    elif choix == '6':
        print("L'exponentielle de", a, "est", exponentielle(a))

    elif choix == '7':
        print("Le logarithme de", a, "est", logarithme(a))

    elif choix == '8':
        print("Le sinus de", a, "est", sinus(a))

    elif choix == '9':
        print("Le cosinus de", a, "est", cosinus(a))

    elif choix == '10':
        print("La tangente de", a, "est", tangente(a))

else:
    print("Choix invalide")
