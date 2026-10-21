from datos import personajes;

def ejercicio1():
    personajes.append({
        "nombre": "trunks",
                "raza": "Saiyan",
                "nivel_pelea": 13000,
                "tecnicas": ["Galick Ho", "Big Bang Attack"],
                "atributos": {"fuerza": 23, "defensa": 45, "velocidad": 90}
    }) 

def ejercicio2():
    for personaje in personajes:
        atributos = personaje["atributos"]
        media = (
            atributos["fuerza"]
            + atributos["defensa"]
            + atributos["velocidad"]
        ) / 3

        if media > 80:
            print(personaje)

def ejercicio3():
    suma = 0

    for personaje in personajes:
        suma += personaje["atributos"]["velocidad"]

    media = suma / len(personajes)

    for personaje in personajes:
        if personaje["atributos"]["velocidad"] > media:
            print(personaje)

def ejercicio4():
    for personaje in personajes:
        if "Big Bang Attack" in personaje["tecnicas"]:
            fuerza = personaje["atributos"]["fuerza"]
            personaje["atributos"]["fuerza"] = min(fuerza + 10, 100)

    for personaje in personajes:
        print(
            personaje["nombre"],
            personaje["atributos"]["fuerza"]
        )

def ejercicio5():
    for personaje in personajes:
        if personaje["nombre"] == "Vegeta":
            fuerza = personaje["atributos"]["fuerza"]

    for personaje in personajes:
        if personaje["atributos"]["defensa"] < fuerza:
            print(personaje["nombre"], personaje["atributos"]["defensa"])

def ejercicio6():
    for personaje in personajes[:]:
        if personaje["raza"] == "Saiyan":
            personajes.remove(personaje)

    for personaje in personajes:
        print(personaje)