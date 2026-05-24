from backend.app.repositories.employee_repository import (
    EmployeeRepository
)


class SalaryService:
    def __init__(
        self,
        repository: EmployeeRepository
    ):
        self.repository = repository

    def get_salary_insights_by_country(
        self,
        country: str
    ):
        return self.repository.get_salary_insights_by_country(
            country
        )

    def get_average_salary_by_job_title(
        self,
        country: str,
        job_title: str
    ):
        return self.repository.get_average_salary_by_job_title(
            country,
            job_title
        )