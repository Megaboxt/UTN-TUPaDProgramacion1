# Importación de modulos
import random
import statistics


# 1) Escribir un programa que solicite la edad del usuario.

solicitar_edad = int(input("Ingresá tu edad: "))

if solicitar_edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print(" ")


# 2) Escribir un programa que solicite la nota al usuario

solicitar_nota = float(input("Ingresá tu calificación: "))

if solicitar_nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print(" ")


# 3) Escribir un programa que permita ingresar solo números pares.

solicitar_numeros_pares = int(input("Ingrese un número par: "))

if solicitar_numeros_pares % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print(" ")



# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál
# de las siguientes categorías pertenece ( niñ0, adolescente, adulto joven, adulto)

solicitar_edad_categoria = int(input("Por favor, ingrese su edad para saber su categoría: "))

if solicitar_edad_categoria >= 30:
    print("Adulto/a")
elif solicitar_edad_categoria >= 18 and solicitar_edad_categoria < 30:
    print("Adulto/a joven")
elif solicitar_edad_categoria >= 12 and solicitar_edad_categoria < 18:
    print("Adolescente")
elif solicitar_edad_categoria < 12:
    print("Niño/a")

print(" ")




# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14).

solicitar_password = input("Ingrese la contraseña: ")

if len(solicitar_password) >= 8 and len(solicitar_password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print(" ")





# 6) Escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, 
# negativo o no hay sesgo

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

print("Lista de números aleatorios:", numeros_aleatorios)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinando Sesgo
if media > mediana:
    print("La distribución presenta SESGO POSITIVO.")
elif media < mediana:
    print("La distribución presenta SESGO NEGATIVO.")
else:
    print("No hay sesgo (la distribución es simétrica).")

print(" ")





# 7) Escribir un programa que solicite una frase o palabra al usuario.

solicitar_frase = input("Por favor, ingrese una frase o palabra: ")

vocales = ["a", "e", "i", "o", "u"]

if solicitar_frase[-1] in vocales:
    print(f"{solicitar_frase}!")
else:
    print(solicitar_frase)

print(" ")




# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 
# 1, 2 o 3 dependiendo de la opción que desee para (MAYUSCULAS, minusculas, Titulo)


solicitar_nombre = input("Inregsá tu nombre: ")
solicitar_numero_opcion = int(input("Ingresá el número de opción (1, 2 o 3): "))

if solicitar_numero_opcion == 1:
    print(solicitar_nombre.upper())
elif solicitar_numero_opcion == 2:
    print(solicitar_nombre.lower())
elif solicitar_numero_opcion == 3:
    print(solicitar_nombre.title())
else:
    print("Número incorrecto. Elija entre las opciones 1, 2 o 3")


print(" ")



# 9) Escribir un programa que pida al usuario la magnitud de un terremoto.

solicitar_magnitud_terremoto = float(input("Ingrese la magnitud del terremoto según la escala de Ritcher: "))

if solicitar_magnitud_terremoto < 3:
    print("Muy leve (imperceptible).")
elif solicitar_magnitud_terremoto >= 3 and solicitar_magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible).")
elif solicitar_magnitud_terremoto >= 4 and solicitar_magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif solicitar_magnitud_terremoto >= 5 and solicitar_magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif solicitar_magnitud_terremoto >= 6 and solicitar_magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif solicitar_magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
else:
    print("La escala es negativa o incorrecta.")

print(" ")




# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
# qué mes del año es y qué día es.


hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el mes (1 al 12): "))
dia = int(input("Ingrese el día del mes: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"La estación en la que te encuentras es: {estacion}")
