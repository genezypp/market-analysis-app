from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from db.database import get_db
from db.models import Device
from utils.reports import generate_csv_report, generate_pdf_report

-

router = APIRouter()

# Pydantic modele do walidacji danych
class DeviceCreate(BaseModel):
    model: str
    condition: str
    purchase_price: float
    repair_cost: float = 0
    sale_price: float = None

class DeviceResponse(DeviceCreate):
    id: int
    margin: float

    class Config:
        orm_mode = True

@router.get("/", response_model=List[DeviceResponse])
def list_devices(db: Session = Depends(get_db)):
    """
    Zwraca listê urz¹dzeñ.
    """
    return db.query(Device).all()

@router.post("/", response_model=DeviceResponse)
def add_device(device: DeviceCreate, db: Session = Depends(get_db)):
    """
    Dodaje nowe urz¹dzenie do bazy.
    """
    margin = 0
    if device.sale_price:
        margin = device.sale_price - device.purchase_price - device.repair_cost
    new_device = Device(**device.dict(), margin=margin)
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device

@router.put("/{device_id}", response_model=DeviceResponse)
def update_device(device_id: int, device: DeviceCreate, db: Session = Depends(get_db)):
    """
    Aktualizuje istniej¹ce urz¹dzenie.
    """
    db_device = db.query(Device).filter(Device.id == device_id).first()
    if not db_device:
        raise HTTPException(status_code=404, detail="Device not found")
    for key, value in device.dict(exclude_unset=True).items():
        setattr(db_device, key, value)
    if db_device.sale_price:
        db_device.margin = db_device.sale_price - db_device.purchase_price - db_device.repair_cost
    db.commit()
    db.refresh(db_device)
    return db_device

@router.delete("/{device_id}")
def delete_device(device_id: int, db: Session = Depends(get_db)):
    """
    Usuwa urz¹dzenie z bazy.
    """
    db_device = db.query(Device).filter(Device.id == device_id).first()
    if not db_device:
        raise HTTPException(status_code=404, detail="Device not found")
    db.delete(db_device)
    db.commit()
    return {"message": "Device deleted successfully"}

@router.get("/reports/csv")
def download_csv_report(db: Session = Depends(get_db)):
    """
    Generuje i zwraca raport CSV.
    """
    devices = db.query(Device).all()
    generate_csv_report(devices)
    return {"message": "CSV report generated"}

@router.get("/reports/pdf")
def download_pdf_report(db: Session = Depends(get_db)):
    """
    Generuje i zwraca raport PDF.
    """
    devices = db.query(Device).all()
    generate_pdf_report(devices)
    return {"message": "PDF report generated"}
