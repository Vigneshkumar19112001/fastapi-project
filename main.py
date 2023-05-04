from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine, SessionLocal
from pydantic import BaseModel, validator, Field, EmailStr
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import timedelta, datetime, date
from starlette import status
import re


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "nothing"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def hash_passord(pwd):
    return bcrypt_context.hash(pwd)

def check_password(password, pwd):
    return bcrypt_context.verify(password, pwd)

def authenticate_user(username: str, pwd: str, db):
    user = db.query(models.StudentTable).filter(models.StudentTable.username == username).first()
    if not user:
        return False
    if not check_password(pwd, user.password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user")
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user")

class StudentLogin(BaseModel):
    username : str = Field(...,min_length=4)
    password : str = Field(...,min_length=8)
    email : EmailStr
    first_name : str
    last_name : str
    phonenumber : str
    address : str
    gender : str
    dob : date

    @validator('username')
    def username_validation(cls, v):
        assert v.isalnum(), 'must be an alphanumeric'
        return v
    
    @validator('gender')
    def gender_validation(cls, value):
        if value not in ('male', 'female', 'others'):
            raise ValueError("gender must be male, female or others")
        return value
    
    @validator('password')
    def password_validator(cls, value):
        assert value.isalnum(), 'must be an alphanumeric'
        return value
    
class Token(BaseModel):
    access_token: str
    token_type: str

class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str

class Login(BaseModel):
    username: str
    password: str


@app.post("/register")
async def register_student(student : StudentLogin, db: Session = Depends(get_db)):
    new_student = models.StudentTable()

    new_student.username = student.username
    new_student.password = hash_passord(student.password)
    new_student.email = student.email
    new_student.first_name = student.first_name
    new_student.last_name = student.last_name
    new_student.phone_number = student.phonenumber
    new_student.address = student.address
    new_student.gender = student.gender
    new_student.dob = student.dob

    check_user = db.query(models.StudentTable).filter(models.StudentTable.username == student.username).first()

    if check_user:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, detail="User Already Existed")
    else:
        db.add(new_student)
        db.commit()
    return "successfull post"


@app.get("/student_list")
async def list_of_students(db:Session=Depends(get_db)):
    return db.query(models.StudentTable).all()


@app.post("/token", response_model=Token)
async def login_for_access_token(response: Response, login: Login, db:Session=Depends(get_db)):
    user = authenticate_user(login.username, login.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user")
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    response.set_cookie(key="access_token", value=token, httponly=True)
    return {'access_token': token, 'token_type': 'bearer'}


@app.get("/logout")
async def logout(response: Response):
    response.delete_cookie(key='access_token')
    return "Logout Successfull"


@app.put("/edit_password")
async def edit_password(request: Request, user_verification: UserVerification, user: dict = Depends(get_current_user), db: Session=Depends(get_db)):
    if user is None:
        return "user not found"
    student_model = db.query(models.StudentTable).filter(models.StudentTable.id == user.get('id')).first()

    if student_model is not None:
        if user_verification.username == student_model.username and check_password(
                user_verification.password,student_model.password):
            student_model.password = hash_passord(user_verification.new_password)
            db.add(student_model)
            db.commit()
            return 'Successful'
    return 'Invalid user or request'
