import random
from pathlib import Path

from sqlalchemy.orm import Session
from backend.app.database.session import Base, SessionLocal, engine
from backend.app.models.employee import Employee
Base.metadata.create_all(bind=engine)

TOTAL_EMPLOYEES = 10000

JOB_TITLES = [
    "Software Engineer",
    "Senior Software Engineer",
    "QA Engineer",
    "Product Manager",
    "HR Executive",
    "Data Analyst",
    "Engineering Manager",
    "DevOps Engineer",
    "Business Analyst",
    "Designer"
]

COUNTRIES = [
    "India",
    "USA",
    "Germany",
    "Canada",
    "UK",
    "Australia",
    "Singapore"
]

MIN_SALARY = 30000
MAX_SALARY = 300000


def load_names(file_path: Path) -> list[str]:
    with open(file_path, "r") as file:
        return [
            line.strip()
            for line in file.readlines()
            if line.strip()
        ]


def generate_full_name(
    first_names: list[str],
    last_names: list[str]
) -> str:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"


def create_employee(
    first_names: list[str],
    last_names: list[str]
) -> Employee:
    return Employee(
        full_name=generate_full_name(
            first_names,
            last_names
        ),
        job_title=random.choice(
            JOB_TITLES
        ),
        country=random.choice(
            COUNTRIES
        ),
        salary=random.randint(
            MIN_SALARY,
            MAX_SALARY
        )
    )


def seed_employees():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    base_path = Path(__file__).parent

    first_names = load_names(
        base_path / "first_name.txt"
    )

    last_names = load_names(
        base_path / "last_name.txt"
    )

    db: Session = SessionLocal()

    try:
        employees = []

        for _ in range(TOTAL_EMPLOYEES):
            employees.append(
                create_employee(
                    first_names,
                    last_names
                )
            )

        db.bulk_save_objects(
            employees
        )

        db.commit()

        print(
            f"Successfully seeded "
            f"{TOTAL_EMPLOYEES} employees"
        )

    finally:
        db.close()


if __name__ == "__main__":
    seed_employees()