a="Bienvenu a iuc."
if 'i' in a:
    print('true')
else:
    print('False')
print(a.count('i'))

ch1=input("Entrer une chaine :")
ch2=ch1[0]
for i in range(1,len(ch1)):
    ch2+='*'
    ch2+=ch1[i]
print(ch2)
print(ch1.invert())
#taf prendre un verbe du 1er groupe et le conjuguer au present de l' indicatif
