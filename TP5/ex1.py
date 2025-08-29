# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7
L=list()
n=int(input("quelle est la taille de votre liste: "))
for i in range(n):
        a=int(input("Entrer la "+str(i+1)+"eme(ere) valeur: "))
        L.append(a)
print(L)
