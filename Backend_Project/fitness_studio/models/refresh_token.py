from pydantic import BaseModel
from datetime import datetime

class RefreshRequest(BaseModel):
    refresh_token: str

class RefreshTokenDB(BaseModel):
    username: str
    refresh_token_hash: str
    revoked: bool
    created_at: datetime
    expires_at: datetime