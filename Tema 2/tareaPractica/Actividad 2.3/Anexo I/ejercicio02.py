from datosPokemons import pokemons

pokemonMediaAltura = 0.0

contador = 0.0
for poke in pokemons:
    pokemonMediaAltura += poke["altura_m"]
    contador += 1

pokemonMediaAltura /= contador

       
print("Media de altura de todos los pokemons es: ",pokemonMediaAltura)

