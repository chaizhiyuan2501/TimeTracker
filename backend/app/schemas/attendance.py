from datetime import datetime
from pydantic import BaseModel


class AttendanceBase(BaseModel):
    name: str


class AttendanceCreate(AttendanceBase):
    check_in: datetime


class AttendanceOut(AttendanceBase):
    id: int
    check_in: datetime
    check_out: datetime | None = None

    class Config:
        orm_mode = True
