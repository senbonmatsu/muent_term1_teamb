from sqlalchemy.orm import Session
from sqlalchemy import desc

from db import models, schema
import random


def create_user(db: Session, user: schema.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_users(db: Session, offset: int = 0, limit: int = 100):
    users = db.query(models.User).offset(offset).limit(limit).all()
    return users


def read_user_by_id(db: Session, user_id: int):
    # 指定idの読み取り
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


def read_user_by_name(db: Session, user_name: str):
    #指定したnameのUserを取得する
    user = db.query(models.User).filter(models.User.name == user_name).first()
    return user

def delete_user_by_id(db: Session, user_id: int):
    #指定したidのUserを削除
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return user_id

def get_music_ids(db: Session,):
    #音楽に登録してある中で一番大きいidを取得
    max = db.query(models.Music.id).order_by(desc(models.Music.id)).first()
    min = db.query(models.Music.id).first()
    max = max[0]
    min = min[0]
    return max,min

def music_choice(db: Session,min: int,max: int):
    #ランダムに選曲
    random_id = random.randint(min,max)
    music_chose = db.query(models.Music).filter(models.Music.id == random_id).one()
    return music_chose

def music_create(db: Session,music: schema.MusicBase):
    add_music = models.Music()
    add_music.music_name = music.music
    add_music.url = music.url
    db.add(add_music)
    db.commit()
    db.refresh(add_music)
    return add_music
