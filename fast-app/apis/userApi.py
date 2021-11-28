import sys
sys.path.append('../')
from fastapi import APIRouter
from typing import List

from database import session  # DBと接続するためのセッション
from models.user import UserTable  # 今回使うモデルをインポート

from schemas.user import UserCreate, UserSelect, UserDelete

router = APIRouter()

@router.get("/user", response_model=List[UserSelect])
def getAll():
    try:
        users = session.query(UserTable).all()
    except ValueError as e:
        print(e.json())
    return users

@router.post("/user")
def create(user: UserCreate):
    userObj = UserTable(
        first_name = user.first_name,
        last_name  = user.last_name,
        email      = user.email,
        password   = user.password,
        img_url    = user.img_url,
    )
    session.add(userObj)
    session.commit()
    return {"message": "登録完了しました"}

@router.delete("/delete/{id}")
def delete(id):
    try:
        data = session.query(UserTable).filter(UserTable.id == id).one()
        session.delete(data)
        session.commit()
    except Exception as e:
        return {"message": "★★★削除失敗しました★★★"}
    return {"message": "削除完了しました"}
