from datosFieren import personajes_frieren

print("Personajes con demonios: ", len(personajes_frieren))

for personaje in personajes_frieren[:]:
    if personaje["raza"] == "Demonio":
        personajes_frieren.remove(personaje)

print("Personajes sin demonios: ", len(personajes_frieren))