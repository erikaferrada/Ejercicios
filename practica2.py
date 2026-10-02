#Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")

#Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario

try:
    numero = 10
    texto = "hola"
    
    resultado = numero + texto
    print(f"El resultado es: {resultado}")

except TypeError:
    print(f"Error: No se puede sumar {numero} con '{texto}'.")

#Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

usuario = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Madrid"
}

try:
    email = usuario["email"]
    print(f"El correo es: {email}")

except KeyError:
    print("Error: No se encontró la clave buscada")

#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe

nombre_archivo = "archivo.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
    print("Creando el archivo...")
    
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Este archivo fue creado automáticamente.")
    
    print(f"El archivo '{nombre_archivo}' se ha sido creado correctamente")

#Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario

try:
    num3 = float(input("Ingresa el primer número: "))
    num4 = float(input("Ingresa el segundo número: "))
    
    resultado = num3 / num4
    print(f"El resultado de la división es: {resultado}")

except ValueError:
    print("Error: El valor ingresado no es un número válido.")

except ZeroDivisionError:
    print("Error: No es posible dividir por cero.")