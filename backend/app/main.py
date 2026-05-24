from fastapi import FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware
)

from backend.app.api.employee_routes import (
    router
)
from backend.app.database.session import (
    Base,
    engine,
)
from backend.app.api.salary_routes import (
    router as salary_router
)


Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Salary Management"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
app.include_router(
    salary_router
)