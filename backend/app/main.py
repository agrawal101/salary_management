from fastapi import FastAPI

from backend.app.api import employee_router
from backend.app.database.session import Base, engine
from backend.app import models


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Salary Management")
app.include_router(employee_router)
