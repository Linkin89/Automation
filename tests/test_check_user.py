import requests
import pytest


def test_check_user(get_base_url, get_headers): 
    url = f"{get_base_url}/users/existense?email=driver-edit%40mailforspam.com"

    response = requests.get(url, headers=get_headers)

    assert response.json()['data']['exist'] == True, "Такого пользователя не существует"

    print(response.json())
