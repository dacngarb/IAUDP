from datosFieren import personajes_frieren

for personaje in personajes_frieren:
    for afiliacion in personaje["afiliacion"]:
        if afiliacion == "Magos de Primera Clase":
            print(personaje["nombre"], personaje["raza"])
            break