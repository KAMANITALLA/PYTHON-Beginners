# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7

moyenne = float(input("Entrez la moyenne de l'élève : "))

if moyenne >= 10 and moyenne < 12:
    print("Mention : passable")
elif moyenne >= 12 and moyenne < 14:
    print("Mention : assez bien")
elif moyenne >= 14 and moyenne < 16:
    print("Mention : bien")
elif moyenne >= 16:
    print("Mention : très bien")
else:
    print("Moyenne invalide.")
