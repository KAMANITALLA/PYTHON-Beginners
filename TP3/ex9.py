# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7

date = input("Entrez une date sous la forme jj/mm/aa: ")
jour, mois, annee = date.split("/")

# Conversion des chaînes de caractères en entiers
jour = int(jour)
mois = int(mois)
annee = int(annee)

# Conditions sur jour,mois et annee???

# Calcul de la date du lendemain
if mois in [1, 3, 5, 7, 8, 10, 12]:
    nb_jours = 31
elif mois == 2:
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        nb_jours = 29
    else:
        nb_jours = 28
else:
    nb_jours = 30

if jour == nb_jours:
    jour = 1
    if mois == 12:
        mois = 1
        annee += 1
    else:
        mois += 1
else:
    jour += 1

# Affichage de la date du lendemain
print("La date du lendemain est :", jour, "/", mois, "/", annee)
