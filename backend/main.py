from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
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

# Serwowanie plików statycznych (np. index.html, style.css, JS)
app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

# Endpoint do zwracania pliku HTML (frontendu)
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("frontend/build/index.html", "r") as f:
        return f.read()

# Funkcje wywo³ywane przy starcie aplikacji
@app.on_event("startup")
def on_startup():
    # Uruchamianie zadañ w tle, np. powiadomieñ
    start_scheduler()

# Prosty endpoint testowy
@app.get("/api/test")
def root():
    return {"message": "Market Analysis App is running!"}
