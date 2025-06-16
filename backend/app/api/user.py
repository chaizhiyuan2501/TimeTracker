from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.curd.user import get_user_by_name, create_user, authenticate_user
from app.deps import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.post("/login")
def login(user:UserCreate,db:Session = Depends(get_db)):
    db_user = authenticate_user(db=db, name=user.name, password=user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful", "user": db_user}