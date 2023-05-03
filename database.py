import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATBASE_URL = os.environ.get("DATABASE_URL")
# postgres://student_q1dk_user:gOHyHhquLRXh7tXHRmWKzvYNvAaGP6dg@dpg-ch8vh2bhp8u0vh8edr80-a.oregon-postgres.render.com/student_q1dk

engine = create_engine(
    SQLALCHEMY_DATBASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
