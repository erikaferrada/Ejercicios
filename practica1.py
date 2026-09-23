A = [1,5,9,13,15]
B = [1,5,9,9,11,12,13,15]

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos.
union = set(A) | set(B)
print("Unión:", union)

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B
interseccion = set(A) & set(B)
print("Intersección:", interseccion)

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
diferencia_simetrica = set(A) ^ set(B)
print("Diferencia simétrica:",diferencia_simetrica)

#Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B
print("A:",A)
print("B:",B)
es_subconjunto = set(A) <= set(B)
print("¿Es A un subconjunto de B?:", es_subconjunto)

#Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto
conjunto_A = set(A)
print("El conjunto A es:", conjunto_A)
print("El número de elementos del conjunto es:", len(conjunto_A))