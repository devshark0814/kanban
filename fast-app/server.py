from sqlalchemy.sql.functions import user
from fastapi import FastAPI
from typing import List  # ネストされたBodyを定義するために必要
from starlette.middleware.cors import CORSMiddleware

from apis import testApi, sampleApi, userApi

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(testApi.router, prefix="/api/test", tags=["test"])
app.include_router(sampleApi.router, prefix="/api/sample", tags=["sample"])

app.include_router(userApi.router, prefix="/api/user", tags=["user"])