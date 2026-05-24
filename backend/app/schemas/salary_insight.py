from pydantic import BaseModel

class CountrySalaryInsightsResponse(BaseModel):
    country: str
    minimum_salary: float
    maximum_salary: float
    average_salary: float

class JobTitleSalaryResponse(BaseModel):
    country: str
    job_title: str
    average_salary: float