from pydantic import BaseModel, ConfigDict


class EmployeeCreate(BaseModel):
    full_name: str
    job_title: str
    country: str
    salary: int


class EmployeeRead(EmployeeCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
