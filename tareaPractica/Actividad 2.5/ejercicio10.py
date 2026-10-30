from anexo import series;
"""
10. Muestra una lista con todos los nombres de los usuarios que hayan opinado en
alguna serie de Drama. No importa si hay nombres repetidos.
"""
listaUsuario = [(s["titulo"], u["usuario"]) for s in series for u in s["reseñas"] if "Drama" in s["generos"]]
print(listaUsuario)