precioProducto = float(input("Dame el precio del producto: "))
tipoIva = str(input("Dame el tipo de IVA (General, Reducido, Superreducido): "))



if tipoIva == "General":
    print("Calculo final: ", (precioProducto * 1.21))
elif tipoIva == "Reducido":
    print("Calculo final: ", precioProducto * 1.10)
elif tipoIva == "Superreducido":
    print("Calculo final: ", precioProducto * 1.04)


match tipoIva:
    case "General":

        print("Calculo final con IVA General: ", precioProducto * 1.21)
    case "Reducido":
        print("Calculo final con IVA reducido: ", precioProducto * 1.10)
    case "Reducido":
        print("Calculo final con IVA Superreducido: ", precioProducto * 1.04)
    case _:
        print("No válida")