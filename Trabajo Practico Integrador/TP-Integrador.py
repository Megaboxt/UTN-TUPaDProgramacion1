import os
import csv

# ------------------------------------------------------------
# Utilidades
# ------------------------------------------------------------

def es_entero(valor):
    if valor.strip() == "":
        return False
    return valor.isdigit()

# ------------------------------------------------------------
# Manejo del CSV
# ------------------------------------------------------------

NOMBRE_ARCHIVO = "paises.csv"
ENCABEZADO = ["nombre", "continente", "poblacion", "superficie"]

def cargar_datos_csv():
    """Carga el CSV si existe, de lo contrario devuelve lista vacia."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("\nNo se encontró el archivo, se creara uno nuevo cuando guardes cambios.\n")
        return []

    datos = []
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        filas = list(lector)

        if len(filas) == 0 or filas[0] != ENCABEZADO:
            print("\nEl archivo CSV existe, pero su formato es incorrecto.\n")
            return []

        for fila in filas[1:]:
            if len(fila) == 4 and fila[2].isdigit() and fila[3].isdigit():
                datos.append({
                    "nombre": fila[0],
                    "continente": fila[1],
                    "poblacion": int(fila[2]),
                    "superficie": int(fila[3])
                })

    print(f"\nDatos cargados correctamente del archivo {NOMBRE_ARCHIVO}.\n")
    return datos


def guardar_datos_csv(lista_paises):

    if len(lista_paises) == 0:
        print("No hay datos cargados para guardar o actualizar")
        return
    
    # Aviso si el archivo no existe (se creara uno nuevo)
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("\nNo existe un archivo previo. Se creara uno nuevo.\n")
    else:
        print("\nActualizando archivo existente...\n")

    """Guarda todos los datos en el archivo CSV."""
    with open(NOMBRE_ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(ENCABEZADO)

        for pais in lista_paises:
            escritor.writerow([
                pais["nombre"],
                pais["continente"],
                pais["poblacion"],
                pais["superficie"]
            ])

    print("\nDatos guardados correctamente.\n")

# ------------------------------------------------------------
# Funciones del sistema
# ------------------------------------------------------------

def agregar_pais(lista):
    print("\n--- Agregar pais ---")

    nombre = input("Ingrese el nombre del Pais: ").strip()
    continente = input("Ingrese el Continente: ").strip()

    poblacion = input("Ingrese el numero de la Poblacion: ")
    while not es_entero(poblacion):
        poblacion = input("Valor invalido. Ingrese población nuevamente: ")
    poblacion = int(poblacion)

    superficie = input("Ingrese el numero de superficie: ")
    while not es_entero(superficie):
        superficie = input("Valor invalido. Ingrese superficie nuevamente: ")
    superficie = int(superficie)

    lista.append({
        "nombre": nombre,
        "continente": continente,
        "poblacion": poblacion,
        "superficie": superficie
    })

    print("\nPais agregado correctamente.\n")


def actualizar_pais(lista):

    if len(lista) == 0:
        print("\nNo existen datos para actualizar.")
        return
    
    print("\n--- Actualizar pais ---")
    nombre = input("Ingrese el nombre del pais: ").strip().lower()

    for pais in lista:
        if pais["nombre"].lower() == nombre:
            print(f"\nPais encontrado: {pais['nombre']}")

            nueva_poblacion = input("Ingrese la nueva cantidad de poblacion: ")
            while not es_entero(nueva_poblacion):
                nueva_poblacion = input("Valor invalido. Ingrese la poblacion nuevamente: ")

            nueva_superficie = input("Nueva superficie: ")
            while not es_entero(nueva_superficie):
                nueva_superficie = input("Valor invalido. Ingrese la superficie nuevamente: ")

            pais["poblacion"] = int(nueva_poblacion)
            pais["superficie"] = int(nueva_superficie)

            print("\nPais actualizado.\n")
            return

    print("\nPais no encontrado.\n")


def buscar_pais(lista):

    if len(lista) == 0:
        print("\nNo hay datos cargados para buscar.")
        return
    
    print("\n--- Buscar pais ---")
    termino = input("Ingrese nombre parcial o completo: ").strip().lower()

    resultados = []
    for pais in lista:
        if termino in pais["nombre"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print("\nNo se encontraron coincidencias.\n")
    else:
        print("\nResultados:")
        for p in resultados:
            print(f"- {p['nombre']} ({p['continente']}): "
                  f"{p['poblacion']} hab, {p['superficie']} km2")
        print()


def filtrar_por_continente(lista):

    if len(lista) == 0:
        print("\nNo hay datos cargados para filtrar")
        return
    
    cont = input("\nIngrese continente: ").strip().lower()
    filtrados = [p for p in lista if p["continente"].lower() == cont]

    if len(filtrados) == 0:
        print("\nNo se encontraron paises en ese continente.\n")
    else:
        print("\nPaises encontrados:")
        for p in filtrados:
            print(f"- {p['nombre']} ({p['poblacion']} hab)")
        print()


def filtrar_por_rangos(lista):

    if len(lista) == 0:
        print("\nNo hay datos cargados para filtrar")
        return
    
    print("\n--- Filtrar por rangos ---")

    mini = input("Ingrese la población minima: ")
    while not es_entero(mini):
        mini = input("Valor invalido. Ingrese nuevamente: ")
    mini = int(mini)

    maxi = input("Ingrese la población maxima: ")
    while not es_entero(maxi):
        maxi = input("Valor invalido. Ingrese nuevamente: ")
    maxi = int(maxi)

    filtrados = [p for p in lista if mini <= p["poblacion"] <= maxi]

    if len(filtrados) == 0:
        print("\nNo hay paises en ese rango.\n")
    else:
        print("\nResultados:")
        for p in filtrados:
            print(f"- {p['nombre']} ({p['poblacion']} hab)")
        print()


def ordenar_paises(lista):

    if len(lista) == 0:
        print("\nNo hay datos cargados para ordenar.\n")
        return

    print("""
