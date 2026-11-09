from datosPokemons import pokemons

for poke in pokemons:
    for pokeTipo in poke["tipos"]:
        if pokeTipo == "Agua":
            print(poke["nombre"], poke["tipos"])