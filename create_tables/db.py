from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

# engine = config(connec)
# Session = sessionmaker(bind=engine)
# session = Session()

Base = declarative_base()

#subclase for constructing ours maps or models.

class Message(Base):
    __tableName__ = 'messages'

    id = Column(Integer, primary_key=True)
    message = Column(String)