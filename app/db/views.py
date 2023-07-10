import calendar

from fastapi import Depends, HTTPException,status,Cookie,Response
from sqlalchemy.orm import Session
from typing import Optional
from db import schema,crud,models,database
from db.database import get_db
from db.models import User
from main import Users_type, app
from db.schema import *
import os




@app.get("/") #テスト
async def root():
    return {"message":"Hello World"}

@app.get("/items/{user_id}") # よくわからん(使わない)
def read_item(user_id:int,q:str=None):
    if q:
        return {"user_id":user_id,"q":q}
    return {"user_id":user_id}

@app.post("/items") # ユーザー情報が返ってくる、セキュリティガバ(使わない)
def update_item(user: Users_type):
    return {"user_name": user.name,"password": user.password}

@app.post("/set_cookie/")# set cookie
def save_cookie(response: Response,key: str, value: int):
    value = str(value)
    response.set_cookie(key, value)
    return "set cookie"

@app.get('/receive_cookie') # receive cookie
def get_cookie(sample_cookie: Optional[str] = Cookie(None)):
    return {
        "test": sample_cookie
    }

@app.post("/user/signup", response_model=schema.User, tags=['user']) # 新規ユーザー作成
def signup(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.read_user_by_name(db=db, user_name=user.name)
    # 既にユーザ名が存在する場合は400エラーを返す
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    new_user = crud.create_user(db=db, user=user)
    return new_user

@app.post("/user/delete",tags=['user']) # ユーザー削除
def delete(user_id:schema.User, db: Session=Depends(get_db)):
    user_id_del = crud.read_user_by_id(db,user_id.id)
    if user_id_del == None:
        return {"message":"ユーザーが存在していません"}
    else:
        crud.delete_user_by_id(db,user_id.id)
        return {"message":"ユーザーを削除しました"}
    

@app.post("/user/login",tags=['user']) # ログイン機能
def login(user_input_info:schema.UserCreate,db:Session=Depends(get_db)):
    user_info = crud.read_user_by_name(db,user_input_info.name)
    if user_info == None:
        return {"message":"ユーザーが存在していません"}
    elif user_input_info.name != user_info.name or user_input_info.password != user_info.password :
        return {"message":"ユーザーネームかパスワードが間違っています"}
    else:
        return {"id":user_info.id,"username":user_info.name}



@app.get("/calender",tags=["calender"])# 年と月を入力することで該当年月のカレンダーが返ってくる
def calender(year:int,month:int):
    calendar.setfirstweekday(calendar.SUNDAY)
    month_calender=calendar.monthcalendar(year,month)
    return month_calender

@app.get("/get_music",tags=["music"])# 音楽プレイリストの取得
def music(db:Session=Depends(get_db)):
    max,min = crud.get_music_ids(db)
    musics = crud.music_choice(db,min,max)
    return {"music_name":musics.music_name,"music_url":musics.url}

@app.post("/create_musics",tags=["music"])# 音楽をプレイリストに追加、音楽名とyoutubeのURLが必要
def create_music(create_m :schema.MusicBase,db:Session=Depends(get_db)):
    crud.music_create(db,create_m)
    return {"message":"楽曲を追加しました"}


