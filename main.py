import models, schemas, crud
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import session
from database import engine, Sessionlocal, Base
from typing import List 


Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency to get database session 
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

# endpoints
# 1. creating employee
@app.post("/employee", response_model= schemas.EmployeeOut)

def create_new_employee(employee: schemas.EmployeeCreate, db:session= Depends(get_db)):
    return crud.create_employee(db, employee)

# 2. retrieve an employee
@app.get("/employees", response_model= List[schemas.EmployeeOut])

def retrive_employees(db:session = Depends(get_db)):
    return crud.get_employees(db)

# 3. retrive specific employee
@app.get("/employee/{emp_id}", response_model=schemas.EmployeeOut)

def retrive_specific_emp(emp_id : int, db:session = Depends(get_db)):
    emp =  crud.get_specific_employee(db, emp_id)
    if emp is None:
        raise HTTPException(status_code= 404, detail="Employee not found!")
    return emp

# 4. update an employee
@app.put("/employee/{emp_id}", response_model= schemas.EmployeeOut)

def update_employee(emp_id : int,employee: schemas.EmployeeUpdate, db:session = Depends(get_db)):
    emp = crud.update_employee(db, emp_id, employee)
    if emp is None:
        raise HTTPException(status_code= 404, detail="Employee not found!")
    return emp

# 5. delete an employee
@app.delete("/employee/{emp_id}", response_model= dict)  # response_model = schemas.EmpolyeeOut if we want to return the emp object ie return emp . 

def del_employee(emp_id: int, db:session = Depends(get_db)):
    emp = crud.To_delete_employee(emp_id=emp_id, db= db)  # - Python matches arguments positionally unless you use keyword arguments.
    if emp is None:
        raise HTTPException(status_code= 404, detail="Invalid Employee Id")
    # return emp

    return {"detail":"Employee deleted."}

    
