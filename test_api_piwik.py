import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class BearerTokenCreator:
    def __init__(self):
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.base_url = os.getenv('BASE_URL')
        self.bearer = None

    def create_bearer(self):
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(
            f"{self.base_url}.piwik.pro/auth/token", headers={"Content-Type": "application/json"}, json=data)
        response_token = response.json()
        self.bearer = response_token['access_token']
        
def test_piwik_api():
    WEBSITE_ID = os.getenv('WEBSITE_ID')
    data = {
        "website_id":WEBSITE_ID,
        "columns": fields_request,
        "date_from": date_min,
        "date_to": date_max,
        "limit": 10000,
        "offset": offset,
        }

# Example usage
if __name__ == "__main__":
    token_creator = BearerTokenCreator()
    token_creator.create_bearer()
    