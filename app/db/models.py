from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String,Text

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    created_at = Column(DateTime,default = datetime.now(), nullable=False)

class Music(Base):
    __tablename__ = "musics"
    id = Column(Integer, primary_key=True )
    music_name = Column(String, nullable=False)
    url = Column(Text,nullable = False)

    
