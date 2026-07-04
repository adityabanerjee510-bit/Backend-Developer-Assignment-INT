from pymongo import MongoClient
from passlib.context import CryptContext
from datetime import datetime, timezone
import os
import dotenv

dotenv.load_dotenv()

# MongoDB Connection
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["fitness_booking"]     # Change to your database name
users_collection = db["users/admins"]     # Change to your collection name

# Password Hasher
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# Hash the password
hashed_password = pwd_context.hash("sripali")   

# Insert the admin
users_collection.insert_one({
    "username": "Aditya Banerjee",              
    "email": "aditya@example.com",      
    "password": hashed_password,
    "role": "admin",
    "created_at": datetime.now(timezone.utc)
})

print("Admin created successfully!")