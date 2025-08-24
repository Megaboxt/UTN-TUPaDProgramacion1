# Importando modulos 
import math


# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

print(" ")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

saludar_nombre = input("Ingrese su nombre: ")

print(f"Hola {saludar_nombre}!")

print(" ")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ej: el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”

nombre_oracion = input("Ingrese otro nombre: ")
apellido_oracion = input("Ingrese su apellido: ")
edad_oracion = int(input("Ingrese su edad: "))
lugar_residencia = input("Ingrese el lugar donde reside: ")

print(f"Soy {nombre_oracion} {apellido_oracion}, tengo {edad_oracion} años y vivo en {lugar_residencia}")

print(" ")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio del circulo: "))

area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

print(" ")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

solicitar_segundos = int(input("Ingresá la cantidad de segundos: "))

horas = solicitar_segundos / 3600

print(f"Los segundos equivalen a: {horas} horas")

print(" ")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.


tabla_multiplicar_n = int(input("Ingresá un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del número: {tabla_multiplicar_n}")

for i in range(1, 11):
    print(f"{tabla_multiplicar_n} x {i} = {tabla_multiplicar_n * i}")

print(" ")


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

primer_numero = int(input("Ingresá el primer número entero (distinto de 0): "))
segundo_numero = int(input("Ingresá el segundo número entero (distinto de 0): "))

if primer_numero == 0 or segundo_numero == 0:
    print("Los números deben ser distintos de cero.")
else:
    resultado_suma = primer_numero + segundo_numero
    resultado_resta = primer_numero - segundo_numero
    resultado_multiplicacion = primer_numero * segundo_numero
    resultado_division = primer_numero / segundo_numero

    print(f"La suma de {primer_numero} y {segundo_numero} es: {resultado_suma}")
    print(f"La resta de {primer_numero} y {segundo_numero} es: {resultado_resta}")
    print(f"La multiplicación de {primer_numero} y {segundo_numero} es: {resultado_multiplicacion}")
    print(f"La división de {primer_numero} y {segundo_numero} es: {resultado_division}")

print(" ")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 
# IMC = peso en kg /(altura en m)2

altura = float(input("Ingresá tu altura en metros: "))
peso = float(input("Ingresá tu peso en kilogramos: "))

imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal es de: {imc:.2f}")

print(" ")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 / 5 . Temperatura en Celsius + 32

celsius = float(input("Ingresá la temperatura en grados Celsius: "))

fahrenheit = 9 / 5 * celsius + 32

print(f"{celsius} grados Celsius equivalen a: {fahrenheit:.2f} grados fahrenheit.")

print(" ")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))

promedio = (num1 + num2 + num3 ) / 3

print(f"El promedio de los tres números es: {promedio}")