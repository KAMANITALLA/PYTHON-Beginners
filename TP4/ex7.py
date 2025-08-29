# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7
n = int(input("Entrez le nombre de lignes pour le triangle isocèle : "))

for i in range(1, n+1):
    print(" "*(n-i) + "* "*(i))
