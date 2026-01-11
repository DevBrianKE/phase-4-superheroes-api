# 🦸 Superheroes API

A simple RESTful **Flask API** for managing **superheroes, their powers, and hero–power relationships**.

This project demonstrates CRUD operations, relational database modeling, and REST API best practices using Flask and SQLAlchemy.

---

## 🚀 Features

- List all heroes and powers
- View a single hero with their associated powers
- Create new heroes
- Assign powers to heroes
- Update power descriptions
- Manage nested hero–power relationships

---

## 🛠 Tech Stack

- **Python 3**
- **Flask**
- **Flask-SQLAlchemy**
- **Flask-Migrate**
- **SQLite**

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DevBrianKE/phase-4-superheroes-api.git
cd phase-4-superheroes-api
```

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

> **Windows**
```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Database Migrations

```bash
flask db init      # Run only once
flask db migrate
flask db upgrade
```

---

### 5️⃣ Seed the Database

```bash
python seed.py
```

---

### 6️⃣ Run the Server

```bash
flask run
```

📍 API will be available at:  
**http://127.0.0.1:5000**

If port **5000** is busy:

```bash
flask run --port 5001
```

---

## 📌 API Endpoints

### 🦸 Heroes

#### Get All Heroes
```http
GET /heroes
```

#### Get Hero by ID (with powers)
```http
GET /heroes/<id>
```

#### Create a Hero
```http
POST /heroes
```

**Request Body**
```json
{
  "name": "Peter Parker",
  "super_name": "Spider-Man"
}
```

---

### ⚡ Powers

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

**Request Body**  
> Description must be **at least 20 characters**

```json
{
  "description": "Grants superhuman strength to the hero."
}
```

**Valid Strength Values**
- `Strong`
- `Average`
- `Weak`

---

### 🔗 Hero-Powers

#### Assign a Power to a Hero
```http
POST /hero_powers
```

**Request Body**
```json
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 3
}
```

---

## 🧪 Testing the API

```bash
curl http://127.0.0.1:5000/heroes
curl http://127.0.0.1:5000/powers
curl -X POST http://127.0.0.1:5000/heroes \
     -H "Content-Type: application/json" \
     -d '{"name":"Peter Parker","super_name":"Spider-Man"}'
curl http://127.0.0.1:5000/heroes/1
```

---

## 📁 Project Structure

```text
.
├── app/
│   ├── models.py
│   ├── routes.py
│   └── __init__.py
├── migrations/
├── seed.py
├── app.py
├── requirements.txt
└── README.md
```

---
