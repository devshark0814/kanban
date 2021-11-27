from pydantic import BaseModel

# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class UserCreate(BaseModel):
    first_name  : str
    last_name   : str
    email       : str
    img_url     : str


class UserSelect(BaseModel):
    id          : int
    first_name  : str
    last_name   : str
    email       : str
    img_url     : str
    created_pg  : str
    created_at  : str
    updated_pg  : str
    updated_at  : str
    deleted_pg  : str
    deleted_at  : str