"""Programa para determinar si, dados 3 números enteros, la suma de los 2 primeros es igual al tercero"""

x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))
z = int(input("Digite el valor de z: "))


if x + y == z:
    print("La suma de ", x, " y ", y, " es igual a ", z)

else:
    print("La suma de ", x, " y ", y, " no es igual a ", z)
    