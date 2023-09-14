import settings

from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

from mailjet_rest import Client


class EmailSender:
    """
    Class to handle the email sending.
    """
    def __init__(self):
        self.connection = SMTP(settings.EMAIL_HOST)
        self.mailjet = Client(auth=(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD), version='v3.1')

    def send_email(self, email_body):
        self.connection.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
        message = MIMEText(email_body, 'html')
        message['Subject'] = 'Expired App Secrets'
        message['From'] = f'{settings.EMAIL_FROM_NAME} <{settings.EMAIL_FROM}>'
        message['To'] = settings.EMAIL_TO
        result = self.connection.sendmail(settings.EMAIL_FROM, settings.EMAIL_TO, message.as_string())
        self.connection.quit()
        return result

    def send_email_mailjet(self, email_body):
        data = {
            'Messages': [
                    {
                        "From": {
                            "Email": settings.EMAIL_FROM,
                            "Name": settings.EMAIL_FROM_NAME
                        },
                        "To": [
                            {
                                "Email": settings.EMAIL_TO,
                            }
                        ],
                        "Subject": "Your app secrets are about to expire!",
                        "TextPart": email_body,
                        "HTMLPart": email_body
                    }
                ]
        }
        result = self.mailjet.send.create(data=data)
        return result
