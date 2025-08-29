# Créé par GENERAL STORES, le 17/11/2023 en Python 3.7
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, 10, 100) #Donnees en abscisse
y1=10*np.sin(x) #Donnees en ordonnee de y1
y2=6*np.sin(x-1) #Donnees en ordonnee de y2

plt.plot(x,y1,'*' ,label='10.sin(x)') #Trace de la courbe y1 avec texte legende
plt.plot(x,y2,label='6.sin(x-1)') #Trace de la courbe y2 avec texte legende
plt.title("Y1=sin(x) et Y2=sin(x-1)") #titre du graphe
plt.xlabel('Axe des abscisses (X)') #Nom de l'axe x
plt.ylabel('Axe des ordonnees (Y)') #Nom de l'axe y
plt.legend() #ajout de la legende
plt.grid() #quadrillage
plt.show() #Affichage de la courbe
