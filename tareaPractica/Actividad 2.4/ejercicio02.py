from anexo import jugadores;

"""
2. Muestra la lista de los jugadores que llevan el dorsal número 10.
"""
lista_dorsal = [d for d in jugadores if d["dorsal"] == 10]
print(lista_dorsal)