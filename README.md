# Superheroes API

## Project Overview

The Superheroes API is a RESTful Flask application for managing superheroes, their powers, and the relationships between them. It demonstrates backend development concepts such as CRUD operations, relational database modeling, validations, and REST API best practices using Flask and SQLAlchemy.

The API allows users to create heroes, define powers, assign powers to heroes with different strength levels, and retrieve relational data in JSON format.

---

## Motivation

This project was built to strengthen backend development skills using Python and Flask. It focuses on designing RESTful APIs, working with relational databases, and structuring scalable Flask applications.

---

## Features

- Retrieve all heroes
- Retrieve a single hero with associated powers
- Retrieve all powers
- Create new heroes
- Update power descriptions with validation
- Assign powers to heroes with strength levels
- Manage hero–power relationships

---

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DevBrianKE/phase-4-superheroes-api.git
cd phase-4-superheroes-api
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Database Migrations

```bash
flask db init
flask db migrate
flask db upgrade
```

---

### 5. Seed the Database

```bash
python seed.py
```

---

### 6. Run the Application

```bash
flask run
```

The API will be available at:

```
http://127.0.0.1:5000
```

If port 5000 is busy:

```bash
flask run --port 5001
```

---

## API Endpoints

### Heroes

#### Get All Heroes

```http
GET /heroes
```

#### Get Hero by ID

```http
GET /heroes/<id>
```

#### Create a Hero

```http
POST /heroes
```

Request Body:

```json
{
  "name": "Peter Parker",
  "super_name": "Spider-Man"
}
```

---

### Powers

#### Get All Powers

```http
GET /powers
```

#### Get Power by ID

```http
GET /powers/<id>
```

#### Update Power Description

```http
PATCH /powers/<id>
```

Request Body:

```json
{
  "description": "Grants superhuman strength to the hero."
}
```

Validation Rule:
- Description must be at least 20 characters long

---

### Hero Powers

#### Assign a Power to a Hero

```http
POST /hero_powers
```

Request Body:

```json
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 3
}
```

Valid Strength Values:
- Strong
- Average
- Weak

---

## Testing the API

```bash
curl http://127.0.0.1:5000/heroes
curl http://127.0.0.1:5000/powers
```

---

## Project Structure

```text
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
├── migrations/
├── seed.py
├── app.py
├── requirements.txt
└── README.md
```

---

## Author

Brian  
GitHub: https://github.com/DevBrianKE

---

## License

MIT License
