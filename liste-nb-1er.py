a=int(input("Entrer un nombre:"))
liste=list(range(a))
l=list()
print(liste)
for i in range(2,a):
    for j in range(2,i+1):
        if i%j==0:
            break
    if i==j:
            l.append(i)
print("les nombres premiers inferieurs a ",a," sont:",l)
