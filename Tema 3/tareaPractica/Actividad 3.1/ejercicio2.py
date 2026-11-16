def convertirTemperatura(temperatura: float, unidadOrigen: str, unidadDestino: str) -> float:

    # Comprobar que las unidades sean válidas
    if unidadOrigen not in ("C", "K", "F") or unidadDestino not in ("C", "K", "F"):
        raise ValueError("Unidad de temperatura no válida")

    # Convertir primero a Celsius
    if unidadOrigen == "C":
        celsius = temperatura
    elif unidadOrigen == "K":
        celsius = temperatura - 273.15
    else:
        celsius = (temperatura - 32) * 5 / 9

    # Convertir de Celsius a la unidad de destino
    if unidadDestino == "C":
        resultado = celsius
    elif unidadDestino == "K":
        resultado = celsius + 273.15
    else:
        resultado = (celsius * 9 / 5) + 32

    return round(resultado, 2)


# Ejemplos
print(convertirTemperatura(10, "F", "C"))  # -12.22
print(convertirTemperatura(25, "C", "K"))  # 298.15
print(convertirTemperatura(0, "C", "F"))   # 32.0
