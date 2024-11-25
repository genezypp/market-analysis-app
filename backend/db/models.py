from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="user")  # Mo¿liwe role: user, admin


class SearchProfile(Base):
    __tablename__ = "search_profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    min_price = Column(Integer)
    max_price = Column(Integer)
    location = Column(String)
    condition = Column(String)  # Mo¿liwe wartoœci: "new", "used", "damaged"

    user = relationship("User")  # Powi¹zanie z tabel¹ u¿ytkowników


class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)
    condition = Column(String, nullable=False)  # Mo¿liwe wartoœci: "new", "used", "damaged"
    purchase_price = Column(Float, nullable=False)
    repair_cost = Column(Float, default=0)
    sale_price = Column(Float, nullable=True)
    margin = Column(Float, default=0)


class UserLog(Base):
    __tablename__ = "user_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String, nullable=False)
    min_price = Column(Integer, nullable=True)
    max_price = Column(Integer, nullable=True)
    alert_email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)  # Powiadomienie aktywne lub nieaktywne

    user = relationship("User")  # Powi¹zanie z tabel¹ u¿ytkowników
