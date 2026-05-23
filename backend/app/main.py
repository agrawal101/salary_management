from fastapi import FastAPI

from backend.app.api.employee_routes import router
from backend.app.database.session import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Salary Management")
app.include_router(router)
