from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, ForeignKey

from db.database import Base

from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    created_at = Column(DateTime,default = datetime.now(), nullable=False)

    

class schedule(Base):
    # id : Column(Integer)
    # name : Column(String)
    # password : Column(String)
    # created_at : Column(DateTime)
    # things : Column(String)
    # user_id : Column(Integer)
    # label : Column(String)
    # start_date : Column(DateTime)
    # finish_date : Column(DateTime)


    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    things = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    label = Column(String)
    start_date = Column(DateTime)
    finish_date = Column(DateTime)

    notes = relationship("Note", back_populates="owner")


class Note(Base):

    # id : Column(Integer)
    # title : Column(String)
    # content : Column(String)
    # created_at : Column(DateTime)
    # owner_id : Column(Integer)
    # things : Column(String)
    # user_id : Column(Integer)
    # label : Column(String)
    # start_date : Column(DateTime)
    # finish_date : Column(DateTime)

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    things = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    label = Column(String)
    start_date = Column(DateTime)
    finish_date = Column(DateTime)

    owner = relationship("shedule", back_populates="notes")
    

