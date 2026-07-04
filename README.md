# 🏋️ FitStream - Fitness Studio Booking API

A production-ready **RESTful Fitness Studio Booking API** built with **FastAPI**, **MongoDB**, and **JWT Authentication**.

The application allows users to register, authenticate securely, browse fitness classes, book available slots, manage bookings, and enables administrators to create and manage fitness classes. The project follows a modular architecture and implements production-level authentication with Access Tokens, Refresh Tokens, password hashing, role-based authorization, and token revocation.

---

# 🚀 Features

## 🔐 Authentication & Security

- User Registration
- User Login
- JWT Access Token Authentication
- Refresh Token Authentication
- Secure Logout (Token Revocation)
- Password Hashing using bcrypt
- Change Password
- Protected Routes
- Role-Based Authorization
- Emergency Admin Login
- Refresh Token Storage
- Refresh Token Hashing
- Refresh Token Revocation

---

## 👤 User Features

- Register Account
- Login
- Change Password
- View Available Fitness Classes
- Book Fitness Classes
- Prevent Duplicate Bookings
- View Personal Bookings
- Automatic Slot Reduction
- JWT Authentication

---

## 👨‍💼 Admin Features

- Create Fitness Classes
- View All Classes
- View All Bookings
- Emergency Login
- Protected Admin Routes

---

## 📅 Booking System

- Real-time Slot Availability
- Prevent Duplicate Booking
- Automatic Remaining Slot Update
- Class Capacity Validation
- Booking History

---

## 🛡 Production Security

- Password Hashing (bcrypt)
- JWT Authentication
- Access Token
- Refresh Token
- Refresh Token Rotation Ready
- Refresh Token Revocation
- Secure Password Verification
- Environment Variables
- Protected API Endpoints

---

# 🏗 Project Structure

```text
Backend_Project/
│
├── fitness_studio/
│
├── database/
│   └── database.py
│
├── models/
│   ├── booking_model.py
│   ├── change_password.py
│   ├── classes_model.py
│   ├── login_signup_model.py
│   └── refresh_token.py
│
├── routers/
│   ├── signup.py
│   ├── login.py
│   ├── refresh.py
│   ├── logout.py
│   ├── change_password.py
│   ├── create_class.py
│   ├── find_class.py
│   ├── create_booking.py
│   └── find_booking.py
│
├── security/
│   ├── auth.py
│   └── utils.py
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

# 🛠 Tech Stack

| Technology | Used |
|------------|------|
| Python | ✅ |
| FastAPI | ✅ |
| MongoDB | ✅ |
| PyMongo | ✅ |
| JWT | ✅ |
| Passlib (bcrypt) | ✅ |
| Python-Jose | ✅ |
| Pydantic | ✅ |
| Uvicorn | ✅ |
| dotenv | ✅ |

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/FitStream.git

cd FitStream
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MONGO_URI=

SECRET_KEY=

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=15

REFRESH_TOKEN_EXPIRE_DAYS=30

ADMIN_USERNAME=

ADMIN_PASSWORD=
```

---

# ▶ Running the Project

```bash
uvicorn main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger Docs

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📖 API Endpoints

---

## Authentication

### User Signup

```
POST /signup
```

### User Login

```
POST /login
```

Returns

- Access Token
- Refresh Token

---

### Refresh Access Token

```
POST /refresh
```

Uses Refresh Token to generate a new Access Token.

---

### Logout

```
POST /logout
```

Revokes Refresh Token.

---

### Change Password

```
POST /change-password
```

---

## Classes

### Create Class (Admin)

```
POST /classes
```

---

### View All Classes

```
GET /classes
```

Accessible by authenticated users.

---

## Booking

### Book Class

```
POST /bookings
```

Features

- Prevent Duplicate Booking
- Reduce Available Slots
- Validate Capacity

---

### View My Bookings

```
GET /bookings
```

Returns bookings of currently logged-in user.

---

### View All Bookings (Admin)

```
GET /bookings/all
```

---

# 🔐 Authentication Flow

```text
Signup
    │
    ▼
Password Hashing
    │
    ▼
MongoDB
    │
    ▼
Login
    │
    ▼
Verify Password
    │
    ▼
Generate

Access Token
Refresh Token

    │
    ▼
Protected APIs
    │
    ▼
Access Token Expired
    │
    ▼
POST /refresh
    │
    ▼
New Access Token
```

---

# 📦 MongoDB Collections

The application uses the following collections:

```
users

classes

bookings

refresh_tokens
```

---

# 📌 Business Rules

### User

- Cannot book the same class twice.
- Cannot book a full class.
- Can view only their own bookings.
- Must be authenticated.

---

### Admin

- Can create classes.
- Can view all bookings.
- Uses role-based authorization.
- Supports Emergency Login.

---

# 🔒 Security Features

- bcrypt Password Hashing
- JWT Authentication
- Refresh Tokens
- Token Revocation
- Refresh Token Hashing
- Protected Routes
- Environment Variables
- Role-Based Authorization
- Password Verification

---

# 📸 Screenshots

## Swagger Documentation

> *(Add Screenshot Here)*

---

## MongoDB Collections

> *(Add Screenshot Here)*

---

## Successful Booking

> *(Add Screenshot Here)*

---

## Login Response

> *(Add Screenshot Here)*

---

# 📚 Future Improvements

- Email Verification
- Forgot Password via Email
- Docker Support
- Unit Testing
- CI/CD Pipeline
- Rate Limiting
- Redis Token Cache
- Refresh Token Rotation
- Logging Middleware
- API Versioning
- Background Tasks
- Pagination
- Search & Filtering
- Appointment Cancellation
- Notifications
- Deployment on AWS/Azure

---

# 👨‍💻 Author

### Aditya Banerjee

**Python Developer | FastAPI Backend Engineer | Agentic AI Developer**

**Skills**

- Python
- FastAPI
- MongoDB
- JWT Authentication
- REST APIs
- AI Agents
- LangChain
- Pandas
- Matplotlib
- Async Programming

---

# ⭐ If you found this project useful...

Give the repository a ⭐ on GitHub.

It motivates future improvements and helps others discover the project.

---

## License

This project is created for learning, portfolio demonstration, and backend development practice.
