from apscheduler.schedulers.background import BackgroundScheduler
from services.notifications import check_notifications

scheduler = BackgroundScheduler()

def start_scheduler():
    """
    Uruchamia harmonogram powiadomieñ.
    """
    scheduler.add_job(check_notifications, "interval", minutes=10)  # Co 10 minut
    scheduler.start()
