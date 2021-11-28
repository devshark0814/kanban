from pydantic import BaseModel, Field
from datetime import datetime

# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class UserCreate(BaseModel):
    first_name  : str = Field(..., title="姓")
    last_name   : str = Field(..., title="名")
    email       : str = Field(..., title="メールアドレス")
    password    : str = Field(..., title="パスワード")
    img_url     : str = Field(None, title="アイコンパス")


class UserSelect(BaseModel):
    id          : int           = Field("", title="ユーザーID")
    first_name  : str           = Field(None, title="姓")
    last_name   : str           = Field(None, title="名")
    email       : str           = Field(None, title="メールアドレス")
    password    : str           = Field(None, title="パスワード")
    img_url     : str           = Field(None, title="イメージパス")
    created_pg  : str           = Field(None, title="作成プログラム")
    created_at  : datetime      = Field(None, title="作成日時")
    updated_pg  : str           = Field(None, title="更新プログラム")
    updated_at  : datetime      = Field(None, title="更新日時")
    deleted_pg  : str           = Field(None, title="削除プログラム")
    deleted_at  : datetime      = Field(None, title="削除日時")
    class Config:
        orm_mode = True

class UserDelete(BaseModel):
    id          : int