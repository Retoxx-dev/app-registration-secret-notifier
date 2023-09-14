from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

from settings import Settings

from datetime import datetime


class AppRegistrations:
    """
    Class to handle the Azure AD App Registrations.
    """
    def __init__(self):
        self.settings = Settings()
        self.credential = DefaultAzureCredential()
        self.graph_client = GraphClient(credential=self.credential)

    def is_expired(self, end_date_time):
        # end_date_time can contain a dot or not, so we need to check for both cases
        if "." in end_date_time:
            end_date_time = datetime.strptime(end_date_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            end_date_time = datetime.strptime(end_date_time, "%Y-%m-%dT%H:%M:%S%fZ")
        return self.settings.EXPIRE_DAYS >= (end_date_time - datetime.now()).days

    def get_applications(self):
        applications = self.graph_client.get('/applications?$select=id,displayName,passwordCredentials')
        applications.raise_for_status()
        return applications.json()

    def parse_applications(self, applications):
        parsed_applications = []
        for application in applications['value']:
            parsed_applications.append({
                'id': application['id'],
                'displayName': application['displayName'],
                'passwordCredentials': application['passwordCredentials']
            })
        return parsed_applications

    def get_expired_app_secrets(self, applications):
        expired_app_secrets = []
        for application in applications:
            for secret in application['passwordCredentials']:
                if self.is_expired(secret['endDateTime']):
                    parsed_date = datetime.strptime(secret['endDateTime'],
                                                    "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d %B, %Y at %H:%M:%S")
                    expired_app_secrets.append({
                        'applicationId': application['id'],
                        'applicationName': application['displayName'],
                        'secretName': secret['displayName'],
                        'secretEndDateTime': parsed_date,
                        'secretHint': secret['hint']
                    })
        return expired_app_secrets
