print("ACTIVIDAD 1")
for i in range(1, 11):
    if i % 2 != 0:
        print(i)

print(" ")
print("ACTIVIDAD 2")
cont = int(0)

while cont < 11:
    cont += 1
    if cont % 2 != 0:
        print(cont)
        
print(" ")
print("ACTIVIDAD 3")

while True:
    word = str(input("Ingrese la palabra por favor:"))
    if word == "chupacabra":
        print("felicidades,B!Has dejado el bucle con C)xito")
        break

print(" ")
print("ACTIVIDAD 4")
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

for letra in user_word:
    if letra in ("A", "E", "I", "O", "U"):
        continue
    print(letra)
    
print(" ")
print("ACTIVIDAD 5")

blocks = int(input("Ingresa la cantidad de bloques: "))
altura = 0
bloques_usados = 0

while True:
    altura += 1
    bloques_usados += altura
    if bloques_usados > blocks:
        altura -= 1
        break

print("La altura de la pirámide es:", altura)

