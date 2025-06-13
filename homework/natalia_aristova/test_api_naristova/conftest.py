import pytest
from endpoints.create_object import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.get_all_objects import GetAllObjects
from endpoints.get_one_object import GetOneObject
from endpoints.patch_object import PatchObject
from endpoints.delete_object import DeleteObject

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