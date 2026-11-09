edad = int(input("Dime tu edad: "))

if edad >= 0 and edad < 18:
    print("Es menor de edad")
elif edad < 0:
    print("ERROR")
elif edad >= 18 and edad <= 120:
    print("Es mayor  de edad")
elif edad > 120:
    print("Es un vampiro")
