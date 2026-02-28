from sqlalchemy.orm import Session
import models, schemas

def get_employees(db:Session):
    return db.query(models.Employee).all()


def get_specific_employee(db:Session, emp_id: int):
    return ( db
            .query(models.Employee)
            .filter(models.Employee.id == emp_id)
            .first()
    )








