import requests
import allure

from Natalia.homework.natalia_aristova.test_api_naristova.endpoints.endpoint import Endpoint

class GetOneObject(Endpoint):

    @allure.step('Get one object')
    def get_one_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/{object_id}', headers=headers)
        return self.response