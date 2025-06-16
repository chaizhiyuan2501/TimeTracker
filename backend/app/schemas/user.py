from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr  # メールアドレス（必須）
    name: str  # ユーザー名（必須）
    password: Optional[EmailStr] = None  # パスワード（任意）※型がEmailStrになっていますが、通常はstrです

class UserOut(BaseModel):
    id: int  # ユーザーID
    name: str  # ユーザー名
    email: Optional[str] = None  # メールアドレス（任意）
    is_admin: int  # 管理者フラグ

    class Config:
        orm_mode = True  # ORMモード有効化（ORMオブジェクトからデータを取得可能にする）
