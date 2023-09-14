from app_registrations import AppRegistrations
from email_sender import EmailSender
from tabulate import tabulate
from settings import Settings


def main():
    applications = AppRegistrations().get_applications()
    parsed_apps = AppRegistrations().parse_applications(applications)
    expired_app_secrets = AppRegistrations().get_expired_app_secrets(parsed_apps)

    if expired_app_secrets != []:
        table = tabulate(expired_app_secrets, headers='keys', tablefmt='html')
        print(table)

        if Settings().USE_MAILJET_LIB:
            mailjet_email = EmailSender().send_email_mailjet(table)
            print(mailjet_email.json())
        else:
            EmailSender().send_email(table)

    else:
        print('No expired app secrets found.')


if __name__ == '__main__':
    main()
