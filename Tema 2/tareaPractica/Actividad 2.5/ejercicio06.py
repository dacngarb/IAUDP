from anexo import series;

"""
6. Muestra una lista de cadenas con el formato “La serie {titulo} tiene {n} reseñas”, para
todas las series.
"""
listaCadena = [("La serie " + s["titulo"] + " tiene " + str(len(s["reseñas"])) + " reseñas") for s in series]
print(listaCadena)