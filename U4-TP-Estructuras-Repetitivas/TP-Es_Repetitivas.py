import random


# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 

for contador in range(0, 101):
    print(contador)



# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un numero entero: "))

numero_str = str(abs(numero)) # abs convierte en n positivo

cantidad_digitos = len(numero_str)

print(f"El numero: {numero} tiene {cantidad_digitos} digitos.")



# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

suma_comprendidos = 0

for contador in range(numero1 + 1, numero2):
    suma_comprendidos += contador
    
print(f"La suma de los comprendidos es: {suma_comprendidos}")



# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

ingresar_num = True
suma = 0

while ingresar_num:
    numeros_ent = int(input("Ingrese un numero o cero para salir y ver la suma: "))
    
    suma += numeros_ent

    if numeros_ent == 0:
        ingresar_num = False


print(f"La suma de todos los numeros ingresados es de: {suma}")



# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

random_num = random.randint(0, 9)

print("Adivina el numero entre 0 y 9")

intentos = 0
acertado = False

while not acertado:
    intento = int(input("Ingrese un numero: "))
    intentos += 1

    if intento == random_num:
        acertado = True
        print("Adivinaste el numero!")
    else: 
        print("Numero incorrecto, intetalo de nuevo")

print(f"Cantidad de intentos: {intentos}")



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -2, -2):
    print(i)



# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.


numero_positivo = int(input("Ingrese un numero entero positivo: "))

if numero_positivo < 0:
    print("El numero debe ser positivo")
else:
    suma_positivos = 0

    for contador in range(0, numero_positivo):
        suma_positivos += contador

    print(f"La suma de todos los enteros positivos entre 0 y {numero_positivo} es: {suma_positivos}")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. indicando cuántos de estos son pares, impares, negativos y positivos. 

print("Ingrese 100 numeros enteros: ")

pares = 0
impares = 0
negativos = 0
positivos = 0
lista_numeros = 1

while lista_numeros <= 10:
    numero = int(input(f"Numero en la posicion {lista_numeros}: "))

    # Detectando numeros pares o impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares +=1

    # Indicando los negativos o positivos
    if numero < 0:
        negativos += 1
    else:
        positivos += 1

    lista_numeros += 1

print(f"La cantidad de numeros pares es de: {pares} ")
print(f"La cantidad de numeros impares es de: {impares}")
print(f"La cantidad de numeros negativos es de: {negativos}")
print(f"La cantidad de numeros positivos es de: {positivos}")



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.

print("Ingresa 100 numeros enteros para calcular el promedio: ")

N = 1
LIMITE = 10
suma = 0
promedio = 0

while N <= LIMITE:
    numero = int(input(f"Numero {N}: "))

    suma += numero

    if N == LIMITE:
        promedio = suma / LIMITE
    
    N += 1

print(F"El promedio de los {LIMITE} numeros es de: {promedio}")



# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.

digitos = int(input("Ingresa un numero para invertir su orden (mas de 2 digitos): "))
numero_original = digitos

invetir_digitos = 0

while digitos > 0:
    ultimo_digito = digitos % 10
    invetir_digitos = invetir_digitos * 10 + ultimo_digito
    digitos = digitos // 10

print(f"El numero {numero_original} invertido queda como: {invetir_digitos}")