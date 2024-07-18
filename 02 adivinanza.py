# EL SCOPE es el alcance de una variable

import random


numero_secreto = random.randint(1,101)
adivinado=False
intentos=0
intentos_maximos = 7

print("JUEGO DEL NUMERO SECRETO")
print("Tienes " + str(intentos_maximos) + " intentos.")
while not adivinado:
    if intentos==intentos_maximos:
        print("¡Lo siento, se acabaron tus intentos!")
        break

    numero = int(input("Ingresa un número del 1 al 100: ")) #TODO: revisar si esto esta bien

    if numero == numero_secreto:
        print("¡Felicidades! ¡Adivinaste!")
        adivinado=True
    elif numero_secreto > numero:
        print("El numero secreto es MAYOR al que ingresaste.")
    else:
        print("El numero secreto es MENOR al que ingresaste")

    intentos+=1