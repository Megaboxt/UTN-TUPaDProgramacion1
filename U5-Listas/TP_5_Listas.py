import random

# ====================================================
# 1) Crear una lista con las notas de 10 estudiantes.
# ====================================================

def listar_notas(cantidad = 10):
    print("== Ejercicio 1: Listar notas de estudiantes ==")
    notas = []

    for i in range(1, cantidad + 1):
        nota_est = input(f"Ingresa la nota del estudiante {i}: ").strip()
        nota = float(nota_est)
        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            print("Por favor, ingresa un numero entre 0 y 10.")
            break

    if len(notas) == 10:
        print("\nLista de notas: ")
        for i in range(len(notas)):
            print("Estudiante", i + 1, ":", notas[i])


        promedio = sum(notas) / len(notas)
        nota_mas_alta = max(notas)
        nota_mas_baja = min(notas)

        print("\nPromedio:", round(promedio, 2))
        print("Nota más alta:", nota_mas_alta)
        print("Nota más baja:", nota_mas_baja)
    else:
        print("Error al cargar datos en la lista de notas.")





# =========================================================
# 2) Pedir al usuario que cargue 5 productos en una lista
# =========================================================

def listar_productos(cantidad = 5):
    print("== Ejercicio 2: Lista de productos ==")
    productos = []

    for i in range(1, cantidad + 1):
        producto = input(f"Ingresá el nombre del producto {i}: ").strip()
        productos.append(producto)

    print("\nLista de productos ingresados: ")
    for i in range(len(productos)):
        print(f"{i + 1}. {productos[i]}")

    # Ordenar alfabéticamente
    productos_ordenados = sorted(productos)

    print("\nLista ordenada alfabéticamente:")
    for i in range(len(productos_ordenados)):
        print(f"{i + 1}. {productos_ordenados[i]}")


    # Eliminar un producto
    delete_ask = input("\nQuerés eliminar algún producto? (SI/NO): ")

    if delete_ask == "SI":
        eliminar = input("\nIngresá el nombre del producto que querés eliminar: ").strip()

        if eliminar in productos_ordenados:
            productos_ordenados.remove(eliminar)
            print(f"\nEl producto '{eliminar}' fue eliminado correctamente.")
        else:
            print(f"\nEl producto '{eliminar}' no se encontró en la lista.")

        # Mostrar lista final
        print("\nLista final actualizada:")
        for i in range(len(productos_ordenados)):
            print(f"{i + 1}. {productos_ordenados[i]}")
    elif delete_ask == "NO":
        print("Elegiste la opcion NO")
        # Mostrar lista final
        print("\nLista final actualizada:")
        for i in range(len(productos_ordenados)):
            print(f"{i + 1}. {productos_ordenados[i]}")
    else:
        print("Opcion incorrecta o mal tipeada.")

    # Mostrar lista final
    print("\nLista final actualizada:")
    for i in range(len(productos_ordenados)):
        print(f"{i + 1}. {productos_ordenados[i]}")





# ===================================================================
# 3) Generar una lista con 15 números enteros al azar entre 1 y 100
# ===================================================================

def numeros_azar(cantidad = 15):
    print("== Ejercicio 3: Números pares e impares ==")
    numeros = []

    # Generar números aleatorios
    for i in range(cantidad):
        num = random.randint(1, 100)
        numeros.append(num)

    print("\nLista completa de números generados:")
    for i in range(len(numeros)):
        print(f"{i + 1}. {numeros[i]}")

    # Separar pares e impares
    pares = []
    impares = []

    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    # Mostrar resultados
    print("\nNúmeros pares:")
    for i in range(len(pares)):
        print(pares[i])

    print("\nNúmeros impares:")
    for i in range(len(impares)):
        print(impares[i])

    print("\nCantidad de números pares:", len(pares))
    print("Cantidad de números impares:", len(impares))





# ========================================================================================
# 4) Dada una lista con valores repetidos, crear una nueva lista sin elementos repetidos
# ========================================================================================

def eliminar_valores_repetidos():
    print("== Ejercicio 4: Eliminar elementos repetidos ==")

    lista_original = [1, 3, 5, 3, 7, 1, 9, 5, 3]

    print("\nLista original con repetidos:")
    for i in range(len(lista_original)):
        print(f"Elemento número {i + 1}: {lista_original[i]}")

    lista_sin_repetidos = []

    for elemento in lista_original:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)

    print("\nLista sin elementos repetidos:")
    for i in range(len(lista_sin_repetidos)):
        print(f"Elemento número {i + 1}: {lista_sin_repetidos[i]}")





# ========================================================================
# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase
# ========================================================================

