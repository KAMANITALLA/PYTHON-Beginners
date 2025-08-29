# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7

x = int(input("Entrez le premier entier relatif: "))
y = int(input("Entrez le deuxième entier relatif: "))

resultat = 0

if x < 0 and y < 0:
    x, y = -x, -y

for i in range(abs(y)):
    resultat += abs(x)

if x < 0 or y < 0:
    resultat = -resultat

print("Le résultat de la multiplication est :", resultat)
