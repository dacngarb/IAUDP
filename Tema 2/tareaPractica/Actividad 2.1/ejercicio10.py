num1 = int(input("Dame un número: "))
num2 = int(input("Dame otro número: "))



for x in range(num1, num2  +1):
    contador = 0
    for divisor in range(1, x + 1):
        if x % divisor == 0:
            contador = contador + 1  

    if (contador == 2):
        print(x," es primo")
        
    else:
        print(x," No es primo")

if num1 > num2:
    print("ERROR")
    