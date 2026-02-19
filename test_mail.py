import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
USER = os.environ.get("MY_EMAIL")
PASS = os.environ.get("TITAN_PASSWORD")
HOST = 'smtp.titan.email'
PORT = 465

msg = EmailMessage()
msg.set_content("Debug Test from Binjaz Script")
msg['Subject'] = "Protocol Test"
msg['From'] = USER
msg['To'] = USER

try:
    print(f"Attempting connection to {HOST} on {PORT}...")
    with smtplib.SMTP_SSL(HOST, PORT) as server:
        server.login(USER, PASS)
        server.send_message(msg)
    print("SUCCESS: Connection and Login worked perfectly.")
except Exception as e:
    print(f"FAILURE: {e}")