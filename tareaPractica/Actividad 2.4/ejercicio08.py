from anexo import jugadores;

"""
8. Crea una lista de tuplas con el nombre del jugador y el texto "Goleador" si su atributo
de tiro es mayor o igual a 9, o "Asistente" en caso contrario. Muéstrala.
"""

lisra_goleador = [(g["nombre"], "Goleador") if g["atributos"]["tiro"] >= 9 else (g["nombre"], "Asistente") for g in jugadores]
print(lisra_goleador)
