a=" Bienvenu dans iuc "
print(a)
print(a[5:10])
print(len(a))
b=a[:] # on affecte a b une copie de la chaine a
print(b)
print(b.upper())# mets tout en maj
print(b.swapcase()) #inverse les maj et min
print(b.title()) #1ere lettre de chaque mots en maj
print(b.startswith(' '))#est ce que la chaine commence par ' '
print(b.index('iuc'))#la position de 'iuc'
print(b.count('e'))#Le nombre d'occurence de 'e'
print(b.split('e'))# separe a partir des 'e'(join fait l'inverse)
c=4
d=0.123
print('la valeur de c est %d' %c)
print('la valeur de d est %2f' %(d))##incomplet???
