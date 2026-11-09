from anexo import series;
"""
4. Muestra una lista de tuplas (titulo_serie, nota_dada) de las reseñas dejadas por el
usuario Elena.
"""

listaResenia = [(n["titulo"], r["nota"]) for n in series for r in n["reseñas"] if r["usuario"] == "Elena"]

print(listaResenia)