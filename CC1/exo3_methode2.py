# Créé par GENERAL STORES, le 08/12/2023 en Python 3.7
def Maximum(a,b,c,d):
    l=[a,b,c,d]
    M=l[0]
    print(l)
    for i in l:
        if i>M:
            M=i
    return M
print(Maximum(1,5,3,4))

