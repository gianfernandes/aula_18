from sqlalchemy.sql import func
from sqlalchemy import Column, String, Integer, DateTime
from db import Base

class Pokemon(Base):
  __tablename__ = 'pokemons'
  id = Column(Integer, primary_key = True, index = True)
  name = Column(String)
  type = Column(String)
  created_at = Column(DateTime, default=func.now()) # Campo adicionado