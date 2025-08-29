# Créé par GENERAL STORES, le 17/11/2023 en Python 3.7
import numpy as np
import matplotlib.pyplot as plt
x=[5,6,4,7,6,7,6,8,6,5,6,5,3,9,4,6,5,8,7,6]

plt.hist(x, range=(0,10), bins=10, rwidth=0.8, align='left')
plt.show()