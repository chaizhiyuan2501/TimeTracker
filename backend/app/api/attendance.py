from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.attendance import AttendanceCreate, AttendanceOut
from app.crud.attendance import create_attendance, get_attendances
from app.deps import get_db

router = APIRouter()


@router.post("/", response_model=AttendanceOut)
def create(data: AttendanceCreate, db: Session = Depends(get_db)):
    return create_attendance(db, data)


@router.get("/", response_model=list[AttendanceOut])
def read_all(db: Session = Depends(get_db)):
    return get_attendances(db)
