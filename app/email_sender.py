from settings import Settings

from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText

from mailjet_rest import Client


class EmailSender:
    """
    Class to handle the email sending.
    """
    def __init__(self):
        self.settings = Settings()
        self.email_host = self.settings.EMAIL_HOST
        self.email_from = self.settings.EMAIL_FROM
        self.email_from_name = self.settings.EMAIL_FROM_NAME
        self.email_to = self.settings.EMAIL_TO
        self.email_username = self.settings.EMAIL_USERNAME
        self.email_password = self.settings.EMAIL_PASSWORD
        self.connection = SMTP(self.email_host)
        self.mailjet = Client(auth=(self.email_username, self.email_password), version='v3.1')

    def send_email(self, email_body):
        self.connection.login(self.email_username, self.email_password)
        message = MIMEText(email_body, 'html')
        message['Subject'] = 'Expired App Secrets'
        message['From'] = f'{self.email_from_name} <{self.email_from}>'
        message['To'] = self.email_to
        result = self.connection.sendmail(self.email_from, self.email_to, message.as_string())
        self.connection.quit()
        return result

    def send_email_mailjet(self, email_body):
        data = {
            'Messages': [
                    {
                        "From": {
                            "Email": f"{self.email_from}",
                            "Name": f"{self.email_from_name}"
                        },
                        "To": [
                            {
                                "Email": f"{self.email_to}"
                            }
                        ],
                        "Subject": "Your app secrets are about to expire!",
                        "TextPart": f"{email_body}",
                        "HTMLPart": f"{email_body}"
                    }
                ]
        }
        result = self.mailjet.send.create(data=data)
        return result
