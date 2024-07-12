from celery import Celery
import smtplib
from email.mime.text import MIMEText

celery = Celery('tasks', broker='pyamqp://guest@localhost//')

@celery.task
def send_email(recipient, message):
    msg = MIMEText(message)
    msg['Subject'] = 'Your Subject Here'  # Add your subject here
    msg['From'] = 'your_email@example.com'  # Replace with your sender email
    msg['To'] = recipient

    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)

