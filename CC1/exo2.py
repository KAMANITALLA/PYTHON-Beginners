# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7
'''exo1
1-err      2-err    3-err
4--26      5-neg et imp   6-err
7-8
'''
exo2
from math import sqrt
n=int(input("Entrer le nombre de termes: "))
u0,som=1,0
for i in range(1,n):
    u=sqrt(u0)+1/(i+1)
    som+=u
    u0=u
print("la somme est: ",som)

