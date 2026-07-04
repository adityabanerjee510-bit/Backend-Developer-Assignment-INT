from fastapi import APIRouter, Depends, HTTPException
from fitness_studio.models.login_signup_model import (SignupRequest, SignupInDB,AdminSignupRequest)
from fitness_studio.database.database import users_collection 
from fitness_studio.security.auth import hash_password
from fitness_studio.security.utils import get_current_admin

router = APIRouter(prefix="/signup", tags=["Signup"])

@router.post("/")
def signup(signup_request: SignupRequest):
    
    existing_user = users_collection.find_one({"$or": {"email": signup_request.email}})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    
    hashed_password = hash_password(signup_request.password)

    
    new_user = SignupInDB(
        username=signup_request.username,
        email=signup_request.email,
        password=hashed_password,
        created_at=signup_request.created_at,
        role="user"
    )

    users_collection.insert_one(new_user.model_dump())

    return {"message": "User created successfully"}

@router.post("/admin")
def admin_signup(admin: AdminSignupRequest,current_admin=Depends(get_current_admin)):

    existing = users_collection.find_one({
        "$or":[
            {"username": admin.username},
            {"email": admin.email}
        ],
        "role": "admin"
    })

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Admin already exists"
        )

    hashed = hash_password(admin.password)

    users_collection.insert_one({
        "username": admin.username,
        "email": admin.email,
        "password": hashed,
        "role": "admin",
        "created_at": admin.created_at
    })

    return {
        "message":"Admin Registered"
    }