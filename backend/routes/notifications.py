from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from db.database import get_db
from db.models import Notification

router = APIRouter()

# Pydantic modele do walidacji danych
class NotificationCreate(BaseModel):
    category: str
    min_price: int = None
    max_price: int = None
    alert_email: str

class NotificationResponse(NotificationCreate):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

@router.get("/", response_model=List[NotificationResponse])
def list_notifications(user_id: int, db: Session = Depends(get_db)):
    """
    Zwraca listê aktywnych powiadomieñ dla u¿ytkownika.
    """
    return db.query(Notification).filter(Notification.user_id == user_id).all()

@router.post("/", response_model=NotificationResponse)
def create_notification(notification: NotificationCreate, user_id: int, db: Session = Depends(get_db)):
    """
    Tworzy nowe powiadomienie.
    """
    new_notification = Notification(user_id=user_id, **notification.dict())
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification

@router.put("/{notification_id}")
def update_notification(notification_id: int, notification: NotificationCreate, db: Session = Depends(get_db)):
    """
    Aktualizuje powiadomienie.
    """
    db_notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    for key, value in notification.dict(exclude_unset=True).items():
        setattr(db_notification, key, value)

    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.delete("/{notification_id}")
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    """
    Usuwa powiadomienie.
    """
    db_notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not db_notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(db_notification)
    db.commit()
    return {"message": "Notification deleted successfully"}
