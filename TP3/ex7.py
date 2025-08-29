#ex7
#Écrire un programme C qui permet de dire si une année est bissextile ou non. 
#Une année est bissextile si elle est divisible par 4 et non divisible par 100 ou 
#divisible par 400.
annee=int(input("Entrer une annee: "))
if (annee%4==0 and annee%100!=0) or annee%400==0:
    print(str(annee)+' est une annee bissextile.')
else:
    print(str(annee)+' n`est pas une annee bissextile.')
