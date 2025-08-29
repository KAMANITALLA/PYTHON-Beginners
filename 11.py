
def estPremier(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True

def LST(n):
    lst=[False,False]
    for i in range(2,N+1):
        if estPremier(i):
            lst.append(True)
        else:
            lst.append(False)
        return lst


N=int(input("Entrer un entier"))
L1=list()
lst[:]=LST(N)
for i in range(N+1):
    if lst[i]==True:
        L1.append(i)
print(L1)
