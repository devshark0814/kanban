from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@db:3306/kanban_db?charset=utf8mb4"

# サポートしているDBと対話するためのエンジン
ENGINE = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# DBに接続するためのセッション作成
# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# declarativeメタクラス
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
Base.query = session.query_property()