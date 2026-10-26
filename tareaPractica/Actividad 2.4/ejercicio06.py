from anexo import jugadores;

"""
6. Muestra una lista con los jugadores que tienen tiro >= 8 Y regate >= 9.
"""

lista_tiro = [t for t in jugadores if t["atributos"]["tiro"] >= 8 and t["atributos"]["regate"] >= 9]
print(lista_tiro)