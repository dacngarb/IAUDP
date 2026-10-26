from anexo import jugadores;

"""
1. Muestra una lista solo con los nombres de todos los futbolistas.
"""

lista_futbolistas = [f["nombre"] for f in jugadores]
print(lista_futbolistas)