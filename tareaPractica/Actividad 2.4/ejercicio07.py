from anexo import jugadores;

"""
7. Crea una lista de cadenas de texto con la forma "Nombre (Equipo)" para cada
jugador. Muéstrala.
"""
lista_cadenaTexto = [(n["nombre"], n["equipo"]) for n in jugadores]
print(lista_cadenaTexto)