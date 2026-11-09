from anexo import jugadores;

"""
5. Muestra la lista de los jugadores que saben hacer la filigrana "ruleta".
"""
lista_filigrana = [f for f in jugadores for j in f["filigranas"] if j == "ruleta"]
print(lista_filigrana)