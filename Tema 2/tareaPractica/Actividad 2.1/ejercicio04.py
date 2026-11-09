lluviaAcumulado = int(input("¿Cuántos mm de lluvia hay acumulados?: "))

if lluviaAcumulado >= 60 and lluviaAcumulado < 120:
    print("alerta amarilla")
elif lluviaAcumulado >= 120:
    print("alerta roja")

match lluviaAcumulado:
    case mm if 60 <= mm < 120:
        print("alerta amarilla")
    case mm if mm >= 120:
        print("alerta roja")
    case _:
        print("Sin alerta (lluvia normal)")
