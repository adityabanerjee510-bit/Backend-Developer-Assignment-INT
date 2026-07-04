from pydantic import BaseModel, Field, EmailStr
from datetime import datetime, timezone

class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SignupInDB(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    role: str = "user"  # Default role is "user"

class AdminSignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "admin"  # Default role is "admin"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class EmergencyLoginRequest(BaseModel):
    username: str
    password: str