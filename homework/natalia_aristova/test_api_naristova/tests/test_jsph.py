import pytest

from Natalia.homework.natalia_aristova.test_api_naristova.conftest import delete_object

TEST_DATA = [
    {"data": {"color": "white", "size": "big"}, "name": "Second object"},
    {"data": {"color": "red", "size": "medium"}, "name": "New object"},
    {"data": {"color": "green", "size": "small"}, "name": "Old object"},
    {"data": {"color": "white", "size": "big"}, "name": "7th object"}
]

NEGATIVE_DATA = [
    {"data": {"color": "green", "size": "small"}, "name": ["Old object"]},
    {"data": {"color": "white", "size": "big"}, "name": {"7th object": ''}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_new_object(create_post_endpoint, data, delete_object):
    create_post_endpoint.new_post(body=data)
    create_post_endpoint.check_status_code_is_correct()
    create_post_endpoint.check_response_name_is_correct(data['name'])
    id_of_created_object = create_post_endpoint.new_post(body=data).json()['id']
    delete_object.delete_object(id_of_created_object)


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(create_post_endpoint, data):
    create_post_endpoint.new_post(data)
    create_post_endpoint.check_bad_request()


def test_put(create_post_endpoint, update_post_endpoint, delete_object):
    body = {
        "data": {"color": "white", "size": "big"},
        "name": "test object"
    }
    id_of_created_object = create_post_endpoint.new_post(body=body).json()['id']
    body = {
        "data": {"color": "white", "size": "big"},
        "name": "test object"
    }
    update_post_endpoint.make_changes_in_object(id_of_created_object, body)
    update_post_endpoint.check_status_code_is_correct()
    update_post_endpoint.check_response_name_is_correct(body['name'])
    delete_object.delete_object(id_of_created_object)


def test_get_all_objects(get_all_objects):
    get_all_objects.get_list_of_objects()
    get_all_objects.check_status_code_is_correct()


def test_get_one_object(get_one_object):
    get_one_object.get_one_object(1)
    get_one_object.check_status_code_is_correct()


def test_patch(create_post_endpoint, patch_object, delete_object):
    body = {
        "data": {"color": "white", "size": "big"},
        "name": "test object"
    }
    id_of_created_object = create_post_endpoint.new_post(body=body).json()['id']
    body = {
        "name": "new object"
    }
    patch_object.patch(id_of_created_object, body)
    patch_object.check_response_name_is_correct(body['name'])
    patch_object.check_status_code_is_correct()
    delete_object.delete_object(id_of_created_object)


def test_delete(create_post_endpoint, delete_object):
    body = {
        "data": {"color": "white", "size": "big"},
        "name": "test object"
    }
    id_of_created_object = create_post_endpoint.new_post(body=body).json()['id']
    delete_object.delete_object(id_of_created_object)
    delete_object.check_status_code_is_correct()
