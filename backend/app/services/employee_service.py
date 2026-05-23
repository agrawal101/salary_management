from backend.app.models.employee import Employee
from backend.app.repositories.employee_repository import EmployeeRepository
from backend.app.schemas.employee import EmployeeCreate


class EmployeeService:
    def __init__(self, repository: EmployeeRepository) -> None:
        self.repository = repository

    def create_employee(self, employee_data: EmployeeCreate) -> Employee:
        return self.repository.create(employee_data)
    
    def get_employee(self, employee_id: int) -> Employee:
        return self.repository.get_by_id(employee_id)
