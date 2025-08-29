t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','nomvembre','decembre']
t3=list()
for i in range(12):
    t3.append(t2[i])
    t3.append(t1[i])
#print(t3)
for i in range(len(t2)):
   # print(t2[i])

p=[32,12,8,2,5,3,75,15]
pair=list()
impair=list()
print(p)
for i in range(len(p)):
    if p[i]%2==0:
        pair.append(p[i])
    else:
        impair.append(p[i])
print("liste pairs ",pair)
print("liste impairs ",impair)