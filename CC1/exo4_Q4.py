# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7
# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7
def estPremier(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
N=int(input("Entrer un entier"))
lst=[False,False]

for i in range(2,N+1):
    if estPremier(i):
        lst.append(True)
    else:
        lst.append(False)
print(lst)

L1=list()
for i in range(N+1):
    if lst[i]==True:
        L1.append(i)
print(L1)
