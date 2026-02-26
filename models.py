from sqlalchemy import Column, String, Integer # C capital for Column
from database import Base


class Employee(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    email = Column(String, unique= True, index = True)