==== Ordenar Paises ====
1. Nombre ASC
2. Nombre DESC
3. Población ASC
4. Población DESC
5. Superficie ASC
6. Superficie DESC \n""")

    opcion_ordenar = input("Seleccione una opcion: ")

    while not es_entero(opcion_ordenar):
        opcion_ordenar = input("Valor invalido. Ingrese una opcion nuevamente: ")
    opcion_ordenar = int(opcion_ordenar)

    if opcion_ordenar == 1:
        ordenados = sorted(lista, key=lambda x: x["nombre"].lower())
    elif opcion_ordenar == 2:
        ordenados = sorted(lista, key=lambda x: x["nombre"].lower(), reverse=True)
    elif opcion_ordenar == 3:
        ordenados = sorted(lista, key=lambda x: x["poblacion"])
    elif opcion_ordenar == 4:
        ordenados = sorted(lista, key=lambda x: x["poblacion"], reverse=True)
    elif opcion_ordenar == 5:
        ordenados = sorted(lista, key=lambda x: x["superficie"])
    elif opcion_ordenar == 6:
        ordenados = sorted(lista, key=lambda x: x["superficie"], reverse=True)
    else:
        print("\nOpción invalida.\n")
        return

    print("\nPaises ordenados:")
    for p in ordenados:
        print(f"- {p['nombre']}: {p['poblacion']} hab, {p['superficie']} km2")
    print()


def estadisticas(lista):
    if len(lista) == 0:
        print("\nNo hay datos cargados para poder hacer una estadistica.\n")
        return

    mayor = max(lista, key=lambda x: x["poblacion"])
    menor = min(lista, key=lambda x: x["poblacion"])
    promedio_p = sum(p["poblacion"] for p in lista) / len(lista)
    promedio_s = sum(p["superficie"] for p in lista) / len(lista)

    conteo_cont = {}
    for p in lista:
        continente = p["continente"]
        if continente not in conteo_cont:
            conteo_cont[continente] = 0
        conteo_cont[continente] += 1

    print("\n--- Estadisticas ---")
    print(f"Pais con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"Pais con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Población promedio: {promedio_p:.2f}")
    print(f"Superficie promedio: {promedio_s:.2f}")
    print("\nPaises por continente:")
    for c, cant in conteo_cont.items():
        print(f"- {c}: {cant}")
    print()


# ------------------------------------------------------------
# Funcion principal (main)
# ------------------------------------------------------------

def menu():
    paises = cargar_datos_csv()

    while True:
        print("""
=============================
GESTIÓN DE PAiSES
=============================
1. Agregar pais
2. Actualizar pais
3. Buscar pais
4. Filtrar por continente
5. Filtrar por rangos de población
6. Ordenar paises
7. Estadisticas
8. Guardar cambios
9. Salir
""")

        opcion_menu = input("Seleccione una opción: ")

        while not es_entero(opcion_menu):
            opcion_menu = input("Valor invalido. Ingrese una opcion nuevamente: ")
        opcion_menu = int(opcion_menu)

        if opcion_menu == 1:
            agregar_pais(paises)
        elif opcion_menu == 2:
            actualizar_pais(paises)
        elif opcion_menu == 3:
            buscar_pais(paises)
        elif opcion_menu == 4:
            filtrar_por_continente(paises)
        elif opcion_menu == 5:
            filtrar_por_rangos(paises)
        elif opcion_menu == 6:
            ordenar_paises(paises)
        elif opcion_menu == 7:
            estadisticas(paises)
        elif opcion_menu == 8:
            guardar_datos_csv(paises)
        elif opcion_menu == 9:
            print("\nSaliendo del sistema...\n")
            return
        else:
            print("\nOpción invalida.\n")



# Ejecutando programa principal
menu()
