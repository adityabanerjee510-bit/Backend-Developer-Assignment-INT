from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["fitness_booking"]

users_collection = db["users/admins"]
classes_collection = db["fitness_classes"]
bookings_collection = db["bookings"]
refresh_tokens_collection = db["refresh_tokens"]
