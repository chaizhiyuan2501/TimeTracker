from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate


def create_attendance(db: Session, data: AttendanceCreate):
    record = Attendance(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_attendances(db: Session):
    return db.query(Attendance).all()
