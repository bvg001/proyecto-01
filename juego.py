import random
numero_real = random.randint(1, 10)

print ("!Bienvenido al juego de adivinar un numero del 1 al 10")
intento = int(input("¿cual crees que es el numero?"))

if intento == numero_real:
    print ("felicidades, ganaste!")
else:
    print (f"upss perdiste :( (el numero era {numero_real})")

