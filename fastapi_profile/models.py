from sqlalchemy import JSON, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Measures(Base):
    __tablename__ = "measures"

    id = Column(Integer, primary_key=True)
    path = Column(String(256))
    method = Column(String(256))
    headers = Column(JSON)
    url = Column(String(256))
    query_params = Column(JSON)
    path_params = Column(JSON)
    form = Column(JSON)
    body = Column(JSON)
    elapsed = Column(Float)
