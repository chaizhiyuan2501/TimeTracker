from fastapi import APIRouter
from app.api import attendance

api_router = APIRouter()
api_router.include_router(attendance.router, prefix="/attendances", tags=["出勤記録"])
