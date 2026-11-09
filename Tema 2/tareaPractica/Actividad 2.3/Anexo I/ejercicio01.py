from datosPokemons import pokemons

pokemonPesado = pokemons[0]

for poke in pokemons:
    if poke["peso_kg"] > pokemonPesado["peso_kg"]:
        pokemonPesado = poke
print("Pokemon más pesado: ",pokemonPesado["nombre"], "Peso: ",pokemonPesado["peso_kg"], "kg")
