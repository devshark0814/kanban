from sqlalchemy.sql.functions import user
from fastapi import FastAPI
from typing import List  # ネストされたBodyを定義するために必要
from starlette.middleware.cors import CORSMiddleware

from database import session  # DBと接続するためのセッション
from models.test import TestTable  # 今回使うモデルをインポート

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/api/hello")
def index():
    return {"message": "Hello World"}

@app.get("/api/test/get")
def getTest():
    users = session.query(TestTable).all();
    return users;