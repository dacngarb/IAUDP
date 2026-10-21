from datosPeliculas import peliculas

for pelicula in peliculas[:]:
    if pelicula["edad_recomendada"] == 0:
        peliculas.remove(pelicula)
