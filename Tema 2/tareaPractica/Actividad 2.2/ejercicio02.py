"""
2. Pedir al usuario un número entero y 
calcular el factorial desde 1 hasta dicho número
(incluido). Si el número introducido 
es menor que 1, mostrar un mensaje de error.
"""

num = int(input("Dame un número: "))

calculo = 1

if num < 1:
    print("EROR")
else:   
    for i in range(1, num +1):
        calculo = calculo * i

print(calculo)

