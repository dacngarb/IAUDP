"""
3. Pedir al usuario dos números enteros (base y potencia). Calcular el resultado de
elevar la base al exponente. Mostrar un error en caso de que la base sea menor que
1 o que la potencia sea menor que 0.
"""

base = int(input("Dame un número para la base: "))
potencia = int(input("Dame un número para la potencia: "))

calculoPotencia = 1

if base < 1 or potencia < 0:
    print("Error")
else:
    for calculo in range(potencia):
        calculoPotencia *= base
print(calculoPotencia)

