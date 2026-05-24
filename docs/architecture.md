# Architecture & Tradeoffs

## Architecture

The project follows a layered backend structure:

```text
API Layer
    ↓
Service Layer
    ↓
Repository Layer
    ↓
Database
```

### API Layer
Responsible for request handling and response serialization.

### Service Layer
Contains business logic and orchestration.

### Repository Layer
Handles database interactions using SQLAlchemy.

## Key Decisions

### SQLite
Chosen for simplicity and quick local setup suitable for an assessment.

### Layered Architecture
Used to improve separation of concerns and maintainability.

### Material UI
Chosen to build a clean and usable UI quickly.

### Test Isolation
Implemented separate test database setup to ensure deterministic tests.

### Bulk Insert in Seed Script
Used for performance while inserting 10,000 employees.

## Tradeoffs

- SQLite chosen over PostgreSQL for simplicity
- Basic UI prioritized over advanced styling
- Pagination implemented with fixed size for simplicity
- Minimal feature scope maintained to align with assignment requirements
