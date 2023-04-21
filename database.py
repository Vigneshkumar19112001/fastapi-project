from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATBASE_URL = "postgresql://postgres:Yazhini@localhost/StudentTask"

engine = create_engine(
    SQLALCHEMY_DATBASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
