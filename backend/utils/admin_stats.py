from sqlalchemy.orm import Session
from db.models import User, SearchProfile, Device

def calculate_admin_stats(db: Session) -> dict:
    """
    Oblicza statystyki dla panelu administratora.
    """
    users_count = db.query(User).count()
    active_profiles = db.query(SearchProfile).count()
    devices_count = db.query(Device).count()

    return {
        "users_count": users_count,
        "active_profiles": active_profiles,
        "devices_count": devices_count
    }
