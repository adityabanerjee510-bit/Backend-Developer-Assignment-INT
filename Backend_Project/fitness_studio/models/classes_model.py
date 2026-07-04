from pydantic import BaseModel, Field
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


class FitnessClassCreate(BaseModel):
    name: str
    date_time: datetime 
    instructor: str
    total_slots: int

class FitnessClassInDB(BaseModel):
    class_id: int
    name: str
    date_time: datetime
    instructor: str
    total_slots: int
    available_slots: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class FitnessClassResponse(BaseModel):
    class_id: int
    name: str
    date_time: datetime
    instructor: str
    total_slots: int
    available_slots: int

class CreateClassResponse(BaseModel):
    message: str
    content: FitnessClassResponse