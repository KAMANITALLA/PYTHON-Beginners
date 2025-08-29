#fonction energie mecanique
def Ec(m,v):
    return (1/2)*m*v**2
def Ep(m,h):
    return m*g*h
M=float(input("Entrer la valeur de la masse: "))
g=9.81
H=float(input("Entrer la hauteur: "))
V=float(input("Entrer la vitesse: "))
Em=Ec(M,V)+Ep(M,H)
print("L energie mecanique sera: ",Em)
