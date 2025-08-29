a=int(input("Entrer un nombre entier quelconque :"))
b=range(10, 21)
cpt=1
while a not in b:
    
    if a<10:
        print("le nombre est trop petit!!!")
        a=int(input("Entrer un nombre plus grand: "))
        cpt+=1
    if a>20:
        print("le nombre est trop grand!!!")
        a=int(input("Entrer un nombre plus petit: "))
        cpt+=1
print("bravo vous avez utilise ",cpt," essaies.")
