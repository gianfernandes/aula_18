import requests
from schema import PokemonSchema
from models import Pokemon
from db import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

def pega_pokemon(pokemon_id: int):
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
  if response.status_code == 200:
    data = response.json()
    types = ', '.join(type_info['type']['name'] for type_info in data['types'])
    return PokemonSchema(name=data['name'], type=types)
  else:
    return None

def adiciona_pokemon_db(pokemon_schema: PokemonSchema) -> Pokemon:
  with SessionLocal() as db:
    db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon