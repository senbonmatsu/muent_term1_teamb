from fastapi import FastAPI
from pydantic import BaseModel

from db import database, models


class Users_type(BaseModel):
    name: str
    password: str


app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

import views
