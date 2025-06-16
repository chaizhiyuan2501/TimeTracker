from sqlalchemy import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from passlib.hash import bcrypt

def get_user_by_name(db: Session, name: str):
    """
    ユーザー名でユーザーを取得
    """
    return db.query(User).filter(User.name == name).first()

def create_user(db: Session, user: UserCreate):
    hashed_pw = bcrypt.hash(user.password)
    db_user = User(name=user.name, password=hashed_pw, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, name: str, password: str):
    """
    ユーザー名とパスワードでユーザーを認証
    """
    user = get_user_by_name(db, name)
    if not user:
        return None
    if not bcrypt.verify(password, user.password):
        return None
    return user