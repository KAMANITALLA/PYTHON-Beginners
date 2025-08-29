# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7
jour = input("Entrez un jour de la semaine (en français) : ")

if jour == "lundi" or jour == "mardi" or jour == "mercredi" or jour == "jeudi" or jour == "vendredi":
    print("Il y a cours aujourd'hui.")
elif jour == "samedi":
    print("Il y a devoir surveillé aujourd'hui.")
elif jour == "dimanche":
    print("Aujourd'hui, on se repose.")
else:
    print("Jour invalide.")

