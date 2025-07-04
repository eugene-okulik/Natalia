from locust import task, HttpUser
import random


class MemeUser(HttpUser):

    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(3)
    def get_one_post(self):
        self.client.get(f'/object/{random.choice([1, 142, 143, 144, 145])}')

    @task(2)
    def post_and_delete_object(self):
        body = {
            "data": {"color": "white", "size": "big"},
            "name": "Second object"
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post('/object', json=body, headers=headers)
        post_id = response.json()['id']
        self.client.delete(f'http://167.172.172.115:52353/object/{post_id}')
