from anexo import series;
"""
7. Muestra una lista de tuplas (titulo_serie, comentario) para todas las reseñas que
hayan dado una puntuación de 10.
"""
listaTupla = [(n["titulo"], r["nota"]) for n in series for r in n["reseñas"] if r["nota"] == 10]
print(listaTupla)