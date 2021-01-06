import sqlalchemy
from sqlalchemy import Column, Integer, String, Numeric

from .....shared.infra.sqlalchemy.base import Base


class Ship(Base):
  __tablename__ = 'ships'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  hyperdrivespeed = Column(Numeric)
  sublightspeed = Column(Numeric)

  def __init__(self, name, hyperdrivespeed ,sublightspeed):
        self.name = name
        self.hyperdrivespeed = hyperdrivespeed
        self.sublightspeed = sublightspeed