from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://cotzugyr:gNFad4ZCwP50TJG0uB_cMr5izbrqMoii@motty.db.elephantsql.com/cotzugyr")
Base = declarative_base
Session = sessionmaker(bind=engine)
session = Session()