def comprobar_estado(nombreEspecie: str) -> str:
    animales = [
        ["Lobo ibérico", "Mamífero", 2500],
        ["Lince ibérico", "Mamífero", 1668],
        ["Quebrantahuesos", "Ave", 2000],
        ["Oso pardo", "Mamífero", 500]
    ]

    for animal in animales:
        if animal[0] == nombreEspecie:
            ejemplares = animal[2]

            if ejemplares == 0:
                return "Extinto"
            elif ejemplares <= 500:
                return "En peligro crítico"
            elif ejemplares <= 2000:
                return "En peligro"
            else:
                return "Amenazado"

    raise ValueError("La especie no está en la lista")


print(comprobar_estado("Oso pardo"))