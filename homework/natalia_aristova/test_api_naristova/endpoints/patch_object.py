import requests
import allure

from Natalia.homework.natalia_aristova.test_api_naristova.endpoints.endpoint import Endpoint

class PatchObject(Endpoint):

    @allure.step('Patch')
    def patch(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(f'{self.url}/{object_id}',
                                json=body,
                                headers=headers)
        self.json = self.response.json()
        return self.response
