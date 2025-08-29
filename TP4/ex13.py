#exo13
from math import pow
#from math import factorial
def factoriel(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factoriel(a-1)

k=int(input("Entrer une valeur entiere de k: "))
x=float(input("Entrer un reel quelconque x: "))
S=0
for i in range(1,k+1):
    S=S+pow(-1,i)*(pow(x,2*i)+1)/factoriel(2*i+1)
print
print("La somme S vaut: ",S)
