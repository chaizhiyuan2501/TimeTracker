from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = 'users'  # テーブル名を指定

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True,nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    is_admin = Column(Integer, default=0)  # 0:一般ユーザー, 1:管理者