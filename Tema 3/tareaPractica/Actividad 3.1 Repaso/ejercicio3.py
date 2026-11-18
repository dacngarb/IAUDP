def cambiar_divisa(cantidadDinero: float, tipoDivisaActual: str, tipoDivisaConvertir: str)-> float:
    divisaActual = tipoDivisaActual.lower()
    divisaFinal = tipoDivisaConvertir.lower()

    cambioMoneda = 1
    if divisaActual == "euro":
        if divisaFinal == "dolar":
            cambioMoneda = cantidadDinero * 1.09
        elif divisaFinal == "yen":
            cambioMoneda = cantidadDinero * 163.38
    elif divisaActual == "dolar":
        if divisaFinal == "euro":
            cambioMoneda = cantidadDinero * 0.92
        elif divisaFinal == "yen":
            cambioMoneda = cantidadDinero * 149.67
    elif divisaActual == "yen":
        if divisaFinal == "euro":
            cambioMoneda = cantidadDinero * 0.0061
        elif divisaFinal == "dolar":
            cambioMoneda = cantidadDinero * 0.0067
    return round(cambioMoneda,3)

print (cambiar_divisa(50, "euro", "dolar"))