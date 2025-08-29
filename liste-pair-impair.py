
pe=[32,12,8,2,5,3,75,15]
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
