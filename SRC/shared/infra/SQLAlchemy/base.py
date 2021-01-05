from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://usr:pass@localhost:5432/starships')
Session = sessionmaker(bind=engine)

Base = declarative_base()