#exercice 12
sexe=input('etes-vous de sexe masculin(M)ou feminin(F): ')
taille=float(input("Entrer votre taille en centimetre: "))
poids=float(input("Entrer votre poids en kilogramme: "))

if sexe=='M' or sexe=='m':
    PI=taille-100-(taille-150)/4
    print("Monsieur votre poids ideal est de: ",PI)
elif sexe=='F' or sexe=='f':
    PI=taille-100-(taille-150)/2
    print("Madame votre poids ideal est de: ",PI)
else:
    print("Etes-vous un homonculus 🤨?")

BMI=poids/taille**2
if BMI<27:
    print("Vous avez un poids normale")
elif BMI in range(27,33):
    print("Vous etes obese")
else:
    print("Vous etes malade")
