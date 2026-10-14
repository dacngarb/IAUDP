from datosPokemons import pokemons

for poke in pokemons[:]:
    for tipo in poke["tipos"]:
        if tipo == "Normal":
            pokemons.remove(poke)
            break
print("\n",pokemons)
    