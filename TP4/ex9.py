# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7

n = int(input("Entrez le nombre d'entiers : "))
positifs = 0
negatifs = 0
pairs = 0
impairs = 0
maximum = float('-inf')
minimum = float('inf')

for i in range(n):
    entier = int(input("Entrez un entier : "))
    if entier > 0:
        positifs += 1
    elif entier < 0:
        negatifs += 1
    if entier % 2 == 0:
        pairs += 1
    else:
        impairs += 1
    if entier > maximum:
        maximum = entier
    if entier < minimum:
        minimum = entier

print("Nombre d'entiers positifs : ", positifs)
print("Nombre d'entiers négatifs : ", negatifs)
print("Nombre d'entiers pairs : ", pairs)
print("Nombre d'entiers impairs : ", impairs)
print("Maximum : ", maximum)
print("Minimum : ", minimum)
