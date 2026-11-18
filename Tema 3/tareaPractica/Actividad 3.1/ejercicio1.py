def comprobarLetraDNI(dni: str) -> bool:
    """Comprobar DNI

    Args:
        dni (str): dni a comprobar

    Returns:
        bool: comprobacion si el dni es correcto ono
    """
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    valido = True
    # Comprobar que tenga 8 números y una letra
    if len(dni) != 9:
        valido = False

    if not dni[:8].isdigit() or not dni[8].isalpha():
        valido = False

    # Calcular la letra correspondiente
    numero = int(dni[:8])
    resto = numero % 23
    letra_correcta = letras[resto]

    # Comparar las letras sin distinguir mayúsculas
    return dni[8].upper() == letra_correcta


# Ejemplos
print(comprobarLetraDNI("26835432K"))  # True
print(comprobarLetraDNI("12345678A"))  # False