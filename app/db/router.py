from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db import crud
from db import schemas
from db.database import get_db

router = APIRouter()


@router.get("/users", response_model=list[schemas.User], tags=['user'])
def read_users(offset: int = 0,
               limit: int = 100,
               db: Session = Depends(get_db)):
    """
    複数のUserを取得する

    Parameters
    ----------
    offset : int, default 0
        取得するユーザIDの始点
    limit : int, default 100
        取得するユーザIDの数
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    users : list of models.User
        {offset}番目から{limit}個分のUserモデルのリスト
    """

    users = crud.read_users(db=db, offset=offset, limit=limit)
    return users


@router.get("/user/{user_id}", response_model=schemas.User, tags=['user'])
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    指定したidのUserを取得する

    Parameters
    ----------
    user_id : int
        ユーザID
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    user : models.User
        ユーザIDが一致するUserモデル
    """

    user = crud.read_user_by_id(db=db, user_id=user_id)
    return user


@router.post("/user/signup", response_model=schemas.User, tags=['user'])
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Userを作成する

    Parameters
    ----------
    user : schemas.UserCreate
        ユーザ名とパスワードを含んだデータ
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    new_user : models.User
        Userモデル
    """

    db_user = crud.read_user_by_name(db=db, user_name=user.name)
    # 既にユーザ名が存在する場合は400エラーを返す
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    new_user = crud.create_user(db=db, user=user)
    return new_user


@router.post("/user/signin", response_model=schemas.User, tags=['user'])
def signin(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    アカウント認証を行う

    Parameters
    ----------
    user : schemas.UserCreate
        ユーザ名とパスワードを含んだデータ
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    user : models.User
        Userモデル
    """

    db_user = crud.read_user_by_name(db=db, user_name=user.name)
    # パスワードが一致しない場合は401エラーを返す
    if user.password != db_user.password:
        raise HTTPException(
            status_code=401, detail="Password is incorrect")

    return db_user


@router.post("/schedule", response_model=schemas.Schedule, tags=['schedule'])
def create_schedule(schedule: schemas.ScheduleCreate, user_id: int, db: Session = Depends(get_db)):
    """
    Userを作成する

    Parameters
    ----------
    user : schemas.UserCreate
        ユーザ名とパスワードを含んだデータ
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    new_user : models.User
        Userモデル
    """

    new_schedule = crud.create_schedule(db=db, schedule=schedule, user_id=user_id)
    return new_schedule

@router.put("/schedule/update", response_model=schemas.Schedule, tags=['schedule'])
def update_schedule(schedule: schemas.Schedule, db: Session = Depends(get_db)):
    """
    Noteを更新する

    Parameters
    ----------
    note : schemas.Note
        Noteモデル
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    new_note : models.Note
        Noteモデル
    """

    db_schedule = crud.read_schedule_by_id(db=db, schedule_id=schedule.id)
    # ノートが存在しない場合は400エラーを返す
    if not db_schedule:
        raise HTTPException(
            status_code=400, detail="Schedule does not exist")

    new_schedule = crud.update_schedule(db=db, schedule=schedule)
    return new_schedule


@router.delete("/schedule/delete", response_model=schemas.Schedule, tags=['schedule'])
def delete_schedule(schedule: schemas.Schedule, db: Session = Depends(get_db)):
    """
    Noteを削除する

    Parameters
    ----------
    note_id : int
        ノートのID
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    delete_note : models.Note
        空のNoteモデル
    """

    db_schedule = crud.read_schedule_by_id(db=db, schedule_id=schedule.id)
    # ノートが存在しない場合は400エラーを返す
    if not db_schedule:
        raise HTTPException(
            status_code=400, detail="Schedule does not exist")

    delete_schedule = crud.delete_schedule_by_id(db=db, schedule_id=schedule.id)
    return delete_schedule



@router.post("/todo", response_model=schemas.Todo, tags=['todo'])
def create_todo(todo: schemas.TodoCreate, user_id: int, db: Session = Depends(get_db)):
    """
    Userを作成する

    Parameters
    ----------
    user : schemas.UserCreate
        ユーザ名とパスワードを含んだデータ
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    new_user : models.User
        Userモデル
    """

    new_todo = crud.create_todo(db=db, todo=todo, user_id=user_id)
    return new_todo

@router.put("/todo/update", response_model=schemas.Todo, tags=['todo'])
def update_todo(todo: schemas.Todo, db: Session = Depends(get_db)):
    """
    Noteを更新する

    Parameters
    ----------
    note : schemas.Note
        Noteモデル
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    new_note : models.Note
        Noteモデル
    """

    db_todo = crud.read_todo_by_id(db=db, todo_id=todo.id)
    # ノートが存在しない場合は400エラーを返す
    if not db_todo:
        raise HTTPException(
            status_code=400, detail="Todo does not exist")

    new_todo = crud.update_todo(db=db, todo=todo)
    return new_todo


@router.delete("/todo/delete", response_model=schemas.Todo, tags=['todo'])
def delete_note(todo: schemas.Todo, db: Session = Depends(get_db)):
    """
    Noteを削除する

    Parameters
    ----------
    note_id : int
        ノートのID
    db : Session
        データベースとの接続を行うための情報

    Returns
    -------
    delete_note : models.Note
        空のNoteモデル
    """

    db_todo = crud.read_todo_by_id(db=db, todo_id=todo.id)
    # ノートが存在しない場合は400エラーを返す
    if not db_todo:
        raise HTTPException(
            status_code=400, detail="Todo does not exist")

    delete_todo = crud.delete_todo_by_id(db=db, todo=todo)
    return delete_todo