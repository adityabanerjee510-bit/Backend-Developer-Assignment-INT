from pydantic import BaseModel, Field, EmailStr, model_validator, computed_field
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


class ChangePasswordRequest_Emergency(BaseModel):
    new_password: str = Field(min_length=8)

class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str = Field(min_length=8)