import math

# 1)
def imprimir_hola_mundo():
    print("Hola Mundo!\n")

# 2) 
def saludar_usuario(nombre):
    print(f"Hola {nombre}!\n")
    
# 3)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}\n")


# 4) Calcular Area y Perimetro de un Circulo
def calcular_area_circulo(radio):
    area = math.pi * radio * radio
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

# 5) 
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# 6) 
def tabla_multiplicar(numero):
    print()
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)
    print()

# 7) 
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

# 8)
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

# 9)
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 10)
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


# Programa Principal
def main():
    
    # 1) Imprimir saludo
    imprimir_hola_mundo()

    # 2) Saludar Usuario
    usuario_nombre = input("Por favor, ingresa tu nombre: ").strip()
    while usuario_nombre == "" or usuario_nombre.isdigit():
        print("El nombre no puede estar vacio o ser un valor numerico.")
        usuario_nombre = input("Por favor, ingresa tu nombre: ").strip()
    saludar_usuario(usuario_nombre)

    # 3) Pedir Datos Personales
    print("DATOS PERSONALES\n")

    info_personal_nombre = input("Ingresa tu nombre: ").strip()
    while info_personal_nombre == "" or info_personal_nombre.isdigit():
        print("Ingrese un nombre valido, evite utilizar numeros")
        info_personal_nombre = input("Ingresa tu nombre: ").strip()

    info_personal_apellido = input("Ingresa tu apellido: ").strip()
    while info_personal_apellido == "" or info_personal_apellido.isdigit():
        print("Ingrese un apellido valido, evite utilizar numeros")
        info_personal_apellido = input("Ingresa tu apellido: ").strip()

    
    info_personal_edad = input("Ingresa tu edad: ").strip()
    while info_personal_edad == "" or not info_personal_edad.isdigit():
        print("El campo no puede estar vacio y debe ser un valor numerico.")
        info_personal_edad = input("Ingresa tu edad: ").strip()
    info_personal_edad = int(info_personal_edad)        


    info_personal_residencia = input("Ingresa la ciudad donde vivis: ").strip()
    while info_personal_residencia == "" or info_personal_residencia.isdigit():
        print("Debe ingresar un nombre de ciudad valido.")
        info_personal_residencia = input("Ingresa la ciudad donde vivis: ").strip()
    informacion_personal(info_personal_nombre, info_personal_apellido, info_personal_edad, info_personal_residencia)


    # 4) Calcular Area y Perimetro de un Circulo
    print("CALCULAR AREA Y PERIMETRO\n")
    
    radio = input("Ingrese el radio del círculo: ").strip()

    while radio == "" or not radio.isdigit():
        print("El valor del radio debe ser numérico.")
        radio = input("Ingrese el radio del círculo: ").strip()
    radio = float(radio)

    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es: {round(area, 2)}")
    print(f"El perímetro del círculo es: {round(perimetro, 2)}\n")

    # 5) Pasar segundos a horas
    print("PASAR SEG A HS\n")

    segundos = input("Ingresa la cantidad de segundos: ").strip()
    while segundos == "" or not segundos.isdigit():
        print("El valor de los segundos debe ser numérico.")
        segundos = input("Ingresa la cantidad de segundos: ").strip()
    segundos = float(segundos)
    resultado_segundos_a_horas = segundos_a_horas(segundos)
    print(f"La cantidad en horas es de: {round(resultado_segundos_a_horas, 2)}\n")

    # 6) Funcion Tabla de multiplicar
    print("TABLA DE MULTIPLICACION\n")

    numero_tabla = input("Ingrese el numero a multiplicar: ")
    while numero_tabla == "" or not numero_tabla.isdigit():
        print("El campo no puede estar vacio y debe ser un valor numerico.")
        numero_tabla = input("Ingrese el numero a multiplicar: ").strip()
    numero_tabla = int(numero_tabla)
    tabla_multiplicar(numero_tabla)

    # 7) Operaciones matematicas
    print("OPERACIONES MATEMATICAS\n")

    a = input("Ingrese el primer numero: ").strip()
    while a == "" or not a.isdigit():
        print("El campo no puede estar vacio y debe ser un valor numerico.")
        a = input("Ingrese el primer numero: ").strip()
    a = int(a)

    b = input("Ingrese el segundo numero: ").strip()
    while b == "" or not b.isdigit():
        print("El campo no puede estar vacio y debe ser un valor numerico.")
        b = input("Ingrese el primer numero: ").strip()
    b = int(b)
    resultado_operaciones_basicas = operaciones_basicas(a, b)
    print("\nResultado de las operaciones matematicas: \n")
    print(f"Suma: {resultado_operaciones_basicas[0]}")
    print(f"Resta: {resultado_operaciones_basicas[1]}")
    print(f"Multiplicación: {resultado_operaciones_basicas[2]}")
    print(f"División: {resultado_operaciones_basicas[3]}\n")

    # 8) Calcular el Indice de Masa Corporal
    print("CALCULAR INDICE DE MASA CORPORAL\n")

    indice_peso = input("Ingresa tu peso en kg: ").strip()
    while indice_peso.replace(".", "", 1).isdigit() == False or indice_peso == "":
        print("El campo no puede estar vacío y debe ser un valor numérico.")
        indice_peso = input("Ingresa tu peso en kg: ").strip()
    indice_peso = float(indice_peso)

    indice_altura = input("Ingresa tu altura en metros: ").strip()
    while indice_altura.replace(".", "", 1).isdigit() == False or indice_altura == "":
        print("El campo no puede estar vacío y debe ser un valor numérico.")
        indice_altura = input("Ingresa tu altura en metros: ").strip()
    indice_altura = float(indice_altura)

    resultado_calcular_imc = calcular_imc(indice_peso, indice_altura)
    print(f"El Indice de tu Masa Corporal es de: {round(resultado_calcular_imc, 2)}\n")



    # 9) Calcular grados Celsius
    print("CALCULAR GRADOS CELSIUS\n")
    temperatura_celsius = input("Ingresá la temperatura en Celsius: ").strip()
    while temperatura_celsius == "" or not temperatura_celsius.isdigit():
        print("El campo no puede estar vacio y debe ser un valor numerico.")
        temperatura_celsius = input("Ingresa tu altura en metros: ").strip()
    temperatura_celsius = float(temperatura_celsius)
    resultado_pasar_celsius_a_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
    print(f"La temperatura en Fahrenheit es: {resultado_pasar_celsius_a_fahrenheit}\n")


    # 10) Calcular promedio
    print("CALCULAR PROMEDIO\n")
    numero_promedio_1 = input("Ingresa el primer número: ").strip()
    while numero_promedio_1 == "" or not numero_promedio_1.isdigit():
        print("El campo no puede estar vacio y debe ser un valor numerico.")
        numero_promedio_1 = input("Ingresa tu altura en metros: ").strip()
    numero_promedio_1 = float(numero_promedio_1)

    numero_promedio_n2 = input("Ingresa el segundo número: ").strip()
    while numero_promedio_n2 == "" or not numero_promedio_n2.isdigit():
        print("El campo no puede estar vacio y debe ser un valor numerico.")
        numero_promedio_n2 = input("Ingresa tu altura en metros: ").strip()
    numero_promedio_n2 = float(numero_promedio_n2)

    numero_promedio_n3 = input("Ingresa el tercer número: ").strip()
    while numero_promedio_n3 == "" or not numero_promedio_n3.isdigit():
        print("El campo no puede estar vacio y debe ser un valor numerico.")
        numero_promedio_n3 = input("Ingresa tu altura en metros: ").strip()
    numero_promedio_n3 = float(numero_promedio_n3)

    resultado_calcular_promedio = calcular_promedio(numero_promedio_1, numero_promedio_n2, numero_promedio_n3)
    print(f"El promedio de los tres números es: {resultado_calcular_promedio}")



# Ejecutando la funcion
main()
