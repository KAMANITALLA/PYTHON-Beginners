def premier(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

N=int(input("Entrer un nombre: "))
for j in range(2,N):
    if premier(j):
        print(j)
    
