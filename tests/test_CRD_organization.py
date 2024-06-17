from apis.organizations.organization_api import OrganizationApi
import pytest
from pprint import pprint
import jsonschema
from allure import step


@step("Создание организации")
def test_create_organization(create_organization):
    """
    Создание новой организации
    """
    response = create_organization
    pprint(response.json())
    assert response.status_code == 200, "Организация не создана"
    print("куку")

@step("Получение организации")
def test_check_organization(create_organization):
    """
    Получение организации
    """

    response = create_organization
    status = response.json()['data']['status']
    pprint(response.json()["data"]["id"])
    assert status == "accepted", "Такой организации не существует"


@step("Удаление организации")
def test_delete_organization(create_organization, get_base_url_ELK, get_token):
    """
    Удаление организации
    """
        
    # Создание организации и получение её ID
    response = create_organization
    organization_id = response.json()["data"]["id"]

    # Удаление организации
    response = OrganizationApi(host=get_base_url_ELK, token=get_token)
    delete_org_response = response.delete_organization(organization_id)

    assert delete_org_response.status_code == 200, "Организация не удалена"
    assert delete_org_response.json()['errors'] is None , "Организация не удалена"

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
        jsonschema.validate(delete_org_response.json(), schema)
    except jsonschema.exceptions.ValidationError as elem:
        print(f"Ошибка валидации: {elem}")

    if __name__ == "__main__":
        pytest.main()
