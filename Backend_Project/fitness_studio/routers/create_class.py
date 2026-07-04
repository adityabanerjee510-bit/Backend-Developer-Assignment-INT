from fastapi import APIRouter, Depends
from fitness_studio.models.classes_model import (FitnessClassCreate,FitnessClassInDB,FitnessClassResponse)
from fitness_studio.database.database import classes_collection
from fitness_studio.security.utils import get_current_admin

router = APIRouter(prefix="/classes",tags=["Classes"])

@router.post("/", response_model=FitnessClassResponse)
def create_class(
    fitness_class: FitnessClassCreate,
    admin=Depends(get_current_admin)
):
    last_class = classes_collection.find_one(sort=[("class_id", -1)])

    next_id = last_class["class_id"] + 1 if last_class else 1

    class_data = FitnessClassInDB(
        class_id=next_id,
        name=fitness_class.name,
        date_time=fitness_class.date_time,
        instructor=fitness_class.instructor,
        total_slots=fitness_class.total_slots,
        available_slots=fitness_class.total_slots
    )

    classes_collection.insert_one(class_data.model_dump())

    return class_data