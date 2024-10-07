nombre_1 = int(input(" entrer un nombre : "))
nombre_2 = int(input(" entrer un nombre : "))
nombre_3 = int(input(" entrer un nombre : "))
if nombre_1 > nombre_2 and nombre_1 < nombre_3:
    print(nombre_1)
else:
    if nombre_2 > nombre_3 :
        print(nombre_2)
    else:
        print(nombre_3)