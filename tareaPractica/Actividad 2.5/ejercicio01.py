from anexo import series;
"""
1. Muestra una lista con los títulos de las series que sean de Animación.
"""
listaTitulos = [t["titulo"] for t in series if "Animación" in t["generos"]]
print(listaTitulos)