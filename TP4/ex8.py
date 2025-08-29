# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7
for i in range(1, 101):
    somme_chiffres = 0
    for chiffre in str(i):
        somme_chiffres += int(chiffre)
    if somme_chiffres == 11:
        print(i)

