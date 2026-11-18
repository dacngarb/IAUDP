def sumatorio(numeroPositivo: int) -> int:
    if numeroPositivo < 0:
        raise ValueError("El número debe ser positivo o cero.")

    resultado = 0
    for i in range(numeroPositivo + 1):
        resultado += i

    return resultado


def factorial(numeroMayor1: int) -> int:
    if numeroMayor1 < 1:
        raise ValueError("El número debe ser mayor o igual a 1.")

    resultado = 1
    for i in range(1, numeroMayor1 + 1):
        resultado *= i

    return resultado


def aplicar_funcion(valorNumerico: int, cadenaTexto: str) -> int:
    if cadenaTexto == "sumatorio":
        return sumatorio(valorNumerico)

    elif cadenaTexto == "factorial":
        return factorial(valorNumerico)

    else:
        raise ValueError("Función no reconocida.")


# Ejemplos
print(aplicar_funcion(3, "sumatorio"))  # 6
print(aplicar_funcion(3, "factorial"))  # 6

