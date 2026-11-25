
def convertir_acciones(compania, numero_acciones, moneda):

    compania = compania.upper()
    moneda = moneda.lower()

    valor_accion = 0.0

    if compania == "NVDA":
        valor_accion = 156.20

    elif compania == "SONY":
        valor_accion = 24.16

    elif compania == "BMW":
        valor_accion = 58.12

    cantidad_acciones = numero_acciones

    valor_total_euros = valor_accion * cantidad_acciones

    valor_final = 0.0

    if moneda == "euro":

        valor_final = valor_total_euros

    elif moneda == "dolar":

        tipo_cambio = 1.10

        valor_final = valor_total_euros * tipo_cambio

    elif moneda == "libra":

        tipo_cambio = 0.83

        valor_final = valor_total_euros * tipo_cambio

    resultado = round(valor_final, 2)

    resultado_final = float(resultado)

    return resultado_final

print(convertir_acciones("NVDA", 10, "euro"))

print(convertir_acciones("SONY", 5, "dolar"))

print(convertir_acciones("BMW", 20, "libra"))