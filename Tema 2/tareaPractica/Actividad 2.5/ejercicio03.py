from anexo import series;
"""
3. Muestra los títulos de las series que tengan una nota igual o superior a 9 y que
además tengan 3 o más géneros.
"""
tituloseriesNota = [n["titulo"] for n in series if n["nota"] >= 9 and len(n["generos"]) >= 3]
print(tituloseriesNota)
