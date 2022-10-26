from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1.sss123.1@postgresql/btsdemodb"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    lastname = Column(String(256))