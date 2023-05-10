import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATBASE_URL = "postgresql://student_z5u6_user:ZJ7RBq6WF9xmkXQUfD62dm8FWVHLTih3@dpg-chaa512k728r8861np4g-a.oregon-postgres.render.com/student_z5u6"
# postgresql://student_z5u6_user:ZJ7RBq6WF9xmkXQUfD62dm8FWVHLTih3@dpg-chaa512k728r8861np4g-a.oregon-postgres.render.com/student_z5u6
engine = create_engine(
    SQLALCHEMY_DATBASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
