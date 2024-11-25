from fastapi import FastAPI
from db.database import Base, engine
from routes import auth, search_profiles, analysis, notifications, devices, admin
from services.scheduler import start_scheduler




# Inicjalizacja bazy danych
Base.metadata.create_all(bind=engine)

# Tworzenie aplikacji FastAPI
app = FastAPI(
    title="Market Analysis App",
    description="API for analyzing the secondary electronics market",
    version="1.0.0"
)

# Rejestracja tras (endpointów API)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(search_profiles.router, prefix="/profiles", tags=["Search Profiles"])
app.include_router(analysis.router, prefix="/analysis", tags=["Market Analysis"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
app.include_router(devices.router, prefix="/devices", tags=["Device Management"])
app.include_router(admin.router, prefix="/admin", tags=["Administration"])


# Funkcje wywo³ywane przy starcie aplikacji
@app.on_event("startup")
def on_startup():
    # Uruchamianie zadañ w tle, np. powiadomieñ
    start_scheduler()

# Prosty endpoint testowy
@app.get("/")
def root():
    return {"message": "Market Analysis App is running!"}
