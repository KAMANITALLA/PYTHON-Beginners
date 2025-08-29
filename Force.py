# Créé par GENERAL STORES, le 21/11/2023 en Python 3.7
from math import *

g=6.67*(10**-11)
ma=10000
mb=10000
d=0.05
while d<=2.0:
      f=g*ma*mb/d**2
      print("d=",d," m ; La force vaut ",f," N")
      d*=2