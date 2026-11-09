"""
4. Pedir al usuario un número entero y añadir todos los números de la serie de
fibonacci desde 0 hasta ese número (incluido) a una lista. Mostrar dicha lista al
acabar. Si el número introducido es menor que 0, mostrar un mensaje de error.
"""
num = int(input("Dame un número: "))

list =[0,1]

if num < 0:
    print("ERROR")
else:
    for fibonacci in range(0,(num -2)):
        list.append(list[-1] + list[-2])
print(list)




     


