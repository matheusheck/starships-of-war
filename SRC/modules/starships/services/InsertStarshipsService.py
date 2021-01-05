# coding=utf-8

from ship import ship
from base import Session, engine, Base


Base.metadata.create_all(engine)

session = Session()


slave_1 = Ship("Slave I", 1, 2.5)
e_wing_fighter = Ship("E-Wing Starfighter", 2, 4.2)
lady_luck = Ship("Lady Luck", 1, 2.2)
jade_shadow = Ship("Slave I", 0.5, 2.5)
hound_tooth = Ship("Hound Tooth", 1.5, 2.5)
ig_2000 = Ship("IG-2000", 2, 2.5)
sharp_spiral = Ship("Sharp Spiral", 0.6, 4.8)
naboo_royal = Ship("Naboo Royal Starship", 1.8, 2.5)
naboo_cruiser = Ship("Naboo Cruiser", 0.8, 2.4)


session.add(slave_1)
session.add(e_wing_fighter)
session.add(lady_luck)
session.add(jade_shadow)
session.add(hound_tooth)
session.add(ig_2000)
session.add(sharp_spiral)
session.add(naboo_royal)
session.add(naboo_cruiser)


session.commit()
session.close()