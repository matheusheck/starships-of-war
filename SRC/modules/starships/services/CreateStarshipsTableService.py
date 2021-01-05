# coding=utf-8

from ..infra.sqlalchemy.ship import Ship
from ....shared.infra.sqlalchemy.base import Session, engine, Base

def execute():
    Base.metadata.create_all(engine)
    session = Session()




    session.commit()
    session.close()