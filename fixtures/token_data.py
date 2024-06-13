from pytest import fixture
import requests


@fixture
def url_get_token():
    return "https://id-test.etpgpb.ru/auth/realms/master/protocol/openid-connect/token"

@fixture
def auth_payload():
    return {
            'grant_type' : 'client_credentials',
            'client_id' : 'hub-admin-service',
            'client_secret' : 'a42f090b-cda5-4b2c-86ab-aa52c42fb061'
            }

@fixture
def auth_headers():
    return {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

@fixture
def get_token(url_get_token, auth_payload):
    response = requests.post(url_get_token, auth_payload)
    return f"Bearer {response.json()['access_token']}"