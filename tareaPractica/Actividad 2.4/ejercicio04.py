from anexo import jugadores;

"""
4. Muestra una lista con los nombres de los jugadores que tienen una puntuación de
pase igual o superior a 9 en sus atributos.
"""

lista_puntuacion = [p for p in jugadores if p["atributos"]["pase"] >= 9]
print(lista_puntuacion)

