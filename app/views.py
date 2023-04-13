from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from db import schema
from db.database import get_db
from db.models import User
from main import Users_type, app


@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/items/{user_id}")
def read_item(user_id:int,q:str=None):
    if q:
        return {"user_id":user_id,"q":q}
    return {"user_id":user_id}

@app.post("/items")
def update_item(user: Users_type):
    return {"user_name": user.name,"password": user.password}


@app.post("/user/signup", response_model=schema.User, tags=['user'])
def signup(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.read_user_by_name(db=db, user_name=user.name)
    # 既にユーザ名が存在する場合は400エラーを返す
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    new_user = crud.create_user(db=db, user=user)
    return new_user

@app.post("/user/delete",tags=['user'])
def delete(user_id:schema.User, db: Session=Depends(get_db)):
    user_id_del = crud.read_user_by_id(db,user_id.id)
    if user_id_del == None:
        return {"message":"ユーザーが存在していません"}
    else:
        crud.delete_user_by_id(db,user_id.id)
        return {"message":"ユーザーを削除しました"}
    
