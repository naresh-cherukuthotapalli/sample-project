import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unicodedata
import os
from typing import Union, List
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

def clean_text(text: str) -> str:
    """Sanitize and normalize email content."""
    text = text.replace('\xa0', ' ')
    text = unicodedata.normalize("NFKD", text)
    return text.encode("utf-8", "ignore").decode("utf-8")

def send_email(
    to: Union[str, List[str]],
    subject: str,
    body: str,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587,
    username: str = "",
    password: str = ""
):
    try:
        # Get credentials from environment if not passed directly
        username = username or os.getenv("EMAIL_USER")
        password = password or os.getenv("EMAIL_PASS")

        if not username or not password:
            return {"status": "Failed", "error": "Missing email credentials."}

        # Normalize recipients to a list
       # Properly split comma-separated string into list of emails
        recipients = [email.strip() for email in to.split(",")] if isinstance(to, str) else to


        # Clean email body
        clean_body = clean_text(body)

        # Compose email
        msg = MIMEMultipart()
        msg["From"] = username
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.attach(MIMEText(clean_body, "plain", "utf-8"))

        # Send via SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(username, recipients, msg.as_string())

        return {"status": "Email sent successfully."}

    except Exception as e:
        return {"status": "Failed to send email", "error": str(e)}
