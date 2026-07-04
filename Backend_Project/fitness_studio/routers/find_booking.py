from fastapi import APIRouter, Depends, HTTPException
from fitness_studio.models.booking_model import BookingInDB
from fitness_studio.database.database import (bookings_collection, classes_collection)
from fitness_studio.security.utils import get_current_admin, get_current_user


router = APIRouter(prefix="/find_booking", tags=["Find Booking"])

@router.get("/{class_id}")
def get_booking_by_id(
    class_id: int,
    current_user=Depends(get_current_user)
):
    booking = bookings_collection.find_one(
        {"class_id": class_id},
        {"_id": 0}
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found."
        )

    return booking

@router.get("/")
def get_all_bookings(
    admin=Depends(get_current_admin)
):
    bookings = list(
        bookings_collection.find(
            {},
            {"_id": 0}
        )
    )

    if not bookings:
        raise HTTPException(
            status_code=404,
            detail=[]
        )

    return bookings