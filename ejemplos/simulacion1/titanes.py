from datos import personajes

def ejercicio1():
    listaNombres = [n["nombre"] for n in personajes if n["afiliacion"] == "Cuerpo de Exploración" and n["vivo"] == True]
    print(listaNombres)

def ejercicio2():
    nombrePersonajes = [
        n["nombre"] for n in personajes
        if n["afiliacion"] == "Cuerpo de Exploración"
        and "Supervivencia" in n["habilidades"]
        and "Sigilo" in n["habilidades"]
    ]
    print(nombrePersonajes)

def ejercicio3():
    listaTuplas = [(n["nombre"], n["afiliacion"])for n in personajes if n["afiliacion"] != "Cuerpo de Exploración"]
    print(listaTuplas)

def ejercicio4():
    listaCadena = [(n["nombre"]+ " " + "(" + n["afiliacion"] + ")")for n in personajes if n["registro_combate"]["misiones_completadas"] >= 20]
    print(listaCadena)

def ejercicio5():
    listaTupNomb = [(n["nombre"], n["estatura_m"]*100)for n in personajes if n["estatura_m"] > 1.70]
    print(listaTupNomb)

def ejercicio6():
    listaAplanada = [h for n in personajes for h in n["habilidades"]]
    print(listaAplanada)

def ejercicio7():
    titanesMatado = [n["nombre"]
        for n in personajes
        if n["registro_combate"]["titanes_solo"] + n["registro_combate"]["titanes_equipo"] >= 5]
    print(titanesMatado)

def ejercicio8():
    listaAtributos = [(n["nombre"] + ": " + str(n["registro_combate"]["titanes_solo"] + n["registro_combate"]["titanes_equipo"])) for n in personajes]
    print(listaAtributos)

def ejercicio9():
    listaMedia = sum([m["estatura_m"] for m in personajes]) / len(personajes)
    print(listaMedia)

def ejercicio10():
    listaMedia = sum([m["estatura_m"] for m in personajes]) / len(personajes)
    listaAltMed = [(n["nombre"], n["estatura_m"]) for n in personajes if n["estatura_m"] > listaMedia]
    print(listaAltMed)