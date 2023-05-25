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
    created_at: datetime = Field(datetime.now(), title="Creation Date")

    class Config:
        orm_mode = True

class MusicBase(BaseModel):
    #読み取り用、作成用
    music: str = Field(...,title="Music title")
    url : str = Field(...,title = "Music URL")

class Music_read(MusicBase):
    #読み取り用
    id: int = Field(0,title="Music ID")
    class Config:
        orm_mode = True
