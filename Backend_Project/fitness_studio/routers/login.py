from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, status , Depends
from fitness_studio.models.login_signup_model import  EmergencyLoginRequest 
from fitness_studio.database.database import users_collection , refresh_tokens_collection
from fitness_studio.security.auth import create_refresh_token, hash_refresh_token, verify_password, create_access_token,create_refresh_token
from fastapi.security import OAuth2PasswordRequestForm


import os

load_dotenv()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    # First search as user
    user = users_collection.find_one({
        "username": form_data.username,
        "role": "user"
    })

    # If not found, search as admin
    if not user:
        user = users_collection.find_one({
            "username": form_data.username,
            "role": "admin"
        })

    # Still not found
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # Verify password
    if not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # Create token
    access_token = create_access_token(
        {
            "sub": user["username"],
            "role": user["role"]
        }
    )
    refresh_token = create_refresh_token(
        {
            "sub": user["username"],
            "role": user["role"]
        }
    )
    hashed_refresh = hash_refresh_token(refresh_token)

    refresh_tokens_collection.insert_one(
        {
            "user_id": user["_id"],
            "refresh_token_hash": hashed_refresh,
            "created_at": datetime.now(timezone.utc),
            "expires_at":datetime.now(timezone.utc)+ timedelta(days=7),
            "revoked": False
        }
    )
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# @router.post("/admin")
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     # Check if the user exists in the database
#     admin = users_collection.find_one({
#         "username": form_data.username,
#         "role": "admin"  # Determine role based on username
#     })
#     if not admin:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

#     # Verify the password
#     if not verify_password(form_data.password, admin["password"]):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

#     # Create an access token
#     access_token = create_access_token(
#         data={
#             "sub": admin["username"],
#             "role": admin["role"]
#         }
#     )

#     return {"access_token": access_token, "token_type": "bearer"}

@router.post("/admin/forgot_emergency")
def forgot_admin_emergency(login_request: EmergencyLoginRequest):

    admin = users_collection.find_one({
        "username": login_request.username,
        "role": "admin"
    })

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Admin not found"
        )

    if login_request.password != ADMIN_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid emergency password"
        )

    token = create_access_token(
        {
            "sub": admin["username"],
            "role": admin["role"],
            "emergency": True
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }