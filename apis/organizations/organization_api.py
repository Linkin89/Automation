import requests
from mimesis.builtins import RussiaSpecProvider
from mimesis import Person
ru_spec = RussiaSpecProvider()
fake = Person()



class OrganizationApi:
    fake_inn = ru_spec.inn()
    fake_ogrn = ru_spec.ogrn()
    fake_kpp = ru_spec.kpp()
    fake_email = fake.email()
    fake_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_patronymic = ru_spec.patronymic()
    fake_full_name = fake.full_name()

    print("ИНН: ", fake_inn)
    print("ОГРН: ", fake_ogrn)
    print("КПП: ", fake_kpp)
    print("email: ", fake_email)
    print("name: ", fake_name)
    print("fake_full_name: ", fake_full_name)
    print("fake_patronymic: ", fake_patronymic)

    def __init__(self, host, token):
        self.host = f'{host}/hub/organizations'
        self.token = token


    def create_organization(self):
        """
        Create new organization

        Returns:
            response: return data of new organization
        """
        
        headers = {
            'Authorization': self.token
            }
        
        fake_inn = ru_spec.inn()
        fake_ogrn = ru_spec.ogrn()
        fake_kpp = ru_spec.kpp()
        fake_email = fake.email()
        fake_name = fake.first_name()
        fake_full_name = fake.full_name()
        fake_patronymic = ru_spec.patronymic()
        
        json_data = {
        "law223fl": False,
        "requisites": {
            "residentRequisites": {
                "inn": fake_inn,
                "kpp": fake_kpp,
                "ogrn": fake_ogrn,
                "registrationDate": "2016-04-01T21:00:00+03:00"
            },
            "headRequisites": {
                "headLastName": "Новиков",
                "headFirstName": fake_name,
                "headMiddleName": fake_patronymic,
                "headJob": "Директор"
            }
        },
        "contacts": {
            "email": fake_email,
            "phone": "+78314179472",
            "person": fake_full_name
        },
        "bankAccounts": {
            "resident": {
                "bank": "Волго-Вятское ГУ Банка России//УФК по Нижегородской области г. Нижний Новгород",
                "account": "03214643000000013200",
                "accountKor": "40102810745370000024",
                "bik": "012202102"
            }
        },
        "addresses": {
            "legal": {
                "countryIso": "643",
                "city": "г. Нижний Новгород",
                "street": "ул.Ульянова",
                "house": "д.46",
                "index": "603950"
            },
            "postal": {
                "countryIso": "643",
                "city": "г. Нижний Новгород",
                "street": "ГСП-105",
                "house": "1",
                "index": "603950"
            }
        },
        "fullName": "Институт физики микроструктур РАН – филиал Федерального государственного бюджетного научного учреждения «Федеральный исследовательский центр Институт прикладной физики им. А.В. Гапонова-Грехова Российской академии наук»",
        "shortName": "ИФМ РАН",
        "participantType": "ul",
        "resident": True,
        "residentSng": False,
        "smallBizRegistry": False,
        "smallBizRegistryType": "0",
        "status": "accepted",
        "ownedBy": "elk-demo",
        "ecosystems": [
            "etpgpb"
        ],
        "classificatorCodes": [
            {
                "type": "okpd",
                "codes": [
                    {
                        "code": "72.19",
                        "value": "Научные исследования и разработки в области естественных и технических наук прочие"
                    },
                    {
                        "code": "62.01",
                        "value": "Разработка компьютерного программного обеспечения"
                    },
                    {
                        "code": "62.02",
                        "value": "Деятельность консультативная и работы в области компьютерных технологий"
                    },
                    {
                        "code": "85.23",
                        "value": "Подготовка кадров высшей квалификации"
                    }
                ]
            }
        ]
    }

        # Создание организации
        response = requests.post(f'{self.host}', headers=headers, json=json_data)

        return response


    def delete_organization(self, organization_id):
        """
        Delete organization
        """
        headers = {
            'Authorization': self.token
            }
        
        # Удалеине организации
        response = requests.delete(f'{self.host}?id={organization_id}', headers=headers)
        return response