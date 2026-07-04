from fastapi import APIRouter, Depends, HTTPException
from fitness_studio.models.change_passward import ChangePasswordRequest, ChangePasswordRequest_Emergency
from fitness_studio.security.auth import verify_password 
from fitness_studio.security.auth import hash_password
from fitness_studio.security.utils import get_current_admin, get_emergency_admin
from fitness_studio.database.database import users_collection

router = APIRouter(prefix="/change_password", tags=["Change Password"])

@router.post("/admin/emergency")
def change_password_emergency(
    change_request: ChangePasswordRequest_Emergency,
    current_admin=Depends(get_emergency_admin)
):

    hashed_password = hash_password(change_request.new_password)

    users_collection.update_one(
        {
            "username": current_admin["sub"],
            "role": "admin"
        },
        {
            "$set": {
                "password": hashed_password
            }
        }
    )

    return {
        "message": "Password changed successfully. Please log in again."
    }
@router.post("/admin")
def change_password(change_request: ChangePasswordRequest, current_admin=Depends(get_current_admin)):
    # Fetch the admin's current password from the database
    admin = users_collection.find_one({
        "username": current_admin["sub"],
        "role": "admin"
    })

    # Verify the old password
    if not verify_password(change_request.old_password, admin["password"]):
        raise HTTPException(status_code=400, detail="Old password is incorrect")

    # Hash the new password
    hashed_password = hash_password(change_request.new_password)

    # Update the admin's password in the database
    users_collection.update_one(
        {"username": current_admin["sub"]},
        {"$set": {"password": hashed_password}}
    )

    return {"message": "Password changed successfully."}