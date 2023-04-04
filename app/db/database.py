import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#.envで読み込みを行う
load_dotenv()
USERNAME = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
HOSTNAME = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
DBNAME = os.environ.get("POSTGRES_DB")
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}"

#SQlite版
#DATABASE_URL = f"sqlite:////{Path(__file__).parent}/db.sqlite"

print(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
