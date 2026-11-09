nota = int(input("Introduce un número: "))

match nota:
    case 1  | 2 | 3 | 4:
        print("Suspenso")
    case 5 | 6:
        print("Aprobado")
    case 7 | 8:
        print("Notable")
    case 9 | 10:
        print("Sobresaliente")
    case _:
        print("No válida")

if nota >= 0 and nota < 5: 
    print("Suspenso")
elif nota == 5 or nota == 6: 
    print("Aprobado")
elif nota == 7 or nota == 8:
    print("Notable")
elif nota == 9 or nota == 10:
    print ("Sobresaliente")
else:
    print("No válida")
