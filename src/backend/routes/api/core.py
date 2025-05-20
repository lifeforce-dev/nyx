from fastapi import APIRouter

from backend.routes.api.workout import router as workout_router
from backend.routes.api.stretches import router as stretches_router
from backend.routes.api.stats import router as stats_router

router = APIRouter(prefix="/api/v1")
router.include_router(workout_router)
router.include_router(stretches_router)
router.include_router(stats_router)