import smtplib
from email.message import EmailMessage
from app.config import settings

def send_email(to: str, subject: str, content: str):
    if not settings.MAIL_HOST:
        return False

    msg = EmailMessage()
    msg["From"] = settings.MAIL_FROM
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(content)

    with smtplib.SMTP(settings.MAIL_HOST, settings.MAIL_PORT) as server:
        server.starttls()
        server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
        server.send_message(msg)

    return True
