pdContraseña = int(input("Dame la contraseña: "))

contraseña = 12345


while pdContraseña != contraseña:
    print("Contraseña incorrecta. Intentalo de nuevo")

    pdContraseña = int(input("Dame la contraseña: "))

print("Contraseña correctamente. Bienvenido")
        