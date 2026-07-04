from fastapi import FastAPI

# Import Routers
from fitness_studio.routers.signup import router as signup_router
from fitness_studio.routers.login import router as login_router
from fitness_studio.routers.change_passward import router as change_password_router
from fitness_studio.routers.create_class import router as create_class_router
from fitness_studio.routers.find_class import router as find_class_router
from fitness_studio.routers.create_booking import router as create_booking_router
from fitness_studio.routers.find_booking import router as find_booking_router
from fitness_studio.routers import refresh

app = FastAPI(
    title="Fitness Studio Booking API",
    version="1.0.0"
)
@app.get("/")
def home():
    return {
        "message": "Welcome to Fitness Studio Booking API"
    }

app.include_router(signup_router)
app.include_router(login_router)
app.include_router(change_password_router)
app.include_router(create_class_router)
app.include_router(find_class_router)
app.include_router(create_booking_router)
app.include_router(find_booking_router)
app.include_router(refresh.router)

