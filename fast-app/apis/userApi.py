import sys
sys.path.append('../')
from fastapi import APIRouter
from typing import List

from database import session  # DBと接続するためのセッション
from models.user import UserTable  # 今回使うモデルをインポート

from schemas.user import UserCreate, UserSelect

router = APIRouter()

@router.get("/getAll", response_model=List[UserSelect])
def getAll():
    users = session.query(UserTable).all();
    return users;

@router.post("/create")
def create(user: UserCreate):
    userObj = UserTable(
        first_name = user.first_name,
        last_name  = user.last_name,
        email      = user.email,
        img_url    = user.img_url,
    )
    session.add(userObj)
    session.commit()
    return {"message": "登録完了しました"}

