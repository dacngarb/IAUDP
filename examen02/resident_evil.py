from datos import personajes

def ejercicio1():
    listaNombres = [n["nombre"] for n in personajes if n["afiliacion"] == "Policía de Racoon City" and n["vivo"] == True]
    print(listaNombres)

def ejercicio2():
    listaNom = [n["nombre"] for n in personajes if n["afiliacion"] == "Policía de Racoon City" and "Pistolas Samurai Edge" in n["armas"] and "Lanzagranadas" in n["armas"] ]
    print(listaNom)

def ejercicio3():
    listaTupla = [(t["nombre"], t["afiliacion"]) for t in personajes if t["afiliacion"] != "Policía de Racoon City"]
    print(listaTupla)

def ejercicio4():
    listaCadena = [(n["nombre"]+ " " + "(" + n["afiliacion"] + ")")for n in personajes if n["registro_misiones"]["misiones_completadas"] >= 20]
    print(listaCadena)

def ejercicio5():
    listaTuplas = [(n["nombre"], n["estatura_m"]*100) for n in personajes if n["estatura_m"] > 1.70]
    print(listaTuplas)

def ejercicio6():
    listaArmas = [a for n in personajes for a in n["armas"]]
    print(listaArmas)

def ejercicio7():
    listaMuertes = [n["nombre"] for n in personajes if n["registro_misiones"]["zombies_solo"] + n["registro_misiones"]["zombies_equipo"] > 100]
    print(listaMuertes)

def ejercicio8():
    listaDicci = [{"nombre" : n["nombre"], "zombies_totales" : n["registro_misiones"]["zombies_solo"] + n["registro_misiones"]["zombies_equipo"]} for n in personajes]
    print(listaDicci)

def ejercicio9():
    listaMedia = sum([m["estatura_m"] for m in personajes])/len(personajes)
    print(listaMedia)

def ejercicio10():
    listaMedia = sum([m["estatura_m"] for m in personajes])/len(personajes)
    listaTuplaMedia = [(n["nombre"], n["estatura_m"]) for n in personajes if n["estatura_m"] > listaMedia]
    print(listaTuplaMedia)