from datos import personajes


def ejercicio1():
    # Obtener los nombres de todos los personajes que están vivos.
    nombrePersonajes = [p["nombre"] for p in personajes if p["vivo"] == True]
    print(nombrePersonajes)


def ejercicio2():
    # Obtener los nombres de los personajes cuya clase sea Guerrero.
    nombrePersonajesG = [n["nombre"] for n in personajes if n["clase"] == "Guerrero"]
    print(nombrePersonajesG)


def ejercicio3():
    # Obtener los nombres de los personajes que tengan un nivel superior a 40.
    nombreNivel = [n["nombre"] for n in personajes if n["nivel"] > 40]
    print(nombreNivel)


def ejercicio4():
    # Obtener los nombres de los personajes que tengan la habilidad "Fuego".
    nombreHabilidadeP = [n["nombre"] for n in personajes if "Fuego" in n["habilidades"]]
    print(nombreHabilidadeP)


def ejercicio5():
    # Obtener los nombres de los personajes que tengan más de 2000 monedas.
    nombrePerMo = [n["nombre"] for n in personajes if n["estadisticas"]["monedas"] > 2000]
    print(nombrePerMo)


def ejercicio6():
    # Crear una lista aplanada con todas las habilidades
    # de todos los personajes.
    listaHabilidades = [h for n in personajes for h in n["habilidades"]]
    print(listaHabilidades)


def ejercicio7():
    # Crear una lista de tuplas con el nombre de cada personaje
    # y la suma de sus victorias y derrotas.
    listaTuplas = [(n["nombre"], n["estadisticas"]["victorias"] + n["estadisticas"]["derrotas"]) for n in personajes]
    print(listaTuplas)


def ejercicio8():
    # Crear una lista de cadenas con el nombre de cada personaje
    # seguido de su nivel.
    # Ejemplo: "Aldric: 45"
    listaCadena = [(n["nombre"] + ": " + str(n["nivel"])) for n in personajes]
    print(listaCadena)


def ejercicio9():
    # Calcular y mostrar la media de monedas de todos los personajes.
    mediaMonedas = sum([n["estadisticas"]["monedas"] for n in personajes])/ len(personajes)
    print(mediaMonedas)


def ejercicio10():
    # Calcular la media de nivel de todos los personajes
    # y crear una lista de tuplas con el nombre y el nivel
    # de aquellos personajes que superen dicha media.
    mediaNivel = sum([m["nivel"] for m in personajes])/len(personajes)
    listaTuplaNN = [(n["nombre"], n["nivel"]) for n in personajes if n["nivel"] > mediaNivel]
    print(listaTuplaNN)