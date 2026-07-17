# Student Management System (SMS)

A backend **Student Management System API** built using **FastAPI**, **Pydantic**, and **SQL database integration**. This project provides RESTful API endpoints to manage student records efficiently.

The project was built as part of my journey to learn backend development with FastAPI, focusing on API development, CRUD operations, routing, data validation, database integration, and API testing.

## Features

* Create new student records
* Retrieve all students
* Retrieve a student by ID
* Update existing student information
* Delete student records
* Filter students using query parameters
* Data validation using Pydantic models
* Organized API routes using `APIRouter`
* Database integration for persistent data storage
* Error handling using `HTTPException`
* Interactive API documentation with Swagger UI

## Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **SQL**
* **Uvicorn**
* **Swagger UI**
* **Git & GitHub**

## API Endpoints

| Method   | Endpoint                 | Description                |
| -------- | ------------------------ | -------------------------- |
| `POST`   | `/students/`             | Create a new student       |
| `GET`    | `/students/`             | Get all students           |
| `GET`    | `/students/{student_id}` | Get a student by ID        |
| `PUT`    | `/students/{student_id}` | Update student information |
| `DELETE` | `/students/{student_id}` | Delete a student           |
| `GET`    | `/students/?course=AIML` | Filter students by course  |

## Student Data Model

A student record contains information such as:

```json
{
  "name": "Harry",
  "age": 20,
  "course": "AIML"
}
```

## Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd SMS
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

Install your database dependencies as required by the project.

### 5. Start the FastAPI server

```bash
uvicorn main:app --reload
```

The API will run locally at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI automatically provides interactive API documentation.

**Swagger UI:**

`http://127.0.0.1:8000/docs`

**ReDoc:**

`http://127.0.0.1:8000/redoc`

You can use Swagger UI to test the API endpoints directly from your browser.

## Project Structure

```text
SMS/
│
├── main.py
├── routers/
│   └── students.py
├── models/
├── database/
├── requirements.txt
└── README.md
```

The exact project structure may evolve as more features are added.

## Future Improvements

* Add user authentication and authorization
* Implement student login functionality
* Add course and attendance management
* Add pagination and advanced filtering
* Improve database relationships
* Add automated API tests
* Deploy the backend to a cloud platform
* Build a frontend interface

## Learning Outcomes

Through this project, I practiced:

* Building REST APIs with FastAPI
* Implementing CRUD operations
* Working with path and query parameters
* Using Pydantic for request validation
* Organizing endpoints with `APIRouter`
* Handling API errors with HTTP status codes
* Connecting a FastAPI application to a database
* Testing endpoints using Swagger UI
* Structuring a backend project for future scalability

## Author

**Harry Bhangal**

Computer Science student specializing in Artificial Intelligence and Data Science.

---

This project is part of my backend development learning journey and will continue to evolve as I learn and implement more FastAPI concepts.

