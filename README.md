# Employee Salary Management System

A minimal full-stack employee salary management system built as part of the Incubyte Software Craftsperson assessment.

## Features

### Employee Management
- Create employee
- View employee(s)
- Update employee
- Delete employee

### Salary Insights
- Minimum salary by country
- Maximum salary by country
- Average salary by country
- Average salary for a job title within a country

### Additional Features
- Pagination support
- Seed script for 10,000 employees
- Automated test coverage
- Minimal frontend UI

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pytest

### Frontend
- React (Vite)
- Material UI
- Axios

---

## Project Structure

```text
salary_management/
├── backend/
├── frontend/
├── docs/
└── README.md
```

## Setup Instructions

### Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

Backend runs on:

`http://localhost:8000`

Swagger Docs:

`http://localhost:8000/docs`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

`http://localhost:5173`

## Running Tests

```bash
pytest -v
```

## Seed 10,000 Employees

```bash
python -m backend.seed_data.seed_employees
```

## Design Considerations

- TDD-inspired incremental development with small commits
- Test isolation using separate test database
- Repository + Service layer separation for maintainability
- Bulk insertion used in seed script for performance
- Minimal yet usable UI as per assignment expectations

## AI Usage

AI-assisted development details and prompts used are documented in:

`docs/ai-usage.md`
