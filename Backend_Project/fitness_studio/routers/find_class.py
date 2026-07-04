from fastapi import APIRouter, Depends, HTTPException
from fitness_studio.models.classes_model import FitnessClassResponse
from fitness_studio.database.database import classes_collection , bookings_collection, users_collection
from fitness_studio.security.utils import get_current_admin, get_current_user

router = APIRouter(prefix="/find", tags=["Find Classes"])

@router.get("/", response_model=list[FitnessClassResponse])
def get_all_classes(current_user = Depends(get_current_user)):
    user = users_collection.find_one({
        "username": current_user["sub"]
    })

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    bookings = list(
        bookings_collection.find(
            {"user_id": str(user["_id"])},
            {"_id": 0}
        )
    )

    return bookings
@router.get("/{class_id}", response_model=FitnessClassResponse)
def get_class_by_id(class_id: int, current_user=Depends(get_current_user)):
    fitness_class = classes_collection.find_one(
        {"class_id": class_id},
        {"_id": 0}
    )

    if not fitness_class:
        raise HTTPException(
            status_code=404,
            detail="Class not found."
        )

    return fitness_class