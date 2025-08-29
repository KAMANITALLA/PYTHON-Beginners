verbe=input("Entrer un verbe :")
radical = verbe[:-2]
terminaison = verbe[-2:]
f = verbe[-3]
if terminaison == "er" and f!="g" and verbe!="aller":
    print("je " + radical + "e")
    print("tu " + radical + "es")
    print("il/elle " + radical + "e")
    print("nous " + radical + "ons")
    print("vous " + radical + "ez")
    print("ils/elles " + radical + "ent")
elif terminaison == "er" and  f=="g" and verbe!="aller":
    print("je " + radical + "e")
    print("tu " + radical + "es")
    print("il/elle " + radical + "e")
    print("nous " + radical + "eons")
    print("vous " + radical + "ez")
    print("ils/elles " + radical + "ent")
else:
    print("Ce verbe n'est pas du premier groupe.")

