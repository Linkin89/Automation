from apis.organizations.organization_api import OrganizationApi
from pytest import fixture
from mimesis.builtins import RussiaSpecProvider
from mimesis import Person
ru_spec = RussiaSpecProvider()
fake = Person()


@fixture
def create_organization(get_base_url_ELK, get_token):
    """
    Create organization
    """
    organization = OrganizationApi(host=get_base_url_ELK, token=get_token)
    response = organization.create_organization()
    yield response