import smtplib
from email.mime.text import MIMEText
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Notification
from utils.olx_api import fetch_ads

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your-email@gmail.com"
SMTP_PASSWORD = "your-email-password"

def send_email(recipient, subject, body):
    """
    Wysyła e-mail z powiadomieniem.
    """
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = recipient

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, recipient, msg.as_string())

def check_notifications(db: Session = next(get_db())):
    """
    Sprawdza powiadomienia i wysyła alerty dla nowych ofert.
    """
    notifications = db.query(Notification).filter(Notification.is_active == True).all()

    for notification in notifications:
        ads = fetch_ads(notification.category, notification.min_price, notification.max_price)
        if ads:
            body = "\n".join([f"{ad['title']} - {ad['price']} PLN: {ad['url']}" for ad in ads])
            send_email(notification.alert_email, "New Deals Found!", body)
