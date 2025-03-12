print("EJERCICIO 2")

model = int(input("ingrese año del vehiculo: "))
div = model % 2
resta = 2025 - model
if model < 2001:
    print("El auto no tiene restricción de uso")
    if div == 0:
        print("Solo circula los sabados medio día")
    if model >= 25:
        print("debe hacerse mantenimiento")
elif model > 2001:
    plate = str(input("Ingrese numero de placa completo: "))
    if plate.endswith("0") or plate.endswith("2") or plate.endswith("4") or plate.endswith("6") or plate.endswith("8"):
        print("no circula los lunes")
    elif plate.endswith("1") or plate.endswith("3") or plate.endswith("5") or plate.endswith("7") or plate.endswith("9"):
        print("No circula los viernes")
    
    if div == 0:
        print("Solo circula los sabados medio día")