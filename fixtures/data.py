from pytest import fixture


@fixture
def get_base_url_ELK():
    return "https://demo-passport.etpgpb.ru/api/v2"


@fixture
def get_headers(get_token):
    return {
        'accept': 'application/json',
        'Authorization' : get_token
    }