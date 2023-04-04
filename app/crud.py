from sqlalchemy.orm import Session

from db import models, schema


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
