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

    def get_all_employees(self, page: int, size: int):
        return self.repository.get_all(page, size)

    def update_employee(self, employee_id: int, employee_data: EmployeeCreate):
        return self.repository.update(employee_id, employee_data)

    def delete_employee(self, employee_id: int):
        self.repository.delete(employee_id)
