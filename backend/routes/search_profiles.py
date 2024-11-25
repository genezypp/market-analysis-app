from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from db.database import get_db
from db.models import SearchProfile

router = APIRouter()

# Pydantic model do walidacji danych
class SearchProfileCreate(BaseModel):
    name: str
    category: str
    min_price: int = None
    max_price: int = None
    location: str = None
    condition: str = None

class SearchProfileResponse(SearchProfileCreate):
    id: int

    class Config:
        orm_mode = True

@router.get("/", response_model=List[SearchProfileResponse])
def list_profiles(user_id: int, db: Session = Depends(get_db)):
    """
    Zwraca listê profili wyszukiwania dla danego u¿ytkownika.
    """
    profiles = db.query(SearchProfile).filter(SearchProfile.user_id == user_id).all()
    return profiles

@router.post("/", response_model=SearchProfileResponse)
def create_profile(profile: SearchProfileCreate, user_id: int, db: Session = Depends(get_db)):
    """
    Tworzy nowy profil wyszukiwania dla u¿ytkownika.
    """
    new_profile = SearchProfile(user_id=user_id, **profile.dict())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@router.put("/{profile_id}", response_model=SearchProfileResponse)
def update_profile(profile_id: int, profile: SearchProfileCreate, db: Session = Depends(get_db)):
    """
    Aktualizuje istniej¹cy profil wyszukiwania.
    """
    db_profile = db.query(SearchProfile).filter(SearchProfile.id == profile_id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    for key, value in profile.dict(exclude_unset=True).items():
        setattr(db_profile, key, value)
    db.commit()
    db.refresh(db_profile)
    return db_profile

@router.delete("/{profile_id}")
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    """
    Usuwa profil wyszukiwania.
    """
    db_profile = db.query(SearchProfile).filter(SearchProfile.id == profile_id).first()
    if not db_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    db.delete(db_profile)
    db.commit()
    return {"message": "Profile deleted successfully"}
