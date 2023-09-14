from app_registrations import AppRegistrations
from email_sender import EmailSender
from tabulate import tabulate
import settings


def main():
    app_registrations = AppRegistrations()
    applications = app_registrations.get_applications()
    parsed_apps = app_registrations.parse_applications(applications)
    expired_app_secrets = app_registrations.get_expired_app_secrets(parsed_apps)
    
    email_sender = EmailSender()

    if expired_app_secrets:
        table = tabulate(expired_app_secrets, headers='keys', tablefmt='html')
        print(table)

        if settings.USE_MAILJET_LIB:
            mailjet_email = email_sender.send_email_mailjet(table)
            print(mailjet_email.json())
        else:
            email_sender.send_email(table)

    else:
        print('No expired app secrets found.')


if __name__ == '__main__':
    main()
