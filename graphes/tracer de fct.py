# Créé par GENERAL STORES, le 17/11/2023 en Python 3.7
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10, 10, 100)
y=(x+1)/(x-2)
fig,ax=plt.subplots()
ax.plot(x,y,label='y=(x+1)/(x-2)')
ax.set_title("Y=(x+1)/(x-2)")
ax.set_xlabel('Axe des abscisses (X)')
ax.set_ylabel('Axe des ordonnees (Y)')
plt.legend()
plt.grid()
plt.show()

# OU
#import numpy as np
#import matplotlib.pyplot as plt
#x=np.linspace(-10, 10, 100)
#y=(x+1)/(x-2)
#plt.plot(x,y,label='y=(x+1)/(x-2)')
#plt.title("Y=(x+1)/(x-2)")
#pltxlabel('Axe des abscisses (X)')
#plt.ylabel('Axe des ordonnees (Y)')
#plt.legend()
#plt.grid()
#plt.show()