def listar_estudiantes_presentes(cantidad = 8):
    print("== Ejercicio 5: Lista de estudiantes ==")
    estudiantes = []

    # Cargar los nombres
    for i in range(1, cantidad + 1):
        nombre = input(f"Ingresá el nombre del estudiante {i}: ").strip()
        estudiantes.append(nombre)

    print("\nLista actual de estudiantes:")
    for i in range(len(estudiantes)):
        print(f"{i + 1}. {estudiantes[i]}")

    # Preguntar al usuario si quiere agregar o eliminar
    salir = True

    while salir:
        opcion = input("\n¿Querés agregar o eliminar un estudiante? (agregar/eliminar/salir): ").strip().lower()

        if opcion == "agregar":
            nuevo = input("Ingresá el nombre del nuevo estudiante: ").strip()
            estudiantes.append(nuevo)
            print(f"\nEl estudiante '{nuevo}' fue agregado correctamente.")
        elif opcion == "eliminar":
            borrar = input("Ingresá el nombre del estudiante que querés eliminar: ").strip()
            if borrar in estudiantes:
                estudiantes.remove(borrar)
                print(f"\nEl estudiante '{borrar}' fue eliminado correctamente.")
            else:
                print(f"\nEl estudiante '{borrar}' no se encontró en la lista.")
        elif opcion == "salir":
            salir = False
        else:
            print("\nOpción no válida. No se realizaron cambios.")

        # Mostrar la lista final
        print("\nLista final actualizada:")
        for i in range(len(estudiantes)):
            print(f"{i + 1}. {estudiantes[i]}")





# =========================================================================================
# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
# =========================================================================================

def rotar_elementos():
    print("== Ejercicio 6: Rotar elementos de una lista ==")

    numeros = [10, 20, 30, 40, 50, 60, 70]

    # Rotar ultima posición hacia la derecha (se convierte en el primero)
    ultimo = numeros[-1]
    for i in range(len(numeros) - 1, 0, -1):
        numeros[i] = numeros[i - 1]
    numeros[0] = ultimo

    print("\nLista rotada una posición a la derecha:")
    for i in range(len(numeros)):
        print(f"{i + 1}. {numeros[i]}")





# ==========================================================================
# 7) Crear una matriz con las temperaturas mínimas y máximas de una semana
# ==========================================================================

def temperaturas_min_max_semana():
    print("== Ejercicio 7: Temperaturas mínimas y máximas ==")

    temperaturas = []

    for i in range(1, 8):
        print(f"\nDía {i}:")
        temp_min = float(input("Ingresá la temperatura mínima: "))
        temp_max = float(input("Ingresá la temperatura máxima: "))
        temperaturas.append([temp_min, temp_max])

    print("\nTemperaturas registradas (Mín - Máx):")
    for i in range(len(temperaturas)):
        print(f"Día {i + 1}: {temperaturas[i][0]}°C - {temperaturas[i][1]}°C")

    # Calcular promedios
    suma_min = 0
    suma_max = 0
    for i in range(len(temperaturas)):
        suma_min += temperaturas[i][0]
        suma_max += temperaturas[i][1]

    prom_min = suma_min / len(temperaturas)
    prom_max = suma_max / len(temperaturas)

    print("\nPromedio de temperaturas mínimas:", round(prom_min, 2), "°C")
    print("Promedio de temperaturas máximas:", round(prom_max, 2), "°C")

    # Determinar el día con mayor amplitud térmica
    mayor_amplitud = 0
    dia_mayor = 0

    for i in range(len(temperaturas)):
        amplitud = temperaturas[i][1] - temperaturas[i][0]
        if amplitud > mayor_amplitud:
            mayor_amplitud = amplitud
            dia_mayor = i + 1

    print(f"\nLa mayor amplitud térmica fue de {mayor_amplitud}°C, registrada el día {dia_mayor}.")





# ==================================================================
# 8) Mostrar el promedio de los estudiantes
# ==================================================================

def promedio_estudiantes():
    print("== Ejercicio 8: Matriz de notas ==")

    estudiantes = 5
    materias = 3
    notas = []

    # Cargar las notas
    for i in range(1, estudiantes + 1):
        print(f"\nEstudiante {i}:")

        materias_alumno = []
        for j in range(1, materias + 1):
            nota_materia = input(f"Ingresá la nota de la materia {j}: ").strip()
            nota_float = float(nota_materia)

            if nota_float >= 0 and nota_float <= 10:
                materias_alumno.append(nota_float)
            else:
                print("Por favor, ingresa un numero entre 0 y 10.")
                break
        
        if len(materias_alumno) == 3:
            notas.append(materias_alumno)
        else:
            print("Error al cargar los datos, intentelo de nuevo.")
            break

    # Mostrar matriz y promedios
    if len(notas) == 5:
        print("\nLista de notas de cada estudiante:")
        for i in range(len(notas)):
            print(f"Estudiante {i + 1}: {notas[i]}")

        # Promedio de cada estudiante
        print("\nPromedio de cada estudiante:")
        for i in range(len(notas)):
            promedio_est = sum(notas[i]) / materias
            print(f"Estudiante {i + 1}: {round(promedio_est, 2)}")

        # Promedio de cada materia
        print("\nPromedio de cada materia:")
        for j in range(materias):
            suma_materia = 0
            for i in range(estudiantes):
                suma_materia += notas[i][j]
            promedio_mat = suma_materia / estudiantes
            print(f"Materia {j + 1}: {round(promedio_mat, 2)}")





