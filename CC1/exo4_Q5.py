# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7
from math import sqrt
N=int(input("Entrer un entier"))

L=[False,False]
for i in range(2,N+1):
    L.append(True)
for i in range(int(sqrt(N))+1):

    if L[i]==True:
        for j in range(i*2,N+1):

            if j%i==0:
                L[j]=False

print(L)
