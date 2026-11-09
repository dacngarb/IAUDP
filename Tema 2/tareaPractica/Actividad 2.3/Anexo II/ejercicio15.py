from datosFieren import personajes_frieren

for personaje in personajes_frieren:
    if personaje["raza"] == "Humano" and personaje["edad"] >= 100:
        personaje["raza"] = "Zombie"

for personaje in personajes_frieren:
    if personaje["raza"] == "Zombie":
        print(f"{personaje["nombre"]} {personaje["raza"]} {personaje["edad"]}")