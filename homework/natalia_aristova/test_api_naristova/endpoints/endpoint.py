import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    response_json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step(f'Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        response_json = self.response.json()
        assert response_json['name'] == name, 'Name is incorrect'

    @allure.step(f'Check that status code is 200')
    def check_status_code_is_correct(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step(f'Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, 'Status code is not correct'
