from apis.organizations.organization_api import OrganizationApi
import pytest
from pprint import pprint
import jsonschema
from allure import step

@step("Создание организации")
def test_create_organization(get_base_url_ELK, get_token):
    """
    Создание новой организации
    """
    organization = OrganizationApi(host=get_base_url_ELK, token=get_token)

    response = organization.create_organization()

    pprint(response.json()["data"]["id"])

    assert response.status_code == 200, "Организация не создана"


def check_organization(get_base_url_ELK, get_token):
    """
    Проверка существует ли организация
    """
    organization = OrganizationApi(host=get_base_url_ELK, token=get_token)

    response = organization.check_organization()


@step("Удаление организации")
def test_delete_organization(get_base_url_ELK, get_token):
    """
    Удаление новой организации
    """
    organization = OrganizationApi(host=get_base_url_ELK, token=get_token)
    
    # Создание организации
    organization_id = organization.create_organization().json()["data"]["id"]
    pprint(organization_id)

    # Удаление организации
    response = organization.delete_organization(organization_id)

    assert response.status_code == 200, "Организация удалена"
    assert response.json()['errors'] is None , "Организация удалена"

    # Валидация по схеме ответа об удалении 
    schema = {
        "type": "object",
        "properties": {
            "errors": {"type": "null"},
            "data": {"type": "array", "items": {"items": {}}},
            "requestId": {"type": "string"},
        },
        "required": ["errors", "data", "requestId"],
    }

    try:
        jsonschema.validate(response.json(), schema)
    except jsonschema.exceptions.ValidationError as elem:
        print(f"Ошибка валидации: {elem}")

    if __name__ == "__main__":
        pytest.main()
