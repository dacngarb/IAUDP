from anexo import series;
"""
9. Muestra una lista con todos los géneros de todas las series. No importa si hay
géneros duplicados.
"""
listaGenero = [(s["titulo"], s["generos"]) for s in series]
print(listaGenero)