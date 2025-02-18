import time
import random
from controller import pega_pokemon, adiciona_pokemon_db

def main():
  while True:
    pokemon_id = random.randint(1,350) #Gera um ID aleatório entre 1 e 350
    pokemon_schema = pega_pokemon(pokemon_id)
    if pokemon_schema:
      print(f"Adicionando {pokemon_schema.name} ao banco de dados")
      adiciona_pokemon_db(pokemon_schema)
    else:
      print(f"Não foi possível obter dados para o Pokémon com ID {pokemon_id}")
    time.sleep(10)

if __name__ == "__main__":
  main()