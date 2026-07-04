from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timezone


class BookingCreate(BaseModel):
    class_name: str
    instructor: str

class BookingInDB(BaseModel):
    booking_id: int
    user_id: str
    class_id: int
    username: str
    name: str
    instructor: str
    booking_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))