from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from db.database import get_db
from db.models import User, UserLog
from utils.admin_stats import calculate_admin_stats

router = APIRouter()

# Pydantic modele do walidacji danych
class UserUpdate(BaseModel):
    username: str = None
    email: str = None
    is_active: bool = None
    role: str = None

@router.get("/users", response_model=List[dict])
def list_users(db: Session = Depends(get_db)):
    """
    Zwraca listê u¿ytkowników.
    """
    users = db.query(User).all()
    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "is_active": user.is_active,
        }
        for user in users
    ]

@router.put("/users/{user_id}")
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    """
    Aktualizuje dane u¿ytkownika.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    return {"message": "User updated successfully"}

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Usuwa u¿ytkownika.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@router.get("/logs")
def get_user_logs(db: Session = Depends(get_db)):
    """
    Zwraca logi dzia³añ u¿ytkowników.
    """
    logs = db.query(UserLog).all()
    return [
        {
            "user_id": log.user_id,
            "action": log.action,
            "timestamp": log.timestamp,
        }
        for log in logs
    ]

@router.get("/stats")
def get_admin_stats(db: Session = Depends(get_db)):
    """
    Zwraca statystyki dla panelu administratora.
    """
    return calculate_admin_stats(db)
