from datosPokemons import pokemons

for poke in pokemons:
    if poke["nombre"][-1] == "a":
            print(poke["nombre"])