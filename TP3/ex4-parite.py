# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7

val=int(input("Entrer un nombre entier: "))
while val<=0:
      val=int(input("Entrer un nombre entier: "))

if val%2==0:
   print(val," est pair.")
elif val%2!=0:
   print(val," est impair.")

