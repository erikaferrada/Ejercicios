#Calcular el mayor de dos números ingresados por teclado usando un operador ternario

num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))

mayor = num1 if num1 > num2 else num2

print("El mayor es:", mayor)

#Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

def buscar_palabra(palabra, *args):
    resultado = "La palabra está en la lista" if palabra in args else "La palabra no está en la lista"
    print(resultado)

lista = input("Ingrese las palabras separadas por un espacio: ").split(" ")
palabra = input("Insegrese palabra a buscar: ")

buscar_palabra(palabra, *lista)

#Determinar si un número es par o impar
numero = int(input("Ingresá un número: "))

resultado = "Es par" if numero % 2 == 0 else "Es impar"

print(resultado)

#Calcular el promedio de una lista de números usando args y un operador ternario
def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else 0
    print("El promedio es:", promedio)

calcular_promedio(8, 6, 10, 4)

#Imprimir un mensaje de error si no se pasan suficientes argumentos
def calcular(*args):
    mensaje = "Error: no hay suficientes argumentos" if len(args) < 2 else "Argumentos suficientes"
    print(mensaje)

calcular(5)