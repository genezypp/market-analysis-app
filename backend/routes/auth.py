from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db.database import get_db
from db.models import User
from utils.security import hash_password, verify_password, create_access_token

router = APIRouter()

class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
def register(data: UserRegister, db: Session = Depends(get_db)):
    """
    Rejestracja nowego użytkownika.
    """
    hashed_password = hash_password(data.password)
    new_user = User(username=data.username, email=data.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    """
    Logowanie użytkownika.
    """
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
