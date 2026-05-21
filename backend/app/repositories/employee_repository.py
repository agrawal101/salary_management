from sqlalchemy.orm import Session

from backend.app.models.employee import Employee
from backend.app.schemas.employee import EmployeeCreate


class EmployeeRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, employee_data: EmployeeCreate) -> Employee:
        employee = Employee(**employee_data.model_dump())
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee
