from sqlalchemy.orm import Session

from db import models, schema
<<<<<<< HEAD:app/crud.py
=======
import random
>>>>>>> 3e2f51634b07cebd76ae0f1627df525628cab15d:app/db/crud.py


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

def create_schedule(db: Session, schedule: schema.ScheduleCreate, user_id: int):
    db_schedule = models.Schedule(**schedule.dict(), user_id=user_id)
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return  db_schedule

def read_schedules(db: Session, offset: int = 0, limit: int = 100):
    schedules = db.query(models.schedule).offset(offset).limit(limit).all()
    return schedules

def read_schedule_by_id(db: Session, schedule_id: int):
    schdule = db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()
    return schdule

def update_schedule(db: Session, schedule: schema.Schedule):
    db_schedule = db.query(models.Schedule).filter(models.Schedule.id == schedule.id).first()
    db_schedule.things = schedule.things
    db_schedule.label = schedule.label
    db_schedule.start_date = schedule.start_date
    db_schedule.finish_date = schedule.finish_date
    db.commit()
    return db_schedule

def delete_schedule_by_id(db: Session, schedule_id: int):
    #指定したidのUserを削除
    db.query(models.Schedule).filter(models.Schedule.id == schedule_id).delete()
    db.commit()
    return schedule_id

def create_todo(db: Session, todo: schema.TodoCreate, user_id: int):
    db_todo = models.Todo(**todo.dict(), user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return  db_todo

def read_todos(db: Session, offset: int = 0, limit: int = 100):
    todos = db.query(models.todo).offset(offset).limit(limit).all()
    return todos

def read_todo_by_id(db: Session, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return todo

def update_todo(db: Session, todo: schema.Todo):
    db_todo = db.query(models.Schedule).filter(models.Schedule.id == todo.id).first()
    db_todo.things = todo.things
    db_todo.label = todo.label
    db_todo.start_date = todo.start_date
    db_todo.finish_date = todo.finish_date
    db.commit()
    return db_todo

def delete_todo_by_id(db: Session, todo_id: int):
    #指定したidのUserを削除
    db.query(models.Todo).filter(models.User.id == todo_id).delete()
    db.commit()
<<<<<<< HEAD:app/crud.py
    return todo_id
=======
    return todo_id

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

>>>>>>> 3e2f51634b07cebd76ae0f1627df525628cab15d:app/db/crud.py
