from datosFieren import personajes_frieren

for personaje in personajes_frieren:
    for afiliacion in personaje["afiliacion"]:
        if afiliacion == "Grupo de los Cuatro Héroes":
            print(f"{personaje["nombre"]} {personaje["raza"]} {personaje["edad"]}")