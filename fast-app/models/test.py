# -*- coding: utf-8 -*-
# モデルの定義
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base
from database import ENGINE


# userテーブルのモデルUserTableを定義
class TestTable(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class Test(BaseModel):
    id: int
    name: str

def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()