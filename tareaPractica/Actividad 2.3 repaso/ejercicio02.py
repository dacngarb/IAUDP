from datosPeliculas import peliculas

suma = 0

for pelicula in peliculas:
    suma += pelicula["duracion"]

media = suma / len(peliculas)

for pelicula in peliculas:
    if pelicula["duracion"] > media:
        print(pelicula["titulo"], pelicula["duracion"])
