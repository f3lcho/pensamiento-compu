saldo = int(3000)
cont = int(1)

while True:
    retirar = int(input("Ingrese cantidad a retirar: "))
    retiro = saldo-retirar
    if retiro < 0:
        print("Cantidad Insuficiente, ingrese otra cantidad valida")
        cont += 1 
    if cont == 4:
        print("intentos terminados")
        break
    if retiro >= 0:
        print("Operacion valida")
        print("Su saldo restante es de ",retiro)
        break