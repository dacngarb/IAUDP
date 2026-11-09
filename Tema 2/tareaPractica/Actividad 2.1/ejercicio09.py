num = int(input("Dame un número: "))
contador = 0
for divisor in range(1, num + 1):
        
        if num % divisor == 0:
            contador = contador + 1  

if (contador == 2):
    print(num," es primo")
        
else:
    print(num," No es primo")