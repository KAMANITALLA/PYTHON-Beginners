import math
a=int(input("Entrer le premier coefficient de l'equation du second degre"))
b=int(input("Entrer le deuxieme coefficient de l'equation du second degre"))
c=int(input("Entrer le troisieme coefficient de l'equation du second degre"))
delta=(b*b-4*a*c)
if delta>0:
    x1=(-b-math.sqrt(delta))/2*a
    x2=(-b+math.sqrt(delta))/2*a
    print("ils existent deux solutions distinctes:",x1,x2)
elif delta==0:
    x0=(-b)/(2*a)
    print("il n'existe qu'une solution unique:",x0)
else:
    print("Il n'existe pas de solutions reels")
