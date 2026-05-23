import sys; print(sys.path)
from fastapi import APIRouter, Depends, status,Query
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.employee_repository import EmployeeRepository
from backend.app.schemas.employee import EmployeeCreate, EmployeeRead
from backend.app.services.employee_service import EmployeeService

router = APIRouter(prefix="/employees", tags=["employees"])


def get_employee_service(db: Session = Depends(get_db)) -> EmployeeService:
    return EmployeeService(EmployeeRepository(db))


@router.post("", response_model=EmployeeRead, status_code=status.HTTP_201_CREATED)
def create_employee(
    employee: EmployeeCreate,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeRead:
    return service.create_employee(employee)

@router.get("/{employee_id}", response_model=EmployeeRead)
def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeRead:
    return service.get_employee(employee_id)

@router.get("", response_model=list[EmployeeRead])
def get_all_employees(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    service: EmployeeService = Depends(get_employee_service),
):
    return service.get_all_employees(page, size)