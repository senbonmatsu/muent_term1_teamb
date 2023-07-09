from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from db import database, models


class Users_type(BaseModel):
    name: str
    password: str


app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

import db.views
