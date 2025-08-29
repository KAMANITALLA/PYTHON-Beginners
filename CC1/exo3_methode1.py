# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7
def Maximum(a,b,c,d):

    if a>b and a>c and a>d:
        return a
    if b>a and b>c and b>d:
        return b
    if c>a and c>b and c>d:
        return c
    if d>a and d>b and d>c:
        return d

print(Maximum(1,5,3,4))
