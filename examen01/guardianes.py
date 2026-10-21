from datos import personajes


def ejercicio1():
    personajes.append({
        "nombre": "jett",
        "raza": "Humano",
        "ocupacion": "Agente",
        "estilo_combate":["Experta en cuchillos", "Letal"],
        "atributos":{"fuerza":55, "defensa":65, "velocidad":80}
    })

def ejercicio2():
    for personaje in personajes:
        atributos = personaje["atributos"]
        media = (atributos["fuerza"]+ atributos["defensa"]+ atributos["velocidad"]) / 3
        if media > 85:
            print(personaje)


def ejercicio3():
    suma = 0
    for personaje in personajes:
        suma += personaje["atributos"]["fuerza"]

    media = suma / len(personajes)

    for personaje in personajes:
        if personaje["atributos"]["fuerza"] > media:
            print(personaje)
        

def ejercicio6():
    for personaje in personajes[:]:
        for ocupacion in personaje["ocupacion"]:
            if ocupacion == "Cazador de demonios":
                personajes.remove(personaje)
                break
    print(personajes)
