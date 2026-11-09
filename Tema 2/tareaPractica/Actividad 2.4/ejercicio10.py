from anexo import jugadores;

"""
10. Extrae en una única lista todas las filigranas de todos los jugadores (no importa si
hay duplicadas) y muéstrala.
"""

lista_filigrana = [f for j in jugadores for f in j["filigranas"]]
print(lista_filigrana)