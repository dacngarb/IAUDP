from datosPokemons import pokemons

pokemonMediaAltura = 0.0

contador = 0.0
for poke in pokemons:
    pokemonMediaAltura += poke["altura_m"]
    contador += 1

pokemonMediaAltura /= contador

       
for poke in pokemons:
    if poke["altura_m"] < pokemonMediaAltura:
        print(poke["altura_m"], poke["nombre"])