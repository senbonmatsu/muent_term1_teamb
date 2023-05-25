from datetime import datetime

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    #作成・読み取り用
    name: str = Field(..., title="User Name")#バリデーション。説明


class UserCreate(UserBase):
    #作成用
    password: str = Field(..., title="Password")


class User(UserBase):
    #読み取り用
    id: int = Field(0, title="User ID")

    class Config:
        orm_mode = True

class  ScheduleBase(BaseModel):
    things : str = Field(..., title="Things")
    label: str = Field(..., title="Label")
    start_date : datetime = Field(..., title="StartDate")
    finish_date : datetime = Field(..., title="FinishDate")


class ScheduleCreate(ScheduleBase):
    pass


class Schedule(ScheduleBase):
    user_id: int = Field(0, title="User ID")
    id: int = Field(0, title="Schdule ID")
    created_at: datetime = Field(datetime.now(), title="CreateDate")

    class Config:
        orm_mode = True


class  TodoBase(BaseModel):
    things : str = Field(..., title="Things")
    label: str = Field(..., title="Label")
    check: int = Field(..., title="Check")
    date : datetime = Field(..., title="Date")


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    user_id: int = Field(0, title="User ID")
    id: int = Field(0, title="Schdule ID")
    

    class Config:
        orm_mode = True
        