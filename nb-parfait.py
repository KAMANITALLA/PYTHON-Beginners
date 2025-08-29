a=int(input("Entrer un nombre:"))
c=0
for i in range(2,a):
        if i%j==0:
            c+=i
if a==c:
    print(a,' est parfait.')    
if c==a/2:
    print(a," n'est pas parfait.")
