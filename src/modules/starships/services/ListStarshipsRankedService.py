# function recives hyperdrivespeed or underlightspeed and returns sorted by its argument

from ..infra.sqlalchemy.ship import Ship
from ....shared.infra.sqlalchemy.base import Session

def execute():
    session = Session()
    spaceships = session.query(Ship).all()
    noHyperdrive = []

    for spaceship in spaceships:
        if spaceship.hyperdrivespeed < 0:
            noHyperdrive.insert(1, spaceship)
            spaceships.remove(spaceship)

    
    orderedShips = sorted(spaceships, key=lambda x: x.hyperdrivespeed, reverse=False)
    orderedShips.extend(noHyperdrive)

    session.close()
    return orderedShips