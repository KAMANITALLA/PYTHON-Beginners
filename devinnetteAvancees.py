import random
a=random.randint(100)
b=range(a-10, a+10)
c=int(input("devinne le nombre que j'ai choisi:"))
cpt=0
while c not in b:
    print("Perdu :) Essaie encore:")
    c=int(input("devinne le nombre que j'ai choisi:"))
    cpt+=1
    if c in b:
        break
print("bravo vous avez utilise ",cpt," essaies.")
