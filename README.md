# Document-Management-and-Application

# 📄 Document Management and Application System

A robust backend system built with **FastAPI** to manage users, documents, permissions, and secure file uploads/downloads, with JWT-based authentication and CORS middleware.

---

## 🚀 Features

- ✅ User Authentication with JWT
- ✅ Role-based Access Control
- ✅ Document Upload and Download APIs
- ✅ Secure Token Refresh on Each Request
- ✅ CORS Middleware Support
- ✅ Scalable Middleware Architecture
- ✅ PostgreSQL support via SQLAlchemy
- ✅ Modular Code Structure (Controllers, Middleware, Utilities)

---

## 🧱 Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Language  | Python 3.11+       |
| Framework | FastAPI            |
| Database  | PostgreSQL 	 |
| ORM       | SQLAlchemy         |
| Auth      | JWT (PyJWT)        |
| Deployment| Uvicorn  		 |

---

## 📁 Project Structure

```
📦 document-management/
├── app/
│   ├── main.py               # FastAPI app entry point
│   ├── routes/               # All routers
│   ├── models/               # SQLAlchemy models
│   ├── schemas/              # Pydantic schemas
│   ├── controllers/          # Business logic
│   ├── middlewares/          # Token Validation and CORS middleware
│   ├── utility/              # Token utilities, encryption 
│   └── config.py             # Environment config contains database , token secret key,upload file path
├── requirements.txt
└── README.md
```

---

## 🔐 Authentication

- **JWT-based Auth** with:
  - Access token creation
  - Automatic token refresh via middleware
  - Token expiration handling
  - Secured routes (e.g. `/documents/upload`, `/documents/download`)

---

## 🔄 Token Refresh Logic

Each valid request:
- Validates JWT from `Authorization: Bearer <token>`
- If valid, allows the request and generates a **new token** in `X-New-Token` response header
- If invalid or missing → returns `401 Unauthorized`

---

## 🌐 CORS Support

CORS Middleware ensures:
- Proper handling of `OPTIONS` preflight requests
- Supports `Authorization`, `Content-Type`, `X-New-Token` headers
- Configured globally for all routes

---

## 📦 Installation & Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/document-management.git
cd document-management
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
uvicorn app.main:app --reload
```

---

## 🛠️ API Endpoints (Sample)

| Method | Endpoint               | Description              |
|--------|------------------------|--------------------------|
| POST   | `/login`               | User login               |
| POST   | `/documents/` Upload a document        |
| GET    | `/documents/documents/download/{doc_id}`  | Download a document      |
| GET    | `/users/users/{userStatus}`               | Get all users            |

---

## 🔐 Security Notes

- All routes (except `/login`) are protected by JWT
- Token is short-lived and refreshed after each request
- CORS headers are added to **every** response

---
