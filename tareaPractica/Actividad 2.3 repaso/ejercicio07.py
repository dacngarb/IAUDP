from datosPeliculas import peliculas

peliculas_infantiles = []

for pelicula in peliculas:
    if "Infantil" in pelicula["generos"]:
        peliculas_infantiles.append(pelicula)

print(peliculas_infantiles)
