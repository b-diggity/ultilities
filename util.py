#!/usr/bin/python3
''' Helper Utilities to include in scripts '''

import smtplib
from email.mime.text import MIMEText
import os


# Function for sending emails via outlook
def email_now_outlook(message: str = None, subject: str = None):
    mail_user = os.getenv('MAIL_USER_OUTLOOK')
    mail_key = os.getenv('MAIL_PASS_OUTLOOK')
    mail_server = "smtp-mail.outlook.com"

    body = MIMEText(f'{message}\n\nNotification Autobot')

    body['Subject'] = subject
    body['From'] = mail_user
    body['To'] = mail_user

    # Send message
    server = smtplib.SMTP(mail_server, 587)
    server.ehlo()
    server.starttls()
    server.login(mail_user, mail_key)
    server.sendmail(mail_user, mail_user, body.as_string())
    server.quit()
    