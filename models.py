from sqlalchemy import String, Integer, Column
from database import Base

class StudentTable(Base):
    __tablename__ = "student_login"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    phone_number = Column(String, nullable=False)
    address = Column(String)
