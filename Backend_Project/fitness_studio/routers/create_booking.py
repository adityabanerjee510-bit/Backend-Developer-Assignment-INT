from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from fitness_studio.database.database import (bookings_collection,classes_collection,users_collection)
from fitness_studio.models.booking_model import (BookingCreate,BookingInDB)
from fitness_studio.security.utils import get_current_user

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

@router.post("/")
def create_booking(
    booking: BookingCreate,
    current_user=Depends(get_current_user)
):
    

    user = users_collection.find_one({
        "username": current_user["sub"]
    })

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    fitness_class = classes_collection.find_one({
        "name": booking.class_name,
        "instructor": booking.instructor
    })

    if not fitness_class:
        raise HTTPException(
            status_code=404,
            detail="Class not found."
        )

    if fitness_class["available_slots"] <= 0:
        raise HTTPException(
            status_code=400,
            detail="Class is full."
        )


    existing_booking = bookings_collection.find_one({
        "user_id": user["_id"],
        "class_id": fitness_class["class_id"]
    })

    if existing_booking:
        raise HTTPException(
            status_code=400,
            detail="You have already booked this class."
        )

    last_booking = bookings_collection.find_one(
        sort=[("booking_id", -1)]
    )

    if last_booking:
        next_booking_id = last_booking["booking_id"] + 1
    else:
        next_booking_id = 1

    booking_data = BookingInDB(
        username=user["username"],
        booking_id=next_booking_id,
        user_id=str(user["_id"]),
        class_id=fitness_class["class_id"],
        booking_date=datetime.now(timezone.utc),
        name = booking.class_name,
        instructor = booking.instructor
    )

    bookings_collection.insert_one(
        booking_data.model_dump()
    )

    classes_collection.update_one(
        {
            "class_id": fitness_class["class_id"]
        },
        {
            "$inc": {
                "available_slots": -1
            }
        }
    )

    return {
        "message": "Booking Successful",
        "booking_id": next_booking_id,
        "class": fitness_class["name"],
        "instructor": fitness_class["instructor"],
        "remaining_slots": fitness_class["available_slots"] - 1
    }