import requests
import allure

from Natalia.homework.natalia_aristova.test_api_naristova.endpoints.endpoint import Endpoint


class GetAllObjects(Endpoint):

    @allure.step('Get list of all objects')
    def get_list_of_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(self.url, headers=headers)
        return self.response
