from anexo import jugadores;

"""
9. Muestra una lista con los nombres de los jugadores que dominan más de 2 filigranas
distintas.
"""

lista_dominan = [d["nombre"] for d in jugadores if len(d["filigranas"]) > 2]
print(lista_dominan)