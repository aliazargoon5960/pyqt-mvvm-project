from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    code = Column(String)
    name = Column(String)
    family = Column(String)
    is_active = Column(Boolean)

