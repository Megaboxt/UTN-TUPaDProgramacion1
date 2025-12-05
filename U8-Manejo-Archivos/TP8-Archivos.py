import os

ruta_archivo = "productos.txt"
productos = []

print("Bienvenido ! Corroborando si existe el archivo .txt ...\n")

# 2) Funcion para Leer y mostrar productos
def mostrar_productos():
    if os.path.exists(ruta_archivo):
        print("El archivo existe. Procediendo a leerlo...\n")

        with open(ruta_archivo, "r") as archivo:
            print("==== LISTADO DE PRODUCTOS ====\n")
            for linea in archivo:
                linea = linea.strip()
                nombre_producto, precio_producto, cantidad_producto = linea.split(",")

                print(f"Producto: {nombre_producto} | Precio: {precio_producto} | Cantidad: {cantidad_producto}")


# 3) Agregar productos
def agregar_producto():
    if os.path.exists(ruta_archivo):
        print("\n==== AGREGAR NUEVO PRODUCTO ====\n")

        nuevo_nombre = input("Ingresa el nombre del Producto: ").strip()
        while nuevo_nombre == "" or nuevo_nombre.isdigit():
            print("El nombre del producto no puede estar vacio o ser un digito. ")
            nuevo_nombre = input("Ingresa el nombre del Producto: ").strip()
        
        nuevo_precio = input("Ingresa el precio del producto: ").strip()
        while nuevo_precio == "" or not nuevo_precio.isdigit() or int(nuevo_precio) <= 0:
            print("El precio del producto no puede estar vacio, ser menor a cero o no ser un digito. ")
            nuevo_precio = input("Ingresa el precio del producto: ").strip()
        nuevo_precio = int(nuevo_precio)
        
        nuevo_cantidad = input("Ingresa el stock(cantidad) del producto: ").strip()
        while nuevo_cantidad == "" or not nuevo_cantidad.isdigit() or int(nuevo_cantidad) <= 0:
            print("El stock del producto no puede estar vacio, ser menor a cero o no ser un digito. ")
            nuevo_cantidad = input("Ingresa el stock(cantidad) del producto: ").strip()
        nuevo_cantidad = int(nuevo_cantidad)

        producto_existe = False

        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                nombre = linea.split(",")
                nombre_producto = nombre[0]

                if nuevo_nombre.lower() == nombre_producto.lower():
                    producto_existe = True
                    break

        if producto_existe:
            print("\nEl producto ya existe, no se puede agregar un producto existente.")
        else:
            with open(ruta_archivo, "a") as archivo:
                    archivo.write(f"\n{nuevo_nombre},{nuevo_precio},{nuevo_cantidad}")
            print("Producto agregado correctamente.\n")


# 4) Cargar productos en una lista de diccionarios
def productos_list():
    if os.path.exists(ruta_archivo):
        print("\n==== CARGAR PRODUCTOS EN UNA LISTA ====\n")

        with open(ruta_archivo, "r") as archivo:
            # next(archivo) # Salta la primer linea (encabezados)

            for linea in archivo:
                    linea = linea.strip()
                    nombre_producto, precio_producto, cantidad_producto = linea.split(",")

                    producto = {
                        "nombre": nombre_producto,
                        "precio": precio_producto,
                        "cantidad": cantidad_producto
                    }

                    productos.append(producto)
            print("Productos cargados correctamente en la lista.")
            print(productos)


# 5) Buscar producto por nombre
def buscar_producto():
    if os.path.exists(ruta_archivo):
        print("\n==== BUSCAR PRODUCTOS POR NOMBRE ====\n")

        buscar_producto = input("Ingresa el nombre del producto: ").strip()
        while buscar_producto == "" or buscar_producto.isdigit():
            print("El nombre del producto no puede estar vacio o ser un digito.")
            buscar_producto = input("Ingresa el nombre del producto: ").strip()
        
        producto_encontrado = False

        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                nombre_producto, precio_producto, cantidad_producto = linea.split(",")

                if nombre_producto.lower() == buscar_producto.lower():
                    print("\nProducto Encontrado:")
                    print(f"Producto: {nombre_producto} | Precio: {precio_producto} | Cantidad: {cantidad_producto}\n")
                    producto_encontrado = True
                
            if not producto_encontrado:
                print("\nNo existe un producto con ese nombre.\n")


# 6) Guardar productos
def guardar_productos():
    if os.path.exists(ruta_archivo):
        print("\n==== GUARDAR PRODUCTO ====\n")

        lista_actualizada = productos
        # print(lista_actualizada)
        with open(ruta_archivo, "w") as archivo:
            total = len(lista_actualizada)

            for i in range(total):
                producto = lista_actualizada[i]
                linea = f"{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}"

                if i < total - 1:
                    archivo.write(linea + "\n")
                else:
                    archivo.write(linea)
        print("Archivo actualizado correctamente.")


# ==== Funcion principal =====
def main():
    mostrar_productos()
    agregar_producto()
    productos_list()
    buscar_producto()
    guardar_productos()

main()