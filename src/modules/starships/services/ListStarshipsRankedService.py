# function recives hyperdrivespeed or underlightspeed and returns sorted by its argument

from ..infra.sqlalchemy.ship import Ship
from ....shared.infra.sqlalchemy.base import Session

def execute():
    session = Session()

    spaceships = session.query(Ship).all()
    orderedShips = sorted(spaceships, key=lambda x: x.hyperdrivespeed, reverse=False)

    return orderedShips