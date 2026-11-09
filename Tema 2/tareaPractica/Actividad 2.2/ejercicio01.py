"""
1. Pedir al usuario un número entero y calcular el sumatorio desde 1 hasta dicho
número (incluido). Si el número introducido es menor que 1, mostrar un mensaje de
error.
"""

num1 = int(input("Dame un número: "))

calculo = 0

if num1 < 1:
    print("EROR")
else:   
    for i in range(1, num1 + 1):
        calculo = calculo + i

print(calculo)
