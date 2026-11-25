def convertir_acciones(compania: str, numero_acciones: int, moneda_cambio: str)-> float:

    compania = compania.upper()
    moneda_cambio = moneda_cambio.lower()

    valor_accion = 0.0

    if compania == "NVDA":
        valor_accion = 156.20
    elif compania == "SONY":
        valor_accion = 24.16
    elif compania == "BMW":
        valor_accion = 58.12
        
    valor_total_euros = valor_accion * numero_acciones


    valor_final = 0.0

    if moneda_cambio == "euro":
        valor_final = valor_total_euros
    elif moneda_cambio == "dolar":
        tipo_cambio = 1.10
        valor_final = valor_total_euros * tipo_cambio
    elif moneda_cambio == "libra":
        tipo_cambio = 0.83
        valor_final = valor_total_euros * tipo_cambio

    return round(valor_final, 2)

print(convertir_acciones("NVDA", 10, "euro"))
print(convertir_acciones("SONY", 5, "dolar"))
print(convertir_acciones("BMW", 20, "libra"))