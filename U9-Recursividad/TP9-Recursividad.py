
# Funciones reutilizables para validar 
def pedir_entero_positivo(mensaje):
    valor_ingresado = input(mensaje)
    while not valor_ingresado.isdigit():
        print("\nTenes que ingresar un numero entero positivo.\n")
        valor_ingresado = input(mensaje)
    return int(valor_ingresado)

def pedir_entero(mensaje):
    valor_ingresado = input(mensaje)
    while not valor_ingresado.lstrip("-").isdigit():
        print("\nTenes que ingresar un numero entero positivo o negativo\n")
        valor_ingresado = input(mensaje)
    return int(valor_ingresado)

def pedir_digito(mensaje):
    valor_ingresado = input(mensaje)
    while not (valor_ingresado.isdigit() and len(valor_ingresado) == 1):
        print("\nTenes que ingresar un solo digito (entre 0 y 9)\n")
        valor_ingresado = input(mensaje)
    return int(valor_ingresado)

def pedir_palabra(mensaje):
    palabra_ingresada = input(mensaje)
    while not palabra_ingresada.isalpha():
        print("\nSolo se permiten letras.\n")
        palabra_ingresada = input(mensaje)
    return palabra_ingresada


# -----------------------------------------------------------
#  EJERCICIO 1 - Calcular factorial de un numero 
# -----------------------------------------------------------

def ejercicio_1():
    print("===== CALCULAR EL FACTORIAL DE UN NUMERO =====\n")
    def calcular_factorial(numero_actual):
        if numero_actual == 0 or numero_actual == 1:
            return 1
        return numero_actual * calcular_factorial(numero_actual - 1)

    def mostrar_factoriales_hasta_limite(limite):
        print("\nFactoriales desde 1 hasta", limite)
        for numero in range(1, limite + 1):
            print(f"{numero}! = {calcular_factorial(numero)}")
        print()

    limite_factorial = pedir_entero_positivo("Ingrese un número para mostrar sus factoriales: ")
    mostrar_factoriales_hasta_limite(limite_factorial)


# -----------------------------------------------------------
#  EJERCICIO 2 - Averiguar fibonacci de un numero
# -----------------------------------------------------------

def ejercicio_2():
    print("==== CALCULAR FORMULA FIBONACCI =====\n")
    def calcular_fibonacci(posicion):
        if posicion == 0:
            return 0
        if posicion == 1:
            return 1
        return calcular_fibonacci(posicion - 1) + calcular_fibonacci(posicion - 2)

    def mostrar_fibonacci_hasta_limite(limite):
        print("\nSerie de Fibonacci hasta", limite)
        for pos in range(limite + 1):
            print(f"fibonacci({pos}) = {calcular_fibonacci(pos)}")
        print()

    limite_fibonacci = pedir_entero_positivo("Ingrese hasta qué posición desea ver Fibonacci: ")
    mostrar_fibonacci_hasta_limite(limite_fibonacci)


# -----------------------------------------------------------
#  EJERCICIO 3 - Calcular potencia de un numero
# -----------------------------------------------------------

def ejercicio_3():
    print("===== CALCULAR LA POTENCIA DE UN NUMERO =====\n")
    def calcular_potencia(base, exponente):
        if exponente == 0:
            return 1
        return base * calcular_potencia(base, exponente - 1)

    base_potencia = pedir_entero("Ingrese la base (puede ser negativa): ")
    exponente_potencia = pedir_entero_positivo("Ingrese el exponente (entero positivo): ")

    resultado = calcular_potencia(base_potencia, exponente_potencia)
    print(f"{base_potencia}^{exponente_potencia} =", resultado)
    print()


# -----------------------------------------------------------
#  EJERCICIO 4 - Convertiro numero decimal a binario
# -----------------------------------------------------------

def ejercicio_4():
    print("===== CONVERTIR NUMERO DECIMAL A BINARIO =====\n")
    def convertir_decimal_a_binario_recursivo(numero):
        if numero == 0:
            return ""
        resto = numero % 2
        return convertir_decimal_a_binario_recursivo(numero // 2) + str(resto)

    def convertir_decimal_a_binario(numero):
        if numero == 0:
            return "0"
        return convertir_decimal_a_binario_recursivo(numero)

    numero_decimal = pedir_entero_positivo("Ingrese un número decimal para convertir a binario: ")
    print("Binario:", convertir_decimal_a_binario(numero_decimal))
    print()


# -----------------------------------------------------------
#  EJERCICIO 5 - Averiguar si es una palabra palindroma
# -----------------------------------------------------------

def ejercicio_5():
    print("===== VERIFICAR PALABRAS PALINDROMAS =====\n")
    def verificar_palindromo_recursivo(cadena, izquierda, derecha):
        if izquierda >= derecha:
            return True
        if cadena[izquierda] != cadena[derecha]:
            return False
        return verificar_palindromo_recursivo(cadena, izquierda + 1, derecha - 1)

    def verificar_palindromo(cadena):
        return verificar_palindromo_recursivo(cadena, 0, len(cadena) - 1)

    palabra = pedir_palabra("Ingrese una palabra para verificar si es palíndromo: ")
    if verificar_palindromo(palabra) == True:
        print("Esta palabra es palíndroma.\n")
    else:
        print("La palabra no es palíndroma.\n")


# -----------------------------------------------------------
#  EJERCICIO 6 - Calcular la suma de todos los digitos
# -----------------------------------------------------------

def ejercicio_6():
    print("===== CALCULAR LA SUMA DE TODOS LOS DIGITOS =====\n")
    def calcular_suma_digitos(numero):
        if numero < 10:
            return numero
        ultimo = numero % 10
        resto = numero // 10
        return ultimo + calcular_suma_digitos(resto)

    numero_positivo = pedir_entero_positivo("Ingrese un número entero positivo para sumar sus dígitos: ")
    print(f"La suma de sus dígitos es: {calcular_suma_digitos(numero_positivo)}\n")


# -----------------------------------------------------------
#  EJERCICIO 7 - Calcular suma de los naturales
# -----------------------------------------------------------

def ejercicio_7():
    print("===== CONTADOR DE BLOQUES =====\n")
    def contar_bloques(n):
        if n <= 1:
            return n
        return n + contar_bloques(n - 1)

    limite = pedir_entero_positivo("Ingrese un número para contar los bloques: ")
    print(f"Cantidad de bloques: {contar_bloques(limite)}\n")


# -----------------------------------------------------------
#  EJERCICIO 8 - Contar la cant de veces que aparece un digito 
# -----------------------------------------------------------

def ejercicio_8():
    print("===== CONTAR DIGITOS =====\n")
    def contar_digitos_recursivo(numero, buscado):
        if numero == 0:
            return 0
        ultimo = numero % 10
        coincide = 1 if ultimo == buscado else 0
        return coincide + contar_digitos_recursivo(numero // 10, buscado)

    def contar_digitos(numero, buscado):
        if numero == 0:
            return 1 if buscado == 0 else 0
        return contar_digitos_recursivo(numero, buscado)

    numero_completo = pedir_entero("Ingrese un número: ")
    digito_buscado = pedir_digito("Ingrese el dígito a contar (0-9): ")

    print("Apariciones:", contar_digitos(numero_completo, digito_buscado))


# -----------------------------------------------------------
#  FUNCION PRINCIPAL (MAIN)
# -----------------------------------------------------------

def main():

    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_6()
    ejercicio_7()
    ejercicio_8()


# Ejecutar programa
main()
