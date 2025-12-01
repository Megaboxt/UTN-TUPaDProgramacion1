
# 1) Dado el diccionario precios_frutas
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)
print()



# 2) actualizar los precios de las siguientes frutas [Banana = 1330, Manzana = 1700, Melón = 2800]

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)
print()


# 3) Convertir el diccionario en una lista de solo keys

precios_frutas_sin_precio = list(precios_frutas.keys())

print(precios_frutas_sin_precio)


# 4) Agenda de contactos

contactos = {}

for i in range(5):
    nombre_contacto = input(f"\nIngresa el nombre del contacto {i+1}: ").strip()
    if nombre_contacto == "" or nombre_contacto.isdigit():
        print("El campo debe tener un nombre y no debe ser numerico.")
    numero_contacto = input(f"\nIngresa el numero del contacto {i+1}: ").strip()
    if numero_contacto == "" or not numero_contacto.isdigit():
        print("El campo debe contener un numero telefonico.")
    else:
        numero_contacto = int(numero_contacto)
    contactos[nombre_contacto] = numero_contacto
print(contactos)

buscar_nombre_contacto = input("\nIngrese el nombre que desea buscar: ").strip()

if buscar_nombre_contacto in contactos:
    if contactos[buscar_nombre_contacto] == "":
        print("Contacto agendado sin numero.")

if buscar_nombre_contacto in contactos:
    print(f"El número de {buscar_nombre_contacto} es: {contactos[buscar_nombre_contacto]}")
else:
    print("Ese nombre no existe en la agenda.")


# 5) Solicitar una frase

frase = input("Ingresa una frase: ").strip()
palabras = frase.split()
palabras_unicas = set(palabras)

recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Muestra resultados
print(f"Palabras_únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")


# 6) Sacar Promedio de notas 

alumnos = {}

for i in range(3):
    nombre_alumno = input(f"\nIngresar el nombre del alumno {i+1}: ").strip()

    notas_alumno = tuple(float(input(f"Ingrese la nota {j+1} de {nombre_alumno}: ")) for j in range(3))
    alumnos[nombre_alumno] = notas_alumno


print("\nPROMEDIO DE NOTAS")
for nombre_alumno, notas_alumno in alumnos.items():
    promedio = sum(notas_alumno) / len(notas_alumno)
    print(f"{nombre_alumno}: {round(promedio, 2)}")



# 7) Lista de Aprobados

aprobaron_parcial_1 = {"Ana", "Jorge", "Luis"}
aprobaron_parcial_2 = {"Maria", "Pedro", "Carla", "San pedro"}

aprobaron_ambos_parciales = aprobaron_parcial_1 and aprobaron_parcial_2

aprobaron_solo_uno = aprobaron_parcial_1 ^ aprobaron_parcial_2

almenos_uno = aprobaron_parcial_1 | aprobaron_parcial_2

print(f"Aprobaron ambos parciales: {aprobaron_ambos_parciales}")
print(f"Aprobaron solo uno: {aprobaron_solo_uno}")
print(f"Aprobaron al menos un parcial: {almenos_uno}")



# 8) Diccionario de Productos

stock_productos = {
    "manzana": 10,
    "Naranja": 72,
    "mandarina": 25,
    "manteca": 21,
}

opcion = ""

while opcion != "4":
    print("\nMENÚ DE STOCK")
    print("1) Consultar stock")
    print("2) Agregar unidades a un producto existente")
    print("3) Agregar un producto nuevo")
    print("4) Salir")
    
    opcion = input("Elija una opción: ").strip()
    while opcion == "" or not opcion.isdigit():
        print("Valor ingresado incorrecto.")
        opcion = input("Elija una opción: ").strip()

    # 1) Consultar stock
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ").lower()
        
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]}")
        else:
            print("El producto no existe")

    # 2) Agregar unidades a un producto existente
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ").lower()

        if producto in stock_productos:
            unidades = int(input("Cuantas unidades queres agregar?: "))
            stock_productos[producto] = stock_productos[producto] + unidades
            print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
        else:
            print("Ese producto no existe.")

    # 3) Agregar un producto nuevo
    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ").lower()

        if producto in stock_productos:
            print("El producto ya existe.")
        else:
            unidades_iniciales = int(input("Ingrese el stock inicial: "))
            stock_productos[producto] = unidades_iniciales
            print("Producto agregado correctamente.")

    # 4) Salir
    elif opcion == "4":
        print("Saliendo del programa...")

    else:
        print("Opción incorrecta. Intente nuevamente.")

print("\nDiccionario final actualizado: ")
print(stock_productos)


# 9) Agenda de tuplas

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de Inglés",
    ("viernes", "18:30"): "Gimnasio"
}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (por ejemplo 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividad programada en ese día y hora.")



# 10) Diccionario Invertido

# Diccionario original
diccionario_original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
}

# Diccionario invertido
diccionario_invertido = {}

for pais, capital in diccionario_original.items():
    diccionario_invertido[capital] = pais

print("Diccionario invertido:")
print(diccionario_invertido)
