import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contrato de dados, schema de dados, a view de dados
  name: str
  type: str

  class Config:
    orm_mode = True

def pegar_pokemon(id: int):
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
  data = response.json()
  data_types = data['types']
  types_list = []
  for type_info in data_types:
    types_list.append(type_info['type']['name'])
  types = ', '.join(types_list)
  return PokemonSchema(name=data['name'], type=types)

if __name__ == "__main__":
  numero = 0
  while numero != 'sair':
    numero = input('Informe o número de um pokemon (escreva "sair" para sair): ')
    if numero != 'sair':
      pokemon = pegar_pokemon(numero)
      print(pokemon)
