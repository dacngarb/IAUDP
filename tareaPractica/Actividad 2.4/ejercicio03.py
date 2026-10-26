from anexo import jugadores;

"""
3. Muestra una lista con los nombres de los jugadores que pertenecen al "FC
Barcelona".
"""
lista_equipo = [e for e in jugadores if e["equipo"] == "FC Barcelona"]
print(lista_equipo)