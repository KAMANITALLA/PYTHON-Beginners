L=list()
n=int(input("quelle est la taille de votre tableau: "))
if n>50:
    print("Taille maximale depassee:")
else:
    for i in range(n):
        a=int(input("Entrer la "+str(i+1)+"eme(ere) valeur: "))
        L.append(a)

print(L)
S=0
for i in range(n):
    S=S+L[i]
print("Somme=",S)
print("Le max est: ",max(L))
print("Le min est: ",min(L))
#position du max et du min: fonction index()
for i in range(n):
    if L[i]!=max(L):
        continue
    else:
        break
print("la position du max est:",i)
for i in range(n):
    if L[i]!=min(L):
        continue
    else:
        break
print("la position du min est:",i)
L.reverse()
print("son inverse est:",L)
