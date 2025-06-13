import requests
import allure

from Natalia.homework.natalia_aristova.test_api_naristova.endpoints.endpoint import Endpoint

class CreatePost(Endpoint):

    @allure.step('Created a new post')
    def new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        #self.response_json = self.response.json() # убрала отсюда джейсон, т.к. при коде 400 возвращается html
        return self.response
