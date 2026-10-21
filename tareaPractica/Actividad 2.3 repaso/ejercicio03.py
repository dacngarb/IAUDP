from datosPeliculas import peliculas

for pelicula in peliculas:
    if "Drama" in pelicula["generos"]:
        pelicula["edad_recomendada"] = 18
