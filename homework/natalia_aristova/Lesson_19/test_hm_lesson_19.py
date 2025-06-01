import requests
import pytest


@pytest.fixture()
def new_object():
    body = {
        "data": {"color": "white", "size": "big"},
        "name": "Second object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    id_of_new_object = response.json()['id']
    yield id_of_new_object
    requests.delete(f'http://167.172.172.115:52353/object/{id_of_new_object}')


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def text_for_every_test():
    print('before test')
    yield
    print('after test')


@pytest.mark.critical
def test_get_all_objects(hello, text_for_every_test):
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'


def test_get_one_object(text_for_every_test, new_object):
    response = requests.get(f'http://167.172.172.115:52353/object/{new_object}')
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.medium
@pytest.mark.parametrize('body', [{"data": {"color": "red", "size": "medium"}, "name": "New object"},
                                  {"data": {"color": "green", "size": "small"}, "name": "Old object"},
                                  {"data": {"color": "white", "size": "big"}, "name": "7th object"}])
def test_post_a_new_object(text_for_every_test, body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    assert response.status_code == 200, 'Status code is incorrect'


def test_put(text_for_every_test, new_object):
    body = {
        "data": {"color": "white", "size": "big"},
        "name": "test object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://167.172.172.115:52353/object/{new_object}',
                            json=body,
                            headers=headers)
    assert response.json()['name'] == 'test object'
    assert response.status_code == 200, 'Status code is incorrect'


def test_patch(text_for_every_test, new_object):
    body = {
        "name": "new object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://167.172.172.115:52353/object/{new_object}',
                              json=body,
                              headers=headers)
    assert response.json()['name'] == 'new object'
    assert response.status_code == 200, 'Status code is incorrect'


def test_delete(text_for_every_test, new_object):
    response = requests.delete(f'http://167.172.172.115:52353/object/{new_object}')
    assert response.status_code == 200, 'Status code is incorrect'
