import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATBASE_URL = "postgresql://student_z5u6_user:ZJ7RBq6WF9xmkXQUfD62dm8FWVHLTih3@dpg-chaa512k728r8861np4g-a.oregon-postgres.render.com/student_z5u6"
# postgresql://student_q1dk_user:gOHyHhquLRXh7tXHRmWKzvYNvAaGP6dg@dpg-ch8vh2bhp8u0vh8edr80-a.oregon-postgres.render.com/student_q1dk
# postgresql://student_hb4b_user:WxsteU0A3LBSiRNYEaCD2Vt5TbT94cxx@dpg-cha9i7m7avj5o485u160-a.oregon-postgres.render.com/student_hb4b
# postgresql://student_z5u6_user:ZJ7RBq6WF9xmkXQUfD62dm8FWVHLTih3@dpg-chaa512k728r8861np4g-a.oregon-postgres.render.com/student_z5u6
engine = create_engine(
    SQLALCHEMY_DATBASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
