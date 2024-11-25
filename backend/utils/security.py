from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Konfiguracja JWT
SECRET_KEY = "supersecretkey"  # Zmieñ na bezpieczny klucz w œrodowisku produkcyjnym
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Obs³uga haszowania hase³
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Zwraca zahashowane has³o.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Weryfikuje has³o u¿ytkownika z hashem.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    """
    Tworzy token JWT na podstawie danych u¿ytkownika.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
