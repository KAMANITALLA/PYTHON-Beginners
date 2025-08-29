from math import sqrt
def disc(a,b,c):
    return b**2-4*a*c

A=int(input("Entrer le 1er coefficient: "))
B=int(input("Entrer le 2eme coefficient: "))
C=int(input("Entrer le 3eme coefficient: "))
d=disc(A,B,C)
if d>0:
    print("les racines sont: r1="+str((-B-sqrt(d))/2*A)+" et r2="+str((-B+sqrt(d))/2*A))
elif d==0:
    print("la racine double est: r0="+str((-B)/2*A))
else:
    print("les racines n' existent pas")
