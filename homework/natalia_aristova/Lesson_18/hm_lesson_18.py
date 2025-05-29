import requests


def get_all_posts():
    response = requests.get('http://167.172.172.115:52353/object')
    assert len(response.json()['data']) == 1, 'Not all posts returned'  # сбил с толку ключ 'data') len был всегда 1.
    assert response.status_code == 200, 'Status code is incorrect'

def new_post():                                           # прекондишн
    body = {
        "data": {"color":"white","size":"big"},
        "name": "Second object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    return response.json()['id']

def clear(post_id):                                       # посткондишн
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')

def get_one_post():
    post_id = new_post()
    response = requests.get(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.json()['id'] == post_id, 'Wrong post returned'
    assert response.status_code == 200, 'Status code is incorrect'
    clear(post_id)

def post_a_new_post():
    body = {
        "data": {"color": "yellow", "size": "medium"},
        "name": "Second object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == 2, 'Id is incorrect'
    clear(response.json()['id'])

def put():
    post_id = new_post()
    body = {
        "data": {"color":"white","size":"big"},
        "name": "test object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://167.172.172.115:52353/object/{post_id}',
                            json=body,
                            headers=headers)
    assert response.json()['name'] == 'test object'
    assert response.status_code == 200, 'Status code is incorrect'
    clear(post_id)

def patch():
    post_id = new_post()
    body = {
        "name": "new object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://167.172.172.115:52353/object/{post_id}',
                              json=body,
                              headers=headers)
    assert response.json()['name'] == 'new object'
    assert response.status_code == 200, 'Status code is incorrect'
    clear(post_id)

def delete():
    post_id = new_post()
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200, 'Status code is incorrect'

get_all_posts()
get_one_post()
post_a_new_post()
put()
patch()
delete()
