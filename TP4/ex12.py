'''Soit la suite Un suivante : U1=1, U2=2 et Un= Un-1 + Un-2.
Ecrire un programme python qui lit un nombre entier k>=1 et affiche la valeur de Uk.'''
k=int(input('Entrer un entier k>=1: '))
u1, u2 = 1, 2

if k == 1:
    print("U1 = 1")
elif k == 2:
    print("U2 = 2")
else:
    for i in range(3, k+1):
        u = u1 + u2
        u1, u2 = u2, u
    print("U", k, "=", u)
