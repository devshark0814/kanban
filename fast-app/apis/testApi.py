from fastapi import APIRouter

from database import session  # DBと接続するためのセッション
from models.test import TestTable  # 今回使うモデルをインポート

router = APIRouter()

@router.get("/get")
def getTest():
    users = session.query(TestTable).all();
    return users;