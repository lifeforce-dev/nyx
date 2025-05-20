from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/workout", tags=["Workout"])

@router.post("/start")
def start_workout():
    # logic here
    return {"message": "Workout started!"}