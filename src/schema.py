from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contrato de dados, schema de dados, a view de dados
  name: str
  type: str

  class Config:
    orm_mode = True