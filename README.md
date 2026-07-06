# FastAPI User Management API

A RESTful backend API for creating and managing user records, built with **FastAPI** and **SQLAlchemy ORM**, backed by a **MySQL** database, with request validation handled by **Pydantic**.

## Features

- User creation endpoint (`POST /users/`)
- Request validation using Pydantic schemas
- SQLAlchemy ORM models mapped to MySQL tables
- Auto-generated interactive API documentation via Swagger UI (`/docs`)

## Tech Stack

| Layer          | Technology       |
|----------------|------------------|
| Framework      | FastAPI          |
| ORM            | SQLAlchemy       |
| Database       | MySQL (PyMySQL)  |
| Validation     | Pydantic         |
| Server         | Uvicorn          |

## Project Structure

```
.
├── main.py     # FastAPI app instance and route definitions
├── model.py    # SQLAlchemy ORM models (database tables)
├── schema.py   # Pydantic schemas (request/response validation)
└── db.py       # Database engine and session configuration
```

## Prerequisites

- Python 3.9+
- MySQL server running locally
- A MySQL database named `pranay` (or update `DATABASE_URL` in `db.py`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-user-api.git
   cd fastapi-user-api
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql
   ```

## Running the App

Start the development server:

```bash
uvicorn main:app --reload
```

Then open your browser to:

- API root: `http://127.0.0.1:8000`
- Interactive docs (Swagger UI): `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint    | Description       |
|--------|-------------|--------------------|
| POST   | `/users/`   | Create a new user  |

### Example Request

```json
POST /users/
{
  "id": 1,
  "email": "user@example.com",
  "name": "Pranay",
  "password": "yourpassword"
}
```

## Notes & Future Improvements

- Passwords are currently stored as plain text — hashing (e.g. via `passlib`) should be added before any real-world use.
- `id` is currently accepted from the client — ideally the database should auto-generate this.
- Database credentials are hardcoded in `db.py` — consider moving these to environment variables using `python-dotenv`.
- Only a create endpoint exists so far — GET, PUT, and DELETE routes would make this a complete CRUD API.

## License

This project is open source and available for personal/educational use.
