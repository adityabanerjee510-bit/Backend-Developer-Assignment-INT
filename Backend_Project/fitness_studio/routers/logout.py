from fastapi import APIRouter, HTTPException
from fitness_studio.models.refresh_token import RefreshRequest
from fitness_studio.security.auth import (verify_token, hash_refresh_token)
from fitness_studio.database.database import (refresh_tokens_collection)

router = APIRouter(prefix="/logout",tags=["Logout"])

@router.post("/logout")
def logout(request: RefreshRequest):

    result = refresh_tokens_collection.update_one(
        {
            "refresh_token_hash": hash_refresh_token(request.refresh_token),
            "revoked": False
        },
        {
            "$set": {
            "revoked": True
            }
        }
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Refresh token not found or already revoked."
        )

    return {
        "message": "Logged out successfully"
    }