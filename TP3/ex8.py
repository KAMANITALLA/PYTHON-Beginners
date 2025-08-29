# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7
mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

date = input("Entrez la date au format JJ MM AAAA: ")
jour, mois_num, annee = date.split()
'''int(jour)
int(mois_num)
int(annee)
while jour==0 or jour>=32 or mois_num==0 or mois_num>=13:
      date = input("Entrez la date au format JJ MM AAAA: ")
      jour, mois_num, annee = date.split()'''
print(jour, mois[int(mois_num)-1], annee)
