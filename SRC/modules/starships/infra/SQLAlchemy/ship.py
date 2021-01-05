import sqlalchemy
from sqlalchemy import Column, Integer, String, Numeric

from base import Base


class Ship(Base):
  __tablename__ = 'ships'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  hyperdrivespeed = Column(Numeric)
  sublightspeed = Column(Numeric)

  def __repr__(self):
    return "<Ships(name='%s', hyperdrivespeed='%s', sublightspeed='%s')>" % (
      self.name, self.hyperdrivespeed, self.sublightspeed)