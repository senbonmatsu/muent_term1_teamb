from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

# class Schedule(Base):
#     __tablename__ = "schedule"
    

    
