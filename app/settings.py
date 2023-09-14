from os import environ


#################################################################
# GENERAL
#################################################################
EXPIRE_DAYS = int(environ.get('EXPIRE_DAYS', 30))

#################################################################
# AZURE ACCESS SPECIFIC
#################################################################
AZURE_CLIENT_ID = environ.get('AZURE_CLIENT_ID')
AZURE_CLIENT_SECRET = environ.get('AZURE_CLIENT_SECRET')
AZURE_TENANT_ID = environ.get('AZURE_TENANT_ID')

#################################################################
# EMAIL SPECIFIC
#################################################################
USE_MAILJET_LIB = bool(environ.get('USE_MAILJET_LIB', False))
EMAIL_HOST = environ.get('EMAIL_HOST')
EMAIL_FROM = environ.get('EMAIL_FROM')
EMAIL_FROM_NAME = environ.get('EMAIL_FROM_NAME')
EMAIL_TO = environ.get('EMAIL_TO')
EMAIL_USERNAME = environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = environ.get('EMAIL_PASSWORD')
