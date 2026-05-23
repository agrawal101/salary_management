from sqlalchemy.orm import Session
from fastapi import HTTPException, status
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
    
    def get_by_id(self, employee_id: int):
        employee = (
            self.db.query(Employee)
            .filter(Employee.id == employee_id)
            .first()
        )

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        return employee
    
    def get_all(self, page: int, size: int):
        offset = (page - 1) * size
        return (
            self.db.query(Employee)
            .offset(offset)
            .limit(size)
            .all()
        )
    
    def update(self, employee_id: int, employee_data: EmployeeCreate):
        employee = self.get_by_id(employee_id)
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        employee.full_name = employee_data.full_name
        employee.job_title = employee_data.job_title
        employee.country = employee_data.country
        employee.salary = employee_data.salary

        self.db.commit()
        self.db.refresh(employee)

        return employee

    def delete(self, employee_id: int):
            employee = (
                self.db.query(Employee)
                .filter(Employee.id == employee_id)
                .first()
            )

            if not employee:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Employee not found"
                )

            self.db.delete(employee)
            self.db.commit()