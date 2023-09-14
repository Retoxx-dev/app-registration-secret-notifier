# app-registration-secret-notifier

This is a simple CRON function that will send an email to a specified email address when a secret of Azure Active Directory App Registration is about to expire.

## Prerequisites
In order for this script to work, you need to have SMTP credentials to send the email and an Azure Active Directory App Registration with the `Application.Read.All` permission to read the secrets of the App Registration.

## How to use
Copy and rename `.env.dist` to `.env` and fill in the required values.

Available environment variables are:
- `AZURE_CLIENT_ID` - is the client ID of the Azure Active Directory App Registration used to authenticate to Azure AD.
- `AZURE_CLIENT_SECRET` - is the client secret of the Azure Active Directory App Registration used to authenticate to Azure AD.
- `AZURE_TENANT_ID` - is the tenant ID of the Azure Active Directory App Registration used to authenticate to Azure AD.
- `USE_MAILJET_LIB` - is a boolean value that indicates whether to use the Mailjet library or not. If set to `false`, the function will use the python SMTP library.
- `EMAIL_HOST` - is the SMTP host to use to send the email.
- `EMAIL_FROM` - is the email address to use as the sender of the email.
- `EMAIL_FROM_NAME` - is the name to use as the sender of the email.
- `EMAIL_TO` - is the email address to send the email to.
- `EMAIL_USERNAME` - is the username to use to authenticate to the SMTP server.
- `EMAIL_PASSWORD` - is the password to use to authenticate to the SMTP server.
- `EXPIRE_DAYS` - is an integer value that indicates how many days before the secret expires the email should be sent. Default value is `30`.

To run locally, use `docker-compose up`
