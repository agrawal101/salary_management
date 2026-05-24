from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.employee_repository import EmployeeRepository
from backend.app.schemas.salary_insight import (
    CountrySalaryInsightsResponse,
    JobTitleSalaryResponse,
)
from backend.app.services.salary_service import SalaryService


router = APIRouter(
    prefix="/salary-insights",
    tags=["salary-insights"]
)


def get_salary_service(
    db: Session = Depends(get_db)
) -> SalaryService:
    return SalaryService(
        EmployeeRepository(db)
    )


@router.get(
    "/country/{country}",
    response_model=CountrySalaryInsightsResponse
)
def get_salary_insights_by_country(
    country: str,
    service: SalaryService = Depends(
        get_salary_service
    ),
):
    return service.get_salary_insights_by_country(
        country
    )


@router.get(
    "/job-title",
    response_model=JobTitleSalaryResponse
)
def get_average_salary_by_job_title(
    country: str = Query(...),
    job_title: str = Query(...),
    service: SalaryService = Depends(
        get_salary_service
    ),
):
    return service.get_average_salary_by_job_title(
        country,
        job_title
    )