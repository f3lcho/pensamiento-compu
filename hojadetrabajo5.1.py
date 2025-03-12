print("EJERCICIO 1")

mts = int(input("ingrese cantidad de metros cuadrados: "))

if mts < 15:
    print("la tarifa por metro cúbico es de Q.5")
    total = mts * 5 
    print("el precio total es Q.",total)
elif mts >= 15 and mts <= 29:
    habitantes = int(input("Ingrese cantidad de habitantes: "))
    if habitantes > 3:
        print("la tarifa es de Q.4 por metro cúbico")
        total = mts * 4
        print("el precio total es Q.",total)
    elif habitantes == 3:
        print("la tarifa es de Q.4.5 por metro cúbico")
        total = mts * 4.5
        print("el precio total es Q.",total)
    elif habitantes < 3:
        print("la tarifa es de Q.5 por metro cúbico")
        total = mts * 5
        print("el precio total es Q.",total)
elif mts > 30:
    habitantes = int(input("Ingrese cantidad de habitantes: "))
    div = habitantes % 2
    if habitantes > 5:
        print("la tarifa es de Q.3.5 por metro cúbico")
        total = mts * 3.5
        print("el precio total es Q.",total)
    elif div == 0:
        print("la tarifa es de Q.4 por metro cúbico")
        total = mts * 4
        print("el precio total es Q.",total)
    elif habitantes < 5 or div != 0:
        print("la tarifa es de Q.4.2 por metro cúbico")
        total = mts * 4.2
        print("el precio total es Q.",total)