# -*- coding: utf-8 -*-
# モデルの定義
import sys
sys.path.append('../')
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base
from database import ENGINE


# userテーブルのモデルUserTableを定義
class UserTable(Base):
    __tablename__ = 'users'
    id          = Column(Integer, primary_key=True, autoincrement=True)
    first_name  = Column(String(255))
    last_name   = Column(String(255))
    email       = Column(String(255))
    password    = Column(String(255))
    img_url     = Column(Text(100))
    created_pg  = Column(String(255))
    created_at  = Column(DateTime, default=datetime.now)
    updated_pg  = Column(String(255))
    updated_at  = Column(DateTime, default=datetime.now)
    deleted_pg  = Column(String(255))
    deleted_at  = Column(DateTime)
    __table_args__ = (
        UniqueConstraint('first_name', 'last_name', name='unique_name'),
    )

def main(args):
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)