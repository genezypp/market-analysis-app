import hashlib
import hmac
import base64
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Konfiguracja JWT
SECRET_KEY = "supersecretkey"  # Zmień na bezpieczny klucz w środowisku produkcyjnym
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Obsługa haszowania haseł
SALT = "static_salt"  # Możesz zmienić na dynamiczne generowanie soli dla każdego użytkownika


def hash_password(password: str) -> str:
    """
    Zwraca zahashowane hasło za pomocą SHA-256.
    """
    salted_password = f"{SALT}{password}".encode()  # Dodanie soli do hasła
    hashed = hashlib.sha256(salted_password).hexdigest()
    return hashed


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Weryfikuje hasło użytkownika, porównując jego hash z zapisanym.
    """
    return hash_password(plain_password) == hashed_password


def create_access_token(data: dict):
    """
    Tworzy token JWT na podstawie danych użytkownika.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
