# Créé par GENERAL STORES, le 17/11/2023 en Python 3.7
import numpy as np
import matplotlib.pyplot as plt
x=np.array([0, 1.01, 2.02, 2.99, 3.98]) #Donnees en abscisse
y=np.array([10.02, 7.96, 6.03, 4.04, 2.01]) #Donnees en ordonnee
plt.plot(x,y,'x') #Trace de la courbe
plt.title('fig') #titre du graphe
plt.xlabel('X') #Nom de l'axe x
plt.xlim(0,4) #Echelle sur l'axe x (ou limite a gauche et a droite)
plt.ylabel('Y') #Nom de l'axe y
plt.xlim(0,11) #Echelle sur l'axe y (ou limite en bas et en haut)
plt.grid() #quadrillage
plt.show() #Affichage de la courbe