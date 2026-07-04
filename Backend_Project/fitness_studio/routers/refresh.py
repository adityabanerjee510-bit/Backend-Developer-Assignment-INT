from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException, status
from fitness_studio.database.database import refresh_tokens_collection
from fitness_studio.models.refresh_token import RefreshRequest
from fitness_studio.security.auth import (verify_token,create_access_token,create_refresh_token,hash_refresh_token)
from fitness_studio.models.refresh_token import RefreshTokenDB

router = APIRouter(prefix="/refresh",tags=["Refresh"],)

@router.post("/")
def refresh(request: RefreshRequest):
    hashed = hash_refresh_token(request.refresh_token)

    token = refresh_tokens_collection.find_one(
        {
            "refresh_token_hash": hashed,
            "revoked": False,
        }
    )

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token revoked or not found",
        )

    payload = verify_token(request.refresh_token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token required",
        )
    new_access = create_access_token(
        {
            "sub": payload["sub"],
            "role": payload["role"],
        }
    )
    new_refresh = create_refresh_token(
        {
            "sub": payload["sub"],
            "role": payload["role"],
            "type": "refresh",
        }
    )
    new_hash = hash_refresh_token(new_refresh)

    refresh_tokens_collection.update_one(
        {
            "refresh_token_hash": hashed,
        },
        {
            "$set": {
                "revoked": True,
                "last_used_at": datetime.now(timezone.utc),
            }
        },
    )

    token = RefreshTokenDB(
        username=payload["sub"],
        refresh_token_hash=new_hash,
        revoked=False,
        created_at=datetime.now(timezone.utc),
        expires_at=datetime.now(timezone.utc) + timedelta(days=30)
    )

    refresh_tokens_collection.insert_one(
        token.model_dump()
    )
    return {
        "access_token": new_access,
        "refresh_token": new_refresh,
        "token_type": "bearer",
    }