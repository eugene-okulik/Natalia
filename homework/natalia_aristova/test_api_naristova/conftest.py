import pytest
import requests
from test_api_naristova.endpoints.create_object import CreatePost
from test_api_naristova.endpoints.update_post import UpdatePost
from test_api_naristova.endpoints.get_all_objects import GetAllObjects
from test_api_naristova.endpoints.get_one_object import GetOneObject
from test_api_naristova.endpoints.patch_object import PatchObject
from test_api_naristova.endpoints.delete_object import DeleteObject
from test_api_naristova.endpoints.endpoint import Endpoint


@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def patch_object():
    return PatchObject()


@pytest.fixture()
def get_all_objects():
    return GetAllObjects()


@pytest.fixture()
def get_one_object():
    return GetOneObject()


@pytest.fixture()
def delete_object():
    return DeleteObject()


@pytest.fixture()
def new_object():
    precondition_object = Endpoint()
    body = {
        "data": {"color": "white", "size": "big"},
        "name": "Second object"
    }
    response = requests.post(precondition_object.url, json=body, headers=precondition_object.headers)
    id_of_new_object = response.json()['id']
    yield id_of_new_object
    requests.delete(f'{precondition_object.url}/{id_of_new_object}')
