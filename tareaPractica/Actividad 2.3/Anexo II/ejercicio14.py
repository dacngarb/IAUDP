from datosFieren import personajes_frieren

for personaje in personajes_frieren:
    for afiliacion in personaje["afiliacion"]:
        if afiliacion == "Asociación Continental de Magia":
            personaje["afiliacion"].remove(afiliacion)
        