from decimal import Decimal, ROUND_CEILING

def calcularValorBruto(precio: float, tipoIVA: str) -> float:

    # Determinar el porcentaje de IVA
    if tipoIVA == "GENERAL":
        iva = 21
    elif tipoIVA == "REDUCIDO":
        iva = 10
    elif tipoIVA == "SUPERREDUCIDO":
        iva = 4
    else:
        raise ValueError("Tipo de IVA no válido")

    # Calcular el precio con IVA
    resultado = Decimal(str(precio)) * (1 + Decimal(iva) / 100)

    # Redondear siempre hacia arriba a dos decimales
    resultado = resultado.quantize(
        Decimal("0.01"),
        rounding=ROUND_CEILING
    )

    return float(resultado)


# Ejemplos
print(calcularValorBruto(10, "GENERAL"))        # 12.1
print(calcularValorBruto(10, "REDUCIDO"))        # 11.0
print(calcularValorBruto(10, "SUPERREDUCIDO"))  # 10.4