# ==============================================
# 9) Representar un tablero de Ta-Te-Ti
# ==============================================

def tablero_ta_te_ti():
    print("== Ejercicio 9: Tablero de Ta-Te-Ti ==")

    # Crear tablero 
    tablero = []
    for i in range(3):
        fila = ["-", "-", "-"]
        tablero.append(fila)

    print("\nTablero inicial:")
    for fila in tablero:
        print(fila)

    def ganador(simbolo):
        # Revisar filas
        for fila in tablero:
            if fila.count(simbolo) == 3:
                return True
        # Revisar columnas
        for c in range(3):
            if tablero[0][c] == simbolo and tablero[1][c] == simbolo and tablero[2][c] == simbolo:
                return True
        # Revisar diagonales
        if tablero[0][0] == simbolo and tablero[1][1] == simbolo and tablero[2][2] == simbolo:
            return True
        if tablero[0][2] == simbolo and tablero[1][1] == simbolo and tablero[2][0] == simbolo:
            return True
        return False

    for turno in range(8):  
        jugador = "Cruz" if turno % 2 == 0 else "Circulo"
        simbolo = "X" if turno % 2 == 0 else "O"
        print(f"\nTurno del jugador {jugador}")
        
        fila = int(input("Ingresá la fila (0, 1 o 2): "))

        if fila >= 0 and fila < 3:
            columna = int(input("Ingresá la columna (0, 1 o 2): "))
            if columna >= 0 and columna <= 10:
                # Validar posición libre
                if tablero[fila][columna] == "-":
                    tablero[fila][columna] = simbolo
                else:
                    print("Esa posicion ya esta ocupada. Perdes el turno.")
                    continue

                # Mostrar tablero actualizado
                print("\nTablero actual:")
                for fila_tablero in tablero:
                    print(fila_tablero)

                if ganador(simbolo):
                    print(f"\nLinea! Gano el jugador: {jugador} ! ")
                    return
            else:
                print("El numero de la columna ingresado es incorrecto.")
                break
        else:
            print("El numero de la fila ingresado es incorrecto.")
            break

    print("\nSe acabaron los intentos, no hubo ganador.")





# ===================================================================
# 10) Registro de ventas en la tienda
# ===================================================================

def registro_ventas_tienda():
    print("== Ejercicio 10: Ventas de productos ==")

    productos = 4
    dias = 7
    ventas = []

    # Cargar datos
    for i in range(1, productos + 1):
        print(f"\nProducto {i}:")
        fila = []
        for j in range(1, dias + 1):
            venta = int(input(f"Ingresá las ventas del día {j}: "))
            fila.append(venta)
        ventas.append(fila)

    print("\nListado de productos y ventas por dia: ")
    for i in range(len(ventas)):
        print(f"Producto {i + 1}: {ventas[i]}")


    print("\nTotal vendido por cada producto:")
    totales_productos = []
    for i in range(len(ventas)):
        total = sum(ventas[i])
        totales_productos.append(total)
        print(f"Producto {i + 1}: {round(total, 2)}")

    # Día con mayores ventas totales
    totales_dias = []
    for j in range(dias):
        total_dia = 0
        for i in range(productos):
            total_dia += ventas[i][j]
        totales_dias.append(total_dia)

    dia_mayor = totales_dias.index(max(totales_dias)) + 1
    print(f"\nEl día con mayores ventas totales fue el día {dia_mayor} con {round(max(totales_dias), 2)} unidades.")

    # Producto más vendido en la semana
    producto_mayor = totales_productos.index(max(totales_productos)) + 1
    print(f"El producto más vendido en la semana fue el Producto {producto_mayor} con {round(max(totales_productos), 2)} unidades.")





# ===================================================================
# FUNCION PRINCIPAL - EJECUTA TODOS LOS BLOQUES
# ===================================================================
def main():
    listar_notas()
    listar_productos()
    numeros_azar()
    eliminar_valores_repetidos()
    listar_estudiantes_presentes()
    rotar_elementos()
    temperaturas_min_max_semana()
    promedio_estudiantes()
    tablero_ta_te_ti()
    registro_ventas_tienda()


main()