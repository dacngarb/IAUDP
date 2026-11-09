from datosPeliculas import peliculas

for pelicula in peliculas:
    if "Fantasía" in pelicula["generos"] and "Aventura" in pelicula["generos"]:
        print(pelicula["titulo"], pelicula["duracion"])
