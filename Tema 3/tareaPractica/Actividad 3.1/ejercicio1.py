def comprobarLetraDNI(dni: str) -> bool:
    """Comprobar DNI

    Args:
        dni (str): dni a comprobar

    Returns:
        bool: comprobacion si el dni es correcto ono
    """
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    # Comprobar que tenga 8 números y una letra
    if len(dni) != 9:
        return False

    if not dni[:8].isdigit() or not dni[8].isalpha():
        return False

    # Calcular la letra correspondiente
    numero = int(dni[:8])
    resto = numero % 23
    letra_correcta = letras[resto]

    # Comparar las letras sin distinguir mayúsculas
    return dni[8].upper() == letra_correcta


# Ejemplos
print(comprobarLetraDNI("12345678Z"))  # True
print(comprobarLetraDNI("12345678A"))  # False