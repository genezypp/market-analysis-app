from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from db.database import Base, engine
from routes import auth, search_profiles, analysis, notifications, devices, admin
from services.scheduler import start_scheduler
import os

# Inicjalizacja bazy danych
Base.metadata.create_all(bind=engine)

# Tworzenie aplikacji FastAPI
app = FastAPI(
    title="Market Analysis App",
    description="API for analyzing the secondary electronics market",
    version="1.0.0"
)

# Konfiguracja CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Dostosuj do adresu frontendu
    allow_credentials=True,
    allow_methods=["*"],  # Zezwalaj na wszystkie metody
    allow_headers=["*"],  # Zezwalaj na wszystkie nag³ówki
)

# Rejestracja tras (endpointów API)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(search_profiles.router, prefix="/profiles", tags=["Search Profiles"])
app.include_router(analysis.router, prefix="/analysis", tags=["Market Analysis"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
app.include_router(devices.router, prefix="/devices", tags=["Device Management"])
app.include_router(admin.router, prefix="/admin", tags=["Administration"])

# Serwowanie plików statycznych (np. index.html, style.css, JS)
static_dir = "frontend/build/static"
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")
else:
    print(f"Warning: Static directory '{static_dir}' not found. Static files may not be served.")

# Endpoint do zwracania pliku HTML (frontendu)
@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_file = "frontend/build/index.html"
    if os.path.exists(index_file):
        with open(index_file, "r") as f:
            return f.read()
    else:
        raise HTTPException(status_code=404, detail="Frontend index.html not found")

# Funkcje wywo³ywane przy starcie aplikacji
@app.on_event("startup")
def on_startup():
    # Uruchamianie zadañ w tle, np. powiadomieñ
    start_scheduler()

# Prosty endpoint testowy
@app.get("/api/test")
def root():
    return {"message": "Market Analysis App is running!"}
