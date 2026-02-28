import pydantic
from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id : int

    class Config:
        if pydantic.__version__.startswith("1."):
            orm_mode = True # if using pydantic v2 then its not orm_mode its from_attribute=True
        else:
            from_attributes = True

