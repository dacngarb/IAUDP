from datosPeliculas import peliculas

for pelicula in peliculas:
    edad = pelicula["edad_recomendada"]

    if edad >= 7 and edad <= 13:
        print(pelicula["titulo"], edad)
