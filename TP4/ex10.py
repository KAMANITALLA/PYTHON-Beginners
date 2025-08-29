# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7
# 1er volet: savoir si n est parfait ou non.
n = int(input("Entrez un entier : "))
somme = 0

for i in range(1, n):
    if n % i == 0:
        somme += i

if somme == n:
    print(n, "est un nombre parfait.")
else:
    print(n, "n'est pas un nombre parfait.")

# 2em volet: afficher les nombres parfaits entre 1 et n.
n = int(input("Entrez un entier : "))
somme = 0

for i in range(1, n+1):
    if n % i == 0:
        somme += i

if somme == n:
    print(n)