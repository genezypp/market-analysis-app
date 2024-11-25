import hashlib
import hmac
import base64
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Konfiguracja JWT
SECRET_KEY = "supersecretkey"  # Zmieñ na bezpieczny klucz w œrodowisku produkcyjnym
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Obs³uga haszowania hase³
SALT = "static_salt"  # Mo¿esz zmieniæ na dynamiczne generowanie soli dla ka¿dego u¿ytkownika


def hash_password(password: str) -> str:
    """
    Zwraca zahashowane has³o za pomoc¹ SHA-256.
    """
    salted_password = f"{SALT}{password}".encode()  # Dodanie soli do has³a
    hashed = hashlib.sha256(salted_password).hexdigest()
    return hashed


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Weryfikuje has³o u¿ytkownika, porównuj¹c jego hash z zapisanym.
    """
    return hash_password(plain_password) == hashed_password


def create_access_token(data: dict):
    """
    Tworzy token JWT na podstawie danych u¿ytkownika.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
